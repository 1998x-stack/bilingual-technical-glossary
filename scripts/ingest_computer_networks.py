#!/usr/bin/env python3
"""Sync Computer Networks TSV into TERM/ATLAS JSON, CSV, and Pages exports."""
from __future__ import annotations
import csv
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/computer-networks.tsv"
SLUG = "computer-networks"
FIELDS = ["category", "chapter", "topic", "en", "zh", "abbr", "definition", "notation"]

def load_records(source: Path = SOURCE):
    records = []
    chapter = 0
    topic = ""
    for index, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            match = re.fullmatch(r"# (\d{2}) (.*?) / (.+)", line)
            if not match:
                raise ValueError(f"Invalid chapter at line {index}: {line}")
            chapter = int(match.group(1))
            topic = match.group(2)
            continue
        values = [x.strip() for x in line.split("|")]
        if len(values) != 3 or not chapter or not all(values):
            raise ValueError(f"Invalid row at line {index}: {line}")
        en, zh, definition = values
        abbreviated = re.findall(r"\(([A-Z][A-Z0-9/.-]{1,18})\)", en)
        # Abbreviations in some protocols and tools are part of the term itself.
        abbr = abbreviated[-1] if abbreviated else ""
        records.append(dict(category=SLUG, chapter=chapter, topic=topic,
                            en=en, zh=zh, abbr=abbr, definition=definition))
    by_chapter = defaultdict(list)
    for entry in records:
        by_chapter[entry["chapter"]].append(entry)
    if len(records) != 359 or sorted(by_chapter) != list(range(1, 19)):
        raise ValueError(f"Unexpected records: {len(records)} rows, {len(by_chapter)} chapters")
    duplicates = [(row["chapter"], row["en"].casefold())
                  for row in records]
    if len(duplicates) != len(set(duplicates)):
        raise ValueError("Duplicate English term in chapter")
    return records

def main():
    additions = load_records()
    indexed = ROOT / "data/terms.json"
    old = json.loads(indexed.read_text(encoding="utf-8"))
    old = [x for x in old if x["category"] != SLUG]
    data = old + additions
    indexed.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Preserve every existing optional JSON field in CSV, matching corpus_integrity.
    fields = ["category", "chapter", "topic", "en", "zh", "abbr", "definition"]
    fields += sorted({key for row in data for key in row} - set(fields))
    with (ROOT / "data/terms.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(data)

    # Preserve the manually curated glossary with editorial contrasts and citations.
    target_md = ROOT / "docs/glossaries/computer-networks.md"
    target_md.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "glossaries/computer-networks.md", target_md)

    web = ROOT / "docs/data"
    web.mkdir(parents=True, exist_ok=True)
    (web / "terms.json").write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    catalog_path = web / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    meta = {
        "slug": SLUG,
        "en": "Computer Networks",
        "zh": "计算机网络",
        "description": "Layers, Ethernet, Wi-Fi, IPv4/IPv6, routing, TCP, QUIC, DNS, HTTP, TLS and network operations",
        "icon": "network",
        "count": len(additions),
        "topics": len(set(x["topic"] for x in additions)),
    }
    catalog = [item for item in catalog if item["slug"] != SLUG]
    # Insert near related core systems topics.
    anchor = next((i for i, item in enumerate(catalog) if item["slug"] == "operating-systems"), len(catalog))
    catalog.insert(anchor + 1, meta)
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {len(additions)} Computer Networks terms in {meta['topics']} topics; corpus {len(data)} terms")

if __name__ == "__main__":
    main()
