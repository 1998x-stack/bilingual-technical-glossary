---
name: term-atlas-wiki-batch
description: Research and write a batch of up to 20 long-form TERM/ATLAS concept Wiki articles with precise definitions, intuitive explanations, mechanisms, engineering cases, medium-level interview and exam questions, references, and GitHub Pages synchronization. Use for AI Infra Wiki Batch 03 onward and other domain Wiki batches; not for simple glossary translation.
---

# TERM/ATLAS · Deep Wiki Batch Authoring

Use for **knowledge-article production**, not for ordinary bilingual term corrections. Read `AGENTS.md`, `wiki/TEMPLATE.md`, `wiki/README.md`, and the domain's batch plan first.

## Plan the batch from source data
1. Read the current `main` branch. Detect completed articles and open PRs before deciding the next batch; never assume a previous chat's completion state is current.
2. Find the domain's canonical term order in its source; for AI Infra use `data/ai-infrastructure.tsv`. Read `wiki/ai-infrastructure/batches.json` and `docs/wiki/ai-infrastructure/manifest.json`.
3. Select the **next uncompleted contiguous group of up to 20 terms** in source order (the final group may be shorter). Avoid writing duplicate numbered pages or reordering IDs. For AI Infra, Batch 03 is 041–060 unless the repository has since changed.
4. Define per-article scope: prerequisites, related terms, candidate authoritative references, a mechanism, an engineering example, and assessment objectives.

## Write each article
Use one numbered, stable-slug Markdown file per term: `wiki/<domain>/<NNN>-<english-slug>.md`. Follow the actual template; essential sections are:
- **Core definition:** bilingual name, actual abbreviation, context/architecture/version, one precise explanation.
- **Intuition:** vivid analogy **plus its limits**; avoid metaphors that claim impossible hardware or guaranteed performance.
- **Mechanics:** data path, execution steps, mathematical formula, algorithm, diagram or code as appropriate; state assumptions and units.
- **Engineering:** realistic use case, trade-offs, bottlenecks, failure modes, profiler/test approach.
- **Distinctions and links:** nearby concepts, prerequisites, implementation-specific meanings.
- **Interview:** at least **two medium-difficulty questions with reasoned reference answers**, preferably design/troubleshooting scenarios.
- **Exam:** at least **two medium-difficulty problems with worked solutions**, formula, units, and grading points; independently check arithmetic.
- **References:** relevant official standards, maintained documentation, papers; use the primary source for version-sensitive claims, and mark unverified links.

## Publish only completed articles
1. Update domain batch plan and statuses without inflating completed counts. Statuses should distinguish `planned`, `drafted_in_pr`, and `merged`/published where supported; do not call unreviewed drafts final.
2. Copy or generate the exact article mirror under `docs/wiki/<domain>/`, update the manifest, long-form index, study path, and website reader (if changed). Keep stable deep links and do not silently remove articles.
3. Check all Markdown local links, number continuity, bilingual metadata, topic counts, duplicate pages, equation assumptions, and source relevance.
4. For AI Infra run `python3 scripts/verify_wiki.py`, `python3 scripts/verify.py`, and tests. For other domains, create an equivalent corpus-aware validator before declaring coverage.
5. Open **one focused PR per batch** referencing the tracking Issue. Verify CI and Pages before claiming publication; record what remains planned.

## Editorial stop conditions
Do not fabricate version-specific hardware performance, benchmark results, unavailable official URLs, references, or answers. When a source is uncertain, use an explicit research note and keep that item out of the completed count until vetted.

## Report
Summarize article IDs, titles, new Q&A counts, exact files and links, tests actually executed, PR/merge state, and total verified progress.
