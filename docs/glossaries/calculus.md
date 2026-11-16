# 微积分 · Calculus

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：361 条 · 专题：16 类**

Limits, derivatives, integrals, series, multivariable and vector calculus

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与函数（24 条）
- 02. 极限与连续性（27 条）
- 03. 导数与微分（27 条）
- 04. 微分定理与函数分析（27 条）
- 05. 不定积分与积分技巧（20 条）
- 06. 定积分与积分基本定理（22 条）
- 07. 反常积分与数值积分（20 条）
- 08. 积分的几何与物理应用（16 条）
- 09. 无穷数列与级数（24 条）
- 10. 幂级数与函数展开（20 条）
- 11. 多元函数与偏导数（25 条）
- 12. 多元最优化与隐函数（18 条）
- 13. 重积分与坐标变换（20 条）
- 14. 向量微积分（27 条）
- 15. 常微分方程入门（18 条）
- 16. 常用数学记号与英文表达（26 条）

---

## 01. 基础概念与函数

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Calculus | 微积分 | — | 研究变化率、累积量及其联系的数学分支 |
| 2 | Differential calculus | 微分学 | — | 主要研究导数及局部变化 |
| 3 | Integral calculus | 积分学 | — | 主要研究累积、面积和积分 |
| 4 | Function | 函数 | f: A → B | 将定义域中的元素映射到值域中的元素 |
| 5 | Independent variable | 自变量 | x | 函数的输入变量 |
| 6 | Dependent variable | 因变量 | y = f(x) | 随自变量变化的输出变量 |
| 7 | Domain | 定义域 | dom(f) | 函数允许的输入集合 |
| 8 | Codomain | 陪域 | B | 函数声明的目标集合 |
| 9 | Range / image | 值域 | f(A) | 函数实际取得的输出集合 |
| 10 | Graph of a function | 函数图像 | y = f(x) | 函数输入与输出的几何表示 |
| 11 | Composite function | 复合函数 | f ∘ g | 由多个函数依次作用形成 |
| 12 | Inverse function | 反函数 | f⁻¹ | 在适当条件下撤销原函数映射 |
| 13 | Piecewise-defined function | 分段函数 | — | 在不同区间采用不同表达式 |
| 14 | Even function | 偶函数 | f(−x)=f(x) | 关于纵轴对称的函数 |
| 15 | Odd function | 奇函数 | f(−x)=−f(x) | 关于原点对称的函数 |
| 16 | Periodic function | 周期函数 | f(x+T)=f(x) | 按固定周期重复函数值 |
| 17 | Monotonically increasing | 单调递增 | — | 自变量增加时函数值不下降 |
| 18 | Strictly increasing | 严格递增 | — | 自变量增加时函数值严格增大 |
| 19 | Bounded function | 有界函数 | — | 函数值落在有限界限内 |
| 20 | Continuous function | 连续函数 | — | 在所论点或区间上满足连续性 |
| 21 | Elementary function | 初等函数 | — | 由常用基本函数经有限次运算与复合得到 |
| 22 | Parametric equation | 参数方程 | x=x(t), y=y(t) | 以参数表示曲线坐标 |
| 23 | Polar coordinates | 极坐标 | (r, θ) | 通过半径与角度描述平面位置 |
| 24 | Radian | 弧度 | rad | 以弧长与半径之比定义的角度单位 |

## 02. 极限与连续性

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Limit | 极限 | lim | 描述变量接近某点时的趋近值 |
| 2 | Limit of a function | 函数极限 | limₓ→ₐ f(x) | 函数在自变量趋近时的变化趋势 |
| 3 | Limit of a sequence | 数列极限 | limₙ→∞ aₙ | 描述数列项的渐近行为 |
| 4 | Left-hand limit | 左极限 | limₓ→ₐ⁻ | 从左侧趋向指定点的极限 |
| 5 | Right-hand limit | 右极限 | limₓ→ₐ⁺ | 从右侧趋向指定点的极限 |
| 6 | Infinite limit | 无穷极限 | ∞ / −∞ | 函数值向正或负无穷增大 |
| 7 | Limit at infinity | 无穷远处的极限 | limₓ→∞ | 当自变量绝对值增大时考察极限 |
| 8 | One-sided limit | 单侧极限 | — | 从某一侧靠近点时的极限 |
| 9 | Infinitesimal | 无穷小量 | — | 在给定极限过程中趋于零的量 |
| 10 | Infinitely large quantity | 无穷大量 | — | 在给定极限过程中绝对值趋于无穷的量 |
| 11 | Asymptotically equivalent infinitesimals | 等价无穷小 | f ∼ g | 两量之比趋于 1 |
| 12 | Higher-order infinitesimal | 高阶无穷小 | f=o(g) | 相对另一无穷小收敛得更快 |
| 13 | Little-o notation | 小 o 记号 | o(g) | 描述可忽略的相对阶 |
| 14 | Big-O notation | 大 O 记号 | O(g) | 描述渐近量级上界 |
| 15 | Squeeze theorem / sandwich theorem | 夹逼定理 | — | 用上下界共同极限确定目标极限 |
| 16 | Epsilon-delta definition | ε–δ 定义 | ε, δ | 函数极限的严格定义方式 |
| 17 | Epsilon-N definition | ε–N 定义 | ε, N | 数列极限的严格定义方式 |
| 18 | Continuity | 连续性 | — | 极限值等于函数在该点的值 |
| 19 | Left continuity | 左连续 | — | 左极限等于函数值 |
| 20 | Right continuity | 右连续 | — | 右极限等于函数值 |
| 21 | Point of discontinuity | 间断点 | — | 函数不连续的位置 |
| 22 | Removable discontinuity | 可去间断点 | — | 重新定义函数值后可使其连续 |
| 23 | Jump discontinuity | 跳跃间断点 | — | 左右极限有限但不相等 |
| 24 | Intermediate value theorem | 介值定理 | IVT | 连续函数取得端点函数值之间的所有值 |
| 25 | Extreme value theorem | 最值定理 | EVT | 闭区间上连续函数达到最大最小值 |
| 26 | Sequential criterion for limits | 海涅定理 | — | 通过任意趋近点的数列刻画函数极限 |
| 27 | Cauchy criterion | 柯西收敛准则 | — | 通过项间距离刻画收敛 |

## 03. 导数与微分

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Derivative | 导数 | f′(x) | 函数在一点的瞬时变化率 |
| 2 | Derivative function | 导函数 | f′ | 把每一点映射到其导数的函数 |
| 3 | Definition of derivative | 导数定义 | limₕ→₀ [f(x+h)−f(x)]/h | 差商的极限 |
| 4 | Difference quotient | 差商 | Δy/Δx | 函数增量与自变量增量的比 |
| 5 | Increment | 增量 | Δx, Δy | 变量发生的变化量 |
| 6 | Tangent line | 切线 | — | 在可导点与曲线一阶贴合的直线 |
| 7 | Slope of tangent line | 切线斜率 | f′(x₀) | 切线的斜率 |
| 8 | Differential | 微分 | dy=f′(x)dx | 函数的线性主部变化 |
| 9 | Differentiability | 可导性 | — | 导数存在的性质 |
| 10 | Left-hand derivative | 左导数 | f′₋(x) | 从左侧差商得到的导数 |
| 11 | Right-hand derivative | 右导数 | f′₊(x) | 从右侧差商得到的导数 |
| 12 | First derivative | 一阶导数 | f′(x) | 函数的第一次求导结果 |
| 13 | Second derivative | 二阶导数 | f″(x) | 导数的导数 |
| 14 | Higher-order derivative | 高阶导数 | f⁽ⁿ⁾(x) | 重复求导得到的导数 |
| 15 | Leibniz notation | 莱布尼茨导数记号 | dy/dx | 用微分符号表示导数 |
| 16 | Lagrange notation | 拉格朗日导数记号 | f′(x) | 用撇号表示导数 |
| 17 | Newton's notation | 牛顿导数记号 | ẋ, ẍ | 常用于对时间求导 |
| 18 | Chain rule | 链式法则 | (f∘g)′=(f′∘g)g′ | 复合函数求导法则 |
| 19 | Product rule | 乘积法则 | (fg)′=f′g+fg′ | 两个函数乘积的求导法则 |
| 20 | Quotient rule | 商法则 | (f/g)′=(f′g−fg′)/g² | 两个函数商的求导法则 |
| 21 | Power rule | 幂函数求导法则 | d(xⁿ)/dx=nxⁿ⁻¹ | 幂函数的基本求导公式 |
| 22 | Implicit differentiation | 隐函数求导 | — | 对隐式方程两边求导 |
| 23 | Logarithmic differentiation | 对数求导法 | — | 先取对数再求导以简化乘幂关系 |
| 24 | Parametric differentiation | 参数方程求导 | dy/dx=(dy/dt)/(dx/dt) | 按参数求导再取比值 |
| 25 | Inverse function differentiation | 反函数求导 | — | 依据原函数导数计算反函数导数 |
| 26 | Linear approximation | 线性近似 | f(a)+f′(a)(x−a) | 用切线近似函数 |
| 27 | Local linearization | 局部线性化 | — | 用一阶线性模型刻画局部行为 |

## 04. 微分定理与函数分析

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Fermat's theorem on stationary points | 费马引理 | — | 可导函数在内点极值处导数为零 |
| 2 | Rolle's theorem | 罗尔定理 | — | 端点函数值相等时存在导数为零的内点 |
| 3 | Mean value theorem | 拉格朗日中值定理 | MVT | 某内点导数等于区间平均变化率 |
| 4 | Cauchy's mean value theorem | 柯西中值定理 | — | 将中值定理推广到两函数 |
| 5 | L'Hôpital's rule | 洛必达法则 | — | 在适当条件下用导数比求未定式极限 |
| 6 | Taylor's theorem | 泰勒定理 | — | 用多项式及余项近似光滑函数 |
| 7 | Taylor polynomial | 泰勒多项式 | Tₙ(x) | 某点附近的有限阶多项式近似 |
| 8 | Maclaurin polynomial | 麦克劳林多项式 | Tₙ at 0 | 在零点展开的泰勒多项式 |
| 9 | Peano form of remainder | 佩亚诺余项 | o((x−a)ⁿ) | 泰勒公式的渐近余项 |
| 10 | Lagrange form of remainder | 拉格朗日余项 | — | 以高阶导数表达的泰勒余项 |
| 11 | Stationary point | 驻点 | f′(x)=0 | 一阶导数为零的点 |
| 12 | Critical point | 临界点 | — | 定义域内导数为零或不存在的内点 |
| 13 | Local maximum | 局部极大值 | — | 邻域内不小于周围函数值 |
| 14 | Local minimum | 局部极小值 | — | 邻域内不大于周围函数值 |
| 15 | Global maximum | 全局最大值 | — | 定义域内的最大函数值 |
| 16 | Global minimum | 全局最小值 | — | 定义域内的最小函数值 |
| 17 | First derivative test | 一阶导数判别法 | — | 依据导数符号变化判断极值 |
| 18 | Second derivative test | 二阶导数判别法 | — | 通过二阶导数符号分析驻点 |
| 19 | Convex function | 凸函数 | — | 函数图像位于任意弦下方或弦上 |
| 20 | Concave function | 凹函数 | — | 函数图像位于任意弦上方或弦下方 |
| 21 | Inflection point | 拐点 | — | 曲线凹凸性发生变化的点 |
| 22 | Curvature | 曲率 | κ | 刻画曲线弯曲程度的量 |
| 23 | Asymptote | 渐近线 | — | 曲线逐渐接近的直线 |
| 24 | Horizontal asymptote | 水平渐近线 | y=L | 趋向无穷远时接近的水平直线 |
| 25 | Vertical asymptote | 垂直渐近线 | x=a | 靠近该直线时函数值趋于无穷 |
| 26 | Oblique asymptote | 斜渐近线 | y=mx+b | 无穷远处接近的非水平直线 |
| 27 | Optimization | 最优化 | — | 寻找目标函数的极值 |

## 05. 不定积分与积分技巧

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Antiderivative | 原函数 | F′=f | 导数等于给定函数的函数 |
| 2 | Indefinite integral | 不定积分 | ∫f(x)dx | 函数所有原函数的族 |
| 3 | Constant of integration | 积分常数 | C | 不定积分中的任意常数 |
| 4 | Variable of integration | 积分变量 | x | 积分运算所对应的变量 |
| 5 | Integrand | 被积函数 | f(x) | 积分号内部被积的函数 |
| 6 | Integral sign | 积分号 | ∫ | 表示积分运算的符号 |
| 7 | Differential element | 积分微元 | dx | 积分表达式中的微分记号 |
| 8 | Basic integration formulas | 基本积分公式 | — | 常见函数的原函数公式 |
| 9 | Integration by substitution | 换元积分法 | u=g(x) | 通过变量替换简化积分 |
| 10 | Substitution method | 第一类换元法 | — | 利用复合函数形式进行换元 |
| 11 | Change-of-variable method | 第二类换元法 | x=φ(t) | 显式引入新变量进行换元 |
| 12 | Integration by parts | 分部积分法 | ∫u dv=uv−∫v du | 由乘积法则导出的积分方法 |
| 13 | Integration of rational functions | 有理函数积分 | — | 有理函数的积分计算 |
| 14 | Partial fraction decomposition | 部分分式分解 | — | 将有理式拆为简单分式之和 |
| 15 | Trigonometric substitution | 三角代换 | — | 利用三角恒等式简化根式积分 |
| 16 | Trigonometric identities | 三角恒等变换 | — | 用三角公式转化被积函数 |
| 17 | Tangent half-angle substitution | 万能代换 | t=tan(x/2) | 把部分三角积分转为有理函数积分 |
| 18 | Reduction formula | 递推积分公式 | — | 将某类积分化为较低阶积分 |
| 19 | Non-elementary antiderivative | 不可用初等函数表示的原函数 | — | 不能写为有限个初等函数组合的原函数 |
| 20 | Error function | 误差函数 | erf(x) | 高斯函数积分相关的特殊函数 |

## 06. 定积分与积分基本定理

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Definite integral | 定积分 | ∫ₐᵇ f(x)dx | 区间上函数的有符号累积量 |
| 2 | Interval of integration | 积分区间 | [a,b] | 定积分的自变量范围 |
| 3 | Upper limit of integration | 积分上限 | b | 定积分区间右端点 |
| 4 | Lower limit of integration | 积分下限 | a | 定积分区间左端点 |
| 5 | Riemann sum | 黎曼和 | Σf(ξᵢ)Δxᵢ | 用小区间加权和近似积分 |
| 6 | Riemann integral | 黎曼积分 | — | 用分割和的极限定义的积分 |
| 7 | Riemann integrable | 黎曼可积 | — | 黎曼和极限存在且与取样一致 |
| 8 | Partition | 分割 | P={x₀,…,xₙ} | 把区间划分为若干小区间 |
| 9 | Mesh size of a partition | 分割网格大小 | ‖P‖ | 分割中最长小区间的长度 |
| 10 | Upper Darboux sum | 上和 | U(f,P) | 各小区间上确界构成的和 |
| 11 | Lower Darboux sum | 下和 | L(f,P) | 各小区间下确界构成的和 |
| 12 | Darboux integral | 达布积分 | — | 以达布上、下和定义积分 |
| 13 | Mean value theorem for integrals | 积分中值定理 | — | 连续函数的积分等于区间长度乘某函数值 |
| 14 | Fundamental theorem of calculus | 微积分基本定理 | FTC | 建立求导与定积分之间的关系 |
| 15 | Integral with variable upper limit | 变上限积分 | F(x)=∫ₐˣ f(t)dt | 上限变化产生的累积函数 |
| 16 | Newton–Leibniz formula | 牛顿–莱布尼茨公式 | ∫ₐᵇ f=F(b)−F(a) | 使用原函数计算定积分 |
| 17 | Linearity of integration | 积分的线性性 | — | 积分与线性组合交换 |
| 18 | Additivity of definite integrals | 积分可加性 | — | 积分可按区间拆分相加 |
| 19 | Comparison theorem for integrals | 积分比较定理 | — | 点态不等式在积分下保持序关系 |
| 20 | Integral estimation | 积分估计 | — | 用上界和下界估算积分值 |
| 21 | Differentiation of integral with variable limits | 变限积分求导 | — | 对上下限含变量的积分求导 |
| 22 | Leibniz integral rule | 莱布尼茨积分法则 | — | 适当条件下对含参数的积分求导 |

## 07. 反常积分与数值积分

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Improper integral | 反常积分 | — | 无限区间或无界被积函数上的积分 |
| 2 | Integral over an infinite interval | 无穷区间积分 | ∫ₐ^∞ f(x)dx | 积分区间延伸到无穷 |
| 3 | Improper integral with singularity | 瑕积分 | — | 被积函数在积分端点或内部无界 |
| 4 | Convergence of improper integrals | 反常积分收敛 | — | 相关极限存在且有限 |
| 5 | Absolute convergence | 绝对收敛 | ∫∣f∣<∞ | 绝对值的反常积分收敛 |
| 6 | Conditional convergence | 条件收敛 | — | 原积分收敛但绝对积分不收敛 |
| 7 | Comparison test | 比较判别法 | — | 通过正函数大小比较判断收敛性 |
| 8 | Limit comparison test | 极限比较判别法 | — | 用函数比值的极限判断收敛 |
| 9 | Cauchy principal value | 柯西主值 | PV∫ | 以对称方式取极限的积分值 |
| 10 | Gamma function | 伽马函数 | Γ(s) | 阶乘向实数或复数的推广 |
| 11 | Beta function | 贝塔函数 | B(p,q) | 与伽马函数相关的特殊积分 |
| 12 | Numerical integration / quadrature | 数值积分 | — | 用数值方法近似计算定积分 |
| 13 | Quadrature rule | 求积公式 | — | 使用加权函数值近似积分 |
| 14 | Trapezoidal rule | 梯形法则 | — | 以梯形面积近似曲线下面积 |
| 15 | Simpson's rule | 辛普森法则 | — | 以二次插值近似积分 |
| 16 | Composite trapezoidal rule | 复化梯形公式 | — | 分段应用梯形公式 |
| 17 | Composite Simpson's rule | 复化辛普森公式 | — | 分段应用辛普森公式 |
| 18 | Gaussian quadrature | 高斯求积 | — | 选择节点与权重提高积分精度 |
| 19 | Adaptive quadrature | 自适应求积 | — | 依据误差估计细化积分区间 |
| 20 | Truncation error | 截断误差 | — | 近似公式与精确目标之间的误差 |

## 08. 积分的几何与物理应用

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Area under a curve | 曲线下面积 | — | 函数与坐标轴之间的几何面积 |
| 2 | Area between curves | 曲线间面积 | — | 两条曲线围成区域的面积 |
| 3 | Volume of a solid of revolution | 旋转体体积 | — | 平面区域绕直线旋转得到的体积 |
| 4 | Disk method | 圆盘法 | — | 通过圆盘横截面积计算体积 |
| 5 | Washer method | 垫片法 | — | 通过圆环横截面积计算体积 |
| 6 | Cylindrical shell method | 柱壳法 | — | 通过薄柱壳累加计算体积 |
| 7 | Method of cross sections | 截面法 | — | 通过截面积积分求体积 |
| 8 | Arc length | 弧长 | s | 曲线的长度 |
| 9 | Surface area | 曲面面积 | A | 二维曲面在三维空间中的面积 |
| 10 | Surface area of revolution | 旋转曲面面积 | — | 曲线旋转形成曲面的面积 |
| 11 | Center of mass | 质心 | — | 按质量分布确定的平均位置 |
| 12 | Centroid | 形心 | — | 几何区域的均匀密度中心 |
| 13 | Moment of inertia | 转动惯量 | I | 质量相对于转轴分布的二次矩 |
| 14 | Work | 功 | W=∫F·ds | 力沿位移的累积作用 |
| 15 | Average value of a function | 平均值 | [1/(b−a)]∫ₐᵇ f | 函数在区间内的积分平均 |
| 16 | Net change | 累积变化量 | ∫ₐᵇ f′(x)dx | 变化率积分得到的净变化 |

## 09. 无穷数列与级数

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Infinite sequence | 无穷数列 | (aₙ) | 按自然数索引的数列 |
| 2 | Monotone sequence | 单调数列 | — | 各项按同一方向变化 |
| 3 | Bounded sequence | 有界数列 | — | 所有项落在某有界区间 |
| 4 | Monotone convergence theorem (sequences) | 单调收敛定理 | — | 单调且有界的实数数列必收敛 |
| 5 | Subsequence | 子列 | (aₙₖ) | 从原数列按递增索引抽取的数列 |
| 6 | Cluster point / accumulation point | 聚点 | — | 可由数列子列趋近的点或集合的聚集点 |
| 7 | Limit superior | 上极限 | lim sup | 数列尾部上界的渐近极限 |
| 8 | Limit inferior | 下极限 | lim inf | 数列尾部下界的渐近极限 |
| 9 | Infinite series | 无穷级数 | Σaₙ | 无穷多个项的形式和 |
| 10 | Partial sum | 部分和 | Sₙ=Σₖ₌₁ⁿaₖ | 级数前 n 项的和 |
| 11 | Series convergence | 级数收敛 | — | 部分和数列存在有限极限 |
| 12 | Series divergence | 级数发散 | — | 部分和数列不收敛到有限值 |
| 13 | Geometric series | 几何级数 | Σarⁿ | 公比固定的级数 |
| 14 | Harmonic series | 调和级数 | Σ1/n | 著名的发散正项级数 |
| 15 | p-series | p 级数 | Σ1/nᵖ | 以指数 p 判断收敛的标准级数 |
| 16 | Alternating series | 交错级数 | Σ(−1)ⁿaₙ | 正负项交替的级数 |
| 17 | Alternating series test | 莱布尼茨判别法 | — | 判断特定交错级数收敛的准则 |
| 18 | Ratio test | 比值判别法 | — | 通过相邻项比值判断绝对收敛 |
| 19 | Root test | 根值判别法 | — | 通过项绝对值 n 次根判断收敛 |
| 20 | Integral test | 积分判别法 | — | 用正函数反常积分判断对应级数 |
| 21 | Comparison test for series | 比较判别法（级数） | — | 与已知正项级数比较 |
| 22 | Dirichlet's test | 狄利克雷判别法 | — | 基于部分和有界与因子趋零的判别法 |
| 23 | Abel's test | 阿贝尔判别法 | — | 基于级数收敛与因子单调有界的判别法 |
| 24 | Rearrangement of a series | 重排 | — | 改变级数各项的排列顺序 |

## 10. 幂级数与函数展开

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Series of functions | 函数项级数 | Σfₙ(x) | 各项本身为函数的级数 |
| 2 | Power series | 幂级数 | Σaₙ(x−c)ⁿ | 围绕中心 c 的幂函数级数 |
| 3 | Center of convergence | 收敛中心 | c | 幂级数展开的中心点 |
| 4 | Radius of convergence | 收敛半径 | R | 幂级数保证绝对收敛的半径 |
| 5 | Interval of convergence | 收敛区间 | — | 实变量幂级数的收敛 x 范围 |
| 6 | Pointwise convergence | 逐点收敛 | — | 对每个固定点函数项序列收敛 |
| 7 | Uniform convergence | 一致收敛 | — | 收敛速度可以与点的选择无关 |
| 8 | Weierstrass M-test | 一致收敛判别法 | M-test | 用可求和上界判别一致收敛 |
| 9 | Term-by-term differentiation | 逐项求导 | — | 在适当条件下交换求导与求和 |
| 10 | Term-by-term integration | 逐项积分 | — | 在适当条件下交换积分与求和 |
| 11 | Taylor series | 泰勒级数 | Σf⁽ⁿ⁾(a)(x−a)ⁿ/n! | 用各阶导数构造的幂级数 |
| 12 | Maclaurin series | 麦克劳林级数 | Taylor series at 0 | 以零为展开中心的泰勒级数 |
| 13 | Taylor expansion | 泰勒展开 | — | 函数在某点附近的多项式或级数展开 |
| 14 | Analytic function | 解析函数 | — | 局部可由收敛幂级数表示的函数 |
| 15 | Remainder term | 余项 | Rₙ(x) | 截断展开后剩余的部分 |
| 16 | Endpoint of convergence | 收敛端点 | c±R | 幂级数收敛区间的候选端点 |
| 17 | Binomial series | 二项式级数 | — | 广义二项式函数的幂级数展开 |
| 18 | Fourier series | 傅里叶级数 | Σ(aₙcos nx+bₙsin nx) | 用正弦和余弦展开周期函数 |
| 19 | Fourier coefficients | 傅里叶系数 | aₙ, bₙ | 傅里叶展开中的权重 |
| 20 | Orthogonality | 正交性 | — | 内积为零的性质 |

## 11. 多元函数与偏导数

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Multivariable function | 多元函数 | f(x₁,…,xₙ) | 输入由多个变量组成的函数 |
| 2 | Function of two variables | 二元函数 | f(x,y) | 输入由两个变量组成的函数 |
| 3 | Domain (multivariable) | 定义域（多元） | D⊆ℝⁿ | 多元函数的输入点集合 |
| 4 | Level curve | 等值线 | f(x,y)=c | 二维函数具有相同函数值的点集 |
| 5 | Level surface | 等值面 | f(x,y,z)=c | 三维函数具有相同函数值的曲面 |
| 6 | Contour plot | 等高线图 | — | 在平面上显示各等值线的图形 |
| 7 | Partial derivative | 偏导数 | ∂f/∂x | 保持其他自变量不变的变化率 |
| 8 | Partial differential | 偏微分 | ∂f/∂x · dx | 与某坐标方向相关的微分项 |
| 9 | Second partial derivative | 二阶偏导数 | ∂²f/∂x² | 对某变量重复求偏导 |
| 10 | Mixed partial derivative | 混合偏导数 | ∂²f/∂x∂y | 按不同变量求高阶偏导 |
| 11 | Clairaut's theorem / Schwarz's theorem | 克莱罗定理 | fₓᵧ=fᵧₓ | 在适当连续性条件下混合偏导相等 |
| 12 | Gradient | 梯度 | ∇f | 由各偏导数组成的向量 |
| 13 | Gradient vector | 梯度向量 | grad f | 函数增加最快方向的向量 |
| 14 | Directional derivative | 方向导数 | Dᵤf | 沿指定方向的变化率 |
| 15 | Unit direction vector | 单位方向向量 | ‖u‖=1 | 用于定义方向导数的单位向量 |
| 16 | Total differential | 全微分 | df=Σ(∂f/∂xᵢ)dxᵢ | 多元函数的一阶线性变化量 |
| 17 | Total derivative | 全导数 | df/dt | 沿参数路径的函数变化率 |
| 18 | Total differential formula | 全微分公式 | — | 以偏导数表示一阶变化 |
| 19 | Multivariable chain rule | 多元链式法则 | — | 对多变量复合映射求导的法则 |
| 20 | Jacobian matrix | 雅可比矩阵 | J_f | 向量值函数的一阶偏导数矩阵 |
| 21 | Jacobian determinant | 雅可比行列式 | det J | 方形雅可比矩阵的行列式 |
| 22 | Hessian matrix | 海森矩阵 | H_f | 标量函数的二阶偏导矩阵 |
| 23 | Tangent plane | 切平面 | — | 曲面在一点的一阶线性近似 |
| 24 | Normal vector | 法向量 | n | 与曲面切空间正交的向量 |
| 25 | Differentiability (multivariable) | 可微性（多元） | — | 函数可由线性映射一阶近似的性质 |

## 12. 多元最优化与隐函数

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Partial derivative test | 偏导数判别法 | — | 利用一阶偏导数寻找候选极值点 |
| 2 | Stationary point (multivariable) | 驻点（多元） | ∇f=0 | 梯度为零的点 |
| 3 | Critical point (multivariable) | 临界点（多元） | — | 梯度为零或微分失效等候选点 |
| 4 | Local extremum | 局部极值（多元） | — | 局部邻域内的最大或最小值 |
| 5 | Saddle point | 鞍点 | — | 附近既有更大值也有更小值的驻点 |
| 6 | Positive-definite matrix | 正定矩阵 | vᵀHv>0 | 多元二阶充分条件中的一种矩阵性质 |
| 7 | Second-order sufficient condition | 二阶充分条件 | — | 根据 Hessian 正负定性判断严格局部极值 |
| 8 | Constrained optimization | 约束优化 | — | 在等式或不等式限制下求极值 |
| 9 | Unconstrained optimization | 无约束优化 | — | 不含显式限制条件的优化 |
| 10 | Method of Lagrange multipliers | 拉格朗日乘子法 | ∇f=λ∇g | 用于等式约束下的驻点条件 |
| 11 | Lagrangian | 拉格朗日函数 | L=f−λg | 把目标函数与约束组合为辅助函数 |
| 12 | Lagrange multiplier | 拉格朗日乘子 | λ | 与约束相关的辅助变量 |
| 13 | Implicit function | 隐函数 | F(x,y)=0 | 由关系式局部确定的函数 |
| 14 | Implicit function theorem | 隐函数定理 | IFT | 给出方程局部可解出变量的条件 |
| 15 | Inverse function theorem | 反函数定理 | — | 给出局部可逆和反函数可微的条件 |
| 16 | Multivariable Taylor expansion | 多元泰勒展开 | — | 用梯度和 Hessian 等高阶项作局部近似 |
| 17 | Gradient descent | 梯度下降 | xₖ₊₁=xₖ−η∇f | 沿负梯度更新以降低目标函数 |
| 18 | Newton's method (optimization) | 牛顿法（优化） | — | 结合梯度与 Hessian 寻找驻点 |

## 13. 重积分与坐标变换

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Double integral | 二重积分 | ∬_D f(x,y)dA | 在平面区域上的累积运算 |
| 2 | Triple integral | 三重积分 | ∭_V f(x,y,z)dV | 在空间区域上的累积运算 |
| 3 | Multiple integral | 重积分 | — | 对多维区域的积分统称 |
| 4 | Region of integration | 积分区域 | D, V | 多重积分覆盖的区域 |
| 5 | Iterated integral | 累次积分 | ∫∫ f dxdy | 按多个一维积分依次计算 |
| 6 | Fubini's theorem | 富比尼定理 | — | 在相应条件下交换积分次序 |
| 7 | Tonelli's theorem | 托内利定理 | — | 非负可测函数可交换积分次序（扩展内容） |
| 8 | Changing the order of integration | 积分次序交换 | — | 更换多重积分计算顺序 |
| 9 | Polar coordinate transformation | 极坐标变换 | x=r cosθ, y=r sinθ | 二维区域积分的坐标替换 |
| 10 | Cylindrical coordinates | 柱坐标 | (r, θ, z) | 以极坐标和高度描述空间点 |
| 11 | Spherical coordinates | 球坐标 | (ρ, θ, φ) | 以径向距离和角度描述空间点 |
| 12 | Change of variables formula | 变量替换公式 | — | 用雅可比行列式变换积分元 |
| 13 | Jacobian factor | 雅可比因子 | abs(det J) | 积分换元时的局部面积或体积伸缩因子 |
| 14 | Area element | 面积元素 | dA | 平面区域的微小面积 |
| 15 | Volume element | 体积元素 | dV | 空间区域的微小体积 |
| 16 | Area element in polar coordinates | 极坐标面积元素 | dA=r dr dθ | 极坐标下的面积微元 |
| 17 | Volume element in cylindrical coordinates | 柱坐标体积元素 | dV=r dr dθ dz | 柱坐标下的体积微元 |
| 18 | Volume element in spherical coordinates | 球坐标体积元素 | dV=ρ² sinφ dρ dφ dθ | 球坐标下的体积微元（φ 为极角） |
| 19 | Mass density | 质量密度 | ρ(x,y,z) | 单位长度、面积或体积的质量分布 |
| 20 | Center of gravity | 重心 | — | 重力近似均匀时与质心相同 |

## 14. 向量微积分

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Vector field | 向量场 | F: ℝⁿ→ℝⁿ | 为区域中每一点指定向量 |
| 2 | Scalar field | 标量场 | f: ℝⁿ→ℝ | 为区域中每一点指定标量 |
| 3 | Position vector | 位置向量 | r(t) | 描述空间点位置的向量 |
| 4 | Vector-valued function | 向量值函数 | r(t) | 输出为向量的函数 |
| 5 | Parametric curve | 参数曲线 | r(t) | 由参数描绘的曲线 |
| 6 | Smooth curve | 光滑曲线 | — | 具有足够连续导数且通常无退化切向的曲线 |
| 7 | Line integral | 曲线积分 | ∫_C f ds / ∫_C F·dr | 沿一条曲线积分 |
| 8 | Scalar line integral | 第一类曲线积分 | ∫_C f ds | 对标量场按弧长积分 |
| 9 | Vector line integral | 第二类曲线积分 | ∫_C F·dr | 沿有向曲线计算向量场做功 |
| 10 | Path integral | 路径积分 | — | 常指沿路径的积分；在数学与物理中语义略有区别 |
| 11 | Surface integral | 曲面积分 | ∬_S f dS | 在曲面上的积分 |
| 12 | Scalar surface integral | 第一类曲面积分 | ∬_S f dS | 标量函数的曲面积分 |
| 13 | Flux integral | 通量积分 | ∬_S F·n dS | 向量场穿过有向曲面的净通量 |
| 14 | Circulation | 环流 | ∮_C F·dr | 沿闭合曲线的向量场线积分 |
| 15 | Flux | 通量 | Φ | 穿过指定曲面的流量类量 |
| 16 | Divergence | 散度 | ∇·F | 描述向量场局部发散强度的标量 |
| 17 | Curl | 旋度 | ∇×F | 描述三维向量场局部旋转的向量 |
| 18 | Laplacian | 拉普拉斯算子 | ∇²f / Δf | 梯度的散度 |
| 19 | Nabla operator | 哈密顿算子 | ∇ | 梯度、散度和旋度所用的微分算子 |
| 20 | Conservative vector field | 保守向量场 | F=∇φ | 可表示为标量势梯度的向量场 |
| 21 | Potential function | 势函数 | φ | 其梯度给出保守向量场的标量函数 |
| 22 | Path independence | 路径无关性 | — | 线积分仅由起点和终点决定 |
| 23 | Green's theorem | 格林公式 | — | 联系平面闭曲线积分与区域二重积分 |
| 24 | Divergence theorem / Gauss's theorem | 高斯散度定理 | — | 联系封闭曲面通量与体积分中的散度 |
| 25 | Stokes' theorem | 斯托克斯定理 | — | 联系边界环流与曲面旋度通量 |
| 26 | Oriented surface | 定向曲面 | — | 指定连续单位法向选择的曲面 |
| 27 | Outward unit normal | 外法向量 | n | 封闭曲面朝外的单位法向量 |

## 15. 常微分方程入门

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Differential equation | 微分方程 | — | 包含未知函数及其导数的方程 |
| 2 | Ordinary differential equation | 常微分方程 | ODE | 未知函数关于单个自变量的微分方程 |
| 3 | Partial differential equation | 偏微分方程 | PDE | 包含多变量未知函数偏导数的方程 |
| 4 | Order of a differential equation | 方程阶数 | — | 方程中出现的最高阶导数的阶数 |
| 5 | General solution | 通解 | — | 包含任意常数的解族（在线性等常见情形） |
| 6 | Particular solution | 特解 | — | 满足附加条件的某个具体解 |
| 7 | Initial value problem | 初值问题 | IVP | 给出某个初始点处数据的微分方程问题 |
| 8 | Boundary value problem | 边值问题 | BVP | 给出边界处约束的微分方程问题 |
| 9 | Separable differential equation | 可分离变量方程 | dy/dx=g(x)h(y) | 可将变量分离到方程两侧 |
| 10 | First-order linear ODE | 一阶线性微分方程 | y′+p(x)y=q(x) | 未知函数及一阶导数线性出现 |
| 11 | Integrating factor | 积分因子 | μ(x) | 将线性方程转为可直接积分的形式 |
| 12 | Homogeneous linear ODE | 齐次线性微分方程 | L[y]=0 | 线性微分方程右端为零 |
| 13 | Nonhomogeneous linear ODE | 非齐次线性微分方程 | L[y]=g(x) | 线性微分方程含非零外部项 |
| 14 | Characteristic equation | 特征方程 | p(λ)=0 | 求解常系数线性方程时的代数方程 |
| 15 | Euler's method | 欧拉法 | yₙ₊₁=yₙ+h f(xₙ,yₙ) | 基于切线斜率的数值方法 |
| 16 | Improved Euler method | 改进欧拉法 | — | 利用预测校正或梯形思想提高精度 |
| 17 | Runge–Kutta method | 龙格–库塔法 | RK | 通过多个斜率估计推进数值解 |
| 18 | Existence and uniqueness theorem | 存在唯一性定理 | — | 描述初值问题何时存在唯一局部解 |

## 16. 常用数学记号与英文表达

| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |
|---:|---|---|---|---|
| 1 | Tends to / approaches | 趋于 | x→a | 描述极限过程 |
| 2 | Infinity | 无穷大 | ∞ | 不表示一个普通实数 |
| 3 | Summation | 求和 | Σ | 对离散项求和 |
| 4 | Product notation | 乘积记号 | Π | 对离散项连乘 |
| 5 | Partial derivative symbol | 偏导符号 | ∂ | 用于多元偏导数 |
| 6 | Differential operator | 微分算子 | d/dx | 作用于函数以求导 |
| 7 | Delta | 增量符号 | Δ | 表示有限变化或差分 |
| 8 | Asymptotically equivalent to | 趋近符号 | ∼ | 在此术语表中主要用于渐近等价 |
| 9 | Approximately equal to | 约等于 | ≈ | 近似相等 |
| 10 | Identically equal to | 恒等于 | ≡ | 恒等关系或同余，依语境区分 |
| 11 | Element of | 属于 | ∈ | 集合成员关系 |
| 12 | Subset of | 包含于 | ⊆ | 集合包含关系 |
| 13 | Set of real numbers | 实数集 | ℝ | 所有实数的集合 |
| 14 | Set of natural numbers | 自然数集 | ℕ | 自然数的集合（是否含零依约定） |
| 15 | n-dimensional Euclidean space | n 维欧氏空间 | ℝⁿ | 实向量组成的 n 维空间 |
| 16 | Closed interval | 闭区间 | [a,b] | 包含左右端点的区间 |
| 17 | Open interval | 开区间 | (a,b) | 不包含左右端点的区间 |
| 18 | Neighborhood | 邻域 | — | 包含目标点的某个开集合 |
| 19 | Open set | 开集 | — | 每个点都具有包含于该集合的邻域 |
| 20 | Closed set | 闭集 | — | 补集为开集的集合 |
| 21 | Supremum | 上确界 | sup | 所有上界中的最小者 |
| 22 | Infimum | 下确界 | inf | 所有下界中的最大者 |
| 23 | Sufficient condition | 充分条件 | — | 足以推出结论的条件 |
| 24 | Necessary condition | 必要条件 | — | 结论成立所必需的条件 |
| 25 | Necessary and sufficient condition | 充分必要条件 | iff / ⇔ | 两个命题等价 |
| 26 | Almost everywhere | 几乎处处 | a.e. | 除一个零测集外均成立（扩展内容） |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/calculus.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
