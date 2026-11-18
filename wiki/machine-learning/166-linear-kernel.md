# Linear Kernel（线性核）

> 领域：机器学习 · 专题：支持向量机、核方法与近邻 · 数学形式、优化条件与独立评估

## 1. 核心定义

线性核（Linear Kernel）是 K(x,z)=xᵀz 的核函数，等价于直接使用原始特征的内积，通常不引入非线性的隐式映射。在线性 SVM 中它形成输入空间的超平面，适用于许多高维稀疏文本和可被原始线性边界有效区分的任务。

## 2. 形象理解

像比较两份文档的各词向量：每个对应词的数值相乘再相加，词的维度本身就是核使用的显式坐标。

**类比的局限：**相同线性核不代表不同软件的 LinearSVC 与 SVC(kernel='linear') 会给出完全相同的模型：损失、正则、截距处理和求解器可以不同。

## 3. 技术原理与核心内容

K(x,z)=Σ_j x_j z_j，K(x,x)=||x||²；对于 SVM 对偶 f(x)=Σ_i α_i y_i x_iᵀx+b，可重排为 wᵀx+b，其中 w=Σ_iα_i y_i x_i，因此无需逐个计算核即可在线 O(d) 预测。LinearSVC 通常在原始线性参数空间用 liblinear 等方法求解，与核 SVC 在损失形式、默认参数和多类策略上可能不同。线性核值受缩放影响，稀疏矩阵可高效点积。

## 4. 工程实践与设计权衡

千万维稀疏词袋或 TF–IDF 文本通常优先测试 LinearSVC/SGD 线性分类器，训练与推理可利用稀疏结构；把 `kernel='linear'` 的 SVC 当作大量样本天然快的解决方案可能导致训练成本失控。

## 5. 关联知识与易混辨析

Linear Kernel 是具体核 K=xᵀz；Kernel Trick 是更一般的内积替换；Polynomial 与 RBF 可产生输入空间非线性决策面；Cosine Similarity 会按向量范数归一化。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么线性核 SVM 可以把支持向量加权和合并成一个 w？** 答：因为内积满足线性性，Σ_i α_i y_i(x_iᵀx)=(Σ_iα_i y_i x_i)ᵀx；因此可预先计算模型权重。

2. **问：LinearSVC 与 SVC(kernel='linear') 是否一定等价？** 答：不能保证。默认 hinge 与 squared hinge、C 缩放、截距和一对多/一对一等求解细节可能不同，需具体设置对照。

## 7. 中等难度考试题（含解析）

1. **题：x=(1,2)、z=(3,−1)，线性核是多少？** 解：K=1×3+2×(−1)=1。

2. **题：若支持向量 x₁=(1,0)、x₂=(0,2)，α₁y₁=2、α₂y₂=−0.5，则聚合 w？** 解：w=2×(1,0)−0.5×(0,2)=(2,−1)，故 f(x)=2x₁−x₂+b。

## 8. 权威来源与延伸阅读

- [scikit-learn Support Vector Machines 完整数学指南](https://scikit-learn.org/stable/modules/svm.html)：用于核查正式数学定义、原始论文或官方求解器行为。
- [scikit-learn LinearSVC API](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)：用于核查正式数学定义、原始论文或官方求解器行为。

> 数值算例为教学题设，不代表线上实验。独立专家技术审核状态仍为 pending。
