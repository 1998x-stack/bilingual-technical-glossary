# 大学数学 · University Mathematics

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：627 条 · 专题：17 类**

Calculus, mathematical analysis, differential equations, algebra, statistics, geometry and optimization

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 集合、逻辑与数学语言（34 条）
- 02. 函数、极限与连续（40 条）
- 03. 一元微分学（38 条）
- 04. 积分学、无穷级数与幂级数（39 条）
- 05. 多元微积分与向量分析（44 条）
- 06. 线性代数与矩阵论（56 条）
- 07. 概率论与随机变量（43 条）
- 08. 数理统计与数据分析（45 条）
- 09. 常微分方程与动力系统（30 条）
- 10. 复变函数与复分析（32 条）
- 11. 实分析、测度与泛函分析（33 条）
- 12. 抽象代数与数论基础（33 条）
- 13. 几何、拓扑与流形（29 条）
- 14. 数值分析与科学计算（37 条）
- 15. 最优化与运筹学（32 条）
- 16. 离散数学、组合与图论（34 条）
- 17. 偏微分方程与傅里叶分析（28 条）

---

## 01. 集合、逻辑与数学语言

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | set | 集合 |  | 对象组成的整体 |
| 2 | element | 元素 |  | 集合中的一个对象 |
| 3 | subset | 子集 |  | 一个集合包含于另一集合 |
| 4 | proper subset | 真子集 |  | 不等于原集合的子集 |
| 5 | empty set | 空集 |  | 不含任何元素的集合 |
| 6 | universal set | 全集 |  | 讨论范围内的全部元素 |
| 7 | union | 并集 |  | 属于至少一个集合 |
| 8 | intersection | 交集 |  | 同时属于两个集合 |
| 9 | set difference | 差集 |  | 属于前者而不属于后者 |
| 10 | complement | 补集 |  | 全集中不属于该集合 |
| 11 | Cartesian product | 笛卡儿积 |  | 按顺序配对形成的集合 |
| 12 | power set | 幂集 |  | 所有子集构成的集合 |
| 13 | ordered pair | 有序对 |  | 顺序影响对象的二元组 |
| 14 | relation | 关系 |  | 两个集合之间的子集结构 |
| 15 | equivalence relation | 等价关系 |  | 满足自反、对称、传递 |
| 16 | partial order | 偏序关系 |  | 满足自反、反对称、传递 |
| 17 | mapping / map | 映射 |  | 按规则指定对应元素 |
| 18 | domain | 定义域 |  | 映射输入的集合 |
| 19 | codomain | 陪域 |  | 映射规定的目标集合 |
| 20 | image / range | 像集 |  | 实际取得的输出值集合 |
| 21 | preimage | 原像 |  | 映射到给定集合的输入集合 |
| 22 | injective map / injection | 单射 |  | 不同输入对应不同输出 |
| 23 | surjective map / surjection | 满射 |  | 每个陪域元素都有原像 |
| 24 | bijective map / bijection | 双射 |  | 既单射又满射 |
| 25 | inverse map | 逆映射 |  | 双射的反向对应 |
| 26 | proposition | 命题 |  | 可判断真假的陈述 |
| 27 | sufficient condition | 充分条件 |  | 条件成立保证结论成立 |
| 28 | necessary condition | 必要条件 |  | 结论成立需要该条件 |
| 29 | necessary and sufficient condition | 充要条件 |  | 两个方向的蕴含都成立 |
| 30 | universal quantifier | 全称量词 |  | “对所有” |
| 31 | existential quantifier | 存在量词 |  | “存在至少一个” |
| 32 | proof by contradiction | 反证法 |  | 假设结论不成立推出矛盾 |
| 33 | mathematical induction | 数学归纳法 |  | 基例与归纳步骤 |
| 34 | contrapositive | 逆否命题 |  | 与原蕴含命题等价 |

## 02. 函数、极限与连续

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | real number | 实数 |  | 可由实数轴上的点表示 |
| 2 | rational number | 有理数 |  | 可表示为整数之比 |
| 3 | irrational number | 无理数 |  | 不能写成整数之比 |
| 4 | interval | 区间 |  | 实数轴上的连续一段 |
| 5 | open interval | 开区间 |  | 不包含端点 |
| 6 | closed interval | 闭区间 |  | 包含两端点 |
| 7 | upper bound | 上界 |  | 不小于集合中所有元素的数 |
| 8 | lower bound | 下界 |  | 不大于集合中所有元素的数 |
| 9 | supremum / least upper bound | 上确界 |  | 所有上界中的最小者 |
| 10 | infimum / greatest lower bound | 下确界 |  | 所有下界中的最大者 |
| 11 | function | 函数 |  | 每个自变量对应唯一函数值 |
| 12 | composite function | 复合函数 |  | 一个函数作用于另一个函数值 |
| 13 | inverse function | 反函数 |  | 互换自变量与函数值的对应 |
| 14 | odd function | 奇函数 |  | 满足 f(-x)=-f(x) |
| 15 | even function | 偶函数 |  | 满足 f(-x)=f(x) |
| 16 | periodic function | 周期函数 |  | 函数值按固定间隔重复 |
| 17 | nondecreasing / monotonically increasing | 单调不减 |  | 自变量增大时函数值不减 |
| 18 | nonincreasing / monotonically decreasing | 单调不增 |  | 自变量增大时函数值不增 |
| 19 | bounded function | 有界函数 |  | 函数值具有统一上下界 |
| 20 | elementary function | 初等函数 |  | 由基本初等函数有限次组合得到 |
| 21 | exponential function | 指数函数 |  | 自变量出现在指数位置 |
| 22 | logarithmic function | 对数函数 |  | 指数函数的反函数 |
| 23 | inverse trigonometric function | 反三角函数 |  | 适当限定定义域后的三角函数反函数 |
| 24 | sequence | 数列 |  | 按自然数索引的项 |
| 25 | subsequence | 子列 |  | 按严格递增指标抽取的项 |
| 26 | convergence | 收敛 |  | 趋向有限极限 |
| 27 | divergence | 发散 |  | 不收敛到有限值 |
| 28 | limit of a sequence | 数列极限 |  | 项的指标趋于无穷时的极限 |
| 29 | limit of a function | 函数极限 |  | 自变量趋近指定点的极限 |
| 30 | left-hand limit | 左极限 |  | 从左侧趋近 |
| 31 | right-hand limit | 右极限 |  | 从右侧趋近 |
| 32 | infinitesimal | 无穷小量 |  | 极限为零的变量 |
| 33 | infinitely large quantity | 无穷大量 |  | 绝对值趋向无穷的量 |
| 34 | asymptotically equivalent infinitesimals | 等价无穷小 |  | 比值趋于 1 的无穷小 |
| 35 | continuity | 连续性 |  | 函数极限等于该点函数值 |
| 36 | point of discontinuity | 间断点 |  | 不满足连续性的位置 |
| 37 | removable discontinuity | 可去间断点 |  | 补定或重定义函数值可连续 |
| 38 | jump discontinuity | 跳跃间断点 |  | 左右极限有限而不相等 |
| 39 | intermediate value theorem | 介值定理 |  | 连续函数取到端点值之间的各值 |
| 40 | extreme value theorem | 最值定理 |  | 闭区间连续函数可取到最值 |

## 03. 一元微分学

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | derivative | 导数 |  | 函数值变化率的极限 |
| 2 | differentiability | 可导性 |  | 导数存在的性质 |
| 3 | left-hand derivative | 左导数 |  | 由左侧差商求得 |
| 4 | right-hand derivative | 右导数 |  | 由右侧差商求得 |
| 5 | derivative function | 导函数 |  | 将每点导数组成的函数 |
| 6 | differential | 微分 |  | 一阶线性近似量 |
| 7 | differential coefficient | 微分系数 |  | 导数的另一称法 |
| 8 | geometric interpretation of the derivative | 导数的几何意义 |  | 曲线切线斜率 |
| 9 | tangent line | 切线 |  | 局部的一阶逼近直线 |
| 10 | normal line | 法线 |  | 垂直于切线的直线 |
| 11 | product rule | 导数的乘积法则 |  | 乘积求导的规则 |
| 12 | quotient rule | 导数的商法则 |  | 商式求导的规则 |
| 13 | chain rule | 链式法则 |  | 复合函数求导的规则 |
| 14 | implicit differentiation | 隐函数求导 |  | 不显式解出函数而求导 |
| 15 | differentiation of parametric equations | 参数方程求导 |  | 通过参数表示求导数 |
| 16 | logarithmic differentiation | 对数求导法 |  | 先取对数再求导 |
| 17 | higher-order derivative | 高阶导数 |  | 多次求导得到的导数 |
| 18 | second derivative | 二阶导数 |  | 导数的导数 |
| 19 | Rolle's theorem | 罗尔定理 |  | 满足条件时存在导数为零的点 |
| 20 | mean value theorem | 拉格朗日中值定理 |  | 平均变化率等于某点瞬时变化率 |
| 21 | Cauchy's mean value theorem | 柯西中值定理 |  | 两函数的中值定理 |
| 22 | L'Hôpital's rule | 洛必达法则 |  | 特定未定式的极限求法 |
| 23 | Taylor's theorem | 泰勒定理 |  | 用多项式和余项表示局部行为 |
| 24 | Taylor expansion | 泰勒展开 |  | 围绕某点的多项式展开 |
| 25 | Maclaurin expansion | 麦克劳林展开 |  | 在零点处的泰勒展开 |
| 26 | Peano remainder | 佩亚诺余项 |  | 用小 o 表示的余项 |
| 27 | Lagrange remainder | 拉格朗日余项 |  | 含某中间点高阶导数的余项 |
| 28 | stationary point | 驻点 |  | 一阶导数为零的点 |
| 29 | critical point | 临界点 |  | 导数为零或不存在的定义域内点 |
| 30 | local maximum | 局部极大值 |  | 邻域内相对较大的函数值 |
| 31 | local minimum | 局部极小值 |  | 邻域内相对较小的函数值 |
| 32 | concavity | 凹性 |  | 函数图形弯曲性质 |
| 33 | inflection point | 拐点 |  | 凹凸性发生改变的点 |
| 34 | asymptote | 渐近线 |  | 曲线在极限意义下靠近的直线 |
| 35 | curvature | 曲率 |  | 曲线弯曲程度 |
| 36 | radius of curvature | 曲率半径 |  | 曲率非零时的倒数 |
| 37 | linear approximation | 线性近似 |  | 用切线近似函数 |
| 38 | Newton's method | 牛顿法 |  | 利用切线迭代求根 |

## 04. 积分学、无穷级数与幂级数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | antiderivative | 原函数 |  | 导数为原函数对象的函数 |
| 2 | indefinite integral | 不定积分 |  | 所有原函数及积分常数 |
| 3 | definite integral | 定积分 |  | 区间上的极限求和 |
| 4 | constant of integration | 积分常数 |  | 不定积分中的任意常数 |
| 5 | Riemann sum | 黎曼和 |  | 小区间函数值乘区间宽度求和 |
| 6 | Riemann integral | 黎曼积分 |  | 黎曼和极限定义的积分 |
| 7 | fundamental theorem of calculus | 牛顿—莱布尼茨公式 |  | 连接微分与积分 |
| 8 | substitution method | 换元积分法 |  | 通过变量替换计算积分 |
| 9 | integration by parts | 分部积分法 |  | 由乘积求导公式导出 |
| 10 | improper integral | 反常积分 |  | 区间无界或被积函数无界 |
| 11 | generalized integral | 广义积分 |  | 反常积分的常见别名 |
| 12 | integral over an infinite interval | 无穷区间积分 |  | 积分区间至少一端无界 |
| 13 | integral with a singularity | 瑕积分 |  | 被积函数在区间上有无界点 |
| 14 | mean value theorem for integrals | 积分平均值定理 |  | 连续函数积分与某点函数值有关 |
| 15 | fundamental theorem of calculus | 微积分基本定理 |  | 说明积分与导数互逆关系 |
| 16 | integral function with variable upper limit | 积分上限函数 |  | 积分上限为自变量的函数 |
| 17 | area under a curve | 曲边梯形面积 |  | 定积分的几何应用 |
| 18 | volume of a solid of revolution | 旋转体体积 |  | 利用切片或壳层求体积 |
| 19 | arc length | 弧长 |  | 曲线长度 |
| 20 | infinite series | 无穷级数 |  | 数列各项的无穷求和 |
| 21 | partial sum | 部分和 |  | 级数前有限项之和 |
| 22 | convergence of a series | 级数收敛 |  | 部分和序列收敛 |
| 23 | geometric series | 几何级数 |  | 相邻项比值固定的级数 |
| 24 | harmonic series | 调和级数 |  | 倒数 1/n 的级数，发散 |
| 25 | series of nonnegative terms | 正项级数 |  | 各项非负的级数 |
| 26 | comparison test | 比较判别法 |  | 与已知级数比较敛散性 |
| 27 | ratio test | 比值判别法 |  | 考察相邻项绝对值比 |
| 28 | root test | 根值判别法 |  | 考察项绝对值的 n 次方根 |
| 29 | integral test | 积分判别法 |  | 用相应反常积分判别 |
| 30 | alternating series | 交错级数 |  | 正负项交替的级数 |
| 31 | alternating series test | 莱布尼茨判别法 |  | 单调趋零项的交错级数收敛 |
| 32 | absolute convergence | 绝对收敛 |  | 绝对值组成的级数收敛 |
| 33 | conditional convergence | 条件收敛 |  | 级数收敛而非绝对收敛 |
| 34 | power series | 幂级数 |  | 按自变量幂次展开的级数 |
| 35 | radius of convergence | 收敛半径 |  | 幂级数绝对收敛区域的半径 |
| 36 | interval of convergence | 收敛区间 |  | 使幂级数收敛的实数集合 |
| 37 | term-by-term differentiation | 逐项微分 |  | 在适当条件下对级数逐项求导 |
| 38 | term-by-term integration | 逐项积分 |  | 在适当条件下对级数逐项积分 |
| 39 | Fourier series | 傅里叶级数 |  | 用正弦余弦或复指数展开周期函数 |

## 05. 多元微积分与向量分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | multivariable function | 多元函数 |  | 具有两个或更多自变量 |
| 2 | function of two variables | 二元函数 |  | 两个自变量决定函数值 |
| 3 | partial derivative | 偏导数 |  | 固定其余变量求导 |
| 4 | partial differential | 偏微分 |  | 与一个自变量变化有关的微分 |
| 5 | total differential | 全微分 |  | 所有自变量的一阶变化线性和 |
| 6 | total differentiability | 可微性（多元） |  | 存在统一的线性主部 |
| 7 | gradient | 梯度 |  | 由各偏导数组成的向量 |
| 8 | directional derivative | 方向导数 |  | 沿指定方向的变化率 |
| 9 | Jacobian matrix | 雅可比矩阵 |  | 向量值函数的一阶偏导矩阵 |
| 10 | Jacobian determinant | 雅可比行列式 |  | 方形雅可比矩阵的行列式 |
| 11 | Hessian matrix | 海森矩阵 |  | 标量函数的二阶偏导矩阵 |
| 12 | mixed partial derivative | 混合偏导数 |  | 对不同变量依次求偏导 |
| 13 | Clairaut's theorem / Schwarz's theorem | 施瓦茨定理 |  | 条件满足时混合偏导可交换 |
| 14 | tangent plane | 切平面 |  | 曲面在一点的线性近似平面 |
| 15 | normal vector | 法向量 |  | 垂直于切平面的向量 |
| 16 | implicit function theorem | 隐函数定理 |  | 局部从方程组解出变量 |
| 17 | inverse function theorem | 反函数定理 |  | 局部可逆映射的判定定理 |
| 18 | multivariable Taylor expansion | 多元泰勒展开 |  | 多变量函数的局部多项式展开 |
| 19 | double integral | 二重积分 |  | 二维区域上的积分 |
| 20 | triple integral | 三重积分 |  | 三维区域上的积分 |
| 21 | iterated integral | 累次积分 |  | 按变量依次进行积分 |
| 22 | Fubini's theorem | 富比尼定理 |  | 在适当条件下交换积分次序 |
| 23 | polar coordinates | 极坐标 |  | 用半径与角度表示平面位置 |
| 24 | cylindrical coordinates | 柱坐标 |  | 平面极坐标加高度 |
| 25 | spherical coordinates | 球坐标 |  | 用径向距离与两个角定位 |
| 26 | change-of-variables formula | 变量替换公式 |  | 积分变量变换及雅可比因子 |
| 27 | scalar line integral | 第一类曲线积分 |  | 沿曲线对标量场积分 |
| 28 | vector line integral | 第二类曲线积分 |  | 沿曲线积分向量场的切向分量 |
| 29 | scalar surface integral | 第一类曲面积分 |  | 对曲面标量场积分 |
| 30 | flux integral | 第二类曲面积分 |  | 向量场穿过定向曲面的通量 |
| 31 | vector field | 向量场 |  | 每一点对应一个向量 |
| 32 | scalar field | 标量场 |  | 每一点对应一个标量 |
| 33 | divergence | 散度 |  | 描述向量场局部源汇 |
| 34 | curl | 旋度 |  | 描述向量场的局部旋转 |
| 35 | flux | 通量 |  | 向量场穿过面的总效应 |
| 36 | circulation | 环流 |  | 向量场沿闭合路径的线积分 |
| 37 | conservative vector field | 保守场 |  | 路径积分可由势函数表示 |
| 38 | potential function | 势函数 |  | 梯度生成相应向量场的标量函数 |
| 39 | path independence | 路径无关性 |  | 线积分与路径选择无关 |
| 40 | Green's theorem | 格林公式 |  | 平面边界线积分与区域积分相关 |
| 41 | divergence theorem / Gauss's theorem | 高斯散度定理 |  | 闭曲面的通量等于区域内散度积分 |
| 42 | Stokes' theorem | 斯托克斯定理 |  | 曲面的旋度通量等于边界环流 |
| 43 | constrained extremum | 约束极值 |  | 满足约束条件下的最值 |
| 44 | method of Lagrange multipliers | 拉格朗日乘数法 |  | 利用约束梯度寻找驻点 |

## 06. 线性代数与矩阵论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | vector | 向量 |  | 可加且可数乘的对象 |
| 2 | zero vector | 零向量 |  | 向量加法单位元 |
| 3 | vector space | 向量空间 |  | 满足线性运算公理的集合 |
| 4 | subspace | 子空间 |  | 对线性运算封闭的子集 |
| 5 | linear combination | 线性组合 |  | 向量的标量加权和 |
| 6 | linear dependence | 线性相关 |  | 存在非零系数组合为零 |
| 7 | linear independence | 线性无关 |  | 只有零系数组合为零 |
| 8 | span | 张成 |  | 线性组合可得到的全部向量 |
| 9 | basis | 基 |  | 既线性无关又张成空间的向量组 |
| 10 | dimension | 维数 |  | 有限维空间基中的向量数 |
| 11 | coordinates | 坐标 |  | 向量相对于基的系数 |
| 12 | change of basis | 基变换 |  | 同一向量不同基下的坐标转换 |
| 13 | linear transformation | 线性变换 |  | 保持加法与数乘的映射 |
| 14 | linear operator | 线性算子 |  | 从向量空间到自身的线性映射 |
| 15 | kernel / null space | 核 |  | 被映射为零的向量集合 |
| 16 | image / range of a linear map | 像空间 |  | 线性映射输出所张成的子空间 |
| 17 | rank | 秩 |  | 线性映射像空间的维数 |
| 18 | nullity | 核维数 |  | 线性变换核的维数 |
| 19 | rank-nullity theorem | 秩—零度定理 |  | 秩与零度之和等于定义域维数 |
| 20 | matrix | 矩阵 |  | 按行列排列的数或元素 |
| 21 | row vector | 行向量 |  | 只有一行的矩阵 |
| 22 | column vector | 列向量 |  | 只有一列的矩阵 |
| 23 | square matrix | 方阵 |  | 行数与列数相同的矩阵 |
| 24 | identity matrix | 单位矩阵 |  | 主对角为 1，其他为 0 |
| 25 | zero matrix | 零矩阵 |  | 所有元素为零 |
| 26 | transpose | 转置矩阵 |  | 行列互换得到的矩阵 |
| 27 | conjugate transpose / Hermitian transpose | 共轭转置 |  | 转置并逐项取复共轭 |
| 28 | inverse matrix | 逆矩阵 |  | 与原矩阵相乘得到单位矩阵 |
| 29 | invertible matrix | 可逆矩阵 |  | 存在双侧逆矩阵的方阵 |
| 30 | elementary row operation | 初等行变换 |  | 交换、缩放、倍加行 |
| 31 | row echelon form | 行阶梯形矩阵 |  | 主元位置呈阶梯排列 |
| 32 | reduced row echelon form | 简化行阶梯形矩阵 |  | 每个主元列除主元外均为零 |
| 33 | Gaussian elimination | 高斯消元法 |  | 通过行变换求解线性方程组 |
| 34 | determinant | 行列式 |  | 描述方阵体积缩放及可逆性 |
| 35 | trace | 迹 |  | 方阵对角线元素之和 |
| 36 | eigenvalue | 特征值 |  | 满足 Av=λv 的标量 |
| 37 | eigenvector | 特征向量 |  | 满足 Av=λv 的非零向量 |
| 38 | characteristic polynomial | 特征多项式 |  | det(λI-A) 对应的多项式 |
| 39 | eigenspace | 特征空间 |  | 给定特征值对应的特征向量与零向量 |
| 40 | similar matrices | 相似矩阵 |  | 通过可逆矩阵换基相联系 |
| 41 | diagonalization | 对角化 |  | 在适当基下化为对角矩阵 |
| 42 | orthogonal vectors | 正交向量 |  | 内积为零的向量 |
| 43 | orthogonal matrix | 正交矩阵 |  | 满足 QᵀQ=I 的实方阵 |
| 44 | unitary matrix | 酉矩阵 |  | 满足 U*U=I 的复方阵 |
| 45 | symmetric matrix | 对称矩阵 |  | 满足 Aᵀ=A 的实矩阵 |
| 46 | Hermitian matrix | 埃尔米特矩阵 |  | 满足 A*=A 的复矩阵 |
| 47 | positive definite matrix | 正定矩阵 |  | 非零向量满足 x*Ax>0 的 Hermitian 矩阵 |
| 48 | inner product | 内积 |  | 衡量长度与角度的双线性或半双线性结构 |
| 49 | norm | 范数 |  | 满足范数公理的长度度量 |
| 50 | Euclidean norm / 2-norm | 欧几里得范数 |  | 向量分量平方和的平方根 |
| 51 | orthogonal projection | 正交投影 |  | 沿正交方向投到子空间 |
| 52 | Gram-Schmidt orthogonalization | 格拉姆—施密特正交化 |  | 将无关向量组转为正交组 |
| 53 | least squares method | 最小二乘法 |  | 最小化残差平方和 |
| 54 | singular value decomposition (SVD) | 奇异值分解 | SVD | 将矩阵分为 UΣV* 结构 |
| 55 | singular value | 奇异值 |  | A*A 特征值的非负平方根 |
| 56 | spectral theorem | 谱定理 |  | 自伴随或正规算子的谱分解结果 |

## 07. 概率论与随机变量

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | random experiment | 随机试验 |  | 结果不确定但可重复描述的试验 |
| 2 | sample space | 样本空间 |  | 全部可能结果的集合 |
| 3 | sample point / outcome | 样本点 |  | 样本空间中的单个结果 |
| 4 | event | 随机事件 |  | 样本空间的子集 |
| 5 | mutually exclusive events | 互斥事件 |  | 不能同时发生的事件 |
| 6 | complementary event | 对立事件 |  | 某事件的不发生 |
| 7 | probability | 概率 |  | 满足概率公理的测度 |
| 8 | classical probability | 古典概率 |  | 等可能有限样本空间计数 |
| 9 | conditional probability | 条件概率 |  | 在给定事件下的概率 |
| 10 | law of total probability | 全概率公式 |  | 用划分事件计算总体概率 |
| 11 | Bayes' theorem | 贝叶斯公式 |  | 条件概率反向更新公式 |
| 12 | independent events | 独立事件 |  | 交事件概率等于概率乘积 |
| 13 | random variable | 随机变量 |  | 将随机结果映为数值的函数 |
| 14 | discrete random variable | 离散型随机变量 |  | 取值可数的随机变量 |
| 15 | continuous random variable | 连续型随机变量 |  | 通常以密度描述分布的变量 |
| 16 | probability mass function (PMF) | 概率质量函数 | PMF | 离散变量各取值概率 |
| 17 | probability density function (PDF) | 概率密度函数 | PDF | 积分给出区间概率的函数 |
| 18 | cumulative distribution function (CDF) | 累积分布函数 | CDF | F(x)=P(X≤x) |
| 19 | joint distribution | 联合分布 |  | 多个随机变量的联合规律 |
| 20 | marginal distribution | 边缘分布 |  | 从联合分布得到单变量分布 |
| 21 | conditional distribution | 条件分布 |  | 给定部分变量后的分布 |
| 22 | expected value / expectation | 数学期望 |  | 随机变量按概率加权的平均 |
| 23 | variance | 方差 |  | 相对期望的平方偏差的期望 |
| 24 | standard deviation | 标准差 |  | 方差的非负平方根 |
| 25 | covariance | 协方差 |  | 两个变量共同变化的度量 |
| 26 | correlation coefficient | 相关系数 |  | 标准化的协方差 |
| 27 | moment | 矩 |  | 随机变量幂的期望或中心化期望 |
| 28 | moment-generating function (MGF) | 矩母函数 | MGF | 在存在时用于生成矩的函数 |
| 29 | characteristic function | 特征函数（概率） |  | 复指数期望，刻画概率分布 |
| 30 | Bernoulli distribution | 伯努利分布 |  | 仅取 0 与 1 的分布 |
| 31 | binomial distribution | 二项分布 |  | 独立伯努利试验成功次数分布 |
| 32 | geometric distribution | 几何分布 |  | 首次成功前后试验次数约定需注明 |
| 33 | Poisson distribution | 泊松分布 |  | 描述计数事件的离散分布 |
| 34 | uniform distribution | 均匀分布 |  | 区间内密度恒定的分布 |
| 35 | exponential distribution | 指数分布 |  | 常用于等待时间建模 |
| 36 | normal / Gaussian distribution | 正态分布 |  | 钟形曲线对应的连续分布 |
| 37 | law of large numbers | 大数定律 |  | 样本平均趋近总体期望的定理 |
| 38 | central limit theorem (CLT) | 中心极限定理 | CLT | 适当标准化的和趋向正态分布 |
| 39 | Chebyshev's inequality | 切比雪夫不等式 |  | 利用方差约束偏离概率 |
| 40 | Markov's inequality | 马尔可夫不等式 |  | 约束非负随机变量尾概率 |
| 41 | convergence in probability | 依概率收敛 |  | 偏离极限超过阈值的概率趋零 |
| 42 | almost sure convergence | 几乎处处收敛 |  | 除零概率集合外逐点收敛 |
| 43 | convergence in distribution | 依分布收敛 |  | 分布函数在连续点上收敛 |

## 08. 数理统计与数据分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | population | 总体 |  | 研究对象的完整集合或分布 |
| 2 | sample | 样本 |  | 从总体抽取的观测 |
| 3 | random sample | 随机样本 |  | 通常指独立同分布样本 |
| 4 | sample size | 样本量 |  | 样本观测的数量 |
| 5 | statistic | 统计量 |  | 仅由样本计算的函数 |
| 6 | parameter | 参数 |  | 刻画总体分布的未知量 |
| 7 | sample mean | 样本均值 |  | 样本观测的算术平均 |
| 8 | sample variance | 样本方差 |  | 以 n-1 为分母的常用无偏形式 |
| 9 | sample standard deviation | 样本标准差 |  | 样本方差平方根 |
| 10 | empirical distribution function (ECDF) | 经验分布函数 | ECDF | 样本中不超过 x 的比例 |
| 11 | histogram | 直方图 |  | 按区间统计频数或密度的图形 |
| 12 | box plot | 箱线图 |  | 显示四分位数与异常点的图形 |
| 13 | quantile | 分位数 |  | 对应指定累积概率的位置 |
| 14 | median | 中位数 |  | 0.5 分位数 |
| 15 | mode | 众数 |  | 概率质量或密度较高的取值 |
| 16 | point estimation | 点估计 |  | 用单个数估计未知参数 |
| 17 | interval estimation | 区间估计 |  | 用随机区间估计参数 |
| 18 | estimator | 估计量 |  | 用于估计参数的样本函数 |
| 19 | estimate | 估计值 |  | 估计量在样本上的具体结果 |
| 20 | unbiased estimation | 无偏估计 |  | 估计量期望等于目标参数 |
| 21 | consistency | 一致性 |  | 样本增大时估计量趋近真参数 |
| 22 | efficiency | 有效性 |  | 在指定准则下的估计精度 |
| 23 | maximum likelihood estimation (MLE) | 最大似然估计 | MLE | 最大化观测数据似然 |
| 24 | method of moments | 矩估计法 |  | 匹配样本矩与理论矩 |
| 25 | sufficient statistic | 充分统计量 |  | 保留参数相关全部样本信息 |
| 26 | confidence interval (CI) | 置信区间 | CI | 具有指定长期覆盖率的构造区间 |
| 27 | confidence level | 置信水平 |  | 区间过程的覆盖率目标 |
| 28 | significance level | 显著性水平 |  | 预先规定的一类错误上限 |
| 29 | null hypothesis (H₀) | 原假设 |  | 接受检验的基准假设 |
| 30 | alternative hypothesis (H₁) | 备择假设 |  | 与原假设相竞争的假设 |
| 31 | test statistic | 检验统计量 |  | 用于判断假设的统计量 |
| 32 | rejection region | 拒绝域 |  | 统计量落入时拒绝原假设的区域 |
| 33 | p-value | p 值 |  | 原假设下至少同样极端结果的概率 |
| 34 | Type I error | 第一类错误 |  | 原假设为真却拒绝它 |
| 35 | Type II error | 第二类错误 |  | 原假设为假却未拒绝它 |
| 36 | statistical power | 检验功效 |  | 正确拒绝错误原假设的概率 |
| 37 | t-test | t 检验 |  | 基于 t 分布的均值相关检验 |
| 38 | chi-square test | 卡方检验 |  | 常用于拟合优度或独立性检验 |
| 39 | analysis of variance (ANOVA) | 方差分析 | ANOVA | 比较组均值的统计框架 |
| 40 | regression analysis | 回归分析 |  | 研究响应变量与解释变量关系 |
| 41 | linear regression | 线性回归 |  | 模型在参数上呈线性 |
| 42 | residual | 残差 |  | 观测值与拟合值之差 |
| 43 | coefficient of determination (R²) | 决定系数 |  | 常用于衡量回归拟合优度 |
| 44 | overfitting | 过拟合 |  | 训练样本拟合好但泛化差 |
| 45 | cross-validation | 交叉验证 |  | 通过样本划分评估模型表现 |

## 09. 常微分方程与动力系统

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | differential equation | 微分方程 |  | 含未知函数及其导数的方程 |
| 2 | ordinary differential equation (ODE) | 常微分方程 | ODE | 未知函数仅依赖一个自变量 |
| 3 | order of a differential equation | 方程的阶 |  | 出现的最高阶导数阶数 |
| 4 | linear differential equation | 线性微分方程 |  | 未知函数及其导数线性出现 |
| 5 | nonlinear differential equation | 非线性微分方程 |  | 不满足线性结构的方程 |
| 6 | homogeneous linear equation | 齐次线性方程 |  | 线性方程右端为零 |
| 7 | nonhomogeneous linear equation | 非齐次线性方程 |  | 线性方程具有非零外力项 |
| 8 | general solution | 通解 |  | 包含任意常数的解族 |
| 9 | particular solution | 特解 |  | 满足指定条件的具体解 |
| 10 | initial value problem (IVP) | 初值问题 | IVP | 给定某时刻函数状态 |
| 11 | boundary value problem (BVP) | 边值问题 | BVP | 给定不同边界位置的条件 |
| 12 | separable differential equation | 可分离变量方程 |  | 可分为函数与自变量两侧 |
| 13 | first-order linear ODE | 一阶线性方程 |  | 一阶未知函数线性方程 |
| 14 | integrating factor | 积分因子 |  | 使方程成为可直接积分形式的因子 |
| 15 | Bernoulli differential equation | 伯努利微分方程 |  | 可经变量替换线性化的一阶方程 |
| 16 | exact differential equation | 恰当微分方程 |  | 对应某势函数的全微分 |
| 17 | characteristic equation | 特征方程 |  | 用于常系数线性 ODE 求解的代数方程 |
| 18 | constant-coefficient differential equation | 常系数微分方程 |  | 系数为常数的线性方程 |
| 19 | homogeneous solution | 齐次解 |  | 对应齐次方程的解 |
| 20 | superposition principle | 特解叠加 |  | 线性系统解的叠加性质 |
| 21 | variation of parameters | 参数变易法 |  | 利用齐次解构造非齐次特解 |
| 22 | method of undetermined coefficients | 待定系数法 |  | 针对特定外力型猜测特解 |
| 23 | Laplace transform | 拉普拉斯变换 |  | 将微分问题转换到复频域 |
| 24 | existence and uniqueness theorem | 存在唯一性定理 |  | 保证初值问题局部解的条件 |
| 25 | Picard-Lindelöf theorem | 皮卡—林德勒夫定理 |  | 利用局部 Lipschitz 条件的存在唯一性 |
| 26 | phase plane | 相平面 |  | 二维自治系统状态所在平面 |
| 27 | equilibrium point | 平衡点 |  | 系统演化时保持不变的状态 |
| 28 | stability | 稳定性 |  | 扰动后解是否保持附近 |
| 29 | asymptotic stability | 渐近稳定性 |  | 扰动后轨道逐渐回到平衡点 |
| 30 | Lyapunov function | 李雅普诺夫函数 |  | 用于判断动力系统稳定性 |

## 10. 复变函数与复分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | complex number | 复数 |  | 形如 a+bi 的数 |
| 2 | real part | 实部 |  | 复数的实系数 |
| 3 | imaginary part | 虚部 |  | 复数的虚系数 |
| 4 | imaginary unit | 虚数单位 |  | 满足 i²=-1 的单位 |
| 5 | complex conjugate | 复共轭 |  | a+bi 变为 a-bi |
| 6 | modulus / absolute value | 模 |  | 复平面到原点的距离 |
| 7 | argument | 辐角 |  | 复数对应的方向角 |
| 8 | principal argument | 主辐角 |  | 选定角度区间内的辐角 |
| 9 | polar form | 极形式 |  | 复数的模与角表示 |
| 10 | Euler's formula | 欧拉公式 |  | e^(iθ)=cosθ+i sinθ |
| 11 | complex plane | 复平面 |  | 以实部、虚部为坐标的平面 |
| 12 | complex-valued function | 复函数 |  | 输出为复数的函数 |
| 13 | analytic function | 解析函数 |  | 局部可由收敛幂级数表示 |
| 14 | holomorphic function | 全纯函数 |  | 复开集上处处复可导 |
| 15 | entire function | 整函数 |  | 整个复平面全纯的函数 |
| 16 | Cauchy-Riemann equations | 柯西—黎曼方程 |  | 复可导的必要条件之一 |
| 17 | Cauchy's integral theorem | 柯西积分定理 |  | 适当条件下闭路积分为零 |
| 18 | Cauchy's integral formula | 柯西积分公式 |  | 通过边界积分求内部函数值 |
| 19 | complex contour integral | 复路径积分 |  | 沿复平面路径的积分 |
| 20 | closed contour | 闭路 |  | 起点和终点重合的路径 |
| 21 | simply connected domain | 单连通区域 |  | 任意闭路可连续收缩为一点 |
| 22 | isolated singularity | 孤立奇点 |  | 邻域穿孔后全纯的异常点 |
| 23 | removable singularity | 可去奇点 |  | 可通过延拓消除的奇点 |
| 24 | pole | 极点 |  | 函数在该处呈有限阶负幂发散 |
| 25 | essential singularity | 本性奇点 |  | 既非极点也非可去的孤立奇点 |
| 26 | residue | 留数 |  | 洛朗级数中 (z-z₀)^(-1) 项系数 |
| 27 | residue theorem | 留数定理 |  | 闭路积分可由留数和计算 |
| 28 | Laurent series | 洛朗级数 |  | 含正幂与负幂的局部展开 |
| 29 | analytic continuation | 解析延拓 |  | 将解析函数扩展到更大区域 |
| 30 | conformal map | 保角映射 |  | 局部保持角度的映射 |
| 31 | maximum modulus principle | 最大模原理 |  | 非常值全纯函数模无法在内部取局部极大 |
| 32 | argument principle | 幅角原理 |  | 用对数导数积分计数零点与极点 |

## 11. 实分析、测度与泛函分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | completeness | 完备性 |  | 柯西列在空间内收敛 |
| 2 | Cauchy sequence | 柯西列 |  | 充分靠后的各项任意接近 |
| 3 | limit point / accumulation point | 极限点 |  | 任意邻域有不同于该点的集合点 |
| 4 | closure | 闭包 |  | 集合与其全部极限点组成的最小闭集 |
| 5 | interior | 内部 |  | 所有内点组成的集合 |
| 6 | boundary | 边界 |  | 每个邻域都同时接触集合与其补集 |
| 7 | open set | 开集 |  | 每点都有包含于该集合的邻域 |
| 8 | closed set | 闭集 |  | 其补集为开集 |
| 9 | compactness | 紧致性 |  | 每个开覆盖有有限子覆盖 |
| 10 | Heine-Borel theorem | 海涅—博雷尔定理 |  | 欧氏空间中闭且有界等价于紧致 |
| 11 | uniform continuity | 一致连续 |  | 连续性中的 δ 不依赖于选点 |
| 12 | uniform convergence | 一致收敛 |  | 对整个定义域统一控制误差 |
| 13 | pointwise convergence | 逐点收敛 |  | 每个固定自变量处收敛 |
| 14 | sequence of functions | 函数列 |  | 按指标排列的一列函数 |
| 15 | series of functions | 函数项级数 |  | 各项为函数的无穷级数 |
| 16 | Weierstrass M-test | 魏尔斯特拉斯判别法 |  | 用收敛数项级数证明一致收敛 |
| 17 | Lipschitz continuity | 利普希茨连续 |  | 函数值差由距离的常数倍控制 |
| 18 | measure | 测度 |  | 对集合大小进行可列可加的赋值 |
| 19 | measurable set | 可测集 |  | 属于给定 σ-代数的集合 |
| 20 | sigma-algebra | σ-代数 |  | 对补与可数并封闭的集合族 |
| 21 | Lebesgue measure | 勒贝格测度 |  | 扩展长度、面积和体积的测度 |
| 22 | Lebesgue integral | 勒贝格积分 |  | 按函数取值分层定义的积分 |
| 23 | almost everywhere (a.e.) | 几乎处处 |  | 除零测集外成立 |
| 24 | measure-zero set / null set | 零测集 |  | 测度等于零的集合 |
| 25 | dominated convergence theorem | 控制收敛定理 |  | 由可积控制函数推出极限与积分交换 |
| 26 | monotone convergence theorem | 单调收敛定理 |  | 非负递增可测函数的积分极限定理 |
| 27 | normed space | 赋范空间 |  | 定义了范数的线性空间 |
| 28 | Banach space | 巴拿赫空间 |  | 完备的赋范线性空间 |
| 29 | Hilbert space | 希尔伯特空间 |  | 完备的内积空间 |
| 30 | bounded linear operator | 有界线性算子 |  | 具有有限算子范数的线性算子 |
| 31 | dual space | 对偶空间 |  | 连续线性泛函组成的空间 |
| 32 | weak convergence | 弱收敛 |  | 通过连续线性泛函检验的收敛 |
| 33 | operator norm | 算子范数 |  | 线性算子的最大放大率 |

## 12. 抽象代数与数论基础

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | algebraic structure | 代数结构 |  | 带有特定运算及公理的集合 |
| 2 | binary operation | 二元运算 |  | 从两个输入产生一个输出的运算 |
| 3 | closure under an operation | 封闭性 |  | 运算结果仍属于原集合 |
| 4 | associative law | 结合律 |  | 改变括号不改变结果 |
| 5 | commutative law | 交换律 |  | 交换运算对象不改变结果 |
| 6 | identity element | 单位元 |  | 与任意元素运算不改变它 |
| 7 | inverse element | 逆元 |  | 与给定元素运算得到单位元 |
| 8 | group | 群 |  | 满足群公理的集合及运算 |
| 9 | Abelian group | 阿贝尔群 |  | 运算可交换的群 |
| 10 | subgroup | 子群 |  | 本身也构成群的子集 |
| 11 | cyclic group | 循环群 |  | 由单个元素生成的群 |
| 12 | coset | 陪集 |  | 子群经群元素平移的集合 |
| 13 | normal subgroup | 正规子群 |  | 左右陪集相等的子群 |
| 14 | quotient group | 商群 |  | 由正规子群陪集形成的群 |
| 15 | group homomorphism | 群同态 |  | 保持群运算的映射 |
| 16 | group isomorphism | 群同构 |  | 可逆的群同态 |
| 17 | Lagrange's theorem | 拉格朗日定理（群论） |  | 有限群中子群阶整除群阶 |
| 18 | ring | 环 |  | 具有加法与乘法运算的代数结构 |
| 19 | commutative ring | 交换环 |  | 乘法满足交换律的环 |
| 20 | integral domain | 整环 |  | 无零因子的交换含幺环 |
| 21 | field | 域 |  | 非零元素对乘法可逆的交换环 |
| 22 | ideal | 理想 |  | 对环乘法吸收的加法子群 |
| 23 | quotient ring | 商环 |  | 用理想定义同余类的环 |
| 24 | polynomial ring | 多项式环 |  | 系数在给定环中的多项式结构 |
| 25 | scalar field | 向量空间的标量域 |  | 决定向量数乘系数的域 |
| 26 | greatest common divisor (GCD) | 最大公因数 | GCD | 同时整除若干整数的最大正整数 |
| 27 | least common multiple (LCM) | 最小公倍数 | LCM | 若干整数的最小正公倍数 |
| 28 | congruence modulo n | 同余 |  | 整数之差被模数整除 |
| 29 | modular arithmetic | 模运算 |  | 按余数进行的运算 |
| 30 | prime number | 素数 |  | 大于 1 且只有两个正因子的整数 |
| 31 | Euclidean algorithm | 欧几里得算法 |  | 利用带余除法求最大公因数 |
| 32 | Chinese remainder theorem (CRT) | 中国剩余定理 | CRT | 特定同余方程组的求解定理 |
| 33 | Fermat's little theorem | 费马小定理 |  | 素数模意义下的幂同余关系 |

## 13. 几何、拓扑与流形

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Euclidean space | 欧几里得空间 |  | 具有标准距离和内积的空间 |
| 2 | affine space | 仿射空间 |  | 可做点差与向量平移的空间 |
| 3 | convex set | 凸集 |  | 任意两点之间线段都在集合内 |
| 4 | convex hull | 凸包 |  | 包含给定集合的最小凸集 |
| 5 | affine subspace | 线性流形（仿射子空间） |  | 向量子空间的平移 |
| 6 | metric space | 度量空间 |  | 定义了距离函数的集合 |
| 7 | metric / distance function | 度量 |  | 满足非负、对称、三角不等式等 |
| 8 | neighborhood | 邻域 |  | 包含某开球的集合 |
| 9 | topological space | 拓扑空间 |  | 给定开集族的集合 |
| 10 | continuous map | 连续映射 |  | 开集的原像仍为开集 |
| 11 | homeomorphism | 同胚 |  | 具有连续逆映射的双射 |
| 12 | connectedness | 连通性 |  | 空间不能分成两个不交非空开集 |
| 13 | path connectedness | 道路连通 |  | 任意两点可用连续路径连接 |
| 14 | product topology | 积拓扑 |  | 乘积空间上的自然拓扑 |
| 15 | quotient topology | 商拓扑 |  | 通过识别点构造的拓扑 |
| 16 | manifold | 流形 |  | 局部类似欧氏空间的空间 |
| 17 | smooth manifold | 光滑流形 |  | 配备相容光滑坐标图的流形 |
| 18 | coordinate chart | 坐标图 |  | 流形局部到欧氏空间的坐标映射 |
| 19 | tangent space | 切空间 |  | 一点处可行方向组成的向量空间 |
| 20 | tangent vector | 切向量 |  | 切空间中的向量 |
| 21 | Riemannian metric | 黎曼度量 |  | 切空间上的平滑内积族 |
| 22 | geodesic | 测地线 |  | 在几何结构下局部直的曲线 |
| 23 | surface | 曲面 |  | 局部呈二维的几何对象 |
| 24 | Gaussian curvature | 高斯曲率 |  | 曲面两个主曲率的乘积 |
| 25 | mean curvature | 平均曲率 |  | 主曲率的算术平均 |
| 26 | differential form | 微分形式 |  | 可对定向几何对象积分的反对称张量场 |
| 27 | exterior derivative | 外微分 |  | 将 k-形式映到 (k+1)-形式 |
| 28 | fundamental group | 基本群 |  | 由基点闭路的同伦类组成的群 |
| 29 | homotopy | 同伦 |  | 连续变形一条映射到另一条映射 |

## 14. 数值分析与科学计算

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | numerical error | 数值误差 |  | 近似值与目标值的偏差 |
| 2 | absolute error | 绝对误差 |  | 误差的绝对值 |
| 3 | relative error | 相对误差 |  | 误差相对于真值尺度的比例 |
| 4 | truncation error | 截断误差 |  | 截断无限过程引入的误差 |
| 5 | round-off error | 舍入误差 |  | 有限精度数值表示造成的误差 |
| 6 | machine epsilon | 机器精度 |  | 浮点数中可分辨的相对间隔尺度 |
| 7 | floating-point number | 浮点数 |  | 通过尾数与指数近似表示实数 |
| 8 | numerical stability | 数值稳定性 |  | 算法对误差扰动的放大程度 |
| 9 | condition number | 条件数 |  | 问题解对输入扰动的敏感程度 |
| 10 | ill-conditioned problem | 病态问题 |  | 微小输入扰动可能造成巨大输出变化 |
| 11 | iterative method | 迭代法 |  | 重复更新近似解的方法 |
| 12 | bisection method | 二分法 |  | 对有符号变化区间反复折半求根 |
| 13 | secant method | 割线法 |  | 以两点割线近似切线求根 |
| 14 | fixed-point iteration | 不动点迭代 |  | 迭代 x=g(x) 的形式 |
| 15 | order of convergence | 收敛阶 |  | 迭代误差减小的速率等级 |
| 16 | linear convergence | 线性收敛 |  | 误差大致按固定比例下降 |
| 17 | quadratic convergence | 二次收敛 |  | 下一步误差大致与当前误差平方成正比 |
| 18 | interpolation | 插值 |  | 构造通过已知数据点的函数 |
| 19 | Lagrange interpolation | 拉格朗日插值 |  | 用基多项式构造插值多项式 |
| 20 | Newton interpolation | 牛顿插值 |  | 使用差商形式构造插值多项式 |
| 21 | piecewise interpolation | 分段插值 |  | 在不同区间使用不同插值函数 |
| 22 | spline interpolation | 样条插值 |  | 用分段多项式满足平滑衔接条件 |
| 23 | numerical integration / quadrature | 数值积分 |  | 用离散加权求和近似积分 |
| 24 | trapezoidal rule | 梯形公式 |  | 用线性插值近似积分 |
| 25 | Simpson's rule | 辛普森公式 |  | 用二次插值近似积分 |
| 26 | Gaussian quadrature | 高斯求积 |  | 优化节点和权重的求积公式 |
| 27 | numerical differentiation | 数值微分 |  | 用离散函数值近似导数 |
| 28 | finite difference | 有限差分 |  | 以相邻数值之差代替导数信息 |
| 29 | forward difference | 前向差分 |  | 利用前方节点构造差分 |
| 30 | central difference | 中心差分 |  | 利用两侧节点构造差分 |
| 31 | Euler's method | 欧拉方法 |  | 求解 ODE 的一阶步进方法 |
| 32 | Runge-Kutta method | 龙格—库塔法 |  | 利用多次斜率评估的 ODE 积分方法 |
| 33 | finite element method (FEM) | 有限元法 | FEM | 用分片基函数离散连续问题 |
| 34 | finite volume method (FVM) | 有限体积法 | FVM | 对控制体积实施守恒离散 |
| 35 | conjugate gradient method (CG) | 共轭梯度法 | CG | 求解特定对称正定线性系统 |
| 36 | LU decomposition | LU 分解 |  | 矩阵分解为下三角与上三角矩阵 |
| 37 | QR decomposition | QR 分解 |  | 矩阵分解为正交（酉）与上三角矩阵 |

## 15. 最优化与运筹学

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | objective function | 目标函数 |  | 待最小化或最大化的函数 |
| 2 | feasible region / feasible set | 可行域 |  | 满足全部约束的解集合 |
| 3 | constraint | 约束条件 |  | 限制候选解的条件 |
| 4 | unconstrained optimization | 无约束优化 |  | 不带显式限制的最优化 |
| 5 | constrained optimization | 约束优化 |  | 具有等式或不等式约束的优化 |
| 6 | local optimum | 局部最优解 |  | 某邻域内的最优解 |
| 7 | global optimum | 全局最优解 |  | 整个可行域上的最优解 |
| 8 | convex function | 凸函数 |  | 函数值不超过连接两点函数值的线性插值 |
| 9 | strictly convex function | 严格凸函数 |  | 对不同点的凸性不等式严格成立 |
| 10 | convex optimization | 凸优化 |  | 凸目标在凸可行域上求最小值 |
| 11 | first-order optimality condition | 一阶最优性条件 |  | 基于梯度或方向导数的必要条件 |
| 12 | second-order optimality condition | 二阶最优性条件 |  | 基于 Hessian 的最优性条件 |
| 13 | Lagrangian | 拉格朗日函数 |  | 将目标函数与约束按乘子组合 |
| 14 | dual problem | 对偶问题 |  | 由原问题构造的相关优化问题 |
| 15 | weak duality | 弱对偶性 |  | 对偶目标对原问题给出界 |
| 16 | strong duality | 强对偶性 |  | 原问题与对偶问题最优值相等 |
| 17 | Karush-Kuhn-Tucker (KKT) conditions | KKT 条件 | KKT | 含驻点、可行性及互补条件 |
| 18 | complementary slackness | 互补松弛 |  | 约束松弛量与乘子乘积为零 |
| 19 | gradient descent | 梯度下降法 |  | 沿负梯度方向更新变量 |
| 20 | stochastic gradient descent (SGD) | 随机梯度下降 | SGD | 用随机梯度近似更新 |
| 21 | learning rate / step size | 学习率 |  | 每次迭代的更新幅度 |
| 22 | Newton's method for optimization | 牛顿优化法 |  | 利用 Hessian 的二阶优化方法 |
| 23 | quasi-Newton method | 拟牛顿法 |  | 近似 Hessian 或其逆的迭代方法 |
| 24 | line search | 线搜索 |  | 沿搜索方向选择步长 |
| 25 | projected gradient method | 梯度投影法 |  | 迭代后投影回可行集合 |
| 26 | linear programming (LP) | 线性规划 | LP | 线性目标和线性约束的优化 |
| 27 | integer programming (IP) | 整数规划 | IP | 部分或全部变量被限制为整数 |
| 28 | simplex method | 单纯形法 |  | 在线性规划顶点间搜索 |
| 29 | interior-point method | 内点法 |  | 从可行域内部逼近优化解 |
| 30 | sensitivity analysis | 敏感性分析 |  | 分析输入变化对最优解的影响 |
| 31 | dynamic programming | 动态规划 |  | 通过最优子结构递推求解 |
| 32 | Bellman equation | 贝尔曼方程 |  | 刻画最优价值函数的递推等式 |

## 16. 离散数学、组合与图论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | counting principle | 计数原理 |  | 确定对象数量的基本规则 |
| 2 | addition principle | 加法原理 |  | 不重叠情形数相加 |
| 3 | multiplication principle | 乘法原理 |  | 连续选择的情形数相乘 |
| 4 | permutation | 排列 |  | 考虑顺序的元素安排 |
| 5 | combination | 组合 |  | 不考虑顺序的元素选取 |
| 6 | factorial | 阶乘 |  | 从 1 到 n 的整数连乘 |
| 7 | binomial coefficient | 二项式系数 |  | 组合数 C(n,k) |
| 8 | binomial theorem | 二项式定理 |  | 二项式整数幂的展开定理 |
| 9 | inclusion-exclusion principle | 容斥原理 |  | 通过交集修正并集计数 |
| 10 | pigeonhole principle | 鸽巢原理 |  | 对象多于容器则某容器至少有两个 |
| 11 | recurrence relation | 递推关系 |  | 用先前项定义后续项 |
| 12 | generating function | 生成函数 |  | 用形式幂级数编码数列 |
| 13 | graph | 图 |  | 由顶点与边组成的结构 |
| 14 | vertex | 顶点 |  | 图中的节点 |
| 15 | edge | 边 |  | 连接两个顶点的对象 |
| 16 | directed graph / digraph | 有向图 |  | 每条边有方向的图 |
| 17 | undirected graph | 无向图 |  | 边不带方向的图 |
| 18 | weighted graph | 加权图 |  | 边或顶点具有权重的图 |
| 19 | degree | 度 |  | 与一个顶点关联的边的数量 |
| 20 | path | 路径 |  | 按边依次连接的顶点序列 |
| 21 | cycle | 回路 |  | 首尾相连的非平凡路径结构 |
| 22 | connected graph | 连通图 |  | 任意两顶点之间存在路径 |
| 23 | tree | 树 |  | 连通且无回路的无向图 |
| 24 | spanning tree | 生成树 |  | 覆盖全部顶点的子树 |
| 25 | minimum spanning tree (MST) | 最小生成树 | MST | 总权重最小的生成树 |
| 26 | shortest path | 最短路径 |  | 两顶点间总权重最小的路径 |
| 27 | Eulerian circuit | 欧拉回路 |  | 每条边恰经过一次的闭合迹 |
| 28 | Hamiltonian cycle | 哈密顿回路 |  | 每个顶点恰经过一次的回路 |
| 29 | adjacency matrix | 邻接矩阵 |  | 编码顶点之间边关系的矩阵 |
| 30 | adjacency list | 邻接表 |  | 按顶点列出邻接节点的数据结构 |
| 31 | graph coloring | 图着色 |  | 使相邻顶点满足颜色差异条件 |
| 32 | bipartite graph | 二分图 |  | 顶点可分成两组且边只跨组连接 |
| 33 | matching | 匹配 |  | 任意两条边不共享端点的边集合 |
| 34 | maximum flow | 最大流 |  | 满足容量约束的最大网络流量 |

## 17. 偏微分方程与傅里叶分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | partial differential equation (PDE) | 偏微分方程 | PDE | 含多个自变量的未知函数偏导数 |
| 2 | first-order PDE | 一阶偏微分方程 |  | 最高偏导阶数为 1 的方程 |
| 3 | second-order PDE | 二阶偏微分方程 |  | 最高偏导阶数为 2 的方程 |
| 4 | elliptic PDE | 椭圆型方程 |  | 二阶 PDE 的一种类型 |
| 5 | parabolic PDE | 抛物型方程 |  | 二阶 PDE 的一种类型 |
| 6 | hyperbolic PDE | 双曲型方程 |  | 二阶 PDE 的一种类型 |
| 7 | Laplace's equation | 拉普拉斯方程 |  | 满足 Δu=0 的方程 |
| 8 | Poisson's equation | 泊松方程 |  | 满足 Δu=f（符号约定可异）的方程 |
| 9 | heat equation | 热传导方程 |  | 描述扩散过程的 PDE |
| 10 | wave equation | 波动方程 |  | 描述振动与波传播的 PDE |
| 11 | diffusion equation | 扩散方程 |  | 描述物质或热量扩散 |
| 12 | initial condition | 初始条件 |  | 指定初始时刻的状态 |
| 13 | boundary condition | 边界条件 |  | 指定空间边界上的条件 |
| 14 | Dirichlet boundary condition | 狄利克雷边界条件 |  | 指定边界上的函数值 |
| 15 | Neumann boundary condition | 诺伊曼边界条件 |  | 指定边界法向导数 |
| 16 | Robin boundary condition | 罗宾边界条件 |  | 函数值与法向导数的线性组合 |
| 17 | separation of variables | 分离变量法 |  | 试将解写为各变量函数的乘积 |
| 18 | weak solution | 弱解 |  | 在积分或分布意义下满足方程 |
| 19 | classical solution | 经典解 |  | 具有足够导数并逐点满足方程 |
| 20 | Green's function | 格林函数 |  | 反映单位源响应的核函数 |
| 21 | Fourier transform | 傅里叶变换 |  | 将函数表示到频率域 |
| 22 | inverse Fourier transform | 傅里叶逆变换 |  | 从频域表示恢复原函数 |
| 23 | spectrum / frequency spectrum | 频谱 |  | 信号频率成分的描述 |
| 24 | convolution | 卷积 |  | 通过平移乘积积分组合两个函数 |
| 25 | convolution theorem | 卷积定理 |  | 卷积在变换域转为乘法 |
| 26 | Parseval's identity | 帕塞瓦尔恒等式 |  | 时域与频域能量之间的等式 |
| 27 | Plancherel's theorem | 普朗歇雷尔定理 |  | 傅里叶变换在 L² 上保持范数（适当归一化） |
| 28 | Dirac delta distribution | 狄拉克 delta 分布 |  | 广义函数中的单位点源 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/university-mathematics.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。


---

## 附录 / Appendices

> 与本卷 PDF 附录对应；译法和符号读法可能随学科语境变化。

### A. 易混数学术语辨析

| 术语对照 | 区别与使用提醒 |
|---|---|
| 导数 derivative / 微分 differential | derivative 是变化率；differential 是变化量的一阶线性部分。 |
| 像集 image / 陪域 codomain | 像集是实际输出的集合；陪域是预先指定的目标集合。 |
| 单射 injective / 满射 surjective | 单射强调输入不混淆；满射强调输出无遗漏。 |
| 极大值 maximum / 上确界 supremum | maximum 必须被集合某元素取到；supremum 可以取不到。 |
| 可导 differentiable / 连续 continuous | 一元函数可导必连续；连续不一定可导。 |
| 等价 equivalent / 相等 equal | 等价依赖语境中的关系；相等强调值或对象相同。 |
| 秩 rank / 维数 dimension | 秩通常指像空间维数；维数可指任意向量空间的基数。 |
| 特征值 eigenvalue / 奇异值 singular value | 特征值可为复数；奇异值为非负实数，且一般不相同。 |
| 互斥 mutually exclusive / 独立 independent | 互斥指不能同时发生；独立指 P(A∩B)=P(A)P(B)。 |
| 概率密度 PDF / 分布函数 CDF | PDF 不直接表示单点概率；CDF 表示 P(X≤x)。 |
| 统计量 statistic / 参数 parameter | 统计量依赖样本；参数描述总体分布。 |
| 估计量 estimator / 估计值 estimate | estimator 是随机函数；estimate 是计算后的具体数值。 |
| 显著 statistical significance / 实际重要 practical importance | 统计显著不自动意味着效应足够大或具有应用价值。 |
| 逐点收敛 pointwise / 一致收敛 uniform | 一致收敛要求误差在整个定义域统一小。 |
| 稳定性 stability / 收敛性 convergence | 稳定性关注误差传播；收敛性关注离散化细化后的极限。 |
| 局部最优 local optimum / 全局最优 global optimum | 局部最优只比较附近；全局最优比较整个可行域。 |
| 解析 analytic / 全纯 holomorphic | 在复分析开集上两者等价；在实分析中 analytic 要求局部幂级数展开。 |
| 条件收敛 conditional / 绝对收敛 absolute | 绝对收敛可推出收敛；条件收敛不满足绝对收敛。 |
| 拓扑同胚 homeomorphism / 微分同胚 diffeomorphism | 后者要求映射及其逆足够光滑，条件更强。 |
| 标准差 standard deviation / 标准误 standard error | 标准差刻画数据散布；标准误刻画估计量抽样波动。 |

### B. 常用数学符号

| 符号 | 英文表达 | 中文释义 |
|---|---|---|
| ∀ | for all | 对任意 |
| ∃ | there exists | 存在 |
| ∈ | element of | 属于 |
| ⊆ | subset of | 子集 |
| ∪ | union | 并集 |
| ∩ | intersection | 交集 |
| ∅ | empty set | 空集 |
| ℝ | real numbers | 实数集 |
| ℂ | complex numbers | 复数集 |
| ℤ | integers | 整数集 |
| ℚ | rational numbers | 有理数集 |
| ℕ | natural numbers | 自然数集，是否包含 0 需声明 |
| ⇒ | implies | 推出 |
| ⇔ | if and only if | 当且仅当 |
| ∑ | summation | 求和 |
| ∏ | product | 连乘 |
| ∫ | integral | 积分 |
| ∂ | partial derivative | 偏导记号 |
| ∇ | nabla / del | 梯度与微分算子 |
| Δ | Laplacian / change | 常表示拉普拉斯算子或变化量，依上下文 |
| ‖x‖ | norm | 范数 |
| ⟨u,v⟩ | inner product | 内积 |
| Aᵀ | transpose | 转置 |
| A* | conjugate transpose | 共轭转置，亦有其他约定 |
| det(A) | determinant | 行列式 |
| tr(A) | trace | 迹 |
| P(A) | probability of A | 事件 A 的概率 |
| E[X] | expectation | 期望 |
| Var(X) | variance | 方差 |
| Cov(X,Y) | covariance | 协方差 |
| O(·) | big O notation | 阶数上界记号 |
| o(·) | little o notation | 高阶小量记号 |

### C. 高频英文缩写

| 缩写 | 英文全称 | 中文含义 |
|---|---|---|
| ODE | ordinary differential equation | 常微分方程 |
| PDE | partial differential equation | 偏微分方程 |
| PMF | probability mass function | 概率质量函数 |
| PDF | probability density function | 概率密度函数；在文件语境也指 PDF 格式 |
| CDF | cumulative distribution function | 累积分布函数 |
| CLT | central limit theorem | 中心极限定理 |
| IID / i.i.d. | independent and identically distributed | 独立同分布 |
| MLE | maximum likelihood estimation | 最大似然估计 |
| CI | confidence interval | 置信区间 |
| ANOVA | analysis of variance | 方差分析 |
| SVD | singular value decomposition | 奇异值分解 |
| PCA | principal component analysis | 主成分分析 |
| QR | QR decomposition | QR 分解 |
| LU | LU decomposition | LU 分解 |
| FEM | finite element method | 有限元法 |
| FVM | finite volume method | 有限体积法 |
| FFT | fast Fourier transform | 快速傅里叶变换 |
| DFT | discrete Fourier transform | 离散傅里叶变换 |
| LP | linear programming | 线性规划 |
| IP | integer programming | 整数规划 |
| KKT | Karush-Kuhn-Tucker conditions | KKT 最优性条件 |
| SGD | stochastic gradient descent | 随机梯度下降 |
| IVP | initial value problem | 初值问题 |
| BVP | boundary value problem | 边值问题 |
| MST | minimum spanning tree | 最小生成树 |
| GCD | greatest common divisor | 最大公因数 |

