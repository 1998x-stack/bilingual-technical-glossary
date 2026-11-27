# Optimization Theory · 最优化理论 — Source and Review Notes

- **Canonical source:** `data/optimization-theory/chapters/01.tsv`–`16.tsv`.
- **Schema:** `English|中文|abbr|definition` (blank abbreviations permitted; never use abbreviation column for notation).
- **Compiled intermediates:** `data/optimization-theory/parts/` are four-chapter mirrors, not the source-of-truth.
- **Rebuild:** `node scripts/render_optimization_theory.mjs` (write) or `node scripts/render_optimization_theory.mjs --check` (read-only).
- **Scope:** 400 concise entries, 16 chapters, 14 concept contrasts, 10 medium interview questions and 10 medium exam questions with explanations.
- **Status:** field count and English headword uniqueness verified automatically; independent mathematical review and human visual PDF inspection are pending.
- **Boundary:** optimization guarantees require stated convexity, regularity, convergence, numerical precision and problem assumptions; examples are educational, not proofs of all solver variants.

## References
1. [Convex Optimization — Boyd & Vandenberghe (2004)](https://stanford.edu/~boyd/cvxbook/)
2. [Numerical Optimization — Nocedal & Wright (2nd ed.)](https://link.springer.com/book/10.1007/978-0-387-40065-5)
3. [Nonlinear Programming — Bertsekas](https://faculty.engineering.asu.edu/bertsekas/books/nonlinear-programming-convex-optimization)
4. [Proximal Algorithms — Parikh & Boyd (2014)](https://stanford.edu/~boyd/papers/prox_algs.html)
5. [Distributed Optimization and Statistical Learning via ADMM — Boyd et al. (2011)](https://stanford.edu/~boyd/papers/admm_distr_stats.html)
6. [NEOS Guide — Optimization Problems and Algorithms](https://neos-guide.org/guide/)
7. [CVXPY — Disciplined Convex Programming Tutorial](https://www.cvxpy.org/tutorial/dcp/)
8. [Introduction to Online Convex Optimization — Hazan](https://mitpress.mit.edu/9780262046985/introduction-to-online-convex-optimization/)

## Editorial concerns to review before marking verified

1. Constraint qualifications differ by problem class; KKT necessity and sufficiency must not be conflated.
2. Slater sufficient for strong duality under specified convex setup, not unique solution.
3. ADMM, accelerated methods and stochastic optimizers have conditional convergence statements.
4. Mixed-integer optimality gaps must specify objective sign, normalization and solver convention.
5. Standard CJK CID PDF font should be rendered on Chromium and a desktop PDF reader; inspect missing glyphs and searchable text.
