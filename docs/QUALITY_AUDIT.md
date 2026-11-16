# TERM/ATLAS · Historical main branch quality audit (2026-11-16)

> **历史快照，非当前状态报告。** 本文保留基线 `ac15ffb...` 的已发现问题及当时的建议，**其中独立 Wiki 导航与 Batch UI 建议已经不适用**：当前读者从统一 Explorer 点击术语进入 `term.html`。仓库随后扩展至 25 个学科、8,889 条结构化索引词条和 40 篇已发布的 AI Infra 深度文章。最新文档层审计及未完成风险请见 [DOCUMENTATION_AUDIT_2026-11-16.md](DOCUMENTATION_AUDIT_2026-11-16.md)；日常维护流程见 [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md)。

> 下表“Remediation in this change”描述**该历史 PR 当时实施的措施**，不表示本页列出的旧界面方案仍应保留。

Audit baseline: `ac15ffb16ff238a17b0d9eac4903449ad7d2f1ee`. Scope: 7,554 searchable terms, 21 subjects, 313 topics, Python exporters, independent PDF/Markdown handbooks, Pages, and GitHub Actions.

## Verified defects and remediation

| Severity | Observed defect | Remediation in this change |
|---|---|---|
| P0 | `scripts/ingest_kafka.py` exported only seven CSV fields using `extrasaction="ignore"`, silently dropping Calculus `notation`. | Export all fields from the JSON schema and fail on unexpected writer omissions. |
| P0 | `scripts/sync_data_structures.py` also exported only the core fields and discarded optional fields. | Build fieldnames from the union of all records' keys. |
| P0 | `scripts/verify.py` compared CSV row count with JSON count, not actual field values. | Compare all CSV fields, column schema and row order with canonical JSON. Assert 361 Calculus notation values survive. |
| P1 | The source page `site/index.html` lacked Wiki links already in `docs/index.html`; a rebuild would overwrite the Pages version. | Restore Wiki navigation to the source page; require exact site/Pages mirroring. |
| P1 | GitHub Actions validation did not always run when only `site/**` or `docs/**` changed. | Validate on every PR and every main push; add syntax checks. |
| P1 | `scripts/verify_wiki.py` required exactly 20 completed articles. | Derive batch sizes from the manifest and compare actual ready articles with published metadata. |
| P2 | Public Wiki page still said Batch 01 was awaiting merge; it rendered a hard-coded 20-article badge. | Make wording accurate and badge count depend on each batch's published articles. |
| P2 | READMEs still described the initial Pages activation as an outstanding task. | Clarify that successful deployments have been observed; keep setup steps for fresh deployments. |

## Additional findings for follow-up work

1. **Direct writes to `main` by publishing workflows.** Several publication and synchronization jobs have `contents: write` and push commits directly. Even with retries, they can bypass a PR review workflow, race with concurrent changes, or repeatedly regenerate expensive artifacts. Migrate publication to reviewable PRs (or a single serialized publishing workflow) and use branch protection/rulesets requiring status checks. This is architectural follow-up work, not silently changed here.
2. **Action supply-chain pinning.** `actions/checkout@v4`, `setup-python@v5` and deployment actions use version tags rather than verified immutable commit SHAs/lockfiles. Align on the official GitHub workflow dependency guidance after verifying approved SHA revisions.
3. **PDF reproducibility.** The general build mixes data synchronization and multiple expensive renderers; a developer may regenerate multiple unrelated PDFs while adding one term. Split read-only validation from explicit per-volume rendering, and add image/page-level spot checks for new print editions.
4. **Provenance and licensing.** The repository explicitly has not selected a license. Do not present materials as under an open-source license until the maintainer chooses one. Keep per-volume source citations and distinguish indexed records from original PDFs, including the unindexed 678-entry Computer Organization handbook.
5. **UI and content accessibility.** Add browser-level tests (keyboard navigation, contrast, responsive overflow, empty states) and validate external documentation links with a bounded, cached checker. Avoid network-dependent tests on every pull request.

## Verification contract

Run from the repository root:

```bash
python -m compileall -q scripts tests
node --check site/app.js
python scripts/verify.py
python scripts/verify_wiki.py
python -m unittest discover -s tests -v
```

A valid publication must retain all canonical JSON fields in CSV, match Pages JSON, preserve authored Markdown/PDF mirrors byte-for-byte, keep `site/` assets synchronized with `docs/`, and publish Wiki articles only when their source/Pages content and readiness manifest agree.

**Editorial note:** This audit covers structural correctness and source consistency, not a human peer review of all 7,554 definitions.
