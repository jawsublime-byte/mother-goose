from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_REPO = "jawsublime-byte/mother-goose"
USER_AGENT = "mother-goose-skill-updater/1.0"


def request(url: str) -> Request:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return Request(url, headers=headers)


def get_json(url: str):
    with urlopen(request(url), timeout=30) as response:
        return json.load(response)


def get_bytes(url: str) -> bytes:
    with urlopen(request(url), timeout=30) as response:
        return response.read()


def api_contents(repo: str, path: str, ref: str):
    encoded_path = quote(path, safe="/")
    encoded_ref = quote(ref, safe="")
    url = f"https://api.github.com/repos/{repo}/contents/{encoded_path}?ref={encoded_ref}"
    return get_json(url)


def remote_skill_names(repo: str, ref: str) -> list[str]:
    entries = api_contents(repo, "skills", ref)
    return sorted(entry["name"] for entry in entries if entry.get("type") == "dir")


def remote_skill_files(repo: str, skill: str, ref: str) -> list[tuple[str, str]]:
    root = f"skills/{skill}"
    pending = [root]
    files: list[tuple[str, str]] = []
    while pending:
        current = pending.pop()
        entries = api_contents(repo, current, ref)
        if not isinstance(entries, list):
            raise RuntimeError(f"Expected directory listing for {current}")
        for entry in entries:
            entry_type = entry.get("type")
            if entry_type == "dir":
                pending.append(entry["path"])
            elif entry_type == "file":
                download_url = entry.get("download_url")
                if not download_url:
                    raise RuntimeError(f"No download URL for {entry['path']}")
                relative = entry["path"][len(root) + 1 :]
                files.append((relative, download_url))
    return sorted(files)


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


def installed_skill_names(target_root: Path) -> set[str]:
    if not target_root.exists():
        return set()
    return {
        folder.name
        for folder in target_root.iterdir()
        if folder.is_dir() and (folder / "SKILL.md").is_file()
    }


def stage_skill(repo: str, skill: str, ref: str, staging_root: Path) -> Path:
    staged = staging_root / skill
    for relative, url in remote_skill_files(repo, skill, ref):
        target = staged / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(get_bytes(url))
    if not (staged / "SKILL.md").is_file():
        raise RuntimeError(f"Remote skill {skill} has no SKILL.md")
    return staged


def install_skill(
    repo: str,
    skill: str,
    ref: str,
    target_root: Path,
    *,
    overwrite: bool,
) -> None:
    target = target_root / skill
    if target.exists() and not overwrite:
        raise RuntimeError(f"{skill} is already installed")

    target_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skill-update-") as temp:
        staged = stage_skill(repo, skill, ref, Path(temp))
        if target.exists():
            shutil.copytree(staged, target, dirs_exist_ok=True)
        else:
            shutil.copytree(staged, target)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check a public skill repository and install only missing skills, or refresh "
            "specific installed skills, without redownloading the full collection."
        )
    )
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"GitHub owner/repo; default: {DEFAULT_REPO}.")
    parser.add_argument("--ref", default="main", help="Git branch or tag; default: main.")
    parser.add_argument(
        "--host",
        choices=("codex", "claude-code", "custom"),
        default="codex",
        help="Installed skill host; default: codex.",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="User-wide or one-project installation; default: user.",
    )
    parser.add_argument("--project", type=Path, help="Project root for project scope.")
    parser.add_argument("--destination", type=Path, help="Explicit skill directory for a custom host.")
    parser.add_argument(
        "--install-new",
        action="store_true",
        help="Install every remote skill that is missing locally. Existing skill folders are untouched.",
    )
    parser.add_argument(
        "--refresh",
        action="append",
        default=[],
        metavar="SKILL",
        help="Refresh one named installed skill from GitHub. Repeat for several skills.",
    )
    parser.add_argument(
        "--no-refresh-router",
        action="store_true",
        help="Do not refresh the repository router after installing new add-ons.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_root = destination(args)
    remote = remote_skill_names(args.repo, args.ref)
    installed = installed_skill_names(target_root)
    missing = [name for name in remote if name not in installed]

    print(f"Repository: {args.repo}@{args.ref}")
    print(f"Destination: {target_root}")
    print(f"Remote skills: {len(remote)}")
    print(f"Installed from any source: {len(installed)}")
    print("Missing from this collection: " + (", ".join(missing) if missing else "none"))

    if not args.install_new and not args.refresh:
        print("Check only. Use --install-new to add missing skills or --refresh NAME to refresh one skill.")
        return 0

    if args.install_new:
        for name in missing:
            print(f"Installing new skill: {name}")
            install_skill(args.repo, name, args.ref, target_root, overwrite=False)

        router = args.repo.rsplit("/", 1)[-1]
        if missing and not args.no_refresh_router and router in remote and (target_root / router).exists():
            print(f"Refreshing router only: {router}")
            install_skill(args.repo, router, args.ref, target_root, overwrite=True)

    for name in dict.fromkeys(args.refresh):
        if name not in remote:
            raise SystemExit(f"Remote skill not found: {name}")
        if not (target_root / name).exists():
            raise SystemExit(f"{name} is not installed. Use --install-new for missing add-ons.")
        print(f"Refreshing selected skill: {name}")
        install_skill(args.repo, name, args.ref, target_root, overwrite=True)

    print("Skill update complete. Restart the host if the new or refreshed skills do not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
