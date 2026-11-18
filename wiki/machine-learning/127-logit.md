# Logit（对数几率）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 数学原理、技术约束与工程实践

## 1. 核心定义

对数几率（Logit）是将二元事件概率 p∈(0,1) 映射为实数 ln[p/(1−p)] 的函数，是伯努利广义线性模型的典型链接函数。它衡量“发生”相对“不发生”的对数优势比，不是普通对数概率 ln p，也不是线性概率本身。

## 2. 形象理解

把事件发生与不发生的‘票数比’先算成 odds，再取对数：两种结果势均力敌时 logit 为零，正值偏向发生，负值偏向不发生。

**类比的局限：**当 p 逼近 0 或 1，logit 向正负无穷延伸；若直接对精确的 0 或 1 取 logit 会发生数值问题。

## 3. 技术原理与核心内容

odds=p/(1−p)，logit(p)=ln(p)−ln(1−p)，其反函数 sigmoid(z)=1/(1+e^(−z))。逻辑回归假设 logit(P(Y=1|X=x))=wᵀx+b；其他特征固定时 x_j 增 1，odds 乘 e^{w_j}，并不意味着概率恒定增加 w_j。若类先验移位，概率修正往往影响截距或偏移项；数值实现可用 logit/expit 的稳定函数。

## 4. 工程实践与设计权衡

医疗风险模型可报告调整后的优势比 exp(β) 并清楚标注观测关联不是因果效应；若患病率极低，odds ratio 与 risk ratio 可能接近但并不严格相同。

## 5. 关联知识与易混辨析

Logit 是概率到实数的变换，Sigmoid 是其反变换；Log-Odds 不同于 Log Probability；Coefficient 决定 log-odds 的单位变化，Intercept 是参考输入下的 log-odds。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么逻辑回归 β=0.7 不能直接说概率增加 70%？** 答：β 是 log-odds 的增加，优势比乘 e^0.7≈2.01；概率变化取决于起始概率，必须通过 sigmoid 计算。

2. **问：为什么数据极度不平衡时更要区分 odds 与 probability？** 答：odds=p/(1−p)，只有 p 很小时近似 p；错误混同可能造成风险、阈值和成本解释错误。

## 7. 中等难度考试题（含解析）

1. **题：p=0.8 时 odds 和 logit 分别是多少？** 解：odds=0.8/0.2=4，logit=ln4≈1.3863。

2. **题：若 logit 为 0，事件概率是多少？** 解：p=1/(1+e^0)=0.5；正负两类的 odds=1。

## 8. 权威来源与延伸阅读

- [SciPy special logit 官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.logit.html)：用于核对定义、数理行为、参数或实现限制。
- [scikit-learn Logistic Regression Guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)：用于核对定义、数理行为、参数或实现限制。

> 文中定量例题均为教学假设而非生产实测数据；独立技术专家审稿记录仍为 pending。
