#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from benchmark_utils import load_json

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_SKILLS_CONFIG = REPO_ROOT / "config" / "skills.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download skills defined in config/skills.json."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_SKILLS_CONFIG,
        help="Skills config JSON path",
    )
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path("skills"),
        help="Directory used to store downloaded skills",
    )
    return parser.parse_args()


def ensure_skill_dir(path: Path) -> Path:
    resolved = path if path.is_absolute() else REPO_ROOT / path
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def load_skills_config(path: Path) -> list[dict]:
    payload = load_json(path)
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: config must be a JSON object")

    skills = payload.get("skills")
    if not isinstance(skills, list):
        raise ValueError(f"{path}: skills must be a list")

    return skills


def clone_github_repo(repo_url: str, branch: str, destination: Path) -> None:
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--branch",
            branch,
            repo_url,
            str(destination),
        ],
        check=True,
    )


def copy_skill_source(source_path: Path, destination_path: Path) -> None:
    if destination_path.exists():
        if destination_path.is_dir():
            shutil.rmtree(destination_path)
        else:
            destination_path.unlink()

    if source_path.is_dir():
        shutil.copytree(source_path, destination_path)
        return

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)


def download_github_skill(skill: dict, skill_root: Path) -> None:
    name = str(skill.get("name") or "").strip()
    repo_url = str(skill.get("github_repo") or "").strip()
    branch = str(skill.get("github_branch") or "").strip()
    github_path = str(skill.get("github_path") or "").strip()
    if not name:
        raise ValueError("skill.name is required")
    if not repo_url:
        raise ValueError(f"skill {name}: github_repo is required")
    if not branch:
        raise ValueError(f"skill {name}: github_branch is required")
    if not github_path:
        raise ValueError(f"skill {name}: github_path is required")

    destination_path = skill_root / name
    with tempfile.TemporaryDirectory(prefix="incarbench-skill-") as tmp_dir:
        clone_root = Path(tmp_dir) / "repo"
        clone_github_repo(repo_url, branch, clone_root)

        source_path = clone_root / github_path
        if not source_path.exists():
            raise FileNotFoundError(
                f"skill {name}: path not found in cloned repo: {github_path}"
            )

        copy_skill_source(source_path, destination_path)


def download_skill(skill: dict, skill_root: Path) -> None:
    if not isinstance(skill, dict):
        raise ValueError("each skill entry must be an object")

    source_type = str(skill.get("source_type") or "").strip().lower()
    if source_type == "github":
        download_github_skill(skill, skill_root)
        return

    raise ValueError(f"unsupported source_type: {skill.get('source_type')}")


def main() -> None:
    args = parse_args()
    skill_root = ensure_skill_dir(args.skill_dir)
    skills = load_skills_config(args.config)

    print(f"Downloading {len(skills)} skill(s) into {skill_root}", flush=True)
    for skill in skills:
        name = skill.get("name", "<unknown>")
        print(f"Downloading skill {name}", flush=True)
        download_skill(skill, skill_root)
    print("Skill download completed.", flush=True)


if __name__ == "__main__":
    main()
