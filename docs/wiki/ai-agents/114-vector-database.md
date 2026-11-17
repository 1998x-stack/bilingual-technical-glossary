# Vector Database（向量数据库）

> AI Agents · 专题：检索与知识增强 · 数学原理、检索架构与工程权衡；具体参数随产品和版本变化

## 1. 核心定义

**Vector Database（向量数据库）**：Vector Database（向量数据库）是支持向量字段存储、索引与相似性查询的数据服务，通常可配合元数据过滤、持久化、增删改与近似最近邻（ANN）算法。它可作为 RAG 的检索基础设施，却不是知识可信度或用户授权的自动保证。

**适用边界：**实现可能是独立向量产品、通用搜索引擎或关系数据库的向量扩展；不能泛称所有向量库都采用 HNSW 或支持相同事务/过滤语义。

## 2. 形象理解

像按‘内容相似程度’组织的图书馆目录，能找到相近书籍，却仍需核对读者权限和原始内容。

**类比的局限：**目录引擎并不验证书的真假，且搜索接近不意味着最精确的法律条款已经找到。

## 3. 技术原理与核心内容

存储 `{id,vector(d),metadata,source,version,acl}` 并建立 ANN 或 exact kNN 索引。查询链路为 query_embedding → candidate search → metadata/ACL filter → optional rerank → return refs。对删除和更新需验证索引可见性、租户隔离和过滤前后语义；不同引擎的 pre-filter/post-filter 影响召回与性能。对向量规模与延迟进行容量规划。

## 4. 工程实践与设计权衡

**工程案例：**内部文档平台使用向量库按部门查研发设计说明，但先基于可信 tenant_id 和项目成员权限过滤；某条设计规范更新后，旧版本向量应及时失效，避免搜索返回历史接口参数。

**失败模式与验证：**ANN 近似漏掉应有结果、删除后旧索引仍被查询、向量缓存混用不同客户、索引版本不匹配 embedding 模型。通过 exact kNN 基线比较 recall@k，监测索引构建和更新延迟。

## 5. 关联知识与易混辨析

Vector Database 是索引与存储服务；Embedding 是向量表示；Vector Search 是查询操作；Knowledge Base 还包含文档、版本、权限与知识治理等更高层能力。

## 6. 中等难度面试题（含参考答案）

1. **问：向量数据库为何不能直接取代知识库的权限与版本管理？** 答：相似度引擎不自动确认信息来源、用户授权或文档是否现行；需在可信存储/检索层强制元数据过滤。
2. **问：如何衡量 ANN 索引质量？** 答：用同一数据集的精确 kNN 结果作基准，计算 recall@k，并同时比较查询延迟、更新一致性和资源成本。

## 7. 中等难度考试题（含解析）

1. **题：精确 kNN 的 top-10 里有 10 个邻居，ANN 返回的 top-10 与其重合 8 个，ANN recall@10？** 解：8/10=80%；这是近邻召回指标，不是回答正确率。
2. **题：向量库有 2000 条记录，删除 200 条旧版又新增 150 条新版，假设成功且无重复，最终多少？** 解：2000−200+150=1950 条。

## 8. 权威来源与延伸阅读

- [OpenAI API · Retrieval](https://developers.openai.com/api/docs/guides/retrieval)：文件切分、嵌入与索引管理。
- [OpenAI API · File search](https://developers.openai.com/api/docs/guides/tools-file-search)：向量存储与混合文档检索。
