# TF–IDF（词频-逆文档频率）

> 领域：机器学习 · 专题：数据预处理与特征工程 · 数理原理、适用条件与生产风险

## 1. 核心定义

词频—逆文档频率（TF–IDF）通过词在当前文档中的频率与在整个训练语料的普遍程度共同确定权重，帮助突出相对有区分性的词项。它不直接理解语义，也不等同出现越多就一定越重要。

## 2. 形象理解

某技术词在一份文档里多次出现、但在其他文档很少出现，像一张有辨识度的主题标签；“的”“是”等处处都有的词权重较低。

**类比的局限：**同义词、否定与词序不被基础 TF-IDF 捕捉；罕见拼写错误同样可能有很高的 IDF 权重。

## 3. 技术原理与核心内容

常见自定义公式 tf(t,d)=count(t,d)，idf(t)=ln(N/df(t))，tfidf=tf×idf；实现可能加 1 和平滑以避免零或改善稳定性。scikit-learn TfidfVectorizer 默认平滑 IDF：idf(t)=ln((1+N)/(1+df(t)))+1，并默认对每行做 L2 归一化；必须注明公式约定。fit IDF 只用训练语料，测试只 transform，否则存在语料分布泄漏。

## 4. 工程实践与设计权衡

知识库检索与工单分类可先用 TF-IDF+余弦相似度建立基线。语料规模、分词、min_df 与 max_df、字词 n-gram 影响稀疏度与速度；上线应版本化训练词表、IDF 与 tokenizer。

## 5. 关联知识与易混辨析

TF-IDF 是词袋计数上的加权策略；BM25 有长度归一化与概率模型背景；Embedding 用向量学习语义相似性，三者需在领域检索测试上比较。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么需要冻结 IDF 而不是根据每批查询文档重新 fit？** 答：重新估计全局文档频率会改变特征尺度与模型输入契约，且若测试语料参与训练特征设计则违反评估隔离。

2. **问：TF-IDF 适合短文本或语义检索吗？** 答：它可作为低成本强基线，但同义词或跨语言语义匹配有限。可与 BM25、Dense Embedding 混合，在独立查询集评估召回、延迟和成本。

## 7. 中等难度考试题（含解析）

1. **题：在不平滑定义 idf=ln(N/df) 下，N=100、某词 df=10，idf 多少？** 解：ln(100/10)=ln10≈2.303；此题特意使用不平滑定义，不能当作 sklearn 默认 IDF。

2. **题：scikit-learn 默认平滑 IDF，N=9、df=1，求 idf。** 解：ln((1+9)/(1+1))+1=ln5+1≈2.609；如果还做 L2 归一化，最终权重需按整篇文档向量范数再缩放。

## 8. 权威来源与延伸阅读

- [TfidfVectorizer API](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)：核对该机制的定义、公式与技术边界。
- [Text Feature Extraction / TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html)：核对该机制的定义、公式与技术边界。

> 本文数值是教学设定，非工业设备实测数据；领域专家技术审核状态仍 pending。
