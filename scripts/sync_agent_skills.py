#!/usr/bin/env python3
"""Synchronize and audit portable TERM/ATLAS Agent Skills (stdlib only).

Canonical source: .agents/skills/
Consumer mirrors: .codex/skills/, .pi/skills/, .claude/skills/

Commands:
    python3 scripts/sync_agent_skills.py --check
    python3 scripts/sync_agent_skills.py --sync
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(".agents/skills")
MIRRORS = (
    Path(".codex/skills"),
    Path(".pi/skills"),
    Path(".claude/skills"),
)
REQUIRED = {
    "term-atlas-glossary-curation",
    "term-atlas-wiki-batch",
    "term-atlas-release-qa",
}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(data: bytes, expected_name: str) -> list[str]:
    """Check the portable YAML subset without needing PyYAML."""
    errors = []
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["SKILL.md must be valid UTF-8"]
    lines = text.splitlines()
    if len(lines) < 10 or lines[0] != "---":
        return ["SKILL.md must start with YAML frontmatter and have instructions"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return ["SKILL.md missing frontmatter closing delimiter"]
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            errors.append(f"invalid metadata line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key in fields:
            errors.append(f"duplicate metadata: {key}")
        fields[key] = value
    if set(fields) != {"name", "description"}:
        errors.append(f"metadata must contain only name/description: {sorted(fields)}")
    name = fields.get("name", "")
    if len(name) > 64 or not NAME.fullmatch(name) or name != expected_name:
        errors.append(f"invalid skill name {name!r}, expected {expected_name!r}")
    desc = fields.get("description", "")
    if not (30 <= len(desc) <= 1024) or "<" in desc or ">" in desc:
        errors.append("description must be informative, <=1024 characters and plain text")
    if "Use" not in desc and "when" not in desc.lower():
        errors.append("description must say when the skill should be used")
    body = "\n".join(lines[end + 1:]).strip()
    if len(body) < 350 or not body.startswith("# "):
        errors.append("skill body must contain substantive Markdown instructions")
    return errors


def skill_files(path: Path) -> set[Path]:
    """Return relative regular files; reject link-based directory escape."""
    if path.is_symlink():
        raise ValueError(f"symlinked skill directory is not allowed: {path}")
    if not path.is_dir():
        raise ValueError(f"missing skill directory: {path}")
    result: set[Path] = set()
    for p in path.rglob("*"):
        if p.is_symlink():
            raise ValueError(f"symlink in skill is not allowed: {p}")
        if p.is_file():
            result.add(p.relative_to(path))
    if Path("SKILL.md") not in result:
        raise ValueError(f"SKILL.md missing in {path}")
    return result


def validate_repository(root: Path = ROOT) -> list[str]:
    """Return errors rather than raising, suitable for CI and unit tests."""
    errors: list[str] = []
    source_dir = root / SOURCE
    if not source_dir.is_dir():
        return [f"missing canonical directory: {source_dir}"]
    for loc in (SOURCE, *MIRRORS):
        base = root / loc
        if not base.is_dir():
            errors.append(f"missing skill collection: {loc}")
            continue
        actual = {p.name for p in base.iterdir() if p.is_dir()}
        if actual != REQUIRED:
            errors.append(f"{loc}: expected {sorted(REQUIRED)}, got {sorted(actual)}")
    for name in sorted(REQUIRED):
        canonical = source_dir / name
        try:
            expected = skill_files(canonical)
        except ValueError as e:
            errors.append(str(e))
            continue
        for problem in parse_frontmatter((canonical / "SKILL.md").read_bytes(), name):
            errors.append(f"{SOURCE / name / 'SKILL.md'}: {problem}")
        for loc in MIRRORS:
            mirror = root / loc / name
            try:
                actual = skill_files(mirror)
            except ValueError as e:
                errors.append(str(e))
                continue
            if actual != expected:
                errors.append(f"{loc / name}: file set differs; expected {sorted(map(str, expected))}")
            for relative in expected & actual:
                if (canonical / relative).read_bytes() != (mirror / relative).read_bytes():
                    errors.append(f"{loc / name / relative}: content differs from canonical")
    return errors


def sync_repository(root: Path = ROOT) -> None:
    """Copy only the canonical files. Extra mirror files are never deleted."""
    source = root / SOURCE
    if not source.is_dir():
        raise ValueError(f"missing canonical source: {source}")
    for name in sorted(REQUIRED):
        canonical = source / name
        for rel in skill_files(canonical):
            target = (root / MIRRORS[0]) / name / rel
            for loc in MIRRORS:
                dst = root / loc / name / rel
                if dst.is_symlink():
                    raise ValueError(f"refusing to overwrite symlink: {dst}")
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes((canonical / rel).read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate canonical and mirrors (default)")
    mode.add_argument("--sync", action="store_true", help="copy canonical skills into all three mirrors")
    args = parser.parse_args()
    try:
        if args.sync:
            sync_repository(ROOT)
        errors = validate_repository(ROOT)
    except (OSError, ValueError) as e:
        print(f"FAIL — {e}")
        return 1
    if errors:
        print(f"FAIL — {len(errors)} agent-skill issue(s)")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"PASS — {len(REQUIRED)} portable skills, four locations, valid frontmatter and identical content")
    return 0


if __name__ == "__main__":
    sys.exit(main())
