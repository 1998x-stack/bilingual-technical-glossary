# Chunking（文本切分）

> AI Agents · 专题：检索与知识增强 · 数学原理、检索架构与工程权衡；具体参数随产品和版本变化

## 1. 核心定义

**Chunking（文本切分）**：Chunking（文本切分）是把较长文档按文本结构、语义边界或长度划为可索引的较小单元，以适配检索模型、token 预算与引用定位。合理切分追求信息完整、召回有效和成本可控，不是固定每 N 个字截断就一定最佳。

**适用边界：**切分粒度取决于文档类型：代码、表格、政策条款和普通段落的最佳边界可能不同。chunk_overlap 可以缓解跨边界断裂，但会增大索引体积和重复召回。

## 2. 形象理解

像把一本法律手册分成有标题的小节，每节保留页码与章节号，检索时能找对条款而不必读完整本书。

**类比的局限：**如果把‘不得’和它修饰的操作分到不同片段，单独读取后可能产生相反结论。

## 3. 技术原理与核心内容

常用算法包括 fixed-size、sentence/heading-aware 与 recursive splitter；定义 chunk_size S、overlap O，理想滑窗步长为 S−O。在足够长、无结构断点的文本中，粗略块数可按 `1+ceil((L−S)/(S−O))`（L>S）估算，实际框架对分隔符和末尾短块的处理不同。每块需保留 doc_id、heading_path、page/span_offset、source_version 和 ACL；不能让局部 chunk 丢失继承的权限属性。

## 4. 工程实践与设计权衡

**工程案例：**法务 Agent 需要检索含例外条款的合同。采用按标题和条款切分，跨段时保留‘适用范围/但书’，另用交叉引用检索相邻条款。通过问答测试核验条款号与原始 PDF 页码。

**失败模式与验证：**固定窗口截断公式或表格、overlap 过大产生重复排名、过小丢失上下文；中英文标点与 token 计数差异也导致截断。比较 recall@k、引用定位正确率、重复率和索引成本。

## 5. 关联知识与易混辨析

Chunking 是形成检索单元的处理过程；Chunk 是单个产物；Embedding 将块映射为向量；Document Ingestion 是包含解析、切分、索引的更大管线。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 chunk_size 不能对所有文档都设 1000？** 答：合同条款、代码函数、表格和图像描述各有不同结构；固定长度可能截断关键条件，需按文档类型和查询集调优。
2. **问：overlap 增大一定提高 RAG 质量吗？** 答：不一定，可能增加冗余召回和成本，且切分结构问题并非只靠重复文字能解决；需联合评估上下文完整性。

## 7. 中等难度考试题（含解析）

1. **题：L=1000 token、S=300、O=50，理想固定滑窗（保留末尾短块）约几块？** 解：步长 250；1+ceil((1000−300)/250)=1+ceil(2.8)=4 块。
2. **题：一份 900-token 文档按 300-token 不重叠切分，会得到多少个满块？** 解：900/300=3 个；不计标题和元数据额外 token。

## 8. 权威来源与延伸阅读

- [LangChain · Recursive text splitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter)：递归切分、chunk_size 与 chunk_overlap。
- [OpenAI API · Retrieval](https://developers.openai.com/api/docs/guides/retrieval)：文件切分、嵌入与索引管理。
