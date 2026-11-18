# 机器学习 · 深度 Wiki 内部批次路线图

> 唯一权威词序：[机器学习术语原稿](../../glossaries/machine-learning.md) · **447 条 / 19 专题 / 18 批**。本目录供内部编辑与复核，不作为公众独立 Wiki 入口。

每批连续 **25** 条（末批 **22**），保持原始章节、英文名称与中文译名，不按章节重置全局编号。每篇含精准定义与适用边界、形象类比及局限、算法机制、工程实践及失败模式、相邻术语辨析、**2 道中等面试问答 + 2 道中等考试题及推导**、至少两项可追溯一手来源。每批独立 PR；专家审核记为 pending 直至真实审核人签署。

| 批次 | 全局编号 | 覆盖主题 | 术语数 | 生产状态 |
|---|---|---|---:|---|
| 01 | 001–025 | 基础概念与学习范式 / 数据、样本与数据集划分 | 25 | merged |
| 02 | 026–050 | 数据、样本与数据集划分 | 25 | merged |
| 03 | 051–075 | 数据、样本与数据集划分 / 数据预处理与特征工程 | 25 | merged |
| 04 | 076–100 | 数据预处理与特征工程 / 统计学习与泛化理论 | 25 | merged |
| 05 | 101–125 | 统计学习与泛化理论 / 回归、分类与线性模型 | 25 | drafted_in_pr |
| 06 | 126–150 | 回归、分类与线性模型 / 树模型与集成学习 | 25 | planned |
| 07 | 151–175 | 树模型与集成学习 / 支持向量机、核方法与近邻 | 25 | planned |
| 08 | 176–200 | 支持向量机、核方法与近邻 / 概率模型与统计推断 | 25 | planned |
| 09 | 201–225 | 概率模型与统计推断 / 无监督学习与聚类 | 25 | planned |
| 10 | 226–250 | 降维、分解与流形学习 / 优化算法与模型训练 | 25 | planned |
| 11 | 251–275 | 优化算法与模型训练 | 25 | planned |
| 12 | 276–300 | 损失函数与回归评估 / 分类指标与概率校准 | 25 | planned |
| 13 | 301–325 | 分类指标与概率校准 / 调参与模型选择 | 25 | planned |
| 14 | 326–350 | 调参与模型选择 / 时间序列与预测 / 推荐系统与排序学习 | 25 | planned |
| 15 | 351–375 | 推荐系统与排序学习 / 深度学习相关核心术语 | 25 | planned |
| 16 | 376–400 | 深度学习相关核心术语 / 机器学习工程与生产部署 | 25 | planned |
| 17 | 401–425 | 机器学习工程与生产部署 / 可解释性、公平性与安全 | 25 | planned |
| 18 | 426–447 | 可解释性、公平性与安全 | 22 | planned |

## 来源、发布与验证

- 源稿：`wiki/machine-learning/<NNN>-<slug>.md`；Pages 镜像：`docs/wiki/machine-learning/`（逐字节相同）。
- 元数据：本目录 `batches.json`、`docs/wiki/machine-learning/manifest.json`、`wiki/reviews/machine-learning.json`；网站统一 `docs/data/wiki-index.json`。
- 公共入口仍为 [Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/?category=machine-learning#explorer) → 术语详情，不暴露批次计划。
- `python3 scripts/build_wiki_index.py --check`、`python3 scripts/verify_wiki_reviews.py --check`、整库测试、Chromium E2E；审稿和 CI 分开记录。

## 第一批 001–025（已合并 main）

覆盖“基础概念与学习范式”24 条，以及第二个专题“数据、样本与数据集划分”第 1 条 **Dataset**。不要误将第二章局部编号 1 当作全局编号 1。

1. Machine Learning (ML)（机器学习）
2. Artificial Intelligence (AI)（人工智能）
3. Statistical Learning（统计学习）
4. Supervised Learning（监督学习）
5. Unsupervised Learning（无监督学习）
6. Semi-supervised Learning（半监督学习）
7. Self-supervised Learning（自监督学习）
8. Reinforcement Learning (RL)（强化学习）
9. Online Learning（在线学习）
10. Offline Learning / Batch Learning（离线学习／批量学习）
11. Active Learning（主动学习）
12. Transfer Learning（迁移学习）
13. Multi-task Learning（多任务学习）
14. Meta-learning（元学习）
15. Few-shot Learning（少样本学习）
16. Zero-shot Learning（零样本学习）
17. Domain Adaptation（领域自适应）
18. Inductive Learning（归纳学习）
19. Transductive Learning（直推学习）
20. Generative Model（生成模型）
21. Discriminative Model（判别模型）
22. Predictive Modeling（预测建模）
23. Representation Learning（表征学习）
24. Foundation Model（基础模型）
25. Dataset（数据集）


**第一批知识路径：**[BATCH-01.md](BATCH-01.md)。

**25 篇候审稿：**

1. [Machine Learning (ML)（机器学习）](001-machine-learning.md)
2. [Artificial Intelligence (AI)（人工智能）](002-artificial-intelligence.md)
3. [Statistical Learning（统计学习）](003-statistical-learning.md)
4. [Supervised Learning（监督学习）](004-supervised-learning.md)
5. [Unsupervised Learning（无监督学习）](005-unsupervised-learning.md)
6. [Semi-supervised Learning（半监督学习）](006-semi-supervised-learning.md)
7. [Self-supervised Learning（自监督学习）](007-self-supervised-learning.md)
8. [Reinforcement Learning (RL)（强化学习）](008-reinforcement-learning.md)
9. [Online Learning（在线学习）](009-online-learning.md)
10. [Offline Learning / Batch Learning（离线学习／批量学习）](010-offline-learning-batch-learning.md)
11. [Active Learning（主动学习）](011-active-learning.md)
12. [Transfer Learning（迁移学习）](012-transfer-learning.md)
13. [Multi-task Learning（多任务学习）](013-multi-task-learning.md)
14. [Meta-learning（元学习）](014-meta-learning.md)
15. [Few-shot Learning（少样本学习）](015-few-shot-learning.md)
16. [Zero-shot Learning（零样本学习）](016-zero-shot-learning.md)
17. [Domain Adaptation（领域自适应）](017-domain-adaptation.md)
18. [Inductive Learning（归纳学习）](018-inductive-learning.md)
19. [Transductive Learning（直推学习）](019-transductive-learning.md)
20. [Generative Model（生成模型）](020-generative-model.md)
21. [Discriminative Model（判别模型）](021-discriminative-model.md)
22. [Predictive Modeling（预测建模）](022-predictive-modeling.md)
23. [Representation Learning（表征学习）](023-representation-learning.md)
24. [Foundation Model（基础模型）](024-foundation-model.md)
25. [Dataset（数据集）](025-dataset.md)

> 第一批已合并 main；专业审稿仍为 pending，批次生产状态不在公共站点展示。


## 第二批 026–050（已合并 main）

本批全属于「数据、样本与数据集划分」，学习路径参见 [BATCH-02](BATCH-02.md)。

26. [Sample / Instance（样本／实例）](026-sample-instance.md)
27. [Observation（观测）](027-observation.md)
28. [Feature（特征）](028-feature.md)
29. [Target / Label（目标变量／标签）](029-target-label.md)
30. [Ground Truth（真实标注／参考真值）](030-ground-truth.md)
31. [Feature Matrix (X)（特征矩阵）](031-feature-matrix.md)
32. [Target Vector (y)（目标向量）](032-target-vector.md)
33. [Training Set（训练集）](033-training-set.md)
34. [Validation Set（验证集）](034-validation-set.md)
35. [Test Set（测试集）](035-test-set.md)
36. [Holdout Set（留出集）](036-holdout-set.md)
37. [Train–Test Split（训练测试划分）](037-train-test-split.md)
38. [Stratified Sampling（分层抽样）](038-stratified-sampling.md)
39. [Group Split（分组划分）](039-group-split.md)
40. [Temporal Split（时间划分）](040-temporal-split.md)
41. [Cross-validation (CV)（交叉验证）](041-cross-validation.md)
42. [K-fold Cross-validation（K 折交叉验证）](042-k-fold-cross-validation.md)
43. [Stratified K-fold（分层 K 折交叉验证）](043-stratified-k-fold.md)
44. [Leave-one-out CV (LOOCV)（留一交叉验证）](044-leave-one-out-cv.md)
45. [Out-of-fold Prediction (OOF)（折外预测）](045-out-of-fold-prediction.md)
46. [Data Leakage（数据泄漏）](046-data-leakage.md)
47. [Label Leakage（标签泄漏）](047-label-leakage.md)
48. [Sampling Bias（抽样偏差）](048-sampling-bias.md)
49. [Class Imbalance（类别不平衡）](049-class-imbalance.md)
50. [Missing Value（缺失值）](050-missing-value.md)

> 第二批已合并 main，Pages 发布验证成功；专家独立审稿仍 pending。


## 第三批 051–075（已合并 main 并发布 Pages）

覆盖第二专题末尾 2 篇和第三专题前 23 篇。重要技术主线：**源数据质量 → 预处理与填补 → 尺度变换 → 类别编码 → 非线性交互 → 文本向量化**。详见 [第三批学习路径](BATCH-03.md)。

51. [Outlier（离群点）](051-outlier.md)
52. [Data Annotation（数据标注）](052-data-annotation.md)
53. [Data Cleaning（数据清洗）](053-data-cleaning.md)
54. [Data Preprocessing（数据预处理）](054-data-preprocessing.md)
55. [Feature Engineering（特征工程）](055-feature-engineering.md)
56. [Feature Extraction（特征提取）](056-feature-extraction.md)
57. [Feature Selection（特征选择）](057-feature-selection.md)
58. [Imputation（缺失值填补）](058-imputation.md)
59. [Mean Imputation（均值填补）](059-mean-imputation.md)
60. [Standardization（标准化）](060-standardization.md)
61. [Normalization（归一化）](061-normalization.md)
62. [Min–Max Scaling（最小最大缩放）](062-min-max-scaling.md)
63. [Robust Scaling（稳健缩放）](063-robust-scaling.md)
64. [One-hot Encoding（独热编码）](064-one-hot-encoding.md)
65. [Ordinal Encoding（序数编码）](065-ordinal-encoding.md)
66. [Target Encoding（目标编码）](066-target-encoding.md)
67. [Label Encoding（标签编码）](067-label-encoding.md)
68. [Binning / Discretization（分箱／离散化）](068-binning-discretization.md)
69. [Polynomial Features（多项式特征）](069-polynomial-features.md)
70. [Interaction Feature（交互特征）](070-interaction-feature.md)
71. [Log Transformation（对数变换）](071-log-transformation.md)
72. [Box–Cox Transformation（Box–Cox 变换）](072-box-cox-transformation.md)
73. [Feature Hashing（特征哈希）](073-feature-hashing.md)
74. [Bag of Words (BoW)（词袋模型）](074-bag-of-words.md)
75. [TF–IDF（词频-逆文档频率）](075-tf-idf.md)

> 第三批已通过 PR CI 并发布至 Pages；专业人工审核仍 pending。


## 第四批 076–100（已合并 main 并发布 Pages）

本批延续第三专题最后 7 条（Embedding–Pipeline），并进入第四专题统计学习与泛化理论 18 条（Empirical Risk–PAC Learning）。含理论公式、工程适用边界、两道中等面试问答和两道中等考试题及解析。知识路径详见 [BATCH-04.md](BATCH-04.md)。

76. [Embedding（嵌入向量）](076-embedding.md)
77. [Sparse Feature（稀疏特征）](077-sparse-feature.md)
78. [Dense Feature（稠密特征）](078-dense-feature.md)
79. [Data Augmentation（数据增强）](079-data-augmentation.md)
80. [Resampling（重采样）](080-resampling.md)
81. [SMOTE（合成少数类过采样技术）](081-smote.md)
82. [Pipeline（流水线）](082-pipeline.md)
83. [Empirical Risk（经验风险）](083-empirical-risk.md)
84. [Expected Risk（期望风险）](084-expected-risk.md)
85. [Empirical Risk Minimization (ERM)（经验风险最小化）](085-empirical-risk-minimization.md)
86. [Structural Risk Minimization (SRM)（结构风险最小化）](086-structural-risk-minimization.md)
87. [Generalization（泛化）](087-generalization.md)
88. [Generalization Gap（泛化差距）](088-generalization-gap.md)
89. [Overfitting（过拟合）](089-overfitting.md)
90. [Underfitting（欠拟合）](090-underfitting.md)
91. [Bias–Variance Tradeoff（偏差-方差权衡）](091-bias-variance-tradeoff.md)
92. [Inductive Bias（归纳偏置）](092-inductive-bias.md)
93. [Regularization（正则化）](093-regularization.md)
94. [L1 Regularization（L1 正则化）](094-l1-regularization.md)
95. [L2 Regularization（L2 正则化）](095-l2-regularization.md)
96. [Elastic Net Regularization（弹性网络正则化）](096-elastic-net-regularization.md)
97. [Model Complexity（模型复杂度）](097-model-complexity.md)
98. [Capacity（模型容量）](098-capacity.md)
99. [VC Dimension（VC 维）](099-vc-dimension.md)
100. [PAC Learning（概率近似正确学习）](100-pac-learning.md)

> 第四批已完成 PR CI、main 合并及 Pages 发布；专业人工审稿仍为 pending。


## 第五批 101–125（25 篇深度候审稿）

本批从 Sample Complexity 到 Decision Boundary，覆盖第四专题最后 7 个学习理论/分布偏移术语，以及第五专题前 18 个分类与回归模型。每篇均有 2 道中等面试问答和 2 道中等考试题及解析；详细交叉术语学习路径见 [BATCH-05.md](BATCH-05.md)。

101. [Sample Complexity（样本复杂度）](101-sample-complexity.md)
102. [Learning Curve（学习曲线）](102-learning-curve.md)
103. [Validation Curve（验证曲线）](103-validation-curve.md)
104. [Distribution Shift（分布偏移）](104-distribution-shift.md)
105. [Covariate Shift（协变量偏移）](105-covariate-shift.md)
106. [Label Shift / Prior Shift（标签偏移／先验偏移）](106-label-shift-prior-shift.md)
107. [Concept Drift（概念漂移）](107-concept-drift.md)
108. [Regression（回归）](108-regression.md)
109. [Classification（分类）](109-classification.md)
110. [Binary Classification（二分类）](110-binary-classification.md)
111. [Multiclass Classification（多类别分类）](111-multiclass-classification.md)
112. [Multilabel Classification（多标签分类）](112-multilabel-classification.md)
113. [Multioutput Prediction（多输出预测）](113-multioutput-prediction.md)
114. [Linear Regression（线性回归）](114-linear-regression.md)
115. [Ordinary Least Squares (OLS)（普通最小二乘法）](115-ordinary-least-squares.md)
116. [Ridge Regression（岭回归）](116-ridge-regression.md)
117. [Lasso Regression（套索回归）](117-lasso-regression.md)
118. [Elastic Net（弹性网络）](118-elastic-net.md)
119. [Logistic Regression（逻辑回归）](119-logistic-regression.md)
120. [Softmax Regression（Softmax 回归）](120-softmax-regression.md)
121. [Generalized Linear Model (GLM)（广义线性模型）](121-generalized-linear-model.md)
122. [Poisson Regression（泊松回归）](122-poisson-regression.md)
123. [Quantile Regression（分位数回归）](123-quantile-regression.md)
124. [Robust Regression（稳健回归）](124-robust-regression.md)
125. [Decision Boundary（决策边界）](125-decision-boundary.md)

> 第 5 批暂为 PR 候审，须以真实 CI 结果、合并及 Pages 部署为准。独立专业审稿仍 pending。
