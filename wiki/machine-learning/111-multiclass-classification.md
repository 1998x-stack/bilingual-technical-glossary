# Multiclass Classification（多类别分类）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 监督目标、优化公式和工程条件

## 1. 核心定义

多类别分类（Multiclass Classification）是每个样本恰属于 K≥3 个互斥类别之一的监督任务，预测时可输出 K 维得分或概率分布。与多标签任务不同，同一样本不能在同一标签维度被多个互斥类同时判为真。

## 2. 形象理解

像将交通标志识别为“限速”“停车”“让行”中的一个类别，每张输入图片只对应指定的单一主类。

**类比的局限：**现实图片可能含多个交通标志；此时需要对象检测或多标签定义，而不能强制单标签分类解决所有需求。

## 3. 技术原理与核心内容

模型给每个类别 logit z_k，可经 softmax 得 p_k=exp(z_k)/Σ_jexp(z_j)，数值实现应减去 max(z) 避免溢出。交叉熵对真实类别 y 记为 −log p_y。One-vs-Rest 与多项式 Logistic/Softmax 都可用于多类；宏平均 F1 对各类别同权，微平均汇总样本计数，应说明分类不平衡对指标的影响。

## 4. 工程实践与设计权衡

工业故障诊断若每条告警必须选择唯一故障码，可用多类分类；未知故障需人工复核或拒判机制，不能硬把全新故障映射到已有类别。关注稀有故障召回与误报成本。

## 5. 关联知识与易混辨析

Multiclass 每行恰一类；Multilabel 可多个独立标签同时为真；Multioutput 可有多个独立目标变量，每个目标又可能是多类。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么多类 Softmax 输出概率之和为 1？** 答：它将每个类别的指数得分除以所有类别指数和，因此非负且总和为 1，表达互斥类别分布。

2. **问：多类问题应只看 Micro-F1 吗？** 答：不应。单标签多类中 Micro-F1 可能退化为 Accuracy，掩盖稀有类；应补充 Macro-F1、各类 Recall 和混淆矩阵。

## 7. 中等难度考试题（含解析）

1. **题：三类 logit [0,0,0]，softmax 概率各是多少？** 解：每类 exp(0)=1，分母为 3，故都是 1/3。

2. **题：真实类别为索引 1，模型该类概率 0.25，交叉熵损失多少？** 解：−ln(0.25)=ln4≈1.3863，单位为 nats；假设采用自然对数。

## 8. 权威来源与延伸阅读

- [scikit-learn Multiclass and Multilabel](https://scikit-learn.org/stable/modules/multiclass.html)：用以核对原理、公式、定义与 API 实现。
- [scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)：用以核对原理、公式、定义与 API 实现。

> 数值算例属于教学题设；独立领域专家审校状态仍为 pending。
