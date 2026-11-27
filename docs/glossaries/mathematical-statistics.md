# 数理统计 · Mathematical Statistics

> Professional Bilingual Statistical Glossary | 专业中英文术语对照表

**400 条术语 · 16 个专业章节 · 2026-11-27**

以经典数理统计课程体系组织：统计模型、常见分布、抽样分布、充分性、估计、置信区间、假设检验、渐近理论、似然推断、回归与实验设计，以及非参数、重抽样、贝叶斯与现代应用。定义均为独立撰写的简明概括，具体结论须考虑分布、独立性、正则性、样本设计和识别假设。

**编辑审稿状态：**结构、字段、计数和英文术语重复项自动校验；未宣称独立专家逐条技术审稿。

## 目录

- 01. 统计推断基础与数据生成（25 条）
- 02. 概率分布与参数族（25 条）
- 03. 样本统计量与抽样分布（25 条）
- 04. 数据约简、充分性与指数族（25 条）
- 05. 点估计、损失与估计量性质（25 条）
- 06. 区间估计与置信集合（25 条）
- 07. 假设检验原理与决策理论（25 条）
- 08. 经典参数检验与列联分析（25 条）
- 09. 大样本理论与渐近推断（25 条）
- 10. 似然理论、Fisher 信息与推断（25 条）
- 11. 线性回归与广义线性模型（25 条）
- 12. 方差分析、实验设计与随机化（25 条）
- 13. 非参数统计与经验过程（25 条）
- 14. 重抽样、多重检验与研究可信度（25 条）
- 15. 贝叶斯推断与计算方法（25 条）
- 16. 多元、时间序列、生存与因果推断（25 条）

---

## 01. 统计推断基础与数据生成

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Mathematical Statistics | 数理统计 |  | 利用概率论研究从随机数据推断未知总体特征的方法与理论。 |
| 2 | Statistical Inference | 统计推断 |  | 基于观察数据对总体参数、分布或科学假设作出推断的过程。 |
| 3 | Population | 总体 |  | 研究目标所对应的全部单位或随机生成机制。 |
| 4 | Sample | 样本 |  | 从总体或数据生成过程获得的一组观测。 |
| 5 | Observation | 观测值 |  | 对单个研究对象或事件记录的变量取值。 |
| 6 | Sampling Unit | 抽样单位 |  | 在抽样设计中被选取的最基本对象或集合。 |
| 7 | Statistical Unit | 统计单位 |  | 实际测量属性或结果的分析对象。 |
| 8 | Parameter | 参数 |  | 描述统计模型或总体特征的未知常数。 |
| 9 | Statistic | 统计量 |  | 只依赖样本观测而不含未知参数的可计算函数。 |
| 10 | Estimator | 估计量 |  | 用于推断未知参数的样本函数。 |
| 11 | Estimate | 估计值 |  | 估计量在某次实际样本上计算得到的数值。 |
| 12 | Sampling Design | 抽样设计 |  | 规定样本如何从目标总体被选择的概率或程序规则。 |
| 13 | Simple Random Sampling | 简单随机抽样 | SRS | 使规定大小的每个单位子集有相同被选概率的抽样方法。 |
| 14 | Stratified Sampling | 分层抽样 |  | 按已知特征划分层并在每层独立抽样的方法。 |
| 15 | Cluster Sampling | 整群抽样 |  | 首先抽取群组，再调查群内全部或部分单位的设计。 |
| 16 | Systematic Sampling | 系统抽样 |  | 在随机起点后按固定间隔选取总体单位的方法。 |
| 17 | Sampling Frame | 抽样框 |  | 可用于实施抽样的目标单位名单或覆盖结构。 |
| 18 | Selection Bias | 选择偏倚 |  | 样本进入机制使观测分布系统性偏离研究目标的偏倚。 |
| 19 | Nonresponse Bias | 无应答偏倚 |  | 未回答单位与回答单位系统性不同而造成的估计偏差。 |
| 20 | Measurement Error | 测量误差 |  | 记录值与真实目标量之间因仪器或过程产生的差异。 |
| 21 | Confounding Variable | 混杂变量 |  | 同时关联解释因素与结局、可能扭曲两者关系的变量。 |
| 22 | Independent and Identically Distributed | 独立同分布 | IID | 样本分量相互独立且具有相同概率分布的假设。 |
| 23 | Random Sample | 随机样本 |  | 通常指从同一分布独立抽取的一组随机变量。 |
| 24 | Statistical Model | 统计模型 |  | 为数据生成分布指定的概率分布族。 |
| 25 | Model Misspecification | 模型设定错误 |  | 假设的分布族或结构不能充分描述真实数据机制的情形。 |

## 02. 概率分布与参数族

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Probability Distribution | 概率分布 |  | 为随机变量可能取值或事件分配概率的数学规律。 |
| 2 | Probability Mass Function | 概率质量函数 | PMF | 为离散随机变量每个可能取值给出概率的函数。 |
| 3 | Probability Density Function | 概率密度函数 | PDF | 连续变量在区间上积分得到概率的非负函数。 |
| 4 | Cumulative Distribution Function | 累积分布函数 | CDF | 给出随机变量不大于某个阈值概率的函数。 |
| 5 | Survival Function | 生存函数 |  | 给出随机变量大于某阈值概率的函数。 |
| 6 | Quantile Function | 分位数函数 |  | 把概率水平映射为分布阈值的广义反函数。 |
| 7 | Bernoulli Distribution | 伯努利分布 |  | 描述一次成功或失败试验的二点离散分布。 |
| 8 | Binomial Distribution | 二项分布 |  | 描述固定次数独立伯努利试验成功总数的分布。 |
| 9 | Poisson Distribution | 泊松分布 |  | 以单个速率参数描述单位区间独立事件计数的离散分布。 |
| 10 | Geometric Distribution | 几何分布 |  | 描述首次成功所需试验次数或之前失败次数的分布。 |
| 11 | Negative Binomial Distribution | 负二项分布 |  | 描述达到指定成功次数前失败数等计数的分布。 |
| 12 | Hypergeometric Distribution | 超几何分布 |  | 有限总体不放回抽样中成功单位数量的分布。 |
| 13 | Discrete Uniform Distribution | 离散均匀分布 |  | 在有限离散取值集合上分配相同概率的分布。 |
| 14 | Continuous Uniform Distribution | 连续均匀分布 |  | 在有限区间具有常数密度的分布。 |
| 15 | Normal Distribution | 正态分布 |  | 由均值与方差确定、密度呈钟形的连续分布。 |
| 16 | Standard Normal Distribution | 标准正态分布 |  | 均值为零且方差为一的正态分布。 |
| 17 | Student t Distribution | 学生 t 分布 |  | 正态变量与独立卡方变量标准化比值产生的分布。 |
| 18 | Chi-square Distribution | 卡方分布 |  | 若干独立标准正态变量平方和所服从的分布。 |
| 19 | F Distribution | F 分布 |  | 两个独立卡方变量分别除以其自由度所得比值的分布。 |
| 20 | Exponential Distribution | 指数分布 |  | 具有无记忆性质的连续非负等待时间分布。 |
| 21 | Gamma Distribution | 伽马分布 |  | 可描述多个独立指数等待时间和的非负连续分布族。 |
| 22 | Beta Distribution | 贝塔分布 |  | 定义在零到一区间、由两个形状参数控制的连续分布。 |
| 23 | Weibull Distribution | 威布尔分布 |  | 用于寿命分析、可产生不同危险率形状的正值分布。 |
| 24 | Lognormal Distribution | 对数正态分布 |  | 对数服从正态分布的正值随机变量分布。 |
| 25 | Multivariate Normal Distribution | 多元正态分布 |  | 由均值向量及协方差矩阵刻画的联合正态分布。 |

## 03. 样本统计量与抽样分布

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sample Mean | 样本均值 |  | 样本观测值的算术平均数。 |
| 2 | Sample Median | 样本中位数 |  | 排序后位于样本位置中央的值或两中央值的平均。 |
| 3 | Sample Variance | 样本方差 |  | 样本偏离均值平方和的标准化量，分母可取 n 或 n−1。 |
| 4 | Unbiased Sample Variance | 无偏样本方差 |  | 以 n−1 为分母、在 IID 且方差有限时无偏估计总体方差的统计量。 |
| 5 | Sample Standard Deviation | 样本标准差 |  | 样本方差的非负平方根。 |
| 6 | Sample Proportion | 样本比例 |  | 样本中满足某项二元属性的单位所占比例。 |
| 7 | Order Statistic | 次序统计量 |  | 将样本排序后指定秩位置的观测值。 |
| 8 | Sample Range | 样本极差 |  | 样本最大值与最小值之差。 |
| 9 | Interquartile Range | 四分位距 | IQR | 上四分位数与下四分位数之差。 |
| 10 | Sample Covariance | 样本协方差 |  | 衡量两变量共同变化方向与幅度的样本中心化乘积统计量。 |
| 11 | Pearson Correlation Coefficient | 皮尔逊相关系数 |  | 协方差除以两变量标准差后得到的线性相关度量。 |
| 12 | Spearman Rank Correlation | 斯皮尔曼等级相关系数 |  | 对观测秩次计算相关性的单调关联度量。 |
| 13 | Sampling Distribution | 抽样分布 |  | 在重复使用同一抽样方案时统计量取值的概率分布。 |
| 14 | Standard Error | 标准误 |  | 估计量抽样分布的标准差。 |
| 15 | Degrees of Freedom | 自由度 |  | 统计量或残差在约束下可独立变化的维数或参数。 |
| 16 | Pooled Variance | 合并方差 |  | 在等方差假设下结合多组样本信息得到的共同方差估计。 |
| 17 | Coefficient of Variation | 变异系数 | CV | 标准差与非零均值的比值，用于描述相对离散程度。 |
| 18 | Sample Skewness | 样本偏度 |  | 以样本中心三阶矩刻画分布不对称性的统计量。 |
| 19 | Sample Kurtosis | 样本峰度 |  | 基于四阶标准化中心矩描述尾部与峰形的统计量。 |
| 20 | Moment | 矩 |  | 随机变量幂次或中心化幂次的期望，概括分布形状。 |
| 21 | Raw Moment | 原点矩 |  | 随机变量 k 次幂的期望。 |
| 22 | Central Moment | 中心矩 |  | 随机变量相对均值偏差的 k 次幂期望。 |
| 23 | Moment Generating Function | 矩母函数 | MGF | 在存在的邻域内，用指数变换期望编码分布矩的函数。 |
| 24 | Characteristic Function | 特征函数 |  | 复指数变换的期望，在全部实数自变量上存在。 |
| 25 | Probability Generating Function | 概率母函数 | PGF | 用幂级数期望表征非负整数随机变量分布的函数。 |

## 04. 数据约简、充分性与指数族

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Reduction | 数据约简 |  | 通过提取统计量减少原始数据维度并保留推断信息的过程。 |
| 2 | Sufficient Statistic | 充分统计量 |  | 在给定该统计量后，样本条件分布与未知参数无关的统计量。 |
| 3 | Minimal Sufficient Statistic | 最小充分统计量 |  | 能由任何其他充分统计量确定的充分统计量。 |
| 4 | Factorization Theorem | 因子分解定理 |  | 利用似然密度或质量函数的分解判定统计量充分性的定理。 |
| 5 | Likelihood Factorization | 似然因子分解 |  | 将联合样本概率表示为参数依赖部分与参数无关部分乘积的形式。 |
| 6 | Complete Statistic | 完全统计量 |  | 任何期望恒为零的统计量函数几乎必然为零的统计量。 |
| 7 | Boundedly Complete Statistic | 有界完全统计量 |  | 完全性的判定只要求有界可测函数满足零期望性质。 |
| 8 | Ancillary Statistic | 辅助统计量 |  | 其抽样分布不依赖未知参数的统计量。 |
| 9 | Basu Theorem | 巴苏定理 |  | 完全充分统计量与辅助统计量相互独立的经典结论。 |
| 10 | Rao–Blackwell Theorem | 拉奥—布莱克威尔定理 |  | 对估计量条件化于充分统计量可使凸损失风险不增的定理。 |
| 11 | Lehmann–Scheffé Theorem | 莱曼—谢费定理 |  | 完全充分统计量的无偏函数在通常条件下为唯一 UMVU 估计量。 |
| 12 | Exponential Family | 指数族 |  | 概率密度可表示为统计量与自然参数内积的指数形式的分布族。 |
| 13 | Natural Parameter | 自然参数 |  | 指数族表达式中与充分统计量直接内积的参数。 |
| 14 | Natural Statistic | 自然统计量 |  | 指数族表达式中与自然参数耦合的样本函数。 |
| 15 | Log-partition Function | 对数配分函数 |  | 使指数族密度归一化的指数归一化常数的对数。 |
| 16 | Canonical Form | 规范参数形式 |  | 用指数族自然参数与自然统计量表示分布的形式。 |
| 17 | Full Exponential Family | 完全指数族 |  | 自然参数空间覆盖所允许区域而非受额外低维限制的指数族。 |
| 18 | Curved Exponential Family | 曲指数族 |  | 自然参数被约束在低维曲面上的指数族。 |
| 19 | Parameter Space | 参数空间 |  | 统计模型允许未知参数取得的全部值的集合。 |
| 20 | Nuisance Parameter | 干扰参数 |  | 虽影响数据分布、但不是当前推断目标的未知参数。 |
| 21 | Parameter of Interest | 目标参数 |  | 研究所希望估计或检验的参数分量或函数。 |
| 22 | Identifiability | 可识别性 |  | 不同参数值对应不同可观测分布的模型性质。 |
| 23 | Nonidentifiability | 不可识别性 |  | 存在不同参数值产生同一观测分布而无法由数据区分的现象。 |
| 24 | Invariant Statistic | 不变统计量 |  | 在指定变换群作用下保持取值不变的统计量。 |
| 25 | Maximal Invariant | 极大不变统计量 |  | 能区分变换群各不同轨道的不变统计量。 |

## 05. 点估计、损失与估计量性质

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Point Estimation | 点估计 |  | 使用单个统计量数值推测未知参数的推断方式。 |
| 2 | Bias of an Estimator | 估计量偏差 |  | 估计量期望与真实目标参数之间的差。 |
| 3 | Unbiased Estimator | 无偏估计量 |  | 在参数空间内期望等于目标参数的估计量。 |
| 4 | Asymptotically Unbiased Estimator | 渐近无偏估计量 |  | 样本量增大时偏差趋于零的估计量。 |
| 5 | Consistent Estimator | 相合估计量 |  | 样本量增大时依概率收敛到真实参数的估计量。 |
| 6 | Mean Squared Error | 均方误差 | MSE | 估计量与目标参数之差的平方期望。 |
| 7 | Variance of an Estimator | 估计量方差 |  | 估计量围绕其期望值抽样波动程度的平方量。 |
| 8 | Bias–Variance Decomposition | 偏差—方差分解 |  | 平方损失风险可拆成估计量方差与偏差平方之和。 |
| 9 | Efficiency of an Estimator | 估计效率 |  | 相对于理论下界或另一估计量衡量抽样方差的性质。 |
| 10 | Relative Efficiency | 相对效率 |  | 比较两个估计量方差或风险表现的比值。 |
| 11 | Maximum Likelihood Estimator | 极大似然估计量 | MLE | 选择使观测数据似然达到最大值的参数估计量。 |
| 12 | Method of Moments | 矩估计法 | MoM | 以样本矩匹配理论矩来求解未知参数的估计方法。 |
| 13 | Generalized Method of Moments | 广义矩估计法 | GMM | 通过一组矩条件构造加权二次目标并估计参数。 |
| 14 | Minimum Variance Unbiased Estimator | 最小方差无偏估计量 | MVUE | 在无偏估计量类中具有最低方差的估计量。 |
| 15 | Uniformly Minimum Variance Unbiased Estimator | 一致最小方差无偏估计量 | UMVUE | 对所有允许参数均达到无偏类最小方差的估计量。 |
| 16 | Best Linear Unbiased Estimator | 最佳线性无偏估计量 | BLUE | 在线性无偏估计量类中协方差最小的估计量。 |
| 17 | Loss Function | 损失函数 |  | 量化估计行动与真实参数之间代价的函数。 |
| 18 | Quadratic Loss | 平方损失 |  | 估计误差的平方，常用于推导均方误差最优估计。 |
| 19 | Absolute Error Loss | 绝对误差损失 |  | 估计值与目标之间差值绝对值构成的损失。 |
| 20 | Risk Function | 风险函数 |  | 给定真实参数时，估计规则损失的期望。 |
| 21 | Admissible Estimator | 容许估计量 |  | 不存在在所有参数上风险不高且至少一处更低的其他估计量。 |
| 22 | Minimax Estimator | 极小极大估计量 |  | 使参数空间内最大风险达到最小的估计量。 |
| 23 | Shrinkage Estimator | 收缩估计量 |  | 将初始估计朝某个中心或结构压缩以改善平均风险的估计方法。 |
| 24 | James–Stein Estimator | James–Stein 估计量 |  | 在维度至少为三的正态均值估计中可支配通常样本均值的收缩估计量。 |
| 25 | Empirical Bayes Estimator | 经验贝叶斯估计量 |  | 用观测样本估计先验超参数后构造贝叶斯型估计的规则。 |

## 06. 区间估计与置信集合

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Interval Estimation | 区间估计 |  | 用依数据而变的区间表达未知参数估计不确定性的方式。 |
| 2 | Confidence Interval | 置信区间 | CI | 按预定覆盖率构造、在重复抽样中包含固定真参数的随机区间。 |
| 3 | Confidence Level | 置信水平 |  | 置信区间构造程序预先设定的覆盖概率下界或标称值。 |
| 4 | Coverage Probability | 覆盖概率 |  | 给定真实参数时随机置信集合覆盖该参数的概率。 |
| 5 | Confidence Set | 置信集合 |  | 用随机集合而不局限于数轴区间表达参数不确定性的推断结果。 |
| 6 | Two-sided Confidence Interval | 双侧置信区间 |  | 同时具有下界与上界的随机区间。 |
| 7 | One-sided Confidence Bound | 单侧置信界 |  | 仅提供参数上界或下界的置信推断结果。 |
| 8 | Margin of Error | 误差限 |  | 置信区间中心至端点的半宽度，适用于对称区间表达。 |
| 9 | Pivotal Quantity | 枢轴量 |  | 抽样分布不依赖未知参数的样本与参数函数。 |
| 10 | Pivot Method | 枢轴法 |  | 反演枢轴量分位数不等式构造置信区间的方法。 |
| 11 | Normal Approximation Interval | 正态近似区间 |  | 利用估计量近似正态分布构造的置信区间。 |
| 12 | Student t Confidence Interval | 学生 t 置信区间 |  | 利用 t 抽样分布估计正态总体均值的区间。 |
| 13 | Wald Confidence Interval | Wald 置信区间 |  | 用参数估计值及其标准误构成的渐近正态区间。 |
| 14 | Score Confidence Interval | 得分置信区间 |  | 通过反演得分检验获得的参数区间。 |
| 15 | Likelihood-ratio Confidence Region | 似然比置信域 |  | 通过反演似然比检验得到的参数集合。 |
| 16 | Wilson Score Interval | Wilson 得分区间 |  | 反演二项比例得分检验得到的比例置信区间。 |
| 17 | Clopper–Pearson Interval | Clopper–Pearson 区间 |  | 通过反演精确二项检验构造的保守比例区间。 |
| 18 | Bootstrap Percentile Interval | Bootstrap 百分位区间 |  | 取重抽样估计量分布分位数作为区间端点的方法。 |
| 19 | Bootstrap-t Interval | 学生化 Bootstrap 区间 |  | 通过重抽样学生化统计量的分位数反演构造的区间。 |
| 20 | BCa Bootstrap Interval | 偏差校正加速 Bootstrap 区间 | BCa | 利用偏差校正和加速因子调整重抽样分位数的区间。 |
| 21 | Profile Likelihood Interval | 剖面似然区间 |  | 在每个目标参数值下优化干扰参数后反演似然比的区间。 |
| 22 | Prediction Interval | 预测区间 |  | 为未来单个观测或指定预测量提供覆盖保证的随机区间。 |
| 23 | Tolerance Interval | 容忍区间 |  | 以指定置信度覆盖总体中至少给定比例个体的区间。 |
| 24 | Simultaneous Confidence Interval | 同时置信区间 |  | 控制一组参数区间同时覆盖真值概率的推断程序。 |
| 25 | Multiplicity-adjusted Interval | 多重性校正区间 |  | 针对多个比较调整覆盖要求以控制总体错误率的置信区间。 |

## 07. 假设检验原理与决策理论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Statistical Hypothesis | 统计假设 |  | 关于总体分布、参数或随机机制的可检验命题。 |
| 2 | Null Hypothesis | 原假设 | H0 | 检验中作为基准或待反驳的假设集合。 |
| 3 | Alternative Hypothesis | 备择假设 | H1 | 原假设之外、研究希望获得证据支持的参数或分布集合。 |
| 4 | Simple Hypothesis | 简单假设 |  | 完全指定一个概率分布的统计假设。 |
| 5 | Composite Hypothesis | 复合假设 |  | 包含两个或更多可能概率分布的统计假设。 |
| 6 | Test Statistic | 检验统计量 |  | 从样本计算并用于判断是否拒绝原假设的函数。 |
| 7 | Rejection Region | 拒绝域 |  | 统计量落入后决定拒绝原假设的结果集合。 |
| 8 | Acceptance Region | 不拒绝域 |  | 检验规则不拒绝原假设的观测结果集合。 |
| 9 | Significance Level | 显著性水平 | α | 事先规定的最大允许第一类错误概率，通常针对原假设取上确界。 |
| 10 | Type I Error | 第一类错误 |  | 原假设为真时错误拒绝它。 |
| 11 | Type II Error | 第二类错误 |  | 备择假设为真时未拒绝原假设。 |
| 12 | Power Function | 功效函数 |  | 随参数值变化的拒绝原假设概率函数。 |
| 13 | Statistical Power | 检验功效 |  | 在指定备择参数或效应下正确拒绝原假设的概率。 |
| 14 | P-value | p 值 |  | 在原假设成立下，检验统计量至少同样极端的尾部概率或相应复合零假设上界。 |
| 15 | Critical Value | 临界值 |  | 将统计量取值划分为拒绝和不拒绝区域的阈值。 |
| 16 | One-sided Test | 单侧检验 |  | 备择强调参数向单一方向偏离的检验。 |
| 17 | Two-sided Test | 双侧检验 |  | 备择允许参数朝两个方向偏离的检验。 |
| 18 | Most Powerful Test | 最强力检验 |  | 在给定显著性水平下，对指定备择具有最大功效的检验。 |
| 19 | Uniformly Most Powerful Test | 一致最强力检验 | UMP | 在整个备择参数集合上均具有最大功效的检验。 |
| 20 | Neyman–Pearson Lemma | 奈曼—皮尔逊引理 |  | 对两个简单假设，以似然比阈值构造最强力检验的定理。 |
| 21 | Likelihood Ratio Test | 似然比检验 | LRT | 比较受限与不受限参数空间内的最大似然值的检验。 |
| 22 | Wald Test | Wald 检验 |  | 利用参数估计值与其估计协方差衡量偏离原假设的检验。 |
| 23 | Score Test | 得分检验 |  | 在原假设限制下依据对数似然一阶导数检测偏离的检验。 |
| 24 | Test Inversion | 检验反演 |  | 收集所有未被对应假设检验拒绝的参数值构造置信集合。 |
| 25 | Equivalence Test | 等效性检验 |  | 检验效应是否落入预先规定的等效范围，而非是否精确为零。 |

## 08. 经典参数检验与列联分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | One-sample t Test | 单样本 t 检验 |  | 在正态或适当大样本条件下检验总体均值是否等于指定值。 |
| 2 | Two-sample t Test | 双样本 t 检验 |  | 对两个独立样本均值差进行推断的参数检验。 |
| 3 | Paired t Test | 配对 t 检验 |  | 对成对观测的差值均值进行的单样本 t 检验。 |
| 4 | Welch t Test | Welch t 检验 |  | 不假设两总体方差相同的独立双样本均值检验。 |
| 5 | Z Test | Z 检验 |  | 用标准正态参考分布对参数或标准化统计量作检验。 |
| 6 | Chi-square Goodness-of-fit Test | 卡方拟合优度检验 |  | 用观测与期望频数差异检验分类分布拟合程度的方法。 |
| 7 | Pearson Chi-square Test | 皮尔逊卡方检验 |  | 使用 Pearson 卡方统计量检验分类变量关系或拟合情况的检验。 |
| 8 | Chi-square Test of Independence | 卡方独立性检验 |  | 判断列联表两个分类变量是否独立的渐近检验。 |
| 9 | Fisher Exact Test | Fisher 精确检验 |  | 通过条件超几何分布对列联表关联作精确概率检验。 |
| 10 | McNemar Test | McNemar 检验 |  | 对配对二元结果的非对角频数比较边际同质性。 |
| 11 | Binomial Test | 二项检验 |  | 基于确切二项分布检验成功概率的程序。 |
| 12 | Poisson Rate Test | 泊松率检验 |  | 依据泊松计数及暴露时间检验事件发生率的程序。 |
| 13 | Variance Ratio Test | 方差比检验 |  | 在独立正态总体假设下用 F 分布检验方差比。 |
| 14 | Bartlett Test | Bartlett 方差齐性检验 |  | 在近似正态前提下检验多个总体方差相等的统计方法。 |
| 15 | Levene Test | Levene 方差齐性检验 |  | 利用组内绝对偏差检验不同组方差是否相等。 |
| 16 | Brown–Forsythe Test | Brown–Forsythe 检验 |  | 基于组内对中位数绝对偏差的稳健方差齐性检验。 |
| 17 | Shapiro–Wilk Test | Shapiro–Wilk 正态性检验 |  | 比较样本有序值与正态期望次序结构的正态性检验。 |
| 18 | Kolmogorov–Smirnov Test | Kolmogorov–Smirnov 检验 | KS | 用经验分布函数与参考分布的最大偏差作拟合或两样本检验。 |
| 19 | Anderson–Darling Test | Anderson–Darling 检验 |  | 对经验分布与理论分布偏差赋予尾部更大权重的拟合检验。 |
| 20 | Jarque–Bera Test | Jarque–Bera 检验 |  | 基于样本偏度与峰度检验正态性的大样本方法。 |
| 21 | Odds Ratio | 优势比 | OR | 比较两组事件优势的比值，常用于二元结局关联分析。 |
| 22 | Risk Ratio | 风险比 | RR | 两组事件发生概率的比值，亦称相对风险。 |
| 23 | Risk Difference | 风险差 | RD | 两组事件发生概率相减得到的绝对效应量。 |
| 24 | Contingency Table | 列联表 |  | 按两个或更多分类变量联合频数交叉汇总的数据表。 |
| 25 | Expected Cell Count | 期望单元格频数 |  | 在给定零假设下列联表各单元格的理论期望计数。 |

## 09. 大样本理论与渐近推断

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Asymptotic Statistics | 渐近统计 |  | 研究样本量趋于无穷时估计量与检验统计量性质的理论。 |
| 2 | Convergence in Probability | 依概率收敛 |  | 估计误差超过任意固定正阈值的概率趋于零的收敛方式。 |
| 3 | Almost Sure Convergence | 几乎处处收敛 |  | 随机变量序列在概率为一的事件上逐点收敛。 |
| 4 | Convergence in Distribution | 依分布收敛 |  | 随机变量分布函数在极限分布连续点收敛的性质。 |
| 5 | Convergence in Mean Square | 均方收敛 |  | 随机变量与极限之间平方差的期望趋于零的收敛方式。 |
| 6 | Weak Law of Large Numbers | 弱大数定律 | WLLN | 在适当条件下样本均值依概率趋向总体期望的定理。 |
| 7 | Strong Law of Large Numbers | 强大数定律 | SLLN | 在适当条件下样本均值几乎处处收敛到总体期望的定理。 |
| 8 | Central Limit Theorem | 中心极限定理 | CLT | 在相应条件下标准化随机变量和趋近正态分布的定理族。 |
| 9 | Lindeberg Condition | 林德伯格条件 |  | 用于三角阵中心极限定理、控制单项大偏差贡献的条件。 |
| 10 | Lyapunov Condition | 李雅普诺夫条件 |  | 通过高阶矩上界确保一类独立变量中心极限定理成立的充分条件。 |
| 11 | Slutsky Theorem | 斯卢茨基定理 |  | 将依分布收敛与依概率收敛的随机量组合得到极限分布的定理。 |
| 12 | Continuous Mapping Theorem | 连续映射定理 |  | 在适当连续性条件下收敛随机变量经函数映射仍收敛的定理。 |
| 13 | Delta Method | Delta 方法 |  | 借助泰勒展开推导可微变换后估计量渐近分布的方法。 |
| 14 | Multivariate Delta Method | 多元 Delta 方法 |  | 以函数雅可比矩阵传播多元估计量渐近协方差的方法。 |
| 15 | Asymptotic Normality | 渐近正态性 |  | 经适当中心化和缩放的统计量依分布趋向正态分布的性质。 |
| 16 | Asymptotic Variance | 渐近方差 |  | 估计量标准化极限分布的方差参数。 |
| 17 | Asymptotic Bias | 渐近偏差 |  | 大样本尺度上估计量期望相对真值的系统差异。 |
| 18 | Asymptotic Efficiency | 渐近效率 |  | 根据极限方差或局部风险比较估计程序效率的性质。 |
| 19 | Asymptotic Relative Efficiency | 渐近相对效率 | ARE | 达到相同精度所需样本量或极限方差的比较指标。 |
| 20 | Stochastic Order | 随机阶记号 |  | 用概率界刻画随机变量序列规模的符号。 |
| 21 | Big O in Probability | 依概率有界阶 | Op | 表示随机量按给定尺度缩放后在概率意义下有界。 |
| 22 | Little o in Probability | 依概率小阶 | op | 表示随机量按给定尺度缩放后依概率趋向零。 |
| 23 | Contiguity | 相邻连续性 |  | 一个概率测度序列的零概率极限事件也被另一序列赋予渐近零概率的关系。 |
| 24 | Local Asymptotic Normality | 局部渐近正态性 | LAN | 局部参数扰动下对数似然比近似高斯移位结构的性质。 |
| 25 | Berry–Esseen Bound | 贝里—埃塞恩界 |  | 在矩条件下量化标准化独立变量和与正态分布之间最大误差的上界。 |

## 10. 似然理论、Fisher 信息与推断

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Likelihood Function | 似然函数 |  | 把观测数据固定后视为未知参数函数的概率密度或质量函数。 |
| 2 | Log-likelihood | 对数似然 |  | 似然函数取对数后得到、便于求导和数值计算的目标函数。 |
| 3 | Score Function | 得分函数 |  | 对数似然函数对模型参数的一阶导数或梯度。 |
| 4 | Observed Information | 观测信息 |  | 观测数据对应负对数似然海森矩阵的值。 |
| 5 | Fisher Information | 费舍尔信息 |  | 在正则条件下等于得分方差或负期望海森矩阵的信息量。 |
| 6 | Information Matrix | 信息矩阵 |  | 多参数模型中以得分协方差刻画参数局部可辨程度的矩阵。 |
| 7 | Cramér–Rao Lower Bound | 克拉美—罗下界 | CRLB | 在正则条件下对无偏估计量方差给出的信息论下界。 |
| 8 | Information Inequality | 信息不等式 |  | 把无偏估计量方差与 Fisher 信息联系起来的不等式。 |
| 9 | Regularity Conditions | 正则性条件 |  | 允许微积分、期望交换与渐近展开等操作成立的模型假设。 |
| 10 | Likelihood Principle | 似然原则 |  | 主张固定观测数据的似然函数承载关于参数的全部相关证据的原则。 |
| 11 | Profile Likelihood | 剖面似然 |  | 对干扰参数取最大化后得到的目标参数似然函数。 |
| 12 | Marginal Likelihood | 边际似然 |  | 对未观察变量或参数按指定概率分布积分所得的数据似然。 |
| 13 | Partial Likelihood | 偏似然 |  | 只利用部分联合样本分布结构构建的推断似然。 |
| 14 | Composite Likelihood | 复合似然 |  | 组合低维边际或条件似然以近似完整联合似然的方法。 |
| 15 | Penalized Likelihood | 惩罚似然 |  | 从似然目标中减去复杂度或参数惩罚项的估计准则。 |
| 16 | Likelihood Ratio Statistic | 似然比统计量 |  | 以受限与非受限最大似然值之比构成的检验量。 |
| 17 | Wilks Theorem | 威尔克斯定理 |  | 在正则嵌套模型下负二倍对数似然比渐近服从卡方分布的结果。 |
| 18 | Information Criterion | 信息准则 |  | 以拟合优度和模型复杂度惩罚比较统计模型的分数。 |
| 19 | Akaike Information Criterion | 赤池信息准则 | AIC | 用负二倍最大对数似然加参数数目的两倍比较模型。 |
| 20 | Bayesian Information Criterion | 贝叶斯信息准则 | BIC | 用负二倍最大对数似然加参数数目乘样本量对数的准则。 |
| 21 | Cross-entropy | 交叉熵 |  | 按一个分布对另一分布的对数概率取负期望的量。 |
| 22 | Kullback–Leibler Divergence | 库尔贝克—莱布勒散度 | KL | 衡量两个概率分布相对信息差异的非对称函数。 |
| 23 | Hellinger Distance | 海林格距离 |  | 由两个分布平方根密度差定义的对称概率距离。 |
| 24 | Total Variation Distance | 全变差距离 |  | 两个概率分布对所有事件赋予概率差的最大绝对值。 |
| 25 | Identified Set | 可识别集合 |  | 与所观察数据分布相容的全部目标参数值集合。 |

## 11. 线性回归与广义线性模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Linear Regression | 线性回归 |  | 将响应变量条件均值表示为解释变量线性组合的建模方法。 |
| 2 | Simple Linear Regression | 一元线性回归 |  | 使用一个解释变量和截距拟合响应变量的线性模型。 |
| 3 | Multiple Linear Regression | 多元线性回归 |  | 同时用多个解释变量解释响应均值的线性模型。 |
| 4 | Ordinary Least Squares | 普通最小二乘 | OLS | 通过最小化残差平方和估计线性模型系数的方法。 |
| 5 | Generalized Least Squares | 广义最小二乘 | GLS | 在误差协方差已知或可建模时用逆协方差加权估计系数。 |
| 6 | Weighted Least Squares | 加权最小二乘 | WLS | 以不同观测的非负权重最小化平方残差和的估计方法。 |
| 7 | Regression Coefficient | 回归系数 |  | 控制其他模型变量时，解释变量单位变化对应的模型参数。 |
| 8 | Intercept | 截距 |  | 当全部解释变量为零时模型线性预测器的常数项。 |
| 9 | Residual | 残差 |  | 观测响应减去模型预测响应的差值。 |
| 10 | Fitted Value | 拟合值 |  | 依据估计模型与观测解释变量计算的预测响应值。 |
| 11 | Hat Matrix | 帽子矩阵 |  | 在线性最小二乘中把响应向量映射为拟合值的投影矩阵。 |
| 12 | Leverage | 杠杆值 |  | 量化观测解释变量在回归设计空间中异常程度的帽子矩阵对角元。 |
| 13 | Influential Observation | 有影响观测 |  | 删除或改变该观测会显著影响拟合系数或预测的样本。 |
| 14 | Cook Distance | 库克距离 |  | 衡量删除某观测对整体回归拟合影响程度的诊断量。 |
| 15 | Coefficient of Determination | 决定系数 | R² | 描述回归模型相对基准解释响应变化程度的统计量。 |
| 16 | Adjusted R-squared | 调整决定系数 |  | 考虑解释变量数量与样本量对 R² 做自由度调整的指标。 |
| 17 | Multicollinearity | 多重共线性 |  | 多个解释变量高度线性关联使部分系数估计不稳定的现象。 |
| 18 | Variance Inflation Factor | 方差膨胀因子 | VIF | 衡量解释变量与其他解释变量线性相关引起系数方差膨胀的指标。 |
| 19 | Heteroskedasticity | 异方差性 |  | 模型误差的条件方差随解释变量或样本单位变化的性质。 |
| 20 | Homoskedasticity | 同方差性 |  | 误差条件方差在给定设计范围内保持常数的假设。 |
| 21 | Generalized Linear Model | 广义线性模型 | GLM | 利用指数族响应分布和连接函数建立条件均值模型的框架。 |
| 22 | Link Function | 连接函数 |  | 把响应变量条件均值映射到线性预测器尺度的函数。 |
| 23 | Logistic Regression | 逻辑回归 |  | 通过 logit 连接函数对二元响应概率进行建模的广义线性模型。 |
| 24 | Poisson Regression | 泊松回归 |  | 常用对数连接函数建模计数条件均值的广义线性模型。 |
| 25 | Deviance | 偏差统计量 |  | 由饱和模型与拟合模型最大对数似然差构造的拟合度量。 |

## 12. 方差分析、实验设计与随机化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Analysis of Variance | 方差分析 | ANOVA | 以组间与组内变异分解检验均值或因素效应的模型方法。 |
| 2 | One-way ANOVA | 单因素方差分析 |  | 研究单一分类因素不同水平对均值影响的方差分析。 |
| 3 | Two-way ANOVA | 双因素方差分析 |  | 同时考察两个分类因素主效应及可选交互效应的分析。 |
| 4 | Factorial Design | 析因设计 |  | 在实验中系统组合多个因素水平以估计效应与交互作用的设计。 |
| 5 | Factor | 实验因素 |  | 研究者操纵或记录、可能影响响应的实验变量。 |
| 6 | Treatment | 处理 |  | 实验中施加给研究单位的具体干预条件或因素组合。 |
| 7 | Control Group | 对照组 |  | 在实验中不接受目标处理或接受基准处理的比较组。 |
| 8 | Random Assignment | 随机分配 |  | 按已知随机机制将研究单位分配至不同处理组的过程。 |
| 9 | Blocking | 区组设计 |  | 将相似实验单位先分组，再在区组内进行处理比较的策略。 |
| 10 | Randomized Complete Block Design | 随机完全区组设计 | RCBD | 每个区组包含全部处理并在区组内随机分配的实验设计。 |
| 11 | Latin Square Design | 拉丁方设计 |  | 用行列双重区组控制两个干扰因素的平衡设计。 |
| 12 | Interaction Effect | 交互效应 |  | 一个因素对响应的影响随另一因素水平变化的现象。 |
| 13 | Main Effect | 主效应 |  | 对其他因素水平平均后的某因素水平变化效应。 |
| 14 | Sum of Squares | 平方和 | SS | 对一组偏差平方求和，用于量化不同来源的变异。 |
| 15 | Residual Sum of Squares | 残差平方和 | RSS | 观测响应与拟合值差的平方之和。 |
| 16 | Mean Square | 均方 | MS | 平方和除以相应自由度得到的方差类统计量。 |
| 17 | F Statistic | F 统计量 |  | 在适当零假设与误差条件下比较两个均方的比值统计量。 |
| 18 | Balanced Design | 平衡设计 |  | 各处理组合或分类单元包含相等观测数的实验设计。 |
| 19 | Unbalanced Design | 非平衡设计 |  | 处理组合之间样本量不同的实验设计。 |
| 20 | Repeated Measures Design | 重复测量设计 |  | 同一实验单位在多个条件或时间点上被反复观测的设计。 |
| 21 | Mixed-effects Model | 混合效应模型 |  | 同时包含总体固定效应与随机效应的统计模型。 |
| 22 | Random Effect | 随机效应 |  | 把某些组别或单位差异视为来自随机分布的模型效应。 |
| 23 | Fixed Effect | 固定效应 |  | 作为待估固定系数处理的因素水平或解释变量效应。 |
| 24 | Power Analysis | 统计功效分析 |  | 根据效应量、样本量、显著性水平与误差变化推导检验功效的分析。 |
| 25 | Sample Size Calculation | 样本量计算 |  | 根据目标精度或检验功效及模型假设确定所需观测数量的过程。 |

## 13. 非参数统计与经验过程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Nonparametric Statistics | 非参数统计 |  | 不预先限定为有限维参数分布族、利用数据推断结构的统计方法领域。 |
| 2 | Distribution-free Test | 分布无关检验 |  | 零假设下统计量分布不依赖某些未知总体分布形式的检验。 |
| 3 | Sign Test | 符号检验 |  | 依据配对差值正负号检验位置或中位数条件的非参数方法。 |
| 4 | Wilcoxon Signed-rank Test | Wilcoxon 符号秩检验 |  | 利用配对差值绝对值秩及符号检验对称位置偏移的程序。 |
| 5 | Mann–Whitney U Test | Mann–Whitney U 检验 |  | 通过两组观测相对秩次比较独立样本分布的检验。 |
| 6 | Kruskal–Wallis Test | Kruskal–Wallis 检验 |  | 用合并秩次比较三个及以上独立组分布的检验。 |
| 7 | Friedman Test | Friedman 检验 |  | 利用区组内秩次比较多个配对处理条件的非参数检验。 |
| 8 | Kendall Tau | 肯德尔秩相关系数 | τ | 依据两个变量观测对的一致与不一致排序衡量单调关联的统计量。 |
| 9 | Theil–Sen Estimator | Theil–Sen 估计量 |  | 使用成对斜率中位数估计直线斜率的稳健非参数方法。 |
| 10 | Hodges–Lehmann Estimator | Hodges–Lehmann 估计量 |  | 利用 Walsh 平均或成对差值中位数构造稳健位置估计。 |
| 11 | Empirical Distribution Function | 经验分布函数 | ECDF | 样本中不大于指定值的观测比例所形成的阶梯函数。 |
| 12 | Glivenko–Cantelli Theorem | 格利文科—坎泰利定理 |  | 经验分布函数对真实分布函数一致收敛的结果。 |
| 13 | Dvoretzky–Kiefer–Wolfowitz Inequality | DKW 不等式 | DKW | 对经验分布函数最大偏差给出分布无关指数尾界的不等式。 |
| 14 | Kernel Density Estimation | 核密度估计 | KDE | 在样本点周围叠加缩放核函数估计连续概率密度的方法。 |
| 15 | Bandwidth | 带宽 |  | 平滑估计中控制邻域宽度与偏差方差权衡的参数。 |
| 16 | Histogram Density Estimate | 直方图密度估计 |  | 通过固定数据分箱内频数和箱宽估计概率密度的方法。 |
| 17 | Local Polynomial Regression | 局部多项式回归 |  | 在预测点附近加权拟合低次多项式以估计条件均值的技术。 |
| 18 | LOESS | 局部加权散点平滑 | LOESS | 在每个目标位置采用近邻加权局部回归的平滑方法。 |
| 19 | Spline Regression | 样条回归 |  | 使用分段多项式基函数及连续性约束建立灵活回归曲线的方法。 |
| 20 | Quantile Regression | 分位数回归 |  | 通过分位数损失估计响应变量指定条件分位数的回归方法。 |
| 21 | Median Regression | 中位数回归 |  | 将条件响应中位数作为预测目标的分位数回归特例。 |
| 22 | Isotonic Regression | 保序回归 |  | 在预测值必须满足单调性限制下拟合数据的回归方法。 |
| 23 | Empirical Process | 经验过程 |  | 以函数类索引的样本均值偏差随机函数集合。 |
| 24 | Functional Delta Method | 泛函 Delta 方法 |  | 通过函数空间中的可微性推导复杂统计泛函的极限分布。 |
| 25 | Rank-based Inference | 基于秩的推断 |  | 依靠观测次序而非原始数值开展参数或分布推断的方法。 |

## 14. 重抽样、多重检验与研究可信度

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Bootstrap Resampling | Bootstrap 重抽样 |  | 从观测数据重新抽取伪样本以近似统计量抽样分布的方法。 |
| 2 | Nonparametric Bootstrap | 非参数 Bootstrap |  | 从经验分布中有放回抽样并重新计算统计量的重抽样程序。 |
| 3 | Parametric Bootstrap | 参数 Bootstrap |  | 从拟合的参数分布中模拟新数据并重算统计量的程序。 |
| 4 | Block Bootstrap | 分块 Bootstrap |  | 以时间或空间相邻观测块为单位抽样、保留局部依赖结构的方法。 |
| 5 | Wild Bootstrap | 野 Bootstrap |  | 通过对残差乘随机权重生成伪样本以处理异方差等结构的方法。 |
| 6 | Bootstrap Standard Error | Bootstrap 标准误 |  | 用多次重抽样估计值的样本标准差估计原估计量标准误。 |
| 7 | Jackknife | 刀切法 |  | 系统删除观测子集并重算统计量以估计偏差和方差的方法。 |
| 8 | Delete-one Jackknife | 逐一删除刀切法 |  | 每轮从样本中删除一个观测并重算统计量的 Jackknife 特例。 |
| 9 | Permutation Test | 置换检验 |  | 在零假设可交换性条件下置换标签并比较统计量的检验。 |
| 10 | Randomization Inference | 随机化推断 |  | 依据实验实际随机分配机制计算统计量参考分布的推断框架。 |
| 11 | Cross-validation | 交叉验证 | CV | 反复分割训练与验证数据以评估拟合模型预测表现的方法。 |
| 12 | K-fold Cross-validation | K 折交叉验证 |  | 将样本划分为 K 份、逐轮留一份验证其余份拟合的方法。 |
| 13 | Leave-one-out Cross-validation | 留一交叉验证 | LOOCV | 每次留出一个观测作为验证、其余观测用于拟合的程序。 |
| 14 | Multiple Hypothesis Testing | 多重假设检验 |  | 在同一研究中同时检验多个假设并控制联合错误的统计问题。 |
| 15 | Family-wise Error Rate | 族错误率 | FWER | 一个假设族中至少错误拒绝一个真原假设的概率。 |
| 16 | False Discovery Rate | 错误发现率 | FDR | 被拒绝假设中假阳性比例的期望，零拒绝时通常定义为零。 |
| 17 | Benjamini–Hochberg Procedure | Benjamini–Hochberg 程序 | BH | 在独立或特定正依赖条件下控制 FDR 的逐步检验规则。 |
| 18 | Bonferroni Correction | Bonferroni 校正 |  | 通过将每个检验的显著性水平除以检验数控制族错误率的方法。 |
| 19 | Holm Procedure | Holm 逐步校正 |  | 按排序 p 值逐步比较调整阈值以控制 FWER 的方法。 |
| 20 | Šidák Correction | Šidák 校正 |  | 在独立检验条件下按联合概率调整单次检验阈值的方法。 |
| 21 | Westfall–Young Adjustment | Westfall–Young 校正 |  | 借助重抽样联合零分布进行多重比较调整的方法。 |
| 22 | Selective Inference | 选择性推断 |  | 在考虑数据驱动选择过程之后评估估计或检验误差的推断方法。 |
| 23 | Post-selection Inference | 模型选择后推断 |  | 对使用同一数据挑选模型后的参数推断进行校正的研究领域。 |
| 24 | P-hacking | p 值操纵 |  | 通过反复试验分析决策并选择性报告获得显著结果的研究行为。 |
| 25 | Preregistration | 预注册 |  | 在观察研究结果前记录主要假设、分析方案与决策规则的实践。 |

## 15. 贝叶斯推断与计算方法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Bayesian Inference | 贝叶斯推断 |  | 利用先验和似然通过贝叶斯定理计算参数后验分布的推断框架。 |
| 2 | Bayes Theorem | 贝叶斯定理 |  | 把条件概率与先验概率联系起来的概率恒等式。 |
| 3 | Prior Distribution | 先验分布 |  | 在分析当前数据之前为未知参数赋予的概率分布。 |
| 4 | Posterior Distribution | 后验分布 |  | 结合观察数据后依据贝叶斯定理得到的参数条件分布。 |
| 5 | Posterior Predictive Distribution | 后验预测分布 |  | 对参数后验分布积分所得未来观测的预测概率分布。 |
| 6 | Prior Predictive Distribution | 先验预测分布 |  | 对参数先验分布积分所得尚未观察数据的预测分布。 |
| 7 | Conjugate Prior | 共轭先验 |  | 更新指定似然后后验仍属于同一分布族的先验选择。 |
| 8 | Hyperparameter | 超参数 |  | 控制先验或层级模型形状、并可固定或进一步建模的参数。 |
| 9 | Maximum a Posteriori Estimate | 最大后验估计 | MAP | 选择后验密度达到最大值的参数点估计。 |
| 10 | Posterior Mean | 后验均值 |  | 参数后验分布的期望，平方损失下常为贝叶斯最优点估计。 |
| 11 | Posterior Median | 后验中位数 |  | 参数后验分布的中位数，绝对误差损失下常为贝叶斯最优点估计。 |
| 12 | Credible Interval | 可信区间 |  | 在给定数据与先验模型后，后验概率达到指定水平的参数区间。 |
| 13 | Highest Posterior Density Region | 最高后验密度区域 | HPD | 包含指定后验概率质量且优先选择高后验密度点的集合。 |
| 14 | Bayes Factor | 贝叶斯因子 | BF | 两个假设或模型对应边际似然之比。 |
| 15 | Posterior Odds | 后验优势 |  | 两个假设后验概率的比值，等于先验优势乘贝叶斯因子。 |
| 16 | Hierarchical Bayesian Model | 层级贝叶斯模型 |  | 为多层群组参数及超参数指定条件概率结构的模型。 |
| 17 | Posterior Predictive Check | 后验预测检验 |  | 将模型后验预测复制数据与实际数据比较以评估模型适配的程序。 |
| 18 | Prior Sensitivity Analysis | 先验敏感性分析 |  | 比较不同合理先验设定对后验推断结果影响的评估。 |
| 19 | Markov Chain Monte Carlo | 马尔可夫链蒙特卡洛 | MCMC | 构造以目标后验为平稳分布的马尔可夫链进行近似采样的计算方法。 |
| 20 | Gibbs Sampling | 吉布斯采样 |  | 通过逐个从参数条件后验分布采样构造马尔可夫链的方法。 |
| 21 | Metropolis–Hastings Algorithm | Metropolis–Hastings 算法 | MH | 使用提议分布和接受概率构造目标平稳分布马尔可夫链的算法。 |
| 22 | Hamiltonian Monte Carlo | 哈密顿蒙特卡洛 | HMC | 引入动量并模拟哈密顿动力学以高效采样连续参数的算法。 |
| 23 | Variational Inference | 变分推断 | VI | 通过优化可计算近似分布与目标后验的差异来进行贝叶斯近似推断。 |
| 24 | Evidence Lower Bound | 证据下界 | ELBO | 由变分分布构造的边际对数似然下界，常用作变分优化目标。 |
| 25 | Bayesian Decision Rule | 贝叶斯决策规则 |  | 选择后验期望损失最小的行动或估计规则。 |

## 16. 多元、时间序列、生存与因果推断

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Covariance Matrix | 协方差矩阵 |  | 随机向量各分量之间方差与协方差组成的对称半正定矩阵。 |
| 2 | Principal Component Analysis | 主成分分析 | PCA | 寻找正交方向使投影方差依次最大的线性降维方法。 |
| 3 | Factor Analysis | 因子分析 |  | 用少量潜在公共因子解释多变量协方差结构的统计模型。 |
| 4 | Linear Discriminant Analysis | 线性判别分析 | LDA | 在类别条件协方差共享等假设下构建线性分类判别规则的方法。 |
| 5 | Multivariate Analysis of Variance | 多元方差分析 | MANOVA | 联合检验多个响应变量处理均值向量差异的分析方法。 |
| 6 | Canonical Correlation Analysis | 典型相关分析 | CCA | 寻找两组变量线性组合间最大相关性的多元方法。 |
| 7 | Survival Analysis | 生存分析 |  | 处理事件发生时间及未完全观察事件时间的统计方法。 |
| 8 | Censoring | 删失 |  | 仅部分获知事件时间或其他响应变量真实取值的观测机制。 |
| 9 | Right Censoring | 右删失 |  | 已知事件发生时间大于某个观察终止时点的删失形式。 |
| 10 | Kaplan–Meier Estimator | Kaplan–Meier 估计量 |  | 利用事件时刻与风险集乘积极限估计生存函数的非参数方法。 |
| 11 | Hazard Function | 风险函数／危险率函数 |  | 给定已存活至某时间时事件在随后瞬间发生的条件速率。 |
| 12 | Cox Proportional Hazards Model | Cox 比例风险模型 |  | 通过协变量对数线性作用刻画事件危险率比的半参数回归模型。 |
| 13 | Log-rank Test | Log-rank 检验 |  | 在风险集基础上比较多个群组生存曲线的检验。 |
| 14 | Accelerated Failure Time Model | 加速失效时间模型 | AFT | 通过协变量线性模型描述对数生存时间或时间尺度的回归框架。 |
| 15 | Causal Inference | 因果推断 |  | 从实验或观察数据识别和估计干预对结果影响的统计研究领域。 |
| 16 | Potential Outcomes Framework | 潜在结果框架 |  | 为每种处理条件定义个体可能结果并以其差异描述因果效应的框架。 |
| 17 | Average Treatment Effect | 平均处理效应 | ATE | 目标总体中接受处理与不接受处理潜在结果差的平均。 |
| 18 | Propensity Score | 倾向得分 |  | 在给定已观测协变量条件下个体获得处理的概率。 |
| 19 | Inverse Probability Weighting | 逆概率加权 | IPW | 按处理分配或抽样概率倒数加权以估计目标量的方法。 |
| 20 | Difference-in-Differences | 双重差分 | DiD | 通过处理组与对照组随时间变化差异估计处理效果的设计。 |
| 21 | Instrumental Variable | 工具变量 | IV | 用于识别内生解释变量因果效应、需满足相关性与排除等条件的变量。 |
| 22 | Stationary Time Series | 平稳时间序列 |  | 统计性质不随时间平移而变化的序列，须说明严格或弱平稳含义。 |
| 23 | Autocorrelation Function | 自相关函数 | ACF | 描述同一时间序列不同时间间隔观测值线性相关的函数。 |
| 24 | Autoregressive Integrated Moving Average | 自回归差分移动平均模型 | ARIMA | 结合自回归、差分与移动平均成分描述时间序列的模型族。 |
| 25 | Heteroskedasticity and Autocorrelation Consistent Standard Error | 异方差与自相关稳健标准误 | HAC | 在一定条件下对异方差及序列相关稳健的协方差估计构造。 |

## 核心概念辨析

| 概念组合 | 定义区别与适用范围 |
|---|---|
| 总体参数、估计量与估计值 | 总体参数是未知的固定目标；估计量是随机样本的函数；估计值是本次样本给出的具体数值。 |
| 总体标准差与标准误 | 总体标准差描述个体取值离散程度；标准误描述估计量在重复抽样下的波动。 |
| 数据分布与抽样分布 | 数据分布是单个观察变量的概率规律；抽样分布是从重复样本计算统计量后的概率规律。 |
| 无偏性与相合性 | 无偏性要求每个样本量下估计期望等于真值；相合性要求样本量增长时估计依概率接近真值。二者互不等价。 |
| 充分统计量与完全统计量 | 充分性保证不丢失关于模型参数的抽样信息；完全性排除非平凡零期望函数，二者是不同性质。 |
| 置信区间与贝叶斯可信区间 | 频率学派置信区间的概率保证针对随机抽样程序；可信区间给定数据与先验后可有明确后验概率解释。 |
| 置信区间、预测区间和容忍区间 | 三者分别关注固定参数、未来随机观测、总体指定比例的覆盖；即使同为 95% 也有不同覆盖对象。 |
| p 值与原假设为真概率 | p 值是原假设模型下得到至少如此极端统计量的概率，不是给定数据后原假设为真的概率。 |
| 第一类错误、第二类错误与功效 | 第一类错误是原假设真时误拒绝；第二类错误是在指定备择下漏拒绝；功效为 1−第二类错误率。 |
| 统计显著性与实际显著性 | 较小 p 值并不保证效应足够大或有业务价值；应联合报告效应量、区间及研究设计。 |
| 风险比与优势比 | 风险比比较事件发生概率，优势比比较事件优势；基准事件不罕见时两者数值差异可能明显。 |
| 多重检验的 FWER 与 FDR | FWER 约束至少出现一次假阳性的概率；FDR 控制所有发现中假发现比例的期望。 |
| Bootstrap 与置换检验 | Bootstrap 常近似估计量的抽样分布；置换检验在适当可交换性零假设下构造检验统计量的参考分布。 |
| 回归相关与因果关系 | 回归关联可能受到混杂、选择或反向因果影响；因果解释通常需要随机化或明确识别假设。 |

## 中等难度面试题与答案

### 面试 1. 为什么样本方差常用 n−1 作为分母？

**参考思路：**估计总体均值消耗一个自由度；独立同分布且有限方差下，中心化平方和期望是 (n−1)σ²，因此除以 n−1 无偏。

### 面试 2. 如何区分 p 值和第一类错误率？

**参考思路：**显著性水平是检验程序事先控制的错误上界；p 值则是本次观察到的数据在零假设下的极端性指标。

### 面试 3. 什么情况下 t 区间是精确而不是渐近近似？

**参考思路：**独立正态样本、总体方差未知且按样本方差学生化时，样本均值与方差的特定独立结构给出精确 t 分布。

### 面试 4. Rao–Blackwell 化为什么可以改善估计？

**参考思路：**把原估计量对充分统计量取条件期望，仍保持无偏，并借条件方差分解使平方损失风险不增加。

### 面试 5. 为什么置信区间不是“真参数有 95% 的频率概率位于该已知区间”？

**参考思路：**在频率模型中参数视为固定；95% 针对重复抽样区间包含参数的长期比例。观测后区间已固定。

### 面试 6. 为什么小 p 值不代表效果大？

**参考思路：**给定固定的非零效应，当样本量足够大时标准误可趋近零，检验可能拒绝极小、缺乏实际意义的效应。

### 面试 7. 为什么两组独立样本均值比较通常优先考虑 Welch t 检验？

**参考思路：**Welch 不强制相同方差，并通过估计标准误及自由度调整降低异方差时传统合并方差检验的失真风险。

### 面试 8. 卡方检验在稀疏列联表中有什么问题？

**参考思路：**小期望频数会影响渐近卡方参考分布准确性，需考虑精确检验或适当重抽样方法。

### 面试 9. 为何在挑选最佳模型后直接报告原始 p 值可能错误？

**参考思路：**模型选择依赖同一数据，会改变估计量与检验统计量的条件分布，引入选择后推断偏差。

### 面试 10. Bootstrap 对时间序列是否可以直接逐点有放回抽样？

**参考思路：**一般不能；逐点抽样破坏序列相关结构，常需要分块 Bootstrap 或其他保留依赖的方案。

### 面试 11. 为什么简单回归中的显著系数通常不能直接解释为因果效应？

**参考思路：**模型残差可能包含与解释变量相关的混杂因素；需随机分配、合理工具变量或其他可辩护的识别设计。

### 面试 12. 贝叶斯可信区间与频率置信区间何时可能相似？

**参考思路：**在大样本、正则模型和较弱先验影响等条件下，后验渐近正态可与似然估计区间近似一致，但不构成普遍保证。

## 中等难度考试题与解析

### 考试 1. IID 样本总体标准差 12、样本量 36，样本均值的标准误是多少？

**解析：**SE=σ/√n=12/6=2。

### 考试 2. 100 次独立伯努利试验，样本成功比例 0.4，估算比例标准误。

**解析：**将 p 用样本比例替代，SE≈√(0.4×0.6/100)≈0.049。

### 考试 3. 样本 1、2、3 的无偏样本方差是多少？

**解析：**均值为 2，平方离差和为 2，除以 n−1=2，得到 s²=1。

### 考试 4. 单样本检验 n=25、样本均值 105、零假设均值 100、样本标准差 10，t 统计量？

**解析：**t=(105−100)/(10/√25)=2.5，自由度为 24。

### 考试 5. 在 H0 下 X~Binomial(10,0.5)，计算 P(X≥9)。

**解析：**P(X≥9)=[C(10,9)+C(10,10)]/2¹⁰=11/1024≈0.0107。

### 考试 6. 对指数分布率参数 λ，观察到样本 1、2、3，极大似然估计是多少？

**解析：**n=3，总观测和为 6，指数率 MLE 为 n/Σxi=0.5。

### 考试 7. 20 次独立、零假设均为真且单次 α=0.05 的检验，至少一次误拒绝的概率？

**解析：**1−(1−0.05)^20≈0.642；说明多重比较需要错误率控制。

### 考试 8. 4 个 p 值为 0.001、0.020、0.049、0.200，BH 控制 q=0.05 时拒绝几个假设？

**解析：**与 i×0.05/4 阈值比较，最大满足条件的是 i=2，所以拒绝前 2 个。

### 考试 9. 回归模型的残差平方和为 20，总平方和为 100，带截距模型 R² 多少？

**解析：**R²=1−RSS/TSS=1−20/100=0.8。

### 考试 10. 2×2 表中 a=30、b=10、c=20、d=40，样本优势比是多少？

**解析：**OR=(a×d)/(b×c)=30×40/(10×20)=6。

### 考试 11. Beta(2,2) 先验，二项样本成功 8 次失败 2 次，后验均值是多少？

**解析：**后验为 Beta(10,4)，均值 10/(10+4)=5/7≈0.714。

### 考试 12. 若随机变量 Xₙ 依概率收敛到 2，Yₙ 依分布收敛到标准正态，XₙYₙ 的极限分布？

**解析：**由 Slutsky 定理，XₙYₙ 依分布收敛到 2Z，即 N(0,4)。

## 参考教材与技术资料

以下资料为学科体系及术语定义的参考，并非各作者逐条审阅的证明。

1. [Casella & Berger, Statistical Inference (2nd ed.)](https://www.cengage.com/c/statistical-inference-2e-casella-berger/9780534243128)
2. [Wasserman, All of Statistics (Springer, 2004)](https://link.springer.com/book/10.1007/978-0-387-21736-9)
3. [van der Vaart, Asymptotic Statistics (Cambridge University Press)](https://www.cambridge.org/core/books/asymptotic-statistics/A3C7DAD3F7E66A1FA60E9C8FE132EE1D)
4. [Lehmann & Romano, Testing Statistical Hypotheses (4th ed.)](https://link.springer.com/book/10.1007/978-3-030-70578-7)
5. [Efron & Tibshirani, An Introduction to the Bootstrap (CRC)](https://www.routledge.com/An-Introductionto-the-Bootstrap/Efron-Tibshirani/p/book/9780429246593)
6. [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)

## 维护与重建

- 原始词表：`data/mathematical-statistics/chapters/*.tsv`。
- 导出：`data/mathematical-statistics.tsv`、`glossaries/mathematical-statistics.md` 与 `pdf/mathematical-statistics.pdf`。
- 构建校验：`node scripts/render_mathematical_statistics.mjs --check`。
- PDF 需独立进行中文字符与跨阅读器版面检查；专业 Wiki 须另行逐条审稿。
