# Generalized Linear Model (GLM)（广义线性模型 · GLM）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 模型与数学定义、业务应用和边界条件

## 1. 核心定义

广义线性模型（Generalized Linear Model，GLM）是以指数族响应分布、线性预测器和链接函数组织的一类统计回归模型。它允许响应不是正态连续量，如伯努利事件或泊松计数；模型的分布/方差假设需要与数据生成机制匹配。

## 2. 形象理解

像给不同类型测量任务换不同刻度盘：连续温度、事件是否发生、一天订单数的输出分布不同，但背后仍可共享线性特征组合。

**类比的局限：**GLM 不意味着任意非线性都能表达：线性预测器仍限制在指定的特征空间，错误链接函数或方差关系会影响解释和推断。

## 3. 技术原理与核心内容

形式 g(E[Y|X=x])=xᵀβ+b，其中 g 为链接，响应通常来自指数族。高斯-恒等链接得到常见线性回归；伯努利-logit 链接对应二项 Logistic；泊松-log 链接对应计数率模型。GLM 通过极大似然或相应偏差最小化拟合，需根据任务选择方差函数与离散参数；不能仅以预测误差证明分布假设精确。

## 4. 工程实践与设计权衡

医院按病种建就诊次数模型可用 Poisson GLM，但若大量零值或条件方差明显大于均值，需检查过度离散、暴露时长、负二项或零膨胀变体。

## 5. 关联知识与易混辨析

GLM 是统一框架；Linear Regression、Logistic Regression、Poisson Regression 都可在合适链接下纳入；与任意非参数模型不同，GLM 有明确分布和线性预测结构。

## 6. 中等难度面试题（含参考答案）

1. **问：GLM 中链接函数为什么不是简单的后处理装饰？** 答：它把条件均值映射到无约束的线性预测器，决定预测均值如何随特征变化及其适用取值域。

2. **问：为什么计数型目标不一定适合普通高斯线性回归？** 答：线性预测可能为负，且计数的方差与均值关系不同；Poisson 等 GLM 提供更合适的均值链接和似然，但需检验过度离散。

## 7. 中等难度考试题（含解析）

1. **题：若 log-link 的线性预测器 η=ln4，预测条件均值 μ 是多少？** 解：μ=exp(η)=4，天然为正。

2. **题：Bernoulli-logit GLM 的 η=0，对应事件概率是多少？** 解：inverse-logit(0)=0.5。

## 8. 权威来源与延伸阅读

- [scikit-learn Generalized Linear Models 指南](https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-models)：可核验该模型目标、数学式和实际实现的适用条件。
- [scikit-learn TweedieRegressor 官方 API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html)：可核验该模型目标、数学式和实际实现的适用条件。

> 算例为教学假设，不代表真实业务性能；专业独立审稿状态仍为 pending。
