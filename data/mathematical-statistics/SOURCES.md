# Mathematical Statistics · 数理统计 — sources and editorial checks

**Canonical chapter source:** `data/mathematical-statistics/chapters/01.tsv`–`16.tsv`, using `English|中文|abbr|definition` rows. `data/mathematical-statistics/parts/*.tsv` is a temporary four-chapter assembly, not the primary source.

**Rebuild:** `node scripts/render_mathematical_statistics.mjs` or verify with `node scripts/render_mathematical_statistics.mjs --check`.

**Deliverable coverage:** 400 concise definitions in 16 chapters; 14 concept contrasts; 12 intermediate interview questions and 12 worked examination questions; references listed below.

**Review status:** automatically verified row structure, chapter counts, required definitions and English headword uniqueness. Independent expert fact checking, equation verification, glyph appearance and page inspection remain pending. Do not mark verified.

## References
1. [Casella & Berger, Statistical Inference (2nd ed.)](https://www.cengage.com/c/statistical-inference-2e-casella-berger/9780534243128)
2. [Wasserman, All of Statistics (Springer, 2004)](https://link.springer.com/book/10.1007/978-0-387-21736-9)
3. [van der Vaart, Asymptotic Statistics (Cambridge University Press)](https://www.cambridge.org/core/books/asymptotic-statistics/A3C7DAD3F7E66A1FA60E9C8FE132EE1D)
4. [Lehmann & Romano, Testing Statistical Hypotheses (4th ed.)](https://link.springer.com/book/10.1007/978-3-030-70578-7)
5. [Efron & Tibshirani, An Introduction to the Bootstrap (CRC)](https://www.routledge.com/An-Introductionto-the-Bootstrap/Efron-Tibshirani/p/book/9780429246593)
6. [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)

## Nuances to review

- A 95% frequentist confidence interval guarantees coverage under repeated sampling, not 95% posterior probability for fixed data.
- A p-value is not the probability that the null hypothesis is true, nor is failure to reject proof of equivalence.
- Finite-sample exact t and F reference distributions require appropriate independence and distributional assumptions.
- Bootstrap resampling and rank tests require checking exchangeability, dependence and discreteness as applicable.
- Causal claims require design/identification assumptions beyond regression significance.
