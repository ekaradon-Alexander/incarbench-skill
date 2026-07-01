#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from incar_generation_utils import (
    DEFAULT_OUTPUT_ROOT,
    dump_json,
    ensure_output_root,
    missing_generation_grade,
    score_generated_incar,
    summarize_generation_grades,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score one model/skill variant across all INCAR-generation benchmark cases."
    )
    parser.add_argument(
        "--benchmark-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Benchmark root directory",
    )
    parser.add_argument(
        "--model-name",
        required=True,
        help="Model-variant label to score, or `all` to score every discovered model/skill output.",
    )
    return parser.parse_args()


def case_dirs_under(benchmark_root: Path) -> list[Path]:
    return sorted(
        path for path in (benchmark_root / "cases").iterdir() if path.is_dir()
    )


def variant_label(model_name: str, skill_name: str) -> str:
    return f"{model_name}-{skill_name}"


def discovered_model_variants(benchmark_root: Path) -> dict[str, tuple[str, str]]:
    variants: dict[str, tuple[str, str]] = {}
    case_dirs = case_dirs_under(benchmark_root)
    for case_dir in case_dirs:
        model_outputs_dir = case_dir / "model_outputs"
        if not model_outputs_dir.is_dir():
            continue
        for model_dir in model_outputs_dir.iterdir():
            if not model_dir.is_dir():
                continue
            for skill_variant_dir in model_dir.iterdir():
                if not skill_variant_dir.is_dir():
                    continue
                label = variant_label(model_dir.name, skill_variant_dir.name)
                variants[label] = (model_dir.name, skill_variant_dir.name)
    return dict(sorted(variants.items()))


def resolve_requested_variant(
    benchmark_root: Path,
    requested_label: str,
) -> tuple[str, str, str]:
    discovered = discovered_model_variants(benchmark_root)
    if requested_label in discovered:
        model_name, skill_name = discovered[requested_label]
        return requested_label, model_name, skill_name

    no_skill_label = variant_label(requested_label, "no-skill")
    if no_skill_label in discovered:
        model_name, skill_name = discovered[no_skill_label]
        return no_skill_label, model_name, skill_name

    raise SystemExit(
        f"No discovered generation output matches '{requested_label}'. Expected one of: {', '.join(discovered) or '(none)'}"
    )


def score_one_model_variant(*, benchmark_root: Path, model_label: str) -> None:
    resolved_label, model_name, skill_name = resolve_requested_variant(
        benchmark_root,
        model_label,
    )
    case_dirs = case_dirs_under(benchmark_root)
    grades: list[dict] = []

    for case_dir in case_dirs:
        variant_dir = case_dir / "model_outputs" / model_name / skill_name
        candidate_path = variant_dir / "INCAR_final"
        grade_path = variant_dir / "grade.json"
        grade_path.parent.mkdir(parents=True, exist_ok=True)

        if candidate_path.exists():
            payload = score_generated_incar(
                case_dir=case_dir,
                candidate_path=candidate_path,
                model_name=resolved_label,
            )
        else:
            payload = missing_generation_grade(
                case_dir=case_dir,
                model_name=resolved_label,
                candidate_path=candidate_path,
            )

        dump_json(grade_path, payload)
        grades.append(payload)

    summary = summarize_generation_grades(
        benchmark_root=benchmark_root,
        model_name=resolved_label,
        grades=grades,
    )
    dump_json(
        benchmark_root / "leaderboards" / f"{resolved_label}_summary.json",
        summary,
    )
    print(f"Scored {resolved_label}", flush=True)


def main() -> None:
    args = parse_args()
    benchmark_root = ensure_output_root(args.benchmark_root)

    if args.model_name == "all":
        discovered = discovered_model_variants(benchmark_root)
        if not discovered:
            raise SystemExit(f"No model outputs found under {benchmark_root / 'cases'}")
        print(
            f"Scoring all discovered model variants: {', '.join(discovered)}",
            flush=True,
        )
        for model_label in discovered:
            score_one_model_variant(
                benchmark_root=benchmark_root,
                model_label=model_label,
            )
        return

    score_one_model_variant(benchmark_root=benchmark_root, model_label=args.model_name)


if __name__ == "__main__":
    main()
