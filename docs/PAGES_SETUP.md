# GitHub Pages activation / 部署说明

The TERM/ATLAS site is completely generated under `docs/`, and the custom GitHub Actions workflow `.github/workflows/pages.yml` is committed. **Repository Pages must be enabled once by an administrator.** The `GITHUB_TOKEN` used by this workflow does not have permission to create the Pages site itself.

## Recommended: GitHub Actions deployment / 推荐步骤

1. Open **[repository Settings → Pages](https://github.com/1998x-stack/bilingual-technical-glossary/settings/pages)** while signed into an account with administrator permissions.
2. In **Build and deployment → Source**, choose **GitHub Actions**. Since this repository already has a workflow, **skip GitHub's suggested starter templates**.
3. Open **[Actions → Publish TERM/ATLAS to GitHub Pages](https://github.com/1998x-stack/bilingual-technical-glossary/actions/workflows/pages.yml)** and choose **Run workflow** (or use **Re-run jobs** on the earlier unsuccessful run, which initially lacked Pages enablement).
4. Confirm the deploy job is green. Then visit **https://1998x-stack.github.io/bilingual-technical-glossary/**.

`pages.yml` deploys committed files from `docs/` on subsequent pushes to the `main` branch when `docs/` changes. `validate.yml` independently checks dataset and tests.

## Alternative: branch deployment

If GitHub Actions is undesired, you can choose **Deploy from a branch → main → /docs**. This publishes the exact same prebuilt static site. However, the repository also contains a custom Pages Actions workflow; it is designed for the **GitHub Actions** source and may fail if the branch deployment source is selected. Use the recommended setup above to avoid conflicting deployment sources.

## Troubleshooting

- **Get Pages site failed / Not Found in Configure Pages:** Pages is not yet enabled; set the source to GitHub Actions first, then rerun.
- **404 website:** Make sure the deployment succeeded and the URL includes `/bilingual-technical-glossary/`.
- **JSON did not load:** Check the network request for `./data/terms.json`. Paths are relative to the site root.
- **PDF download error:** Confirm `docs/pdf/*.pdf` are committed on `main`.
- **Opened index.html from disk:** Run `python3 -m http.server 8000 --directory docs` and visit `http://localhost:8000/`; JavaScript `fetch()` does not work reliably over `file://`.

GitHub documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site