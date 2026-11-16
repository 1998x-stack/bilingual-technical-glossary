# 微积分 · Calculus

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：301 条 · 专题：14 类**

覆盖极限、连续性、导数、积分、无穷级数、多元微积分、向量分析、常微分方程与数值近似。

> 编纂说明：优先采用高等数学教材中常见的规范译名；专业术语可能因教材、地区或数学分支存在不同译法。
> 定理条目仅概述结论或用途；阅读原始定理时，应核对完整假设与适用条件。

## 专题目录

- 01. 函数、集合与基础语言（24 条）
- 02. 极限与无穷小（22 条）
- 03. 连续性与函数性质（16 条）
- 04. 导数与微分（26 条）
- 05. 导数的应用（20 条）
- 06. 不定积分与原函数（20 条）
- 07. 定积分与微积分基本定理（20 条）
- 08. 积分应用与广义积分（20 条）
- 09. 数列与无穷级数（30 条）
- 10. 多元函数与偏导数（22 条）
- 11. 多元极值与重积分（20 条）
- 12. 曲线、曲面与向量分析（25 条）
- 13. 常微分方程初步（18 条）
- 14. 数值近似与计算实践（18 条）

---

## 01. 函数、集合与基础语言

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Function | 函数 |  | 将定义域中的每个输入对应到唯一输出的映射。 |
| 2 | Domain | 定义域 |  | 函数允许输入的全部自变量取值组成的集合。 |
| 3 | Codomain | 陪域 |  | 定义函数时指定的目标集合，不必等于实际值域。 |
| 4 | Range | 值域 |  | 函数在定义域上实际取得的输出集合。 |
| 5 | Independent Variable | 自变量 |  | 作为函数输入的变量。 |
| 6 | Dependent Variable | 因变量 |  | 随自变量变化而确定的变量。 |
| 7 | Real-valued Function | 实值函数 |  | 取值属于实数集合的函数。 |
| 8 | Composite Function | 复合函数 |  | 由一个函数的输出作为另一函数输入所形成的函数。 |
| 9 | Inverse Function | 反函数 |  | 在可逆条件下交换输入和输出得到的函数。 |
| 10 | Piecewise Function | 分段函数 |  | 在定义域不同部分使用不同表达式定义的函数。 |
| 11 | Even Function | 偶函数 |  | 满足 f(-x)=f(x) 的函数，图像关于纵轴对称。 |
| 12 | Odd Function | 奇函数 |  | 满足 f(-x)=-f(x) 的函数，图像关于原点对称。 |
| 13 | Periodic Function | 周期函数 |  | 存在正周期 T 使 f(x+T)=f(x) 的函数。 |
| 14 | Monotonic Function | 单调函数 |  | 在指定区间上保持非减或非增的函数。 |
| 15 | Bounded Function | 有界函数 |  | 函数值能被某两个常数从上下界住的函数。 |
| 16 | Elementary Function | 初等函数 |  | 由基本初等函数经过有限次四则运算和复合形成的函数。 |
| 17 | Exponential Function | 指数函数 |  | 自变量出现在指数位置的函数，常见形式为 a^x。 |
| 18 | Logarithmic Function | 对数函数 |  | 指数函数在适当定义域上的反函数。 |
| 19 | Trigonometric Function | 三角函数 |  | 正弦、余弦、正切等与角度相关的函数。 |
| 20 | Parametric Equation | 参数方程 |  | 用一个或多个参数表示曲线上的坐标。 |
| 21 | Polar Coordinates | 极坐标 |  | 通过到原点的距离和方向角描述平面点的坐标。 |
| 22 | Interval | 区间 |  | 实数轴上由端点或无穷界确定的连续数集。 |
| 23 | Neighborhood | 邻域 |  | 包含给定点附近一定范围的点集。 |
| 24 | Absolute Value | 绝对值 |  | 实数到原点的距离，记作绝对值符号包围的 x。 |

## 02. 极限与无穷小

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Limit | 极限 |  | 当自变量趋近某值或无穷远时函数值趋向的确定值。 |
| 2 | Finite Limit | 有限极限 |  | 极限为某个有限实数的情况。 |
| 3 | Infinite Limit | 无穷极限 |  | 函数值的大小在指定趋近过程中无界增长的情况。 |
| 4 | Limit at Infinity | 无穷远处的极限 |  | 自变量趋向正无穷或负无穷时的函数极限。 |
| 5 | One-sided Limit | 单侧极限 |  | 从指定一侧趋近某点时的函数极限。 |
| 6 | Left-hand Limit | 左极限 |  | 自变量从小于目标点的一侧趋近时的极限。 |
| 7 | Right-hand Limit | 右极限 |  | 自变量从大于目标点的一侧趋近时的极限。 |
| 8 | Two-sided Limit | 双侧极限 |  | 自变量从左右两侧趋近同一点时的共同极限。 |
| 9 | Epsilon-Delta Definition | ε-δ 定义 |  | 用任意精度 ε 与相应邻域宽度 δ 严格刻画函数极限。 |
| 10 | Sequential Criterion for Limits | 极限的序列判别法 |  | 利用趋向目标点的任意序列验证函数极限。 |
| 11 | Squeeze Theorem | 夹逼定理 |  | 由两侧函数极限相同推出被夹函数的极限。 |
| 12 | Limit Laws | 极限运算法则 |  | 在条件成立时对和、差、积、商等进行极限运算的规则。 |
| 13 | Indeterminate Form | 未定式 |  | 不能仅由各部分极限直接确定整体极限的表达式类型。 |
| 14 | Infinitesimal | 无穷小量 |  | 在指定过程中极限为零的变量或函数。 |
| 15 | Infinitely Large Quantity | 无穷大量 |  | 在指定过程中绝对值趋于无穷的变量或函数。 |
| 16 | Equivalent Infinitesimals | 等价无穷小 |  | 两个无穷小的比值趋于 1。 |
| 17 | Higher-order Infinitesimal | 高阶无穷小 |  | 相对于另一无穷小其比值趋于 0 的量。 |
| 18 | Asymptotic Equivalence | 渐近等价 |  | 两个非零量的比值在指定过程中趋于 1。 |
| 19 | Little-o Notation | 小 o 记号 |  | 表示某量相对于参照量可忽略的渐近阶。 |
| 20 | Big-O Notation | 大 O 记号 |  | 表示某量的大小在渐近意义下受参照量常数倍控制。 |
| 21 | L'Hopital's Rule | 洛必达法则 |  | 在适当条件下用导数之比计算特定未定式的极限。 |
| 22 | Asymptote | 渐近线 |  | 曲线在趋近某个方向时与之距离趋于零的直线。 |

## 03. 连续性与函数性质

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Continuity | 连续性 |  | 函数在一点的极限存在且等于该点的函数值。 |
| 2 | Continuity at a Point | 一点处连续 |  | 函数在指定点满足极限与函数值相等。 |
| 3 | Continuity on an Interval | 区间连续 |  | 函数在区间内部各点连续并满足端点相应单侧连续条件。 |
| 4 | Left Continuity | 左连续 |  | 一点的左极限等于该点函数值。 |
| 5 | Right Continuity | 右连续 |  | 一点的右极限等于该点函数值。 |
| 6 | Discontinuity | 间断点 |  | 函数不满足连续条件的位置。 |
| 7 | Removable Discontinuity | 可去间断点 |  | 函数极限存在但函数值缺失或不等于该极限。 |
| 8 | Jump Discontinuity | 跳跃间断点 |  | 两侧有限极限存在但不相等的间断点。 |
| 9 | Infinite Discontinuity | 无穷间断点 |  | 至少一侧函数值趋向无穷的间断点。 |
| 10 | Intermediate Value Theorem | 介值定理 | IVT | 连续函数在区间两端函数值之间取遍所有中间值。 |
| 11 | Extreme Value Theorem | 最值定理 | EVT | 连续函数在闭区间上一定能取得最大值和最小值。 |
| 12 | Uniform Continuity | 一致连续性 |  | 选取 δ 时可不依赖区间内具体位置的连续性。 |
| 13 | Heine-Cantor Theorem | 海涅-康托定理 |  | 紧集上的连续函数必一致连续。 |
| 14 | Bolzano's Theorem | 零点存在定理 |  | 连续函数在区间两端异号时区间内部至少有一个零点。 |
| 15 | Lipschitz Continuity | 利普希茨连续性 |  | 函数值差被输入距离的固定常数倍控制。 |
| 16 | Oscillation of a Function | 函数振幅 |  | 函数在一个集合上上确界与下确界之差。 |

## 04. 导数与微分

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Derivative | 导数 |  | 函数增量与自变量增量之比的极限，反映瞬时变化率。 |
| 2 | Differentiability | 可导性 |  | 函数在指定点存在有限导数的性质。 |
| 3 | Difference Quotient | 差商 |  | 函数增量除以自变量增量所得的比值。 |
| 4 | Derivative at a Point | 一点处的导数 |  | 函数在指定点的瞬时变化率。 |
| 5 | Derivative Function | 导函数 |  | 将每个可导点映射到其导数值的函数。 |
| 6 | Left Derivative | 左导数 |  | 从左侧增量计算得到的导数极限。 |
| 7 | Right Derivative | 右导数 |  | 从右侧增量计算得到的导数极限。 |
| 8 | Higher-order Derivative | 高阶导数 |  | 对导函数连续求导得到的导数。 |
| 9 | Second Derivative | 二阶导数 |  | 对一阶导函数再次求导的结果。 |
| 10 | Differential | 微分 |  | 在线性近似中与自变量增量对应的一阶线性变化量。 |
| 11 | Differential Quotient | 微商 |  | 导数的传统称呼，通常表示微分之比。 |
| 12 | Tangent Line | 切线 |  | 在可导点附近与曲线具有相同一阶变化率的直线。 |
| 13 | Normal Line | 法线 |  | 在切点处垂直于切线的直线。 |
| 14 | Chain Rule | 链式法则 |  | 复合函数求导时将外层与内层导数相乘的规则。 |
| 15 | Product Rule | 乘积求导法则 |  | 两个可导函数相乘时的求导规则。 |
| 16 | Quotient Rule | 商求导法则 |  | 两个可导函数相除时的求导规则。 |
| 17 | Power Rule | 幂函数求导法则 |  | 对 x 的实数幂在允许范围内求导的规则。 |
| 18 | Implicit Differentiation | 隐函数求导 |  | 对隐式方程两边求导并解出所需导数的方法。 |
| 19 | Logarithmic Differentiation | 对数求导法 |  | 先取对数再求导以简化乘积、商或变幂函数的方法。 |
| 20 | Parametric Differentiation | 参数方程求导 |  | 用参数导数之比求曲线斜率的方法。 |
| 21 | Derivative of Inverse Function | 反函数求导法则 |  | 在适当条件下反函数导数为原函数导数的倒数。 |
| 22 | Differential Approximation | 微分近似 |  | 利用函数在某点的线性部分估计附近函数值。 |
| 23 | Linearization | 线性化 |  | 用切线对应的一次函数近似原函数。 |
| 24 | Taylor's Theorem | 泰勒定理 |  | 用多项式与余项表示足够光滑函数在某点附近的变化。 |
| 25 | Taylor Polynomial | 泰勒多项式 |  | 以某点各阶导数为系数构造的局部近似多项式。 |
| 26 | Maclaurin Polynomial | 麦克劳林多项式 |  | 以零点为展开中心的泰勒多项式。 |

## 05. 导数的应用

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Critical Point | 临界点 |  | 定义域内导数为零或不存在的候选极值点。 |
| 2 | Stationary Point | 驻点 |  | 函数导数为零的点。 |
| 3 | Local Maximum | 局部最大值 |  | 函数值在某点邻域内不小于邻近函数值。 |
| 4 | Local Minimum | 局部最小值 |  | 函数值在某点邻域内不大于邻近函数值。 |
| 5 | Global Maximum | 全局最大值 |  | 在整个指定定义域上取得的最大函数值。 |
| 6 | Global Minimum | 全局最小值 |  | 在整个指定定义域上取得的最小函数值。 |
| 7 | First Derivative Test | 一阶导数判别法 |  | 用导数符号变化判断局部极值的方法。 |
| 8 | Second Derivative Test | 二阶导数判别法 |  | 在驻点处依据二阶导数符号判断极值的方法。 |
| 9 | Mean Value Theorem | 拉格朗日中值定理 | MVT | 在适当条件下某点导数等于区间平均变化率。 |
| 10 | Rolle's Theorem | 罗尔定理 |  | 两端函数值相等时区间内部至少存在零导数点。 |
| 11 | Cauchy's Mean Value Theorem | 柯西中值定理 |  | 将中值定理推广到两个函数的变化量之比。 |
| 12 | Increasing Function | 递增函数 |  | 自变量增大时函数值不减的函数。 |
| 13 | Decreasing Function | 递减函数 |  | 自变量增大时函数值不增的函数。 |
| 14 | Concavity | 凹凸性 |  | 描述函数图像向上或向下弯曲的性质。 |
| 15 | Concave Up | 凹向上 |  | 在适当光滑条件下二阶导数非负的形状。 |
| 16 | Concave Down | 凹向下 |  | 在适当光滑条件下二阶导数非正的形状。 |
| 17 | Inflection Point | 拐点 |  | 曲线凹凸性发生变化的点。 |
| 18 | Optimization Problem | 最优化问题 |  | 在约束条件下寻找目标函数极大或极小值的问题。 |
| 19 | Related Rates | 相关变化率 |  | 对相关变量的关系式关于时间求导得到变化速率关系。 |
| 20 | Newton's Method | 牛顿迭代法 |  | 利用切线构造近似求解非线性方程根的迭代方法。 |

## 06. 不定积分与原函数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Antiderivative | 原函数 |  | 求导后得到给定函数的函数。 |
| 2 | Indefinite Integral | 不定积分 |  | 给定函数全体原函数组成的表达式。 |
| 3 | Constant of Integration | 积分常数 |  | 不定积分中表示原函数间常数差的符号。 |
| 4 | Integrand | 被积函数 |  | 积分号下需要进行积分运算的函数。 |
| 5 | Variable of Integration | 积分变量 |  | 积分表达式中作为累积变量的符号。 |
| 6 | Differential Element | 微分元 |  | 积分表达式中表示积分变量微分的部分。 |
| 7 | Linearity of Integration | 积分的线性性 |  | 常数倍与有限和可按线性规则移入或移出积分号。 |
| 8 | Substitution Rule | 换元积分法 |  | 通过变量替换将积分转化为较易处理形式的方法。 |
| 9 | Integration by Parts | 分部积分法 |  | 由乘积求导法则推导出的积分变换公式。 |
| 10 | Tabular Integration | 表格积分法 |  | 以表格组织重复分部积分的计算技巧。 |
| 11 | Partial Fraction Decomposition | 部分分式分解 |  | 将有理函数拆解为较简单分式和的方法。 |
| 12 | Trigonometric Substitution | 三角换元法 |  | 用三角函数替换变量以简化根式等积分。 |
| 13 | Trigonometric Identity | 三角恒等式 |  | 用于变换三角函数表达式的恒等关系。 |
| 14 | Reduction Formula | 递推积分公式 |  | 将某类积分化为参数较小同类积分的关系式。 |
| 15 | Rational Function Integration | 有理函数积分 |  | 对多项式之比的函数进行积分。 |
| 16 | Integrating Factor | 积分因子 |  | 乘到微分方程两边使其便于直接积分的函数。 |
| 17 | Elementary Antiderivative | 初等原函数 |  | 能够用有限次初等函数运算表示的原函数。 |
| 18 | Non-elementary Integral | 非初等积分 |  | 无法以有限个初等函数组合表示原函数的积分。 |
| 19 | Integration Formula | 积分公式 |  | 常用被积函数与原函数之间的标准对应关系。 |
| 20 | Improper Substitution | 不适当换元 |  | 未满足替换条件而可能改变积分值的换元操作。 |

## 07. 定积分与微积分基本定理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Definite Integral | 定积分 |  | 在给定区间上以极限方式定义的累积量。 |
| 2 | Riemann Sum | 黎曼和 |  | 以分割区间上的函数值乘小区间长度构成的有限和。 |
| 3 | Partition of an Interval | 区间划分 |  | 将积分区间分成有限个子区间。 |
| 4 | Mesh of a Partition | 分割的网格大小 |  | 划分中最长子区间的长度。 |
| 5 | Tagged Partition | 带标记的划分 |  | 为每个子区间选择一个采样点的划分。 |
| 6 | Riemann Integrability | 黎曼可积性 |  | 黎曼和在分割变细时收敛到同一极限的性质。 |
| 7 | Upper Darboux Sum | 达布上和 |  | 各子区间上确界与区间长度乘积之和。 |
| 8 | Lower Darboux Sum | 达布下和 |  | 各子区间下确界与区间长度乘积之和。 |
| 9 | Fundamental Theorem of Calculus | 微积分基本定理 | FTC | 建立定积分与导数、原函数之间联系的定理。 |
| 10 | Fundamental Theorem of Calculus Part I | 微积分基本定理第一部分 |  | 适当条件下变上限积分函数的导数等于被积函数。 |
| 11 | Fundamental Theorem of Calculus Part II | 微积分基本定理第二部分 |  | 连续函数的定积分可通过其原函数在端点的差计算。 |
| 12 | Net Change Theorem | 净变化定理 |  | 变化率的定积分等于相应量的净变化。 |
| 13 | Average Value of a Function | 函数平均值 |  | 函数在区间上的积分除以区间长度。 |
| 14 | Mean Value Theorem for Integrals | 积分中值定理 |  | 连续函数的积分等于某个函数值乘区间长度。 |
| 15 | Area under a Curve | 曲线下的面积 |  | 用非负函数的定积分表示的平面区域面积。 |
| 16 | Area between Curves | 曲线之间的面积 |  | 以两条曲线纵向或横向差的积分计算的面积。 |
| 17 | Accumulation Function | 累积函数 |  | 以变量为上限对给定函数作积分得到的函数。 |
| 18 | Variable Upper Limit Integral | 变上限积分 |  | 积分上限依赖变量的定积分。 |
| 19 | Signed Area | 有向面积 |  | 考虑函数位于坐标轴上方或下方符号的积分值。 |
| 20 | Additivity over Intervals | 区间可加性 |  | 相邻区间的积分值相加等于合并区间的积分值。 |

## 08. 积分应用与广义积分

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Volume by Slicing | 截面法求体积 |  | 对连续变化的横截面积积分求体积。 |
| 2 | Disk Method | 圆盘法 |  | 用圆盘截面积积分求旋转体体积。 |
| 3 | Washer Method | 圆环法 |  | 用外圆面积减内圆面积积分求旋转体体积。 |
| 4 | Cylindrical Shell Method | 柱壳法 |  | 用薄圆柱壳体积积分求旋转体体积。 |
| 5 | Arc Length | 弧长 |  | 曲线沿其轨迹的长度。 |
| 6 | Surface Area of Revolution | 旋转曲面面积 |  | 曲线绕轴旋转形成的曲面面积。 |
| 7 | Work Integral | 功积分 |  | 沿位移累积变化力做功的积分。 |
| 8 | Mass from Density | 由密度求质量 |  | 对线密度、面密度或体密度积分求质量。 |
| 9 | Center of Mass | 质心 |  | 由质量分布加权平均定义的位置。 |
| 10 | Moment of Inertia | 转动惯量 |  | 质量分布对旋转轴距离平方的加权积分。 |
| 11 | Improper Integral | 广义积分 |  | 积分区间无界或被积函数无界时通过极限定义的积分。 |
| 12 | Convergent Improper Integral | 收敛广义积分 |  | 定义广义积分的极限存在且有限。 |
| 13 | Divergent Improper Integral | 发散广义积分 |  | 定义广义积分的极限不存在或不有限。 |
| 14 | Comparison Test for Integrals | 广义积分比较判别法 |  | 用非负函数大小关系比较其积分敛散性。 |
| 15 | Limit Comparison Test for Integrals | 广义积分极限比较法 |  | 用函数比值的正有限极限判断积分敛散性。 |
| 16 | Absolute Convergence of an Integral | 积分的绝对收敛 |  | 被积函数绝对值的广义积分收敛。 |
| 17 | Conditional Convergence of an Integral | 积分的条件收敛 |  | 原广义积分收敛但绝对值积分发散。 |
| 18 | Principal Value Integral | 主值积分 |  | 通过对称或约定的极限方式定义的特殊积分值。 |
| 19 | Gamma Function | 伽马函数 |  | 通过广义积分定义并推广阶乘的特殊函数。 |
| 20 | Beta Function | 贝塔函数 |  | 由区间上的广义积分定义并与伽马函数相关的特殊函数。 |

## 09. 数列与无穷级数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sequence | 数列 |  | 按自然数下标排列的一串数。 |
| 2 | Limit of a Sequence | 数列极限 |  | 数列项在下标趋于无穷时趋近的值。 |
| 3 | Convergent Sequence | 收敛数列 |  | 具有有限极限的数列。 |
| 4 | Divergent Sequence | 发散数列 |  | 不具有有限极限的数列。 |
| 5 | Monotone Sequence | 单调数列 |  | 各项保持非减或非增的数列。 |
| 6 | Bounded Sequence | 有界数列 |  | 全部数列项都落在某有限区间内。 |
| 7 | Cauchy Sequence | 柯西数列 |  | 序列后部任意两项之间的距离都可任意小。 |
| 8 | Bolzano-Weierstrass Theorem | 博尔查诺-魏尔斯特拉斯定理 |  | 有界实数序列必含收敛子列。 |
| 9 | Subsequence | 子列 |  | 从原数列中按严格递增下标选取项形成的数列。 |
| 10 | Infinite Series | 无穷级数 |  | 数列各项进行无穷累加所对应的对象。 |
| 11 | Partial Sum | 部分和 |  | 级数前有限项的和。 |
| 12 | Convergent Series | 收敛级数 |  | 其部分和数列收敛到有限值的级数。 |
| 13 | Divergent Series | 发散级数 |  | 其部分和数列不收敛到有限值的级数。 |
| 14 | Geometric Series | 几何级数 |  | 相邻项具有固定公比的级数。 |
| 15 | Harmonic Series | 调和级数 |  | 各项为正整数倒数的发散级数。 |
| 16 | p-Series | p 级数 |  | 形如各项为 1/n^p 的无穷级数。 |
| 17 | Alternating Series | 交错级数 |  | 相邻项符号交替变化的级数。 |
| 18 | Alternating Series Test | 莱布尼茨判别法 |  | 对项的绝对值递减且趋零的交错级数给出收敛性判据。 |
| 19 | Ratio Test | 比值判别法 |  | 用相邻项绝对值之比的极限判断级数敛散。 |
| 20 | Root Test | 根值判别法 |  | 用一般项绝对值的 n 次方根的上极限判断敛散。 |
| 21 | Integral Test for Series | 积分判别法 |  | 通过相应非负递减函数的广义积分判断级数敛散。 |
| 22 | Absolute Convergence | 绝对收敛 |  | 级数各项绝对值所成级数收敛。 |
| 23 | Conditional Convergence | 条件收敛 |  | 原级数收敛但绝对值级数发散。 |
| 24 | Power Series | 幂级数 |  | 以变量与中心之差的非负整数次幂展开的级数。 |
| 25 | Radius of Convergence | 收敛半径 |  | 幂级数在展开中心附近绝对收敛的半径。 |
| 26 | Interval of Convergence | 收敛区间 |  | 幂级数在实轴上收敛的全部点组成的区间。 |
| 27 | Taylor Series | 泰勒级数 |  | 由某点各阶导数系数构成的形式幂级数。 |
| 28 | Maclaurin Series | 麦克劳林级数 |  | 以零为中心的泰勒级数。 |
| 29 | Uniform Convergence | 一致收敛 |  | 函数列的收敛精度可以对定义域内各点统一控制。 |
| 30 | Fourier Series | 傅里叶级数 |  | 以正弦和余弦函数展开周期函数的级数。 |

## 10. 多元函数与偏导数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multivariable Function | 多元函数 |  | 以两个或更多变量作为输入的函数。 |
| 2 | Scalar Field | 标量场 |  | 给空间中的每个点赋予一个标量的函数。 |
| 3 | Vector-valued Function | 向量值函数 |  | 输出为向量的函数。 |
| 4 | Vector Field | 向量场 |  | 给空间中的每个点赋予一个向量的函数。 |
| 5 | Level Curve | 等值线 |  | 二维标量函数取同一数值的点组成的曲线。 |
| 6 | Level Surface | 等值面 |  | 三维标量函数取同一数值的点组成的曲面。 |
| 7 | Partial Derivative | 偏导数 |  | 固定其他自变量，对某一自变量求得的导数。 |
| 8 | Second-order Partial Derivative | 二阶偏导数 |  | 对偏导函数再求一次偏导的结果。 |
| 9 | Mixed Partial Derivative | 混合偏导数 |  | 对不同变量依次求偏导形成的高阶偏导数。 |
| 10 | Clairaut's Theorem | 克莱罗定理 |  | 在适当连续性条件下混合二阶偏导数交换次序不变。 |
| 11 | Gradient | 梯度 |  | 由各坐标方向偏导数构成、指向局部最快增长方向的向量。 |
| 12 | Directional Derivative | 方向导数 |  | 函数沿指定方向的瞬时变化率。 |
| 13 | Total Differential | 全微分 |  | 多元可微函数的一阶线性变化部分。 |
| 14 | Total Derivative | 全导数 |  | 沿自变量共同变化的路径计算函数变化率。 |
| 15 | Jacobian Matrix | 雅可比矩阵 |  | 由向量值函数各分量的一阶偏导数组成的矩阵。 |
| 16 | Jacobian Determinant | 雅可比行列式 |  | 方阵雅可比矩阵的行列式，常用于变量替换。 |
| 17 | Hessian Matrix | 海森矩阵 |  | 由实值函数二阶偏导数组成的矩阵。 |
| 18 | Tangent Plane | 切平面 |  | 在可微点对曲面进行一阶线性近似的平面。 |
| 19 | Normal Vector | 法向量 |  | 垂直于曲线切线或曲面切平面的向量。 |
| 20 | Multivariable Chain Rule | 多元链式法则 |  | 使用偏导与雅可比矩阵对复合映射求导的法则。 |
| 21 | Implicit Function Theorem | 隐函数定理 |  | 在雅可比满足可逆性等条件时保证局部隐函数存在的定理。 |
| 22 | Inverse Function Theorem | 反函数定理 |  | 在导数映射可逆等条件下保证局部反函数存在的定理。 |

## 11. 多元极值与重积分

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multivariable Limit | 多元极限 |  | 多元输入以任意允许路径趋近某点时函数的共同极限。 |
| 2 | Path Dependence of a Limit | 极限的路径依赖性 |  | 沿不同路径趋近得到不同结果，说明极限不存在。 |
| 3 | Continuity of Multivariable Functions | 多元函数连续性 |  | 函数值等于输入向目标点趋近时的多元极限。 |
| 4 | Local Extremum in Several Variables | 多元局部极值 |  | 多元函数在某点邻域内达到局部最大或最小值。 |
| 5 | Critical Point in Several Variables | 多元临界点 |  | 梯度为零或某些偏导不存在的候选极值点。 |
| 6 | Saddle Point | 鞍点 |  | 既非局部最大也非局部最小的某类临界点。 |
| 7 | Second Derivative Test in Several Variables | 多元二阶导数判别法 |  | 用海森矩阵的正定性等性质判断驻点类型。 |
| 8 | Constrained Optimization | 约束最优化 |  | 在给定约束条件下优化目标函数。 |
| 9 | Lagrange Multipliers | 拉格朗日乘数法 |  | 利用目标函数梯度与约束梯度关系求约束极值。 |
| 10 | Double Integral | 二重积分 |  | 在二维区域上累积标量函数的积分。 |
| 11 | Triple Integral | 三重积分 |  | 在三维区域上累积标量函数的积分。 |
| 12 | Iterated Integral | 累次积分 |  | 依次对多个积分变量逐个积分的表达式。 |
| 13 | Fubini's Theorem | 富比尼定理 |  | 在适当可积条件下将重积分与累次积分联系起来。 |
| 14 | Tonelli's Theorem | 托内利定理 |  | 对于非负可测函数允许交换重积分顺序的定理。 |
| 15 | Change of Variables in Multiple Integrals | 重积分换元法 |  | 通过坐标变换及雅可比因子改写重积分。 |
| 16 | Polar Coordinate Integration | 极坐标积分 |  | 在平面区域上使用极坐标和相应面积因子积分。 |
| 17 | Cylindrical Coordinates | 柱坐标 |  | 用平面极坐标和高度描述空间点的坐标。 |
| 18 | Spherical Coordinates | 球坐标 |  | 通过半径及两个角度描述空间点的坐标。 |
| 19 | Volume Integral | 体积分 |  | 在三维区域上对函数积分。 |
| 20 | Area Integral | 面积积分 |  | 在二维区域上对函数积分。 |

## 12. 曲线、曲面与向量分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Parametric Curve | 参数曲线 |  | 用参数表示点的位置得到的曲线。 |
| 2 | Smooth Curve | 光滑曲线 |  | 具有连续且通常不为零的切向导数的参数曲线。 |
| 3 | Arc Length Parameter | 弧长参数 |  | 以沿曲线的长度作为曲线参数。 |
| 4 | Line Integral of a Scalar Field | 第一类曲线积分 |  | 沿曲线对标量场按弧长元素积分。 |
| 5 | Line Integral of a Vector Field | 第二类曲线积分 |  | 沿有向曲线对向量场与位移点积积分。 |
| 6 | Circulation | 环流 |  | 向量场沿闭合有向曲线的线积分。 |
| 7 | Conservative Vector Field | 保守向量场 |  | 线积分在适当区域内仅依赖端点的向量场。 |
| 8 | Potential Function | 势函数 |  | 其梯度等于给定保守向量场的标量函数。 |
| 9 | Path Independence | 路径无关性 |  | 两个固定端点间线积分的值与所选路径无关。 |
| 10 | Fundamental Theorem for Line Integrals | 曲线积分基本定理 |  | 梯度场沿曲线的积分等于势函数端点值之差。 |
| 11 | Divergence | 散度 |  | 描述向量场局部净流出强度的标量。 |
| 12 | Curl | 旋度 |  | 描述三维向量场局部旋转趋势的向量。 |
| 13 | Laplacian | 拉普拉斯算子 |  | 标量函数各坐标方向二阶偏导之和构成的算子。 |
| 14 | Surface Integral of a Scalar Field | 第一类曲面积分 |  | 在曲面上对标量场按面积元素积分。 |
| 15 | Flux Integral | 通量积分 |  | 向量场通过定向曲面的法向分量之面积积分。 |
| 16 | Orientation of a Surface | 曲面定向 |  | 为曲面连续选择法向方向的约定。 |
| 17 | Green's Theorem | 格林公式 |  | 将平面闭曲线积分与其包围区域上的二重积分联系起来。 |
| 18 | Stokes' Theorem | 斯托克斯定理 |  | 将曲面边界环流与曲面上旋度通量联系起来。 |
| 19 | Divergence Theorem | 散度定理 |  | 将闭合曲面向外通量与内部散度体积分联系起来。 |
| 20 | Gauss's Theorem | 高斯公式 |  | 散度定理的另一常见名称。 |
| 21 | Solenoidal Field | 无散场 |  | 散度为零的向量场。 |
| 22 | Irrotational Field | 无旋场 |  | 旋度为零的向量场。 |
| 23 | Tangent Vector | 切向量 |  | 表示参数曲线在一点处瞬时运动方向的向量。 |
| 24 | Unit Normal Vector | 单位法向量 |  | 长度为一且垂直于曲面切平面的向量。 |
| 25 | Surface Parameterization | 曲面参数化 |  | 用两个参数表示曲面上点的位置。 |

## 13. 常微分方程初步

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Ordinary Differential Equation | 常微分方程 | ODE | 未知函数只依赖一个自变量的微分方程。 |
| 2 | Differential Equation | 微分方程 |  | 包含未知函数及其导数的方程。 |
| 3 | Order of a Differential Equation | 微分方程的阶 |  | 方程出现的未知函数最高阶导数的阶数。 |
| 4 | Initial Value Problem | 初值问题 | IVP | 给定某个起点的函数值或导数值以确定微分方程解的问题。 |
| 5 | Boundary Value Problem | 边值问题 | BVP | 在区间端点或边界给定条件的微分方程问题。 |
| 6 | General Solution | 通解 |  | 含有足够自由常数的解族。 |
| 7 | Particular Solution | 特解 |  | 满足具体初始或边界条件的一个解。 |
| 8 | Separable Differential Equation | 可分离变量微分方程 |  | 可将自变量与未知函数分别置于两边并积分的方程。 |
| 9 | First-order Linear ODE | 一阶线性常微分方程 |  | 未知函数及一阶导数以线性方式出现的常微分方程。 |
| 10 | Homogeneous Linear ODE | 齐次线性常微分方程 |  | 线性微分方程右端为零的情况。 |
| 11 | Nonhomogeneous Linear ODE | 非齐次线性常微分方程 |  | 线性微分方程右端包含非零外部项的情况。 |
| 12 | Characteristic Equation | 特征方程 |  | 求常系数线性微分方程指数型解时得到的代数方程。 |
| 13 | Equilibrium Solution | 平衡解 |  | 不随自变量变化的常数解。 |
| 14 | Existence and Uniqueness Theorem | 存在唯一性定理 |  | 给出微分方程局部解存在与唯一性的充分条件。 |
| 15 | Picard-Lindelof Theorem | 皮卡-林德勒夫定理 |  | 在适当利普希茨条件下保证初值问题局部唯一解的定理。 |
| 16 | Exponential Growth Model | 指数增长模型 |  | 增长率与当前量成正比的微分方程模型。 |
| 17 | Logistic Equation | 逻辑斯蒂方程 |  | 包含增长上限效应的常见一阶非线性微分方程。 |
| 18 | Phase Line | 相线 |  | 在一维自治微分方程中标示平衡点和解流动方向的图。 |

## 14. 数值近似与计算实践

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Numerical Differentiation | 数值微分 |  | 利用离散函数值近似导数的方法。 |
| 2 | Forward Difference | 前向差分 |  | 用向前相邻采样点构造的差分。 |
| 3 | Backward Difference | 后向差分 |  | 用向后相邻采样点构造的差分。 |
| 4 | Central Difference | 中心差分 |  | 利用点两侧采样值构造的差分。 |
| 5 | Finite Difference Method | 有限差分法 |  | 用网格上的差分表达式近似微分算子的方法。 |
| 6 | Truncation Error | 截断误差 |  | 用有限阶近似替代精确数学表达式产生的误差。 |
| 7 | Round-off Error | 舍入误差 |  | 有限精度数值表示与运算产生的误差。 |
| 8 | Numerical Integration | 数值积分 |  | 利用离散采样和求积公式近似定积分的方法。 |
| 9 | Trapezoidal Rule | 梯形公式 |  | 用相邻采样点连成的梯形面积近似积分。 |
| 10 | Simpson's Rule | 辛普森公式 |  | 用分段二次插值多项式近似积分。 |
| 11 | Quadrature | 数值求积 |  | 用有限加权函数值计算积分近似值的过程。 |
| 12 | Error Bound | 误差界 |  | 对近似值与真实值偏差大小的可证明上界。 |
| 13 | Euler's Method | 欧拉法 |  | 沿微分方程给出的斜率逐步推进近似解的方法。 |
| 14 | Runge-Kutta Method | 龙格-库塔法 |  | 通过多个阶段斜率组合构造常微分方程数值解的方法。 |
| 15 | Step Size | 步长 |  | 数值迭代中自变量每次推进的间隔。 |
| 16 | Adaptive Step Size | 自适应步长 |  | 根据误差估计动态调整数值积分步长的方法。 |
| 17 | Condition Number | 条件数 |  | 衡量问题输出对输入微小扰动敏感程度的量。 |
| 18 | Convergence Rate | 收敛速度 |  | 描述近似误差随迭代次数或网格变细而减小的快慢。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/calculus.pdf) · [独立整理稿](../data/calculus.tsv)

欢迎通过 [CONTRIBUTING.md](../CONTRIBUTING.md) 提交术语修正、标准译名、出处和争议释义。

本词表是供学习与研究使用的社区参考资料，并非教材或标准组织的官方发布版本。
