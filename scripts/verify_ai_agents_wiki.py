#!/usr/bin/env python3
"""Validate the AI Agents glossary-to-Wiki mapping and 20-term PR batch."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "glossaries/ai-agents.md"
WIKI = ROOT / "wiki/ai-agents"
PUBLIC = ROOT / "docs/wiki/ai-agents"
ARTICLES = ("核心定义", "形象理解", "技术原理", "工程实践", "面试题", "考试题", "权威来源")
SLUG = re.compile(r"[^a-z0-9]+")

def canonical_rows():
    rows = []
    chapter = 0
    topic = ""
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        header = re.match(r"^##\s+(\d+)\.\s+(.+)$", line)
        if header:
            chapter, topic = int(header.group(1)), header.group(2)
            continue
        match = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]*)\|\s*([^|]+)\|$", line)
        if match:
            if not chapter:
                raise ValueError("term outside chapter")
            number = len(rows) + 1
            rows.append({"n": number, "chapter": chapter, "topic": topic,
                         "en": match.group(2).strip(), "zh": match.group(3).strip(),
                         "abbr": match.group(4).strip()})
    return rows

def article_filename(index, en):
    base = re.sub(r"\([^)]*\)", "", en).strip().lower()
    slug = SLUG.sub("-", base).strip("-")
    return f"{index:03d}-{slug}.md"

def main():
    rows = canonical_rows()
    assert len(rows) == 332
    assert len(set(r["topic"] for r in rows)) == 16
    plan = json.loads((WIKI / "batches.json").read_text(encoding="utf-8"))
    public = json.loads((PUBLIC / "manifest.json").read_text(encoding="utf-8"))
    assert plan["total_terms"] == public["total"] == len(rows)
    assert plan["source"] == "glossaries/ai-agents.md"
    assert plan["batch_size"] == public["batchSize"] == 20
    assert len(plan["batches"]) == 17
    assert len(public["terms"]) == len(rows)
    ready = []
    for pos, ((r), item) in enumerate(zip(rows, public["terms"]), 1):
        assert item["n"] == pos and item["en"] == r["en"] and item["zh"] == r["zh"]
        assert item["topic"] == r["topic"] and item["abbr"] == r["abbr"]
        assert item["batch"] == (pos - 1) // 20 + 1
        b = plan["batches"][(pos - 1) // 20]
        t = b["terms"][(pos - 1) % 20]
        assert t["no"] == pos and t["en"] == r["en"] and t["zh"] == r["zh"]
        if item["ready"]:
            name = article_filename(pos, r["en"])
            assert item["file"] == name
            assert t["wiki"] == f"wiki/ai-agents/{name}"
            original, mirror = WIKI / name, PUBLIC / name
            assert original.is_file() and mirror.is_file(), name
            body = original.read_bytes()
            assert body == mirror.read_bytes(), f"mirror mismatch {name}"
            content = body.decode("utf-8")
            assert r["en"] in content and r["zh"] in content
            for heading in ARTICLES:
                assert heading in content, f"missing {heading}: {name}"
            assert "易混辨析" in content and "类比的局限" in content
            assert content.count("**问：") >= 2 and content.count("**题：") >= 2
            assert len(re.findall(r"\]\(https://[^)]+\)", content)) >= 2
            ready.append(name)
        else:
            assert item["file"] is None and t["wiki"] is None
            assert t["status"] == "planned"
    assert len(set(ready)) == len(ready)
    assert len(ready) == public["readyInPr"] == public["readyArticles"]
    assert all(item["ready"] == (item["n"] <= len(ready)) for item in public["terms"])
    for i, b in enumerate(plan["batches"]):
        start, end = i * 20 + 1, min((i + 1) * 20, len(rows))
        assert b["batch"] == i + 1 and b["start"] == start and b["end"] == end
        assert b["count"] == end - start + 1 and len(b["terms"]) == b["count"]
        expected = "drafted_in_pr" if end <= len(ready) else "planned"
        assert b["status"] in (expected, "merged") if expected == "drafted_in_pr" else b["status"] == "planned"
    from build_wiki_index import check_index
    check_index(ROOT)
    index = json.loads((ROOT / "docs/data/wiki-index.json").read_text(encoding="utf-8"))
    actual = [a["path"].split("/")[-1] for a in index["articles"] if a["category"] == "ai-agents"]
    assert actual == ready, "Wiki index and AI Agents manifest mismatch"
    print(f"AI Agents Wiki verified: {len(ready)}/{len(rows)} articles, 17 batches, mirrored Pages content.")

if __name__ == "__main__":
    main()
