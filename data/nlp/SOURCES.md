# NLP / 自然语言处理 — Source and editorial notes

**Position:** This is an independent NLP foundations-to-engineering volume, complementing but not replacing the existing LLM and RAG glossaries.

**Canonical manuscript:** `data/nlp/chapters/01.tsv` through `20.tsv`; each data line `English|中文|abbr|definition`. The `data/nlp/parts/*.tsv` files are intermediate 4-chapter aggregation only.

**Rebuild:** `node scripts/render_nlp.mjs`; compare generated TSV, Markdown and PDF mirrors using `node scripts/render_nlp.mjs --check`.

**Scope:** 20 chapters × 25 = 500 unique English headwords; 16 comparison notes; 12 interview questions; 12 medium-difficulty exams with solutions and source bibliography.

**Validation:** source row format, chapter counts, required bilingual fields, unique English headwords and PDF object references checked automatically. Independent mathematical and linguistic expert review, accessibility validation and PDF visual rendering in readers remain pending.

## Academic and official references
1. [Jurafsky & Martin, Speech and Language Processing (3rd ed.)](https://web.stanford.edu/~jurafsky/slp3/)
2. [Manning, Raghavan & Schütze, Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/)
3. [Universal Dependencies — official annotation guidelines](https://universaldependencies.org/)
4. [Vaswani et al., Attention Is All You Need (NeurIPS 2017)](https://arxiv.org/abs/1706.03762)
5. [Devlin et al., BERT: Pre-training of Deep Bidirectional Transformers (NAACL 2019)](https://aclanthology.org/N19-1423/)
6. [Mikolov et al., Efficient Estimation of Word Representations (2013)](https://arxiv.org/abs/1301.3781)
7. [Sutskever et al., Sequence to Sequence Learning with Neural Networks (2014)](https://arxiv.org/abs/1409.3215)
8. [Kudo & Richardson, SentencePiece (EMNLP 2018)](https://aclanthology.org/D18-2012/)
9. [Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training (ACL 2020)](https://aclanthology.org/2020.acl-main.703/)
10. [Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (JMLR 2020)](https://jmlr.org/papers/v21/20-074.html)
11. [Hu et al., LoRA: Low-Rank Adaptation of Large Language Models (2021)](https://arxiv.org/abs/2106.09685)
12. [Papineni et al., BLEU: A Method for Automatic Evaluation of Machine Translation (ACL 2002)](https://aclanthology.org/P02-1040/)
13. [Lin, ROUGE: A Package for Automatic Evaluation of Summaries (2004)](https://aclanthology.org/W04-1013/)
14. [Rajpurkar et al., SQuAD: 100,000+ Questions for Machine Comprehension of Text (2016)](https://aclanthology.org/D16-1264/)
15. [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/)

## Review cautions
1. Tokenizers optimize model vocabulary coverage, not necessarily linguistically meaningful Chinese word boundaries.
2. Perplexity comparisons require compatible tokenization or another properly normalized measurement unit.
3. Sequence labeling has multiple scoring levels; token accuracy differs from strict entity-level exact match.
4. Transformer encoder/decoder restrictions depend on masking and architectural configuration.
5. BLEU and ROUGE scores do not guarantee factual accuracy, fluency or faithfulness.
6. Cross-lingual performance and fairness require testing more than high-resource English datasets.
7. Multimodal and speech tasks have modality-specific error models and metrics.
