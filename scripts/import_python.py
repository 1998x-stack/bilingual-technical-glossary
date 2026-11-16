#!/usr/bin/env python3
"""Import authored Python terminology tables into the canonical JSON search index."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "glossaries/python.md"
DATA = ROOT / "data/terms.json"

def read_python_terms():
    chapter = 0
    topic = ""
    result = []
    for line in SOURCE.read_text(encoding="utf8").splitlines():
        match = re.match(r"^## (\d{2}) (.+?) /", line)
        if match:
            chapter, topic = int(match.group(1)), match.group(2).strip()
            continue
        if line.startswith("## 附录"):
            chapter = 0
        if not chapter or not line.startswith("| ") or re.match(r"^\| (English|---)", line):
            continue
        cols = [s.strip().replace(r"\|", "|") for s in re.split(r"(?<!\\)\|", line[1:-1])]
        if len(cols) != 3:
            raise ValueError(f"Malformed Markdown row: {line[:120]}")
        en, zh, definition = cols
        abbr = re.search(r"\(([A-Z][A-Z0-9/-]{1,9})\)$", en)
        result.append(dict(category="python", chapter=chapter, topic=topic, en=en, zh=zh,
                           abbr=abbr.group(1) if abbr else "", definition=definition))
    if not result:
        raise ValueError("No Python terms found")
    return result

def main():
    python = read_python_terms()
    others = [row for row in json.loads(DATA.read_text(encoding="utf8")) if row["category"] != "python"]
    seen = set()
    for row in python:
        key = row["chapter"], row["en"].casefold(), row["zh"]
        if key in seen:
            raise ValueError(f"Duplicate Python term: {key}")
        seen.add(key)
    DATA.write_text(json.dumps(python + others, ensure_ascii=False, indent=2), encoding="utf8")
    print(f"Indexed {len(python)} Python terms and preserved {len(others)} other entries")

if __name__ == "__main__":
    main()
