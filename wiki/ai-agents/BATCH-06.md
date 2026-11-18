# AI Agents · 第 6 批（101–120）综合学习路径及审稿指南

> 以 [AI Agents 权威源词表](../../glossaries/ai-agents.md) 第 101–120 条为唯一编号依据。这是编辑/审稿材料，不在 GitHub Pages 公开读者导航中展示批次状态。公共 Explorer 直接映射到各术语详情。

## 关键概念地图

**记忆治理与状态恢复**：Memory Write → Memory Consolidation → Memory Forgetting；State Snapshot → State Restoration；User Preference。

**知识供给与索引**：Retrieval-Augmented Generation (RAG) → Agentic Retrieval → Knowledge Base → Document Ingestion → Chunking → Chunk → Embedding → Vector Database。

**搜索与排序**：Vector Search / Semantic Search / Keyword Search → Hybrid Search → Reranking；Query Rewriting 负责在检索前保留约束地表达用户问题。

### 七个必须分清的边界

1. **Memory Write ≠ 模型声称“记住了”**：只有经过权限和来源校验的外部持久写入才能算数；长期偏好必须可更正或撤回。
2. **Memory Forgetting ≠ Context Compression**：缩短模型输入不等于删除主存、索引、缓存或允许范围内的备份。
3. **State Snapshot ≠ 外部事务回滚**：恢复控制状态之前要先与业务系统对账，确保支付、通知等副作用不重复执行。
4. **RAG ≠ 保证真实性**：引用文档可能已过期，Chunk 可能丢失限制条件。应逐条核实来源、版本和权限。
5. **Embedding 相似度 ≠ 概率**：cosine 分数高不代表对应事实成立或回答准确率高。
6. **Vector Search ≠ Semantic Search 的唯一实现**：语义搜索是匹配目标，向量是常见手段；精确实体和否定可借助关键词/结构化约束。
7. **Hybrid Search ≠ Reranking ≠ Query Rewriting**：融合两路检索、重排既有候选和改写上游 query 各属于不同位置。重排无法召回第一阶段遗漏的文档。

## 贯穿案例：公司现行报销制度 RAG

任务：用户问“2026 年国内差旅报销的住宿上限是多少？”，知识库收录多个年度制度、地区例外、表格和旧版 PDF。

1. **摄取**：为每份制度记录 doc_id、有效日期、版本、ACL 和 content_hash；解析表格与页码，检验 1000 是否被 OCR 误作 10000。
2. **切分**：按标题/条款/表格结构划分 Chunk，保存页码和条款范围；涉及例外的段落必须可回读相邻 Chunk。
3. **召回**：关键词系统保留“2026、国内、住宿上限”等硬约束，向量检索弥补同义说法；Hybrid 使用 RRF 排名融合。
4. **精排**：对已授权的候选文段进行 Reranking，过滤已过期制度；Query Rewriting 不能删掉“2026”和“国内”。
5. **回答**：只有定位到有效的制度与地区例外后才给出上限，附精确引用；缺证据则说明暂不能确认。
6. **恢复**：若 Agent 中途宕机，以 State Snapshot 恢复检索步骤而不是重复执行可能存在的外部审批或写入。

## 中等难度综合面试题

**问：**一个 RAG Agent 选中的 top-1 Chunk 余弦相似度高达 0.94，为什么仍不应直接据此批准报销？

**答：**0.94 是向量空间相关性而非事实正确概率。还须检验资料来源、生效年份、地区适用范围、表格和例外条款是否完整。报销审批是敏感外部动作，执行层需独立验证权限和业务金额，RAG 结果不能自动赋权。

## 中等难度综合考试题

**题：**检索系统在 keyword 与 vector 两路中分别将同一文档排第 1 与第 3，使用 RRF 平滑常数 k=60，求融合分数。若第一阶段检索 top-20 含 8 条相关项，资料库总共存在 10 条相关项，求 recall@20。

**解：**RRF = 1/(60+1) + 1/(60+3) ≈ 0.03227。recall@20 = 8/10 = 80%。此分数不代表正确率，相关项未召回的两条也不能由后续 reranker 凭空补出。

## 一手参考

- [Lewis et al. · RAG（NeurIPS 2020）](https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
- [Karpukhin et al. · Dense Passage Retrieval（EMNLP 2020）](https://aclanthology.org/2020.emnlp-main.550/)
- [Ma et al. · Query Rewriting（EMNLP 2023）](https://aclanthology.org/2023.emnlp-main.322/)
- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph · Memory](https://docs.langchain.com/oss/python/concepts/memory)
- [OpenAI · Retrieval](https://developers.openai.com/api/docs/guides/retrieval)
- [OpenAI · Embeddings](https://developers.openai.com/api/docs/guides/embeddings)
- [Elasticsearch · Hybrid Search](https://www.elastic.co/docs/solutions/search/hybrid-search)
- [Elasticsearch · Ranking and reranking](https://www.elastic.co/docs/solutions/search/ranking)
- [Elasticsearch · RRF](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)
