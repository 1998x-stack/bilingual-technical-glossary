#!/usr/bin/env python3
"""Validate Machine Learning Wiki coverage, bilingual term identities and QA.

Editorial readiness is NOT professional certification.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "machine-learning"
BATCH_SIZE = 25
TOTAL = 447
SECTIONS = (
    "核心定义", "形象理解", "技术原理与核心内容",
    "工程实践与设计权衡", "关联知识与易混辨析",
    "中等难度面试题", "中等难度考试题", "权威来源与延伸阅读",
)


def source_terms(root: Path = ROOT):
    text = (root / "glossaries/machine-learning.md").read_text(encoding="utf-8")
    terms = []
    chapter = 0
    topic = ""
    for line in text.splitlines():
        title = re.fullmatch(r"## (\d{2})\. (.+)", line)
        if title:
            chapter, topic = int(title.group(1)), title.group(2)
            continue
        row = re.fullmatch(
            r"\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]*)\|\s*([^|]+)\|",
            line,
        )
        if row and topic:
            terms.append({
                "n": len(terms) + 1, "chapter": chapter, "topic": topic,
                "en": row.group(2).strip(), "zh": row.group(3).strip(),
                "abbr": row.group(4).strip(),
            })
    return terms


def validate(root: Path = ROOT):
    source = source_terms(root)
    assert len(source) == TOTAL, f"source count: {len(source)}"
    assert len({s["chapter"] for s in source}) == 19
    assert source[0]["en"] == "Machine Learning (ML)"
    assert source[24]["en"] == "Dataset"
    plan = json.loads((root / "wiki/machine-learning/batches.json").read_text("utf-8"))
    manifest = json.loads((root / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
    assert plan["total_terms"] == manifest["total"] == TOTAL
    assert plan["batch_size"] == manifest["batchSize"] == BATCH_SIZE
    assert len(plan["batches"]) == 18 and len(manifest["terms"]) == TOTAL
    flat = [term for b in plan["batches"] for term in b["terms"]]
    assert len(flat) == TOTAL
    ready = []
    for i, (src, batch, entry) in enumerate(zip(source, flat, manifest["terms"])):
        n = i + 1
        required = ("en", "zh", "topic", "chapter", "abbr")
        assert all(src[field] == entry[field] for field in required), f"manifest term {n}"
        assert all(src[field] == batch[field] for field in required), f"plan term {n}"
        assert entry["n"] == batch["no"] == n
        expected_batch = i // BATCH_SIZE + 1
        assert entry["batch"] == expected_batch
        assert entry["file"] == Path(batch["wiki"]).name
        assert re.fullmatch(r"\d{3}-[a-z0-9-]+\.md", entry["file"])
        if entry["ready"]:
            ready.append(entry)
            assert batch["status"] in {"drafted_in_pr", "merged"}
            canonical = root / "wiki" / DOMAIN / entry["file"]
            mirror = root / "docs/wiki" / DOMAIN / entry["file"]
            assert canonical.is_file() and mirror.is_file(), entry["file"]
            assert canonical.read_bytes() == mirror.read_bytes(), entry["file"]
            content = canonical.read_text(encoding="utf-8")
            assert src["en"] in content.splitlines()[0]
            assert src["zh"] in content.splitlines()[0]
            assert all(s in content for s in SECTIONS), entry["file"]
            assert len(re.findall(r"^\d+\. \*\*问：", content, re.M)) == 2, entry["file"]
            assert len(re.findall(r"^\d+\. \*\*题：", content, re.M)) == 2, entry["file"]
            assert len(re.findall(r"\[[^\]]+\]\(https://[^)\s]+\)", content)) >= 2
        else:
            assert batch["status"] == "planned", f"unready term {n}"
    assert [t["n"] for t in ready] == list(range(1, len(ready) + 1))
    assert manifest["readyInPr"] == manifest["readyArticles"] == len(ready)
    expected = []
    for i, b in enumerate(plan["batches"]):
        assert b["start"] == i * BATCH_SIZE + 1
        assert b["end"] == min(TOTAL, (i + 1) * BATCH_SIZE)
        assert b["count"] == b["end"] - b["start"] + 1 == len(b["terms"])
        expected.extend(range(b["start"], b["end"] + 1))
        n_ready = sum(t["status"] in {"drafted_in_pr", "merged"} for t in b["terms"])
        if n_ready == 0:
            assert b["status"] == "planned"
        elif n_ready == len(b["terms"]):
            assert b["status"] in {"drafted_in_pr", "merged"}
        else:
            assert b["status"] == "drafted_in_pr"
    assert expected == list(range(1, TOTAL + 1))
    index = json.loads((root / "docs/data/wiki-index.json").read_text("utf-8"))
    ml_index = [article for article in index["articles"] if article["category"] == DOMAIN]
    assert len(ml_index) == len(ready)
    assert {article["path"] for article in ml_index} == {
        f"wiki/{DOMAIN}/{item['file']}" for item in ready
    }
    for record, entry in zip(ml_index, ready):
        assert (record["en"], record["zh"], record["chapter"]) == (
            entry["en"], entry["zh"], entry["chapter"]
        )
    ledger = json.loads((root / "wiki/reviews/machine-learning.json").read_text("utf-8"))
    assert ledger["schemaVersion"] == 1 and ledger["domain"] == DOMAIN
    assert {x["path"] for x in ledger["articles"]} == {
        f"wiki/{DOMAIN}/{t['file']}" for t in ready
    }
    assert all(x["status"] in {"pending", "verified"} for x in ledger["articles"])
    return len(ready)


if __name__ == "__main__":
    count = validate()
    print(f"PASS — machine-learning Wiki: {count}/{TOTAL}, 18 batches, "
          "byte-identical Pages mirrors and complete review ledger")
