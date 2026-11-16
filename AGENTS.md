# AGENTS.md — TERM/ATLAS Editorial & Development Instructions

## Goal
Maintain a precise, versioned Chinese–English technical reference. Accuracy and auditability outrank lexical volume. Never invent definitions, source links, or claims of coverage.

## Source of truth
`data/terms.json` is the structured index for the website. `pdf/*.pdf` includes independently authored original publications. These originals contain additional terms not yet recovered by PDF extraction; do not delete or silently replace them. `data/ai-infrastructure.tsv` is the curated seed used for the AI Infra volume.

## Workflow
1. Understand the affected domain and chapter.
2. Make a minimal change to source JSON.
3. Rebuild with `python3 scripts/build.py`.
4. Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -v`.
5. Check that counts are computed from data, and search returns the updated term.
6. For PDF edits, inspect rendered pages before replacing the publication.
7. Document discrepancies between authored PDFs and extracted entries.

## Quality rules
- English: academically conventional original spelling, correct capitalization/acronym.
- Chinese: commonly accepted translation, with ambiguity explained when warranted.
- Definitions: one or two concise, technically sound sentences.
- Domain classification: no false implication that a proprietary implementation is a universal standard.
- UI: dependency-free HTML/CSS/JS, relative paths for project Pages, semantic labels, input escaping, responsive layout.
- Documentation: keep README totals and topic counts consistent after data changes.
- Security: no secrets in git, escape data before DOM insertion, avoid unsafe external scripts.

## Important distinction
The 6 inherited PDFs collectively report 2,298 terms. The structured extraction contains 2,250 of those terms, plus 142 new AI Infra entries (2,392 searchable terms at initial publication). Do **not** describe the index as a complete lossless transcription unless reconciled row-by-row.

## GPU Kernel edition
The GPU Kernel glossary contains 255 independently authored English–Chinese entries across 13 chapters. Its PDF (`pdf/gpu-kernel.pdf`) and Markdown (`glossaries/gpu-kernel.md`) are source publications and should be kept aligned with the 255 indexed `gpu-kernel` records. `scripts/build.py` regenerates Markdown exports but must not silently replace the authored PDF.

## Calculus volume

The Calculus volume contains 361 entries across 16 topics. An optional `notation` field holds mathematical examples, while `abbr` remains a true abbreviation. Preserve the Calculus PDF as an independently authored publication and compare it to the source manuscript when making corrections.

## Kafka editorial provenance
The 283-row, 16-chapter `glossaries/apache-kafka.md` is an original reference with a preface and concept contrasts. The build intentionally preserves this Markdown and renders its indexed rows to `pdf/apache-kafka.pdf` using `scripts/render_kafka_pdf.py`; mirror to `docs/pdf/`.

## High School Mathematics
The high-school mathematics source is `data/high-school-mathematics.tsv` (351 entries in 16 topics). Build JSON, Markdown and PDF with `scripts/build.py`, which requires a Chinese TrueType font for PDF generation.
