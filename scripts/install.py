from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def available_skills() -> dict[str, Path]:
    return {
        folder.name: folder
        for folder in sorted(SKILLS.iterdir())
        if folder.is_dir() and (folder / "SKILL.md").is_file()
    }


def destination(args: argparse.Namespace) -> Path:
    if args.destination:
        return args.destination.expanduser().resolve()
    if args.host == "custom":
        raise SystemExit("--host custom requires --destination PATH")
    if args.scope == "project":
        if not args.project:
            raise SystemExit("--scope project requires --project PATH")
        base = args.project.expanduser().resolve()
        folder = ".agents" if args.host == "codex" else ".claude"
        return base / folder / "skills"
    folder = ".agents" if args.host == "codex" else ".claude"
    return Path.home() / folder / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install all skills or selected skills without third-party dependencies."
    )
    parser.add_argument(
        "--host",
        choices=("codex", "claude-code", "custom"),
        default="codex",
        help="Host that loads the skills; default: codex.",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="Install for every project or one project; default: user.",
    )
    parser.add_argument("--project", type=Path, help="Project root for project scope.")
    parser.add_argument(
        "--destination",
        type=Path,
        help="Override the destination skill directory for another compatible host.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="selected",
        help="Install one named skill. Repeat to install several. Default: all.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Merge into and overwrite files in an existing skill directory.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show actions without copying.")
    parser.add_argument("--list", action="store_true", help="List available skills and exit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    available = available_skills()

    if args.list:
        print("\n".join(available))
        return 0

    selected = list(dict.fromkeys(args.selected or available))
    unknown = sorted(set(selected) - set(available))
    if unknown:
        raise SystemExit(f"Unknown skill: {', '.join(unknown)}")

    target_root = destination(args)
    conflicts = [name for name in selected if (target_root / name).exists()]
    if conflicts and not args.force:
        names = ", ".join(conflicts)
        raise SystemExit(f"Already installed: {names}. Re-run with --force to update.")

    for name in selected:
        source = available[name]
        target = target_root / name
        print(f"{'Would install' if args.dry_run else 'Installing'} {name} -> {target}")
        if not args.dry_run:
            target_root.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target, dirs_exist_ok=args.force)

    if not args.dry_run:
        print(f"Installed {len(selected)} skill(s). Restart the host if they do not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
