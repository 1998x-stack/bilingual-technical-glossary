# Sigmoid Function（Sigmoid 函数）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 数学原理、技术约束与工程实践

## 1. 核心定义

Sigmoid 函数通常指逻辑函数 σ(z)=1/(1+exp(−z))，将任意实数映射到 (0,1)，是 logit 的反函数，可用于二分类概率建模或神经网络非线性激活。它单调、可微，但会在大幅值输入附近饱和，产生很小梯度。

## 2. 形象理解

像把无限长的直线挤压成一条 0 到 1 的 S 形刻度，零点映射正中间 0.5。

**类比的局限：**输出落在 0–1 不等于模型已经经过概率校准；sigmoid 单独也无法表达多个互斥类别概率总和为 1。

## 3. 技术原理与核心内容

σ'(z)=σ(z)(1−σ(z))，在 z=0 时最大为 0.25，|z| 很大时趋近 0。二元逻辑回归 p=σ(wᵀx+b)，概率是线性 logit 的非线性映射。对于大正负输入，直接计算 exp(−z) 可能溢出，可使用 scipy.special.expit 或稳定分支。深网络若反复堆叠 sigmoid，梯度可随饱和和链式乘积减弱；二分类 logits 通常直接输入 BCEWithLogitsLoss，比先 σ 再取 log 更稳定。

## 4. 工程实践与设计权衡

信用预警输出模型原始 logit，经 sigmoid 得风险概率候选，再用独立验证判断校准与阈值是否满足业务误报成本。深层表征中的隐藏层可比较 ReLU/GELU，避免多层 sigmoid 饱和。

## 5. 关联知识与易混辨析

Sigmoid 是函数，Logit 是反函数；Softmax 对 K 个类别共同归一化，K=2 且取 logit 差可得到 sigmoid；Decision Function 的 score 未必使用 sigmoid。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 sigmoid 在大正或大负输入下容易出现梯度饱和？** 答：导数 σ(1−σ)，当输出靠近 0 或 1 时导数接近 0，梯度链式传播可能变弱。

2. **问：为什么二分类训练常直接传 logits 给稳定的交叉熵实现？** 答：可以合并 sigmoid 和 log loss 做数值稳定计算，避免先把概率截断到 0/1 再取 log 的上溢或下溢。

## 7. 中等难度考试题（含解析）

1. **题：z=0，σ(z) 和导数 σ'(z) 各是多少？** 解：σ(0)=0.5，σ'(0)=0.5×0.5=0.25。

2. **题：若 z=ln3，sigmoid 输出多少？** 解：σ(ln3)=1/(1+1/3)=3/4=0.75。

## 8. 权威来源与延伸阅读

- [SciPy expit API](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expit.html)：用于核对定义、数理行为、参数或实现限制。
- [PyTorch BCEWithLogitsLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html)：用于核对定义、数理行为、参数或实现限制。

> 文中定量例题均为教学假设而非生产实测数据；独立技术专家审稿记录仍为 pending。
