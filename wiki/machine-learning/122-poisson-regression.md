# Poisson Regression（泊松回归）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 模型与数学定义、业务应用和边界条件

## 1. 核心定义

泊松回归（Poisson Regression）是用于计数响应或事件发生率的广义线性模型，常假设在给定特征下 Y 服从泊松分布，条件均值 μ>0，通过 log 链接与输入线性预测器关联。真实任务需核验过度离散、零膨胀和暴露量差异。

## 2. 形象理解

像预测一小时内服务台将接待多少客户：输出是期望事件数，不能出现负人数。

**类比的局限：**泊松假设要求在条件给定时均值等于方差；实际事件可能成簇，使方差大于均值，需要其他统计模型。

## 3. 技术原理与核心内容

典型模型 Y|X∼Poisson(μ)，μ=exp(xᵀβ+b)，P(Y=k)=e^(−μ)μ^k/k!。若观察时长/人口基数不同，可设 offset=ln(exposure)，使 μ=exposure×exp(xᵀβ+b)；将暴露量当普通可训练特征不等于固定系数为 1 的 offset。泊松 deviance 是常用评价目标，y 必须非负，系数解释为乘法性的发生率比。

## 4. 工程实践与设计权衡

预测餐厅每天来客数需要记录营业时长，短营业日与长营业日应使用 exposure 或合适率归一；若方差显著大于均值，应考虑负二项、稳健误差或改进特征，不能只继续加大正则。

## 5. 关联知识与易混辨析

Poisson Regression 是 GLM 的计数成员；Logistic Regression 建模二值事件概率；OLS 可能预测负数；Quantile Regression 建模分位数而不预设泊松均值方差。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么给模型加对数暴露量 offset 与直接加入暴露量特征不同？** 答：offset 固定 ln(exposure) 的系数为 1，使期望计数与暴露时间成比例；普通特征会学习任意系数，不能保证正确率模型。

2. **问：泊松均值为 4，但观测条件方差约 25，说明什么？** 答：条件过度离散，简单泊松方差=均值的假设不合适；需检查群体异质性、聚集事件或负二项替代。

## 7. 中等难度考试题（含解析）

1. **题：若 μ=2，泊松零次事件概率是多少？** 解：P(Y=0)=e^(−2)≈0.1353。

2. **题：单位小时期望 3 次，暴露时长 2 小时且率恒定，预期事件数？** 解：μ=3×2=6 次；需要在目标/参数中采用 exposure。

## 8. 权威来源与延伸阅读

- [scikit-learn PoissonRegressor 官方 API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html)：可核验该模型目标、数学式和实际实现的适用条件。
- [scikit-learn GLM 与 Poisson 损失指南](https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-models)：可核验该模型目标、数学式和实际实现的适用条件。

> 算例为教学假设，不代表真实业务性能；专业独立审稿状态仍为 pending。
