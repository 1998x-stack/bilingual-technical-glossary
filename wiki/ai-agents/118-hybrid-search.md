# Hybrid Search（混合检索）

> AI Agents · 专题：检索与知识增强 · 信息检索基础与 Agent 工程实践；计算示例为教学题设

## 1. 核心定义

**Hybrid Search（混合检索）**：Hybrid Search（混合检索）是综合词项相关性和语义相似性等不同检索信号来召回或排序资料的方法，常见配置为 BM25 + kNN/向量检索。其目标是同时覆盖精确实体与多样化表达，而不保证每个数据集都优于单独方法。

**适用边界：**BM25 分数和 cosine 分数尺度不同，不能未经归一化直接相加。RRF 使用各路检索的排名，不要求数值尺度统一，但也有 rank_constant 和候选窗口等超参数。

## 2. 形象理解

像招聘同时看岗位硬性证书与工作经历语义匹配，再综合排序，而不是只按一个模糊分数。

**类比的局限：**融合后的高分也可能来自错误文档；资格、权限、时间和来源依然是硬筛选条件。

## 3. 技术原理与核心内容

两路候选分别由 BM25 和 vector kNN 产生。可采用 `RRF(d)=Σ_{r∈retrievers, d∈r} 1/(k+rank_r(d))`，其中 rank 从 1 开始、k 为平滑常数（Elasticsearch 常默认 60）；缺席某路的文档不加该项。RRF 排名融合之外还可使用归一化加权分数，但须明确学习/校准方案。所有分支都需适用 ACL 与版本过滤。

## 4. 工程实践与设计权衡

**工程案例：**企业 API 知识库中用户问‘怎样处理数据库死锁 ORA-00060’，BM25 能精确锁定代码，向量搜索扩展‘deadlock’语义说明；通过 RRF 合并后交给 reranker，最后校验数据库版本。

**失败模式与验证：**各检索路的结果数量严重不平衡、候选窗口过短、高权重噪声、错误 ACL 在某一路泄漏。对精确 ID、同义改写和负面例子分层评测 recall@k、nDCG 与成本。

## 5. 关联知识与易混辨析

Hybrid Search 在召回/融合层组合信号；Reranking 在候选之后精排；Semantic Search 是可能的一路；Query Rewriting 是改变查询表述的上游操作。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能简单 BM25=12 加 cosine=0.8 比大小？** 答：两个指标含义与量纲不同，直接求和会让其中一方主导；应归一化/学习权重或采用 RRF 排名融合。
2. **问：RRF 为什么适合不同评分系统？** 答：它依赖各路相对名次而非原始分数，避免尺度冲突，但仍需调 rank_constant 和窗口大小。

## 7. 中等难度考试题（含解析）

1. **题：RRF k=60，文档 X 在两路分别排名第 1、第 3，分数近似多少？** 解：1/61+1/63≈0.01639+0.01587=0.03227。
2. **题：Y 在关键词第 1、向量路缺席；k=60，RRF 分数？** 解：仅有 1/61≈0.01639；没有向量分支贡献。

## 8. 权威来源与延伸阅读

- [Elasticsearch · Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)：RRF 公式、rank_constant 与排名融合。
- [Elastic · Hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search)：关键词与语义融合及 RRF。
