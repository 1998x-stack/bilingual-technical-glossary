# Retrieval-Augmented Generation (RAG)（检索增强生成 · RAG）

> AI Agents · 专题：检索与知识增强 · 适用范围：知识管理与检索工程；具体 API 以版本文档为准

## 1. 核心定义

**Retrieval-Augmented Generation (RAG)（检索增强生成）**：Retrieval-Augmented Generation（RAG，检索增强生成）指在语言模型生成答案时引入来自外部知识库或文档的相关信息，以提高知识可更新性、可追溯性和领域适配。现代工程 RAG 通常包含离线索引与在线检索两条链路。

**适用边界：**RAG 不保证答案天然真实、无幻觉或具备正确引用。Lewis 等 2020 论文给出结合参数化 seq2seq 与非参数化稠密索引的研究形式；当前生产 RAG 可以使用关键词、混合检索与不需微调的提示式方法，两者不能混为一个固定实现。

## 2. 形象理解

像开卷考试：先找到可能相关的书页，再结合题目组织答案，并在关键结论旁指出出处。

**类比的局限：**开卷仍可能找错章节、断章取义或引用过期条款，因此搜到资料不代表回答正确。

## 3. 技术原理与核心内容

离线：`ingest → parse → chunk → embed/index → attach metadata/version/ACL`；在线：`query → retrieve top-k → rerank/filter → context assemble → generate → verify citations`。可使用 BM25、向量或混合召回；来源页码、权限和文档版本必须随 chunk 保留。答案应基于证据而非填补缺失事实；如果召回不足则说明无法确认。

## 4. 工程实践与设计权衡

**工程案例：**企业员工询问今年差旅报销标准，系统从当前生效版制度中检索‘交通/住宿上限’并附条款；如果结果仅来自去年 PDF，必须告知缺少本年依据，不能擅自用旧金额报销。

**失败模式与验证：**切分破坏表格含义、向量召回遗漏精确代码、检索命中未授权文件、引用定位错误、生成结果添加没有来源的数据。通过 recall@k、answer faithfulness、引用准确率及越权检索率分项评测。

## 5. 关联知识与易混辨析

RAG 是检索资料辅助生成的整体框架；Knowledge Base 是被索引的内容系统；Vector Search 是一种召回方法；Agentic Retrieval 在检索过程中增加自主决策和反馈。

## 6. 中等难度面试题（含参考答案）

1. **问：RAG 检索到相关文档，为什么仍可能生成错误答案？** 答：相关不等于支持，切分可能丢条件，生成可能外推；需检查证据与具体断言的对应关系和版本。
2. **问：如何评价企业 RAG 的质量？** 答：分开衡量检索 recall@k、证据权限/新鲜度、回答正确率和引用支持率，不能只用模型主观打分。

## 7. 中等难度考试题（含解析）

1. **题：知识库实际有 10 个相关段落，top-5 里有 4 个相关。precision@5 与 recall@5？** 解：precision@5=4/5=80%；recall@5=4/10=40%。
2. **题：RAG 回答引述了已过期的旧条例，但引用链接可点击，是否一定正确？** 解：不一定。引用存在不代表内容现行有效，还必须核对适用时间及用户问题约束。

## 8. 权威来源与延伸阅读

- [Lewis 等 · Retrieval-Augmented Generation（NeurIPS 2020）](https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)：参数化语言模型与非参数化检索知识结合。
- [OpenAI API · Retrieval](https://developers.openai.com/api/docs/guides/retrieval)：向量存储、自动切分、索引和搜索。
