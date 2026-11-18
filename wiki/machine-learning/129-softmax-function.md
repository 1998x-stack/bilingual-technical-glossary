# Softmax Function（Softmax 函数）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 数学原理、技术约束与工程实践

## 1. 核心定义

Softmax 函数把 K 个任意实数得分 z_k 变为非负且总和为 1 的概率向量：p_k=exp(z_k)/Σ_j exp(z_j)。它常用作互斥多类别模型的输出层，但“数值归一化成 1”并不保证概率与真实频率已经校准。

## 2. 形象理解

像多个候选方案各有打分，softmax 将分数转成总和为 100% 的份额；任意一个得分升高，其他份额通常下降。

**类比的局限：**同样的 logit 加到所有类别不改变输出；温度调整能改变预测分布尖锐程度，但不自动纠正所有分布偏差。

## 3. 技术原理与核心内容

为稳定计算，令 m=max_j z_j，计算 exp(z_k−m)/Σ_j exp(z_j−m)，从而避开指数溢出。给全部 z 加常数 c，概率不变；温度 T>0 定义 p_k(T)=softmax(z/T)，T 大分布较平缓，T 小分布更尖锐。交叉熵 ℓ=−ln p_y，用 LogSumExp 形式可稳定求值。K 类 softmax 与 K 个独立 sigmoid 的不同点是前者强制类别互斥。

## 4. 工程实践与设计权衡

工业缺陷分类在同一张图像只有一个主缺陷类别时使用 softmax；多个缺陷共存时应重新定义多标签输出。部署记录 `classes_` 对应关系与 T 校准版本，并保留未知类处理方案。

## 5. 关联知识与易混辨析

Softmax 是向量映射函数；Softmax Regression 指使用线性 logits 的多类模型；Sigmoid 是单标量二分类变换；Label Shift 会使原概率不再可靠，需要重新评估校准。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 softmax(z+c) 等于 softmax(z)？** 答：分子分母都乘相同的 e^c，因子抵消，因此只由各类相对 logit 差决定。

2. **问：何时不能把 softmax 概率直接当可信度？** 答：模型可能因训练分布偏差、过度自信或目标域变化而失准，需用可靠的保留集检查分箱频率与校准。

## 7. 中等难度考试题（含解析）

1. **题：logits [0,0,0] 的 softmax 是什么？** 解：每个指数为 1，分母 3，因此每类 1/3。

2. **题：logits [ln2,0] 的第一类 softmax 概率？** 解：exp(ln2)=2，exp(0)=1，第一类为 2/(2+1)=2/3。

## 8. 权威来源与延伸阅读

- [PyTorch Softmax 官方接口](https://docs.pytorch.org/docs/stable/generated/torch.nn.Softmax.html)：用于核对定义、数理行为、参数或实现限制。
- [PyTorch CrossEntropyLoss（稳定 logits 计算）](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)：用于核对定义、数理行为、参数或实现限制。

> 文中定量例题均为教学假设而非生产实测数据；独立技术专家审稿记录仍为 pending。
