# Binary Classification（二分类）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 监督目标、优化公式和工程条件

## 1. 核心定义

二分类（Binary Classification）的目标仅有两个互斥类别，通常编码为 0/1，并输出正类分数或概率后按阈值给出最终决策。正类定义、类先验、决策成本和标签成熟时间是模型指标的一部分，不能只看准确率。

## 2. 形象理解

像安检中判断“需要进一步检查”或“无需检查”，分数更像报警强弱，阈值决定多少人进入复核。

**类比的局限：**一个阈值无法同时保证高 Precision 和高 Recall；阈值选择与业务处置资源直接相关。

## 3. 技术原理与核心内容

对预测概率 p=P(Y=1|X)，简单规则是 ŷ=1[p≥τ]；统计 TP、FP、FN、TN。Precision=TP/(TP+FP)，Recall=TP/(TP+FN)，Specificity=TN/(TN+FP)。若概率校准良好且误报成本 C_FP、漏报成本 C_FN 固定，选择正类的期望损失 C_FP(1−p)，选择负类的损失 C_FN p；由此阈值 τ=C_FP/(C_FP+C_FN)。该结论依赖这些简化成本假设。

## 4. 工程实践与设计权衡

欺诈检测在人工复核资源有限时，需要评估固定每日工单量下召回率，而非默认 τ=0.5；标签延迟会影响最近时段的混淆矩阵，线上要单独标识未成熟结果。

## 5. 关联知识与易混辨析

Binary Classification 是 Multiclass K=2 的特例，但二分类单列概率与两列 softmax 输出的接口不同；Multilabel 里的每个标签也可构成独立二分类子问题。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么阈值不是模型的固有属性？** 答：阈值反映误报/漏报成本、类先验与人工处理容量；同一模型得分在不同业务目标下可以采用不同阈值。

2. **问：为什么 Accuracy=99% 在欺诈检测中仍可能很差？** 答：如果真实欺诈只有 1%，全预测正常也有 99% Accuracy，但 Recall=0，无法发现任何欺诈。

## 7. 中等难度考试题（含解析）

1. **题：TP=40、FP=10、FN=20，计算 Precision 和 Recall。** 解：Precision=40/(40+10)=80%；Recall=40/(40+20)=2/3≈66.7%。

2. **题：若 C_FP=2、C_FN=8，概率充分校准且成本只有这两项，最优理论阈值？** 解：τ=2/(2+8)=0.2；概率 p≥0.2 时判正类。实际还需考虑审核容量等约束。

## 8. 权威来源与延伸阅读

- [scikit-learn Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)：用以核对原理、公式、定义与 API 实现。
- [scikit-learn Probability Calibration](https://scikit-learn.org/stable/modules/calibration.html)：用以核对原理、公式、定义与 API 实现。

> 数值算例属于教学题设；独立领域专家审校状态仍为 pending。
