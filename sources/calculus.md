# 微积分专有名词中英文对照表

# Calculus: Chinese–English Glossary

> 版本：v1.0 | 2026-11-16  | 范围：单变量微积分、多元微积分、向量微积分、基础常微分方程
> 共 361 个术语，16 个主题。英文优先选用常见教材表达；相近术语可能因语境而异。

## 使用说明

- “英文名称”以常用的数学教材或学术英文为主，斜杠表示常见同义表达。
- “符号 / 示例”是典型写法，不一定是完整定义或无条件成立的公式。
- 部分定理与公式需要额外的可微性、连续性、可积性或区域条件；请结合教材理解。
- **扩展内容**：个别词条涉及实分析、数值分析或微分方程，便于交叉学科学习。

## 目录

- [01. 基础概念与函数 — Foundations & Functions](#01-基础概念与函数)
- [02. 极限与连续性 — Limits & Continuity](#02-极限与连续性)
- [03. 导数与微分 — Derivatives & Differentials](#03-导数与微分)
- [04. 微分定理与函数分析 — Differential Theorems & Analysis](#04-微分定理与函数分析)
- [05. 不定积分与积分技巧 — Antiderivatives & Techniques](#05-不定积分与积分技巧)
- [06. 定积分与积分基本定理 — Definite Integrals & Fundamental Theorem](#06-定积分与积分基本定理)
- [07. 反常积分与数值积分 — Improper & Numerical Integration](#07-反常积分与数值积分)
- [08. 积分的几何与物理应用 — Applications of Integration](#08-积分的几何与物理应用)
- [09. 无穷数列与级数 — Sequences & Series](#09-无穷数列与级数)
- [10. 幂级数与函数展开 — Power Series & Expansions](#10-幂级数与函数展开)
- [11. 多元函数与偏导数 — Multivariable Functions & Partial Derivatives](#11-多元函数与偏导数)
- [12. 多元最优化与隐函数 — Optimization & Implicit Functions](#12-多元最优化与隐函数)
- [13. 重积分与坐标变换 — Multiple Integrals & Coordinate Changes](#13-重积分与坐标变换)
- [14. 向量微积分 — Vector Calculus](#14-向量微积分)
- [15. 常微分方程入门 — Ordinary Differential Equations](#15-常微分方程入门)
- [16. 常用数学记号与英文表达 — Notation & Academic English](#16-常用数学记号与英文表达)

## 01. 基础概念与函数

*Foundations & Functions · 24 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 微积分 | Calculus | — | 研究变化率、累积量及其联系的数学分支 |
| 微分学 | Differential calculus | — | 主要研究导数及局部变化 |
| 积分学 | Integral calculus | — | 主要研究累积、面积和积分 |
| 函数 | Function | f: A → B | 将定义域中的元素映射到值域中的元素 |
| 自变量 | Independent variable | x | 函数的输入变量 |
| 因变量 | Dependent variable | y = f(x) | 随自变量变化的输出变量 |
| 定义域 | Domain | dom(f) | 函数允许的输入集合 |
| 陪域 | Codomain | B | 函数声明的目标集合 |
| 值域 | Range / image | f(A) | 函数实际取得的输出集合 |
| 函数图像 | Graph of a function | y = f(x) | 函数输入与输出的几何表示 |
| 复合函数 | Composite function | f ∘ g | 由多个函数依次作用形成 |
| 反函数 | Inverse function | f⁻¹ | 在适当条件下撤销原函数映射 |
| 分段函数 | Piecewise-defined function | — | 在不同区间采用不同表达式 |
| 偶函数 | Even function | f(−x)=f(x) | 关于纵轴对称的函数 |
| 奇函数 | Odd function | f(−x)=−f(x) | 关于原点对称的函数 |
| 周期函数 | Periodic function | f(x+T)=f(x) | 按固定周期重复函数值 |
| 单调递增 | Monotonically increasing | — | 自变量增加时函数值不下降 |
| 严格递增 | Strictly increasing | — | 自变量增加时函数值严格增大 |
| 有界函数 | Bounded function | — | 函数值落在有限界限内 |
| 连续函数 | Continuous function | — | 在所论点或区间上满足连续性 |
| 初等函数 | Elementary function | — | 由常用基本函数经有限次运算与复合得到 |
| 参数方程 | Parametric equation | x=x(t), y=y(t) | 以参数表示曲线坐标 |
| 极坐标 | Polar coordinates | (r, θ) | 通过半径与角度描述平面位置 |
| 弧度 | Radian | rad | 以弧长与半径之比定义的角度单位 |

## 02. 极限与连续性

*Limits & Continuity · 27 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 极限 | Limit | lim | 描述变量接近某点时的趋近值 |
| 函数极限 | Limit of a function | limₓ→ₐ f(x) | 函数在自变量趋近时的变化趋势 |
| 数列极限 | Limit of a sequence | limₙ→∞ aₙ | 描述数列项的渐近行为 |
| 左极限 | Left-hand limit | limₓ→ₐ⁻ | 从左侧趋向指定点的极限 |
| 右极限 | Right-hand limit | limₓ→ₐ⁺ | 从右侧趋向指定点的极限 |
| 无穷极限 | Infinite limit | ∞ / −∞ | 函数值向正或负无穷增大 |
| 无穷远处的极限 | Limit at infinity | limₓ→∞ | 当自变量绝对值增大时考察极限 |
| 单侧极限 | One-sided limit | — | 从某一侧靠近点时的极限 |
| 无穷小量 | Infinitesimal | — | 在给定极限过程中趋于零的量 |
| 无穷大量 | Infinitely large quantity | — | 在给定极限过程中绝对值趋于无穷的量 |
| 等价无穷小 | Asymptotically equivalent infinitesimals | f ∼ g | 两量之比趋于 1 |
| 高阶无穷小 | Higher-order infinitesimal | f=o(g) | 相对另一无穷小收敛得更快 |
| 小 o 记号 | Little-o notation | o(g) | 描述可忽略的相对阶 |
| 大 O 记号 | Big-O notation | O(g) | 描述渐近量级上界 |
| 夹逼定理 | Squeeze theorem / sandwich theorem | — | 用上下界共同极限确定目标极限 |
| ε–δ 定义 | Epsilon-delta definition | ε, δ | 函数极限的严格定义方式 |
| ε–N 定义 | Epsilon-N definition | ε, N | 数列极限的严格定义方式 |
| 连续性 | Continuity | — | 极限值等于函数在该点的值 |
| 左连续 | Left continuity | — | 左极限等于函数值 |
| 右连续 | Right continuity | — | 右极限等于函数值 |
| 间断点 | Point of discontinuity | — | 函数不连续的位置 |
| 可去间断点 | Removable discontinuity | — | 重新定义函数值后可使其连续 |
| 跳跃间断点 | Jump discontinuity | — | 左右极限有限但不相等 |
| 介值定理 | Intermediate value theorem | IVT | 连续函数取得端点函数值之间的所有值 |
| 最值定理 | Extreme value theorem | EVT | 闭区间上连续函数达到最大最小值 |
| 海涅定理 | Sequential criterion for limits | — | 通过任意趋近点的数列刻画函数极限 |
| 柯西收敛准则 | Cauchy criterion | — | 通过项间距离刻画收敛 |

## 03. 导数与微分

*Derivatives & Differentials · 27 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 导数 | Derivative | f′(x) | 函数在一点的瞬时变化率 |
| 导函数 | Derivative function | f′ | 把每一点映射到其导数的函数 |
| 导数定义 | Definition of derivative | limₕ→₀ [f(x+h)−f(x)]/h | 差商的极限 |
| 差商 | Difference quotient | Δy/Δx | 函数增量与自变量增量的比 |
| 增量 | Increment | Δx, Δy | 变量发生的变化量 |
| 切线 | Tangent line | — | 在可导点与曲线一阶贴合的直线 |
| 切线斜率 | Slope of tangent line | f′(x₀) | 切线的斜率 |
| 微分 | Differential | dy=f′(x)dx | 函数的线性主部变化 |
| 可导性 | Differentiability | — | 导数存在的性质 |
| 左导数 | Left-hand derivative | f′₋(x) | 从左侧差商得到的导数 |
| 右导数 | Right-hand derivative | f′₊(x) | 从右侧差商得到的导数 |
| 一阶导数 | First derivative | f′(x) | 函数的第一次求导结果 |
| 二阶导数 | Second derivative | f″(x) | 导数的导数 |
| 高阶导数 | Higher-order derivative | f⁽ⁿ⁾(x) | 重复求导得到的导数 |
| 莱布尼茨导数记号 | Leibniz notation | dy/dx | 用微分符号表示导数 |
| 拉格朗日导数记号 | Lagrange notation | f′(x) | 用撇号表示导数 |
| 牛顿导数记号 | Newton's notation | ẋ, ẍ | 常用于对时间求导 |
| 链式法则 | Chain rule | (f∘g)′=(f′∘g)g′ | 复合函数求导法则 |
| 乘积法则 | Product rule | (fg)′=f′g+fg′ | 两个函数乘积的求导法则 |
| 商法则 | Quotient rule | (f/g)′=(f′g−fg′)/g² | 两个函数商的求导法则 |
| 幂函数求导法则 | Power rule | d(xⁿ)/dx=nxⁿ⁻¹ | 幂函数的基本求导公式 |
| 隐函数求导 | Implicit differentiation | — | 对隐式方程两边求导 |
| 对数求导法 | Logarithmic differentiation | — | 先取对数再求导以简化乘幂关系 |
| 参数方程求导 | Parametric differentiation | dy/dx=(dy/dt)/(dx/dt) | 按参数求导再取比值 |
| 反函数求导 | Inverse function differentiation | — | 依据原函数导数计算反函数导数 |
| 线性近似 | Linear approximation | f(a)+f′(a)(x−a) | 用切线近似函数 |
| 局部线性化 | Local linearization | — | 用一阶线性模型刻画局部行为 |

## 04. 微分定理与函数分析

*Differential Theorems & Analysis · 27 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 费马引理 | Fermat's theorem on stationary points | — | 可导函数在内点极值处导数为零 |
| 罗尔定理 | Rolle's theorem | — | 端点函数值相等时存在导数为零的内点 |
| 拉格朗日中值定理 | Mean value theorem | MVT | 某内点导数等于区间平均变化率 |
| 柯西中值定理 | Cauchy's mean value theorem | — | 将中值定理推广到两函数 |
| 洛必达法则 | L'Hôpital's rule | — | 在适当条件下用导数比求未定式极限 |
| 泰勒定理 | Taylor's theorem | — | 用多项式及余项近似光滑函数 |
| 泰勒多项式 | Taylor polynomial | Tₙ(x) | 某点附近的有限阶多项式近似 |
| 麦克劳林多项式 | Maclaurin polynomial | Tₙ at 0 | 在零点展开的泰勒多项式 |
| 佩亚诺余项 | Peano form of remainder | o((x−a)ⁿ) | 泰勒公式的渐近余项 |
| 拉格朗日余项 | Lagrange form of remainder | — | 以高阶导数表达的泰勒余项 |
| 驻点 | Stationary point | f′(x)=0 | 一阶导数为零的点 |
| 临界点 | Critical point | — | 定义域内导数为零或不存在的内点 |
| 局部极大值 | Local maximum | — | 邻域内不小于周围函数值 |
| 局部极小值 | Local minimum | — | 邻域内不大于周围函数值 |
| 全局最大值 | Global maximum | — | 定义域内的最大函数值 |
| 全局最小值 | Global minimum | — | 定义域内的最小函数值 |
| 一阶导数判别法 | First derivative test | — | 依据导数符号变化判断极值 |
| 二阶导数判别法 | Second derivative test | — | 通过二阶导数符号分析驻点 |
| 凸函数 | Convex function | — | 函数图像位于任意弦下方或弦上 |
| 凹函数 | Concave function | — | 函数图像位于任意弦上方或弦下方 |
| 拐点 | Inflection point | — | 曲线凹凸性发生变化的点 |
| 曲率 | Curvature | κ | 刻画曲线弯曲程度的量 |
| 渐近线 | Asymptote | — | 曲线逐渐接近的直线 |
| 水平渐近线 | Horizontal asymptote | y=L | 趋向无穷远时接近的水平直线 |
| 垂直渐近线 | Vertical asymptote | x=a | 靠近该直线时函数值趋于无穷 |
| 斜渐近线 | Oblique asymptote | y=mx+b | 无穷远处接近的非水平直线 |
| 最优化 | Optimization | — | 寻找目标函数的极值 |

## 05. 不定积分与积分技巧

*Antiderivatives & Techniques · 20 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 原函数 | Antiderivative | F′=f | 导数等于给定函数的函数 |
| 不定积分 | Indefinite integral | ∫f(x)dx | 函数所有原函数的族 |
| 积分常数 | Constant of integration | C | 不定积分中的任意常数 |
| 积分变量 | Variable of integration | x | 积分运算所对应的变量 |
| 被积函数 | Integrand | f(x) | 积分号内部被积的函数 |
| 积分号 | Integral sign | ∫ | 表示积分运算的符号 |
| 积分微元 | Differential element | dx | 积分表达式中的微分记号 |
| 基本积分公式 | Basic integration formulas | — | 常见函数的原函数公式 |
| 换元积分法 | Integration by substitution | u=g(x) | 通过变量替换简化积分 |
| 第一类换元法 | Substitution method | — | 利用复合函数形式进行换元 |
| 第二类换元法 | Change-of-variable method | x=φ(t) | 显式引入新变量进行换元 |
| 分部积分法 | Integration by parts | ∫u dv=uv−∫v du | 由乘积法则导出的积分方法 |
| 有理函数积分 | Integration of rational functions | — | 有理函数的积分计算 |
| 部分分式分解 | Partial fraction decomposition | — | 将有理式拆为简单分式之和 |
| 三角代换 | Trigonometric substitution | — | 利用三角恒等式简化根式积分 |
| 三角恒等变换 | Trigonometric identities | — | 用三角公式转化被积函数 |
| 万能代换 | Tangent half-angle substitution | t=tan(x/2) | 把部分三角积分转为有理函数积分 |
| 递推积分公式 | Reduction formula | — | 将某类积分化为较低阶积分 |
| 不可用初等函数表示的原函数 | Non-elementary antiderivative | — | 不能写为有限个初等函数组合的原函数 |
| 误差函数 | Error function | erf(x) | 高斯函数积分相关的特殊函数 |

## 06. 定积分与积分基本定理

*Definite Integrals & Fundamental Theorem · 22 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 定积分 | Definite integral | ∫ₐᵇ f(x)dx | 区间上函数的有符号累积量 |
| 积分区间 | Interval of integration | [a,b] | 定积分的自变量范围 |
| 积分上限 | Upper limit of integration | b | 定积分区间右端点 |
| 积分下限 | Lower limit of integration | a | 定积分区间左端点 |
| 黎曼和 | Riemann sum | Σf(ξᵢ)Δxᵢ | 用小区间加权和近似积分 |
| 黎曼积分 | Riemann integral | — | 用分割和的极限定义的积分 |
| 黎曼可积 | Riemann integrable | — | 黎曼和极限存在且与取样一致 |
| 分割 | Partition | P={x₀,…,xₙ} | 把区间划分为若干小区间 |
| 分割网格大小 | Mesh size of a partition | ‖P‖ | 分割中最长小区间的长度 |
| 上和 | Upper Darboux sum | U(f,P) | 各小区间上确界构成的和 |
| 下和 | Lower Darboux sum | L(f,P) | 各小区间下确界构成的和 |
| 达布积分 | Darboux integral | — | 以达布上、下和定义积分 |
| 积分中值定理 | Mean value theorem for integrals | — | 连续函数的积分等于区间长度乘某函数值 |
| 微积分基本定理 | Fundamental theorem of calculus | FTC | 建立求导与定积分之间的关系 |
| 变上限积分 | Integral with variable upper limit | F(x)=∫ₐˣ f(t)dt | 上限变化产生的累积函数 |
| 牛顿–莱布尼茨公式 | Newton–Leibniz formula | ∫ₐᵇ f=F(b)−F(a) | 使用原函数计算定积分 |
| 积分的线性性 | Linearity of integration | — | 积分与线性组合交换 |
| 积分可加性 | Additivity of definite integrals | — | 积分可按区间拆分相加 |
| 积分比较定理 | Comparison theorem for integrals | — | 点态不等式在积分下保持序关系 |
| 积分估计 | Integral estimation | — | 用上界和下界估算积分值 |
| 变限积分求导 | Differentiation of integral with variable limits | — | 对上下限含变量的积分求导 |
| 莱布尼茨积分法则 | Leibniz integral rule | — | 适当条件下对含参数的积分求导 |

## 07. 反常积分与数值积分

*Improper & Numerical Integration · 20 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 反常积分 | Improper integral | — | 无限区间或无界被积函数上的积分 |
| 无穷区间积分 | Integral over an infinite interval | ∫ₐ^∞ f(x)dx | 积分区间延伸到无穷 |
| 瑕积分 | Improper integral with singularity | — | 被积函数在积分端点或内部无界 |
| 反常积分收敛 | Convergence of improper integrals | — | 相关极限存在且有限 |
| 绝对收敛 | Absolute convergence | ∫∣f∣<∞ | 绝对值的反常积分收敛 |
| 条件收敛 | Conditional convergence | — | 原积分收敛但绝对积分不收敛 |
| 比较判别法 | Comparison test | — | 通过正函数大小比较判断收敛性 |
| 极限比较判别法 | Limit comparison test | — | 用函数比值的极限判断收敛 |
| 柯西主值 | Cauchy principal value | PV∫ | 以对称方式取极限的积分值 |
| 伽马函数 | Gamma function | Γ(s) | 阶乘向实数或复数的推广 |
| 贝塔函数 | Beta function | B(p,q) | 与伽马函数相关的特殊积分 |
| 数值积分 | Numerical integration / quadrature | — | 用数值方法近似计算定积分 |
| 求积公式 | Quadrature rule | — | 使用加权函数值近似积分 |
| 梯形法则 | Trapezoidal rule | — | 以梯形面积近似曲线下面积 |
| 辛普森法则 | Simpson's rule | — | 以二次插值近似积分 |
| 复化梯形公式 | Composite trapezoidal rule | — | 分段应用梯形公式 |
| 复化辛普森公式 | Composite Simpson's rule | — | 分段应用辛普森公式 |
| 高斯求积 | Gaussian quadrature | — | 选择节点与权重提高积分精度 |
| 自适应求积 | Adaptive quadrature | — | 依据误差估计细化积分区间 |
| 截断误差 | Truncation error | — | 近似公式与精确目标之间的误差 |

## 08. 积分的几何与物理应用

*Applications of Integration · 16 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 曲线下面积 | Area under a curve | — | 函数与坐标轴之间的几何面积 |
| 曲线间面积 | Area between curves | — | 两条曲线围成区域的面积 |
| 旋转体体积 | Volume of a solid of revolution | — | 平面区域绕直线旋转得到的体积 |
| 圆盘法 | Disk method | — | 通过圆盘横截面积计算体积 |
| 垫片法 | Washer method | — | 通过圆环横截面积计算体积 |
| 柱壳法 | Cylindrical shell method | — | 通过薄柱壳累加计算体积 |
| 截面法 | Method of cross sections | — | 通过截面积积分求体积 |
| 弧长 | Arc length | s | 曲线的长度 |
| 曲面面积 | Surface area | A | 二维曲面在三维空间中的面积 |
| 旋转曲面面积 | Surface area of revolution | — | 曲线旋转形成曲面的面积 |
| 质心 | Center of mass | — | 按质量分布确定的平均位置 |
| 形心 | Centroid | — | 几何区域的均匀密度中心 |
| 转动惯量 | Moment of inertia | I | 质量相对于转轴分布的二次矩 |
| 功 | Work | W=∫F·ds | 力沿位移的累积作用 |
| 平均值 | Average value of a function | [1/(b−a)]∫ₐᵇ f | 函数在区间内的积分平均 |
| 累积变化量 | Net change | ∫ₐᵇ f′(x)dx | 变化率积分得到的净变化 |

## 09. 无穷数列与级数

*Sequences & Series · 24 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 无穷数列 | Infinite sequence | (aₙ) | 按自然数索引的数列 |
| 单调数列 | Monotone sequence | — | 各项按同一方向变化 |
| 有界数列 | Bounded sequence | — | 所有项落在某有界区间 |
| 单调收敛定理 | Monotone convergence theorem (sequences) | — | 单调且有界的实数数列必收敛 |
| 子列 | Subsequence | (aₙₖ) | 从原数列按递增索引抽取的数列 |
| 聚点 | Cluster point / accumulation point | — | 可由数列子列趋近的点或集合的聚集点 |
| 上极限 | Limit superior | lim sup | 数列尾部上界的渐近极限 |
| 下极限 | Limit inferior | lim inf | 数列尾部下界的渐近极限 |
| 无穷级数 | Infinite series | Σaₙ | 无穷多个项的形式和 |
| 部分和 | Partial sum | Sₙ=Σₖ₌₁ⁿaₖ | 级数前 n 项的和 |
| 级数收敛 | Series convergence | — | 部分和数列存在有限极限 |
| 级数发散 | Series divergence | — | 部分和数列不收敛到有限值 |
| 几何级数 | Geometric series | Σarⁿ | 公比固定的级数 |
| 调和级数 | Harmonic series | Σ1/n | 著名的发散正项级数 |
| p 级数 | p-series | Σ1/nᵖ | 以指数 p 判断收敛的标准级数 |
| 交错级数 | Alternating series | Σ(−1)ⁿaₙ | 正负项交替的级数 |
| 莱布尼茨判别法 | Alternating series test | — | 判断特定交错级数收敛的准则 |
| 比值判别法 | Ratio test | — | 通过相邻项比值判断绝对收敛 |
| 根值判别法 | Root test | — | 通过项绝对值 n 次根判断收敛 |
| 积分判别法 | Integral test | — | 用正函数反常积分判断对应级数 |
| 比较判别法（级数） | Comparison test for series | — | 与已知正项级数比较 |
| 狄利克雷判别法 | Dirichlet's test | — | 基于部分和有界与因子趋零的判别法 |
| 阿贝尔判别法 | Abel's test | — | 基于级数收敛与因子单调有界的判别法 |
| 重排 | Rearrangement of a series | — | 改变级数各项的排列顺序 |

## 10. 幂级数与函数展开

*Power Series & Expansions · 20 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 函数项级数 | Series of functions | Σfₙ(x) | 各项本身为函数的级数 |
| 幂级数 | Power series | Σaₙ(x−c)ⁿ | 围绕中心 c 的幂函数级数 |
| 收敛中心 | Center of convergence | c | 幂级数展开的中心点 |
| 收敛半径 | Radius of convergence | R | 幂级数保证绝对收敛的半径 |
| 收敛区间 | Interval of convergence | — | 实变量幂级数的收敛 x 范围 |
| 逐点收敛 | Pointwise convergence | — | 对每个固定点函数项序列收敛 |
| 一致收敛 | Uniform convergence | — | 收敛速度可以与点的选择无关 |
| 一致收敛判别法 | Weierstrass M-test | M-test | 用可求和上界判别一致收敛 |
| 逐项求导 | Term-by-term differentiation | — | 在适当条件下交换求导与求和 |
| 逐项积分 | Term-by-term integration | — | 在适当条件下交换积分与求和 |
| 泰勒级数 | Taylor series | Σf⁽ⁿ⁾(a)(x−a)ⁿ/n! | 用各阶导数构造的幂级数 |
| 麦克劳林级数 | Maclaurin series | Taylor series at 0 | 以零为展开中心的泰勒级数 |
| 泰勒展开 | Taylor expansion | — | 函数在某点附近的多项式或级数展开 |
| 解析函数 | Analytic function | — | 局部可由收敛幂级数表示的函数 |
| 余项 | Remainder term | Rₙ(x) | 截断展开后剩余的部分 |
| 收敛端点 | Endpoint of convergence | c±R | 幂级数收敛区间的候选端点 |
| 二项式级数 | Binomial series | — | 广义二项式函数的幂级数展开 |
| 傅里叶级数 | Fourier series | Σ(aₙcos nx+bₙsin nx) | 用正弦和余弦展开周期函数 |
| 傅里叶系数 | Fourier coefficients | aₙ, bₙ | 傅里叶展开中的权重 |
| 正交性 | Orthogonality | — | 内积为零的性质 |

## 11. 多元函数与偏导数

*Multivariable Functions & Partial Derivatives · 25 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 多元函数 | Multivariable function | f(x₁,…,xₙ) | 输入由多个变量组成的函数 |
| 二元函数 | Function of two variables | f(x,y) | 输入由两个变量组成的函数 |
| 定义域（多元） | Domain (multivariable) | D⊆ℝⁿ | 多元函数的输入点集合 |
| 等值线 | Level curve | f(x,y)=c | 二维函数具有相同函数值的点集 |
| 等值面 | Level surface | f(x,y,z)=c | 三维函数具有相同函数值的曲面 |
| 等高线图 | Contour plot | — | 在平面上显示各等值线的图形 |
| 偏导数 | Partial derivative | ∂f/∂x | 保持其他自变量不变的变化率 |
| 偏微分 | Partial differential | ∂f/∂x · dx | 与某坐标方向相关的微分项 |
| 二阶偏导数 | Second partial derivative | ∂²f/∂x² | 对某变量重复求偏导 |
| 混合偏导数 | Mixed partial derivative | ∂²f/∂x∂y | 按不同变量求高阶偏导 |
| 克莱罗定理 | Clairaut's theorem / Schwarz's theorem | fₓᵧ=fᵧₓ | 在适当连续性条件下混合偏导相等 |
| 梯度 | Gradient | ∇f | 由各偏导数组成的向量 |
| 梯度向量 | Gradient vector | grad f | 函数增加最快方向的向量 |
| 方向导数 | Directional derivative | Dᵤf | 沿指定方向的变化率 |
| 单位方向向量 | Unit direction vector | ‖u‖=1 | 用于定义方向导数的单位向量 |
| 全微分 | Total differential | df=Σ(∂f/∂xᵢ)dxᵢ | 多元函数的一阶线性变化量 |
| 全导数 | Total derivative | df/dt | 沿参数路径的函数变化率 |
| 全微分公式 | Total differential formula | — | 以偏导数表示一阶变化 |
| 多元链式法则 | Multivariable chain rule | — | 对多变量复合映射求导的法则 |
| 雅可比矩阵 | Jacobian matrix | J_f | 向量值函数的一阶偏导数矩阵 |
| 雅可比行列式 | Jacobian determinant | det J | 方形雅可比矩阵的行列式 |
| 海森矩阵 | Hessian matrix | H_f | 标量函数的二阶偏导矩阵 |
| 切平面 | Tangent plane | — | 曲面在一点的一阶线性近似 |
| 法向量 | Normal vector | n | 与曲面切空间正交的向量 |
| 可微性（多元） | Differentiability (multivariable) | — | 函数可由线性映射一阶近似的性质 |

## 12. 多元最优化与隐函数

*Optimization & Implicit Functions · 18 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 偏导数判别法 | Partial derivative test | — | 利用一阶偏导数寻找候选极值点 |
| 驻点（多元） | Stationary point (multivariable) | ∇f=0 | 梯度为零的点 |
| 临界点（多元） | Critical point (multivariable) | — | 梯度为零或微分失效等候选点 |
| 局部极值（多元） | Local extremum | — | 局部邻域内的最大或最小值 |
| 鞍点 | Saddle point | — | 附近既有更大值也有更小值的驻点 |
| 正定矩阵 | Positive-definite matrix | vᵀHv>0 | 多元二阶充分条件中的一种矩阵性质 |
| 二阶充分条件 | Second-order sufficient condition | — | 根据 Hessian 正负定性判断严格局部极值 |
| 约束优化 | Constrained optimization | — | 在等式或不等式限制下求极值 |
| 无约束优化 | Unconstrained optimization | — | 不含显式限制条件的优化 |
| 拉格朗日乘子法 | Method of Lagrange multipliers | ∇f=λ∇g | 用于等式约束下的驻点条件 |
| 拉格朗日函数 | Lagrangian | L=f−λg | 把目标函数与约束组合为辅助函数 |
| 拉格朗日乘子 | Lagrange multiplier | λ | 与约束相关的辅助变量 |
| 隐函数 | Implicit function | F(x,y)=0 | 由关系式局部确定的函数 |
| 隐函数定理 | Implicit function theorem | IFT | 给出方程局部可解出变量的条件 |
| 反函数定理 | Inverse function theorem | — | 给出局部可逆和反函数可微的条件 |
| 多元泰勒展开 | Multivariable Taylor expansion | — | 用梯度和 Hessian 等高阶项作局部近似 |
| 梯度下降 | Gradient descent | xₖ₊₁=xₖ−η∇f | 沿负梯度更新以降低目标函数 |
| 牛顿法（优化） | Newton's method (optimization) | — | 结合梯度与 Hessian 寻找驻点 |

## 13. 重积分与坐标变换

*Multiple Integrals & Coordinate Changes · 20 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 二重积分 | Double integral | ∬_D f(x,y)dA | 在平面区域上的累积运算 |
| 三重积分 | Triple integral | ∭_V f(x,y,z)dV | 在空间区域上的累积运算 |
| 重积分 | Multiple integral | — | 对多维区域的积分统称 |
| 积分区域 | Region of integration | D, V | 多重积分覆盖的区域 |
| 累次积分 | Iterated integral | ∫∫ f dxdy | 按多个一维积分依次计算 |
| 富比尼定理 | Fubini's theorem | — | 在相应条件下交换积分次序 |
| 托内利定理 | Tonelli's theorem | — | 非负可测函数可交换积分次序（扩展内容） |
| 积分次序交换 | Changing the order of integration | — | 更换多重积分计算顺序 |
| 极坐标变换 | Polar coordinate transformation | x=r cosθ, y=r sinθ | 二维区域积分的坐标替换 |
| 柱坐标 | Cylindrical coordinates | (r, θ, z) | 以极坐标和高度描述空间点 |
| 球坐标 | Spherical coordinates | (ρ, θ, φ) | 以径向距离和角度描述空间点 |
| 变量替换公式 | Change of variables formula | — | 用雅可比行列式变换积分元 |
| 雅可比因子 | Jacobian factor | abs(det J) | 积分换元时的局部面积或体积伸缩因子 |
| 面积元素 | Area element | dA | 平面区域的微小面积 |
| 体积元素 | Volume element | dV | 空间区域的微小体积 |
| 极坐标面积元素 | Area element in polar coordinates | dA=r dr dθ | 极坐标下的面积微元 |
| 柱坐标体积元素 | Volume element in cylindrical coordinates | dV=r dr dθ dz | 柱坐标下的体积微元 |
| 球坐标体积元素 | Volume element in spherical coordinates | dV=ρ² sinφ dρ dφ dθ | 球坐标下的体积微元（φ 为极角） |
| 质量密度 | Mass density | ρ(x,y,z) | 单位长度、面积或体积的质量分布 |
| 重心 | Center of gravity | — | 重力近似均匀时与质心相同 |

## 14. 向量微积分

*Vector Calculus · 27 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 向量场 | Vector field | F: ℝⁿ→ℝⁿ | 为区域中每一点指定向量 |
| 标量场 | Scalar field | f: ℝⁿ→ℝ | 为区域中每一点指定标量 |
| 位置向量 | Position vector | r(t) | 描述空间点位置的向量 |
| 向量值函数 | Vector-valued function | r(t) | 输出为向量的函数 |
| 参数曲线 | Parametric curve | r(t) | 由参数描绘的曲线 |
| 光滑曲线 | Smooth curve | — | 具有足够连续导数且通常无退化切向的曲线 |
| 曲线积分 | Line integral | ∫_C f ds / ∫_C F·dr | 沿一条曲线积分 |
| 第一类曲线积分 | Scalar line integral | ∫_C f ds | 对标量场按弧长积分 |
| 第二类曲线积分 | Vector line integral | ∫_C F·dr | 沿有向曲线计算向量场做功 |
| 路径积分 | Path integral | — | 常指沿路径的积分；在数学与物理中语义略有区别 |
| 曲面积分 | Surface integral | ∬_S f dS | 在曲面上的积分 |
| 第一类曲面积分 | Scalar surface integral | ∬_S f dS | 标量函数的曲面积分 |
| 通量积分 | Flux integral | ∬_S F·n dS | 向量场穿过有向曲面的净通量 |
| 环流 | Circulation | ∮_C F·dr | 沿闭合曲线的向量场线积分 |
| 通量 | Flux | Φ | 穿过指定曲面的流量类量 |
| 散度 | Divergence | ∇·F | 描述向量场局部发散强度的标量 |
| 旋度 | Curl | ∇×F | 描述三维向量场局部旋转的向量 |
| 拉普拉斯算子 | Laplacian | ∇²f / Δf | 梯度的散度 |
| 哈密顿算子 | Nabla operator | ∇ | 梯度、散度和旋度所用的微分算子 |
| 保守向量场 | Conservative vector field | F=∇φ | 可表示为标量势梯度的向量场 |
| 势函数 | Potential function | φ | 其梯度给出保守向量场的标量函数 |
| 路径无关性 | Path independence | — | 线积分仅由起点和终点决定 |
| 格林公式 | Green's theorem | — | 联系平面闭曲线积分与区域二重积分 |
| 高斯散度定理 | Divergence theorem / Gauss's theorem | — | 联系封闭曲面通量与体积分中的散度 |
| 斯托克斯定理 | Stokes' theorem | — | 联系边界环流与曲面旋度通量 |
| 定向曲面 | Oriented surface | — | 指定连续单位法向选择的曲面 |
| 外法向量 | Outward unit normal | n | 封闭曲面朝外的单位法向量 |

## 15. 常微分方程入门

*Ordinary Differential Equations · 18 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 微分方程 | Differential equation | — | 包含未知函数及其导数的方程 |
| 常微分方程 | Ordinary differential equation | ODE | 未知函数关于单个自变量的微分方程 |
| 偏微分方程 | Partial differential equation | PDE | 包含多变量未知函数偏导数的方程 |
| 方程阶数 | Order of a differential equation | — | 方程中出现的最高阶导数的阶数 |
| 通解 | General solution | — | 包含任意常数的解族（在线性等常见情形） |
| 特解 | Particular solution | — | 满足附加条件的某个具体解 |
| 初值问题 | Initial value problem | IVP | 给出某个初始点处数据的微分方程问题 |
| 边值问题 | Boundary value problem | BVP | 给出边界处约束的微分方程问题 |
| 可分离变量方程 | Separable differential equation | dy/dx=g(x)h(y) | 可将变量分离到方程两侧 |
| 一阶线性微分方程 | First-order linear ODE | y′+p(x)y=q(x) | 未知函数及一阶导数线性出现 |
| 积分因子 | Integrating factor | μ(x) | 将线性方程转为可直接积分的形式 |
| 齐次线性微分方程 | Homogeneous linear ODE | L[y]=0 | 线性微分方程右端为零 |
| 非齐次线性微分方程 | Nonhomogeneous linear ODE | L[y]=g(x) | 线性微分方程含非零外部项 |
| 特征方程 | Characteristic equation | p(λ)=0 | 求解常系数线性方程时的代数方程 |
| 欧拉法 | Euler's method | yₙ₊₁=yₙ+h f(xₙ,yₙ) | 基于切线斜率的数值方法 |
| 改进欧拉法 | Improved Euler method | — | 利用预测校正或梯形思想提高精度 |
| 龙格–库塔法 | Runge–Kutta method | RK | 通过多个斜率估计推进数值解 |
| 存在唯一性定理 | Existence and uniqueness theorem | — | 描述初值问题何时存在唯一局部解 |

## 16. 常用数学记号与英文表达

*Notation & Academic English · 26 terms*

| 中文术语 | English term | 常用符号 / 示例 | 简要释义 |
|---|---|---|---|
| 趋于 | Tends to / approaches | x→a | 描述极限过程 |
| 无穷大 | Infinity | ∞ | 不表示一个普通实数 |
| 求和 | Summation | Σ | 对离散项求和 |
| 乘积记号 | Product notation | Π | 对离散项连乘 |
| 偏导符号 | Partial derivative symbol | ∂ | 用于多元偏导数 |
| 微分算子 | Differential operator | d/dx | 作用于函数以求导 |
| 增量符号 | Delta | Δ | 表示有限变化或差分 |
| 趋近符号 | Asymptotically equivalent to | ∼ | 在此术语表中主要用于渐近等价 |
| 约等于 | Approximately equal to | ≈ | 近似相等 |
| 恒等于 | Identically equal to | ≡ | 恒等关系或同余，依语境区分 |
| 属于 | Element of | ∈ | 集合成员关系 |
| 包含于 | Subset of | ⊆ | 集合包含关系 |
| 实数集 | Set of real numbers | ℝ | 所有实数的集合 |
| 自然数集 | Set of natural numbers | ℕ | 自然数的集合（是否含零依约定） |
| n 维欧氏空间 | n-dimensional Euclidean space | ℝⁿ | 实向量组成的 n 维空间 |
| 闭区间 | Closed interval | [a,b] | 包含左右端点的区间 |
| 开区间 | Open interval | (a,b) | 不包含左右端点的区间 |
| 邻域 | Neighborhood | — | 包含目标点的某个开集合 |
| 开集 | Open set | — | 每个点都具有包含于该集合的邻域 |
| 闭集 | Closed set | — | 补集为开集的集合 |
| 上确界 | Supremum | sup | 所有上界中的最小者 |
| 下确界 | Infimum | inf | 所有下界中的最大者 |
| 充分条件 | Sufficient condition | — | 足以推出结论的条件 |
| 必要条件 | Necessary condition | — | 结论成立所必需的条件 |
| 充分必要条件 | Necessary and sufficient condition | iff / ⇔ | 两个命题等价 |
| 几乎处处 | Almost everywhere | a.e. | 除一个零测集外均成立（扩展内容） |

## 编纂说明

本文用于术语速查、英文文献阅读和基础教学；非公理化教材。中文译名可能存在地区差异。

欢迎在 GitHub 提交术语修订、英文变体与出处。