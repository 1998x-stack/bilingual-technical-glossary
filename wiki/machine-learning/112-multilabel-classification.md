# Multilabel Classification（多标签分类）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 监督目标、优化公式和工程条件

## 1. 核心定义

多标签分类（Multilabel Classification）允许每个样本同时拥有多个非互斥标签，目标可表示为 K 维二值向量，例如文章同时属于“机器学习”和“工程实践”。它区别于每条记录只能选择一种互斥类别的多类别分类。

## 2. 形象理解

像一本书可以贴上“数学”“编程”“教育”多张主题贴纸，而不是只能放到某个唯一书架类别。

**类比的局限：**标签之间可能高度相关且存在层级约束；独立训练 K 个二分类器可能忽略这种依赖。

## 3. 技术原理与核心内容

令 Y∈{0,1}^{n×K}，每个样本目标 y_i,k∈{0,1}。常见 Binary Relevance 方式对每个 k 训练二分类器，也可采用联合模型、分类器链。每个标签可单独设阈值 τ_k。指标包含 micro/macro F1、Hamming Loss（所有标签位错误比例）、Subset Accuracy（每条样本的整组标签完全匹配比例），后者更严格。

## 4. 工程实践与设计权衡

电商商品可同时标注“电子”“促销”“易碎”，不应强迫只保留一个标签。上线时对低频标签设置审查、分类本体的版本化和阈值校准，并检查标签并存的业务逻辑。

## 5. 关联知识与易混辨析

Multilabel 的一条样本可多个 1；Multiclass 的 one-hot 目标通常仅有一个 1；Multioutput 则是更宽泛的多个目标任务，也可包括多目标回归。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么多标签任务中的 Subset Accuracy 往往比单标签 Accuracy 低？** 答：只有该样本所有标签位都预测正确才算完全正确；即使每个标签大多正确，整组匹配概率也可能不高。

2. **问：为什么给所有标签统一 0.5 阈值不一定合理？** 答：各标签先验、误报/漏报成本和校准程度不同，可在开发集逐标签设定阈值并进行独立测试。

## 7. 中等难度考试题（含解析）

1. **题：两条样本真值 [[1,0,1],[0,1,0]]，预测 [[1,0,0],[0,1,0]]，Hamming Loss？** 解：总 2×3=6 个标签位，只错一个，因此 Hamming Loss=1/6≈16.7%。

2. **题：以上两条样本的 Subset Accuracy 是多少？** 解：第 1 条未完全匹配，第 2 条完全匹配，所以 Subset Accuracy=1/2=50%。

## 8. 权威来源与延伸阅读

- [scikit-learn Multiclass and Multilabel Guide](https://scikit-learn.org/stable/modules/multiclass.html)：用以核对原理、公式、定义与 API 实现。
- [scikit-learn Hamming Loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html)：用以核对原理、公式、定义与 API 实现。

> 数值算例属于教学题设；独立领域专家审校状态仍为 pending。
