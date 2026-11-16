<div align="center">

# TERM/ATLAS

### Bilingual Technical Glossary · 中英双语专业术语库

**A structured reference spanning mathematics, databases, machine learning, and AI engineering.**

[中文说明](README.zh-CN.md) · [Browse the Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/) · [Glossary Sources](glossaries/) · [Contribute](CONTRIBUTING.md)

</div>

![TERM/ATLAS interface preview](assets/term-atlas-overview.webp)

---

## Overview

TERM/ATLAS is a Chinese–English terminology reference for students, researchers, practitioners and technical writers. The site combines **searchable terminology**, **topic-organized Markdown**, and **PDF handbooks**. All counts on the site are calculated from the actual structured dataset, not manually entered statistics.

### Current coverage

| Field | Chinese subject | Indexed terms | Topics | Markdown | PDF |
|---|---|---:|---:|---|---|
| AI Infrastructure / AI Infra | AI 基础设施 | 142 | 8 | [Read](glossaries/ai-infrastructure.md) | [Download](pdf/ai-infrastructure.pdf) |
| GPU Kernel Engineering | GPU Kernel / GPU 核函数 | 255 | 13 | [Read](glossaries/gpu-kernel.md) | [Download](pdf/gpu-kernel.pdf) |
| AI Agents | AI 智能体 | 332 | 16 | [Read](glossaries/ai-agents.md) | [Download](pdf/ai-agents.pdf) |
| Large Language Models | 大语言模型 LLM | 419 | 16 | [Read](glossaries/large-language-models.md) | [Download](pdf/large-language-models.pdf) |
| Deep Learning | 深度学习 | 500 | 18 | [Read](glossaries/deep-learning.md) | [Download](pdf/deep-learning.pdf) |
| Reinforcement Learning | 强化学习 | 305 | 14 | [Read](glossaries/reinforcement-learning.md) | [Download](pdf/reinforcement-learning.pdf) |
| Linear Algebra | 线性代数 | 289 | 12 | [Read](glossaries/linear-algebra.md) | [Download](pdf/linear-algebra.pdf) |
| Compiler Principles | 编译原理 | 268 | 12 | [Read](glossaries/compiler-principles.md) | [Download](pdf/compiler-principles.pdf) |
| Probability Theory | 概率论 | 405 | 16 | [Read](glossaries/probability-theory.md) | [Download](pdf/probability-theory.pdf) |
| SQL Database | SQL 数据库 | 394 | 13 | [Read](glossaries/sql-database.md) | [Download](pdf/sql-database.pdf) |
| **Total** | **10 domains** | **3,309** | **138** | | |

> **Data provenance.** Six inherited subject PDFs report 2,298 entries, of which 2,250 were indexed from page-layout extraction; the originals remain the authoritative publications for those six domains. AI Infra (142), GPU Kernel (255), and SQL Database (394) also have structured/indexed terminology and Markdown/PDF editions. The SQL PDF is a newly typeset reference of the same 394 glossary entries, not a byte-identical copy of the earlier 22-page handbook with supplementary examples. All site counts are derived from the actual index.

## Features

- **Bilingual full-text search:** English, simplified Chinese, abbreviations, topic names, and definitions; multiple search words supported.
- **138 topic chapters:** thematic navigation from mathematical foundations to operational AI infrastructure.
- **Interactive coverage visualization:** bar chart generated directly from indexed content.
- **Practical reading path:** mathematical concepts → model training → LLM/Agent → AI systems.
- **Export:** subject-level Markdown and PDF; filtered search result as CSV; normalized JSON and CSV for programmatic reuse.
- **Accessible, responsive static site:** light/dark display, keyboard search (`Ctrl/⌘ + K` or `/`), no JavaScript dependencies or build framework required.
- **GitHub Pages ready:** prebuilt site in [`docs/`](docs/), plus optional Actions workflow deployment.

## Repository structure

```text
bilingual-technical-glossary/
├── data/
│   ├── terms.json                 # Canonical indexed terms
│   ├── terms.csv                  # Interoperable CSV export
│   ├── sql-database.json          # SQL Database curated source
│   └── ai-infrastructure.tsv     # Curated AI Infra source notes
├── glossaries/                    # 10 thematic Markdown glossaries
├── pdf/                           # 10 searchable PDF handbooks
├── site/                          # Website source: HTML, CSS, JS, icon
├── docs/                          # GitHub Pages static publish directory
│   ├── data/                      # Optimized JSON for frontend
│   ├── glossaries/                # Markdown downloads
│   └── pdf/                       # PDF downloads
├── scripts/
│   ├── build.py                   # Rebuild indexes, Markdown, site
│   └── verify.py                  # Structural checks
├── tests/                         # Regression tests
├── CONTRIBUTING.md
├── AGENTS.md
└── .github/workflows/
```

## Use locally

```bash
git clone https://github.com/1998x-stack/bilingual-technical-glossary.git
cd bilingual-technical-glossary
python3 -m http.server 8000 --directory docs
# Open http://localhost:8000/
```

To modify existing terminology, edit `data/terms.json` and run:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/verify.py
python3 -m unittest discover -s tests -v
```

The build script generates the AI Infra PDF when a suitable Chinese TTF font is installed. Six inherited PDFs and the separately authored GPU Kernel and SQL Database PDFs are preserved, not silently regenerated from JSON.

## Publish on GitHub Pages

1. Go to **Settings → Pages** on this repository.
2. Under **Build and deployment → Source**, choose **GitHub Actions**. The repository already contains `.github/workflows/pages.yml`, so do not generate another workflow.
3. Open **Actions → Publish TERM/ATLAS to GitHub Pages** and rerun the previously failed workflow (or use **Run workflow**), after enabling Pages.
4. Once deployment succeeds, open `https://1998x-stack.github.io/bilingual-technical-glossary/`.

The static site is fully committed in `docs/`. Initial Pages enablement requires a repository administrator; the workflow cannot enable Pages with its default token. See [deployment instructions](docs/PAGES_SETUP.md).

## Editorial principles

1. Preserve the English form used in primary research or official documentation.
2. Prefer common Chinese textbook/industry translations; record alternatives where necessary.
3. Explain terms in plain language without treating a particular implementation as a universal definition.
4. Distinguish homonyms across mathematics and software engineering (e.g., *rank*; *inference* vs *reasoning*).
5. Keep a verifiable source for proposed corrections; do not conflate models, products, frameworks and protocols.
6. Maintain all exported formats consistently; run validation before submitting PRs.

**License:** Licensing terms for source and reference content have not been selected; all rights remain with their respective authors until a license is explicitly published. Contributions should not include third-party copyrighted textbook passages without permission.