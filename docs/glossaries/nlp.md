# 自然语言处理 · Natural Language Processing (NLP)

> TERM / ATLAS · 中英文专业术语手册 | Bilingual Technical Glossary

**500 条术语 · 20 个专业章节 · 2026-11-27**

知识体系覆盖计算语言学、语料库与数据标注、词元化与形态学、句法及语义、统计 NLP、词嵌入、RNN 与 Transformer、预训练语言模型、微调、NER、问答、机器翻译、摘要、语音与多模态语言处理、基准评测及生产治理。

**适用范围：**NLP 的语言学概念、神经模型、数据格式及评测协议各有特定前提；不应把词元与词语、抽取式与生成式任务、自动指标与事实正确性混为一谈。

**审稿说明：**已自动检查原始条目的字段结构、数量和英文主术语唯一性；独立领域专家逐条事实审稿与 PDF 视觉验收尚未完成。

## 章节目录

- 01. NLP 领域概述与语言处理层次（25 条）
- 02. 语料库、数据标注与语言资源（25 条）
- 03. 文本规范化、分词与子词编码（25 条）
- 04. 词形学、词汇语义与词典资源（25 条）
- 05. 句法分析、依存结构与语法表示（25 条）
- 06. 语义表示、语用与篇章理解（25 条）
- 07. 统计语言模型、N-gram 与概率推断（25 条）
- 08. 特征工程、判别模型与序列分类（25 条）
- 09. 词向量、分布式语义与表示学习（25 条）
- 10. 神经序列模型、编码器与解码器（25 条）
- 11. 注意力机制与 Transformer 结构（25 条）
- 12. 预训练语言模型与自监督目标（25 条）
- 13. 下游适配、监督微调与迁移学习（25 条）
- 14. 实体识别、序列标注与信息抽取（25 条）
- 15. 问答、文档检索与文本匹配（25 条）
- 16. 机器翻译、跨语言迁移与多语建模（25 条）
- 17. 文本生成、摘要、对话与解码控制（25 条）
- 18. 语音语言接口与多模态 NLP（25 条）
- 19. NLP 指标、基准与误差分析（25 条）
- 20. 可靠性、数据治理与生产部署（25 条）

---

## 01. NLP 领域概述与语言处理层次

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Natural Language Processing | 自然语言处理 | NLP | 研究计算机理解、分析与生成人类语言的方法及应用。 |
| 2 | Computational Linguistics | 计算语言学 | CL | 使用计算模型研究语言结构、使用与处理的交叉学科。 |
| 3 | Language Understanding | 语言理解 | NLU | 从文本或语音中推断语义、意图及相关信息的任务集合。 |
| 4 | Natural Language Generation | 自然语言生成 | NLG | 把数据、结构或语义表示转换为自然语言表达的任务。 |
| 5 | Language Technology | 语言技术 |  | 用于语言信息处理、翻译、检索和交互的软件与模型技术总称。 |
| 6 | Text Analytics | 文本分析 |  | 从非结构化文本中抽取统计、主题、关系和其他可用信息的过程。 |
| 7 | Speech and Language Processing | 语音与语言处理 |  | 联合研究语音信号与语言形式及意义的计算领域。 |
| 8 | Linguistic Level | 语言分析层次 |  | 把语言现象划分为语音、形态、句法、语义和语用等不同研究层级的概念。 |
| 9 | Phonetics | 语音学 |  | 研究语音声音的物理产生、传播和感知的学科。 |
| 10 | Phonology | 音系学 |  | 研究语言中区别意义的语音组织规则及音位系统的学科。 |
| 11 | Morphology | 形态学 |  | 研究词的内部构成及词形变化规则的语言学分支。 |
| 12 | Syntax | 句法学 |  | 研究词语如何组合为短语和句子的结构与规则。 |
| 13 | Semantics | 语义学 |  | 研究词语、短语和句子的语言意义及其组合关系。 |
| 14 | Pragmatics | 语用学 |  | 研究话语在特定情境中如何传达超出字面形式的交际意义。 |
| 15 | Discourse Analysis | 篇章分析 |  | 分析跨句子结构、衔接与交际目的的语言研究方法。 |
| 16 | Corpus Linguistics | 语料库语言学 |  | 利用大量真实语言材料统计研究语言规律的方法。 |
| 17 | Language Modeling | 语言建模 |  | 为词元序列及其条件延续分配概率或预测分数的任务。 |
| 18 | Text Classification | 文本分类 |  | 把文本映射到预定义类别或标签集合的任务。 |
| 19 | Sequence Labeling | 序列标注 |  | 为输入序列各个位置预测相应标签的任务。 |
| 20 | Machine Translation | 机器翻译 | MT | 把源语言的内容自动转换为目标语言表达的任务。 |
| 21 | Question Answering | 问答 | QA | 根据问题和可用知识或证据生成或抽取答案的任务。 |
| 22 | Information Extraction | 信息抽取 | IE | 从文本中识别实体、事件、属性及关系并形成结构化结果的任务。 |
| 23 | Dialogue System | 对话系统 |  | 通过多轮语言交互理解用户并产生回应的系统。 |
| 24 | Text Summarization | 文本摘要 |  | 将一篇或多篇文本压缩为保留关键信息的简要表达的任务。 |
| 25 | Multilingual NLP | 多语言自然语言处理 |  | 研究跨多种语言构建、训练和评估语言处理模型的方法。 |

## 02. 语料库、数据标注与语言资源

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Text Corpus | 文本语料库 |  | 用于统计分析、训练或评测的文本资料集合。 |
| 2 | Parallel Corpus | 平行语料库 |  | 含不同语言间对应句段或文档配对的语料集合。 |
| 3 | Monolingual Corpus | 单语语料库 |  | 主要包含同一种语言文本的语料集合。 |
| 4 | Comparable Corpus | 可比语料库 |  | 不同语言或领域主题相似但未逐句对齐的文本集合。 |
| 5 | Annotated Corpus | 标注语料库 |  | 包含实体、句法、情感等人工或程序标签的文本集合。 |
| 6 | Raw Corpus | 原始语料库 |  | 尚未经过目标任务特定标注和深度清洗的语言数据集合。 |
| 7 | Treebank | 句法树库 |  | 为句子标注成分树或依存关系等句法结构的语料资源。 |
| 8 | Universal Dependencies | 通用依存关系框架 | UD | 提供跨语言词性、形态特征和依存句法标注规范的项目体系。 |
| 9 | CoNLL Format | CoNLL 数据格式 |  | 用于序列标注、句法分析等共享任务的若干结构化文本格式。 |
| 10 | CoNLL-U | 通用依存关系文件格式 | CoNLL-U | 用于 UD 标注的以行为词元、以列描述词性与依存关系的数据格式。 |
| 11 | Dataset Split | 数据集划分 |  | 将样本分配到训练、验证和测试等用途的过程。 |
| 12 | Training Set | 训练集 |  | 用于优化模型参数或学习统计模式的数据子集。 |
| 13 | Validation Set | 验证集 |  | 用于模型选择、超参数调优与训练期间监控的独立数据子集。 |
| 14 | Test Set | 测试集 |  | 用于训练完成后估计泛化性能的保留评估数据子集。 |
| 15 | Annotation Guideline | 标注指南 |  | 规定标签定义、边界判断和例外处理的一套标注规则。 |
| 16 | Annotation Schema | 标注模式 |  | 定义任务标签种类、层级、关系与数据结构的规范。 |
| 17 | Inter-annotator Agreement | 标注者间一致性 |  | 衡量不同标注者对相同语料标注结果一致程度的指标。 |
| 18 | Cohen Kappa | 科恩 Kappa 系数 | κ | 对两个标注者分类一致程度进行机会一致性校正的统计量。 |
| 19 | Fleiss Kappa | 弗莱斯 Kappa 系数 |  | 对多个标注者的分类一致程度进行机会校正的统计量。 |
| 20 | Krippendorff Alpha | 克里彭多夫 Alpha 系数 | α | 可用于多名标注者和多种测量尺度的一致性指标。 |
| 21 | Annotation Adjudication | 标注仲裁 |  | 对存在分歧的标签进行复核并确定最终参考标签的流程。 |
| 22 | Data Provenance | 数据来源溯源 |  | 记录语料出处、许可、采集方式和修改历史的元数据。 |
| 23 | Data Contamination | 数据污染 |  | 训练数据包含测试答案或其他本不应泄漏内容导致评测失真的现象。 |
| 24 | Domain Shift | 领域分布偏移 |  | 训练和实际应用中语言主题、风格或数据来源发生变化的现象。 |
| 25 | Corpus Sampling | 语料抽样 |  | 按明确采样方案从目标语言材料中选择文本作为数据集的过程。 |

## 03. 文本规范化、分词与子词编码

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Text Normalization | 文本规范化 |  | 把文本中编码、数字、缩写或书写变体转换为一致表示的过程。 |
| 2 | Sentence Segmentation | 句子切分 |  | 识别文本中的句子或语句边界的处理。 |
| 3 | Word Segmentation | 词语切分 |  | 将连续文本划分为语言词语单位的任务，在中文等语言中尤为重要。 |
| 4 | Tokenization | 词元化 |  | 依据词表或规则将字符串分解为模型处理的 token 序列。 |
| 5 | Token | 词元 | Token | 文本编码器定义的离散处理单元，可为词、子词、字符或特殊符号。 |
| 6 | Tokenizer | 词元切分器 |  | 把文本映射为 token 或 token ID 序列的规则或模型。 |
| 7 | Subword Tokenization | 子词切分 |  | 把文本划分为比完整词更细且可重用的子词单位的编码方式。 |
| 8 | Byte Pair Encoding | 字节对编码 | BPE | 通过迭代合并高频相邻符号学习子词词表的编码算法族。 |
| 9 | WordPiece | WordPiece 子词算法 | WordPiece | 依据训练目标或统计准则学习子词词表的词元化方法。 |
| 10 | Unigram Language Model Tokenization | 一元语言模型子词切分 | Unigram | 从候选子词词表中按概率模型选择切分的编码方法。 |
| 11 | SentencePiece | SentencePiece 词元化工具 |  | 直接处理原始文本并支持 BPE 与 Unigram 等编码方法的子词框架。 |
| 12 | Byte-level Tokenization | 字节级词元化 |  | 以 UTF-8 字节等低层编码单元表示文本并构建词元序列的方案。 |
| 13 | Character-level Tokenization | 字符级词元化 |  | 以 Unicode 字符或相近字符单位作为基本编码单元的方法。 |
| 14 | Whitespace Tokenization | 空白符切分 |  | 利用空格和制表符等分隔符划分词元的简单规则。 |
| 15 | Vocabulary | 词表 |  | 编码器允许表示的 token 与特殊符号的有限集合。 |
| 16 | Vocabulary Size | 词表大小 |  | 词元编码系统中可使用的不同 token 数量。 |
| 17 | Token ID | 词元编号 |  | 将某个词元映射到模型词表中的整数索引。 |
| 18 | Out-of-vocabulary Word | 词表外词 | OOV | 在当前词表中没有对应完整条目的词或符号。 |
| 19 | Unknown Token | 未知词元 | UNK | 某些编码器用于代表未收录词或符号的特殊 token。 |
| 20 | Special Token | 特殊词元 |  | 表示开始、结束、填充或任务控制等非普通文字含义的词元。 |
| 21 | Padding Token | 填充词元 | PAD | 把不同长度样本补齐为统一张量尺寸时使用的占位 token。 |
| 22 | Beginning-of-sequence Token | 序列起始词元 | BOS | 标记输入或生成序列开始位置的特殊 token。 |
| 23 | End-of-sequence Token | 序列结束词元 | EOS | 标记序列结束、可用于终止生成的特殊 token。 |
| 24 | Unicode Normalization | Unicode 规范化 |  | 按照 NFC、NFKC 等规则统一等价字符编码表示的过程。 |
| 25 | Detokenization | 逆词元化 |  | 把生成或标注的词元序列还原为可阅读文本的过程。 |

## 04. 词形学、词汇语义与词典资源

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Morpheme | 语素 |  | 语言中携带意义或语法功能的最小构词单位。 |
| 2 | Morphological Analysis | 词形分析 |  | 把词分解为词根、词缀和词形特征等内部结构的过程。 |
| 3 | Lemma | 词元基本形 |  | 词典中代表某一词形变化集合的规范词形。 |
| 4 | Lemmatization | 词形还原 |  | 根据词汇和形态规则把屈折词形转换为基本形的处理。 |
| 5 | Stemming | 词干提取 |  | 通过截断或规则把词形变体简化为共同词干的处理。 |
| 6 | Inflection | 屈折变化 |  | 表达时态、数、格等语法信息而通常不改变词项类别的词形变化。 |
| 7 | Derivation | 派生构词 |  | 通过词缀或其他手段产生具有新词汇意义的词的过程。 |
| 8 | Prefix | 前缀 |  | 附着在词根前、改变词义或语法功能的构词单位。 |
| 9 | Suffix | 后缀 |  | 附着在词根后、表达构词或屈折信息的构词单位。 |
| 10 | Compound Word | 复合词 |  | 由两个或更多词根或词构成的词汇单位。 |
| 11 | Part-of-speech | 词性 | POS | 按照词的句法与形态行为划分的名词、动词等语法类别。 |
| 12 | Lexeme | 词位 |  | 将词形变体归为同一抽象词汇单位的语言学概念。 |
| 13 | Lexicon | 词典知识库 |  | 记录词项形式、语义、词性和其他词汇特征的数据资源。 |
| 14 | Word Sense | 词义项 |  | 多义词在特定语境下表达的一种可区分意义。 |
| 15 | Polysemy | 一词多义 |  | 同一个词形承载多个相关意义的语言现象。 |
| 16 | Homonymy | 同形同音异义 |  | 相同书写或发音形式对应彼此无关意义的现象。 |
| 17 | Synonymy | 同义关系 |  | 不同词项在一定语境中意义相同或接近的语义关系。 |
| 18 | Antonymy | 反义关系 |  | 两个词项在某一语义维度上表达对立意义的关系。 |
| 19 | Hypernymy | 上位词关系 |  | 较一般概念包含较具体概念实例的词汇语义关系。 |
| 20 | Hyponymy | 下位词关系 |  | 较具体概念属于某较一般概念类别的语义关系。 |
| 21 | Meronymy | 部分—整体关系 |  | 一个实体或概念是另一整体组成部分的语义关系。 |
| 22 | WordNet | WordNet 词汇语义网络 |  | 以同义词集及语义关系组织英文词汇知识的语言资源。 |
| 23 | Synset | 同义词集 | Synset | WordNet 等资源中共同指向一个词义概念的词集合。 |
| 24 | Word Sense Disambiguation | 词义消歧 | WSD | 根据上下文判断多义词所用具体词义的任务。 |
| 25 | Morphological Tagging | 形态特征标注 |  | 为词元预测数、性、格、时态等语法形态属性的任务。 |

## 05. 句法分析、依存结构与语法表示

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Syntactic Parsing | 句法分析 |  | 根据语法规则推断句子的组成关系或词间依存结构的任务。 |
| 2 | Constituency Parsing | 成分句法分析 |  | 把句子组织为嵌套短语节点的树形结构分析。 |
| 3 | Dependency Parsing | 依存句法分析 |  | 预测词与词之间以中心词和依存关系构成的结构。 |
| 4 | Constituency Tree | 成分句法树 |  | 以短语非终结符与词项终结符表示句子层级结构的树。 |
| 5 | Dependency Tree | 依存句法树 |  | 以词为节点、依存边表示语法支配关系的树结构。 |
| 6 | Head Word | 中心词 |  | 在短语或依存结构中决定主要句法性质的词。 |
| 7 | Dependent | 依存词 |  | 在依存分析中通过语法边连接到中心词的词元。 |
| 8 | Dependency Relation | 依存关系标签 |  | 表示词与中心词之间主语、宾语、修饰等语法关系的类别。 |
| 9 | Dependency Arc | 依存弧 |  | 从一个中心词指向其依存词的有向语法边。 |
| 10 | Projective Dependency Tree | 投射依存树 |  | 在词序上依存边能够满足特定不交叉条件的依存树。 |
| 11 | Non-projective Dependency Tree | 非投射依存树 |  | 含有跨越结构、无法用简单投射树表示的依存结构。 |
| 12 | Transition-based Parsing | 基于转移的句法分析 |  | 通过堆栈、缓冲区和一系列转移动作构建句法树的方法。 |
| 13 | Graph-based Parsing | 基于图的句法分析 |  | 在候选语法边或结构的评分空间中搜索最佳句法树的方法。 |
| 14 | Context-free Grammar | 上下文无关文法 | CFG | 产生式左侧只有一个非终结符的形式文法。 |
| 15 | Probabilistic Context-free Grammar | 概率上下文无关文法 | PCFG | 为 CFG 产生式赋予概率并推断解析树的文法模型。 |
| 16 | Production Rule | 产生式规则 |  | 说明非终结符可替换为哪些符号序列的形式语法规则。 |
| 17 | Nonterminal Symbol | 非终结符 |  | 表示可继续展开的语法类别或短语类别的文法符号。 |
| 18 | Terminal Symbol | 终结符 |  | 形式文法中不再由产生式展开的基本符号。 |
| 19 | Parse Chart | 解析图表 |  | 保存子串或跨度解析结果以避免重复计算的动态规划结构。 |
| 20 | CKY Algorithm | CKY 句法分析算法 | CKY | 在适当文法范式下利用区间动态规划寻找成分解析结构的算法。 |
| 21 | Earley Parser | Earley 解析器 |  | 使用预测、扫描和完成操作处理上下文无关文法的图表解析算法。 |
| 22 | Head-driven Phrase Structure Grammar | 中心词驱动短语结构语法 | HPSG | 结合特征结构与类型约束描述词汇和句法的形式语法理论。 |
| 23 | Combinatory Categorial Grammar | 组合范畴语法 | CCG | 用词汇范畴和组合规则统一描述句法与语义组合的语法理论。 |
| 24 | Grammatical Agreement | 语法一致关系 |  | 词语在数、性、人称等语法特征上满足一致约束的现象。 |
| 25 | Syntactic Ambiguity | 句法歧义 |  | 同一句子能够获得多个合理句法结构或附着关系的现象。 |

## 06. 语义表示、语用与篇章理解

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Compositional Semantics | 组合语义 |  | 通过子表达式意义及其组合方式计算整体意义的理论。 |
| 2 | Semantic Parsing | 语义解析 |  | 把自然语言转换为逻辑形式、程序或其他结构化语义表示的任务。 |
| 3 | Logical Form | 逻辑形式 |  | 使用符号表达式描述话语真值条件或关系结构的表示。 |
| 4 | Predicate–Argument Structure | 谓词—论元结构 |  | 描述事件或状态谓词及其参与实体语义角色的结构。 |
| 5 | Semantic Role Labeling | 语义角色标注 | SRL | 识别谓词关联参与者并分配施事、受事等语义角色的任务。 |
| 6 | Agent Role | 施事角色 |  | 语义角色体系中主动发起或控制事件的参与者。 |
| 7 | Patient Role | 受事角色 |  | 在事件中受到动作影响或状态改变的参与者。 |
| 8 | Thematic Role | 题元角色 |  | 用来表征事件参与者语义功能的角色类别。 |
| 9 | Coreference Resolution | 共指消解 |  | 识别文本中哪些提及指向同一实体的任务。 |
| 10 | Anaphora Resolution | 回指消解 |  | 确定代词或其他回指表达与先前语言单位对应关系的任务。 |
| 11 | Entity Mention | 实体提及 |  | 文本中指向某个实体的一个词语或连续片段。 |
| 12 | Discourse Relation | 篇章关系 |  | 表示句段之间因果、对比、解释和条件等连贯关系的语义关系。 |
| 13 | Discourse Coherence | 篇章连贯性 |  | 文本不同部分在主题、指代和逻辑组织上形成整体意义的性质。 |
| 14 | Discourse Representation Theory | 篇章表示理论 | DRT | 利用篇章表示结构描述量词、指代和跨句语义的理论。 |
| 15 | Presupposition | 预设 |  | 话语中被当作背景已知或默认成立的命题内容。 |
| 16 | Implicature | 会话含义 |  | 说话者借助语境和交际原则传递、未直接编码的附加意义。 |
| 17 | Entailment | 语义蕴含 |  | 一个命题成立时能够逻辑保证另一命题成立的关系。 |
| 18 | Contradiction | 语义矛盾 |  | 两个命题在同一解释条件下不可能同时为真的关系。 |
| 19 | Natural Language Inference | 自然语言推断 | NLI | 判断前提对假设构成蕴含、矛盾或中立关系的任务。 |
| 20 | Textual Entailment | 文本蕴含 |  | 判断一个文本陈述能否支持另一个陈述成立的语义推断问题。 |
| 21 | Semantic Similarity | 语义相似度 |  | 衡量两个文本片段意义接近程度的数值或等级。 |
| 22 | Semantic Textual Similarity | 语义文本相似度 | STS | 为两个文本的语义等价或接近程度预测连续评分的任务。 |
| 23 | Semantic Frame | 语义框架 |  | 以事件或情境及其角色组织词汇意义的知识表示。 |
| 24 | FrameNet | FrameNet 语义框架资源 |  | 按语义框架与框架元素标注词汇使用的语言知识库。 |
| 25 | Pragmatic Context | 语用语境 |  | 影响话语解释的说话者意图、对话历史和社会情境信息。 |

## 07. 统计语言模型、N-gram 与概率推断

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | N-gram | N 元语法片段 | N-gram | 由连续 N 个词元构成的序列特征。 |
| 2 | Unigram Model | 一元语言模型 |  | 把词元独立或按边际频率建模的简单概率模型。 |
| 3 | Bigram Model | 二元语言模型 |  | 使用前一个词元预测当前词元概率的语言模型。 |
| 4 | Trigram Model | 三元语言模型 |  | 使用前两个词元预测当前词元的语言模型。 |
| 5 | Markov Assumption | 马尔可夫假设 |  | 假定当前状态或词元仅依赖有限历史状态的近似条件。 |
| 6 | Chain Rule of Probability | 概率链式法则 |  | 将序列联合概率表示为各位置条件概率乘积的恒等式。 |
| 7 | Conditional Probability | 条件概率 |  | 在给定某事件或上下文条件下另一事件成立的概率。 |
| 8 | Maximum Likelihood Estimation | 极大似然估计 | MLE | 选择使观察语料概率达到最大值的模型参数估计原则。 |
| 9 | Count-based Language Model | 计数型语言模型 |  | 通过统计离散词元和上下文共现次数估计序列概率的模型。 |
| 10 | Sparse Data Problem | 数据稀疏问题 |  | 训练样本中大量可能的词序列未出现、使概率估计不稳的现象。 |
| 11 | Smoothing | 概率平滑 |  | 重新分配计数模型概率质量以处理未见或低频事件的方法。 |
| 12 | Add-one Smoothing | 加一平滑 | Laplace | 为每种词项计数加一的简单平滑估计技术。 |
| 13 | Add-k Smoothing | 加 k 平滑 |  | 为每个事件计数加入正伪计数 k 的估计方法。 |
| 14 | Good–Turing Estimation | 古德—图灵估计 |  | 依据事件频次的频次数目调整低频与未见事件概率的技术。 |
| 15 | Backoff Language Model | 回退语言模型 |  | 高阶上下文统计不足时退回低阶语言模型估计的策略。 |
| 16 | Interpolation | 概率插值 |  | 通过加权组合不同阶数或不同来源的概率估计缓解稀疏性的方法。 |
| 17 | Kneser–Ney Smoothing | 克内瑟—内伊平滑 |  | 利用折扣和不同历史上下文多样性构造高质量 N-gram 平滑概率的方法。 |
| 18 | Modified Kneser–Ney | 改进 Kneser–Ney 平滑 |  | 根据计数大小采用不同折扣的 Kneser–Ney 估计变体。 |
| 19 | Discounting | 计数折扣 |  | 从已见事件计数中扣除部分概率质量以分配给其他事件的方法。 |
| 20 | Perplexity | 困惑度 | PPL | 模型在给定 tokenization 下平均负对数似然的指数，用于评价预测不确定性。 |
| 21 | Cross Entropy | 交叉熵 |  | 按真实分布或数据样本对模型对数概率取负期望的量。 |
| 22 | Entropy Rate | 熵率 |  | 随机过程每个新符号在无限历史条件下的平均信息量。 |
| 23 | Hidden Markov Model | 隐马尔可夫模型 | HMM | 通过潜在状态转移与观测发射概率建模序列的概率模型。 |
| 24 | Viterbi Algorithm | 维特比算法 |  | 对状态序列概率模型用动态规划寻找概率最大路径的算法。 |
| 25 | Forward–Backward Algorithm | 前向—后向算法 |  | 通过双向动态规划计算 HMM 等模型隐状态边际概率的算法。 |

## 08. 特征工程、判别模型与序列分类

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Bag-of-words | 词袋模型 | BoW | 忽略词序、用词频或二值特征表示文本的模型。 |
| 2 | Term Frequency | 词频 | TF | 某个词项在文档中出现的次数或归一化次数。 |
| 3 | Inverse Document Frequency | 逆文档频率 | IDF | 反映词项在文档集合中相对稀有程度的统计权重。 |
| 4 | TF–IDF | 词频—逆文档频率 | TF-IDF | 结合文档词频与全语料稀有度构建词项权重的表示。 |
| 5 | Feature Extraction | 特征提取 |  | 把文本变成可供统计模型处理的数值或符号特征的过程。 |
| 6 | Feature Hashing | 特征哈希 |  | 使用哈希函数将高维离散特征映射到固定维度空间的方法。 |
| 7 | Character N-gram Feature | 字符 N 元组特征 |  | 通过连续字符子串捕获词形与拼写信息的文本特征。 |
| 8 | Lexical Feature | 词汇特征 |  | 基于词项、词形或词典匹配而构造的分类或标注输入特征。 |
| 9 | Contextual Feature | 上下文特征 |  | 反映当前词元邻近词和其他上下文信息的模型特征。 |
| 10 | Naive Bayes Classifier | 朴素贝叶斯分类器 | NB | 在给定类别时假设特征条件独立的概率分类模型。 |
| 11 | Multinomial Naive Bayes | 多项式朴素贝叶斯 |  | 对词频或离散计数使用多项式生成假设的朴素贝叶斯模型。 |
| 12 | Bernoulli Naive Bayes | 伯努利朴素贝叶斯 |  | 以特征是否出现的二元变量构造似然的朴素贝叶斯模型。 |
| 13 | Logistic Regression | 逻辑回归 |  | 通过线性打分与 logistic 或 softmax 链接预测类别概率的模型。 |
| 14 | Linear Support Vector Machine | 线性支持向量机 | SVM | 以最大间隔或软间隔准则学习线性分类边界的模型。 |
| 15 | Maximum Entropy Classifier | 最大熵分类器 | MaxEnt | 在特征约束下选择最大熵条件分布的判别分类器，常等价于对数线性模型。 |
| 16 | Conditional Random Field | 条件随机场 | CRF | 对给定输入条件下结构化标签联合分布建模的判别概率模型。 |
| 17 | Linear-chain CRF | 线性链条件随机场 |  | 以相邻标签依赖和输入特征建模序列标签的 CRF 结构。 |
| 18 | Structured Prediction | 结构化预测 |  | 输出标签、树或图等相互依赖对象而非单个类别的预测任务。 |
| 19 | Sequence Classification | 序列分类 |  | 为整个句子、段落或其他序列预测单一类别的任务。 |
| 20 | Multilabel Classification | 多标签分类 |  | 允许同一文本同时归属多个非互斥类别的分类任务。 |
| 21 | Hierarchical Classification | 层次分类 |  | 在树或层级标签体系中预测一个或多个类别的分类任务。 |
| 22 | Class Imbalance | 类别不平衡 |  | 训练或评估样本在不同标签上的数量分布明显不均的现象。 |
| 23 | Cost-sensitive Learning | 代价敏感学习 |  | 在训练目标中对不同预测错误赋予不同成本的学习方法。 |
| 24 | Class Weighting | 类别加权 |  | 按类别频率或重要性调整训练损失贡献的策略。 |
| 25 | Calibration | 概率校准 |  | 使模型预测概率与相应样本真实发生频率相符合的性质或调整过程。 |

## 09. 词向量、分布式语义与表示学习

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Distributional Hypothesis | 分布式语义假说 |  | 语境分布相似的词通常具有相关语义特征的假说。 |
| 2 | Distributional Semantics | 分布式语义学 |  | 通过词语在语料中的共现上下文学习或分析词义的理论与方法。 |
| 3 | Word Embedding | 词嵌入 |  | 把词或子词映射到低维连续向量空间的表示。 |
| 4 | Static Word Embedding | 静态词向量 |  | 对同一词项在不同上下文中使用相同基本向量的表示。 |
| 5 | Contextualized Word Representation | 上下文化词表示 |  | 根据具体上下文动态为同一词项生成不同表示的机制。 |
| 6 | Word2Vec | Word2Vec 词向量模型 |  | 通过预测词与上下文共现关系学习连续词表示的模型族。 |
| 7 | Continuous Bag-of-words | 连续词袋模型 | CBOW | 通过邻近上下文词预测中心词的 Word2Vec 训练结构。 |
| 8 | Skip-gram Model | Skip-gram 模型 |  | 通过中心词预测上下文词来学习词表示的结构。 |
| 9 | Negative Sampling | 负采样 |  | 通过区分真实共现对和采样噪声对近似训练表示模型的策略。 |
| 10 | Noise-contrastive Estimation | 噪声对比估计 | NCE | 将概率密度学习转化为数据与噪声来源区分任务的估计方法。 |
| 11 | Hierarchical Softmax | 层次 Softmax |  | 通过树形类别分解减少大词表概率计算开销的技术。 |
| 12 | Global Vectors for Word Representation | 全局词向量 | GloVe | 利用词共现统计矩阵加权回归学习词向量的方法。 |
| 13 | FastText | fastText 子词表示模型 |  | 利用字符 N-gram 共享信息学习词表示及文本分类模型的工具和方法。 |
| 14 | Subword Embedding | 子词嵌入 |  | 为词内符号片段学习向量并组合形成词或文本表示的技术。 |
| 15 | Co-occurrence Matrix | 共现矩阵 |  | 统计词项与上下文项共同出现次数或权重的矩阵。 |
| 16 | Pointwise Mutual Information | 点互信息 | PMI | 衡量词项联合出现概率相对独立假设增益的关联度。 |
| 17 | Positive PMI | 正点互信息 | PPMI | 将 PMI 的负值截断为零的共现关联表示。 |
| 18 | Singular Value Decomposition | 奇异值分解 | SVD | 把矩阵分解成正交向量与奇异值，用于共现矩阵低秩表示。 |
| 19 | Embedding Space | 嵌入空间 |  | 向量表示所在的几何空间及其相似关系结构。 |
| 20 | Cosine Similarity | 余弦相似度 |  | 通过两个非零向量夹角余弦衡量方向接近程度的指标。 |
| 21 | Vector Analogy | 向量类比 |  | 利用表示空间中的向量偏移尝试刻画词汇关系的技术。 |
| 22 | Semantic Relatedness | 语义相关性 |  | 衡量词汇或文本在主题、用途等意义维度上相互联系的程度。 |
| 23 | Embedding Alignment | 嵌入空间对齐 |  | 学习映射使不同语言或不同模型的向量能够比较的过程。 |
| 24 | Embedding Anisotropy | 词向量各向异性 |  | 表示向量集中在某些方向、难以均匀覆盖向量空间的现象。 |
| 25 | Representation Collapse | 表示坍缩 |  | 训练后不同输入的向量过度相似而失去区分能力的现象。 |

## 10. 神经序列模型、编码器与解码器

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Neural Language Model | 神经语言模型 |  | 使用神经网络预测语言 token 概率或学习序列表示的模型。 |
| 2 | Recurrent Neural Network | 循环神经网络 | RNN | 通过共享递归状态逐位置处理可变长度序列的神经网络。 |
| 3 | Long Short-term Memory | 长短期记忆网络 | LSTM | 通过门控记忆单元缓解普通 RNN 长距离依赖训练困难的结构。 |
| 4 | Gated Recurrent Unit | 门控循环单元 | GRU | 用更新门和重置门控制循环状态的门控神经网络单元。 |
| 5 | Hidden State | 隐状态 |  | 循环或状态空间模型在时间步之间传递的内部表示。 |
| 6 | Encoder | 编码器 |  | 将输入序列映射到隐藏表示或中间语义状态的模型组件。 |
| 7 | Decoder | 解码器 |  | 根据中间表示及已有输出预测目标序列后续内容的组件。 |
| 8 | Encoder–Decoder Architecture | 编码器—解码器架构 |  | 由输入编码网络和输出生成网络组成的序列映射结构。 |
| 9 | Sequence-to-sequence Learning | 序列到序列学习 | Seq2Seq | 学习可变长度输入序列到输出序列映射的任务框架。 |
| 10 | Teacher Forcing | 教师强制 |  | 训练自回归解码器时以真实上一输出作为下一步输入的策略。 |
| 11 | Exposure Bias | 暴露偏差 |  | 训练依赖真实历史、推理依赖自身预测导致输入历史分布不一致的问题。 |
| 12 | Scheduled Sampling | 计划采样 |  | 训练时按调度混合使用真实历史与模型预测历史的技术。 |
| 13 | Bidirectional RNN | 双向循环神经网络 | BiRNN | 分别从前向和后向处理序列并融合上下文表示的模型。 |
| 14 | Bidirectional LSTM | 双向长短期记忆网络 | BiLSTM | 以两个方向 LSTM 捕获前后文的序列表示结构。 |
| 15 | Convolutional Text Encoder | 卷积式文本编码器 |  | 通过一维卷积和局部聚合提取 N-gram 等文本特征的模型。 |
| 16 | Sequence Transduction | 序列变换 |  | 将输入序列转换为另一个相关符号序列的任务。 |
| 17 | Autoregressive Decoding | 自回归解码 |  | 每一步以上一阶段生成 token 为条件预测后续 token 的过程。 |
| 18 | Non-autoregressive Decoding | 非自回归解码 |  | 尝试并行预测部分或全部输出位置、降低逐 token 串行依赖的生成方式。 |
| 19 | Latent Representation | 潜在表示 |  | 模型在中间层学习的连续或离散内部状态特征。 |
| 20 | Context Vector | 上下文向量 |  | 概括输入序列信息、供解码器条件生成的向量。 |
| 21 | Sequence Padding Mask | 序列填充掩码 |  | 标记 PAD 位置并阻止注意力或损失把填充当成有效内容的掩码。 |
| 22 | Packed Sequence | 打包序列 |  | 按真实样本长度组织 RNN 计算以减少不必要填充开销的数据结构。 |
| 23 | Gradient Clipping | 梯度裁剪 |  | 限制梯度范数或幅值以缓和神经网络训练不稳定性的技术。 |
| 24 | Vanishing Gradient | 梯度消失 |  | 深层或长序列反向传播中梯度持续缩小、难以更新早期参数的现象。 |
| 25 | Exploding Gradient | 梯度爆炸 |  | 反向传播中梯度过大导致训练更新发散或数值不稳定的现象。 |

## 11. 注意力机制与 Transformer 结构

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Attention Mechanism | 注意力机制 |  | 按查询与键的匹配为多个值向量分配权重并聚合信息的计算结构。 |
| 2 | Self-attention | 自注意力 |  | 同一输入序列中各位置相互计算注意力权重的机制。 |
| 3 | Cross-attention | 交叉注意力 |  | 查询来自一个序列、键和值来自另一序列的注意力机制。 |
| 4 | Scaled Dot-product Attention | 缩放点积注意力 |  | 计算查询键点积，经维度缩放和 Softmax 后加权值向量的注意力方法。 |
| 5 | Query Vector | 查询向量 | Q | 注意力机制中用于匹配键向量的线性投影表示。 |
| 6 | Key Vector | 键向量 | K | 注意力机制中用于与查询计算匹配分数的向量。 |
| 7 | Value Vector | 值向量 | V | 在注意力权重确定后被加权求和的信息向量。 |
| 8 | Multi-head Attention | 多头注意力 | MHA | 用多个投影头并行学习不同关系并拼接融合输出的注意力结构。 |
| 9 | Attention Head | 注意力头 |  | 由一组独立查询、键和值投影定义的注意力计算分支。 |
| 10 | Attention Mask | 注意力掩码 |  | 限制哪些序列位置可以相互注意的矩阵或逻辑规则。 |
| 11 | Causal Mask | 因果掩码 |  | 阻止自回归预测位置访问未来 token 的注意力掩码。 |
| 12 | Padding Mask | 填充掩码 |  | 阻止模型把无效填充位置当作真实输入参与注意力的掩码。 |
| 13 | Transformer | Transformer 模型 |  | 基于注意力、前馈网络、残差连接和归一化构建的序列处理架构。 |
| 14 | Transformer Encoder | Transformer 编码器 |  | 通常使用双向自注意力获得上下文化输入表示的 Transformer 部分。 |
| 15 | Transformer Decoder | Transformer 解码器 |  | 使用因果自注意力及可选交叉注意力生成序列的 Transformer 部分。 |
| 16 | Position-wise Feed-forward Network | 逐位置前馈网络 | FFN | 在每个 token 位置独立应用共享参数的多层非线性变换。 |
| 17 | Residual Connection | 残差连接 |  | 将层输入与变换输出相加以改善深层网络信息与梯度传递的结构。 |
| 18 | Layer Normalization | 层归一化 | LayerNorm | 在指定特征维度上按均值与方差标准化激活值的方法。 |
| 19 | Positional Encoding | 位置编码 |  | 向序列表示注入 token 顺序或相对位置关系的机制。 |
| 20 | Absolute Position Embedding | 绝对位置嵌入 |  | 为每个序列位置学习或计算与其绝对索引相关的表示。 |
| 21 | Relative Position Bias | 相对位置偏置 |  | 根据查询与键位置之间相对距离调整注意力打分的方式。 |
| 22 | Rotary Position Embedding | 旋转位置嵌入 | RoPE | 通过对查询和键向量实施位置相关旋转编码相对位置信息的技术。 |
| 23 | Attention Complexity | 注意力计算复杂度 |  | 衡量注意力随序列长度及隐藏维度变化的运算量和存储成本。 |
| 24 | FlashAttention | FlashAttention 高效注意力 |  | 通过 IO 感知分块与重计算减少高带宽存储访问的精确注意力算法族。 |
| 25 | Key–Value Cache | 键值缓存 | KV Cache | 自回归生成时缓存已计算注意力键和值以减少重复运算的结构。 |

## 12. 预训练语言模型与自监督目标

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Pretrained Language Model | 预训练语言模型 | PLM | 先在大规模文本上学习通用语言表示、再用于下游任务的模型。 |
| 2 | Self-supervised Learning | 自监督学习 |  | 从未人工标注数据中构造训练目标并学习特征的机器学习方式。 |
| 3 | Masked Language Modeling | 掩码语言建模 | MLM | 根据周围上下文预测被遮蔽输入 token 的预训练目标。 |
| 4 | Causal Language Modeling | 因果语言建模 | CLM | 根据此前 token 预测序列后续 token 的自回归训练目标。 |
| 5 | Denoising Autoencoding | 去噪自编码 |  | 把被破坏的输入还原为原始内容以学习表示的训练任务。 |
| 6 | Span Corruption | 片段破坏恢复 |  | 遮蔽或替换连续 token 片段并训练模型复原其内容的目标。 |
| 7 | Next Sentence Prediction | 下一句预测 | NSP | 判断两段输入是否在原文中具有特定相邻关系的预训练任务。 |
| 8 | Sentence Order Prediction | 句序预测 | SOP | 判断两段句子顺序是否符合语料顺序的训练目标。 |
| 9 | Bidirectional Encoder Representations from Transformers | BERT 双向编码表示 | BERT | 通过掩码语言建模等目标预训练双向 Transformer 编码器的模型。 |
| 10 | Robustly Optimized BERT Pretraining Approach | RoBERTa 预训练方法 | RoBERTa | 调整训练数据、规模及策略以改进 BERT 类编码器预训练的方案。 |
| 11 | Generative Pretrained Transformer | 生成式预训练 Transformer | GPT | 基于 Transformer 自回归语言建模训练的生成模型系列称谓。 |
| 12 | Text-to-text Transfer Transformer | 文本到文本迁移 Transformer | T5 | 将多种 NLP 任务统一写为文本输入到文本输出的编码器—解码器模型。 |
| 13 | Bidirectional and Auto-regressive Transformers | BART 去噪生成模型 | BART | 通过去噪序列重建预训练的 Transformer 编码器—解码器模型。 |
| 14 | Embeddings from Language Models | 语言模型上下文化表示 | ELMo | 利用双向语言模型生成上下文化词表示的方法。 |
| 15 | Permutation Language Modeling | 排列语言建模 |  | 按采样的预测顺序训练模型建模 token 条件依赖的目标。 |
| 16 | Replaced Token Detection | 替换词元检测 |  | 判断输入各位置是否被替换成生成器候选 token 的预训练任务。 |
| 17 | ELECTRA | ELECTRA 预训练框架 |  | 通过判别 token 是否被替换以提高表示学习样本效率的方法。 |
| 18 | Representation Pretraining | 表示预训练 |  | 通过通用目标学习能够迁移到多种下游任务的中间特征。 |
| 19 | Instruction Pretraining | 指令式预训练 |  | 在大规模训练中加入任务说明与响应结构以提高指令理解能力的训练方式。 |
| 20 | Pretraining Corpus | 预训练语料 |  | 用于通用语言模型初始学习的大规模文本集合。 |
| 21 | Training Objective | 训练目标 |  | 用于确定预训练参数更新方向的损失或优化准则。 |
| 22 | Next-token Prediction | 下一词元预测 |  | 在给定历史上下文后预测下一个离散 token 的任务。 |
| 23 | Teacher–Student Distillation | 教师—学生蒸馏 |  | 训练学生模型匹配教师模型的分布、表示或输出的知识迁移过程。 |
| 24 | DistilBERT | DistilBERT 压缩编码器 |  | 通过知识蒸馏获得较小 BERT 类语言模型的预训练方案。 |
| 25 | Domain-adaptive Pretraining | 领域自适应预训练 | DAPT | 继续使用目标领域未标注文本训练通用语言模型的策略。 |

## 13. 下游适配、监督微调与迁移学习

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Transfer Learning | 迁移学习 |  | 把在源任务或语料学到的表示用于新任务的学习方法。 |
| 2 | Fine-tuning | 微调 |  | 在预训练模型基础上用下游任务数据继续优化参数的过程。 |
| 3 | Full-parameter Fine-tuning | 全参数微调 |  | 对模型中全部或大部分权重进行下游训练更新的方式。 |
| 4 | Parameter-efficient Fine-tuning | 参数高效微调 | PEFT | 只训练少量附加或选定参数以降低任务适配成本的方法。 |
| 5 | Adapter Layer | 适配器层 |  | 插入预训练网络中的小型可训练模块，用于低成本任务调整。 |
| 6 | Low-rank Adaptation | 低秩适配 | LoRA | 用低秩矩阵表示权重增量、冻结原权重的参数高效微调方法。 |
| 7 | Prefix Tuning | 前缀调优 |  | 训练可学习的连续前缀状态以引导预训练模型生成的技术。 |
| 8 | Prompt Tuning | 软提示调优 |  | 优化少量输入提示嵌入而不全面更新模型参数的方法。 |
| 9 | Instruction Tuning | 指令微调 |  | 用任务指令和示范回答训练模型遵循自然语言要求的过程。 |
| 10 | Supervised Fine-tuning | 监督微调 | SFT | 通过人工或其他来源的输入输出配对示例优化模型的训练阶段。 |
| 11 | Task-specific Head | 任务专用预测头 |  | 在通用表示模型上附加用于分类、回归或序列标注的预测层。 |
| 12 | Sequence Classification Head | 序列分类头 |  | 把整个序列表示映射为类别分数的模型输出层。 |
| 13 | Token Classification Head | 词元分类头 |  | 把各个 token 隐状态映射为相应标签分数的输出层。 |
| 14 | Feature-based Transfer | 基于特征的迁移 |  | 冻结预训练表示网络、用抽取的向量训练下游模型的方案。 |
| 15 | Feature Extraction Mode | 特征抽取模式 |  | 仅把模型用作固定编码器而不对其参数执行任务更新的使用方式。 |
| 16 | Zero-shot Learning | 零样本学习 |  | 在无目标任务直接标注示例条件下依说明或迁移知识完成预测。 |
| 17 | Few-shot Learning | 少样本学习 |  | 依靠少量示例适配或提示模型完成新任务的范式。 |
| 18 | In-context Learning | 上下文学习 | ICL | 在模型输入中给出指令和示例以改变预测行为、但不更新模型权重的方式。 |
| 19 | Domain Adaptation | 领域适应 |  | 降低训练数据领域与目标应用领域分布差异的方法集合。 |
| 20 | Task Adaptation | 任务适配 |  | 将通用模型能力调整到特定输出格式、标签或目标任务的过程。 |
| 21 | Catastrophic Forgetting | 灾难性遗忘 |  | 继续训练新任务后模型在旧任务或知识上性能显著下降的现象。 |
| 22 | Regularization | 正则化 |  | 通过约束、惩罚或数据策略抑制过拟合并改善泛化的技术。 |
| 23 | Early Stopping | 提前停止 |  | 依据验证集表现终止训练以避免过度拟合的策略。 |
| 24 | Hyperparameter Search | 超参数搜索 |  | 比较学习率、批大小和正则强度等训练配置以选择方案的过程。 |
| 25 | Evaluation Protocol | 评测协议 |  | 规定训练、验证、测试划分以及指标计算和重复实验规则的规范。 |

## 14. 实体识别、序列标注与信息抽取

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Named Entity Recognition | 命名实体识别 | NER | 识别文本中组织、人名、地点等命名实体提及及其类别的任务。 |
| 2 | Entity Boundary Detection | 实体边界检测 |  | 定位文本中实体提及的开始与结束位置的过程。 |
| 3 | Entity Typing | 实体类型判定 |  | 为实体提及分配人、地点、组织或细粒度类别的任务。 |
| 4 | BIO Tagging Scheme | BIO 序列标签方案 | BIO | 使用 B 表开始、I 表内部、O 表非实体的词元级跨度标注规则。 |
| 5 | BIOES Tagging Scheme | BIOES 标签方案 | BIOES | 增加单词实体 S 和实体结尾 E 标签的序列标注格式。 |
| 6 | Span-based NER | 基于跨度的实体识别 |  | 枚举或提议文本片段并对每个片段判断实体边界和类型的方法。 |
| 7 | Nested Named Entity Recognition | 嵌套命名实体识别 |  | 识别多个实体跨度之间可存在包含关系的实体抽取任务。 |
| 8 | Discontinuous Entity Recognition | 非连续实体识别 |  | 识别文本中由多个不相邻片段组成的实体提及的任务。 |
| 9 | Relation Extraction | 关系抽取 | RE | 识别文本中实体之间语义关系及其类别的任务。 |
| 10 | Entity Linking | 实体链接 | EL | 把文本中实体提及映射到知识库具体唯一标识的任务。 |
| 11 | Entity Disambiguation | 实体消歧 |  | 根据上下文区分同名提及所指不同实体的过程。 |
| 12 | Event Extraction | 事件抽取 | EE | 识别事件触发词、事件类型和参与者信息的任务。 |
| 13 | Event Trigger | 事件触发词 |  | 文本中表示某种事件发生或状态改变的词语片段。 |
| 14 | Event Argument | 事件论元 |  | 参与事件并承担时间、地点、施事等语义角色的实体或片段。 |
| 15 | Event Coreference | 事件共指 |  | 判断不同事件提及是否描述同一具体事件的任务。 |
| 16 | Open Information Extraction | 开放信息抽取 | OpenIE | 在不预先限定完整关系模式的条件下从句子抽取关系三元组的方法。 |
| 17 | Slot Filling | 槽位填充 |  | 为指定实体或任务结构补齐预定义属性值的过程。 |
| 18 | Template Filling | 模板填充 |  | 把文本信息填入预先定义的事件或事实模板字段的任务。 |
| 19 | Relation Triple | 关系三元组 |  | 以主体、谓词与客体表示结构化关系事实的形式。 |
| 20 | Knowledge Base Population | 知识库自动填充 | KBP | 从文本中抽取并链接实体属性和关系、更新知识库的过程。 |
| 21 | Distant Supervision | 远程监督 |  | 利用已有知识库对语料中的实体对自动生成弱标注关系标签的策略。 |
| 22 | Weak Supervision | 弱监督 |  | 利用启发式规则、不精确标签或间接信号构建训练数据的方法。 |
| 23 | Span-level F1 | 跨度级 F1 |  | 以预测片段与参考片段完全匹配的精确率和召回率计算的调和均值。 |
| 24 | Entity-level Evaluation | 实体级评估 |  | 根据完整实体边界及类别是否正确衡量抽取质量的评测方式。 |
| 25 | Boundary Error | 边界错误 |  | 预测的实体或答案片段起止位置与参考标注不一致的错误。 |

## 15. 问答、文档检索与文本匹配

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Reading Comprehension | 机器阅读理解 |  | 根据给定文章回答问题并推断文本包含信息的任务。 |
| 2 | Extractive Question Answering | 抽取式问答 |  | 通过定位上下文中的连续文本跨度输出答案的问答形式。 |
| 3 | Abstractive Question Answering | 生成式问答 |  | 根据问题及证据自行生成答案而非直接复制原文片段的任务。 |
| 4 | Open-domain Question Answering | 开放域问答 | ODQA | 利用宽领域语料和检索机制回答不预限主题问题的任务。 |
| 5 | Closed-book Question Answering | 闭卷问答 |  | 不提供实时外部知识库、仅根据模型内部表示回答问题的设定。 |
| 6 | Retrieval-Augmented Generation | 检索增强生成 | RAG | 在生成答案时利用外部检索资料补充语言模型上下文的架构。 |
| 7 | Document Retrieval | 文档检索 |  | 根据查询从语料库中挑选相关文档的任务。 |
| 8 | Passage Retrieval | 段落检索 |  | 根据查询从文档短片段或段落集合中召回相关内容的任务。 |
| 9 | Lexical Retrieval | 词法检索 |  | 通过词项匹配、倒排索引或词频评分查找候选内容的方法。 |
| 10 | Dense Passage Retrieval | 稠密段落检索 | DPR | 分别编码问题和段落向量、通过相似度进行召回的模型方案。 |
| 11 | BM25 | BM25 相关性评分 | BM25 | 结合词频饱和、文档长度和词项逆文档频率的排序函数族。 |
| 12 | Dual Encoder | 双编码器 |  | 分别计算两个输入的向量表示并以匹配函数评分的模型架构。 |
| 13 | Cross Encoder | 交叉编码器 |  | 将两个输入联合编码、直接预测它们的相关或匹配程度的架构。 |
| 14 | Semantic Search | 语义搜索 |  | 利用词向量或语言模型表示寻找语义相关内容的检索方式。 |
| 15 | Text Matching | 文本匹配 |  | 预测两个文本在语义、意图或关系上是否符合某种匹配准则的任务。 |
| 16 | Paraphrase Detection | 复述识别 |  | 判断两个不同表述是否传达基本相同含义的任务。 |
| 17 | Question Similarity | 问题相似度 |  | 衡量不同自然语言问题的语义目标或可互答程度的指标或任务。 |
| 18 | Reranking | 重排序 |  | 对首轮召回的较少候选采用更精细模型重新排列的检索步骤。 |
| 19 | Multi-hop Question Answering | 多跳问答 |  | 需要串联多个事实、实体或文档才能回答的问题类型。 |
| 20 | Answer Span | 答案跨度 |  | 抽取式问答中位于上下文起止 token 之间的连续文本区域。 |
| 21 | Answerability Prediction | 可回答性判定 |  | 根据证据或任务定义判断当前问题是否存在可支持答案的模型任务。 |
| 22 | Evidence Retrieval | 证据检索 |  | 获取支持回答中关键事实或推理步骤的相关文本片段的过程。 |
| 23 | Citation Attribution | 引用归属 |  | 将答案中的事实陈述映射到对应来源文档或证据片段的过程。 |
| 24 | Answer Grounding | 答案锚定 |  | 约束答案事实必须能从指定上下文或外部资料中得到支持的做法。 |
| 25 | Unanswerable Question | 不可回答问题 |  | 在指定证据与约束下缺乏可靠答案的输入问题。 |

## 16. 机器翻译、跨语言迁移与多语建模

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Neural Machine Translation | 神经机器翻译 | NMT | 利用神经编码器解码器或 Transformer 学习源到目标语言映射的翻译方法。 |
| 2 | Statistical Machine Translation | 统计机器翻译 | SMT | 通过概率翻译模型和语言模型构造翻译决策的历史技术体系。 |
| 3 | Rule-based Machine Translation | 基于规则的机器翻译 | RBMT | 利用手工构建的词典、语法和转换规则生成译文的系统。 |
| 4 | Phrase-based Machine Translation | 基于短语的机器翻译 | PBMT | 将词组片段作为基本翻译映射单位的统计机器翻译方法。 |
| 5 | Word Alignment | 词语对齐 |  | 识别源语和目标语中哪些词项相互对应的任务。 |
| 6 | Sentence Alignment | 句子对齐 |  | 在双语文档中匹配互为翻译的句子或段落的过程。 |
| 7 | Parallel Sentence Pair | 平行句对 |  | 表达相同内容的两个不同语言句子的训练或评测单位。 |
| 8 | Translation Memory | 翻译记忆库 | TM | 保存历史原文译文配对供人工或机器翻译检索复用的资源。 |
| 9 | Beam Search | 束搜索 |  | 每个生成步骤保留得分最高的有限数量候选序列进行近似搜索的算法。 |
| 10 | Beam Width | 束宽 |  | 束搜索每步最多保留的候选假设数量。 |
| 11 | Length Penalty | 长度惩罚 |  | 在候选序列评分中调整长度偏好以避免系统性短句偏置的机制。 |
| 12 | Coverage Penalty | 覆盖惩罚 |  | 鼓励解码过程充分关注源文本内容的候选评分修正项。 |
| 13 | Terminology Constraint | 术语约束 |  | 要求译文保留或使用指定专业词汇的翻译条件。 |
| 14 | Constrained Decoding | 受约束解码 |  | 在生成中强制满足特定词项、结构或格式要求的搜索策略。 |
| 15 | Back-translation | 回译数据增强 |  | 把目标语言单语句翻译回源语以构造伪平行训练数据的技术。 |
| 16 | Pivot Translation | 枢轴语言翻译 |  | 先转为中间语言再翻译到目标语言的跨语言转换策略。 |
| 17 | Multilingual Machine Translation | 多语言机器翻译 |  | 单一模型支持多个源语言与目标语言翻译方向的系统。 |
| 18 | Zero-shot Translation | 零样本翻译 |  | 在训练中缺少直接源目标语言句对条件下完成该语言方向翻译的任务。 |
| 19 | Cross-lingual Transfer | 跨语言迁移 |  | 将一种语言中学到的表示或任务知识应用到另一语言的过程。 |
| 20 | Cross-lingual Alignment | 跨语言对齐 |  | 让不同语言中的词、句向量或结构在共享空间中可比较的技术。 |
| 21 | Code-switching | 语码转换 |  | 一段话语中交替使用两种或多种语言的现象。 |
| 22 | Low-resource Language | 低资源语言 |  | 相对于任务需要，可用标注数据、语料或工具资源较少的语言。 |
| 23 | Morphologically Rich Language | 形态丰富语言 |  | 具有多样屈折和派生词形、词型稀疏性明显的语言。 |
| 24 | Language Identification | 语言识别 | LID | 判断文本或音频属于何种语言或语言组合的任务。 |
| 25 | Translation Quality Estimation | 翻译质量估计 | QE | 在没有人工参考译文或无需完整参考译文时估计译文质量的任务。 |

## 17. 文本生成、摘要、对话与解码控制

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Text Generation | 文本生成 |  | 根据提示、输入结构或上下文自动生成自然语言序列的任务。 |
| 2 | Conditional Generation | 条件文本生成 |  | 在给定问题、文档或控制变量条件下生成目标文本的机制。 |
| 3 | Unconditional Generation | 无条件文本生成 |  | 在不提供特定内容上下文时从语言模型先验分布生成文本的过程。 |
| 4 | Greedy Decoding | 贪心解码 |  | 每一步选择当前条件概率最高 token 的生成算法。 |
| 5 | Top-k Sampling | 前 k 候选采样 |  | 每步从概率最高的 k 个 token 中按重归一化概率抽样的解码方法。 |
| 6 | Nucleus Sampling | 核采样 | Top-p | 每步从累计概率达到阈值 p 的最小高概率候选集合采样的策略。 |
| 7 | Temperature Scaling | 温度缩放 |  | 在 Softmax 前调整 logits 尺度以控制生成分布尖锐程度的方法。 |
| 8 | Repetition Penalty | 重复惩罚 |  | 降低已经生成内容再次被选择概率的采样或评分机制。 |
| 9 | Stop Sequence | 终止序列 |  | 一旦在生成文本中匹配到便提前停止输出的指定字符或 token 模式。 |
| 10 | Maximum Generation Length | 最大生成长度 |  | 对单次解码最多可产生的 token 数量施加的上界。 |
| 11 | Minimum Generation Length | 最小生成长度 |  | 在生成达到预定长度前限制或抑制结束操作的控制条件。 |
| 12 | Extractive Summarization | 抽取式摘要 |  | 直接选择原文中的句子或片段组成摘要的任务形式。 |
| 13 | Abstractive Summarization | 生成式摘要 |  | 用新表述压缩和整合原文信息而不局限于原句的摘要形式。 |
| 14 | Query-focused Summarization | 面向查询的摘要 |  | 根据用户问题或指定信息需求选择摘要重点的方法。 |
| 15 | Multi-document Summarization | 多文档摘要 |  | 把多篇相关来源整合为一个覆盖共同或互补信息的摘要。 |
| 16 | Summary Faithfulness | 摘要忠实性 |  | 摘要的事实陈述与原文证据保持一致、不引入不支持信息的性质。 |
| 17 | Factual Consistency | 事实一致性 |  | 生成文本中的事实是否与给定来源或已验证事实相符的性质。 |
| 18 | Dialogue State Tracking | 对话状态跟踪 | DST | 根据多轮交互持续更新用户目标、槽位值和上下文状态的任务。 |
| 19 | Dialogue Act | 对话行为 |  | 对语句执行的提问、确认、告知或请求等交际功能的标注类别。 |
| 20 | Intent Detection | 意图识别 |  | 从用户话语推断请求、目标或操作类别的任务。 |
| 21 | Slot Filling for Dialogue | 对话槽位填充 |  | 提取预定业务槽位所对应实体或参数值的任务。 |
| 22 | Response Generation | 回复生成 |  | 依据对话历史、状态或知识生成系统下一轮话语的过程。 |
| 23 | Turn-taking | 话轮交替 |  | 对话参与者在连续交互中控制说话时机与轮次的机制。 |
| 24 | Context Carryover | 上下文继承 |  | 在后续轮次中继续使用此前确认的实体、条件与约束的能力。 |
| 25 | Dialogue Evaluation | 对话系统评估 |  | 结合任务成功、响应质量、事实支持和用户体验衡量对话系统的流程。 |

## 18. 语音语言接口与多模态 NLP

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Automatic Speech Recognition | 自动语音识别 | ASR | 将语音音频信号转换为文本词序列的技术。 |
| 2 | Speech-to-text | 语音转文本 | STT | 把录制或实时语音解码为文字结果的系统能力。 |
| 3 | Text-to-speech | 文本转语音 | TTS | 根据输入文本合成自然语音波形的任务。 |
| 4 | Speech Synthesis | 语音合成 |  | 通过模型生成声学特征或波形以表达指定语言内容的过程。 |
| 5 | Phoneme | 音位 |  | 语言音系中能够区别词义的抽象声音单位。 |
| 6 | Grapheme | 字素 |  | 书写系统中区别文字形式的基本图形单位。 |
| 7 | Grapheme-to-phoneme Conversion | 字素转音位 | G2P | 将书面形式映射为发音音位序列的任务。 |
| 8 | Acoustic Model | 声学模型 |  | 对音频特征与发音或语言单位之间统计关系建模的组件。 |
| 9 | Pronunciation Lexicon | 发音词典 |  | 记录词语与其对应音位或发音序列的资源。 |
| 10 | Connectionist Temporal Classification | 连接时序分类 | CTC | 对输入输出对齐未知的序列任务求和多条路径概率的训练目标。 |
| 11 | RNN Transducer | 循环神经网络转导器 | RNN-T | 联合声学与输出历史预测符号、适合流式语音识别的转导结构。 |
| 12 | End-to-end ASR | 端到端语音识别 |  | 通过统一神经网络从声学输入直接预测文字或语言单位的框架。 |
| 13 | Streaming ASR | 流式语音识别 |  | 在持续接收音频时增量输出识别结果的系统模式。 |
| 14 | Word Error Rate | 词错误率 | WER | 以替换、删除和插入词数之和除以参考词数的语音识别指标。 |
| 15 | Character Error Rate | 字符错误率 | CER | 以字符层编辑错误数除以参考字符数的识别指标。 |
| 16 | Speaker Diarization | 说话人分离标注 |  | 判断录音中不同时间段由哪位说话人发声的任务。 |
| 17 | Voice Activity Detection | 语音活动检测 | VAD | 识别音频中包含人声或语音的时间区间的任务。 |
| 18 | Forced Alignment | 强制对齐 |  | 在已知文字或音位序列条件下确定其在音频中的时间边界。 |
| 19 | Prosody Modeling | 韵律建模 |  | 对语音节奏、重音、停顿与音调等超音段特征建模的过程。 |
| 20 | Speech Translation | 语音翻译 |  | 把一种语言语音转换为另一语言文本或语音的任务。 |
| 21 | Multimodal NLP | 多模态自然语言处理 |  | 联合文本与图像、音频或视频等模态完成语言理解和生成的领域。 |
| 22 | Vision–Language Model | 视觉—语言模型 | VLM | 联合处理视觉内容与文本语义的模型架构。 |
| 23 | Image Captioning | 图像描述生成 |  | 根据图片内容自动生成自然语言说明的任务。 |
| 24 | Visual Question Answering | 视觉问答 | VQA | 结合图像及文字问题推断并生成答案的任务。 |
| 25 | Document Understanding | 文档智能理解 |  | 综合 OCR、版面结构、表格和语言语义理解复杂文档内容的任务。 |

## 19. NLP 指标、基准与误差分析

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Evaluation Metric | 评测指标 |  | 将模型任务质量量化为明确数值规则的度量。 |
| 2 | Accuracy | 准确率 | Accuracy | 分类预测正确样本数占总样本数的比例。 |
| 3 | Precision | 精确率 | Precision | 预测为正样本中实际为正的比例。 |
| 4 | Recall | 召回率 | Recall | 真实正样本中被正确预测为正的比例。 |
| 5 | F1 Score | F1 分数 | F1 | 精确率与召回率的调和均值。 |
| 6 | Macro Averaging | 宏平均 |  | 分别计算各类别指标后不按类别频数加权平均的方式。 |
| 7 | Micro Averaging | 微平均 |  | 先汇总各类别 TP、FP、FN 再计算总体指标的方式。 |
| 8 | Weighted Averaging | 加权平均 |  | 按类别样本量等预定权重求类别指标平均值的方式。 |
| 9 | Confusion Matrix | 混淆矩阵 |  | 按真实类别和预测类别交叉统计样本数量的矩阵。 |
| 10 | Exact Match | 完全匹配率 | EM | 预测答案与参考答案在约定规范化下完全一致的样本比例。 |
| 11 | BLEU | 机器翻译评分指标 | BLEU | 基于修改后 N-gram 精确率和长度惩罚的机器翻译自动评价指标。 |
| 12 | ROUGE | 面向摘要的召回指标族 | ROUGE | 根据与参考摘要重合的 N-gram 或最长公共子序列评价文本摘要的指标族。 |
| 13 | METEOR | METEOR 翻译评价指标 | METEOR | 利用词形、同义及序列对齐信息衡量候选译文与参考的指标。 |
| 14 | chrF | 字符 N 元 F 分数 | chrF | 以字符 N-gram 精确率和召回率计算机器翻译质量的指标。 |
| 15 | BERTScore | BERTScore 语义相似指标 |  | 用上下文化词向量匹配候选与参考 token 计算文本生成相似度的指标。 |
| 16 | COMET | COMET 翻译质量评测模型 |  | 利用神经网络对源文、候选译文和可选参考译文预测翻译质量的评价框架。 |
| 17 | Human Evaluation | 人工评估 |  | 由评审者根据任务指南检查模型输出正确性、自然度和有用性的流程。 |
| 18 | Inter-rater Reliability | 评审者间可靠性 |  | 量化不同人工评审者作出相近评分或决策程度的性质。 |
| 19 | Benchmark Dataset | 基准数据集 |  | 用固定评测示例与指标比较不同模型能力的数据资源。 |
| 20 | GLUE Benchmark | GLUE 语言理解基准 | GLUE | 包含多个英语分类与自然语言推断任务的模型评测基准。 |
| 21 | SuperGLUE Benchmark | SuperGLUE 语言理解基准 | SuperGLUE | 设计用于挑战语言理解模型的一组更困难任务与评测指标。 |
| 22 | SQuAD | 斯坦福问答数据集 | SQuAD | 以维基百科段落和问题构建的阅读理解数据集。 |
| 23 | Error Analysis | 误差分析 |  | 按任务类型、语言现象或输入子群检查模型错误原因的过程。 |
| 24 | Statistical Significance Test | 统计显著性检验 |  | 在明确零假设与抽样机制下评估观测差异偶然性的方法。 |
| 25 | Bootstrap Confidence Interval | Bootstrap 置信区间 |  | 通过对样本重新抽样估计指标的不确定性区间的方法。 |

## 20. 可靠性、数据治理与生产部署

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Hallucination | 模型幻觉 |  | 语言模型输出看似合理但缺少依据或与可核验事实冲突的内容。 |
| 2 | Grounded Response | 证据支持的回复 |  | 主要事实陈述能从明确提供的资料或可信工具输出中找到依据的回答。 |
| 3 | Abstention | 拒绝无证据作答 |  | 当资料不足时明确承认无法确认而非猜测事实的响应策略。 |
| 4 | Uncertainty Estimation | 不确定性估计 |  | 分析模型预测可靠性、置信程度及潜在错误风险的方法。 |
| 5 | Out-of-distribution Detection | 分布外检测 | OOD | 识别与训练数据分布明显不同的输入或任务情形的技术。 |
| 6 | Robustness Evaluation | 鲁棒性评估 |  | 检验模型在噪声、拼写变化、对抗输入或领域变化下性能稳定性的过程。 |
| 7 | Adversarial Example | 对抗样本 |  | 经过特意设计的输入扰动，可诱导模型作出错误预测的例子。 |
| 8 | Prompt Injection | 提示注入 |  | 攻击者通过输入或外部内容诱导模型违背更高优先级指令的行为。 |
| 9 | Indirect Prompt Injection | 间接提示注入 |  | 把恶意指令隐藏在检索文档、网页或工具输出等低信任内容中的攻击。 |
| 10 | Data Privacy | 数据隐私 |  | 按合法授权与处理目的控制文本中的个人或敏感信息使用的原则。 |
| 11 | Personally Identifiable Information | 可识别个人身份信息 | PII | 可单独或结合其他信息识别个人身份的数据。 |
| 12 | Data Anonymization | 数据匿名化 |  | 通过技术与治理措施降低记录再识别风险、使其不再对应可识别个人的过程。 |
| 13 | De-identification | 去标识化 |  | 删除或替换直接标识符并降低身份关联风险的数据处理方式。 |
| 14 | Bias Evaluation | 偏差评估 |  | 检查模型对不同人口群体、语言变体或主题的错误和不公平差异的过程。 |
| 15 | Fairness Metric | 公平性指标 |  | 用明确数学规则衡量模型在不同群体间表现差异的指标。 |
| 16 | Toxicity Detection | 有害语言检测 |  | 识别文本中骚扰、仇恨、攻击性或其他有害语言类别的任务。 |
| 17 | Content Moderation | 内容审核 |  | 根据约定政策对文本进行允许、限制、标记或人工复核的流程。 |
| 18 | Model Serving | 模型服务化 |  | 将训练模型部署为可被请求调用的推理接口或批量服务的过程。 |
| 19 | Inference Latency | 推理延迟 |  | 从服务接收输入到返回预测或生成结果所需的时间。 |
| 20 | Batch Inference | 批量推理 |  | 一次对多条独立输入执行模型计算以提高硬件利用率的方式。 |
| 21 | Streaming Generation | 流式生成 |  | 在输出序列尚未完成前持续传送已生成 token 或文本的服务模式。 |
| 22 | Quantization | 模型量化 |  | 将权重或激活表示映射为较低位宽数值以降低存储或计算成本的技术。 |
| 23 | Model Distillation | 模型蒸馏 |  | 利用较大教师模型信号训练较小学生模型的模型压缩技术。 |
| 24 | Monitoring Drift | 模型漂移监控 |  | 监测线上语言数据分布、输出或任务指标随时间变化的机制。 |
| 25 | Human-in-the-loop Review | 人在回路中的审核 | HITL | 在自动系统处理过程中安排人工复核、纠错或决策的协同模式。 |

## 16 组核心概念辨析

| 对比对象 | 技术区别及应用边界 |
|---|---|
| NLP、NLU 与 NLG | NLP 是整个自然语言处理领域；NLU 侧重语义与意图理解；NLG 侧重根据条件或知识形成语言输出。 |
| 词语切分与子词词元化 | 中文词语切分寻求语言学意义上的词边界；BPE、WordPiece 等为模型词表压缩与覆盖而切分，结果不一定是自然词。 |
| BPE、WordPiece 与 Unigram | BPE 通常反复合并常见符号对；WordPiece 在指定训练准则下选择子词；Unigram 从候选词表中用概率模型选择切分。 |
| Stemming 与 Lemmatization | Stemming 可用字符串截断得到不一定存在的词干；Lemmatization 利用词形和词典信息找规范词元基本形。 |
| 成分句法与依存句法 | 成分句法用嵌套短语树刻画结构；依存句法用词间有向中心词关系刻画结构，两者可以转换但并不完全等价。 |
| NER、实体链接与共指消解 | NER 识别提及边界与类别；实体链接映射到知识库条目；共指消解决定多个提及是否指向同一实体。 |
| HMM 与 CRF | HMM 建模隐状态和观测的生成概率；CRF 直接建模给定输入的标签条件分布，便于灵活使用输入特征。 |
| 静态词向量与上下文化表示 | 静态向量通常为一个词型固定表示；上下文化表示根据具体句子改变同一个词的向量，有助于区分词义。 |
| CBOW 与 Skip-gram | CBOW 根据上下文预测中心词；Skip-gram 根据中心词预测其周围词，两者是 Word2Vec 经典训练方向。 |
| Transformer 编码器与自回归解码器 | 常见编码器允许输入 token 双向交互；自回归解码器使用因果掩码逐步预测后续 token。 |
| BERT MLM 与 GPT CLM | MLM 根据被遮蔽 token 左右上下文学习双向表示；CLM 根据前缀预测下一个 token，适合自回归生成。 |
| 微调与上下文学习 | 微调通过训练数据更新参数；上下文学习仅改变推理时输入示例与指令，通常不修改模型权重。 |
| LoRA 与全参数微调 | LoRA 以少量低秩参数表示可训练增量，节省显存与存储；全参数微调允许更新模型大部分权重。 |
| 抽取式问答与生成式问答 | 抽取式问答定位上下文中的连续答案跨度；生成式问答可重述综合信息，但更需要证据忠实性验证。 |
| BLEU、ROUGE 与 BERTScore | BLEU 偏重译文的 N-gram 精确率，ROUGE 常用于摘要重叠评估，BERTScore 利用上下文化表示匹配；均非真实事实性证明。 |
| 语音识别 WER 与机器翻译 BLEU | WER 衡量识别词的编辑错误数量；BLEU 比较候选译文与参考译文的 N-gram 重合，指标目标与方向不同。 |

## 中等难度面试问答

### 面试 1：中文分词和 BPE 子词切分为什么不能互相替代？

**参考答案：**中文分词寻求自然语言词的边界；BPE 主要为限制词表、降低 OOV 而服务模型输入。一个中文词可能拆为多个 token，反之 token 也不必是完整词。

### 面试 2：为什么不同 tokenizer 下的语言模型困惑度不能直接比较？

**参考答案：**困惑度按 token 的平均负对数似然定义，token 粒度不同会改变序列长度与概率单位；应使用相同编码或按字节归一化等可比协议。

### 面试 3：依存句法中的 projective 与 non-projective 结构有什么区别？

**参考答案：**投射依存树在词序表示中满足相应不交叉条件；非投射树需要更一般的解析结构，部分语言中跨距依存较常见。

### 面试 4：为什么 HMM 的状态转移与 CRF 的特征建模方式不同？

**参考答案：**HMM 指定潜状态与观测的联合生成分解；线性链 CRF 对给定整段输入条件下的标签序列归一化，可使用任意输入相关的局部特征。

### 面试 5：BERT 预训练与 GPT 类模型的目标有哪些结构差异？

**参考答案：**BERT 典型 MLM 依赖双向上下文恢复被遮蔽位置；GPT 典型 CLM 用因果掩码建模前缀到下一 token 的条件概率。

### 面试 6：为什么单纯提高 beam width 不一定提高机器翻译质量？

**参考答案：**束宽增加可改善当前模型评分的搜索近似，却不能纠正长度偏好或模型分布失准，可能导致短输出或其他质量下降。

### 面试 7：词元分类的 token F1 与实体级 F1 为什么不同？

**参考答案：**token F1 按位置计分，实体级 F1 通常要求预测片段起止边界和类别全部正确；前者可能掩盖边界碎裂错误。

### 面试 8：为什么静态词向量难以处理一词多义？

**参考答案：**一个词的不同语境共用固定词型向量，无法直接表示 bank 等词的多种含义；上下文化编码器可按语境改变表示。

### 面试 9：什么情况下微调优于仅使用 few-shot 提示？

**参考答案：**当任务标签稳定、可用高质量示例较多、推理成本或格式一致性要求高时，微调可能更适用；仍应比较数据成本、泛化与遗忘风险。

### 面试 10：如何检查生成摘要是否忠实于源文档？

**参考答案：**将摘要拆分为事实断言，检索源文支持片段并检查时间、数量与实体是否一致；ROUGE 高分本身不能保证事实正确。

### 面试 11：评测多语言 NLP 时为什么不应只看英语性能？

**参考答案：**语料规模、形态复杂度、文字系统、分词与领域分布不同，英语分数可能掩盖低资源语言上的明显退化。

### 面试 12：部署面向企业文档的 NLP 系统，如何处理间接提示注入？

**参考答案：**把检索内容视为低信任数据，权限校验和外部工具授权在后端实施，隔离指令与证据，并执行引用核验与最小权限控制。

## 中等难度考试题与解析

### 考试 1：一个序列 100 个 token，模型对它们平均负对数概率（自然对数）为 2，困惑度是多少？

**解析：**PPL=exp(2)≈7.389，必须说明以 token 为单位且统一使用自然对数。

### 考试 2：分类任务 TP=80、FP=20、FN=40，计算 Precision、Recall 和 F1。

**解析：**P=80/100=0.8，R=80/120≈0.667，F1=2TP/(2TP+FP+FN)=160/220≈0.727。

### 考试 3：一个实体参考跨度为 token 2–4，系统预测为 2–3 且类型相同，严格实体级匹配能否记为 TP？

**解析：**不能。严格 span-level 评测要求起止边界和类型完全一致，否则会导致相应 FP 与 FN。

### 考试 4：Bigram 模型中 count('自然 语言')=30，count('自然')=50，MLE P(语言|自然) 是多少？

**解析：**30/50=0.6，假定计数来自相同的 bigram 统计口径且无需平滑。

### 考试 5：某词在 10,000 篇文档中出现于 100 篇，使用 ln(N/df) 的 IDF 等于多少？

**解析：**ln(10000/100)=ln(100)≈4.605。

### 考试 6：Attention 有 8 个 head、总隐藏维度 d_model=512，均匀分配时每头维度是多少？

**解析：**512/8=64。实际模型还可能使用不同的键值头数或投影维度。

### 考试 7：对两向量 a=(1,0) 与 b=(1,1)，余弦相似度是多少？

**解析：**a·b/(||a||||b||)=1/√2≈0.7071。

### 考试 8：WER 参考文本 20 词，出现 2 个替换、1 个删除、1 个插入，WER 为多少？

**解析：**WER=(S+D+I)/N=(2+1+1)/20=0.20，即 20%。

### 考试 9：3 句参考摘要中有 6 个不同 bigram，系统摘要命中其中 3 个，按召回定义的 ROUGE-2 Recall 多少？

**解析：**3/6=0.5；实际实现还需规定重复计数和规范化规则。

### 考试 10：两个标签分类结果中 TP=30、FP=10、FN=5，F1 是多少？

**解析：**F1=2TP/(2TP+FP+FN)=60/75=0.8。

### 考试 11：4 个候选 token 归一化概率为 0.5、0.3、0.15、0.05，Top-p=0.8 的最小采样集合包含几个？

**解析：**按概率降序取前两个即可，累计概率 0.5+0.3=0.8；实现对阈值等号可能有边界约定。

### 考试 12：Seq2Seq 参考序列长度 8、预测序列长度 5，是否能仅凭长度判定翻译准确？

**解析：**不能。长度可以影响长度惩罚和覆盖情况，但准确性还需语义、术语、忠实性和任务评测。

## 经典教材、学术论文和技术资料

以下资源用于提供研究背景、模型名称与知识体系，原作者未参与或认可本项目逐条术语审稿。

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

## 数据维护与发布边界

- 原始数据：`data/nlp/chapters/*.tsv`，字段为 `English|中文|abbr|definition`。
- 输出文件：`data/nlp.tsv`、`glossaries/nlp.md`、`pdf/nlp.pdf` 和 `docs/` 镜像。
- 生成与一致性校验：`node scripts/render_nlp.mjs` / `node scripts/render_nlp.mjs --check`。
- 本册是独立出版术语表；**未加入全站搜索索引、未生成 500 篇深度 Wiki**。
