#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from dotenv import load_dotenv
import traceback
from pathlib import Path

from rich.console import Console, Group
from rich.live import Live
from rich.progress import (
    BarColumn,
    Progress,
    TaskID,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.status import Status

from benchmark_utils import dump_json, utc_now
from incar_generation_utils import (
    DEFAULT_SKILL_ROOT,
    DEFAULT_OUTPUT_ROOT,
    configured_skill_names,
    enabled_models,
    ensure_output_root,
    ensure_skill_root,
    extract_incar_from_response,
    invoke_model_with_retries,
    prompt_messages_for_case,
    resolve_skill_paths,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run enabled LLMs over all INCAR-generation benchmark cases."
    )
    parser.add_argument(
        "--benchmark-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Benchmark root directory",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/llm_benchmark_config.json"),
        help="LLM benchmark config path",
    )
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=DEFAULT_SKILL_ROOT,
        help="Directory containing downloaded skills",
    )
    parser.add_argument(
        "--model-name",
        action="append",
        dest="model_names",
        help="Only run the named model. Repeat for multiple models.",
    )
    parser.add_argument(
        "--case-id",
        action="append",
        dest="case_ids",
        help="Only run the named case. Repeat for multiple cases.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing INCAR_final outputs",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned runs without calling models",
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Delete selected cases' model_outputs directories after an explicit confirmation prompt, then exit.",
    )
    return parser.parse_args()


DELETE_CONFIRMATION_TEXT = "Delete all the model output"
console = Console()


def selected_case_dirs(benchmark_root: Path, case_ids: list[str] | None) -> list[Path]:
    case_dirs = sorted(
        path for path in (benchmark_root / "cases").iterdir() if path.is_dir()
    )
    if case_ids:
        requested = set(case_ids)
        case_dirs = [case_dir for case_dir in case_dirs if case_dir.name in requested]
    return case_dirs


def remove_model_outputs(case_dirs: list[Path]) -> None:
    console.print(
        "This will delete each selected case's model_outputs directory.",
    )
    console.print(
        f"Type exactly: {DELETE_CONFIRMATION_TEXT}",
    )
    confirmed = input("> ").strip()
    if confirmed != DELETE_CONFIRMATION_TEXT:
        raise SystemExit("Deletion cancelled: confirmation text did not match.")

    removed = 0
    missing = 0
    for case_dir in case_dirs:
        model_outputs_dir = case_dir / "model_outputs"
        if not model_outputs_dir.exists():
            missing += 1
            console.print(f"Skip missing {model_outputs_dir}")
            continue
        shutil.rmtree(model_outputs_dir)
        removed += 1
        console.print(f"Deleted {model_outputs_dir}")

    console.print(
        f"Removal completed: deleted {removed} model_outputs directorie(s), skipped {missing} missing directorie(s).",
    )


def build_progress(case_count: int) -> Progress:
    return Progress(
        TextColumn("[bold cyan]{task.fields[label]}"),
        BarColumn(),
        TaskProgressColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TextColumn(
            "ok={task.fields[successes]} fail={task.fields[failures]} skip={task.fields[skips]}"
        ),
        TimeElapsedColumn(),
        console=console,
        transient=False,
        expand=True,
    )


def update_task_counts(
    progress: Progress,
    task_id: TaskID,
    *,
    advance: int = 0,
    successes: int = 0,
    failures: int = 0,
    skips: int = 0,
) -> None:
    task = progress.tasks[task_id]
    progress.update(
        task_id,
        advance=advance,
        successes=task.fields["successes"] + successes,
        failures=task.fields["failures"] + failures,
        skips=task.fields["skips"] + skips,
    )


def main() -> None:
    args = parse_args()
    benchmark_root = ensure_output_root(args.benchmark_root)
    case_dirs = selected_case_dirs(benchmark_root, args.case_ids)

    if args.remove:
        remove_model_outputs(case_dirs)
        return

    skill_root = ensure_skill_root(args.skill_dir)
    models = enabled_models(args.config, args.model_names)
    if not models:
        raise SystemExit("No enabled models selected in llm_benchmark_config.json")

    configured_skills = configured_skill_names(args.config)
    skill_paths = resolve_skill_paths(
        skill_dir=skill_root,
        skill_names=configured_skills,
    )
    run_variants: list[tuple[str, list[Path] | None]] = [("no-skill", None)]
    run_variants.extend(
        (skill_name, [skill_path]) for skill_name, skill_path in skill_paths.items()
    )

    load_dotenv()

    console.print(
        f"Starting batch run: {len(models)} model(s), {len(run_variants)} variant(s), {len(case_dirs)} case(s), "
        f"benchmark_root={benchmark_root}",
    )

    progress = build_progress(len(case_dirs))
    status = Status("Waiting to start generation...", console=console)
    task_ids: dict[tuple[str, str], TaskID] = {}
    model_totals: dict[str, dict[str, int]] = {}

    for model_cfg in models:
        model_name = model_cfg["name"]
        model_totals[model_name] = {"successes": 0, "failures": 0}
        for skill_name, _ in run_variants:
            label = f"{model_name}/{skill_name}"
            task_ids[(model_name, skill_name)] = progress.add_task(
                label,
                total=len(case_dirs),
                label=label,
                successes=0,
                failures=0,
                skips=0,
            )

    with Live(
        Group(progress, status),
        console=console,
        refresh_per_second=10,
        transient=False,
    ) as live:
        for model_cfg in models:
            model_name = model_cfg["name"]
            for skill_name, active_skill_paths in run_variants:
                task_id = task_ids[(model_name, skill_name)]
                for case_dir in case_dirs:
                    output_dir = case_dir / "model_outputs" / model_name / skill_name
                    incar_path = output_dir / "INCAR_final"
                    error_path = output_dir / "error.json"

                    if incar_path.exists() and not args.overwrite:
                        status.update(
                            f"Skipping existing case: {model_name}/{skill_name} -> {case_dir.name}"
                        )
                        update_task_counts(progress, task_id, advance=1, skips=1)
                        continue

                    if args.dry_run:
                        status.update(
                            f"Dry run: {model_name}/{skill_name} -> {case_dir.name}"
                        )
                        update_task_counts(progress, task_id, advance=1, skips=1)
                        continue

                    output_dir.mkdir(parents=True, exist_ok=True)
                    response_path = output_dir / "response.json"
                    request_path = output_dir / "request.json"

                    messages = prompt_messages_for_case(case_dir)
                    dump_json(
                        request_path,
                        {
                            "generated_at_utc": utc_now(),
                            "model_name": model_name,
                            "skill_name": skill_name,
                            "skill_paths": [
                                str(path) for path in (active_skill_paths or [])
                            ],
                            "messages": messages,
                        },
                    )

                    status.update(
                        f"Generating case: {model_name}/{skill_name} -> {case_dir.name}"
                    )
                    try:
                        if model_cfg["access_method"] == "mock_copy_reference":
                            text = (case_dir / "inputs" / "INCAR_reference").read_text(
                                encoding="utf-8"
                            )
                            raw = {
                                "mock": True,
                                "skills": [
                                    str(path) for path in (active_skill_paths or [])
                                ],
                            }
                        else:
                            text, raw = invoke_model_with_retries(
                                model_cfg=model_cfg,
                                messages=messages,
                                skill_paths=active_skill_paths,
                            )

                        incar_text = extract_incar_from_response(text)
                        incar_path.write_text(incar_text, encoding="utf-8")
                        dump_json(
                            response_path,
                            {
                                "generated_at_utc": utc_now(),
                                "model_name": model_name,
                                "skill_name": skill_name,
                                "raw_response": raw,
                                "extracted_text": incar_text,
                            },
                        )
                        if error_path.exists():
                            error_path.unlink()
                        model_totals[model_name]["successes"] += 1
                        update_task_counts(progress, task_id, advance=1, successes=1)
                    except Exception as exc:
                        model_totals[model_name]["failures"] += 1
                        dump_json(
                            error_path,
                            {
                                "generated_at_utc": utc_now(),
                                "model_name": model_name,
                                "skill_name": skill_name,
                                "case_id": case_dir.name,
                                "error_type": type(exc).__name__,
                                "error_message": str(exc),
                                "traceback": traceback.format_exc(),
                            },
                        )
                        update_task_counts(progress, task_id, advance=1, failures=1)
                        console.print(
                            f"Failed {model_name}/{skill_name} {case_dir.name}: {exc}"
                        )

            totals = model_totals[model_name]
            console.print(
                f"Completed model {model_name}: {totals['successes']} succeeded, {totals['failures']} failed"
            )

        live.update(
            Group(progress, "[bold green]Status: Batch run completed.[/bold green]")
        )


if __name__ == "__main__":
    main()
