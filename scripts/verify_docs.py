#!/usr/bin/env python3
"""Check core TERM/ATLAS documentation against the committed corpus (stdlib only).

This is a read-only, offline check; it does not validate live external URLs,
article factual correctness, PDF typography, or browser rendering.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (
    "README.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CHANGELOG.md",
    "docs/PAGES_SETUP.md",
    "docs/QUALITY_AUDIT.md",
    "docs/DOCUMENTATION_AUDIT_2026-11-16.md",
    "docs/MAINTAINERS_GUIDE.md",
    "docs/agent-skills.md",
    "wiki/README.md",
    "wiki/TEMPLATE.md",
    "wiki/EDITORIAL_REVIEW.md",
    "wiki/ai-infrastructure/README.md",
    "wiki/ai-infrastructure/BATCH-02.md",
    "wiki/ai-infrastructure/BATCH-03.md",
    "wiki/ai-infrastructure/BATCH-04.md",
    "wiki/ai-infrastructure/BATCH-05.md",
    "wiki/ai-infrastructure/BATCH-06.md",
    "wiki/ai-infrastructure/BATCH-07.md",
    "wiki/ai-infrastructure/BATCH-08.md",
    "docs/wiki/ai-infrastructure/README.md",
    "docs/wiki/ai-infrastructure/BATCH-02.md",
)
MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]\n]*\])\(([^)\n]+)\)")
BACKTICKS = re.compile(r"^\s*(?:```|~~~)")


def local_link_errors(root: Path = ROOT, docs=DOCUMENTS) -> list[str]:
    problems = []
    for filename in docs:
        path = root / filename
        if not path.is_file():
            problems.append(f"missing documentation: {filename}")
            continue
        fenced = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if BACKTICKS.match(line):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in MARKDOWN_LINK.finditer(line):
                target = match.group(1).strip().strip("<>").strip()
                if not target or target.startswith("#"):
                    continue
                # Markdown links with quoted title: split after first whitespace.
                target = target.split(" \"", 1)[0]
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or target.startswith("//"):
                    continue
                path_text = unquote(parsed.path)
                if not path_text or path_text.startswith("#"):
                    continue
                candidate = (path.parent / path_text).resolve()
                if not candidate.is_relative_to(root.resolve()):
                    problems.append(f"{filename}:{line_number} escapes repository: {target}")
                elif not candidate.exists():
                    problems.append(f"{filename}:{line_number} broken local link: {target}")
    return problems


def check_documentation(root: Path = ROOT) -> list[str]:
    problems = local_link_errors(root)
    try:
        # Check canonical and Pages Markdown links for every published article.
        published = json.loads((root / "docs/data/wiki-index.json").read_text(encoding="utf-8"))
        article_paths = []
        for entry in published["articles"]:
            relative = entry["path"]
            if not re.fullmatch(r"wiki/[a-z0-9-]+/[0-9]{3}-[a-z0-9-]+\.md", relative):
                problems.append(f"unsafe published article path: {relative!r}")
                continue
            article_paths.extend((relative, "docs/" + relative))
        problems.extend(local_link_errors(root, article_paths))
        terms = json.loads((root / "data/terms.json").read_text(encoding="utf-8"))
        catalog = json.loads((root / "docs/data/catalog.json").read_text(encoding="utf-8"))
        en = (root / "README.md").read_text(encoding="utf-8")
        zh = (root / "README.zh-CN.md").read_text(encoding="utf-8")
        total = f"{len(terms):,}"
        domains = len(catalog)
        topics = sum(domain["topics"] for domain in catalog)
        for label, content in (("README.md", en), ("README.zh-CN.md", zh)):
            if total not in content:
                problems.append(f"{label}: indexed term count should be {total}")
            if f"{topics}" not in content:
                problems.append(f"{label}: indexed topic count should be {topics}")
        if f"{domains} domains" not in en:
            problems.append(f"README.md: must describe {domains} domains")
        if f"{domains} 个学科" not in zh:
            problems.append(f"README.zh-CN.md: must describe {domains} 个学科")
        if f"{topics} 个专题" not in zh:
            problems.append(f"README.zh-CN.md: must describe {topics} 个专题")
        if "23 个学科、347 个专题" in zh:
            problems.append("README.zh-CN.md: old 23/347 coverage still present")
        template = (root / "wiki/TEMPLATE.md").read_text(encoding="utf-8")
        if re.search(r"(?i)batch\s*\d*|生产批次|编辑检查", template):
            problems.append("wiki/TEMPLATE.md: reader article template exposes editorial production fields")
        if "- [ ]" in template:
            problems.append("wiki/TEMPLATE.md: editorial checklist should live in wiki/EDITORIAL_REVIEW.md")
        historical = (root / "docs/QUALITY_AUDIT.md").read_text(encoding="utf-8")
        if "历史快照" not in historical:
            problems.append("docs/QUALITY_AUDIT.md: missing historical audit warning")
        if not (root / "docs/MAINTAINERS_GUIDE.md").is_file():
            problems.append("docs/MAINTAINERS_GUIDE.md: missing operational guide")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        problems.append(f"could not validate documentation metadata: {exc}")
    return problems


def main() -> int:
    problems = check_documentation()
    if problems:
        print(f"FAIL — {len(problems)} documentation issue(s)")
        for item in problems[:60]:
            print(f" - {item}")
        return 1
    print("PASS — documentation links, catalog totals, reader/editor separation and audit currency")
    return 0


if __name__ == "__main__":
    sys.exit(main())
