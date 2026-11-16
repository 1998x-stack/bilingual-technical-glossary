---
name: term-atlas-glossary-curation
description: Curate, correct, translate, or extend TERM/ATLAS bilingual technical glossary entries and source publications. Use for English-Chinese terminology, TSV/JSON schema, definitions, cross-domain duplicates, and glossary PDF/Markdown alignment; not for long-form Wiki batches.
---

# TERM/ATLAS · Glossary Curation

Use this skill for **terminology-level edits**; use `term-atlas-wiki-batch` when the task is to write long-form concept explanations.

## Inputs and scope
- Identify the domain, affected chapters, source files, and expected output formats.
- Read `AGENTS.md`, `CONTRIBUTING.md`, and the target domain's source notes before changing data.
- Distinguish **canonical source manuscript**, **structured search index**, **generated export**, and **independently authored PDF**. The relationship is domain-specific: `data/terms.json` is the website search index, but not necessarily the authoritative edit point for every glossary.
- For AI Infra, inspect `data/ai-infrastructure.tsv`; C++ uses `data/cpp-glossary.tsv`; University Mathematics uses `sources/university-mathematics.html`; other domains may preserve authored Markdown/PDF.

## Workflow
1. Inventory the real records from files, not README estimates. Note baseline record count and exact chapter, English term, Chinese translation, abbreviation, and definition.
2. Check terminology against the primary technical standard, original paper, stable project documentation, or a reputable textbook. Record ambiguity and version/architecture qualifications; do **not** invent citations.
3. Edit the smallest canonical source(s). Keep English capitalization and acronym semantics correct; `abbr` is only a real abbreviation, and `notation` is a mathematical symbol/example, not an acronym.
4. When structured JSON must change, preserve `category`, positive `chapter`, `topic`, `en`, `zh`, `abbr`, `definition`, and the existing category/topic mapping. Check for duplicates within the same category and chapter, and recognize legitimate cross-domain homonyms.
5. Identify the exact build tool for that domain. Read `scripts/build.py` and domain-specific renderers **before executing them**; builders may regenerate multiple exports and must not overwrite authored publications unintentionally.
6. Reconcile mirrored `docs/` content only when the source was deliberately changed. Preserve independently authored PDFs unless their source and rendered page layout have been reviewed.
7. Run `python3 scripts/verify.py`, `python3 scripts/verify_wiki.py`, and `python3 -m unittest discover -s tests -v`; if a PDF changed, inspect representative pages for glyphs, page breaks, and searchability.
8. Prepare a focused PR: before/after term counts, terminology evidence, affected files, commands/results, and known limitations.

## Do not
- Claim 100% extraction coverage from inherited PDFs; indexed data and source handbooks can differ.
- Turn vendor-specific architecture names into generic standards or use outdated marketing claims as universal definitions.
- Change unrelated domains or bulk-regenerate PDFs without a source-specific need.
- Copy substantial copyrighted source text; paraphrase and cite.
- Report tests as passing unless they were actually run and results observed.

## Completion contract
A reviewed term change is traceable to evidence, respects the correct source-of-truth, preserves unaffected publications, and passes the checks relevant to changed formats. If validation cannot run, report the exact gap.
