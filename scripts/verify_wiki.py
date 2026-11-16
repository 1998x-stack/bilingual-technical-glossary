#!/usr/bin/env python3
"""Validate the AI Infra wiki publication and 20-term batch manifest (stdlib only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TSV = ROOT / "data" / "ai-infrastructure.tsv"
WIKI = ROOT / "wiki" / "ai-infrastructure"
PUBLIC = ROOT / "docs" / "wiki" / "ai-infrastructure"


def main():
    rows = []
    chapter = ""
    for line in TSV.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if line.startswith("#"):
            chapter = line[1:].strip()
            continue
        en, zh, abbr, definition = line.split("|", 3)
        rows.append((en, zh, abbr, chapter))
    assert len(rows) == 142, f"AI Infra source changed: {len(rows)}"
    meta = json.loads((WIKI / "batches.json").read_text(encoding="utf-8"))
    site = json.loads((PUBLIC / "manifest.json").read_text(encoding="utf-8"))
    assert meta["total_terms"] == len(rows) == site["total"]
    assert meta["batch_size"] == site["batchSize"] == 20
    expected_batches = (len(rows) + meta["batch_size"] - 1) // meta["batch_size"]
    assert len(meta["batches"]) == expected_batches
    assert [b["count"] for b in meta["batches"]] == [
        min(meta["batch_size"], len(rows) - i * meta["batch_size"])
        for i in range(expected_batches)
    ]
    assert sum(b["count"] for b in meta["batches"]) == len(rows)
    assert len(site["terms"]) == len(rows)
    completed = 0
    for i, ((en, zh, abbr, topic), item) in enumerate(zip(rows, site["terms"]), start=1):
        assert item["n"] == i and item["en"] == en and item["zh"] == zh
        assert item["abbr"] == abbr and item["topic"] == topic
        assert item["batch"] == ((i - 1) // 20 + 1)
        b = meta["batches"][(i - 1) // 20]
        assert b["terms"][(i - 1) % 20]["en"] == en
        if not item["ready"]:
            assert item["file"] is None
            continue
        completed += 1
        assert item["file"]
        canonical = WIKI / item["file"]
        mirror = PUBLIC / item["file"]
        assert canonical.is_file() and mirror.is_file(), f"missing page: {canonical}"
        body = canonical.read_text(encoding="utf-8")
        assert body == mirror.read_text(encoding="utf-8"), f"unsynced mirror: {canonical}"
        assert en in body and zh in body
        for heading in ("核心定义", "形象理解", "技术原理", "工程实践", "易混概念", "面试题", "考试题", "参考资料"):
            assert heading in body, f"missing {heading}: {canonical}"
        assert body.count("**问：") >= 2 and body.count("**题：") >= 2, f"missing Q&A: {canonical}"
        assert "https://" in body, f"missing reference: {canonical}"
    assert completed == site.get("readyArticles", site["readyInPr"]), "Wiki ready count does not match published files"
    assert len({item["file"] for item in site["terms"] if item["ready"]}) == completed, "Duplicate article file"
    assert all(item["ready"] == (item["n"] <= completed) for item in site["terms"]), "Unexpected completed ordering"
    print(f"AI Infra Wiki verified: {completed}/{len(rows)} articles, 8 batches, mirrored Pages content.")


if __name__ == "__main__":
    main()
