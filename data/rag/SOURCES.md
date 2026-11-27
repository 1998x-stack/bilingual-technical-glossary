# RAG / 检索增强生成 — Source and Editorial Notes

**Canonical source:** `data/rag/chapters/01.tsv` through `14.tsv`, four fields `English|中文|abbr|definition` per line. Compiled `data/rag/parts/*.tsv` groups are intermediate aggregations.

**Rebuild and verification:** `node scripts/render_rag.mjs` or read-only `node scripts/render_rag.mjs --check`.

**Scope:** 350 unique English headwords, 14 chapters, 14 key contrasts, 10 medium-level interview questions with answers, 10 medium-level exam questions with calculations and solutions.

**Validation:** row counts, mandatory fields, duplicate English headwords and reproducible exports are automatically checked. Independent expert factual review and PDF render/visual accessibility inspection remain pending.

## Primary papers and official references
1. [Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
2. [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction (NAACL 2022)](https://aclanthology.org/2022.naacl-main.272/)
3. [Malkov & Yashunin (2018), Hierarchical Navigable Small World Graphs](https://arxiv.org/abs/1603.09320)
4. [Asai et al. (ICLR 2024), Self-RAG: Learning to Retrieve, Generate, and Critique](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html)
5. [Yan et al., Corrective Retrieval Augmented Generation (CRAG)](https://aclanthology.org/2026.findings-aacl.151/)
6. [Edge et al. (2024), From Local to Global: A Graph RAG Approach](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)
7. [RAGAS: Automated Evaluation of Retrieval Augmented Generation (EACL 2024)](https://aclanthology.org/2024.eacl-demo.16/)
8. [ARES: Automated Evaluation Framework for RAG Systems (NAACL 2024)](https://aclanthology.org/2024.naacl-long.20/)
9. [Liu et al. (TACL 2024), Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/)
10. [Anthropic Engineering, Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval)
11. [Microsoft Research GraphRAG project and documentation](https://www.microsoft.com/en-us/research/project/graphrag/)
12. [NIST AI Risk Management Framework, Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

## Editorial distinctions for review

- ANN recall is not ground-truth semantic relevance; assess both stages independently.
- A retrieved source being related to a query does not establish that it supports each generated claim.
- Self-RAG and CRAG are distinct named research designs; other retrieval-feedback loops should not automatically inherit their technical claims.
- RAG does not imply confidentiality: permission filtering must be enforced at the data layer, not only via model instructions.
- A citation is meaningful only when its span is from a real, authorized, versioned source and supports the connected statement.
- Tool output and documents are lower-trust data; do not execute embedded instructions.
