# 机器学习 · Machine Learning

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：447 条 · 专题：19 类**

Foundations, classical algorithms, model evaluation, tuning and MLOps

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与学习范式（24 条）
- 02. 数据、样本与数据集划分（28 条）
- 03. 数据预处理与特征工程（30 条）
- 04. 统计学习与泛化理论（25 条）
- 05. 回归、分类与线性模型（26 条）
- 06. 树模型与集成学习（24 条）
- 07. 支持向量机、核方法与近邻（20 条）
- 08. 概率模型与统计推断（24 条）
- 09. 无监督学习与聚类（24 条）
- 10. 降维、分解与流形学习（20 条）
- 11. 优化算法与模型训练（30 条）
- 12. 损失函数与回归评估（11 条）
- 13. 分类指标与概率校准（27 条）
- 14. 调参与模型选择（18 条）
- 15. 时间序列与预测（18 条）
- 16. 推荐系统与排序学习（19 条）
- 17. 深度学习相关核心术语（25 条）
- 18. 机器学习工程与生产部署（30 条）
- 19. 可解释性、公平性与安全（24 条）

---

## 01. 基础概念与学习范式

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Machine Learning (ML) | 机器学习 | ML | 从数据中学习规律，用于预测、决策或生成的技术总称。 |
| 2 | Artificial Intelligence (AI) | 人工智能 | AI | 研究和构建表现出智能行为的系统的广泛领域。 |
| 3 | Statistical Learning | 统计学习 |  | 以统计理论刻画从样本到预测规则的学习过程。 |
| 4 | Supervised Learning | 监督学习 |  | 利用带目标标签的样本学习输入到输出的映射。 |
| 5 | Unsupervised Learning | 无监督学习 |  | 在无目标标签数据中发现结构、分组或表征。 |
| 6 | Semi-supervised Learning | 半监督学习 |  | 结合少量有标签与大量无标签数据进行学习。 |
| 7 | Self-supervised Learning | 自监督学习 |  | 从数据自身构造监督信号进行表征学习。 |
| 8 | Reinforcement Learning (RL) | 强化学习 | RL | 通过与环境交互、根据奖励学习行动策略。 |
| 9 | Online Learning | 在线学习 |  | 样本持续到来时增量更新模型的学习方式。 |
| 10 | Offline Learning / Batch Learning | 离线学习／批量学习 |  | 先汇集数据，再分批训练模型的方式。 |
| 11 | Active Learning | 主动学习 |  | 模型主动选择最值得人工标注的样本。 |
| 12 | Transfer Learning | 迁移学习 |  | 将源任务或领域所学知识应用于新任务。 |
| 13 | Multi-task Learning | 多任务学习 |  | 联合训练相关任务，以共享有益的表征。 |
| 14 | Meta-learning | 元学习 |  | 学习如何更快适应新的任务或训练设置。 |
| 15 | Few-shot Learning | 少样本学习 |  | 仅使用少量示例完成新任务的学习方法。 |
| 16 | Zero-shot Learning | 零样本学习 |  | 不依赖目标类别的训练样本完成预测。 |
| 17 | Domain Adaptation | 领域自适应 |  | 减小训练域与目标域分布差异带来的影响。 |
| 18 | Inductive Learning | 归纳学习 |  | 从训练样本学习可推广到未知样本的规则。 |
| 19 | Transductive Learning | 直推学习 |  | 针对给定的未标注目标样本进行推断。 |
| 20 | Generative Model | 生成模型 |  | 学习数据分布，支持采样或生成数据。 |
| 21 | Discriminative Model | 判别模型 |  | 学习类别边界或条件预测关系。 |
| 22 | Predictive Modeling | 预测建模 |  | 构建用于预测未知结果的统计或机器学习模型。 |
| 23 | Representation Learning | 表征学习 |  | 自动学习适合下游任务的数据表示。 |
| 24 | Foundation Model | 基础模型 |  | 在广泛数据上预训练、可适配多种任务的模型。 |

## 02. 数据、样本与数据集划分

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Dataset | 数据集 |  | 用于训练、验证或评估的样本集合。 |
| 2 | Sample / Instance | 样本／实例 |  | 数据集中一次观测或一个数据对象。 |
| 3 | Observation | 观测 |  | 被记录的数据测量或事件。 |
| 4 | Feature | 特征 |  | 作为模型输入的可测量属性或变量。 |
| 5 | Target / Label | 目标变量／标签 |  | 希望模型预测或解释的值。 |
| 6 | Ground Truth | 真实标注／参考真值 |  | 用作训练或评估依据的可信参考标签。 |
| 7 | Feature Matrix (X) | 特征矩阵 |  | 以样本为行、特征为列的输入矩阵。 |
| 8 | Target Vector (y) | 目标向量 |  | 与样本对应的预测目标序列。 |
| 9 | Training Set | 训练集 |  | 用于拟合模型参数的数据部分。 |
| 10 | Validation Set | 验证集 |  | 用于模型选择、调参与监控训练的数据部分。 |
| 11 | Test Set | 测试集 |  | 用于最终估计泛化表现的保留数据部分。 |
| 12 | Holdout Set | 留出集 |  | 从训练过程中隔离，用于独立评估的数据。 |
| 13 | Train–Test Split | 训练测试划分 |  | 将样本划分成用于训练和评估的子集。 |
| 14 | Stratified Sampling | 分层抽样 |  | 按类别等分层因素保持分布比例的抽样方式。 |
| 15 | Group Split | 分组划分 |  | 保证同一组的样本不会跨训练与测试划分。 |
| 16 | Temporal Split | 时间划分 |  | 按照时间先后进行数据划分，减少未来信息泄漏。 |
| 17 | Cross-validation (CV) | 交叉验证 | CV | 重复划分训练和验证数据以评估模型。 |
| 18 | K-fold Cross-validation | K 折交叉验证 |  | 将数据分成 K 份，轮流用一份验证。 |
| 19 | Stratified K-fold | 分层 K 折交叉验证 |  | 每折尽量维持类别比例的 K 折验证。 |
| 20 | Leave-one-out CV (LOOCV) | 留一交叉验证 | LOOCV | 每次留一个样本作验证，其余样本训练。 |
| 21 | Out-of-fold Prediction (OOF) | 折外预测 | OOF | 在样本未参与对应模型训练的折上产生预测。 |
| 22 | Data Leakage | 数据泄漏 |  | 训练时不当使用评估集或未来信息造成评估虚高。 |
| 23 | Label Leakage | 标签泄漏 |  | 特征包含了预测时不可获得的目标信息。 |
| 24 | Sampling Bias | 抽样偏差 |  | 样本选取机制导致数据不代表目标总体。 |
| 25 | Class Imbalance | 类别不平衡 |  | 不同类别的样本数量差异明显。 |
| 26 | Missing Value | 缺失值 |  | 某项特征的观测值未被记录。 |
| 27 | Outlier | 离群点 |  | 相对主要数据分布显著偏离的观测。 |
| 28 | Data Annotation | 数据标注 |  | 为原始数据提供类别、边界或其他监督信息。 |

## 03. 数据预处理与特征工程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Cleaning | 数据清洗 |  | 修正重复、缺失、错误或不一致的数据。 |
| 2 | Data Preprocessing | 数据预处理 |  | 模型训练前的清洗、变换和编码流程。 |
| 3 | Feature Engineering | 特征工程 |  | 设计、构造和处理能改善模型表现的特征。 |
| 4 | Feature Extraction | 特征提取 |  | 将原始数据变换为更有用的特征表示。 |
| 5 | Feature Selection | 特征选择 |  | 从候选特征中选择相关、有效的子集。 |
| 6 | Imputation | 缺失值填补 |  | 用规则或模型估计缺失的数据值。 |
| 7 | Mean Imputation | 均值填补 |  | 使用已观测数值的均值替代缺失值。 |
| 8 | Standardization | 标准化 |  | 常指减均值后除以标准差的数值变换。 |
| 9 | Normalization | 归一化 |  | 按约定尺度变换数据；具体含义依场景而异。 |
| 10 | Min–Max Scaling | 最小最大缩放 |  | 将特征线性映射到指定值域。 |
| 11 | Robust Scaling | 稳健缩放 |  | 利用中位数和分位距减弱异常值影响。 |
| 12 | One-hot Encoding | 独热编码 |  | 将类别编码为只有对应位置为 1 的向量。 |
| 13 | Ordinal Encoding | 序数编码 |  | 将类别映射为有顺序的整数值。 |
| 14 | Target Encoding | 目标编码 |  | 利用目标统计量表示类别，需要防止数据泄漏。 |
| 15 | Label Encoding | 标签编码 |  | 将离散标签映射为整数编码。 |
| 16 | Binning / Discretization | 分箱／离散化 |  | 将连续变量划分为有限个区间。 |
| 17 | Polynomial Features | 多项式特征 |  | 通过原特征的幂与交互项扩展输入。 |
| 18 | Interaction Feature | 交互特征 |  | 表征两个或多个变量联合作用的特征。 |
| 19 | Log Transformation | 对数变换 |  | 以对数压缩长尾分布或较大数值范围。 |
| 20 | Box–Cox Transformation | Box–Cox 变换 |  | 对正值数据使用参数化幂变换。 |
| 21 | Feature Hashing | 特征哈希 |  | 通过哈希将高维离散特征映射到固定维度。 |
| 22 | Bag of Words (BoW) | 词袋模型 |  | 以词出现情况或频次表征文本。 |
| 23 | TF–IDF | 词频-逆文档频率 |  | 衡量词在文档中的重要性并抑制常见词。 |
| 24 | Embedding | 嵌入向量 |  | 将对象映射为连续、低维或稠密的数值表示。 |
| 25 | Sparse Feature | 稀疏特征 |  | 取零值或缺失状态的比例很高的特征。 |
| 26 | Dense Feature | 稠密特征 |  | 多数维度都有有效数值的特征。 |
| 27 | Data Augmentation | 数据增强 |  | 通过合理变换样本扩充训练数据多样性。 |
| 28 | Resampling | 重采样 |  | 改变样本选择或重复使用方式以调整数据分布。 |
| 29 | SMOTE | 合成少数类过采样技术 |  | 在特征空间合成少数类样本以缓解不平衡。 |
| 30 | Pipeline | 流水线 |  | 串联预处理和预测器并统一训练、推断的流程。 |

## 04. 统计学习与泛化理论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Empirical Risk | 经验风险 |  | 模型在训练样本上的平均损失。 |
| 2 | Expected Risk | 期望风险 |  | 模型在目标数据分布上的期望损失。 |
| 3 | Empirical Risk Minimization (ERM) | 经验风险最小化 | ERM | 通过最小化训练数据上的损失选择模型。 |
| 4 | Structural Risk Minimization (SRM) | 结构风险最小化 | SRM | 在拟合误差之外控制模型复杂度。 |
| 5 | Generalization | 泛化 |  | 模型对未见样本保持有效表现的能力。 |
| 6 | Generalization Gap | 泛化差距 |  | 训练指标与验证或测试指标之间的差异。 |
| 7 | Overfitting | 过拟合 |  | 模型过度记忆训练样本，未见样本表现下降。 |
| 8 | Underfitting | 欠拟合 |  | 模型表达能力或训练程度不足，难以捕获规律。 |
| 9 | Bias–Variance Tradeoff | 偏差-方差权衡 |  | 模型偏差与对样本变化敏感度之间的折中。 |
| 10 | Inductive Bias | 归纳偏置 |  | 学习算法为了推广到新样本而采用的先验假设。 |
| 11 | Regularization | 正则化 |  | 通过约束或惩罚降低过拟合风险。 |
| 12 | L1 Regularization | L1 正则化 |  | 惩罚参数绝对值之和，可促进稀疏性。 |
| 13 | L2 Regularization | L2 正则化 |  | 惩罚参数平方和，倾向于缩小参数幅度。 |
| 14 | Elastic Net Regularization | 弹性网络正则化 |  | 组合 L1 与 L2 惩罚的正则化方法。 |
| 15 | Model Complexity | 模型复杂度 |  | 衡量模型表达能力或自由度的概念。 |
| 16 | Capacity | 模型容量 |  | 模型能拟合的函数集合的丰富程度。 |
| 17 | VC Dimension | VC 维 |  | 衡量假设类分类表达能力的理论量。 |
| 18 | PAC Learning | 概率近似正确学习 |  | 通过概率保证和样本复杂度研究可学习性。 |
| 19 | Sample Complexity | 样本复杂度 |  | 达到目标误差和置信水平所需样本规模。 |
| 20 | Learning Curve | 学习曲线 |  | 观察性能随训练样本量或训练过程变化的曲线。 |
| 21 | Validation Curve | 验证曲线 |  | 观察训练和验证表现随超参数变化的曲线。 |
| 22 | Distribution Shift | 分布偏移 |  | 训练环境和实际使用环境的数据分布发生改变。 |
| 23 | Covariate Shift | 协变量偏移 |  | 输入分布变化而条件标签机制假设保持不变。 |
| 24 | Label Shift / Prior Shift | 标签偏移／先验偏移 |  | 类别先验比例变化而类条件输入分布保持不变。 |
| 25 | Concept Drift | 概念漂移 |  | 输入与目标之间的预测关系随时间改变。 |

## 05. 回归、分类与线性模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Regression | 回归 |  | 预测连续数值目标的学习任务。 |
| 2 | Classification | 分类 |  | 预测离散类别的学习任务。 |
| 3 | Binary Classification | 二分类 |  | 在两个类别中判断样本所属类别。 |
| 4 | Multiclass Classification | 多类别分类 |  | 在三个及以上互斥类别中分类。 |
| 5 | Multilabel Classification | 多标签分类 |  | 为一个样本预测多个可同时成立的标签。 |
| 6 | Multioutput Prediction | 多输出预测 |  | 对每个输入同时预测多个目标变量。 |
| 7 | Linear Regression | 线性回归 |  | 以特征的线性组合预测连续目标。 |
| 8 | Ordinary Least Squares (OLS) | 普通最小二乘法 | OLS | 最小化残差平方和来估计回归系数。 |
| 9 | Ridge Regression | 岭回归 |  | 采用 L2 惩罚的线性回归。 |
| 10 | Lasso Regression | 套索回归 |  | 采用 L1 惩罚的线性回归。 |
| 11 | Elastic Net | 弹性网络 |  | 同时使用 L1 和 L2 惩罚的线性模型。 |
| 12 | Logistic Regression | 逻辑回归 |  | 通过逻辑函数建模类别条件概率的分类方法。 |
| 13 | Softmax Regression | Softmax 回归 |  | 将多类得分转为类别概率的线性分类模型。 |
| 14 | Generalized Linear Model (GLM) | 广义线性模型 | GLM | 用链接函数连接预测变量和响应均值的模型族。 |
| 15 | Poisson Regression | 泊松回归 |  | 常用于计数型响应变量的广义线性模型。 |
| 16 | Quantile Regression | 分位数回归 |  | 估计条件分布中指定分位数的回归方法。 |
| 17 | Robust Regression | 稳健回归 |  | 降低异常值或模型偏离对估计的影响。 |
| 18 | Decision Boundary | 决策边界 |  | 将不同预测类别划分开的边界。 |
| 19 | Decision Function | 决策函数 |  | 将样本映射为分类得分或判别量的函数。 |
| 20 | Logit | 对数几率 |  | 概率 p 对应的 log(p/(1-p)) 值。 |
| 21 | Sigmoid Function | Sigmoid 函数 |  | 将实数压缩到 0 与 1 之间的 S 形函数。 |
| 22 | Softmax Function | Softmax 函数 |  | 将多个得分变换为和为 1 的概率型向量。 |
| 23 | Residual | 残差 |  | 观测目标与模型拟合值之差。 |
| 24 | Coefficient | 回归系数 |  | 线性模型中描述特征影响的参数。 |
| 25 | Intercept | 截距 |  | 输入特征为零时线性模型的基准输出项。 |
| 26 | Multicollinearity | 多重共线性 |  | 多个输入特征之间存在较强线性相关。 |

## 06. 树模型与集成学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Decision Tree | 决策树 |  | 通过层层条件划分数据的树形预测模型。 |
| 2 | Root Node | 根节点 |  | 决策树最上层的起始节点。 |
| 3 | Internal Node | 内部节点 |  | 用于特征条件判断和样本分裂的节点。 |
| 4 | Leaf Node | 叶节点 |  | 决策树中输出最终预测的终端节点。 |
| 5 | Tree Depth | 树深度 |  | 从根到叶的最大边数或层级数，依实现定义。 |
| 6 | Split Criterion | 划分准则 |  | 判断哪种特征划分最有利的指标。 |
| 7 | Gini Impurity | 基尼不纯度 |  | 衡量节点内类别混杂程度的指标。 |
| 8 | Information Gain | 信息增益 |  | 分裂前后信息熵减少的量。 |
| 9 | Tree Pruning | 决策树剪枝 |  | 删减树枝以控制复杂度和提高泛化能力。 |
| 10 | Bagging (Bootstrap Aggregating) | 自助聚合 |  | 对重采样数据训练多个模型并聚合输出。 |
| 11 | Bootstrap Sampling | 自助采样 |  | 从样本中有放回地重复抽样。 |
| 12 | Random Forest | 随机森林 |  | 组合多棵随机化决策树的集成模型。 |
| 13 | Extra Trees | 极端随机树 |  | 在树的划分阈值中引入更多随机性的集成方法。 |
| 14 | Boosting | 提升法 |  | 顺序训练弱学习器并组合成更强模型。 |
| 15 | AdaBoost | 自适应提升 |  | 根据样本误差动态调整权重的提升算法。 |
| 16 | Gradient Boosting | 梯度提升 |  | 沿损失函数负梯度方向逐步添加基学习器。 |
| 17 | GBDT | 梯度提升决策树 |  | 以决策树为弱学习器的梯度提升模型。 |
| 18 | XGBoost | 极端梯度提升 |  | 高效实现正则化梯度提升树的算法与库。 |
| 19 | LightGBM | 轻量级梯度提升机 |  | 强调高效直方图建树等策略的 GBDT 框架。 |
| 20 | CatBoost | 类别提升 |  | 擅长处理类别特征的梯度提升框架。 |
| 21 | Stacking | 堆叠集成 |  | 用次级模型组合多个基模型的预测。 |
| 22 | Voting Ensemble | 投票集成 |  | 通过投票或概率平均融合多个分类器。 |
| 23 | Out-of-bag Error (OOB) | 袋外误差 | OOB | 利用未被某棵树抽中的样本估计泛化误差。 |
| 24 | Feature Importance | 特征重要性 |  | 估计某特征对模型预测或指标的贡献程度。 |

## 07. 支持向量机、核方法与近邻

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Support Vector Machine (SVM) | 支持向量机 | SVM | 通过间隔最大化等原则构建分类或回归模型。 |
| 2 | Support Vector | 支持向量 |  | 对最大间隔决策边界起关键作用的训练样本。 |
| 3 | Margin | 间隔 |  | 分类边界与样本之间的距离或函数性间隔。 |
| 4 | Maximum Margin Classifier | 最大间隔分类器 |  | 选择使类别分离间隔尽可能大的分类器。 |
| 5 | Hinge Loss | 合页损失 |  | 在间隔不满足要求时产生惩罚的分类损失。 |
| 6 | Soft Margin | 软间隔 |  | 允许部分样本违反间隔要求的 SVM 设定。 |
| 7 | Kernel Trick | 核技巧 |  | 不显式映射高维特征即可计算内积的方法。 |
| 8 | Kernel Function | 核函数 |  | 计算某特征映射空间中内积的函数。 |
| 9 | Linear Kernel | 线性核 |  | 以原始向量内积定义的核函数。 |
| 10 | Polynomial Kernel | 多项式核 |  | 用输入内积的多项式构造非线性相似度。 |
| 11 | RBF Kernel / Gaussian Kernel | 径向基核／高斯核 |  | 根据样本距离构造局部相似度的核函数。 |
| 12 | Support Vector Regression (SVR) | 支持向量回归 | SVR | 采用间隔思想进行连续值预测的方法。 |
| 13 | K-nearest Neighbors (KNN) | K 近邻算法 | KNN | 根据距离最近的 K 个样本作预测。 |
| 14 | Nearest Neighbor Search | 最近邻搜索 |  | 在特征空间中寻找距离最小的样本。 |
| 15 | Distance Metric | 距离度量 |  | 度量两个样本相异程度的函数。 |
| 16 | Euclidean Distance | 欧氏距离 |  | 向量差的 L2 范数。 |
| 17 | Manhattan Distance | 曼哈顿距离 |  | 各坐标绝对差之和。 |
| 18 | Cosine Similarity | 余弦相似度 |  | 由向量夹角余弦衡量方向相似性。 |
| 19 | Metric Learning | 度量学习 |  | 学习使相似样本更近、不相似样本更远的表示或距离。 |
| 20 | Approximate Nearest Neighbor (ANN) | 近似最近邻 | ANN | 以近似正确结果换取更快的近邻检索。 |

## 08. 概率模型与统计推断

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Probability Distribution | 概率分布 |  | 描述随机变量取值概率的数学对象。 |
| 2 | Conditional Probability | 条件概率 |  | 给定一个事件后另一个事件发生的概率。 |
| 3 | Bayes’ Theorem | 贝叶斯定理 |  | 联系先验、似然、证据与后验的公式。 |
| 4 | Prior Probability | 先验概率 |  | 观察当前数据之前对假设的概率判断。 |
| 5 | Likelihood | 似然 |  | 在给定模型参数下观察到数据的相对支持程度。 |
| 6 | Posterior Probability | 后验概率 |  | 结合先验和数据后得到的概率分布。 |
| 7 | Maximum Likelihood Estimation (MLE) | 极大似然估计 | MLE | 选择使观测数据似然最大的参数。 |
| 8 | Maximum A Posteriori (MAP) | 最大后验估计 | MAP | 选择使后验密度或质量最大的参数。 |
| 9 | Bayesian Inference | 贝叶斯推断 |  | 利用贝叶斯规则更新参数或假设的不确定性。 |
| 10 | Naive Bayes | 朴素贝叶斯 |  | 给定类别时假定各特征条件独立的分类器。 |
| 11 | Gaussian Naive Bayes | 高斯朴素贝叶斯 |  | 假设每类内连续特征服从高斯分布的模型。 |
| 12 | Gaussian Mixture Model (GMM) | 高斯混合模型 | GMM | 用多个高斯分布的加权和拟合数据分布。 |
| 13 | Latent Variable | 潜变量 |  | 模型中未直接观测到、用于解释数据的变量。 |
| 14 | Expectation–Maximization (EM) | 期望最大化算法 | EM | 交替求潜变量期望与更新参数的估计方法。 |
| 15 | Markov Chain | 马尔可夫链 |  | 下一状态仅依赖当前状态的随机过程模型。 |
| 16 | Hidden Markov Model (HMM) | 隐马尔可夫模型 | HMM | 通过隐藏状态序列生成观测序列的概率模型。 |
| 17 | Markov Random Field (MRF) | 马尔可夫随机场 | MRF | 用无向图描述变量之间条件依赖的模型。 |
| 18 | Bayesian Network | 贝叶斯网络 |  | 用有向无环图表达概率依赖关系。 |
| 19 | Probabilistic Graphical Model (PGM) | 概率图模型 | PGM | 以图结构表示联合分布和条件依赖的模型。 |
| 20 | Variational Inference (VI) | 变分推断 | VI | 用可优化的近似分布逼近复杂后验。 |
| 21 | Monte Carlo Method | 蒙特卡罗方法 |  | 通过随机采样进行数值估计的方法。 |
| 22 | Markov Chain Monte Carlo (MCMC) | 马尔可夫链蒙特卡罗 | MCMC | 构造马尔可夫链来采样目标分布的技术。 |
| 23 | Gaussian Process (GP) | 高斯过程 | GP | 在函数空间定义联合高斯分布的非参数模型。 |
| 24 | Uncertainty Quantification | 不确定性量化 |  | 分析和表达预测或参数估计不确定性的过程。 |

## 09. 无监督学习与聚类

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Clustering | 聚类 |  | 按相似性把无标签样本划分成若干组。 |
| 2 | Cluster | 簇 |  | 聚类算法发现的相似样本集合。 |
| 3 | Centroid | 质心 |  | 一簇样本的中心位置或均值向量。 |
| 4 | K-means | K 均值聚类 |  | 迭代分配样本并更新 K 个簇中心的算法。 |
| 5 | K-means++ | K-means++ 初始化 |  | 通过距离加权策略选择初始聚类中心的方法。 |
| 6 | K-medoids | K 中心点聚类 |  | 使用真实样本作为簇代表的聚类方法。 |
| 7 | Hierarchical Clustering | 层次聚类 |  | 按层级合并或拆分样本簇的方法。 |
| 8 | Agglomerative Clustering | 凝聚层次聚类 |  | 自底向上逐步合并簇的聚类方法。 |
| 9 | Divisive Clustering | 分裂层次聚类 |  | 自顶向下逐步拆分簇的聚类方法。 |
| 10 | Dendrogram | 树状图 |  | 可视化层次聚类合并或分裂过程的树图。 |
| 11 | DBSCAN | 基于密度的带噪声空间聚类 |  | 根据局部密度识别簇并标记噪声的方法。 |
| 12 | HDBSCAN | 层次密度聚类 |  | 基于多尺度密度结构构造聚类的方法。 |
| 13 | Mean Shift | 均值漂移 |  | 沿局部密度上升方向寻找模式的聚类方法。 |
| 14 | Spectral Clustering | 谱聚类 |  | 利用相似度图的谱结构完成数据划分。 |
| 15 | Affinity Propagation | 亲和传播 |  | 通过消息传递选择代表点的聚类算法。 |
| 16 | Silhouette Coefficient | 轮廓系数 |  | 结合簇内紧密程度与簇间分离程度的指标。 |
| 17 | Davies–Bouldin Index | 戴维斯-博尔丁指数 |  | 比较簇内离散度与簇间距离的聚类指标。 |
| 18 | Adjusted Rand Index (ARI) | 调整兰德指数 | ARI | 比较两个聚类划分一致性的校正指标。 |
| 19 | Normalized Mutual Information (NMI) | 归一化互信息 | NMI | 衡量两组聚类标签共享信息的指标。 |
| 20 | Anomaly Detection | 异常检测 |  | 识别偏离正常模式的样本或事件。 |
| 21 | Novelty Detection | 新颖性检测 |  | 利用正常样本训练后识别未见异常对象。 |
| 22 | Isolation Forest | 孤立森林 |  | 通过随机分割使异常样本更易被孤立的方法。 |
| 23 | Local Outlier Factor (LOF) | 局部离群因子 | LOF | 比较局部邻域密度识别异常的方法。 |
| 24 | One-class SVM | 单类支持向量机 |  | 学习正常数据支持区域以发现异常的模型。 |

## 10. 降维、分解与流形学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Dimensionality Reduction | 降维 |  | 用较少维度保留数据的重要信息。 |
| 2 | Curse of Dimensionality | 维度灾难 |  | 高维空间中样本稀疏、距离性质变化等问题。 |
| 3 | Principal Component Analysis (PCA) | 主成分分析 | PCA | 寻找解释数据方差最多的正交方向。 |
| 4 | Principal Component | 主成分 |  | PCA 识别出的关键正交投影方向。 |
| 5 | Explained Variance Ratio | 解释方差比 |  | 某主成分占总方差的比例。 |
| 6 | Singular Value Decomposition (SVD) | 奇异值分解 | SVD | 将矩阵分解为奇异向量与奇异值的乘积。 |
| 7 | Truncated SVD | 截断奇异值分解 |  | 仅保留主要奇异分量的低秩近似。 |
| 8 | Non-negative Matrix Factorization (NMF) | 非负矩阵分解 | NMF | 用两个非负低秩矩阵近似原始非负矩阵。 |
| 9 | Independent Component Analysis (ICA) | 独立成分分析 | ICA | 分解数据以寻找近似统计独立的潜在来源。 |
| 10 | Factor Analysis (FA) | 因子分析 | FA | 用少量潜在因子解释观测变量的相关结构。 |
| 11 | Linear Discriminant Analysis (LDA) | 线性判别分析 | LDA | 寻找使类间分离与类内紧凑性兼顾的投影。 |
| 12 | Manifold Learning | 流形学习 |  | 假设高维数据位于低维流形上的降维方法。 |
| 13 | t-SNE | t 分布随机邻域嵌入 |  | 常用于可视化的非线性邻域保持降维方法。 |
| 14 | UMAP | 均匀流形近似与投影 |  | 利用邻域图进行非线性降维与可视化。 |
| 15 | Isomap | 等距映射 |  | 利用邻域图测地距离进行流形降维。 |
| 16 | Locally Linear Embedding (LLE) | 局部线性嵌入 | LLE | 通过保留局部线性重构关系进行降维。 |
| 17 | Random Projection | 随机投影 |  | 利用随机矩阵近似保留样本距离的降维方法。 |
| 18 | Low-rank Approximation | 低秩近似 |  | 用低秩矩阵表示主要结构以减少复杂度。 |
| 19 | Eigenvalue | 特征值 |  | 描述线性变换在特征向量方向伸缩的标量。 |
| 20 | Eigenvector | 特征向量 |  | 在线性变换下方向保持不变的非零向量。 |

## 11. 优化算法与模型训练

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Objective Function | 目标函数 |  | 训练过程中希望最小化或最大化的函数。 |
| 2 | Loss Function | 损失函数 |  | 衡量模型预测与目标不一致程度的函数。 |
| 3 | Cost Function | 代价函数 |  | 通常指样本损失的聚合或优化目标。 |
| 4 | Gradient | 梯度 |  | 函数对参数各偏导数组成的方向向量。 |
| 5 | Gradient Descent (GD) | 梯度下降 | GD | 沿目标函数负梯度方向更新参数的方法。 |
| 6 | Stochastic Gradient Descent (SGD) | 随机梯度下降 | SGD | 利用随机样本或小批量梯度更新参数。 |
| 7 | Mini-batch Gradient Descent | 小批量梯度下降 |  | 每次使用一小批样本估计梯度并更新参数。 |
| 8 | Batch Size | 批量大小 |  | 一次参数更新使用的训练样本数量。 |
| 9 | Epoch | 训练轮次 |  | 对训练集完成一轮遍历的单位。 |
| 10 | Iteration / Step | 迭代／更新步 |  | 一次训练循环或参数更新，需结合上下文理解。 |
| 11 | Learning Rate | 学习率 |  | 控制单次参数更新幅度的超参数。 |
| 12 | Learning Rate Schedule | 学习率调度 |  | 按步骤或条件调整学习率的规则。 |
| 13 | Warmup | 预热 |  | 训练初期逐渐增大学习率等训练参数的策略。 |
| 14 | Momentum | 动量 |  | 结合历史梯度方向平滑更新的优化技巧。 |
| 15 | Nesterov Momentum | Nesterov 动量 |  | 在前瞻位置估计梯度的动量方法。 |
| 16 | AdaGrad | 自适应梯度算法 |  | 根据历史梯度平方和调整各参数学习率。 |
| 17 | RMSProp | 均方根传播优化器 |  | 利用梯度平方的指数移动平均缩放更新。 |
| 18 | Adam | 自适应矩估计 |  | 结合梯度一阶矩和二阶矩估计的优化算法。 |
| 19 | AdamW | 解耦权重衰减 Adam |  | 将权重衰减与梯度更新解耦的 Adam 变体。 |
| 20 | Weight Decay | 权重衰减 |  | 在训练更新中缩小参数幅度的正则化机制。 |
| 21 | Gradient Clipping | 梯度裁剪 |  | 限制梯度范数或数值以稳定训练。 |
| 22 | Early Stopping | 提前停止 |  | 依据验证表现决定结束训练以抑制过拟合。 |
| 23 | Convergence | 收敛 |  | 优化迭代趋向稳定解或稳定目标值的性质。 |
| 24 | Local Minimum | 局部最小值 |  | 在局部邻域中目标函数最小的点。 |
| 25 | Global Minimum | 全局最小值 |  | 在整个可行域内目标函数最小的点。 |
| 26 | Saddle Point | 鞍点 |  | 梯度可为零，但某些方向上升、另一些方向下降的点。 |
| 27 | Convex Optimization | 凸优化 |  | 具有凸目标与适当凸约束的优化问题。 |
| 28 | Hessian Matrix | 海森矩阵 |  | 目标函数对参数的二阶偏导数组成的矩阵。 |
| 29 | Backpropagation | 反向传播 |  | 利用链式法则高效计算计算图中参数梯度。 |
| 30 | Automatic Differentiation (Autodiff) | 自动微分 |  | 基于计算图规则精确组合程序的导数。 |

## 12. 损失函数与回归评估

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Mean Squared Error (MSE) | 均方误差 | MSE | 预测与真实值之差平方的平均值。 |
| 2 | Root Mean Squared Error (RMSE) | 均方根误差 | RMSE | 均方误差开平方，量纲与目标相同。 |
| 3 | Mean Absolute Error (MAE) | 平均绝对误差 | MAE | 预测绝对误差的平均值。 |
| 4 | Mean Absolute Percentage Error (MAPE) | 平均绝对百分比误差 | MAPE | 以真实值为分母的相对绝对误差均值；零值时有问题。 |
| 5 | Huber Loss | Huber 损失 |  | 小误差为平方惩罚、大误差为线性惩罚的损失。 |
| 6 | Mean Absolute Deviation | 平均绝对偏差 |  | 相对参照值的绝对偏差平均，需说明参照定义。 |
| 7 | R-squared (R²) | 决定系数 |  | 衡量回归相对于常数基线的拟合改善程度。 |
| 8 | Cross-entropy Loss | 交叉熵损失 |  | 利用真实标签分布衡量预测概率的损失。 |
| 9 | Binary Cross-entropy (BCE) | 二元交叉熵 | BCE | 二分类概率预测常用的交叉熵损失。 |
| 10 | Negative Log-likelihood (NLL) | 负对数似然 | NLL | 对模型赋予真实观测的概率取负对数。 |
| 11 | KL Divergence | KL 散度 |  | 衡量两个概率分布差异的非对称信息量。 |

## 13. 分类指标与概率校准

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Confusion Matrix | 混淆矩阵 |  | 按真实标签与预测标签统计分类结果的矩阵。 |
| 2 | True Positive (TP) | 真正例 | TP | 真实为正且预测为正的样本数。 |
| 3 | False Positive (FP) | 假正例 | FP | 真实为负但预测为正的样本数。 |
| 4 | True Negative (TN) | 真负例 | TN | 真实为负且预测为负的样本数。 |
| 5 | False Negative (FN) | 假负例 | FN | 真实为正但预测为负的样本数。 |
| 6 | Accuracy | 准确率 |  | 所有预测中分类正确的比例。 |
| 7 | Precision / Positive Predictive Value | 精确率／查准率 |  | 预测为正的样本中真正为正的比例。 |
| 8 | Recall / Sensitivity / TPR | 召回率／敏感度／真正例率 |  | 真实正例中被正确识别的比例。 |
| 9 | Specificity / TNR | 特异度／真负例率 |  | 真实负例中被正确识别的比例。 |
| 10 | False Positive Rate (FPR) | 假正例率 | FPR | 真实负例中被误判为正的比例。 |
| 11 | False Negative Rate (FNR) | 假负例率 | FNR | 真实正例中被漏判的比例。 |
| 12 | F1 Score | F1 分数 |  | 精确率与召回率的调和平均。 |
| 13 | F-beta Score | Fβ 分数 |  | 通过 β 调整召回率与精确率权重的指标。 |
| 14 | Balanced Accuracy | 平衡准确率 |  | 对每类召回率等权平均的分类指标。 |
| 15 | ROC Curve | ROC 曲线 |  | 展示不同阈值下真正例率与假正例率的关系。 |
| 16 | ROC AUC | ROC 曲线下面积 |  | 综合衡量二分类得分区分正负类的能力。 |
| 17 | Precision–Recall Curve (PR Curve) | 精确率-召回率曲线 |  | 展示不同阈值下精确率与召回率的关系。 |
| 18 | Average Precision (AP) | 平均精确率 | AP | 通常指对 PR 曲线按召回率增量加权的精确率求和。 |
| 19 | Log Loss | 对数损失 |  | 按真实类别的预测概率计算对数惩罚。 |
| 20 | Brier Score | 布赖尔分数 |  | 预测概率与二元真实标签差的平方均值。 |
| 21 | Calibration | 概率校准 |  | 预测概率与实际发生频率的一致程度。 |
| 22 | Calibration Curve | 校准曲线 |  | 对比预测概率与经验发生频率的图。 |
| 23 | Threshold | 分类阈值 |  | 将预测得分或概率映射为类别的决策界值。 |
| 24 | Macro Average | 宏平均 |  | 先逐类别计算指标，再对类别等权平均。 |
| 25 | Micro Average | 微平均 |  | 先跨类别汇总计数，再计算整体指标。 |
| 26 | Weighted Average | 加权平均 |  | 按类别支持度等权重聚合指标。 |
| 27 | Top-k Accuracy | Top-k 准确率 |  | 真实类别位于最高 k 个候选预测中的比例。 |

## 14. 调参与模型选择

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Parameter | 模型参数 |  | 从训练数据中估计得到的模型内部数值。 |
| 2 | Hyperparameter | 超参数 |  | 训练前配置或由搜索过程选择的控制参数。 |
| 3 | Hyperparameter Optimization (HPO) | 超参数优化 | HPO | 通过搜索与验证寻找效果较好的超参数。 |
| 4 | Grid Search | 网格搜索 |  | 遍历预设的超参数组合进行评估。 |
| 5 | Random Search | 随机搜索 |  | 从超参数分布中随机抽取组合进行评估。 |
| 6 | Bayesian Optimization | 贝叶斯优化 |  | 利用代理模型选择下一组值得评估的参数。 |
| 7 | Tree-structured Parzen Estimator (TPE) | 树结构 Parzen 估计器 | TPE | 使用密度模型引导超参数搜索的方法。 |
| 8 | Successive Halving | 逐次减半 |  | 阶段性淘汰较差配置并增配计算资源。 |
| 9 | Hyperband | 超带算法 |  | 组合多组资源分配策略进行高效搜索。 |
| 10 | Optuna | Optuna 超参数优化框架 |  | 常用于定义搜索空间并运行优化试验的工具。 |
| 11 | Trial | 试验轮次 |  | 超参数搜索中一次配置及其评估。 |
| 12 | Search Space | 搜索空间 |  | 超参数候选值与允许范围的集合。 |
| 13 | Nested Cross-validation | 嵌套交叉验证 |  | 内层选参、外层估计泛化性能的验证策略。 |
| 14 | Model Selection | 模型选择 |  | 依据验证证据在模型或配置中做选择。 |
| 15 | Baseline Model | 基线模型 |  | 作为衡量新方法是否有改进的参考模型。 |
| 16 | Ablation Study | 消融实验 |  | 移除或替换组件，以评估其贡献。 |
| 17 | Reproducibility | 可复现性 |  | 在明确条件下能够重新得到相同或相近结果的性质。 |
| 18 | Random Seed | 随机种子 |  | 初始化伪随机过程以便控制实验随机性。 |

## 15. 时间序列与预测

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Time Series | 时间序列 |  | 按时间顺序排列的观测数据。 |
| 2 | Forecasting | 预测未来值 |  | 根据历史和已知信息估计未来数值。 |
| 3 | Trend | 趋势 |  | 时间序列中的长期方向性变化。 |
| 4 | Seasonality | 季节性 |  | 按固定周期重复出现的模式。 |
| 5 | Stationarity | 平稳性 |  | 统计性质在时间上保持不变的特性，定义依类型而异。 |
| 6 | Autocorrelation (ACF) | 自相关 | ACF | 同一序列在不同时滞间的相关性。 |
| 7 | Partial Autocorrelation (PACF) | 偏自相关 | PACF | 控制中间滞后影响后的相关性。 |
| 8 | Lag Feature | 滞后特征 |  | 将过去时间点的观测作为当前预测输入。 |
| 9 | Rolling Window | 滚动窗口 |  | 随着时间向前移动的固定长度数据窗口。 |
| 10 | Walk-forward Validation | 滚动前向验证 |  | 按时间顺序反复训练并评估未来时间段。 |
| 11 | Backtesting | 回测 |  | 用历史数据模拟策略或预测系统的运行表现。 |
| 12 | Autoregressive Model (AR) | 自回归模型 | AR | 用过去的观测值预测当前值。 |
| 13 | Moving Average Model (MA) | 移动平均模型 | MA | 以过去噪声项构造当前序列的模型。 |
| 14 | ARIMA | 自回归积分滑动平均模型 |  | 结合差分、自回归和移动平均的时间序列模型。 |
| 15 | SARIMA | 季节性 ARIMA |  | 显式建模季节结构的 ARIMA 扩展。 |
| 16 | Exponential Smoothing | 指数平滑 |  | 对较近观测给予更大权重的预测方法。 |
| 17 | Forecast Horizon | 预测步长／预测时域 |  | 从当前时点向未来预测的跨度。 |
| 18 | Prediction Interval | 预测区间 |  | 表示未来观测值可能所在范围的区间。 |

## 16. 推荐系统与排序学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Recommender System | 推荐系统 |  | 根据用户与内容信息预测偏好并推荐对象。 |
| 2 | Collaborative Filtering (CF) | 协同过滤 | CF | 利用用户-物品交互模式产生推荐。 |
| 3 | Content-based Filtering | 基于内容的推荐 |  | 依据物品特征与用户历史兴趣进行推荐。 |
| 4 | Matrix Factorization | 矩阵分解 |  | 将用户-物品交互矩阵分解为潜在因子。 |
| 5 | Implicit Feedback | 隐式反馈 |  | 点击、浏览、购买等间接反映偏好的行为。 |
| 6 | Explicit Feedback | 显式反馈 |  | 评分、点赞等直接表达的偏好信号。 |
| 7 | Cold Start | 冷启动 |  | 新用户或新物品缺乏交互历史的问题。 |
| 8 | Candidate Generation | 候选召回 |  | 从大规模物品库筛选少量可能相关的候选。 |
| 9 | Ranking | 排序 |  | 根据预测相关性或效用排列候选结果。 |
| 10 | Re-ranking | 重排序 |  | 在初次排序后加入业务约束或多样性等目标。 |
| 11 | Learning to Rank (LTR) | 排序学习 | LTR | 通过训练数据学习结果排序函数。 |
| 12 | Pointwise Ranking | 逐点排序 |  | 将排序视为单样本预测任务的方法。 |
| 13 | Pairwise Ranking | 成对排序 |  | 学习两个候选之间相对顺序的方法。 |
| 14 | Listwise Ranking | 列表式排序 |  | 直接基于候选列表优化排序目标的方法。 |
| 15 | Normalized Discounted Cumulative Gain (NDCG) | 归一化折损累计增益 | NDCG | 根据相关性和排序位置评价结果列表的指标。 |
| 16 | Mean Average Precision (MAP) | 平均精确率均值 | MAP | 对多个查询的平均精确率再取均值的指标。 |
| 17 | Mean Reciprocal Rank (MRR) | 平均倒数排名 | MRR | 统计首个相关结果名次倒数的均值。 |
| 18 | Hit Rate@K | 命中率@K |  | 衡量前 K 个推荐是否至少包含目标项目的比例。 |
| 19 | Exploration–Exploitation Tradeoff | 探索-利用权衡 |  | 在尝试新选项与使用已知好选项间取得平衡。 |

## 17. 深度学习相关核心术语

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Deep Learning (DL) | 深度学习 | DL | 使用多层神经网络进行表示和预测的机器学习分支。 |
| 2 | Artificial Neural Network (ANN) | 人工神经网络 | ANN | 由可训练的连接单元组成的函数模型。 |
| 3 | Perceptron | 感知机 |  | 按线性判别规则进行二分类的早期神经模型。 |
| 4 | Multilayer Perceptron (MLP) | 多层感知机 | MLP | 包含多层全连接变换的前馈神经网络。 |
| 5 | Fully Connected Layer | 全连接层 |  | 输出单元与前一层全部输入连接的网络层。 |
| 6 | Activation Function | 激活函数 |  | 在神经网络层中引入非线性变换的函数。 |
| 7 | ReLU | 修正线性单元 |  | 输出 max(0, x) 的常用激活函数。 |
| 8 | GELU | 高斯误差线性单元 |  | 根据输入幅值进行平滑门控的激活函数。 |
| 9 | Dropout | 随机失活 |  | 训练时随机屏蔽部分单元以起正则化作用。 |
| 10 | Batch Normalization | 批量归一化 |  | 用小批量统计量标准化中间激活的技术。 |
| 11 | Layer Normalization | 层归一化 |  | 沿样本内部指定维度归一化激活的技术。 |
| 12 | Convolutional Neural Network (CNN) | 卷积神经网络 | CNN | 擅长处理局部空间结构的网络架构。 |
| 13 | Recurrent Neural Network (RNN) | 循环神经网络 | RNN | 通过循环状态处理序列信息的网络。 |
| 14 | Long Short-term Memory (LSTM) | 长短期记忆网络 | LSTM | 使用门控机制处理长期依赖的循环网络。 |
| 15 | Gated Recurrent Unit (GRU) | 门控循环单元 | GRU | 具有较简化门控结构的循环网络单元。 |
| 16 | Attention Mechanism | 注意力机制 |  | 根据输入元素相关性加权聚合信息的机制。 |
| 17 | Self-attention | 自注意力 |  | 序列内元素相互计算相关性并聚合信息的机制。 |
| 18 | Transformer | Transformer 架构 |  | 以注意力与前馈层为核心的序列建模架构。 |
| 19 | Autoencoder | 自编码器 |  | 通过编码和重构目标学习潜在表示的模型。 |
| 20 | Variational Autoencoder (VAE) | 变分自编码器 | VAE | 结合潜变量概率建模与变分训练的生成模型。 |
| 21 | Generative Adversarial Network (GAN) | 生成对抗网络 | GAN | 通过生成器与判别器竞争进行生成建模。 |
| 22 | Diffusion Model | 扩散模型 |  | 学习逐步去噪过程以生成数据的模型。 |
| 23 | Pretraining | 预训练 |  | 在大规模数据或前置任务上获得初始模型能力。 |
| 24 | Fine-tuning | 微调 |  | 基于预训练模型针对新任务继续调整参数。 |
| 25 | Knowledge Distillation | 知识蒸馏 |  | 让较小模型学习较大模型输出或中间知识。 |

## 18. 机器学习工程与生产部署

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Machine Learning Operations (MLOps) | 机器学习运维 |  | 将 ML 开发、部署、监控和治理工程化的实践。 |
| 2 | ML Pipeline | 机器学习流水线 |  | 串联数据准备、训练、评估及部署的自动化流程。 |
| 3 | Data Pipeline | 数据流水线 |  | 负责收集、清洗、变换和输送数据的处理流程。 |
| 4 | Feature Store | 特征存储平台 |  | 统一管理、复用并服务训练与在线推断特征的系统。 |
| 5 | Feature Registry | 特征注册表 |  | 记录特征定义、元数据与版本的信息目录。 |
| 6 | Experiment Tracking | 实验跟踪 |  | 记录模型参数、代码版本、指标和产物的过程。 |
| 7 | Model Registry | 模型注册表 |  | 管理模型版本、状态和元数据的系统。 |
| 8 | Artifact | 产物 |  | 训练后生成的模型文件、指标文件或其他可复用结果。 |
| 9 | Model Serving | 模型服务 |  | 将模型封装成可供调用的推断服务。 |
| 10 | Inference | 推断 |  | 用训练后的模型对输入数据产生输出。 |
| 11 | Online Inference | 在线推断 |  | 收到请求时实时调用模型生成结果。 |
| 12 | Batch Inference | 批量推断 |  | 定期或离线对大量样本生成预测。 |
| 13 | Streaming Inference | 流式推断 |  | 对连续输入的数据流进行持续预测。 |
| 14 | Inference Latency | 推断延迟 |  | 从请求到获得预测结果所经历的时间。 |
| 15 | Throughput | 吞吐量 |  | 单位时间内处理的请求数或样本数。 |
| 16 | Model Compression | 模型压缩 |  | 在尽量保持质量的同时减小模型资源需求。 |
| 17 | Quantization | 量化 |  | 使用更低精度的数值形式表示参数或计算。 |
| 18 | Model Pruning | 模型剪枝 |  | 删除较不重要的权重、通道或其他结构。 |
| 19 | ONNX | 开放神经网络交换格式 |  | 用于模型表示与不同框架间交换的开放格式。 |
| 20 | Concept Drift Monitoring | 概念漂移监测 |  | 检测模型预测关系随时间改变的迹象。 |
| 21 | Data Drift | 数据漂移 |  | 生产输入数据的统计分布相对参考分布发生变化。 |
| 22 | Training–Serving Skew | 训练与服务偏差 |  | 训练特征与在线推断特征的生成方式或分布不一致。 |
| 23 | Model Monitoring | 模型监控 |  | 持续观察数据、性能、延迟与异常状况。 |
| 24 | Canary Deployment | 金丝雀发布 |  | 先将新模型投放给少量流量验证风险。 |
| 25 | A/B Testing | A/B 测试 |  | 随机分配流量比较两个方案的实际效果。 |
| 26 | Shadow Deployment | 影子部署 |  | 新模型并行预测但不影响正式决策的验证方式。 |
| 27 | Model Rollback | 模型回滚 |  | 当新模型出现问题时恢复到旧版本。 |
| 28 | Reproducible Training | 可复现训练 |  | 固定数据、配置、代码和环境以重建训练结果。 |
| 29 | Data Versioning | 数据版本管理 |  | 追踪训练和评估所用数据快照及其变化。 |
| 30 | Continuous Training (CT) | 持续训练 | CT | 按计划或触发条件自动更新训练模型。 |

## 19. 可解释性、公平性与安全

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Interpretability | 可解释性 |  | 模型机制及其预测原因能被人理解的程度。 |
| 2 | Explainability | 可解释说明能力 |  | 为模型行为提供可理解解释的能力或方法。 |
| 3 | Global Explanation | 全局解释 |  | 解释模型整体规律或普遍行为。 |
| 4 | Local Explanation | 局部解释 |  | 解释针对单个样本的具体预测。 |
| 5 | Permutation Importance | 置换重要性 |  | 打乱特征后根据性能下降估计重要性。 |
| 6 | Partial Dependence Plot (PDP) | 部分依赖图 | PDP | 显示特征变化对模型平均预测的影响。 |
| 7 | Individual Conditional Expectation (ICE) | 个体条件期望图 | ICE | 展示每个样本的预测随某特征变化的轨迹。 |
| 8 | SHAP | SHAP 特征归因 |  | 用 Shapley 值思想分配特征对预测的贡献。 |
| 9 | LIME | 局部可解释模型无关解释 |  | 在预测附近拟合简单替代模型进行解释。 |
| 10 | Counterfactual Explanation | 反事实解释 |  | 展示改变哪些输入可能改变模型预测。 |
| 11 | Fairness | 公平性 |  | 研究模型对不同群体或个体是否存在不当差异。 |
| 12 | Protected Attribute | 受保护属性 |  | 公平性分析中需特别审慎处理的人群属性。 |
| 13 | Demographic Parity | 人口统计均等 |  | 不同群体具有相同正向决策率的公平标准。 |
| 14 | Equal Opportunity | 机会均等 |  | 不同群体在真实正例上的真正例率相同。 |
| 15 | Equalized Odds | 均衡机会 |  | 不同群体的真正例率和假正例率都相同。 |
| 16 | Algorithmic Bias | 算法偏差 |  | 算法预测中可能出现的系统性不公平差异。 |
| 17 | Robustness | 鲁棒性 |  | 面对噪声、扰动或环境变化仍稳定工作的能力。 |
| 18 | Adversarial Example | 对抗样本 |  | 经过特定扰动以诱导模型错误预测的输入。 |
| 19 | Adversarial Training | 对抗训练 |  | 在训练中加入对抗扰动以提升稳健性的方法。 |
| 20 | Privacy-preserving ML | 隐私保护机器学习 |  | 尽量减少模型训练或使用时隐私风险的技术。 |
| 21 | Differential Privacy (DP) | 差分隐私 | DP | 限制单个记录对输出分布影响的隐私保证框架。 |
| 22 | Federated Learning | 联邦学习 |  | 数据留在本地、多方协同训练模型的机制。 |
| 23 | Model Card | 模型卡片 |  | 记录模型用途、评估、限制及风险的说明文档。 |
| 24 | Dataset Documentation | 数据集文档 |  | 描述数据来源、采样、标注和适用边界的信息。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/machine-learning.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
