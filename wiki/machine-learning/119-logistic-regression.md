# Logistic Regression（逻辑回归）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 模型与数学定义、业务应用和边界条件

## 1. 核心定义

逻辑回归（Logistic Regression）是用线性预测器的 sigmoid 链接映射二分类事件概率的判别式模型。尽管名称中含 Regression，它通常解决二分类问题；在合理假设下可以解释条件对数优势比，但不能据此自动作因果推断。

## 2. 形象理解

像把一个可能取任意实数的风险打分放进 S 形压缩器，将它映射到 0–1 之间的概率刻度。

**类比的局限：**线性的是 log-odds 而不是概率本身；模型可能预测很确定却没有校准，稀有事件的阈值也通常不是 0.5。

## 3. 技术原理与核心内容

设 z=wᵀx+b，p=P(Y=1|x)=σ(z)=1/(1+exp(−z))，log[p/(1−p)]=z。二元对数损失为 −[y ln p+(1−y)ln(1−p)]，可加 L1/L2 惩罚。数值训练应使用稳定的 logaddexp/交叉熵实现以避免 p 接近 0/1 时溢出。对训练类先验与部署先验不同的情形，应评估概率校准与阈值；scikit-learn 不同 solver 对惩罚支持不完全相同。

## 4. 工程实践与设计权衡

保险违约模型以用户级分组与时间窗测试，标准化连续变量、编码类别并把所有变换放入 Pipeline；在线上以校准概率和业务误报成本决定人工审核，不把系数误解释为自动干预收益。

## 5. 关联知识与易混辨析

Logistic Regression 处理二分类概率；Linear Regression 直接预测连续均值；Softmax Regression 是多类推广；GLM 更一般地包含分布族与链接函数。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 logistic regression 的系数含义是 log-odds 而不是概率增量？** 答：每增加一单位 x_j（其他条件固定），log-odds 增加 w_j，odds 乘 exp(w_j)；概率变化依赖原有基线 p，不是常数。

2. **问：为什么高 Accuracy 不代表良好的概率校准？** 答：阈值分类只检查离散结果；若预测概率 0.9 的样本仅约 0.6 发生事件，虽然分类可能正确，概率仍失准。

## 7. 中等难度考试题（含解析）

1. **题：若 z=0，sigmoid 概率是多少？** 解：σ(0)=1/(1+1)=0.5。

2. **题：二分类标签 y=1、预测 p=0.8，单样本负对数似然是多少？** 解：−ln(0.8)≈0.22314，使用自然对数，且不含额外正则项。

## 8. 权威来源与延伸阅读

- [scikit-learn LogisticRegression API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)：可核验该模型目标、数学式和实际实现的适用条件。
- [scikit-learn Logistic Regression 用户指南](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)：可核验该模型目标、数学式和实际实现的适用条件。

> 算例为教学假设，不代表真实业务性能；专业独立审稿状态仍为 pending。
