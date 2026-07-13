from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("unclosed YAML frontmatter")
    data: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid frontmatter line: {line}")
        data[key.strip()] = value.strip().strip('"')
    if set(data) != {"name", "description"}:
        raise ValueError("frontmatter must contain only name and description")
    return data


def main() -> int:
    errors: list[str] = []
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
    if plugin.get("name") != ROOT.name:
        errors.append("plugin name must match repository name")
    if plugin.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")

    cases = json.loads((ROOT / "evals" / "cases.json").read_text())
    eval_names = {case.get("skill") for case in cases}
    skill_names: set[str] = set()

    for folder in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill_file = folder / "SKILL.md"
        agent_file = folder / "agents" / "openai.yaml"
        try:
            data = frontmatter(skill_file)
        except (OSError, ValueError) as exc:
            errors.append(f"{folder.name}: {exc}")
            continue

        name = data["name"]
        skill_names.add(name)
        if name != folder.name:
            errors.append(f"{folder.name}: frontmatter name mismatch")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{name}: invalid skill name")
        if not data["description"]:
            errors.append(f"{name}: empty description")

        text = skill_file.read_text(encoding="utf-8")
        if "TODO" in text:
            errors.append(f"{name}: unresolved TODO")
        if not agent_file.exists():
            errors.append(f"{name}: missing agents/openai.yaml")
        else:
            agent_text = agent_file.read_text(encoding="utf-8")
            if "$" + name not in agent_text:
                errors.append(f"{name}: default prompt does not name the skill")
            if "allow_implicit_invocation: false" not in agent_text:
                errors.append(f"{name}: explicit invocation policy missing")

    missing_evals = skill_names - eval_names
    extra_evals = eval_names - skill_names
    if missing_evals:
        errors.append(f"skills missing evaluations: {sorted(missing_evals)}")
    if extra_evals:
        errors.append(f"evaluations without skills: {sorted(extra_evals)}")

    for case in cases:
        if not case.get("should_trigger") or not case.get("should_not_trigger"):
            errors.append(f"{case.get('skill')}: trigger coverage incomplete")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in skill_names:
        if f"skills/{name}/" not in readme:
            errors.append(f"{name}: absent from README catalog")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(skill_names)} skills and {len(cases)} evaluation records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
