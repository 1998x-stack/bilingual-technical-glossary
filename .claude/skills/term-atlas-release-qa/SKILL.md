---
name: term-atlas-release-qa
description: Validate, review, publish, or prepare a GitHub PR for TERM/ATLAS glossary, Wiki, website, and PDF updates. Use for build checks, source/mirror consistency, GitHub Pages readiness, regression tests, release audit, and safe merging; not for drafting a term definition or Wiki article from scratch.
---

# TERM/ATLAS · Release and Quality Gate

Invoke when the task involves **validation or publication**. Read `AGENTS.md` and `.github/workflows/validate.yml` before changing build, CI, or deployment behavior.

## Preflight: determine the actual output
1. Inspect the changed files, repository branch, and latest main. Categorize the change as source data, authored glossary, independent PDF, Wiki, website, CI, or agent configuration.
2. Review `scripts/build.py`, `scripts/verify.py`, `scripts/verify_wiki.py`, relevant domain-specific renderers, and `.github/workflows/pages.yml`.
3. Match the authoritative input to each generated output; ensure `docs/` mirrors agree with authored files and website `site/` assets where applicable. Never infer completeness from a file existing.
4. Run only the smallest necessary build first; inspect `git diff --stat` and changed binary files. Do not accept accidental regeneration of independently authored PDFs.

## Gate checks
- Base: `python3 -m compileall -q scripts tests` and `node --check site/app.js` / `node --check site/term.js` when Node is available; `python3 scripts/verify.py`; `python3 scripts/build_wiki_index.py --check`; `python3 scripts/verify_wiki.py`; `python3 scripts/verify_docs.py`; `python3 -m unittest discover -s tests -v`.
- Documentation: verify local Markdown links, README statistics against structured catalog, article template editorial separation, and the accuracy of maintenance commands; documentation-check success does not certify external references.
- Agent skills: `python3 scripts/sync_agent_skills.py --check` whenever `AGENTS.md`, `CLAUDE.md`, or skill directories are edited.
- Wiki: verify contiguous source ordinals, canonical-vs-mirror Markdown equality, status/count consistency, actual answer quality and citation relevance, working links.
- PDF: verify actual `%PDF-` header, searchability, embedded readable Chinese fonts, representative page rendering, source/manuscript parity.
- Website: the **single Explorer** is the reader-facing entrypoint and term rows link to `term.html`; **never show batch numbers, batch cards or an independent Wiki landing page**. Validate both expanded and not-yet-expanded terms, URL encoding, back navigation, language links, theme, and same-topic browsing. Check relative links under the project subpath, safe Markdown escaping, keyboard/responsive accessibility, and Pages artifact paths. Browser smoke-test deep links if available.
- Published articles: run `python3 scripts/build_wiki_index.py --check`, confirm only real mirrored Wiki files appear in `docs/data/wiki-index.json`, and keep any former standalone Wiki URL as a backward-compatible redirect.

## PR, merge and provenance
1. Create a narrowly scoped branch and PR. Include source files, terminology/provenance decisions, exact executed checks and results, and visible count/coverage effects.
2. Wait for CI results. Review the failure logs; fix and rerun rather than claiming success from a green check on an unrelated commit.
3. Merge only with appropriate repository permission and requested release intent; avoid force-push and destructive history edits. Close tracking Issues only after merge.
4. On main, verify the merge commit and CI. A successful Pages workflow is evidence of deployment, not necessarily proof of manual browser rendering; state what was actually inspected.
5. If permissions, tools, sources, or checks are unavailable, publish a truthful partial outcome with blockers and no invented release claim.

## Failure patterns to catch
Incorrect README totals; stale `docs/` mirrors; broken Wiki deep links; source JSON generated from outdated TSV; invalid Chinese PDF typography; duplicated skill names or drift; unverified references; unauthorized deletion of authored handbooks.

## Final handoff
Return a concise changed-file summary, validation evidence (pass/fail/not-run), PR/merge status, publication links, and any manual follow-up.
