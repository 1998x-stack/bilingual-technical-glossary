# Split Criterion（划分准则）

> 领域：机器学习 · 专题：树模型与集成学习 · 树结构、训练准则与统计边界

## 1. 核心定义

划分准则（Split Criterion）是在决策树训练中评价某个候选特征与阈值分裂效果的目标函数，通常以父节点不纯度减少或子节点加权损失衡量。分类任务常见 Gini、entropy/log_loss，回归任务常见 squared_error、absolute_error 或 Poisson 等；准则不同可能得到不同树。

## 2. 形象理解

像决定把学生分进哪两个辅导班，尝试不同分组方式并计算分组后‘水平是否更一致’，选择改进最大的划法。

**类比的局限：**一次贪心选择不一定形成全局最优整树，且训练准则最优不代表部署指标或公平性最优。

## 3. 技术原理与核心内容

对节点 t 的候选 split，ΔI=I(t)−(n_L/n_t)I(L)−(n_R/n_t)I(R)。分类 Gini=1−Σp_k²，entropy=−Σp_k log p_k；回归平方不纯度为子节点目标围绕均值的 MSE。样本权重会替换普通样本比例；合法分裂还受 min_samples_leaf、min_impurity_decrease、单调约束等条件。相同加权不纯度可出现不同 tie-breaking，因此 random_state 与候选排序也影响复现。

## 4. 工程实践与设计权衡

客户流失树若训练正类占比很低，可试类别权重和 Gini/entropy，再在固定时间测试中观察 Recall 与 PR-AUC；不能假设最大化训练熵下降就必然优化 PR-AUC。

## 5. 关联知识与易混辨析

Split Criterion 是评价候选分裂的方法；Gini Impurity 与 Entropy 是具体分类不纯度；Information Gain 常指基于熵的减少；Tree Pruning 则在建树之后选择更简单子树。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么最大化 Gini 减少量不一定最小化测试分类错误？** 答：它是局部训练不纯度的代理，有限数据和贪心决策会过拟合；要独立验证最终损失。

2. **问：带样本权重的树分裂为什么不能简单按原始样本条数加权？** 答：每条样本对训练目标的贡献已被权重改变，正确的子节点权重占比必须使用权重之和，否则与优化准则不一致。

## 7. 中等难度考试题（含解析）

1. **题：父不纯度 0.5，两个孩子各占一半，子不纯度 0.2 与 0.4，下降量？** 解：子加权不纯度=0.5×0.2+0.5×0.4=0.3，下降 Δ=0.5−0.3=0.2。

2. **题：回归子节点目标 [2,4]，以 MSE 作不纯度，值多少？** 解：均值 3，MSE=((2−3)^2+(4−3)^2)/2=(1+1)/2=1。

## 8. 权威来源与延伸阅读

- [scikit-learn 决策树用户指南](https://scikit-learn.org/stable/modules/tree.html)：核对训练算法、数理定义及 API 行为。
- [scikit-learn DecisionTreeClassifier 官方 API](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)：核对训练算法、数理定义及 API 行为。

> 教学数字是明确算例，非真实工业性能；独立专业审稿仍为 pending。
