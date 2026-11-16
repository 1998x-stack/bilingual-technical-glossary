# GitHub Pages activation / 部署说明

This repo has a **complete static site** at `docs/`. Publishing requires GitHub Pages to be enabled for the repository. The connector may not have permission to make that administrative setting change.

## Recommended: branch deployment (no build needed)

1. Open **Repository → Settings → Pages**.
2. Under **Build and deployment → Source**, select **Deploy from a branch**.
3. Choose branch **main** and folder **/docs**, then **Save**.
4. Once GitHub completes publishing, use: `https://1998x-stack.github.io/bilingual-technical-glossary/`.

## Alternative: GitHub Actions

At **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. The repository's `.github/workflows/pages.yml` uploads the prebuilt `docs/` assets and deploys on `main` commits. The default `GITHUB_TOKEN` cannot enable Pages automatically, so the initial Pages settings step is required.

## Troubleshooting

- **404:** Wait for the Pages deployment to finish, and confirm the source is set to `main /docs` or GitHub Actions.
- **JSON did not load:** Use the full project path including `/bilingual-technical-glossary/`; paths are relative to the site root.
- **PDF download error:** Check that `docs/pdf/*.pdf` are present on `main`.
- **Browser opened index.html from disk:** Start a local HTTP server with `python3 -m http.server 8000 --directory docs` so `fetch()` is allowed.
- **Workflow failed with Pages not enabled:** Enable Pages in Settings; do not configure both deployment sources simultaneously.
