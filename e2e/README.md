# Browser E2E and accessibility smoke tests

The project uses a **real headless Chromium process** and a localhost HTTP server serving the committed `docs/` Pages artifact. This is more meaningful than JavaScript syntax checks, but is not a substitute for human VoiceOver/NVDA testing or academic article review.

## Run locally

```bash
python -m pip install 'playwright==1.56.0'
python -m playwright install --with-deps chromium
python -m unittest discover -s e2e -v
```

The independent GitHub Actions workflow `.github/workflows/browser-e2e.yml` runs on pull requests, main changes affecting the website and manual dispatch. Screenshots are attached as CI artifacts.

## Scenarios

- Main Explorer: category filtering, bilingual name links, published article opening in unified `term.html`.
- Missing long-form Wiki: visible curated definition and honest fallback, not an invented full article.
- Keyboard: `/` search focus, focusable table links, article contents anchor navigation.
- Page state: return to search with original query and category.
- Mobile: 390-pixel viewport, slide-out navigation, document horizontal overflow, dark theme.
- Markdown: tables, code fences, formula-text readability (literal LaTeX is retained when native typesetting is unavailable), HTML and unsafe URL escaping.
- Accessibility smoke: semantic main/navigation regions, meaningful heading hierarchy, visible article table of contents, keyboard operation.

**Explicit limitation:** The current lightweight Markdown reader does not implement a complete LaTeX renderer. The test asserts formulas remain visible as uncorrupted text, not that complex TeX layouts are typeset. Screen reader voice output, WCAG-wide audit and multi-browser compatibility require additional human/specialist testing.
