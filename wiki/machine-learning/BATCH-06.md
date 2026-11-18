# Machine Learning · Batch 06 学习路径（126–150）

> 编辑/教学内部资料。依据 [机器学习中英术语权威序列](../../glossaries/machine-learning.md) 构建，不在 GitHub Pages 创建 /wiki 独立首页。正式读者仍通过统一 Explorer → term.html 获取已公开的文章。

## 主线一（126–133）：评分函数到线性模型可识别性

- **Decision Function vs Decision Boundary**：决策函数输出实数 score，阈值/argmax 决定类别；不能将 SVM 的 margin 当校准概率。
- **Logit** 是 log[p/(1−p)]，**Sigmoid** 是反函数；Logistic 的 β 对应 log-odds 变化，exp(β) 是 odds ratio，而不是概率直接增量。
- **Softmax** 将 K 维 logit 变为互斥类别分布，数值计算应减去最大 logit；单独的 K 个 sigmoid 则用于多标签等不同设置。
- **Residual** 是观测响应减拟合值，与生成模型的误差项 ε 不完全相同；**Coefficient/Intercept** 的解释依赖单位、参考组与中心化；**Multicollinearity** 是列之间线性依赖，VIF=1/(1−R²)，标准化不修复秩亏。

## 主线二（134–142）：一棵决策树怎样训练与变复杂

- **Root Node** 是根，可能同时为内部节点，也可能直接是唯一叶；**Internal Node** 执行条件判断；**Leaf Node** 存储预测分布或统计量。**Tree Depth** 根为 0，满二叉树深 d 最多 2^d 叶。
- **Split Criterion** 比较父不纯度与加权子不纯度；**Gini** 二分类为 2p(1−p)，K 类最大 1−1/K；**Information Gain** 使用 entropy，单位取决于 log 底。
- **Tree Pruning** 包括预剪枝和代价复杂度后剪枝，J_α(T)=R(T)+α|Leaves(T)|。必须在训练开发折选择 α，而不是用最终测试集选枝。

## 主线三（143–150）：并行降方差与逐轮纠错的差别

- **Bootstrap Sampling** 是 n 次有放回抽样，某记录 OOB 概率 (1−1/n)^n，n 大时约 36.8%；不能把抽出的 n 条重复行当成 n 条新独立观测。
- **Bagging** 训练多棵重采样基模型并平均，主要降低预测方差；**Random Forest** 进一步在每节点随机筛选候选特征。
- **Extra Trees** 对候选阈值也引入随机性，sklearn 默认 bootstrap=False，不默认提供 OOB 分数；与 Random Forest **不可视为相同方法**。
- **Boosting** 串行训练；**AdaBoost** 通过错分样本权重更新；**Gradient Boosting** 在函数空间沿负梯度修正；**GBDT** 用回归树作为弱模型。平方半损失下负梯度等于 y−F，分类对数损失不能简单套用硬分类残差。
- **GBDT vs Random Forest**：前者阶段性累加纠错，后者是并行树聚合；调参时要联合考虑树深、叶支持、学习率、轮数、时间泛化和缺失值支持。

## 复合工程案例：面向新客户的信用评分与反欺诈

1. 用户与时间隔离训练和验证，保持事件时点特征可用性。构建 Logistic + 标准化/类别编码的强基线，将决策 score、校准概率、阈值及决策动作分别记录。
2. 对线性基线检查输入共线性、系数稳定性、残差/错误分布；任何关于年龄、地区等变量的因果结论都必须与纯预测相关性区分。
3. 用 Gini/Entropy 调整浅决策树，以 CV 调剪枝参数并检查低覆盖叶及少数用户群；不依赖训练叶 100% 纯度声称概率可信。
4. 比较单树、RandomForest、ExtraTrees、AdaBoost、GBDT 在未来时间窗上的 PR-AUC、校准、人工复核成本和 P95 延迟。OOB 估计不代替真正的新用户外部测试。
5. 验收 Gradient Boosting 的原始 Friedman 论文、Breiman Random Forests、Freund–Schapire AdaBoost、Geurts Extra Trees 与 sklearn 现行 API，特别关注 ExtraTrees 默认 Bootstrap 行为和随机森林软投票的真实实现。

## 专项专业复核

所有 25 篇包含 2 道中等面试问答与 2 道中等考试题及解析。关键可复算案例包括 logit/sigmoid、Gini/entropy、叶数上界、Bootstrap OOB、VIF、AdaBoost alpha、GBDT 分阶段更新。自动 CI 只验证结构和部分公式，150 条的专业审稿台账全部保留 pending，绝不伪造专家签名。
