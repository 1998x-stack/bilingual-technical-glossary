# Robust Regression（稳健回归）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 模型与数学定义、业务应用和边界条件

## 1. 核心定义

稳健回归（Robust Regression）旨在降低少数异常观测、异常残差或某些模型误设对回归估计的过度影响。常见方法包括 Huber 损失、RANSAC 与 Theil–Sen；不同方法的异常模型和统计假设不同，不能泛化为一种万能修复。

## 2. 形象理解

像给整体平均判断加一层异常审核：一个明显错误的仪器读数不应完全支配拟合直线，但也不能直接把珍贵的罕见事件当错误。

**类比的局限：**异常点可能是真实关键风险样本，鲁棒算法的低权重处理会损害该类业务目标；RANSAC 还依赖内点比例及阈值设置。

## 3. 技术原理与核心内容

Huber 损失常定义为 L_δ(r)=0.5r²（|r|≤δ），δ(|r|−0.5δ)（|r|>δ），使大残差惩罚由平方增长转线性增长。RANSAC 通过反复抽取最小子集拟合与统计共识内点，要求足够内点与合理残差阈值；Theil–Sen 使用子样本拟合的稳健汇总。稳健损失不能自行修正 X 的测量误差或时间后验泄漏。

## 4. 工程实践与设计权衡

工厂温度与电耗回归中，少量传感器故障可能造成极大目标残差，可比较 Huber、RANSAC 与 OLS 在独立设备测试的表现；结合质量标记核实异常来源并说明丢弃风险。

## 5. 关联知识与易混辨析

Robust Regression 是一类降低离群影响的方法；Huber Loss 是一种损失函数；Quantile Regression 主要针对条件分位点；Robust Scaling 只调整输入尺度而非直接改变损失。

## 6. 中等难度面试题（含参考答案）

1. **问：Huber 损失为什么兼具 L2 与 L1 的部分性质？** 答：小残差区二次形式有平滑优化优势，大残差区线性增长减轻极端点的主导作用；δ 控制切换范围。

2. **问：RANSAC 为什么在高度污染数据下可能失败？** 答：当内点过少、阈值错误或抽样次数不足时，难以抽到纯内点子集；含多个真实机制时还可能选择错误共识模型。

## 7. 中等难度考试题（含解析）

1. **题：Huber δ=2，残差 r=1 的损失是多少？** 解：|r|≤2，损失=0.5×1²=0.5。

2. **题：Huber δ=2，残差 r=5 的损失？** 解：因为 5>2，L=2×(5−1)=8；而普通半平方损失为 0.5×25=12.5。

## 8. 权威来源与延伸阅读

- [scikit-learn HuberRegressor 官方 API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html)：可核验该模型目标、数学式和实际实现的适用条件。
- [scikit-learn Robustness Regression 指南](https://scikit-learn.org/stable/modules/linear_model.html#robustness-regression-outliers-and-modeling-errors)：可核验该模型目标、数学式和实际实现的适用条件。

> 算例为教学假设，不代表真实业务性能；专业独立审稿状态仍为 pending。
