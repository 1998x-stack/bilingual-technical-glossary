# Out-of-bag Error (OOB)（袋外误差 · OOB）

> 领域：机器学习 · 专题：树模型与集成学习 · 一手研究与实现、真实工程约束、可复算例题

## 1. 核心定义

袋外误差（Out-of-bag Error，OOB）是针对使用 Bootstrap 重采样训练的 Bagging/随机森林，利用某条原样本未被某些基模型选入训练的事实，用这些树对该样本的预测构成内部泛化估计。它可以减少额外随机验证集的需要，但不是与训练实体完全无关的外部测试。

## 2. 形象理解

像每位老师只教自己抽到的一部分学生，评估某学生时只听那些从未教过他的老师给出的答案，避免直接用授课过的学生测教学效果。

**类比的局限：**不同 OOB 模型仍共享别的样本；当同一用户多条记录跨各次重采样、或时间上存在未来信息时，OOB 可能大幅高估真正新用户或未来部署性能。

## 3. 技术原理与核心内容

n-out-of-n Bootstrap 中单条原记录未被一棵树抽中的概率 p_oob=(1−1/n)^n≈e^(−1)=0.368。对记录 i 收集 OOB_i={b: i∉S_b}，以这些模型预测聚合得到 ŷ_i^OOB，计算平均误差或分数。当 B 较少时某些记录可能没有 OOB 预测，scikit-learn 相关指标会出现覆盖不足警告；树数足够多、数据近似 iid 时 OOB 是实用近似。scikit-learn RF 的 `oob_score=True` 要求 `bootstrap=True`，而 ExtraTrees 默认不开 Bootstrap。

## 4. 工程实践与设计权衡

生产反欺诈随机森林可以用 OOB 作为快速调参辅助，但必须保留时间分割的真实客户测试。对同用户存在大量交易记录的情况，OOB 只排除单行不等于排除同用户相关交易。

## 5. 关联知识与易混辨析

OOB 是 Bootstrap 训练下内部验证机制；Cross-validation 显式重新划分训练验证；Out-of-time Test 是未来时段保留集，OOB 不自动替代。OOB error 与 OOB score 指标方向不同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么随机森林 OOB 不是完全无偏的独立未来测试？** 答：OOB 排除了某条训练记录，却不保证排除相同用户、设备、时间相关记录；同时基于 OOB 反复选择超参也引入选择偏差。

2. **问：什么情况下 OOB 分数可能不可计算或不稳定？** 答：如果 bootstrap=False 就无 OOB 定义；如果树数量太少，一些训练样本可能没有任何 OOB 预测，产生不稳定估计。

## 7. 中等难度考试题（含解析）

1. **题：n=2 时一条固定样本对单棵树的 OOB 概率是多少？** 解：(1−1/2)^2=0.25；大 n 的 0.368 只是近似。

2. **题：n 很大、B=100 时一个给定训练样本平均被多少棵树排除？** 解：约 100×e^(−1)≈36.8 棵，实际数量随机，并非精确 37。

## 8. 权威来源与延伸阅读

- [scikit-learn OOB Errors 示例](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html)：用于追溯该术语的算法定义、论文及可核查实现。
- [scikit-learn RandomForestClassifier oob_score 文档](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)：用于追溯该术语的算法定义、论文及可核查实现。

> 数值题为明确设定的教学案例，非真实业务指标。独立专业领域专家审核仍为 pending。
