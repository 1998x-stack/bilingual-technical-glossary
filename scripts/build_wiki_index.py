#!/usr/bin/env python3
"""Build the reader-facing term → full Wiki link index (stdlib only).

The public index contains only articles that are actually published and indexed.
Editorial batch IDs, statuses and production checklists are intentionally excluded.
Usage:
  python3 scripts/build_wiki_index.py --write
  python3 scripts/build_wiki_index.py --check
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/data/wiki-index.json"
ARTICLES = ROOT / "docs/wiki"
SAFE_FILE = re.compile(r"^[0-9]{3}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
SAFE_DOMAIN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def generate_index(root: Path = ROOT) -> dict:
    corpus = json.loads((root / "data/terms.json").read_text(encoding="utf-8"))
    identities: dict[tuple, list[tuple[int, dict]]] = {}
    for i, record in enumerate(corpus):
        key = (record["category"], record["en"], record["zh"], record["topic"])
        identities.setdefault(key, []).append((i, record))

    published: list[tuple[int, dict]] = []
    seen: set[tuple] = set()
    for manifest_path in sorted((root / "docs/wiki").glob("*/manifest.json")):
        category = manifest_path.parent.name
        if not SAFE_DOMAIN.fullmatch(category):
            raise ValueError(f"invalid Wiki domain: {category}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        entries = manifest.get("terms", [])
        if not isinstance(entries, list):
            raise ValueError(f"{manifest_path} must contain a terms array")
        for entry in entries:
            if not entry.get("ready", False):
                continue
            en, zh, topic = (entry.get(k) for k in ("en", "zh", "topic"))
            filename = entry.get("file", "")
            if not isinstance(filename, str) or not SAFE_FILE.fullmatch(filename):
                raise ValueError(f"unsafe article filename in {manifest_path}: {filename!r}")
            key = (category, en, zh, topic)
            matches = identities.get(key, [])
            if len(matches) != 1:
                raise ValueError(f"published Wiki term not uniquely indexed: {key!r} ({len(matches)} matches)")
            _, record = matches[0]
            identity = (category, record["chapter"], en, zh)
            if identity in seen:
                raise ValueError(f"duplicate published Wiki article: {identity!r}")
            seen.add(identity)
            canonical = root / "wiki" / category / filename
            public = root / "docs/wiki" / category / filename
            if not canonical.is_file() or not public.is_file():
                raise ValueError(f"missing original or Pages article: {public}")
            if canonical.read_bytes() != public.read_bytes():
                raise ValueError(f"Wiki article mirror mismatch: {public}")
            published.append((corpus.index(record), {
                "category": category,
                "chapter": record["chapter"],
                "en": en,
                "zh": zh,
                "path": f"wiki/{category}/{filename}",
            }))
    published.sort(key=lambda record: record[0])
    return {"schemaVersion": 1, "articles": [record for _, record in published]}


def serialized_index(root: Path = ROOT) -> str:
    return json.dumps(generate_index(root), ensure_ascii=False, indent=2) + "\n"


def write_index(root: Path = ROOT) -> None:
    target = root / "docs/data/wiki-index.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(serialized_index(root), encoding="utf-8")


def check_index(root: Path = ROOT) -> None:
    target = root / "docs/data/wiki-index.json"
    expected = serialized_index(root)
    actual = target.read_text(encoding="utf-8")
    if actual != expected:
        raise ValueError("Public Wiki index is stale; run: python3 scripts/build_wiki_index.py --write")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="regenerate public Wiki metadata")
    mode.add_argument("--check", action="store_true", help="fail if metadata or mirrors are stale")
    args = parser.parse_args()
    try:
        if args.write:
            write_index()
        check_index()
        count = len(generate_index()["articles"])
        print(f"PASS — {count} published term articles indexed for the unified explorer")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL — {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
