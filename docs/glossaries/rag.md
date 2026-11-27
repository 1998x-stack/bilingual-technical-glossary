# 检索增强生成 · Retrieval-Augmented Generation (RAG)

> TERM/ATLAS · 专业中英文术语对照表 | Bilingual Technical Glossary

**350 条术语 · 14 个专业章节 · 2026-11-27**

覆盖 RAG 基础架构、文档摄入与解析、切块、Embedding、BM25、向量数据库与 ANN、混合检索、重排序、查询规划、证据引用、Agentic RAG、GraphRAG、评测、安全及生产优化。

**使用边界：**这些定义为独立撰写的简明概括，不表示所有技术属于同一标准；Self-RAG、CRAG、ColBERT、RAGAS 等特指原研究或工具。证据相关性不等于回答忠实性，检索系统本身也不自动提供访问授权保障。

**编辑状态：**已执行记录格式、章节数量、英文主术语唯一性校验；尚未完成独立专业人员的逐条事实审稿或跨阅读器排版验收。

## 目录

- 01. RAG 基础、架构与知识来源（25 条）
- 02. 数据接入、文档解析与元数据（25 条）
- 03. 文本切块、上下文单位与结构保留（25 条）
- 04. 文本表示、Embedding 与编码器（25 条）
- 05. 稀疏检索与传统信息检索（25 条）
- 06. 向量搜索、ANN 与索引结构（25 条）
- 07. 混合检索、多阶段排序与重排序（25 条）
- 08. 查询理解、改写与动态路由（25 条）
- 09. 证据组织、提示构建与可信回答（25 条）
- 10. 自适应、递归与 Agentic RAG（25 条）
- 11. GraphRAG、图索引与结构化检索（25 条）
- 12. 离线评测、指标与基准测试（25 条）
- 13. 数据安全、访问控制与可信治理（25 条）
- 14. 生产工程、性能与持续优化（25 条）

---

## 01. RAG 基础、架构与知识来源

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Retrieval-Augmented Generation | 检索增强生成 | RAG | 生成模型在回答时检索外部资料，并利用检索内容辅助生成的架构。 |
| 2 | Knowledge-intensive Task | 知识密集型任务 |  | 需要大量事实、领域知识或可更新外部信息才能完成的任务。 |
| 3 | Parametric Knowledge | 参数化知识 |  | 模型在训练中学习并编码在权重中的信息。 |
| 4 | Non-parametric Memory | 非参数化记忆 |  | 模型权重之外、可由检索访问的文本或数据知识集合。 |
| 5 | Knowledge Base | 知识库 | KB | 为查询、检索和回答提供结构化或非结构化知识的存储集合。 |
| 6 | Retrieval Corpus | 检索语料库 |  | 被建立索引并可供检索的文档或记录集合。 |
| 7 | Retriever | 检索器 |  | 根据查询从候选集合中找到相关内容的系统组件。 |
| 8 | Generator | 生成器 |  | 根据用户输入和检索上下文生成自然语言回答的模型。 |
| 9 | Retriever–Generator Pipeline | 检索—生成流水线 |  | 依次执行问题处理、证据检索和生成回答的工作流。 |
| 10 | Open-domain Question Answering | 开放域问答 | ODQA | 从广泛主题的知识来源中回答自然语言问题的任务。 |
| 11 | Closed-domain Question Answering | 封闭域问答 |  | 仅针对约定文档集或专门领域回答问题的任务。 |
| 12 | Grounded Generation | 有依据生成 |  | 要求模型输出能够由指定来源、证据或约束支持的生成方式。 |
| 13 | Knowledge Grounding | 知识锚定 |  | 将生成结果与可核对的外部知识联系起来的过程。 |
| 14 | Retrieval-time Augmentation | 检索时增强 |  | 在推理期间实时获取资料并补充模型输入的方案。 |
| 15 | Index-time Processing | 建索引阶段处理 |  | 在用户查询前完成解析、清洗、切块与索引构建的离线流程。 |
| 16 | Query-time Processing | 查询阶段处理 |  | 收到请求后执行查询理解、检索、排序和回答的在线流程。 |
| 17 | RAG Pipeline | RAG 流水线 |  | 组织数据导入、索引、召回、证据加工与生成的一系列步骤。 |
| 18 | Naive RAG | 基础 RAG |  | 通常按切块、向量检索和直接拼接上下文实现的简单 RAG 结构。 |
| 19 | Advanced RAG | 增强型 RAG |  | 在基础流程中加入查询优化、混合检索、重排序等改进的架构概称。 |
| 20 | Modular RAG | 模块化 RAG |  | 将检索、路由、记忆、重写和生成等功能组成可替换模块的设计。 |
| 21 | Retrieval-Augmented Language Model | 检索增强语言模型 |  | 把语言建模与可检索外部信息结合的模型体系。 |
| 22 | RAG-Sequence | RAG-Sequence |  | Lewis 等人提出的对整段输出采用统一检索文档潜变量的 RAG 形式。 |
| 23 | RAG-Token | RAG-Token |  | Lewis 等人提出的允许各输出位置依赖不同检索文档潜变量的 RAG 形式。 |
| 24 | Knowledge Freshness | 知识时效性 |  | 知识来源相对于现实变化保持准确和更新的程度。 |
| 25 | Evidence-backed Answer | 证据支持的回答 |  | 关键事实声明能够对应明确检索证据的输出。 |

## 02. 数据接入、文档解析与元数据

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Ingestion | 数据摄入 |  | 将原始资料接入检索系统并转换为可处理形式的流程。 |
| 2 | Document Loader | 文档加载器 |  | 从文件、网站或业务系统读取文档内容的组件。 |
| 3 | Content Connector | 内容连接器 |  | 用于对接外部内容存储或 SaaS 数据源的集成接口。 |
| 4 | Document Parsing | 文档解析 |  | 从文件格式中提取正文、表格、版式及其他结构信息的步骤。 |
| 5 | Optical Character Recognition | 光学字符识别 | OCR | 将扫描图像中的字符识别为可搜索文本的技术。 |
| 6 | Layout-aware Parsing | 版面感知解析 |  | 利用标题、栏位、段落位置和阅读顺序解析复杂文档的方法。 |
| 7 | Table Extraction | 表格抽取 |  | 识别表格结构并提取单元格文本和行列关系的流程。 |
| 8 | PDF Text Extraction | PDF 文本提取 |  | 从 PDF 的文本层还原可处理字符及其位置的过程。 |
| 9 | Document Normalization | 文档规范化 |  | 统一编码、空白、标点及表示形式以便后续索引的步骤。 |
| 10 | Text Cleaning | 文本清洗 |  | 去除乱码、模板噪声与无关片段以提升检索质量的过程。 |
| 11 | Boilerplate Removal | 模板噪声移除 |  | 移除网页导航、页脚或重复说明等非正文内容的技术。 |
| 12 | Deduplication | 内容去重 |  | 识别并删除相同或高度重复文档、片段的处理。 |
| 13 | Near-duplicate Detection | 近重复检测 |  | 识别经过少量编辑却基本相同的内容记录。 |
| 14 | Document Identifier | 文档标识符 |  | 为每份来源文档分配稳定且可追踪的唯一标识。 |
| 15 | Chunk Identifier | 片段标识符 |  | 为切分后的文本片段分配可引用的稳定标记。 |
| 16 | Source URI | 来源统一资源标识符 | URI | 标识文档原始位置或逻辑资源地址的字符串。 |
| 17 | Document Metadata | 文档元数据 |  | 描述文档标题、作者、权限、时间与类型等附属信息。 |
| 18 | Metadata Enrichment | 元数据增强 |  | 抽取或推导主题、实体、标签等字段以改进过滤与排序。 |
| 19 | Ingestion Timestamp | 摄入时间戳 |  | 记录数据首次进入或最近一次进入索引管线的时间。 |
| 20 | Document Version | 文档版本 |  | 标识来源文档某次确定内容快照的版本信息。 |
| 21 | Change Data Capture | 变更数据捕获 | CDC | 从数据库日志等机制检测并传播数据增删改事件的方式。 |
| 22 | Incremental Indexing | 增量建索引 |  | 只处理新文档或变化部分，而不重建全部索引的过程。 |
| 23 | Reindexing | 重新建索引 |  | 按新解析、切块或表示规则重新创建检索索引的操作。 |
| 24 | Data Lineage | 数据血缘 |  | 记录检索片段与上游文件、转换及版本之间关联的可追踪关系。 |
| 25 | Provenance Metadata | 来源溯源元数据 |  | 用于回答证据追踪的文档标识、位置和版本等信息。 |

## 03. 文本切块、上下文单位与结构保留

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Text Chunking | 文本切块 |  | 将长文档划分为适合索引与检索的较小文本单元。 |
| 2 | Chunk Size | 片段大小 |  | 每个文本块允许的字数、字符数或 token 数量。 |
| 3 | Chunk Overlap | 片段重叠 |  | 相邻块重复包含的部分，用来减轻边界信息断裂。 |
| 4 | Fixed-size Chunking | 固定长度切块 |  | 按预设字符或 token 数量切分文档的技术。 |
| 5 | Recursive Chunking | 递归切块 |  | 按段落、句子等层级分隔符逐级拆分超长文本的方式。 |
| 6 | Sentence-based Chunking | 按句切块 |  | 以完整句子为基本边界组织索引片段的方法。 |
| 7 | Paragraph-based Chunking | 按段落切块 |  | 尽量保持原始段落连续性的切块策略。 |
| 8 | Semantic Chunking | 语义切块 |  | 依据内容主题变化或向量相似度选择切块边界的方法。 |
| 9 | Structure-aware Chunking | 结构感知切块 |  | 依据标题、列表、表格及章节层级划分内容的方法。 |
| 10 | Hierarchical Chunking | 分层切块 |  | 同时保存文档、章节和细粒度片段等多个层级的结构。 |
| 11 | Parent–Child Retrieval | 父子片段检索 |  | 先定位子片段，再返回其上级较大语境用于生成的策略。 |
| 12 | Small-to-big Retrieval | 由小到大检索 |  | 使用较小单元精准召回，再扩展到周围大段上下文的策略。 |
| 13 | Sliding-window Chunking | 滑动窗口切块 |  | 通过固定长度窗口及滑动步长产生重叠片段的方式。 |
| 14 | Boundary Preservation | 边界保持 |  | 切分时避免打断句子、代码块、标题或表格结构的约束。 |
| 15 | Section Heading Propagation | 章节标题继承 |  | 将上级章节标题附着在子片段上以保留主题信息。 |
| 16 | Contextual Chunking | 上下文化切块 |  | 为独立片段补充文档标题或周边摘要以消除歧义的策略。 |
| 17 | Contextual Retrieval | 上下文检索增强 |  | 在索引前为片段生成解释其文档背景的上下文并参与检索的方法。 |
| 18 | Chunk Granularity | 片段粒度 |  | 检索单元包含信息的细致程度及其跨度。 |
| 19 | Chunk Boundary Error | 切块边界错误 |  | 关键信息被拆开或错误拼接导致检索证据不足的情况。 |
| 20 | Overlap Redundancy | 重叠冗余 |  | 重叠切块使相似内容在候选结果中重复出现的现象。 |
| 21 | Token Budget | token 预算 |  | 请求允许分配给检索证据、提示和生成输出的 token 数量。 |
| 22 | Context Window | 上下文窗口 |  | 语言模型单次推理可接收或处理的 token 范围。 |
| 23 | Context Packing | 上下文装箱 |  | 在给定 token 预算下选择并排列证据片段的过程。 |
| 24 | Chunk-to-document Mapping | 片段—文档映射 |  | 记录每个切块对应原文档及偏移位置的关联信息。 |
| 25 | Lossless Source Linking | 无损来源定位 |  | 确保片段可以回溯到未经改写的原始文档位置的机制。 |

## 04. 文本表示、Embedding 与编码器

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Embedding | 嵌入表示 |  | 把文本、图片或其他对象映射为可计算相似度的向量表示。 |
| 2 | Text Embedding | 文本嵌入 |  | 用向量编码词句或文档语义及检索特征的表示。 |
| 3 | Sentence Embedding | 句向量 |  | 为整个句子生成单一向量的表示方式。 |
| 4 | Document Embedding | 文档向量 |  | 为文档或文档片段生成向量以支持相似度搜索的结果。 |
| 5 | Query Embedding | 查询向量 |  | 将用户查询转换为检索向量的表示。 |
| 6 | Dense Embedding | 稠密嵌入 |  | 大部分维度为非零连续值的向量表示。 |
| 7 | Sparse Embedding | 稀疏嵌入 |  | 大部分维度为零、常保留词项维度信息的表示。 |
| 8 | Bi-encoder | 双塔编码器 |  | 分别编码查询与文档并使用向量相似度匹配的检索模型。 |
| 9 | Dual Encoder | 双编码器 |  | 为两个输入分支独立生成表示并通过匹配函数评分的模型架构。 |
| 10 | Cross-encoder | 交叉编码器 |  | 联合编码查询与文档对并直接输出相关性得分的模型。 |
| 11 | Embedding Dimension | 嵌入维度 |  | 检索向量的元素数量。 |
| 12 | Vector Norm | 向量范数 |  | 衡量向量大小的函数，常用于归一化与相似度计算。 |
| 13 | L2 Normalization | L2 归一化 |  | 把非零向量除以欧氏范数使其长度为一的变换。 |
| 14 | Cosine Similarity | 余弦相似度 |  | 两个非零向量夹角余弦对应的相似度度量。 |
| 15 | Dot-product Similarity | 点积相似度 |  | 以两个向量内积衡量匹配程度的评分方式。 |
| 16 | Euclidean Distance | 欧氏距离 |  | 由向量分量差平方和开方得到的距离。 |
| 17 | Metric Learning | 度量学习 |  | 学习使相关样本接近且无关样本远离的特征表示或距离函数。 |
| 18 | Contrastive Learning | 对比学习 |  | 通过正负样本关系训练表示空间的学习方法。 |
| 19 | In-batch Negatives | 批内负样本 |  | 将同一训练批次中的其他候选作为对比学习负例的策略。 |
| 20 | Hard Negative Mining | 困难负样本挖掘 |  | 选择与查询较相近却不相关的候选增强检索训练的方法。 |
| 21 | Embedding Drift | 嵌入漂移 |  | 模型版本或数据分布变化导致向量分布发生改变的现象。 |
| 22 | Embedding Model Version | 嵌入模型版本 |  | 标记用于构建索引或查询向量的编码器权重与配置版本。 |
| 23 | Embedding Compatibility | 嵌入兼容性 |  | 查询与文档向量能否在同一表征空间中有效比较的条件。 |
| 24 | Multilingual Embedding | 多语言嵌入 |  | 支持不同语言文本在相近语义向量空间匹配的表示模型。 |
| 25 | Multimodal Embedding | 多模态嵌入 |  | 把文本、图像等不同模态映射到可比较表示空间的技术。 |

## 05. 稀疏检索与传统信息检索

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Information Retrieval | 信息检索 | IR | 根据查询从文档集合中查找相关信息的理论与技术。 |
| 2 | Lexical Retrieval | 词法检索 |  | 基于查询与文档词项匹配的召回方式。 |
| 3 | Full-text Search | 全文搜索 |  | 在文档正文上建立索引并支持词项条件查找的方法。 |
| 4 | Inverted Index | 倒排索引 |  | 从词项映射到包含该词的文档及位置列表的索引结构。 |
| 5 | Posting List | 倒排记录表 |  | 存储某词项出现的文档标识、频次或位置信息的列表。 |
| 6 | Term Frequency | 词频 | TF | 词项在指定文档中出现的次数或加权次数。 |
| 7 | Document Frequency | 文档频率 | DF | 包含某个词项的文档数量。 |
| 8 | Inverse Document Frequency | 逆文档频率 | IDF | 对高频通用词赋予较小权重的全局词项稀有度指标。 |
| 9 | TF–IDF | 词频—逆文档频率 | TF-IDF | 结合文档内词频与语料内稀有程度衡量词项重要性的权重。 |
| 10 | BM25 | BM25 排序函数 | BM25 | 结合词频饱和、逆文档频率和文档长度归一化的经典词法相关性评分。 |
| 11 | BM25F | 字段加权 BM25 | BM25F | 对标题、正文等字段分别加权的 BM25 扩展。 |
| 12 | Tokenization | 词元化 |  | 把自然语言文本分解为检索词项或子词单元的步骤。 |
| 13 | Stop-word Removal | 停用词移除 |  | 过滤对检索区分度贡献有限的常见词项的预处理。 |
| 14 | Stemming | 词干提取 |  | 按词形规则把词语变体简化为词干的处理。 |
| 15 | Lemmatization | 词形还原 |  | 根据语言规则将词语归一化为词典基本形式。 |
| 16 | Phrase Search | 短语搜索 |  | 要求多个词项按指定顺序及相邻关系出现的检索方式。 |
| 17 | Proximity Search | 邻近搜索 |  | 对词项在文档中的相对距离设置限制的检索操作。 |
| 18 | Boolean Retrieval | 布尔检索 |  | 利用与、或、非等逻辑运算组合词项匹配条件的方法。 |
| 19 | Fielded Search | 字段检索 |  | 只针对标题、作者或指定元数据字段执行检索的方式。 |
| 20 | Fuzzy Matching | 模糊匹配 |  | 允许一定字符编辑差异的词项检索方式。 |
| 21 | Edit Distance | 编辑距离 |  | 将一个字符串变为另一个字符串所需编辑操作的最小成本。 |
| 22 | Character N-gram | 字符 N 元组 |  | 由连续 N 个字符组成、用于索引或近似匹配的文本片段。 |
| 23 | Synonym Expansion | 同义词扩展 |  | 把查询词映射到相关近义词以扩大召回的策略。 |
| 24 | Exact Match Retrieval | 精确匹配检索 |  | 要求标识符或关键字段与查询完全一致的检索模式。 |
| 25 | Vocabulary Mismatch | 词汇不匹配 |  | 查询和相关文档使用不同措辞导致词法检索失败的现象。 |

## 06. 向量搜索、ANN 与索引结构

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Dense Retrieval | 稠密检索 |  | 用查询与文档的连续向量相似度召回候选的方式。 |
| 2 | Vector Search | 向量检索 |  | 从向量集合中寻找与查询表示距离较近或相似度较高的对象。 |
| 3 | Nearest Neighbor Search | 最近邻搜索 | NN | 查找距离查询向量最近的数据向量的任务。 |
| 4 | Approximate Nearest Neighbor | 近似最近邻 | ANN | 牺牲部分精确性以减少搜索时间或空间成本的最近邻检索。 |
| 5 | Exact Nearest Neighbor | 精确最近邻 |  | 返回满足指定距离定义的真实最近点的搜索方法。 |
| 6 | Top-k Retrieval | 前 k 项检索 | Top-k | 按照匹配评分返回最靠前的 k 个候选结果。 |
| 7 | High-dimensional Space | 高维空间 |  | 向量具有大量坐标维度的表示或搜索空间。 |
| 8 | Curse of Dimensionality | 维度灾难 |  | 高维时距离、数据稀疏性与搜索效率可能退化的现象。 |
| 9 | Vector Index | 向量索引 |  | 为加速向量相似度查询组织的数据结构。 |
| 10 | HNSW | 分层可导航小世界图 | HNSW | 用多层近邻图导航实现高效近似最近邻搜索的索引。 |
| 11 | Navigable Small World Graph | 可导航小世界图 | NSW | 依靠局部近邻边与长程连接支持图搜索的近邻结构。 |
| 12 | Inverted File Index | 倒排文件聚类索引 | IVF | 把向量聚入多个簇，并优先搜索相关簇的近似索引。 |
| 13 | Product Quantization | 乘积量化 | PQ | 将向量分块并独立码本量化以压缩和近似计算距离的技术。 |
| 14 | Optimized Product Quantization | 优化乘积量化 | OPQ | 通过学习向量变换改善乘积量化失真的方法。 |
| 15 | Scalar Quantization | 标量量化 | SQ | 独立压缩向量各维数值的量化技术。 |
| 16 | Vector Compression | 向量压缩 |  | 减少向量存储与访存开销的数值编码策略。 |
| 17 | Centroid | 聚类中心 |  | 代表一个向量聚类的均值或其他中心点。 |
| 18 | Coarse Quantizer | 粗量化器 |  | 先把查询或数据库向量分配到大粒度簇的量化组件。 |
| 19 | Recall–Latency Tradeoff | 召回率—延迟权衡 |  | 调整 ANN 搜索深度时召回质量与检索时延之间的取舍。 |
| 20 | Search Breadth | 搜索宽度 |  | 检索时扩展的候选节点或簇数量。 |
| 21 | Index Build Time | 索引构建时间 |  | 从输入向量创建可查询索引所需的计算时间。 |
| 22 | Index Recall | 索引召回率 |  | ANN 返回结果与精确近邻参考集合重合的比例。 |
| 23 | Vector Database | 向量数据库 |  | 面向向量相似度查询、元数据过滤及索引管理的数据库系统。 |
| 24 | Vector Collection | 向量集合 |  | 共享向量维度、索引与元数据模式的一组检索对象。 |
| 25 | Metadata Filtering | 元数据过滤 |  | 在召回前、召回中或召回后根据标签、时间、权限等条件缩小候选。 |

## 07. 混合检索、多阶段排序与重排序

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Hybrid Retrieval | 混合检索 |  | 结合词法、向量或其他信号共同生成候选结果的检索方案。 |
| 2 | Sparse–Dense Fusion | 稀疏—稠密融合 |  | 合并稀疏词项评分与稠密向量相似度的排序策略。 |
| 3 | Score Fusion | 分数融合 |  | 对不同检索器的数值评分进行校准和组合的方法。 |
| 4 | Rank Fusion | 名次融合 |  | 根据多个结果列表中的排序位置综合候选排序的方法。 |
| 5 | Reciprocal Rank Fusion | 倒数名次融合 | RRF | 将候选在各列表中排名的倒数形式相加进行排序的算法。 |
| 6 | Weighted Rank Fusion | 加权名次融合 |  | 为不同检索器的排序贡献设置权重的融合方法。 |
| 7 | Score Normalization | 检索分数归一化 |  | 将不同来源分数变换到可比较尺度的预处理。 |
| 8 | Candidate Generation | 候选生成 |  | 以高召回为目标快速产生可能相关文档集合的第一阶段。 |
| 9 | First-stage Retrieval | 首阶段检索 |  | 在大规模库中使用低成本方法召回潜在相关结果的环节。 |
| 10 | Second-stage Ranking | 第二阶段排序 |  | 对首阶段少量候选使用更昂贵模型重新计算排序的环节。 |
| 11 | Reranker | 重排序器 |  | 对检索候选逐项或成组重新评估其与查询相关性的模型。 |
| 12 | Cross-encoder Reranking | 交叉编码器重排序 |  | 联合输入查询与文档、计算精细相关分数的重排序方法。 |
| 13 | Pairwise Ranking | 成对排序 |  | 通过比较两个候选的相对偏好学习或判断排序的方法。 |
| 14 | Listwise Ranking | 列表排序 |  | 在整个候选列表层面定义损失或预测其排列的排序方法。 |
| 15 | Learning to Rank | 排序学习 | LTR | 利用标注相关性或行为信号训练排序模型的技术。 |
| 16 | Late Interaction | 后期交互 |  | 分别编码查询与文档 token 后再聚合细粒度匹配分数的结构。 |
| 17 | ColBERT | ColBERT 检索模型 | ColBERT | 使用 token 级向量及 MaxSim 交互评分的神经检索模型族。 |
| 18 | MaxSim | 最大相似度聚合 | MaxSim | 为每个查询 token 取其与文档 token 的最大相似度后汇总的机制。 |
| 19 | Multi-vector Retrieval | 多向量检索 |  | 为一份文档保存多个向量并利用它们联合计算相关性的方式。 |
| 20 | Diversity-aware Ranking | 多样性感知排序 |  | 在相关性之外约束结果列表覆盖不同信息方面的排序策略。 |
| 21 | Maximal Marginal Relevance | 最大边际相关性 | MMR | 平衡候选与查询相关性及与已选结果冗余程度的选择策略。 |
| 22 | Result Deduplication | 结果去重 |  | 对同一文档或重复内容的多个候选进行合并的步骤。 |
| 23 | Ranking Calibration | 排序分数校准 |  | 将模型评分转换为更稳定、可解释或跨查询可比较尺度的方法。 |
| 24 | Retrieval Score Threshold | 检索评分阈值 |  | 依据相关性分数过滤低质量候选的判定界限。 |
| 25 | Top-k Reranking | 前 k 候选重排序 |  | 只对初始排名靠前的固定数量候选使用重排序器的技术。 |

## 08. 查询理解、改写与动态路由

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Query Understanding | 查询理解 |  | 分析请求意图、实体、时效与约束以决定检索策略的过程。 |
| 2 | Query Rewriting | 查询改写 |  | 将原始问题转写为更适合检索的查询表达。 |
| 3 | Query Expansion | 查询扩展 |  | 加入同义词、上下位词或相关概念提升潜在召回的技术。 |
| 4 | Query Decomposition | 查询分解 |  | 把多条件复杂问题拆成多个可独立检索的子问题。 |
| 5 | Multi-query Retrieval | 多查询检索 |  | 为一个用户问题生成多个查询变体并合并结果的策略。 |
| 6 | Hypothetical Document Embeddings | 假设文档嵌入 | HyDE | 先生成与问题匹配的假设答案文档，再用其向量检索真实文档的方法。 |
| 7 | Step-back Prompting | 后退提问 |  | 先将具体问题泛化为较高层背景问题，以检索基础概念的策略。 |
| 8 | Query Intent Classification | 查询意图分类 |  | 识别查事实、求比较、找操作步骤等不同任务类型的分类步骤。 |
| 9 | Entity Extraction | 实体抽取 |  | 从查询中识别机构、人名、产品、时间或其他实体的过程。 |
| 10 | Entity Linking | 实体链接 |  | 将文本提及映射到知识库中唯一实体标识的步骤。 |
| 11 | Named Entity Recognition | 命名实体识别 | NER | 识别文本中人、组织、地点等预定义类型实体的模型任务。 |
| 12 | Query Routing | 查询路由 |  | 根据查询特征选择数据源、索引或检索器的策略。 |
| 13 | Domain Routing | 领域路由 |  | 把请求分发到相应专业知识域或专用数据集的方法。 |
| 14 | Source Selection | 数据源选择 |  | 在多个知识库中确定最值得访问的来源集合的步骤。 |
| 15 | Retrieval Planning | 检索规划 |  | 为复杂请求决定查询序列、检索工具与停止条件的过程。 |
| 16 | Adaptive Retrieval | 自适应检索 |  | 根据问题难度或中间结果动态调整是否检索以及检索次数的方式。 |
| 17 | Retrieval Gating | 检索门控 |  | 根据判定信号决定是否启用外部检索的机制。 |
| 18 | Clarification Question | 澄清性问题 |  | 当用户意图或关键约束不足时请求补充信息的问题。 |
| 19 | Conversational Query Reformulation | 对话查询重构 |  | 把依赖上文的省略句转换为可独立检索的完整查询。 |
| 20 | Coreference Resolution | 指代消解 |  | 确定代词或省略表达与此前实体之间对应关系的步骤。 |
| 21 | Temporal Query Interpretation | 时间查询解释 |  | 理解“去年”“最新”等时间表达并约束检索时间范围的过程。 |
| 22 | Freshness-aware Routing | 时效感知路由 |  | 根据知识更新速度或请求时间要求选择实时或离线索引的策略。 |
| 23 | Query Complexity Estimation | 查询复杂度估计 |  | 判断问题需要单跳查找、多跳推理或聚合分析的过程。 |
| 24 | Answerability Estimation | 可回答性估计 |  | 估计当前证据是否足够支持可靠回答的过程。 |
| 25 | Query Execution Plan | 查询执行计划 |  | 规定各子查询、数据源和结果融合次序的执行方案。 |

## 09. 证据组织、提示构建与可信回答

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Context Assembly | 上下文组装 |  | 将多份检索证据组合成生成模型可处理的输入。 |
| 2 | Evidence Selection | 证据选择 |  | 从候选片段中筛出最能支持回答的内容。 |
| 3 | Evidence Aggregation | 证据聚合 |  | 将不同来源的互补事实整合为有条理的证据集合。 |
| 4 | Evidence Attribution | 证据归属 |  | 标明某条陈述可追溯至哪些具体资料。 |
| 5 | Citation Generation | 引文生成 |  | 为回答内容产生指向来源文档或片段的引用标记。 |
| 6 | Citation Span | 引用片段 |  | 支持某项回答陈述的最小或指定来源文本范围。 |
| 7 | Source Grounding | 来源锚定 |  | 要求生成文本的事实与可验证来源保持对应的约束。 |
| 8 | Answer Synthesis | 答案综合 |  | 综合多个检索结果生成面向问题的连贯回答。 |
| 9 | Answer Faithfulness | 答案忠实性 |  | 答案中的事实主张是否能由指定证据直接支持的性质。 |
| 10 | Unsupported Claim | 无证据支持的断言 |  | 输出中无法由提供的资料合理推出的事实陈述。 |
| 11 | Hallucination | 幻觉 |  | 生成模型输出看似可信却缺乏事实依据或与依据矛盾的内容。 |
| 12 | Abstention | 拒绝猜答 |  | 证据不足时明确说明无法确认而不生成无根据结论的行为。 |
| 13 | Unanswerable Query | 不可回答查询 |  | 在指定知识库和证据限制下无法可靠回答的问题。 |
| 14 | Grounding Instruction | 证据约束指令 |  | 要求模型仅根据可用资料回答并说明不确定性的提示约束。 |
| 15 | Prompt Template | 提示模板 |  | 将用户问题、系统要求与来源证据组织为固定输入格式的结构。 |
| 16 | Context Delimiter | 上下文分隔符 |  | 将可信指令、用户问题和外部资料明确划分的边界标记。 |
| 17 | Source-aware Prompting | 来源感知提示 |  | 在上下文中保留来源标识、标题与时间等元数据的提示方式。 |
| 18 | Evidence Ordering | 证据排序 |  | 按相关性、可靠性或位置影响调整引用片段顺序的过程。 |
| 19 | Lost-in-the-middle Effect | 中间位置忽视现象 |  | 部分模型在长上下文中对位于中间的关键信息利用不足的观察现象。 |
| 20 | Context Compression | 上下文压缩 |  | 减少冗余或低相关 token、保留关键证据的处理。 |
| 21 | Extractive Compression | 抽取式压缩 |  | 仅选择原文支持句段而不重写证据的上下文精简方式。 |
| 22 | Abstractive Compression | 生成式压缩 |  | 用模型重写或总结证据以缩短输入，可能引入信息损失。 |
| 23 | Token Truncation | token 截断 |  | 因上下文长度限制而删除或裁剪部分文本的过程。 |
| 24 | Citation Verification | 引用核验 |  | 检查每项回答断言是否由所标注来源内容实际支持的步骤。 |
| 25 | Evidence Conflict | 证据冲突 |  | 不同来源在相同实体、时间或条件下给出不一致结论的情况。 |

## 10. 自适应、递归与 Agentic RAG

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Agentic RAG | 智能体式 RAG |  | 由规划或智能体逻辑决定检索动作、工具顺序与后续生成的 RAG 架构。 |
| 2 | Iterative Retrieval | 迭代检索 |  | 根据已获证据或中间答案反复构造新查询继续检索的策略。 |
| 3 | Multi-hop Retrieval | 多跳检索 |  | 为建立跨实体或文档关系而连续执行多个证据查找步骤的过程。 |
| 4 | Multi-hop Question Answering | 多跳问答 |  | 答案需组合两个或更多事实链路的问答任务。 |
| 5 | Decomposed Question Answering | 分解式问答 |  | 先拆分复杂问题并解决子问题，再整合最终答案的方式。 |
| 6 | Tool-augmented Retrieval | 工具增强检索 |  | 在文本检索之外调用数据库、搜索 API 或其他工具获取证据。 |
| 7 | Web Search Augmentation | 网络搜索增强 |  | 将网页检索结果引入专有知识库检索与生成过程的策略。 |
| 8 | Self-RAG | Self-RAG 自反思检索增强生成 | Self-RAG | 通过学习的反思 token 控制检索和评判生成内容的方案。 |
| 9 | Corrective RAG | 纠错式 RAG | CRAG | 根据检索质量评估采取修正检索或外部搜索等补救步骤的方案。 |
| 10 | Retrieval Reflection | 检索反思 |  | 根据中间检索证据评估当前路径是否需要修正的过程。 |
| 11 | Self-critique | 自我评判 |  | 模型检查自身候选回答或证据使用是否符合要求的步骤。 |
| 12 | Retrieval Feedback Loop | 检索反馈循环 |  | 将生成或评估结果反馈到下一轮检索的闭环。 |
| 13 | Evidence Gap Detection | 证据缺口检测 |  | 识别当前资料无法回答的子问题或条件的过程。 |
| 14 | Follow-up Search | 后续检索 |  | 针对证据缺口补充执行的新查询。 |
| 15 | Search Budget | 检索预算 |  | 允许使用的检索调用次数、时间或计算成本额度。 |
| 16 | Tool-call Budget | 工具调用预算 |  | 对单个请求的外部工具执行次数或成本施加的限制。 |
| 17 | Stopping Rule | 停止规则 |  | 当证据充分、预算耗尽或无进展时终止检索的判定条件。 |
| 18 | Planner–Executor Pattern | 规划—执行模式 |  | 一个模块决定检索计划、另一模块执行并回报结果的架构。 |
| 19 | Reflection Loop | 反思循环 |  | 多轮检查与修订中间状态以改善最终答案的控制结构。 |
| 20 | Retrieval Policy | 检索策略 |  | 根据请求状态选择下一检索动作或不检索的决策规则。 |
| 21 | Contextual Bandit Routing | 上下文赌博机路由 |  | 基于请求特征与反馈学习选择检索方案的在线决策策略。 |
| 22 | Active Retrieval | 主动检索 |  | 模型在生成过程中根据当前不确定性主动获取外部证据的方式。 |
| 23 | Search Tool Orchestration | 检索工具编排 |  | 协调不同索引、搜索服务和数据库调用顺序与依赖的过程。 |
| 24 | Knowledge Gap Recovery | 知识缺口恢复 |  | 发现库内缺失关键事实后通过追加来源或安全拒答修复流程的策略。 |
| 25 | Iterative Answer Refinement | 迭代答案修订 |  | 在获取新证据后重新组织、纠正或补充生成回答的过程。 |

## 11. GraphRAG、图索引与结构化检索

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | GraphRAG | 图检索增强生成 | GraphRAG | 结合实体关系图与文本证据检索以支持关联推理或全局概述的 RAG 方法族。 |
| 2 | Knowledge Graph | 知识图谱 | KG | 用实体、关系及属性构成结构化知识网络的表示。 |
| 3 | Entity Node | 实体节点 |  | 知识图中代表特定人、机构、概念或对象的节点。 |
| 4 | Relation Edge | 关系边 |  | 连接两个实体、表示二者语义联系的有向或无向边。 |
| 5 | Knowledge Triple | 知识三元组 |  | 以主体、谓词和客体描述一条结构化事实的表示。 |
| 6 | Graph Extraction | 知识图谱抽取 |  | 从文档中识别实体及关系并转化为图结构的过程。 |
| 7 | Entity Resolution | 实体消歧与合并 |  | 判断不同名称或记录是否指向同一真实实体并合并的步骤。 |
| 8 | Graph Index | 图索引 |  | 用于按节点、边或路径快速访问知识图结构的存储组织。 |
| 9 | Community Detection | 图社区发现 |  | 识别连接相对紧密的子图群组的算法任务。 |
| 10 | Community Summary | 社区摘要 |  | 对知识图某个实体关系群组的主要主题与事实生成的概述。 |
| 11 | Community Report | 社区报告 |  | 对图社区形成可用于问答的结构化描述或总结文档。 |
| 12 | Graph Traversal | 图遍历 |  | 沿知识图节点与边递归或迭代访问相关结构的过程。 |
| 13 | Neighborhood Expansion | 邻域扩展 |  | 从命中实体向一跳或多跳邻接节点扩充证据的策略。 |
| 14 | Graph Path Retrieval | 图路径检索 |  | 通过实体间路径查询建立跨文档关系证据的方式。 |
| 15 | Subgraph Retrieval | 子图检索 |  | 按查询目标抽取局部相关节点、边及属性集合的过程。 |
| 16 | Local Graph Search | 图局部搜索 |  | 以具体实体为中心在邻域中查找相关知识的模式。 |
| 17 | Global Graph Search | 图全局搜索 |  | 依据社区摘要或全局结构回答语料整体性问题的模式。 |
| 18 | Entity-centric Retrieval | 实体中心检索 |  | 从查询涉及的实体出发收集相关记录与关系的策略。 |
| 19 | Relation-aware Retrieval | 关系感知检索 |  | 显式使用实体关系信息判断候选证据相关性的技术。 |
| 20 | Graph Embedding | 图嵌入 |  | 将图节点、边或子图映射为向量表示以支持检索或预测的方法。 |
| 21 | Graph Database | 图数据库 |  | 面向节点、边、属性与图遍历操作的数据管理系统。 |
| 22 | Text-to-Cypher | 文本转 Cypher |  | 将自然语言请求转换为图数据库 Cypher 查询的技术。 |
| 23 | Text-to-SQL | 文本转 SQL |  | 将自然语言查询映射为关系数据库 SQL 语句的技术。 |
| 24 | Structured Retrieval | 结构化检索 |  | 通过模式、字段和查询语言访问表格或图等结构化数据的方式。 |
| 25 | Graph–Text Alignment | 图文对齐 |  | 把图中实体关系与其原始文档证据位置建立对应的机制。 |

## 12. 离线评测、指标与基准测试

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | RAG Evaluation | RAG 系统评测 |  | 分别量化检索质量、证据忠实性、回答相关性与端到端体验的过程。 |
| 2 | Retrieval Evaluation | 检索评测 |  | 利用标注的相关文档判断召回和排序质量的测试。 |
| 3 | Generation Evaluation | 生成评测 |  | 分析模型回答正确性、流畅性、引用支持及任务达成程度的评估。 |
| 4 | End-to-end Evaluation | 端到端评测 |  | 从真实问题输入到最终答案联合衡量 RAG 流程的评价。 |
| 5 | Golden Dataset | 黄金评测数据集 |  | 包含预期答案和必要证据标注、用于回归测试的高质量样本集合。 |
| 6 | Relevance Judgment | 相关性标注 |  | 由人工或约定规则判断文档是否满足查询信息需求的标签。 |
| 7 | Ground Truth | 参考真值 |  | 作为评测依据的经核对答案、相关文档或事实集合。 |
| 8 | Recall at k | 前 k 项召回率 | Recall@k | 前 k 个检索结果覆盖全部标注相关项的比例。 |
| 9 | Precision at k | 前 k 项精确率 | Precision@k | 前 k 个结果中被标注为相关项所占比例。 |
| 10 | Hit Rate at k | 前 k 项命中率 | Hit@k | 前 k 项内是否至少包含一个相关结果的比例或查询平均值。 |
| 11 | Mean Reciprocal Rank | 平均倒数排名 | MRR | 对各查询首个相关结果排名倒数取平均的指标。 |
| 12 | Mean Average Precision | 平均平均精确率 | MAP | 将各查询相关结果位置处精确率求均值后再跨查询平均的指标。 |
| 13 | Normalized Discounted Cumulative Gain | 归一化折损累计增益 | NDCG | 按排名位置折损相关度增益并用理想排序归一化的指标。 |
| 14 | Context Precision | 上下文精确率 |  | 衡量所提供检索上下文中有用证据位置与比例的指标族。 |
| 15 | Context Recall | 上下文召回率 |  | 衡量参考答案必要事实能否从检索上下文中找到的评测维度。 |
| 16 | Faithfulness Metric | 忠实性指标 |  | 测量回答声明受所给证据支持程度的指标。 |
| 17 | Answer Relevance | 答案相关性 |  | 衡量回答是否直接满足用户查询意图的程度。 |
| 18 | Answer Correctness | 答案正确性 |  | 根据参考事实或标准答案判断生成回答对错的指标。 |
| 19 | Citation Accuracy | 引用准确率 |  | 检查引用的来源是否真正支持所对应事实陈述的指标。 |
| 20 | Claim-level Evaluation | 断言级评测 |  | 将回答分解为单条事实主张并逐条核验的方法。 |
| 21 | LLM-as-a-Judge | 大模型裁判 |  | 使用另一语言模型按评分标准评估检索证据或回答的方法。 |
| 22 | Human Evaluation | 人工评测 |  | 由受训标注人员对回答质量与错误类型作出判断的过程。 |
| 23 | RAGAS | RAGAS 评测框架 | RAGAS | 用于评估 RAG 中检索上下文与答案质量的自动化评测工具体系。 |
| 24 | ARES | ARES RAG 评测框架 | ARES | 结合训练式判别模型与人工标注校准评估 RAG 质量的方法。 |
| 25 | Evaluation Leakage | 评测泄漏 |  | 测试答案或标签混入训练、索引或提示而导致指标虚高的情况。 |

## 13. 数据安全、访问控制与可信治理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Retrieval Security | 检索安全 |  | 保障知识库查询、索引和证据传递免受未授权访问或篡改的措施。 |
| 2 | Document-level Access Control | 文档级访问控制 |  | 按用户或角色限制可读取哪些来源文档的权限规则。 |
| 3 | Chunk-level Authorization | 片段级授权 |  | 在检索片段粒度检查请求者是否有权获取该内容。 |
| 4 | Access Control List | 访问控制列表 | ACL | 记录主体对资源允许或拒绝操作的授权规则。 |
| 5 | Role-based Access Control | 基于角色的访问控制 | RBAC | 按预先定义的角色集合决定资源访问权限的机制。 |
| 6 | Attribute-based Access Control | 基于属性的访问控制 | ABAC | 依据用户、资源与环境属性进行权限判定的模型。 |
| 7 | Tenant Isolation | 租户隔离 |  | 防止共享平台中不同租户的数据或检索结果互相泄漏的边界。 |
| 8 | Row-level Security | 行级安全 | RLS | 数据库依据调用者身份或策略过滤可读取记录的功能。 |
| 9 | Pre-filtering | 检索前过滤 |  | 在近邻或全文检索前先用权限或元数据约束候选集合的方法。 |
| 10 | Post-filtering | 检索后过滤 |  | 检索之后对候选结果再执行授权或条件过滤的步骤。 |
| 11 | Permission-aware Retrieval | 权限感知检索 |  | 在召回过程及结果输出中执行用户权限校验的架构。 |
| 12 | Sensitive Information | 敏感信息 |  | 需要按照法律、合同或组织策略限制访问和传播的数据。 |
| 13 | Personally Identifiable Information | 可识别个人身份信息 | PII | 能够直接或结合其他信息识别自然人的数据。 |
| 14 | Data Redaction | 数据脱敏遮盖 |  | 从检索或展示内容中隐藏特定敏感字段的处理。 |
| 15 | Secret Leakage | 机密信息泄漏 |  | 密钥、凭证或不应公开的信息通过检索或生成被意外暴露的事件。 |
| 16 | Prompt Injection | 提示注入 |  | 恶意内容通过输入或外部资料诱导模型违背更高优先级指令的攻击。 |
| 17 | Indirect Prompt Injection | 间接提示注入 |  | 攻击指令藏在被检索文档或工具输出等较低信任内容中的攻击。 |
| 18 | Trust Boundary | 信任边界 |  | 区分高可信指令和低可信外部证据及权限范围的逻辑界线。 |
| 19 | Source Trust Scoring | 来源可信度评分 |  | 依据出处、签名、审核状态等信息评估来源可靠性的机制。 |
| 20 | Content Poisoning | 内容投毒 |  | 攻击者通过操控可检索文档使召回或生成产生误导结果的行为。 |
| 21 | Index Poisoning | 索引投毒 |  | 攻击者向搜索索引插入或操纵条目影响检索结果的攻击。 |
| 22 | Cited-source Spoofing | 引用来源伪造 |  | 构造虚假来源标识或引文诱骗系统采信错误资料的行为。 |
| 23 | Audit Logging | 审计日志记录 |  | 记录索引、授权、检索和回答事件以支持安全追溯的机制。 |
| 24 | Data Retention Policy | 数据保留策略 |  | 规定知识内容和日志应保存多久及如何到期删除的规则。 |
| 25 | Right-to-deletion Workflow | 删除请求执行流程 |  | 将合法删除请求传播到原文、缓存、向量索引和备份的治理程序。 |

## 14. 生产工程、性能与持续优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Production RAG | 生产级 RAG |  | 满足可用性、安全、成本、监控及版本管理要求的线上检索增强系统。 |
| 2 | Retrieval Latency | 检索延迟 |  | 从发起检索到获得候选结果之间的耗时。 |
| 3 | End-to-end Response Time | 端到端响应时间 |  | 从收到用户请求到最终回答完成的总时间。 |
| 4 | Time to First Token | 首 token 延迟 | TTFT | 从开始生成请求到模型输出第一个 token 所需的时间。 |
| 5 | Tail Latency | 尾部延迟 |  | 响应时间分布高百分位、用于描述慢请求体验的指标。 |
| 6 | Throughput | 吞吐量 |  | 系统单位时间内处理的查询或生成请求数量。 |
| 7 | Concurrency Limit | 并发限制 |  | 为检索和生成服务设置同时处理请求数量的上界。 |
| 8 | Rate Limiting | 速率限制 |  | 通过令牌桶等机制限制调用频率以控制负载的措施。 |
| 9 | Retrieval Cache | 检索缓存 |  | 复用近期或相同查询的候选文档结果以减少计算的缓存。 |
| 10 | Embedding Cache | 嵌入缓存 |  | 复用已计算查询或文档向量以节省嵌入推理成本的缓存。 |
| 11 | Semantic Cache | 语义缓存 |  | 对含义接近的请求复用经验证结果的缓存策略。 |
| 12 | Cache Invalidation | 缓存失效 |  | 在权限、数据版本或模型版本变化时使旧缓存不再使用的过程。 |
| 13 | Index Refresh | 索引刷新 |  | 按数据变更或时效要求更新检索索引内容的操作。 |
| 14 | Blue–Green Index Deployment | 蓝绿索引发布 |  | 并行维护新旧两套索引并在验证后切换查询流量的发布方式。 |
| 15 | Shadow Index Testing | 影子索引测试 |  | 将真实查询并行送入候选新索引但不影响用户回答的验证方式。 |
| 16 | A/B Testing | A/B 测试 |  | 随机分配流量比较两种检索或生成策略对业务指标的影响。 |
| 17 | Canary Deployment | 金丝雀发布 |  | 把少量流量先导入新方案以观察风险后逐步扩大的策略。 |
| 18 | Embedding Migration | 嵌入模型迁移 |  | 更换编码器时对文档重新向量化、索引和切换查询的过程。 |
| 19 | Index Versioning | 索引版本管理 |  | 记录索引配置、数据快照和构建时间以支持回滚的机制。 |
| 20 | Pipeline Observability | 流水线可观测性 |  | 跟踪每阶段输入、耗时、错误与质量指标的运维能力。 |
| 21 | Retrieval Trace | 检索链路追踪 |  | 记录查询改写、索引访问、候选得分与排序过程的调试轨迹。 |
| 22 | Cost per Query | 单次查询成本 |  | 按检索、嵌入、重排和生成资源计算的平均请求成本。 |
| 23 | Quality–Cost Tradeoff | 质量—成本权衡 |  | 在召回、答案质量与推理或基础设施开销之间选择平衡方案。 |
| 24 | Feedback-driven Improvement | 反馈驱动改进 |  | 依据人工纠错、用户反馈及评测数据迭代优化检索与生成的流程。 |
| 25 | Retrieval Regression Test | 检索回归测试 |  | 在数据、模型或索引修改后验证关键查询仍返回必要证据的测试。 |

## 核心概念辨析

| 对比术语 | 核心区别与限制 |
|---|---|
| RAG 与微调 | RAG 在推理时访问外部知识；微调通过训练改变模型参数。两者可结合，RAG 不保证纠正模型固有推理错误。 |
| Embedding 检索与 BM25 | Embedding 擅长发现表达不同的语义关联；BM25 强调字面词项匹配，专有名词和标识符可能更适合词法检索。 |
| 稀疏检索与稠密检索 | 稀疏向量大部分维度为零；稠密向量多数维度非零。这是表示差异，并不直接决定检索质量。 |
| Bi-encoder 与 Cross-encoder | 双编码器可分别预编码文档，适合大规模召回；交叉编码器联合处理查询文档对，常用于候选重排序。 |
| 精确近邻与 ANN | 精确近邻返回按指定距离真正最近的候选；ANN 通过近似索引加速搜索，可能遗漏精确最近邻。 |
| Recall@k 与 Precision@k | Recall@k 是 top-k 命中相关文档数除以全部相关文档数；Precision@k 则除以 k。两者分母不同。 |
| 相关性与忠实性 | 检索片段与问题高度相关，并不意味着生成的每个断言都能从片段推出；需要独立检查证据支持。 |
| RRF 与分数加权融合 | RRF 用排名位置融合，不直接依赖各检索器分数的可比性；加权分数融合通常需要校准。 |
| 切块重叠与父子检索 | 重叠切块保留邻近文本但增大索引冗余；父子检索用小片段定位后返回更大上下文。 |
| Self-RAG 与 CRAG | Self-RAG 通过学习反思信号决定检索并评判输出；CRAG 重点根据检索质量触发纠错策略。二者不是同一通用标准。 |
| GraphRAG 与普通向量 RAG | GraphRAG 将实体关系及社区结构用于检索或汇总，适合关系和整体概览任务；成本与数据质量要求因实现而异。 |
| 拒答与幻觉 | 证据不足时明确拒答可能牺牲部分回答覆盖，但比生成无证据断言更符合高可靠性任务目标。 |
| 权限过滤与提示防护 | 文档 ACL 和查询时授权属于数据访问层控制；提示词中的安全要求不能替代后端强制权限校验。 |
| 离线检索评价与线上业务评价 | 离线指标量化标注集上的召回排序；线上指标还受延迟、成本、用户行为和数据变化影响。 |

## 中等难度面试问答

### 面试题 1. 为什么把切块大小统一设为 1,000 token 并不能保证效果最优？

**参考答案：**不同语料的语义单元、表格与上下文依赖不同；需要同时衡量检索召回、证据完整性、冗余与生成质量，通过验证集选择。

### 面试题 2. 什么时候先选 BM25 而不是稠密检索？

**参考答案：**精确产品型号、错误码、订单号、代码符号等词形极关键时，BM25 或精确字段匹配更稳定；可与语义检索融合。

### 面试题 3. 为什么只检查 ANN 索引召回率不能说明 RAG 已经准确？

**参考答案：**ANN 召回是对精确向量最近邻的重合度；语义相关标注、证据覆盖以及生成忠实性是不同目标，需要独立测量。

### 面试题 4. 为什么多个检索器的分数不能不加处理直接求和？

**参考答案：**BM25 与余弦相似度的数值范围和分布不同，直接求和会被尺度主导；可用分数归一化或 RRF 等名次融合。

### 面试题 5. 如何处理一个问题需要从两份合同找到相互引用的条款？

**参考答案：**先拆解成子查询定位第一份条款及引用键，再按引用键查询第二份并保留来源位置，最终校验两段证据的关联。

### 面试题 6. RAG 返回文档链接为什么仍可能出现伪引用？

**参考答案：**仅有链接并不说明链接内容支持特定断言；需要在断言级验证原文片段、时间与适用条件。

### 面试题 7. 用户 A 能否用共享向量数据库查询用户 B 文档，即使生成提示要求模型不泄漏？

**参考答案：**不能依赖提示词。必须在索引或检索服务执行租户隔离和权限过滤，同时避免跨租户缓存复用。

### 面试题 8. 如何评估引用准确性与回答正确性的区别？

**参考答案：**引用准确性检验引用是否支持句子；回答正确性检验答案是否符合外部事实或参考真值。错误来源也可能支持错误答案。

### 面试题 9. 为什么 Self-RAG 和 CRAG 不应被当作任意 RAG 系统默认具备的功能？

**参考答案：**两者源于具体研究设计，分别涉及训练的反思机制或检索纠错流程；通用 RAG 不自动包含这些模块。

### 面试题 10. 向量模型升级为什么往往需要重建索引？

**参考答案：**不同模型的维度、坐标语义和归一化方式可能不兼容；新查询向量通常不能可靠匹配旧文档向量。

## 中等难度考试题与解析

### 考试题 1. 某查询共有 8 个标注相关文档，top-5 返回 3 个相关文档。计算 Recall@5 与 Precision@5。

**解析：**Recall@5=3/8=0.375；Precision@5=3/5=0.60。

### 考试题 2. 三个查询首个相关文档排名分别为 1、2、4。计算 MRR。

**解析：**MRR=(1+1/2+1/4)/3=7/12≈0.5833。

### 考试题 3. 使用 k=60 的 RRF，一份文档分别位列两个检索器的第 1 和第 3，求得分。

**解析：**1/(60+1)+1/(60+3)=1/61+1/63≈0.03226。

### 考试题 4. 上下文上限 8,192 token，系统与用户问题预留 1,024，输出预留 2,048，最多还能放多少检索文本？

**解析：**忽略额外格式标记和内部开销时，8,192−1,024−2,048=5,120 token。

### 考试题 5. 一个向量索引在 100 次查询中累计应返回 1,000 个精确前十邻居，实际命中 920 个，ANN Recall@10 多少？

**解析：**按累计命中定义为 920/1,000=0.92；这不是人工标注相关性召回。

### 考试题 6. 把 10 个文档每份各切成 8 个块、相邻块重叠 100 token，实际索引块数多少？

**解析：**不考虑空块和特殊过滤条件时是 10×8=80 块；重叠增加存储文本量但不改变该数量。

### 考试题 7. 某答案包含 5 条独立事实断言，其中 4 条由证据支持，按简单断言支持率定义忠实性是多少？

**解析：**支持率 4/5=0.8。真实评测需要定义声明拆分与支持判定规则。

### 考试题 8. 向量库包含 100 万条公司文档，某用户只可访问 10 万条。为何不能先返回全球 top-10 再过滤？

**解析：**这样可使授权集合中的高分证据被未授权结果挤出，导致召回严重下降；应尽可能在检索候选生成前或过程中执行授权过滤。

### 考试题 9. 知识库昨晚更新但用户拿到上周答案，最先检查哪几类版本信息？

**解析：**对比来源文档版本、摄入时间、索引更新时间、查询路由目标及缓存键/失效记录，定位陈旧数据环节。

### 考试题 10. 某检索候选前五条重复呈现相同条款，且另一个必要条款未出现，优先考虑什么改进？

**解析：**增加结果去重或 MMR 多样化，并评估分解检索、父子检索和重排序；用证据覆盖而非单纯 top-k 得分衡量效果。

## 主要论文与官方资料

以下来源支持相应研究主题与术语边界，引用不意味着研究作者参与或认可本项目术语逐条审查。

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

## 维护说明

- 原始术语：`data/rag/chapters/*.tsv`（`English|中文|abbr|definition`）。
- 导出文件：`data/rag.tsv`、`glossaries/rag.md`、`pdf/rag.pdf`，以及相同内容的 `docs/` 镜像。
- 构建与核验：`node scripts/render_rag.mjs` / `node scripts/render_rag.mjs --check`。
- 本册是独立出版物，**尚未加入全站术语搜索索引**，也未构建 350 篇长篇 Wiki。
