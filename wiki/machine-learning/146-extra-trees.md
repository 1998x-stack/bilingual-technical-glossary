# Extra Trees（极端随机树）

> 领域：机器学习 · 专题：树模型与集成学习 · 理论、数学与工业决策

## 1. 核心定义

极端随机树（Extra Trees，Extremely Randomized Trees）是一类树集成方法，在随机选取候选特征之外，还对候选分裂阈值进行随机化，再在这些随机候选中挑选较优者，以进一步增加树多样性。scikit-learn ExtraTreesClassifier 默认 `bootstrap=False`，不能直接等同随机森林使用的 Bootstrap 方案。

## 2. 形象理解

像不同调查员不仅各自询问不同问题，还随机选择问题的分界分数，再从这些随机方案中选一套较合适的，最终汇总。

**类比的局限：**随机阈值增加偏差的风险，特别是细粒度数据；更快的训练并不保证所有任务准确率高或内存一定更少。

## 3. 技术原理与核心内容

在节点内随机采集 mtry 个候选特征，对各特征采随机阈值（受合法数据范围与缺失规则约束），选择训练不纯度减少较好的候选。与 RandomForest 的通常搜索相对最佳阈值不同，ExtraTrees 通过阈值随机性降低树间相关；若设置 bootstrap=True 也能使用有放回采样，但 scikit-learn 默认使用全部训练样本构造每棵树。OOB 指标需启用 bootstrap 才适用。

## 4. 工程实践与设计权衡

高维设备传感器表格可以比较 ExtraTrees、RandomForest、HistGradientBoosting 在时间测试的 PR-AUC、训练延时与内存。高噪声数据随机阈值的表现需经过多个种子重复评估。

## 5. 关联知识与易混辨析

Extra Trees 的主要随机性是阈值随机化；Random Forest 主要在样本与候选特征上随机化并搜索阈值；Bagging 是更一般的抽样聚合框架；GBDT 是逐轮纠错的加性树。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Extra Trees 与 Random Forest 不应被笼统称为完全相同算法？** 答：Extra Trees 在节点划分阈值引入额外随机性，且 scikit-learn 默认不使用 Bootstrap；两者拟合与方差—偏差行为因此不同。

2. **问：ExtraTreesClassifier 若未设 bootstrap=True，可以计算标准 OOB 分数吗？** 答：不能。无 Bootstrap 时没有每棵树未抽中的样本子集，OOB_score 依赖 bootstrap=True。

## 7. 中等难度考试题（含解析）

1. **题：Extra Trees 一棵树对 3 个随机候选阈值计算不纯度减少 [0.08,0.12,0.10]，选哪个？** 解：按收益最大准则选择 0.12；前提是三个候选合法且同一训练目标。

2. **题：100 棵 Extra Trees 各给回归输出 5，等权平均结果是什么？** 解：仍为 5；随机性产生多样性，但相同预测不会因数量而改变值。

## 8. 权威来源与延伸阅读

- [scikit-learn ExtraTreesClassifier API](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)：追踪正式定义、原始算法论文与实现限制。
- [Geurts 等 2006 Extremely Randomized Trees 论文 DOI](https://doi.org/10.1007/s10994-006-6226-1)：追踪正式定义、原始算法论文与实现限制。

> 数字演算是教学示例，不代表真实工业数据；独立人类专家审稿状态仍为 pending。
