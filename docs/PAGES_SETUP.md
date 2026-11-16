# GitHub Pages activation / 部署说明

The TERM/ATLAS site is completely generated under `docs/`, and the custom GitHub Actions workflow `.github/workflows/pages.yml` is committed. **Pages requires one-time administrator enablement in newly created or reset repositories.** The `GITHUB_TOKEN` used by this workflow does not have permission to create the Pages site itself.

## Recommended: GitHub Actions deployment / 推荐步骤

1. Open **[repository Settings → Pages](https://github.com/1998x-stack/bilingual-technical-glossary/settings/pages)** while signed into an account with administrator permissions.
2. In **Build and deployment → Source**, choose **GitHub Actions**. Since this repository already has a workflow, **skip GitHub's suggested starter templates**.
3. Open **[Actions → Publish TERM/ATLAS to GitHub Pages](https://github.com/1998x-stack/bilingual-technical-glossary/actions/workflows/pages.yml)** and choose **Run workflow** when initializing Pages. For an active deployment, pushes that change `docs/**` deploy automatically.
4. Confirm the deploy job is green. Then visit **https://1998x-stack.github.io/bilingual-technical-glossary/**.

`pages.yml` deploys committed files from `docs/` on subsequent pushes to the `main` branch when `docs/` changes. `validate.yml` independently checks dataset and tests.

## Alternative: branch deployment

If GitHub Actions is undesired, you can choose **Deploy from a branch → main → /docs**. This publishes the exact same prebuilt static site. However, the repository also contains a custom Pages Actions workflow; it is designed for the **GitHub Actions** source and may fail if the branch deployment source is selected. Use the recommended setup above to avoid conflicting deployment sources.

## Unified Explorer and term detail

- Open [the single Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/#explorer) or select a category such as [reinforcement learning](https://1998x-stack.github.io/bilingual-technical-glossary/?category=reinforcement-learning#explorer).
- Click **any English or Chinese term** to navigate to `term.html`; the page first reads its definition from `data/terms.json`.
- Terms with complete published Wiki articles resolve through `docs/data/wiki-index.json` and load the matching `docs/wiki/<domain>/*.md`. Otherwise, show only the curated short definition. This is expected, not a 404.
- Do not create another public `/wiki` homepage or surface internal Batch production status. A former AI Infra Wiki URL remains only for redirect compatibility.
- `site/` is the frontend source; `docs/` is the Pages mirror, which must contain `term.html`, `term.js`, `term.css`, and `data/wiki-index.json`.

## Troubleshooting

- **Get Pages site failed / Not Found in Configure Pages:** Pages is not yet enabled; set the source to GitHub Actions first, then rerun.
- **404 website:** Make sure the deployment succeeded and the URL includes `/bilingual-technical-glossary/`.
- **JSON did not load:** Check requests for `./data/terms.json`, `./data/catalog.json` and `./data/wiki-index.json`. Paths are relative to the project Pages root.
- **Term detail 404:** Confirm `docs/term.html` is deployed; preserve the `/bilingual-technical-glossary/` subpath and percent-encoded query arguments.
- **Wiki article not displayed:** Only entries in the validated public Wiki index are published as long-form articles. Run `python3 scripts/build_wiki_index.py --check`; verify that the manifest, source and mirrored Markdown match.
- **PDF download error:** Confirm `docs/pdf/*.pdf` are committed on `main`.
- **Opened index.html from disk:** Run `python3 -m http.server 8000 --directory docs` and visit `http://localhost:8000/`; JavaScript `fetch()` does not work reliably over `file://`.

GitHub documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
## Kafka 专题上线检查

Kafka 中英文术语表已并入结构化索引（283 条、16 个专题），可在网站中搜索 `Kafka`、`KRaft`、`Share Group` 等术语，也可以直接使用：

- [Kafka 领域检索](https://1998x-stack.github.io/bilingual-technical-glossary/?category=apache-kafka)
- [Kafka Markdown](./glossaries/apache-kafka.md)
- [Kafka PDF](./pdf/apache-kafka.pdf)

本目录由 GitHub Pages 部署工作流发布；新增或修改 `docs/**` 资源后会触发重新部署。

## 数据结构专题上线检查

数据结构中英文术语表提供 **352 条术语、14 个专题**及 **12 组易混淆概念**，已同步到网站的分类导航与中英双语检索索引。

- [数据结构领域检索](https://1998x-stack.github.io/bilingual-technical-glossary/?category=data-structures)
- [数据结构 Markdown](./glossaries/data-structures.md)
- [数据结构 PDF](./pdf/data-structures.pdf)

维护原始排版时，请同步更新 `glossaries/data-structures.md`、`sources/data-structures.html`，并运行索引同步工作流，避免检索内容与 PDF 手册不一致。

## Safe publication policy

GitHub Actions domain renderer jobs no longer push to main. Download the PDF/patch artifact, inspect it and open a PR against main with the canonical source and matching `docs/` files. `pages.yml` runs an independent read-only pre-deployment verification job and grants only `pages: write` to the deploy job. The repo administrator should also activate main branch protection / Rulesets requiring PR review and both validation and browser E2E checks.

- `python3 scripts/verify_workflow_policy.py`: blocks repository-writing workflows.
- `python3 scripts/verify_wiki_reviews.py --check --report`: checks the integrity of human editorial records but does **not** certify any pending article.
- `python -m unittest discover -s e2e -v`: actual Chromium tests with screenshots (requires [E2E setup](../e2e/README.md)).

