# 概率论 · Probability Theory

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：405 条 · 专题：16 类**

Random variables, distributions, stochastic processes and inference

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 概率空间与事件（30 条）
- 02. 计数原理与经典概率（21 条）
- 03. 条件概率、独立性与贝叶斯公式（24 条）
- 04. 随机变量与分布函数（29 条）
- 05. 常见离散概率分布（20 条）
- 06. 常见连续概率分布（27 条）
- 07. 多维随机变量与联合分布（28 条）
- 08. 数字特征与矩（29 条）
- 09. 随机变量函数与变换（20 条）
- 10. 收敛与极限定理（25 条）
- 11. 条件期望与鞅（19 条）
- 12. 随机过程（31 条）
- 13. 泊松过程与布朗运动（21 条）
- 14. 测度论概率基础（26 条）
- 15. 统计推断与贝叶斯统计（31 条）
- 16. 信息论与概率不等式（24 条）

---

## 01. 概率空间与事件

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | probability theory | 概率论 |  | 研究随机现象的数学理论 |
| 2 | random experiment | 随机试验 |  | 结果不能事先确定 |
| 3 | random phenomenon | 随机现象 |  | 具有不确定性 |
| 4 | sample point; outcome | 样本点 |  | 单次试验的一种结果 |
| 5 | sample space | 样本空间 |  | 常记为 Omega |
| 6 | elementary event | 基本事件 |  | 单个样本点构成的事件 |
| 7 | random event | 随机事件 |  | 样本空间的子集 |
| 8 | certain event; sure event | 必然事件 |  | 整个样本空间 |
| 9 | impossible event | 不可能事件 |  | 空集 |
| 10 | occurrence of an event | 事件发生 |  | 样本点属于该事件 |
| 11 | union of events | 事件的并 |  | A ∪ B |
| 12 | intersection of events | 事件的交 |  | A ∩ B |
| 13 | complement of an event | 事件的补 |  | A 的补集 |
| 14 | difference of events | 差事件 |  | A \ B |
| 15 | mutually exclusive events; disjoint events | 互斥事件 |  | 交集为空 |
| 16 | compatible events | 相容事件 |  | 交集非空 |
| 17 | complementary events | 对立事件 |  | A 与其补集 |
| 18 | event inclusion | 事件包含关系 |  | A ⊆ B |
| 19 | sequence of events | 事件序列 |  | A1, A2, ... |
| 20 | limit superior of events | 上极限事件 |  | 无限多个 A_n 发生 |
| 21 | limit inferior of events | 下极限事件 |  | 除有限个外都发生 |
| 22 | sigma-algebra; σ-algebra | 西格玛代数 |  | 对补与可数并封闭 |
| 23 | field of events; algebra of sets | 事件域 |  | 对有限集合运算封闭 |
| 24 | measurable space | 可测空间 |  | (Omega, F) |
| 25 | probability measure | 概率测度 |  | P(Omega)=1 |
| 26 | probability space | 概率空间 |  | (Omega, F, P) |
| 27 | axioms of probability | 概率公理 |  | Kolmogorov 三公理 |
| 28 | countable additivity; σ-additivity | 可列可加性 |  | 对可数个互斥事件 |
| 29 | null event; zero-probability event | 概率为零事件 |  | P(A)=0 |
| 30 | almost surely; almost certainly | 几乎必然 |  | 概率为 1 |

## 02. 计数原理与经典概率

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | classical probability model | 古典概型 |  | 有限等可能样本点 |
| 2 | equiprobability | 等可能性 |  | 基本结果概率相等 |
| 3 | permutation | 排列 |  | 顺序重要 |
| 4 | combination | 组合 |  | 顺序不重要 |
| 5 | number of permutations | 排列数 |  | P(n,k) |
| 6 | binomial coefficient; combination number | 组合数 |  | C(n,k) |
| 7 | factorial | 阶乘 |  | n! |
| 8 | addition principle | 加法原理 |  | 分类计数 |
| 9 | multiplication principle | 乘法原理 |  | 分步计数 |
| 10 | inclusion-exclusion principle | 容斥原理 |  | 计算并集大小或概率 |
| 11 | pigeonhole principle | 抽屉原理 |  | 鸽巢原理 |
| 12 | permutation with repetition | 重复排列 |  | 允许重复出现 |
| 13 | sampling without replacement | 不重复抽样 |  | 总体元素不放回 |
| 14 | sampling with replacement | 有放回抽样 |  | 总体元素放回 |
| 15 | binomial coefficient | 二项式系数 |  | C(n,k) |
| 16 | multinomial coefficient | 多项式系数 |  | n!/(n1!...nr!) |
| 17 | conditional counting | 条件计数 |  | 附加约束下计数 |
| 18 | uniform sampling | 均匀抽样 |  | 各结果机会相同 |
| 19 | geometric probability model | 几何概型 |  | 按长度、面积或体积测度 |
| 20 | Bernoulli trial | 伯努利试验 |  | 二元结果的单次试验 |
| 21 | independent repeated trials | 独立重复试验 |  | 试验相互独立 |

## 03. 条件概率、独立性与贝叶斯公式

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | conditional probability | 条件概率 |  | P(A \| B) |
| 2 | multiplication rule | 乘法公式 |  | P(A∩B)=P(A\|B)P(B) |
| 3 | law of total probability | 全概率公式 |  | 按完备事件组求和 |
| 4 | Bayes' theorem; Bayes' formula | 贝叶斯公式 |  | 由后验反推原因 |
| 5 | prior probability | 先验概率 |  | 观测前概率 |
| 6 | posterior probability | 后验概率 |  | 观测后概率 |
| 7 | likelihood | 似然 |  | 数据给定后的参数相对支持度 |
| 8 | Bayes factor | 贝叶斯因子 |  | 模型证据比 |
| 9 | prior odds | 先验赔率 |  | 观测前赔率 |
| 10 | posterior odds | 后验赔率 |  | 观测后赔率 |
| 11 | conditional independence | 条件独立 |  | 给定条件下独立 |
| 12 | independence of events | 事件独立 |  | P(A∩B)=P(A)P(B) |
| 13 | pairwise independence | 两两独立 |  | 任意两者独立 |
| 14 | mutual independence; joint independence | 相互独立 |  | 任意有限子组乘积式成立 |
| 15 | family of independent events | 独立事件族 |  | 指标集可为无限 |
| 16 | partition of the sample space | 完备事件组 |  | 两两互斥且并为全体 |
| 17 | odds | 赔率 |  | p/(1-p) |
| 18 | odds ratio | 机会比 |  | 两组赔率之比 |
| 19 | risk ratio; relative risk | 风险比 |  | 两组事件概率之比 |
| 20 | evidence | 证据 |  | 用于更新概率的信息 |
| 21 | conditional distribution | 条件分布 |  | 给定事件或变量的分布 |
| 22 | regular conditional probability | 正则条件概率 |  | 满足可测性条件的条件概率核 |
| 23 | conditional probability kernel | 条件概率核 |  | 随条件变量变化的概率测度 |
| 24 | memoryless property | 无记忆性 |  | 剩余等待与已等待无关 |

## 04. 随机变量与分布函数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | random variable | 随机变量 |  | 从样本空间到实数的可测函数 |
| 2 | discrete random variable | 离散型随机变量 |  | 取值可数 |
| 3 | continuous random variable | 连续型随机变量 |  | 通常指具有密度 |
| 4 | mixed distribution | 混合型分布 |  | 离散与连续成分并存 |
| 5 | random vector | 随机向量 |  | 多维随机变量 |
| 6 | range of a random variable | 随机变量的取值域 |  | 可能取到的值 |
| 7 | distribution | 分布 |  | 概率规律 |
| 8 | probability distribution | 概率分布 |  | 随机变量的分布律 |
| 9 | probability law | 分布律 |  | 分布的另一称呼 |
| 10 | probability mass function; PMF | 概率质量函数 |  | p(x)=P(X=x) |
| 11 | probability density function; PDF | 概率密度函数 |  | f(x)，不是点概率 |
| 12 | cumulative distribution function; CDF | 累积分布函数 |  | F(x)=P(X≤x) |
| 13 | distribution function | 分布函数 |  | 通常指 CDF |
| 14 | survival function | 生存函数 |  | S(x)=P(X>x) |
| 15 | tail distribution function | 尾分布函数 |  | P(X>x) 或 P(X≥x)，依约定 |
| 16 | quantile | 分位数 |  | 分布位置指标 |
| 17 | percentile | 百分位数 |  | 分位数按百分数表示 |
| 18 | median | 中位数 |  | 0.5 分位数 |
| 19 | mode | 众数 |  | 密度或质量函数峰值 |
| 20 | support of a distribution | 支持集 |  | 分布集中所在集合 |
| 21 | atom of a distribution | 原子 |  | 具有正概率的单点 |
| 22 | jump of a distribution function | 分布的跳跃 |  | CDF 的不连续跳跃 |
| 23 | right continuity of a CDF | 分布的右连续性 |  | 分布函数的重要性质 |
| 24 | quantile function; generalized inverse CDF | 逆分布函数 |  | Q(u)=inf{x:F(x)≥u} |
| 25 | hazard rate; hazard function | 危险率（风险率） |  | 瞬时事件发生率 |
| 26 | cumulative hazard function | 累积危险函数 |  | H(t)=-log S(t) |
| 27 | scale parameter | 尺度参数 |  | 控制分布伸缩 |
| 28 | location parameter | 位置参数 |  | 控制分布平移 |
| 29 | shape parameter | 形状参数 |  | 控制分布形状 |

## 05. 常见离散概率分布

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | degenerate distribution | 退化分布 |  | 概率集中于单点 |
| 2 | discrete uniform distribution | 离散均匀分布 |  | 有限各值等概率 |
| 3 | Bernoulli distribution | 伯努利分布 |  | Bernoulli(p) |
| 4 | binomial distribution | 二项分布 |  | Binomial(n,p) |
| 5 | multinomial distribution | 多项分布 |  | Multinomial(n,p) |
| 6 | geometric distribution | 几何分布 |  | Geom(p)，起点有两种约定 |
| 7 | negative binomial distribution | 负二项分布 |  | 达到 r 次成功的等待次数 |
| 8 | hypergeometric distribution | 超几何分布 |  | 无放回抽样成功数 |
| 9 | negative hypergeometric distribution | 负超几何分布 |  | 无放回等待成功次数 |
| 10 | Poisson distribution | 泊松分布 |  | Poisson(lambda) |
| 11 | law of small numbers; Poisson approximation | 稀有事件近似 |  | 二项分布趋近泊松分布 |
| 12 | zero-truncated Poisson distribution | 零截断泊松分布 |  | 泊松分布条件于 X>0 |
| 13 | zero-inflated model | 零膨胀模型 |  | 额外零概率质量 |
| 14 | logarithmic series distribution | 对数级数分布 |  | 离散长尾分布 |
| 15 | Skellam distribution | 斯凯拉姆分布 |  | 两个独立泊松变量之差 |
| 16 | beta-binomial distribution | 贝塔二项分布 |  | 成功率服从 Beta 分布 |
| 17 | Poisson binomial distribution | 泊松二项分布 |  | 独立但成功率不同的伯努利和 |
| 18 | categorical distribution | 分类分布 |  | 单次多类别试验 |
| 19 | Zipf distribution | 齐普夫分布 |  | 重尾离散分布 |
| 20 | parameter of a discrete distribution | 离散分布的参数 |  | n、p、lambda 等 |

## 06. 常见连续概率分布

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | continuous uniform distribution | 连续均匀分布 |  | Uniform(a,b) |
| 2 | normal distribution; Gaussian distribution | 正态分布 |  | Normal(mu,sigma²) |
| 3 | standard normal distribution | 标准正态分布 |  | Normal(0,1) |
| 4 | lognormal distribution | 对数正态分布 |  | log(X) 服从正态 |
| 5 | exponential distribution | 指数分布 |  | Exp(lambda)，率参数 |
| 6 | gamma distribution | 伽马分布 |  | Gamma(shape, rate/scale) |
| 7 | beta distribution | 贝塔分布 |  | Beta(alpha,beta) |
| 8 | chi-squared distribution | 卡方分布 |  | chi-square(k) |
| 9 | Student's t-distribution | 学生 t 分布 |  | t(k) |
| 10 | F-distribution | F 分布 |  | F(d1,d2) |
| 11 | Cauchy distribution | 柯西分布 |  | 均值不存在 |
| 12 | Laplace distribution | 拉普拉斯分布 |  | 双指数分布 |
| 13 | logistic distribution | 逻辑斯谛分布 |  | Logistic(mu,s) |
| 14 | Weibull distribution | 威布尔分布 |  | 寿命分析常用 |
| 15 | Rayleigh distribution | 瑞利分布 |  | 非负连续分布 |
| 16 | Pareto distribution | 帕累托分布 |  | 幂律尾部 |
| 17 | generalized Pareto distribution | 广义帕累托分布 |  | 极值与超阈值模型 |
| 18 | extreme value distribution | 极值分布 |  | 极大值或极小值建模 |
| 19 | Gumbel distribution | 耿贝尔分布 |  | I 型极值分布 |
| 20 | Fréchet distribution | 弗雷歇分布 |  | II 型极值分布 |
| 21 | Weibull extreme value distribution | 魏布尔型极值分布 |  | III 型极值分布 |
| 22 | inverse Gaussian distribution | 逆高斯分布 |  | Wald 分布 |
| 23 | Dirichlet distribution | 狄利克雷分布 |  | 多维概率向量上的分布 |
| 24 | multivariate normal distribution | 多元正态分布 |  | N_d(mu,Sigma) |
| 25 | Gaussian mixture distribution | 混合正态分布 |  | 多个正态加权混合 |
| 26 | truncated normal distribution | 截断正态分布 |  | 限制取值范围并归一化 |
| 27 | noncentral chi-squared distribution | 非中心卡方分布 |  | 非中心参数不为零 |

## 07. 多维随机变量与联合分布

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | joint distribution | 联合分布 |  | 多个变量共同分布 |
| 2 | joint cumulative distribution function | 联合分布函数 |  | F(x,y)=P(X≤x,Y≤y) |
| 3 | joint probability mass function | 联合概率质量函数 |  | p(x,y) |
| 4 | joint probability density function | 联合概率密度函数 |  | f(x,y) |
| 5 | marginal distribution | 边缘分布 |  | 对其他变量积分或求和 |
| 6 | marginal density | 边缘密度 |  | 例如 f_X(x) |
| 7 | conditional density | 条件密度 |  | f(y\|x) |
| 8 | independence of random variables | 变量独立性 |  | 联合分布可分解 |
| 9 | identically distributed | 同分布 |  | 边缘分布相同 |
| 10 | independent and identically distributed; i.i.d. | 独立同分布 |  | 独立且同分布 |
| 11 | covariance | 协方差 |  | Cov(X,Y) |
| 12 | covariance matrix | 协方差矩阵 |  | Sigma |
| 13 | correlation coefficient | 相关系数 |  | rho(X,Y) |
| 14 | Pearson correlation coefficient | 皮尔逊相关系数 |  | 线性相关 |
| 15 | Spearman rank correlation coefficient | 斯皮尔曼等级相关系数 |  | 秩相关 |
| 16 | Kendall's tau | 肯德尔等级相关系数 |  | 一致与不一致对 |
| 17 | uncorrelated | 不相关 |  | Cov(X,Y)=0 |
| 18 | positive correlation | 正相关 |  | 相关系数大于 0 |
| 19 | negative correlation | 负相关 |  | 相关系数小于 0 |
| 20 | zero covariance | 协方差为零 |  | 一般不推出独立 |
| 21 | conditional covariance | 条件协方差 |  | Cov(X,Y\|Z) |
| 22 | correlation matrix | 相关矩阵 |  | 标准化的协方差矩阵 |
| 23 | dependence structure | 相依结构 |  | 变量之间的统计依赖 |
| 24 | coupling | 耦合 |  | 在同一概率空间构造指定边缘分布 |
| 25 | copula | 连接函数 |  | 描述边缘分布之间的依赖 |
| 26 | Sklar's theorem | 斯克拉定理 |  | 联合分布可由边缘分布与 copula 表示 |
| 27 | exchangeability | 交换性 |  | 置换后联合分布不变 |
| 28 | symmetry | 对称性 |  | 分布在特定变换下不变 |

## 08. 数字特征与矩

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | expectation; expected value | 数学期望 |  | E[X] |
| 2 | mean | 均值 |  | 常指 E[X] |
| 3 | variance | 方差 |  | Var(X) |
| 4 | standard deviation | 标准差 |  | SD(X) |
| 5 | raw moment | 原点矩 |  | E[X^k] |
| 6 | central moment | 中心矩 |  | E[(X-E[X])^k] |
| 7 | second moment | 二阶矩 |  | E[X²] |
| 8 | absolute moment | 绝对矩 |  | E[\|X\|^k] |
| 9 | skewness | 偏度 |  | 标准化三阶中心矩 |
| 10 | kurtosis | 峰度 |  | 标准化四阶中心矩 |
| 11 | excess kurtosis | 超额峰度 |  | 峰度减 3 |
| 12 | coefficient of variation | 变异系数 |  | SD(X)/E[X]，均值非零 |
| 13 | moment-generating function; MGF | 矩母函数 |  | M_X(t)=E[e^(tX)] |
| 14 | characteristic function | 特征函数 |  | phi_X(t)=E[e^(itX)] |
| 15 | probability-generating function; PGF | 概率母函数 |  | G_X(s)=E[s^X] |
| 16 | cumulant | 累积量 |  | 对数矩母函数的导数 |
| 17 | cumulant-generating function; CGF | 累积量母函数 |  | K_X(t)=log M_X(t) |
| 18 | Laplace transform | 拉普拉斯变换 |  | E[e^(-sX)]，常用于非负变量 |
| 19 | Fourier transform | 傅里叶变换 |  | 与特征函数密切相关 |
| 20 | linearity of expectation | 期望的线性性 |  | E[aX+bY]=aE[X]+bE[Y] |
| 21 | additivity of variance | 方差的可加性 |  | 独立时方差可相加 |
| 22 | law of total expectation | 全期望公式 |  | E[X]=E[E[X\|Y]] |
| 23 | law of total variance | 全方差公式 |  | Var(X)=E[Var(X\|Y)]+Var(E[X\|Y]) |
| 24 | Jensen's inequality | 詹森不等式 |  | 凸函数与期望 |
| 25 | Cauchy-Schwarz inequality | 柯西-施瓦茨不等式 |  | 随机变量内积不等式 |
| 26 | Hölder's inequality | 霍尔德不等式 |  | L^p 范数不等式 |
| 27 | Minkowski's inequality | 闵可夫斯基不等式 |  | L^p 三角不等式 |
| 28 | tail expectation | 尾部期望 |  | 分布尾部的期望量 |
| 29 | truncated expectation | 截尾期望 |  | 截断变量后的期望 |

## 09. 随机变量函数与变换

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | conditional expectation | 条件期望 |  | E[X\|Y] 或 E[X\|G] |
| 2 | conditional variance | 条件方差 |  | Var(X\|Y) |
| 3 | conditional moment | 条件矩 |  | E[X^k\|Y] |
| 4 | tower property | 条件期望的塔式性质 |  | E[E[X\|G]\|H]=E[X\|H]，H⊆G |
| 5 | linearity of conditional expectation | 条件期望的线性性 |  | 按条件线性组合 |
| 6 | measurability of conditional expectation | 条件期望的可测性 |  | 相对于给定信息集 |
| 7 | conditional probability as expectation | 条件概率的期望表示 |  | P(A\|G)=E[1_A\|G] |
| 8 | transformation of random variables | 变量变换 |  | Y=g(X) |
| 9 | monotone transformation | 单调变换 |  | 利用逆函数求分布 |
| 10 | Jacobian determinant | 雅可比行列式 |  | 多元变换中的密度因子 |
| 11 | convolution | 卷积 |  | 独立随机变量和的分布 |
| 12 | distribution of a sum | 和的分布 |  | X+Y 的概率分布 |
| 13 | distribution of a product | 积的分布 |  | XY 的概率分布 |
| 14 | distribution of a ratio | 商的分布 |  | X/Y 的概率分布 |
| 15 | order statistic | 次序统计量 |  | 样本排序后的随机变量 |
| 16 | sample maximum | 最大次序统计量 |  | X_(n) |
| 17 | sample minimum | 最小次序统计量 |  | X_(1) |
| 18 | sample range | 样本极差 |  | max-min |
| 19 | maximum of random variables | 随机变量的最大值 |  | max(X,Y) |
| 20 | minimum of random variables | 随机变量的最小值 |  | min(X,Y) |

## 10. 收敛与极限定理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | law of large numbers; LLN | 大数定律 |  | 样本平均趋于期望 |
| 2 | weak law of large numbers; WLLN | 弱大数定律 |  | 依概率收敛 |
| 3 | strong law of large numbers; SLLN | 强大数定律 |  | 几乎处处收敛 |
| 4 | central limit theorem; CLT | 中心极限定理 |  | 标准化和趋于正态 |
| 5 | Lindeberg condition | 林德伯格条件 |  | 三角阵 CLT 条件之一 |
| 6 | Lyapunov condition | 李雅普诺夫条件 |  | 三角阵 CLT 的充分条件 |
| 7 | Lévy's continuity theorem | 列维连续性定理 |  | 特征函数与弱收敛 |
| 8 | Slutsky's theorem | 斯卢茨基定理 |  | 收敛变量的运算规则 |
| 9 | continuous mapping theorem | 连续映射定理 |  | 函数变换保持适当收敛 |
| 10 | convergence in probability | 依概率收敛 |  | X_n→P X |
| 11 | almost sure convergence | 几乎处处收敛 |  | X_n→a.s. X |
| 12 | convergence in distribution; weak convergence | 依分布收敛 |  | X_n→d X |
| 13 | mean-square convergence | 均方收敛 |  | L² 收敛 |
| 14 | convergence in L^p | L^p 收敛 |  | E[\|X_n-X\|^p]→0 |
| 15 | uniform integrability | 一致可积 |  | 控制尾部期望 |
| 16 | tightness | 紧性 |  | 概率质量不向无穷逸散 |
| 17 | relative compactness | 相对紧性 |  | 适用弱收敛拓扑 |
| 18 | probability limit; plim | 概率极限 |  | 依概率收敛的极限 |
| 19 | ergodic theorem | 遍历定理 |  | 时间平均与总体平均关系 |
| 20 | Borel-Cantelli lemmas | 波莱尔-康托利引理 |  | 无穷多次事件发生 |
| 21 | zero-one law | 零一律 |  | 某些尾事件概率为 0 或 1 |
| 22 | Kolmogorov's zero-one law | 柯尔莫哥洛夫零一律 |  | 独立序列尾事件 |
| 23 | Hewitt-Savage zero-one law | 休伊特-萨维奇零一律 |  | i.i.d. 交换事件 |
| 24 | large deviation principle; LDP | 大偏差原理 |  | 稀有偏离的指数尺度 |
| 25 | local central limit theorem | 局部中心极限定理 |  | 局部概率的正态近似 |

## 11. 条件期望与鞅

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Markov's inequality | 马尔可夫不等式 |  | 非负变量的尾概率上界 |
| 2 | Chebyshev's inequality | 切比雪夫不等式 |  | 用方差控制尾概率 |
| 3 | Cantelli's inequality | 坎泰利不等式 |  | 单侧切比雪夫界 |
| 4 | Boole's inequality; union bound | 博尔不等式 |  | P(并集)≤各概率之和 |
| 5 | Bonferroni inequalities | 邦费罗尼不等式 |  | 容斥截断给上下界 |
| 6 | Hoeffding's inequality | 霍夫丁不等式 |  | 有界独立和集中界 |
| 7 | Bernstein's inequality | 伯恩斯坦不等式 |  | 考虑方差与单项上界 |
| 8 | Chernoff bound | 切尔诺夫界 |  | 指数矩求尾概率界 |
| 9 | Azuma-Hoeffding inequality | 阿祖马-霍夫丁不等式 |  | 有界差鞅集中界 |
| 10 | McDiarmid's inequality | 麦克迪尔米德不等式 |  | 有界差函数集中界 |
| 11 | sub-Gaussian random variable | 次高斯随机变量 |  | 尾部不重于高斯量级 |
| 12 | sub-exponential random variable | 次指数随机变量 |  | 指数型尾界 |
| 13 | concentration inequality | 集中不等式 |  | 偏离均值的概率上界 |
| 14 | concentration of measure | 浓缩现象 |  | 高维概率集中 |
| 15 | empirical distribution function; EDF | 经验分布函数 |  | F_n(x) |
| 16 | Glivenko-Cantelli theorem | 格利文科-坎泰利定理 |  | 经验分布一致逼近 |
| 17 | Dvoretzky-Kiefer-Wolfowitz inequality | DKW 不等式 |  | 经验 CDF 偏差界 |
| 18 | covariance inequality | 协方差不等式 |  | 控制协方差绝对值 |
| 19 | Paley-Zygmund inequality | 帕利-齐格蒙德不等式 |  | 非负变量非小概率下界 |

## 12. 随机过程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | stochastic process | 随机过程 |  | 按时间或指标变化的随机变量族 |
| 2 | index set | 指标集 |  | 常表示时间集合 |
| 3 | state space | 状态空间 |  | 过程可处的状态集合 |
| 4 | sample path; realization | 样本路径 |  | 一次实现的时间轨迹 |
| 5 | finite-dimensional distribution | 有限维分布 |  | 多个时刻的联合分布 |
| 6 | stationarity of a stochastic process | 随机过程的平稳性 |  | 平移时间后的分布不变 |
| 7 | strict stationarity | 严平稳 |  | 所有有限维分布平稳 |
| 8 | weak stationarity; covariance stationarity | 宽平稳 |  | 均值与协方差满足平稳条件 |
| 9 | Markov property | 马尔可夫性质 |  | 给定现在，未来与过去条件独立 |
| 10 | Markov chain | 马尔可夫链 |  | 满足马尔可夫性质的离散状态过程 |
| 11 | discrete-time Markov chain; DTMC | 离散时间马尔可夫链 |  | 离散时间参数 |
| 12 | continuous-time Markov chain; CTMC | 连续时间马尔可夫链 |  | 连续时间参数 |
| 13 | transition probability | 转移概率 |  | P(X_(n+1)=j \| X_n=i) |
| 14 | transition matrix | 转移矩阵 |  | P=(p_ij) |
| 15 | one-step transition probability | 一步转移概率 |  | p_ij |
| 16 | n-step transition probability | 多步转移概率 |  | p_ij^(n) |
| 17 | Chapman-Kolmogorov equation | 查普曼-柯尔莫哥洛夫方程 |  | 多步转移可分解 |
| 18 | stationary distribution | 平稳分布 |  | pi P=pi |
| 19 | invariant distribution | 不变分布 |  | 转移后分布不变 |
| 20 | reducible Markov chain | 可约链 |  | 状态空间可分解 |
| 21 | irreducible Markov chain | 不可约链 |  | 状态之间可互达 |
| 22 | recurrent state | 常返状态 |  | 最终返回概率为 1 |
| 23 | transient state | 暂留状态 |  | 返回概率小于 1 |
| 24 | period | 周期 |  | 返回步数的最大公约数 |
| 25 | aperiodicity | 非周期性 |  | 周期为 1 |
| 26 | absorbing state | 吸收状态 |  | 进入后不会离开 |
| 27 | absorbing Markov chain | 吸收链 |  | 包含吸收状态的链 |
| 28 | ergodic Markov chain | 遍历马尔可夫链 |  | 依约定需不可约等条件 |
| 29 | detailed balance | 细致平衡 |  | pi_i p_ij=pi_j p_ji |
| 30 | reversible Markov chain | 可逆马尔可夫链 |  | 时间反演分布不变 |
| 31 | mixing time | 混合时间 |  | 接近平稳分布所需时间 |

## 13. 泊松过程与布朗运动

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | counting process | 计数过程 |  | 随时间统计事件次数 |
| 2 | Poisson process | 泊松过程 |  | 独立平稳增量计数过程 |
| 3 | homogeneous Poisson process | 齐次泊松过程 |  | 强度为常数 |
| 4 | nonhomogeneous Poisson process | 非齐次泊松过程 |  | 强度随时间变化 |
| 5 | intensity function | 强度函数 |  | lambda(t) |
| 6 | arrival time | 到达时刻 |  | 第 n 次事件发生时间 |
| 7 | interarrival time | 到达间隔 |  | 相邻事件的等待时间 |
| 8 | waiting time | 等待时间 |  | 直到事件发生的时间 |
| 9 | independent increments | 独立增量 |  | 不交时间段增量独立 |
| 10 | stationary increments | 平稳增量 |  | 增量分布只依赖时间长度 |
| 11 | renewal process | 更新过程 |  | 相邻间隔 i.i.d. 的计数过程 |
| 12 | renewal function | 更新函数 |  | m(t)=E[N(t)] |
| 13 | renewal reward process | 更新报酬过程 |  | 更新周期对应报酬 |
| 14 | compound Poisson process | 复合泊松过程 |  | 泊松次数的随机和 |
| 15 | Markov-modulated Poisson process; MMPP | 马尔可夫调制泊松过程 |  | 速率受马尔可夫链调制 |
| 16 | queueing theory | 排队论 |  | 等待与服务系统的概率模型 |
| 17 | arrival rate | 到达率 |  | 单位时间平均到达数 |
| 18 | service rate | 服务率 |  | 单位时间平均服务数 |
| 19 | utilization | 利用率 |  | 常记 rho |
| 20 | Little's law | 利特尔定律 |  | L=lambda W |
| 21 | M/M/1 queue | M/M/1 排队模型 |  | 泊松到达、指数服务、单服务台 |

## 14. 测度论概率基础

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | filtration | 信息流 |  | 递增的 sigma 代数族 |
| 2 | adapted process | 适应过程 |  | 每个时刻可由当前信息确定 |
| 3 | predictable process | 可预测过程 |  | 在适当信息结构下可预测 |
| 4 | martingale | 鞅 |  | 条件期望等于当前值 |
| 5 | supermartingale | 上鞅 |  | 条件期望不大于当前值 |
| 6 | submartingale | 下鞅 |  | 条件期望不小于当前值 |
| 7 | martingale difference sequence | 鞅差序列 |  | 条件均值为 0 |
| 8 | stopping time | 停时 |  | 是否停止由当前信息决定 |
| 9 | optional stopping theorem | 可选停止定理 |  | 满足条件时停时保持期望 |
| 10 | Doob's maximal inequality | 杜布最大不等式 |  | 鞅最大值尾概率界 |
| 11 | martingale convergence theorem | 鞅收敛定理 |  | 适当条件下鞅收敛 |
| 12 | Brownian motion; Wiener process | 布朗运动 |  | 连续路径、高斯独立增量 |
| 13 | standard Brownian motion | 标准布朗运动 |  | B(0)=0, Var(B(t))=t |
| 14 | Brownian bridge | 布朗桥 |  | 端点受约束的高斯过程 |
| 15 | Gaussian process | 高斯过程 |  | 有限维分布均为多元正态 |
| 16 | Wiener process | 维纳过程 |  | 布朗运动的别称 |
| 17 | stochastic integral | 随机积分 |  | 对随机过程积分 |
| 18 | Itô integral | 伊藤积分 |  | 典型随机积分 |
| 19 | Itô's lemma | 伊藤引理 |  | 随机微积分链式法则 |
| 20 | stochastic differential equation; SDE | 随机微分方程 |  | 含随机驱动项的动力方程 |
| 21 | quadratic variation | 二次变差 |  | 连续鞅重要路径量 |
| 22 | strong solution | 强解 |  | 给定噪声下构造的解 |
| 23 | weak solution | 弱解 |  | 可连同概率空间一起构造 |
| 24 | first passage time; hitting time | 首达时刻 |  | 首次到达目标集合时间 |
| 25 | drift term | 漂移项 |  | 随机微分方程的确定性趋势 |
| 26 | diffusion term | 扩散项 |  | 随机微分方程的噪声强度 |

## 15. 统计推断与贝叶斯统计

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | measure | 测度 |  | 集合上的非负可列可加函数 |
| 2 | finite measure | 有限测度 |  | 全空间测度有限 |
| 3 | sigma-finite measure | 西格玛有限测度 |  | 可数个有限测度集覆盖 |
| 4 | Lebesgue measure | 勒贝格测度 |  | 长度、面积的抽象推广 |
| 5 | Borel set | 博雷尔集合 |  | 由开集生成的 sigma 代数中的集合 |
| 6 | Borel sigma-algebra | 博雷尔西格玛代数 |  | B(R) |
| 7 | measurable function | 可测函数 |  | 逆像满足可测性 |
| 8 | measurable map | 可测映射 |  | 保持可测集合的逆像 |
| 9 | pushforward measure | 推前测度 |  | 由可测映射诱导的分布 |
| 10 | product measure | 乘积测度 |  | 多空间上的联合测度 |
| 11 | Lebesgue integral | 勒贝格积分 |  | 概率期望的积分基础 |
| 12 | integrable function | 可积函数 |  | 绝对值的积分有限 |
| 13 | almost everywhere; a.e. | 几乎处处 |  | 测度为零的集合之外 |
| 14 | monotone convergence theorem; MCT | 单调收敛定理 |  | 非负单调序列交换极限积分 |
| 15 | dominated convergence theorem; DCT | 控制收敛定理 |  | 可积控制函数下交换极限积分 |
| 16 | Fatou's lemma | 法图引理 |  | 下极限与积分的不等式 |
| 17 | Fubini's theorem | 富比尼定理 |  | 可积函数交换积分顺序 |
| 18 | Tonelli's theorem | 托内利定理 |  | 非负函数交换积分顺序 |
| 19 | absolute continuity | 绝对连续 |  | P 对 Q 绝对连续 |
| 20 | mutually singular measures | 相互奇异 |  | 支持在不交的可测部分 |
| 21 | Radon-Nikodym derivative | 拉东-尼科迪姆导数 |  | dP/dQ |
| 22 | density with respect to a measure | 密度（测度意义） |  | 相对于基准测度的导数 |
| 23 | probability kernel | 概率核 |  | 从状态到概率测度的可测映射 |
| 24 | outer measure | 外测度 |  | 通过覆盖定义的外部大小 |
| 25 | complete measure | 完备测度 |  | 零测集的子集也可测 |
| 26 | tail sigma-algebra | 尾西格玛代数 |  | 无穷远处的信息 |
| 27 | generated sigma-algebra | 生成西格玛代数 |  | 由集合族生成的最小 sigma 代数 |
| 28 | separability | 可分性 |  | 可数稠密子集性质 |
| 29 | Prokhorov's theorem | 普罗霍罗夫定理 |  | 紧性与弱相对紧性条件 |
| 30 | convergence in measure | 测度收敛 |  | 依测度意义的收敛 |
| 31 | weak convergence of measures | 弱收敛（测度） |  | 有界连续函数积分收敛 |

## 16. 信息论与概率不等式

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Monte Carlo method | 蒙特卡罗方法 |  | 用随机采样近似计算 |
| 2 | Monte Carlo integration | 蒙特卡罗积分 |  | 抽样均值逼近积分 |
| 3 | inverse transform sampling | 逆变换采样 |  | 由均匀变量和分位数函数抽样 |
| 4 | rejection sampling | 拒绝采样 |  | 按接受概率筛选样本 |
| 5 | importance sampling | 重要性采样 |  | 用加权改变采样分布 |
| 6 | stratified sampling | 分层抽样 |  | 总体分层提高效率 |
| 7 | control variates | 控制变量法 |  | 利用已知期望降低方差 |
| 8 | antithetic variates | 对偶变量法 |  | 构造负相关样本降方差 |
| 9 | Markov chain Monte Carlo; MCMC | 马尔可夫链蒙特卡罗 |  | 用马尔可夫链抽样 |
| 10 | Gibbs sampling | 吉布斯采样 |  | 轮流从条件分布抽样 |
| 11 | Metropolis-Hastings algorithm | 梅特罗波利斯-黑斯廷斯算法 |  | 按接受率设计平稳分布 |
| 12 | prior distribution | 先验分布 |  | 模型参数的观测前分布 |
| 13 | posterior distribution | 后验分布 |  | 给定数据后的参数分布 |
| 14 | posterior predictive distribution | 后验预测分布 |  | 平均参数不确定性的预测 |
| 15 | conjugate prior | 共轭先验 |  | 后验与先验属于同一分布族 |
| 16 | likelihood function | 似然函数 |  | 参数的函数，不是参数概率分布 |
| 17 | sample | 样本 |  | 观测数据集合 |
| 18 | sample mean | 样本均值 |  | X_bar |
| 19 | sample variance | 样本方差 |  | 常用 n-1 校正 |
| 20 | standard error; SE | 标准误 |  | 统计量抽样分布的标准差 |
| 21 | estimator | 估计量 |  | 基于样本的随机函数 |
| 22 | unbiased estimator | 无偏估计量 |  | 估计量期望等于参数 |
| 23 | confidence interval | 置信区间 |  | 重复抽样覆盖率意义 |
| 24 | credible interval | 可信区间 |  | 贝叶斯后验概率意义 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/probability-theory.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
