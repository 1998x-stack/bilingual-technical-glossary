# Softmax Regression（Softmax 回归）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 模型与数学定义、业务应用和边界条件

## 1. 核心定义

Softmax 回归（Softmax Regression）也称多项逻辑回归，用多个类别 logit 通过 softmax 形成互斥 K 类概率分布，通常以多类交叉熵进行训练。它与对每类独立 sigmoid 的多标签模型不同，输出概率必须总和为 1。

## 2. 形象理解

像把来自 K 个候选团队的评分转换成一张总票数固定的占比表，一个类别比例增加通常会影响其他类别比例。

**类比的局限：**Softmax 相对 logit 差值决定概率；所有 logit 同时加常数概率不变，参数化存在冗余，需要合理数值实现。

## 3. 技术原理与核心内容

令 z_k=w_kᵀx+b_k，p_k=exp(z_k)/Σ_jexp(z_j)。稳定实现先设 m=max_j z_j，计算 exp(z_k−m)/Σ_jexp(z_j−m)。对真实类 y 的交叉熵 ℓ=−ln p_y。训练可采用 L2 正则；线性分界满足 z_i=z_j 的超平面（多类最终 argmax 的区域交界由相邻有效竞争类决定）。

## 4. 工程实践与设计权衡

售后工单若必须从“退货、换货、咨询、投诉”选一类，可用 Softmax 分类器；真实业务若一单可包含多意图，应重新定义为多标签或层级任务。分群校准与新增类别处理需在部署契约中明确。

## 5. 关联知识与易混辨析

Softmax Regression 是多类互斥逻辑模型；Binary Logistic Regression 用单个 sigmoid（也可用两类 softmax 等价表示）；One-vs-Rest 独立拟合 K 个二分类器，不必与联合 softmax 同结果。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 softmax 比对 K 个独立 sigmoid 更适用于单标签多类任务？** 答：softmax 的分母耦合所有类别并保证分布总和为 1，符合互斥标签定义；独立 sigmoid 允许同时多个高分。

2. **问：为何必须对 logit 减去最大值再做 exp？** 答：防止大正 logit 指数溢出；同加减常数对 softmax 比值无影响，预测概率保持不变。

## 7. 中等难度考试题（含解析）

1. **题：logit [0,0,0] 的概率是什么？** 解：三个指数都为 1，得到 [1/3,1/3,1/3]。

2. **题：logit [ln2,0] 的 Softmax 正类 0 概率是多少？** 解：指数分别 2、1，p0=2/(2+1)=2/3；p1=1/3。

## 8. 权威来源与延伸阅读

- [scikit-learn Logistic Regression Guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)：可核验该模型目标、数学式和实际实现的适用条件。
- [PyTorch CrossEntropyLoss API](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)：可核验该模型目标、数学式和实际实现的适用条件。

> 算例为教学假设，不代表真实业务性能；专业独立审稿状态仍为 pending。
