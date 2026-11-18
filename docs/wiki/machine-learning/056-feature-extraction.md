# Feature Extraction（特征提取）

> 领域：机器学习 · 专题：数据预处理与特征工程 · 原理、数理条件与工程设计

## 1. 核心定义

特征提取是从原始文本、图像、信号或结构化记录中计算适于模型消费的特征表示。它可以是固定算法（如文本计数、傅里叶谱）或已学习的编码器，与人为筛掉特征的选择任务不同。

## 2. 形象理解

像从整张音乐波形中提取音高、节拍和频谱轮廓，让后续分类器无需直接处理每个采样点。

**类比的局限：**提取器可能丢失关键时序或上下文：词袋不保留词序，平均频谱不保留完整时变结构。

## 3. 技术原理与核心内容

定义 z=φ(x)，原始输入经分词/向量化、滤波/频谱变换、分块统计或神经编码器形成向量/张量。若 φ 含训练词表、标准化参数或编码器微调权重，其 fit 只能使用训练折；对稀疏词频矩阵需保持词表顺序和稀疏格式一致。

## 4. 工程实践与设计权衡

日志分类可先使用 CountVectorizer 或 TfidfVectorizer，把文本编码成 CSR 稀疏矩阵；对于 OOV 词需要明确处理，避免在测试集学习新词表。与文本深度编码器比较性能、延迟、解释性及冷启动成本。

## 5. 关联知识与易混辨析

Feature Extraction 把原数据变为特征；Feature Engineering 更宽泛；Feature Selection 从特征中挑子集；Representation Learning 关注从数据学习 φ 的表示。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么测试集不能参与 CountVectorizer 的词表拟合？** 答：测试词分布进入训练特征空间定义，破坏独立评估；训练集 fit 词表，测试集只 transform，未知词按既定规则处理。

2. **问：文本表示使用词袋还是深度 embedding，怎么选？** 答：数据量、标签成本、语义需求、延迟预算和可解释性决定。词袋简单可审计但不捕捉词序；预训练 embedding 迁移性更强但成本与偏差不同。

## 7. 中等难度考试题（含解析）

1. **题：3 篇文档组成词表共 8 个唯一词，CountVectorizer 的 X 形状是多少？** 解：若无额外 n-gram 和过滤规则，X 为 (3,8)。

2. **题：长度 1,024 点的实信号做离散傅里叶变换，完整复谱含多少个频率系数？** 解：标准 DFT 有 1,024 个复频率系数；若只存非冗余的实信号 rFFT 则通常为 1024/2+1=513 个系数。

## 8. 权威来源与延伸阅读

- [scikit-learn Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html)：核对该术语的正式定义、适用条件及技术边界。
- [scikit-learn CountVectorizer API](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)：核对该术语的正式定义、适用条件及技术边界。

> 本文数值为明确的教学算例，不代表工业实测；独立领域专家审稿仍为 pending。
