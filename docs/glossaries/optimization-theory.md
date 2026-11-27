# 最优化理论 · Optimization Theory

> 400 个专业术语中英文对照 | Bilingual Technical Glossary

**400 条双语术语 · 16 个专业章节 · 2026-11-27**

涉及数学规划、凸优化、无约束和约束优化、KKT 与对偶、线性规划、整数规划、数值方法、一阶与二阶算法、近端方法、随机梯度、大规模与分布式优化、全局优化、多目标与鲁棒优化、动态规划与最优控制。

本册对英文技术术语提供独立撰写的中文定义。各算法的性质依赖凸性、可行性、光滑性、约束资格、故障模型和数值条件等假设，不能脱离假设引用为普遍保证。

**专业审稿状态：**结构、数量、英文主词条唯一性已自动核验；尚未完成独立领域专家逐条事实审稿。参阅末尾来源。

## 章节目录

- 01. 最优化基础与数学建模（25 条）
- 02. 凸集合、凸函数与几何基础（25 条）
- 03. 无约束优化与最优性条件（25 条）
- 04. 约束优化与 KKT 条件（25 条）
- 05. 拉格朗日对偶与灵敏度分析（25 条）
- 06. 线性规划、几何与单纯形法（25 条）
- 07. 整数规划与组合优化（25 条）
- 08. 非线性规划与数值求解策略（25 条）
- 09. 一阶方法、步长与加速理论（25 条）
- 10. 二阶方法与拟牛顿算法（25 条）
- 11. 非光滑优化、次梯度与近端算法（25 条）
- 12. 随机优化与机器学习训练（25 条）
- 13. 分布式、在线与大规模优化（25 条）
- 14. 全局、黑箱与无导数优化（25 条）
- 15. 多目标、鲁棒与风险优化（25 条）
- 16. 动态规划、最优控制与应用（25 条）

---

## 01. 最优化基础与数学建模

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Optimization | 最优化 |  | 在约束条件下寻找使目标函数达到最小或最大的决策过程。 |
| 2 | Optimization Problem | 优化问题 |  | 由决策变量、目标函数与可行性约束共同定义的数学任务。 |
| 3 | Mathematical Programming | 数学规划 |  | 使用数学表达式描述并求解优化决策的研究领域。 |
| 4 | Decision Variable | 决策变量 |  | 由求解过程选择取值、决定方案的未知量。 |
| 5 | Objective Function | 目标函数 |  | 衡量候选方案成本、效用或质量的数值函数。 |
| 6 | Minimization Problem | 最小化问题 |  | 寻找使目标函数取值尽可能小的可行解。 |
| 7 | Maximization Problem | 最大化问题 |  | 寻找使目标函数取值尽可能大的可行解。 |
| 8 | Feasible Set | 可行域 |  | 满足全部问题约束的决策变量集合。 |
| 9 | Feasible Solution | 可行解 |  | 属于可行域、满足全部约束的候选方案。 |
| 10 | Infeasible Problem | 不可行问题 |  | 不存在任何满足所有约束的决策变量的优化问题。 |
| 11 | Unbounded Problem | 无界优化问题 |  | 在可行域上目标值可沿优化方向无限改进的问题。 |
| 12 | Optimal Solution | 最优解 |  | 达到问题定义的最优目标值的可行方案。 |
| 13 | Optimal Value | 最优值 |  | 目标函数在全体可行解上的最小值或最大值。 |
| 14 | Global Minimum | 全局最小值 |  | 函数在整个考虑域内取得的最小值。 |
| 15 | Local Minimum | 局部最小值 |  | 函数在某个邻域内取得的最小值。 |
| 16 | Strict Local Minimum | 严格局部极小值 |  | 邻域中除该点外所有可行点目标值都严格更大的局部解。 |
| 17 | Infimum | 下确界 |  | 所有函数值下界中的最大者，不要求被某点实际取得。 |
| 18 | Supremum | 上确界 |  | 所有函数值上界中的最小者，不要求被某点实际取得。 |
| 19 | Argmin | 最小化解集合 | argmin | 所有达到最小目标值的自变量组成的集合或其取值操作。 |
| 20 | Argmax | 最大化解集合 | argmax | 所有达到最大目标值的自变量组成的集合或其取值操作。 |
| 21 | Optimization Landscape | 优化地形 |  | 目标函数随决策变量变化形成的局部谷地、峰值与鞍点结构。 |
| 22 | Multi-start Optimization | 多起点优化 |  | 从多个不同初值独立运行局部优化器以寻找更好解的策略。 |
| 23 | Optimization Modeling | 优化建模 |  | 将现实决策、成本和限制转写为目标与约束的过程。 |
| 24 | Model Assumption | 模型假设 |  | 为简化或确定优化问题而事先规定的条件。 |
| 25 | Solver | 优化求解器 |  | 针对特定问题类别计算可行解或最优解的软件或算法。 |

## 02. 凸集合、凸函数与几何基础

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Convex Set | 凸集 |  | 集合中任意两点的连线段都完全属于该集合。 |
| 2 | Convex Combination | 凸组合 |  | 权重非负且和为一的点的线性组合。 |
| 3 | Convex Hull | 凸包 |  | 包含给定点集的最小凸集。 |
| 4 | Affine Set | 仿射集 |  | 包含其中任意两点的全部仿射组合的集合。 |
| 5 | Affine Combination | 仿射组合 |  | 系数总和为一、但不要求每个系数非负的线性组合。 |
| 6 | Convex Cone | 凸锥 |  | 同时满足凸性与对非负数乘法封闭性的集合。 |
| 7 | Proper Cone | 正规锥 |  | 通常指闭、凸、尖且内部非空的锥。 |
| 8 | Dual Cone | 对偶锥 |  | 对原锥中每个向量内积均非负的向量集合。 |
| 9 | Polar Cone | 极锥 |  | 与给定锥中所有向量内积均非正的向量集合。 |
| 10 | Hyperplane | 超平面 |  | 由一个非零法向量与固定内积值定义的仿射平面。 |
| 11 | Halfspace | 半空间 |  | 满足某个线性不等式的一侧点集。 |
| 12 | Separating Hyperplane | 分离超平面 |  | 将两个凸集置于两侧或不相交侧的超平面。 |
| 13 | Supporting Hyperplane | 支撑超平面 |  | 经过凸集边界点且整个凸集位于一侧的超平面。 |
| 14 | Relative Interior | 相对内部 |  | 集合相对于其仿射包的内部。 |
| 15 | Closure | 闭包 |  | 包含集合本身及其全部极限点的最小闭集。 |
| 16 | Epigraph | 上图集 |  | 由满足目标函数值不大于高度坐标的点构成的集合。 |
| 17 | Hypograph | 下图集 |  | 由满足高度坐标不大于函数值的点构成的集合。 |
| 18 | Convex Function | 凸函数 |  | 在凸定义域内函数值不大于端点函数值的凸组合。 |
| 19 | Strictly Convex Function | 严格凸函数 |  | 对不同点及内部凸组合满足严格凸不等式的函数。 |
| 20 | Strongly Convex Function | 强凸函数 |  | 减去适当正定二次项后仍为凸函数的函数。 |
| 21 | Concave Function | 凹函数 |  | 取相反数后成为凸函数的函数。 |
| 22 | Quasiconvex Function | 拟凸函数 |  | 每个次水平集都是凸集的函数。 |
| 23 | Log-convex Function | 对数凸函数 |  | 正值函数的对数为凸函数的性质。 |
| 24 | Jensen Inequality | 詹森不等式 |  | 凸函数作用于加权平均的值不超过函数值的加权平均。 |
| 25 | Perspective Function | 透视函数 |  | 由函数 f 生成 t f(x/t) 的变换，凸性可在 t 大于零时保留。 |

## 03. 无约束优化与最优性条件

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Unconstrained Optimization | 无约束优化 |  | 仅优化目标函数而没有显式可行性约束的任务。 |
| 2 | Differentiable Function | 可微函数 |  | 在指定点具有线性一阶近似的函数。 |
| 3 | Gradient | 梯度 |  | 多元标量函数对各决策变量偏导数组成的向量。 |
| 4 | Directional Derivative | 方向导数 |  | 函数沿给定方向变化的瞬时变化率。 |
| 5 | Hessian Matrix | 海森矩阵 |  | 二阶连续可微函数全部二阶偏导数组成的矩阵。 |
| 6 | Critical Point | 临界点 |  | 导数不存在或满足指定一阶驻点条件的候选点。 |
| 7 | Stationary Point | 驻点 |  | 对于可微无约束函数，梯度为零的点。 |
| 8 | First-order Necessary Condition | 一阶必要条件 |  | 可微内点局部最优解必须满足梯度为零的条件。 |
| 9 | Second-order Necessary Condition | 二阶必要条件 |  | 二阶可微内点局部最小值的海森矩阵必须半正定。 |
| 10 | Second-order Sufficient Condition | 二阶充分条件 |  | 梯度为零且海森矩阵正定可保证严格局部极小值。 |
| 11 | Positive Definite Matrix | 正定矩阵 |  | 对任意非零向量二次型值严格为正的对称矩阵。 |
| 12 | Positive Semidefinite Matrix | 半正定矩阵 |  | 对任意向量二次型值非负的对称矩阵。 |
| 13 | Indefinite Hessian | 不定海森矩阵 |  | 二次型既能取正值又能取负值的海森矩阵。 |
| 14 | Saddle Point | 鞍点 |  | 在相邻方向上呈现不同增减行为、不是局部极值的驻点。 |
| 15 | Descent Direction | 下降方向 |  | 目标函数沿该方向的方向导数为负的方向。 |
| 16 | Ascent Direction | 上升方向 |  | 目标函数沿该方向的方向导数为正的方向。 |
| 17 | Level Set | 等值集 |  | 函数取同一固定目标值的全部点的集合。 |
| 18 | Sublevel Set | 次水平集 |  | 函数值小于或等于某阈值的点的集合。 |
| 19 | Lipschitz Continuity | 利普希茨连续性 |  | 函数值变化量受自变量距离的常数倍约束。 |
| 20 | Lipschitz Gradient | 梯度利普希茨连续 |  | 梯度变化量受自变量距离常数倍约束的光滑性假设。 |
| 21 | Condition Number | 条件数 |  | 衡量问题对输入扰动敏感程度的量；二次问题常与特征值比有关。 |
| 22 | Well-conditioned Problem | 良态问题 |  | 较小输入扰动通常只引起可控解或目标变化的问题。 |
| 23 | Ill-conditioned Problem | 病态问题 |  | 细小输入或数值误差可能引起较大解变化的问题。 |
| 24 | Local Optimality | 局部最优性 |  | 候选解在指定邻域内不被其他可行点改进的性质。 |
| 25 | Global Optimality | 全局最优性 |  | 候选解在整个可行域内不被任何可行点改进的性质。 |

## 04. 约束优化与 KKT 条件

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Constrained Optimization | 约束优化 |  | 在等式或不等式条件限制下优化目标函数的任务。 |
| 2 | Equality Constraint | 等式约束 |  | 要求某表达式严格等于指定值的可行性条件。 |
| 3 | Inequality Constraint | 不等式约束 |  | 要求表达式满足上界或下界的可行性条件。 |
| 4 | Active Constraint | 活跃约束 |  | 在当前候选点取等号的不等式约束。 |
| 5 | Inactive Constraint | 非活跃约束 |  | 在当前候选点严格留有余量的不等式约束。 |
| 6 | Constraint Qualification | 约束资格条件 |  | 保证乘子存在或最优性条件适用的约束正则性假设。 |
| 7 | LICQ | 线性无关约束资格条件 | LICQ | 活跃不等式与等式约束的梯度在候选点线性无关。 |
| 8 | MFCQ | Mangasarian–Fromovitz 约束资格条件 | MFCQ | 等式梯度线性无关且存在能严格改善活跃不等式的可行方向。 |
| 9 | Slater Condition | 斯莱特条件 |  | 凸问题存在满足等式并严格满足相关不等式约束的点的条件。 |
| 10 | Karush–Kuhn–Tucker Conditions | 卡鲁什—库恩—塔克条件 | KKT | 在适当正则性下最优解满足的驻点、可行性、对偶可行性与互补条件。 |
| 11 | Lagrangian Function | 拉格朗日函数 |  | 把目标函数与约束函数按乘子加权合并的函数。 |
| 12 | Lagrange Multiplier | 拉格朗日乘子 |  | 为约束配备的系数，在正则条件下可反映边际最优值变化。 |
| 13 | Primal Feasibility | 原始可行性 |  | 决策变量满足优化问题所有原始约束的条件。 |
| 14 | Dual Feasibility | 对偶可行性 |  | 对偶变量满足符号及其他对偶约束的要求。 |
| 15 | Complementary Slackness | 互补松弛性 |  | 不等式约束的松弛量与其对应乘子的乘积为零。 |
| 16 | Stationarity Condition | 驻点条件 |  | 拉格朗日函数对原始变量的梯度或广义梯度满足零条件。 |
| 17 | Normal Cone | 法锥 |  | 以支持不等式刻画凸集边界处外法向方向的集合。 |
| 18 | Tangent Cone | 切锥 |  | 描述可行集合在指定点可沿哪些极限方向移动的锥。 |
| 19 | Feasible Direction | 可行方向 |  | 沿该方向从候选点做足够小步长仍可保持可行的方向。 |
| 20 | Linearized Constraint | 线性化约束 |  | 用一阶导数把非线性约束局部近似为线性关系。 |
| 21 | Constraint Violation | 约束违反量 |  | 度量候选解超出约束允许范围程度的数值。 |
| 22 | Penalty Function | 罚函数 |  | 把违反约束的代价附加到目标函数上的辅助函数。 |
| 23 | Exact Penalty | 精确罚函数 |  | 在足够大但有限的罚系数下可与原问题局部解一致的罚函数形式。 |
| 24 | Barrier Function | 障碍函数 |  | 在可行域边界附近急剧增大、限制迭代越界的函数。 |
| 25 | Interior Feasible Point | 严格内部可行点 |  | 严格满足所有相关不等式约束的点。 |

## 05. 拉格朗日对偶与灵敏度分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Lagrange Duality | 拉格朗日对偶 |  | 通过对约束引入乘子构造可给出原问题目标界的对偶问题。 |
| 2 | Dual Function | 对偶函数 |  | 对拉格朗日函数关于原始变量取下确界所得的函数。 |
| 3 | Dual Problem | 对偶问题 |  | 最大化拉格朗日对偶函数并满足乘子约束的问题。 |
| 4 | Primal Problem | 原始问题 |  | 相对于其拉格朗日对偶问题而言的原优化问题。 |
| 5 | Weak Duality | 弱对偶性 |  | 对于最小化原问题，任意对偶可行目标值不超过原始可行目标值。 |
| 6 | Strong Duality | 强对偶性 |  | 原始问题与对偶问题的最优值相等的性质。 |
| 7 | Duality Gap | 对偶间隙 |  | 原始问题与对偶问题最优目标值的差。 |
| 8 | Primal-dual Pair | 原始—对偶问题对 |  | 由同一优化建模关系联系的原始问题和对偶问题。 |
| 9 | Primal-dual Optimality | 原始—对偶最优性 |  | 结合原始可行、对偶可行及目标值相等验证两边最优的性质。 |
| 10 | Saddle-point Condition | 鞍点条件 |  | 拉格朗日函数在原始变量与乘子方向满足适当最小最大关系。 |
| 11 | Minimax Theorem | 极小极大定理 |  | 在规定凸凹性与紧性等条件下交换最小与最大运算的结论。 |
| 12 | Fenchel Conjugate | 芬切尔共轭 |  | 定义为变量线性内积与原函数之差的上确界的函数。 |
| 13 | Fenchel–Moreau Theorem | 芬切尔—莫罗定理 |  | 适当下半连续真凸函数等于其双共轭的定理。 |
| 14 | Biconjugate | 双共轭函数 |  | 对共轭函数再取一次共轭得到的函数。 |
| 15 | Fenchel Duality | 芬切尔对偶 |  | 利用凸共轭构造复合凸优化问题的对偶表达。 |
| 16 | Sensitivity Analysis | 灵敏度分析 |  | 研究模型参数变化引起最优值、最优解与活跃集变化的方法。 |
| 17 | Perturbation Function | 扰动函数 |  | 用参数描述目标或约束变化后所得最优值的函数。 |
| 18 | Shadow Price | 影子价格 |  | 在可微与正则条件下约束右端参数边际变化对最优值的影响率。 |
| 19 | Marginal Value | 边际价值 |  | 某项参数增加一小单位时目标最优值的变化程度。 |
| 20 | Complementary Dual Variable | 互补对偶变量 |  | 与原始约束互补关系对应的乘子变量。 |
| 21 | Dual Certificate | 对偶证书 |  | 通过可行的对偶解与目标界验证优化质量或最优性的证明对象。 |
| 22 | Primal-dual Gap | 原始—对偶差距 |  | 当前原始与对偶候选目标值之间的差额。 |
| 23 | Dual Ascent | 对偶上升法 |  | 根据对偶函数的上梯度或梯度更新乘子的迭代方法。 |
| 24 | Lagrangian Relaxation | 拉格朗日松弛 |  | 把部分约束移入目标并对其施加乘子罚项的优化方法。 |
| 25 | Dual Decomposition | 对偶分解 |  | 通过共享约束的乘子把原问题拆成可并行子问题的策略。 |

## 06. 线性规划、几何与单纯形法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Linear Programming | 线性规划 | LP | 目标和约束均为线性或仿射表达式的优化问题。 |
| 2 | Standard Form LP | 线性规划标准型 |  | 常写为最小化 cᵀx、满足 Ax=b 与 x≥0 的形式。 |
| 3 | Canonical Form LP | 线性规划规范型 |  | 将不等式和变量符号按统一约定组织的线性规划表达。 |
| 4 | Basic Solution | 基解 |  | 选取线性独立的基列并令非基变量为零所求得的候选解。 |
| 5 | Basic Feasible Solution | 基本可行解 | BFS | 既是基解又满足所有线性规划约束的解。 |
| 6 | Basis Matrix | 基矩阵 |  | 由选定基变量对应系数组成的可逆方阵。 |
| 7 | Nonbasic Variable | 非基变量 |  | 在当前单纯形基解中固定为零的变量。 |
| 8 | Extreme Point | 极点 |  | 无法表示为可行集合中两个不同点的非平凡凸组合的点。 |
| 9 | Polyhedron | 多面体 |  | 有限个线性不等式或等式定义的集合。 |
| 10 | Polytope | 凸多胞体 |  | 有界的凸多面体，亦可表示为有限点的凸包。 |
| 11 | Simplex Method | 单纯形法 |  | 沿基本可行解对应的顶点或边进行换基改进目标的算法。 |
| 12 | Primal Simplex | 原始单纯形法 |  | 保持原始可行性、逐步改善目标的换基算法。 |
| 13 | Dual Simplex | 对偶单纯形法 |  | 保持对偶可行性、逐步消除原始不可行性的算法。 |
| 14 | Revised Simplex | 修正单纯形法 |  | 通过矩阵分解与求解线性方程避免显式完整单纯形表的实现。 |
| 15 | Entering Variable | 入基变量 |  | 单纯形换基步骤中从非基变量选入基的新变量。 |
| 16 | Leaving Variable | 出基变量 |  | 单纯形换基步骤中被替换出基的旧变量。 |
| 17 | Pivot Operation | 枢轴换基操作 |  | 通过改变基与非基变量身份移动到相邻基解的步骤。 |
| 18 | Reduced Cost | 检验数／约化成本 |  | 衡量非基变量进入基后目标一阶改进可能性的系数。 |
| 19 | Degenerate Vertex | 退化顶点 |  | 一个顶点对应多于维度所需的活跃约束或存在零基变量的情形。 |
| 20 | Cycling | 循环换基 |  | 单纯形法反复回到之前某个基而不推进的罕见现象。 |
| 21 | Bland Rule | 布兰德规则 |  | 按变量最小索引选入基与出基以避免单纯形循环的规则。 |
| 22 | Phase I Simplex | 第一阶段单纯形法 |  | 通过人工变量辅助问题寻找原问题初始可行基的阶段。 |
| 23 | Phase II Simplex | 第二阶段单纯形法 |  | 从可行基出发优化原始目标函数的阶段。 |
| 24 | Farkas Lemma | 法卡斯引理 |  | 给出线性不等式可行性与不可行证书二择一关系的定理。 |
| 25 | Linear Programming Dual | 线性规划对偶 |  | 与原始 LP 对应、使用乘子构成的另一个线性规划问题。 |

## 07. 整数规划与组合优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Integer Programming | 整数规划 | IP | 要求部分或全部决策变量取整数值的优化问题。 |
| 2 | Mixed-integer Programming | 混合整数规划 | MIP | 同时包含整数变量和连续变量的数学规划模型。 |
| 3 | Mixed-integer Linear Programming | 混合整数线性规划 | MILP | 具有线性目标与约束、且部分变量为整数的优化问题。 |
| 4 | Binary Decision Variable | 二元决策变量 |  | 只允许取 0 或 1 的决策变量。 |
| 5 | Linear Relaxation | 线性松弛 |  | 去掉整数限制、保留线性约束所得的连续优化问题。 |
| 6 | Integrality Gap | 整数性间隙 |  | 整数最优解与松弛问题最优值之间的差异或比值。 |
| 7 | Branch and Bound | 分支限界法 |  | 依据当前目标界对搜索树分支剪枝并维护最优解的算法框架。 |
| 8 | Branch and Cut | 分支割平面法 |  | 在分支限界搜索中动态加入有效不等式以加强松弛的策略。 |
| 9 | Cutting Plane | 割平面 |  | 去除部分非整数松弛解而不排除任何整数可行解的有效不等式。 |
| 10 | Gomory Cut | 戈莫里割 |  | 从单纯形表的分数结构推导、排除当前非整数解的割。 |
| 11 | Valid Inequality | 有效不等式 |  | 所有整数可行解都满足的额外线性约束。 |
| 12 | Convex Relaxation | 凸松弛 |  | 以较容易求解的凸可行域或凸目标近似原优化问题。 |
| 13 | Big-M Formulation | 大 M 建模 |  | 使用足够大的常数 M 将逻辑蕴含与激活条件写成约束的技术。 |
| 14 | Indicator Constraint | 指示约束 |  | 由二元变量控制某条约束是否必须成立的建模构造。 |
| 15 | Disjunctive Programming | 析取规划 |  | 用多个可行集合的逻辑或关系描述决策约束的模型。 |
| 16 | Set Cover Problem | 集合覆盖问题 |  | 选择最少或最低成本的集合覆盖全部需求元素的优化问题。 |
| 17 | Knapsack Problem | 背包问题 |  | 在容量约束下选择物品使总价值最大化的问题。 |
| 18 | Assignment Problem | 指派问题 |  | 为任务与资源建立一一对应关系并优化总成本的模型。 |
| 19 | Vehicle Routing Problem | 车辆路径问题 | VRP | 在车辆容量、时间等条件下设计访问客户的配送路径。 |
| 20 | Facility Location Problem | 设施选址问题 |  | 综合设施建设成本与用户分配成本选择设施位置的模型。 |
| 21 | Traveling Salesperson Problem | 旅行商问题 | TSP | 寻找经过所有指定地点并回到起点的最低成本巡回路线。 |
| 22 | Column Generation | 列生成 |  | 只维护部分变量并按约化成本按需生成新变量的大规模 LP 方法。 |
| 23 | Branch and Price | 分支定价 |  | 把分支定界与列生成结合以求解大规模整数规划的框架。 |
| 24 | Primal Heuristic | 原始启发式 |  | 快速寻找可行整数解以改善当前上界的搜索方法。 |
| 25 | Mixed-integer Optimality Gap | 混合整数最优性差距 |  | 整数 incumbent 与求解器已证目标界之间的相对或绝对差。 |

## 08. 非线性规划与数值求解策略

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Nonlinear Programming | 非线性规划 | NLP | 目标或约束至少一项为非线性函数的优化问题。 |
| 2 | Sequential Quadratic Programming | 序列二次规划 | SQP | 通过一系列二次规划子问题近似求解非线性约束问题的方法。 |
| 3 | Sequential Linear Programming | 序列线性规划 | SLP | 反复对非线性模型线性化并求解局部 LP 子问题的算法。 |
| 4 | Interior-point Method | 内点法 | IPM | 在可行域内部或障碍路径附近求解优化问题的方法族。 |
| 5 | Primal-dual Interior-point Method | 原始—对偶内点法 |  | 同时更新原始变量、对偶乘子及互补残差的内点算法。 |
| 6 | Central Path | 中心路径 |  | 由不同障碍参数对应的最优或 KKT 解构成的轨迹。 |
| 7 | Barrier Parameter | 障碍参数 |  | 调节障碍函数影响强度、通常逐步趋近于零的参数。 |
| 8 | Trust Region | 信赖域 |  | 在当前迭代点附近限制局部模型有效范围的区域。 |
| 9 | Trust-region Method | 信赖域法 |  | 依模型预测与实际下降的一致程度调整局部搜索区域的方法。 |
| 10 | Line Search | 线搜索 |  | 在既定搜索方向上挑选满足下降条件的步长的过程。 |
| 11 | Armijo Condition | 阿米霍条件 |  | 要求新目标值满足足够下降的步长接受准则。 |
| 12 | Wolfe Conditions | 沃尔夫条件 |  | 组合足够下降与曲率要求的线搜索条件。 |
| 13 | Strong Wolfe Conditions | 强沃尔夫条件 |  | 对方向导数绝对值施加上界的沃尔夫条件变体。 |
| 14 | Backtracking Line Search | 回溯线搜索 |  | 反复缩小试探步长直至满足接受准则的策略。 |
| 15 | Merit Function | 功绩函数 |  | 综合目标与约束违背程度用于评价受约束迭代进展的函数。 |
| 16 | Filter Method | 过滤器方法 |  | 利用目标下降与约束违背下降之间的偏序判断试探点的策略。 |
| 17 | Restoration Phase | 可行性恢复阶段 |  | 当正常优化步骤受阻时集中降低约束违反程度的阶段。 |
| 18 | Feasibility Restoration | 可行性修复 |  | 通过调整候选解使不等式或等式约束重新满足的过程。 |
| 19 | Augmented Lagrangian Method | 增广拉格朗日法 | ALM | 把拉格朗日乘子项与约束罚项组合以改进约束问题求解的方法。 |
| 20 | Method of Multipliers | 乘子法 |  | 交替最小化增广拉格朗日函数并更新乘子的算法。 |
| 21 | Penalty Parameter | 罚参数 |  | 控制约束违反惩罚程度的非负系数。 |
| 22 | Stopping Criterion | 停止准则 |  | 根据梯度、残差、目标变化或迭代预算判断是否终止优化的规则。 |
| 23 | Primal Residual | 原始残差 |  | 衡量候选变量未满足原始约束程度的量。 |
| 24 | Dual Residual | 对偶残差 |  | 衡量当前乘子与优化条件不匹配程度的量。 |
| 25 | Karush–Kuhn–Tucker Residual | KKT 残差 |  | 综合驻点、可行性与互补性误差度量近似最优的指标。 |

## 09. 一阶方法、步长与加速理论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | First-order Method | 一阶优化方法 |  | 主要利用函数值与一阶梯度信息更新决策变量的算法族。 |
| 2 | Gradient Descent | 梯度下降法 | GD | 沿当前负梯度方向迭代更新以减小目标值的算法。 |
| 3 | Steepest Descent | 最速下降法 |  | 在选定范数下取单位约束内局部下降最快方向的算法。 |
| 4 | Projected Gradient Descent | 投影梯度下降 | PGD | 先进行梯度更新，再投影到可行集合的算法。 |
| 5 | Gradient Mapping | 梯度映射 |  | 以当前点与投影梯度更新后的差表征约束最优性的方法。 |
| 6 | Fixed Step Size | 固定步长 |  | 整个迭代过程使用预定不变学习率的更新方式。 |
| 7 | Diminishing Step Size | 递减步长 |  | 根据迭代次数逐步缩小步长的策略。 |
| 8 | Adaptive Step Size | 自适应步长 |  | 根据局部几何、历史变化或反馈动态设定步长的方法。 |
| 9 | Momentum Method | 动量法 |  | 结合当前梯度与历史更新方向抑制震荡、加速移动的算法。 |
| 10 | Heavy-ball Method | 重球法 |  | Polyak 提出的将上一迭代位移加进当前梯度更新的动量方法。 |
| 11 | Nesterov Accelerated Gradient | Nesterov 加速梯度 | NAG | 通过前瞻与特定动量系数实现凸光滑优化加速的算法族。 |
| 12 | Accelerated Gradient Method | 加速梯度法 |  | 在特定凸性条件下取得优于普通梯度下降收敛率的一阶方法。 |
| 13 | Convergence Rate | 收敛速率 |  | 描述迭代误差或目标差距随步数减小速度的渐近界。 |
| 14 | Sublinear Convergence | 次线性收敛 |  | 误差按迭代次数的幂次或更慢速度缩小的收敛方式。 |
| 15 | Linear Convergence | 线性收敛 |  | 误差在充分后期每轮以固定小于一的比例缩小的收敛方式。 |
| 16 | Superlinear Convergence | 超线性收敛 |  | 相邻误差比在极限中趋向零的收敛方式。 |
| 17 | Iteration Complexity | 迭代复杂度 |  | 达到目标误差精度所需要的迭代次数上界。 |
| 18 | Oracle Complexity | 一阶预言机复杂度 |  | 基于查询函数值或梯度次数刻画求解问题所需计算量。 |
| 19 | Smoothness Constant | 光滑常数 |  | 梯度 Lipschitz 不等式中的上界常数。 |
| 20 | Strong Convexity Parameter | 强凸参数 |  | 为强凸性二次下界提供系数的非负参数。 |
| 21 | Polyak–Łojasiewicz Condition | Polyak–Łojasiewicz 条件 | PL | 用梯度范数平方下界控制目标函数最优值差距的条件。 |
| 22 | Error Bound Condition | 误差界条件 |  | 通过残差或梯度大小控制到最优解集合距离的性质。 |
| 23 | Restart Scheme | 重启策略 |  | 周期性或按条件清空动量等历史状态以改善优化稳定性的做法。 |
| 24 | Gradient Clipping | 梯度裁剪 |  | 在梯度范数或分量过大时限制其幅度以避免不稳定更新。 |
| 25 | Numerical Stagnation | 数值停滞 |  | 受精度、条件数或步长影响而出现迭代几乎不再改善的现象。 |

## 10. 二阶方法与拟牛顿算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Second-order Method | 二阶优化方法 |  | 利用海森矩阵、曲率近似或二阶信息构造更新的优化方法。 |
| 2 | Newton Method | 牛顿法 |  | 通过解海森矩阵与梯度构成的线性系统确定局部更新方向。 |
| 3 | Damped Newton Method | 阻尼牛顿法 |  | 给牛顿方向配合线搜索或步长限制提高全局收敛稳健性的方法。 |
| 4 | Newton Decrement | 牛顿减量 |  | 由梯度与海森逆矩阵构成的局部最优性尺度指标。 |
| 5 | Modified Newton Method | 修正牛顿法 |  | 调整海森矩阵使搜索方向满足所需下降或正定性的算法。 |
| 6 | Quasi-Newton Method | 拟牛顿法 |  | 用迭代更新的矩阵近似海森矩阵或其逆的算法。 |
| 7 | Secant Equation | 割线方程 |  | 要求曲率近似满足参数步长与梯度差的关系。 |
| 8 | BFGS Algorithm | BFGS 算法 | BFGS | 依据割线关系更新正定曲率近似的经典拟牛顿方法。 |
| 9 | L-BFGS Algorithm | 有限内存 BFGS | L-BFGS | 只储存少量历史梯度差和步长对的拟牛顿方法。 |
| 10 | DFP Algorithm | DFP 算法 | DFP | Davidon–Fletcher–Powell 提出的拟牛顿矩阵更新方式。 |
| 11 | SR1 Update | 对称秩一更新 | SR1 | 利用秩一修正更新对称海森近似矩阵的方法。 |
| 12 | Gauss–Newton Method | 高斯—牛顿法 |  | 利用残差雅可比构成近似海森矩阵求解非线性最小二乘。 |
| 13 | Levenberg–Marquardt Algorithm | 列文伯格—马夸尔特算法 | LM | 通过阻尼调整高斯—牛顿线性系统处理非线性最小二乘。 |
| 14 | Jacobian Matrix | 雅可比矩阵 |  | 向量值函数各分量对输入变量偏导数构成的矩阵。 |
| 15 | Hessian-vector Product | 海森向量积 | HVP | 计算海森矩阵作用于向量的结果而无须显式形成整矩阵。 |
| 16 | Matrix-free Optimization | 无矩阵优化 |  | 利用矩阵向量积等操作求解而避免存储大型矩阵的数值方法。 |
| 17 | Conjugate Gradient Method | 共轭梯度法 | CG | 利用共轭方向求解对称正定线性系统的迭代算法。 |
| 18 | Truncated Newton Method | 截断牛顿法 |  | 用内层迭代近似求解牛顿方程并提前停止的优化方法。 |
| 19 | Inexact Newton Method | 非精确牛顿法 |  | 允许牛顿线性系统只求得满足一定残差条件的近似解。 |
| 20 | Preconditioning | 预条件化 |  | 通过变量或线性系统变换改善迭代求解器的数值条件。 |
| 21 | Cholesky Factorization | 乔列斯基分解 |  | 将对称正定矩阵表示为三角矩阵与其转置乘积。 |
| 22 | LDLᵀ Factorization | LDLᵀ 分解 |  | 将对称矩阵分解为下三角矩阵、对角或块对角矩阵及转置。 |
| 23 | Curvature Condition | 曲率条件 |  | 拟牛顿更新保持正定等性质时要求步长与梯度差满足的条件。 |
| 24 | Trust-region Subproblem | 信赖域子问题 |  | 在局部二次模型与步长范数约束下求最优搜索步的子问题。 |
| 25 | Cauchy Point | 柯西点 |  | 信赖域内沿最速下降方向最小化局部模型所得的近似步。 |

## 11. 非光滑优化、次梯度与近端算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Nonsmooth Optimization | 非光滑优化 |  | 目标或约束含不可微点的优化问题及其求解方法。 |
| 2 | Subgradient | 次梯度 |  | 对凸函数提供全局仿射下界的线性系数向量。 |
| 3 | Subdifferential | 次微分 |  | 某点所有凸次梯度组成的集合。 |
| 4 | Clarke Generalized Gradient | Clarke 广义梯度 |  | 通过附近梯度极限的凸包定义局部 Lipschitz 函数的广义导数。 |
| 5 | Subgradient Method | 次梯度法 |  | 用合法次梯度替代普通梯度迭代求解非光滑凸问题的算法。 |
| 6 | Proximal Operator | 近端算子 | prox | 使函数值与到输入点平方距离之和最小的映射。 |
| 7 | Proximal Point Algorithm | 近端点算法 | PPA | 通过连续求解带二次正则项的子问题逼近优化解的方法。 |
| 8 | Proximal Gradient Method | 近端梯度法 |  | 对光滑项作梯度步、对非光滑项作近端步的复合优化算法。 |
| 9 | Forward-backward Splitting | 前向—后向分裂 |  | 对一个算子显式更新、另一个算子使用近端或隐式步骤的分裂方法。 |
| 10 | FISTA | 快速迭代收缩阈值算法 | FISTA | 以加速近端梯度策略求解复合凸目标的算法。 |
| 11 | Soft Thresholding | 软阈值算子 |  | 对数值按阈值缩小绝对值，并将小数值置零的算子。 |
| 12 | Hard Thresholding | 硬阈值算子 |  | 保留超出阈值的数值、将其他值直接置零的非连续算子。 |
| 13 | L1 Regularization | L1 正则化 |  | 将参数绝对值和作为惩罚以鼓励稀疏解。 |
| 14 | Elastic Net Regularization | 弹性网络正则化 |  | 同时包含 L1 与 L2 惩罚的正则化方案。 |
| 15 | Group Lasso | 组套索 |  | 对预定义变量组施加组范数惩罚，以促进整组稀疏性。 |
| 16 | Total Variation Regularization | 全变差正则化 | TV | 惩罚相邻值变化或图像梯度，以鼓励分段平滑或常值结构。 |
| 17 | Moreau Envelope | 莫罗包络 |  | 用二次距离惩罚平滑原函数并保留其最优值结构的构造。 |
| 18 | Moreau Decomposition | 莫罗分解 |  | 将向量与凸函数及其共轭的近端映射联系起来的恒等式。 |
| 19 | Indicator Function of a Set | 集合指示函数 |  | 在集合内为零、集合外为正无穷的扩展实值函数。 |
| 20 | Projection Operator | 投影算子 |  | 把点映射到闭凸集合中距离最近点的算子。 |
| 21 | Douglas–Rachford Splitting | Douglas–Rachford 分裂 |  | 通过交替近端反射求解单调算子和的分裂迭代方法。 |
| 22 | Primal-dual Hybrid Gradient | 原始—对偶混合梯度 | PDHG | 交替更新原始与对偶变量、用于鞍点结构问题的算法。 |
| 23 | Chambolle–Pock Algorithm | Chambolle–Pock 算法 |  | 对一类凸凹鞍点问题进行外推与近端更新的原始—对偶算法。 |
| 24 | Monotone Operator | 单调算子 |  | 任意两图点的输出差与输入差内积非负的算子。 |
| 25 | Maximal Monotone Operator | 极大单调算子 |  | 其图无法在保持单调性的同时进一步扩大的单调算子。 |

## 12. 随机优化与机器学习训练

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Stochastic Optimization | 随机优化 |  | 目标、约束或观测含随机性的优化问题及方法。 |
| 2 | Stochastic Gradient Descent | 随机梯度下降 | SGD | 使用单个样本或随机小批量估计梯度并更新参数的算法。 |
| 3 | Mini-batch Gradient | 小批量梯度 |  | 用一组随机选取样本计算的平均梯度估计。 |
| 4 | Full-batch Gradient | 全批量梯度 |  | 使用整个训练数据集计算的目标梯度。 |
| 5 | Stochastic Approximation | 随机逼近 |  | 基于含噪观测递推逼近方程根或最优解的方法族。 |
| 6 | Robbins–Monro Algorithm | Robbins–Monro 算法 |  | 通过递减步长与随机观测寻找期望响应函数零点的随机逼近算法。 |
| 7 | Gradient Noise | 梯度噪声 |  | 随机梯度估计相对真实期望梯度的随机偏差。 |
| 8 | Unbiased Gradient Estimator | 无偏梯度估计 |  | 在适当条件下估计量期望等于目标真实梯度的估计。 |
| 9 | Gradient Variance | 梯度方差 |  | 描述随机梯度估计围绕其期望波动程度的统计量。 |
| 10 | Variance Reduction | 方差缩减 |  | 利用控制变量或历史信息降低梯度估计噪声的技术。 |
| 11 | SVRG | 随机方差缩减梯度 | SVRG | 结合周期性全梯度和局部修正项减少随机梯度方差的方法。 |
| 12 | SAGA | SAGA 方差缩减算法 | SAGA | 维护历史梯度信息并构造低方差无偏更新的随机优化方法。 |
| 13 | AdaGrad | 自适应梯度算法 | AdaGrad | 按历史梯度平方和调整各坐标学习率的优化器。 |
| 14 | RMSProp | 均方根传播优化器 | RMSProp | 利用梯度平方的指数移动平均缩放坐标更新的算法。 |
| 15 | Adam | 自适应矩估计优化器 | Adam | 结合梯度一阶与二阶矩指数移动平均更新参数的优化算法。 |
| 16 | AdamW | 解耦权重衰减 Adam | AdamW | 将权重衰减从自适应梯度更新中分离的 Adam 变体。 |
| 17 | AMSGrad | AMSGrad 优化算法 | AMSGrad | 通过非递减二阶矩尺度修正 Adam 收敛性质的变体。 |
| 18 | Learning Rate Schedule | 学习率调度 |  | 随训练进度调整优化步长的预设或自适应规则。 |
| 19 | Warmup Schedule | 学习率预热 |  | 训练初期逐步提高学习率以减轻更新不稳定的策略。 |
| 20 | Cosine Annealing | 余弦退火 |  | 按余弦曲线周期性或单次降低学习率的调度方式。 |
| 21 | Gradient Accumulation | 梯度累积 |  | 跨多个小批次累加梯度后执行一次参数更新的做法。 |
| 22 | Weight Decay | 权重衰减 |  | 在优化更新中使参数向零缩小的正则化机制。 |
| 23 | Stochastic Objective | 随机目标函数 |  | 依赖随机样本或随机扰动的损失或回报函数。 |
| 24 | Empirical Risk Minimization | 经验风险最小化 | ERM | 通过最小化训练样本平均损失选择模型参数的方法。 |
| 25 | Generalization Error | 泛化误差 |  | 模型在目标数据分布上预测损失的期望水平。 |

## 13. 分布式、在线与大规模优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributed Optimization | 分布式优化 |  | 通过多个节点协作求解共同目标或耦合约束的优化方法。 |
| 2 | Alternating Direction Method of Multipliers | 交替方向乘子法 | ADMM | 结合变量分裂、增广拉格朗日与交替更新的优化算法。 |
| 3 | Consensus Optimization | 一致性优化 |  | 各工作节点维护局部变量并通过一致性约束逼近共同解的优化模型。 |
| 4 | Consensus ADMM | 一致性 ADMM |  | 把多节点局部变量约束到全局共享变量的 ADMM 形式。 |
| 5 | Parameter Server | 参数服务器 |  | 集中或分层管理模型参数并提供梯度聚合与分发的架构。 |
| 6 | Data-parallel Optimization | 数据并行优化 |  | 将样本划分到多个设备并合并各自梯度的训练方式。 |
| 7 | Model-parallel Optimization | 模型并行优化 |  | 把同一模型的参数或计算分布到多个设备并协同求解的方式。 |
| 8 | Synchronous SGD | 同步随机梯度下降 |  | 多个工作节点完成一轮梯度计算后统一更新模型参数的算法。 |
| 9 | Asynchronous SGD | 异步随机梯度下降 |  | 工作节点无需等待全部同伴即可使用或提交梯度的更新方式。 |
| 10 | Gradient Staleness | 陈旧梯度 |  | 某个梯度基于已过期参数版本计算，可能影响收敛的现象。 |
| 11 | Gradient Compression | 梯度压缩 |  | 通过量化、稀疏化或编码减少梯度通信量的方法。 |
| 12 | Communication Complexity | 通信复杂度 |  | 分布式优化完成目标精度所需数据传输量或通信轮次数。 |
| 13 | All-reduce | 全归约 | AllReduce | 跨多个设备聚合数据并将相同聚合结果返回全部参与者的通信原语。 |
| 14 | Decentralized Optimization | 去中心化优化 |  | 节点通过邻居通信而不依赖单一中央参数服务器求解目标。 |
| 15 | Gossip Averaging | 流言平均 |  | 节点反复与邻居交换并平均局部值以趋向全局共识的过程。 |
| 16 | Federated Optimization | 联邦优化 |  | 训练数据保留在各参与端、通过模型更新协作优化的框架。 |
| 17 | Federated Averaging | 联邦平均算法 | FedAvg | 各参与方本地训练多步后加权平均模型参数的联邦方法。 |
| 18 | Client Drift | 客户端漂移 |  | 联邦本地更新因数据异质性而偏离全局优化方向的现象。 |
| 19 | Online Optimization | 在线优化 |  | 决策按时间到来、在获知当前损失全部信息前依次作出的优化框架。 |
| 20 | Online Gradient Descent | 在线梯度下降 | OGD | 每轮依据已观察损失梯度更新后续决策的在线算法。 |
| 21 | Regret | 遗憾值 |  | 算法累计损失与某个固定或动态基准策略累计损失的差。 |
| 22 | Static Regret | 静态遗憾 |  | 与事后最优的单一固定决策比较产生的累计损失差。 |
| 23 | Dynamic Regret | 动态遗憾 |  | 与每轮允许变化的比较决策序列之间的累计损失差。 |
| 24 | Mirror Descent | 镜像下降法 |  | 在一般几何下用 Bregman 散度代替欧氏距离构造更新的算法。 |
| 25 | Bregman Divergence | Bregman 散度 |  | 由严格凸可微函数生成、一般不对称的广义差异度量。 |

## 14. 全局、黑箱与无导数优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Global Optimization | 全局优化 |  | 旨在寻找整个可行域上的最好目标值而非仅局部最优的求解领域。 |
| 2 | Nonconvex Optimization | 非凸优化 |  | 目标或可行域不满足凸优化结构的优化问题。 |
| 3 | Black-box Optimization | 黑箱优化 |  | 只能通过函数评估、而不依赖显式解析表达式来求解的问题。 |
| 4 | Derivative-free Optimization | 无导数优化 | DFO | 不直接使用目标函数解析梯度或海森信息的优化方法。 |
| 5 | Direct Search | 直接搜索法 |  | 通过对若干试探点的函数值比较决定下一步搜索的方法。 |
| 6 | Pattern Search | 模式搜索 |  | 依据预定方向模式逐步试探并调整网格尺度的无导数优化算法。 |
| 7 | Nelder–Mead Method | Nelder–Mead 单纯形法 |  | 在若干顶点构成的几何单纯形上执行反射、扩张等操作的无导数方法。 |
| 8 | Trust-region Derivative-free Method | 无导数信赖域法 |  | 从采样点建立局部替代模型并在信赖域内更新的算法。 |
| 9 | Surrogate Model | 代理模型 |  | 利用已评估样本近似昂贵目标函数的计算模型。 |
| 10 | Response Surface Methodology | 响应面方法 |  | 通过局部统计建模分析输入因素与目标响应关系的优化方法。 |
| 11 | Bayesian Optimization | 贝叶斯优化 | BO | 利用概率代理模型及采集函数选择下一次昂贵函数评估的策略。 |
| 12 | Gaussian Process Surrogate | 高斯过程代理模型 | GP | 用高斯过程对黑箱函数及其不确定性进行建模。 |
| 13 | Acquisition Function | 采集函数 |  | 综合潜在改进与不确定性选择下一次评估位置的函数。 |
| 14 | Expected Improvement | 期望改进 | EI | 以目标函数改进幅度的期望作为采集准则。 |
| 15 | Probability of Improvement | 改进概率 | PI | 用候选点超过当前最好值的概率选择评估位置的准则。 |
| 16 | Upper Confidence Bound | 上置信界 | UCB | 基于预测均值与不确定性加权组合进行探索的策略。 |
| 17 | Exploration–Exploitation Tradeoff | 探索—利用权衡 |  | 在尝试未知区域与利用已知较好区域之间平衡资源分配。 |
| 18 | Random Search | 随机搜索 |  | 按照给定分布随机生成候选配置并评估目标的方法。 |
| 19 | Simulated Annealing | 模拟退火 | SA | 借助随温度降低的概率接受较差解以逃离局部极值的启发式算法。 |
| 20 | Genetic Algorithm | 遗传算法 | GA | 通过选择、交叉和变异演化候选解种群的随机搜索算法。 |
| 21 | Differential Evolution | 差分进化 | DE | 利用个体差分构造变异向量并迭代选择的群体优化算法。 |
| 22 | Particle Swarm Optimization | 粒子群优化 | PSO | 通过个体历史最好解与群体最好信息更新粒子速度和位置的方法。 |
| 23 | CMA-ES | 协方差矩阵自适应进化策略 | CMA-ES | 通过更新高斯采样分布协方差和步长进行无导数连续优化的方法。 |
| 24 | Multimodal Optimization | 多峰优化 |  | 目标函数具有多个局部极值或若干分离良好解区域的优化问题。 |
| 25 | Branch-and-bound Global Optimization | 全局分支定界 |  | 对连续区域建立可证目标界并递归分割以搜索全局最优的策略。 |

## 15. 多目标、鲁棒与风险优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multiobjective Optimization | 多目标优化 |  | 同时考虑两个或更多可能冲突目标函数的优化框架。 |
| 2 | Pareto Optimality | 帕累托最优性 |  | 不存在其他可行方案能不损害任何目标而严格改善至少一个目标的性质。 |
| 3 | Pareto Frontier | 帕累托前沿 |  | 所有非支配方案在目标空间中形成的边界集合。 |
| 4 | Dominance Relation | 支配关系 |  | 一个候选解在所有目标上不差且至少一个目标严格更好的偏序关系。 |
| 5 | Nondominated Solution | 非支配解 |  | 在指定解集合内不存在其他解支配它的候选解。 |
| 6 | Weighted Sum Method | 加权和法 |  | 通过非负权重将多个目标合成为单一标量目标的方法。 |
| 7 | Epsilon-constraint Method | ε 约束法 |  | 把部分目标变成阈值约束、优化剩余主目标的多目标方法。 |
| 8 | Lexicographic Optimization | 字典序优化 |  | 按预定优先级依次优化目标并保留高优先级最优性的策略。 |
| 9 | Goal Programming | 目标规划 |  | 使多个目标偏离指定期望水平的加权或分级偏差最小化的模型。 |
| 10 | Scalarization | 标量化 |  | 把向量目标转为单个目标以应用常规优化算法的过程。 |
| 11 | Robust Optimization | 鲁棒优化 |  | 在规定不确定性集合中保证约束及最坏情形目标表现的优化框架。 |
| 12 | Uncertainty Set | 不确定性集合 |  | 表示未知参数可能取值范围的集合。 |
| 13 | Robust Counterpart | 鲁棒对应问题 |  | 将含不确定参数的约束改写为对所有允许参数都成立的确定性问题。 |
| 14 | Worst-case Optimization | 最坏情形优化 |  | 以不确定情形中最不利结果作为优化准则的方法。 |
| 15 | Distributionally Robust Optimization | 分布鲁棒优化 | DRO | 在某个概率分布集合内优化最坏期望损失的框架。 |
| 16 | Ambiguity Set | 分布模糊集合 |  | 分布鲁棒优化中允许考虑的概率分布集合。 |
| 17 | Chance-constrained Programming | 机会约束规划 |  | 要求某些随机约束以至少指定概率成立的优化建模方式。 |
| 18 | Scenario Optimization | 场景优化 |  | 通过抽样产生的有限情景近似随机或鲁棒约束的优化方法。 |
| 19 | Stochastic Programming | 随机规划 |  | 在模型中显式引入随机参数及概率分布的数学规划方法。 |
| 20 | Two-stage Stochastic Programming | 两阶段随机规划 |  | 先作初始决策、观察随机结果后再做补救决策的模型。 |
| 21 | Recourse Decision | 补救决策 |  | 在不确定事件实现后根据观测结果调整的后续决策。 |
| 22 | Conditional Value at Risk | 条件风险价值 | CVaR | 在给定置信水平下描述分布尾部平均损失的风险度量。 |
| 23 | Value at Risk | 风险价值 | VaR | 在给定置信水平下损失分布的分位数风险度量。 |
| 24 | Mean-variance Optimization | 均值—方差优化 |  | 综合期望收益或成本与波动方差进行决策的模型。 |
| 25 | Risk-averse Optimization | 风险厌恶优化 |  | 在期望目标之外明确惩罚或约束不利随机结果的优化策略。 |

## 16. 动态规划、最优控制与应用

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Dynamic Optimization | 动态优化 |  | 决策随时间演进并受状态转移或时间耦合影响的优化问题。 |
| 2 | Optimal Control | 最优控制 |  | 在动力学约束下选择时间变化的控制输入以优化累计代价的理论。 |
| 3 | State Variable | 状态变量 |  | 描述动态系统当前状态并决定后续演化的变量。 |
| 4 | Control Input | 控制输入 |  | 可由控制器选择、用于影响系统动力学的决策量。 |
| 5 | State Transition Equation | 状态转移方程 |  | 描述下一状态如何由当前状态与控制输入决定的关系。 |
| 6 | Cost-to-go Function | 剩余代价函数 |  | 从某个状态和时刻开始所能达到的最小未来累计成本。 |
| 7 | Bellman Optimality Principle | 贝尔曼最优性原理 |  | 最优策略的后续决策对于到达状态必须构成相应子问题的最优策略。 |
| 8 | Value Function | 价值函数 |  | 把系统状态映射到某个策略或最优策略预期累计回报或成本的函数。 |
| 9 | Bellman Equation | 贝尔曼方程 |  | 把某状态的价值表示为即时成本或奖励与后续价值的递推方程。 |
| 10 | Dynamic Programming | 动态规划 | DP | 通过求解相互依赖的阶段性子问题计算全局最优策略的方法。 |
| 11 | Hamilton–Jacobi–Bellman Equation | 哈密顿—雅可比—贝尔曼方程 | HJB | 连续时间最优控制中描述价值函数的偏微分方程。 |
| 12 | Pontryagin Maximum Principle | 庞特里亚金极大值原理 | PMP | 最优控制轨迹需满足的伴随方程和哈密顿量极值条件。 |
| 13 | Costate Variable | 协态变量 |  | 最优控制中描述状态约束边际价值的伴随变量。 |
| 14 | Control Hamiltonian | 控制哈密顿量 |  | 由即时运行成本与协态和动力学内积构成的控制理论函数。 |
| 15 | Transversality Condition | 横截条件 |  | 最优控制在终端时刻或边界满足的额外必要条件。 |
| 16 | Model Predictive Control | 模型预测控制 | MPC | 反复求解有限时域最优控制并只执行当前第一步控制的策略。 |
| 17 | Receding Horizon Control | 滚动时域控制 |  | 随着时间推进持续更新有限预测窗口并重新优化控制的方案。 |
| 18 | Finite-horizon Optimization | 有限时域优化 |  | 在固定有限时间或阶段长度内优化动态决策的模型。 |
| 19 | Infinite-horizon Optimization | 无限时域优化 |  | 在无限时间范围内考虑折现或长期平均累计成本的模型。 |
| 20 | Trajectory Optimization | 轨迹优化 |  | 把状态轨迹和控制序列作为决策变量直接优化动态系统性能。 |
| 21 | Direct Collocation | 直接配点法 |  | 在时间网格上离散动力学并联合优化状态与控制变量的方法。 |
| 22 | Shooting Method | 打靶法 |  | 通过选择初始控制或协态变量、积分动力学满足终端约束的技术。 |
| 23 | Differential Dynamic Programming | 微分动态规划 | DDP | 利用局部二阶近似和时间反向递推改进控制轨迹的算法。 |
| 24 | Linear Quadratic Regulator | 线性二次调节器 | LQR | 针对线性动力学与二次成本求最优状态反馈控制律的方法。 |
| 25 | Optimal Transport | 最优传输 | OT | 在给定边缘分布约束下最小化将质量从源分布搬运至目标分布成本的问题。 |

## 核心术语辨析

| 对比对象 | 关键区别 |
|---|---|
| 凸优化 vs 非凸优化 | 凸目标在凸可行域上的任意局部极小点就是全局极小点；非凸问题通常只能依赖局部条件和额外结构保证。 |
| 必要条件 vs 充分条件 | 梯度为零和海森半正定一般只是局部极小值必要条件；梯度为零且海森正定可保证严格局部极小值。 |
| KKT 条件 vs 强对偶 | KKT 是在适当约束资格与凸性等条件下的最优性刻画；强对偶是原始与对偶最优值相等的性质，两者不能直接互相替代。 |
| 弱对偶 vs 强对偶 | 最小化原问题的任意对偶可行值给出下界是弱对偶；最优值相等才是强对偶，常需额外条件。 |
| LP 可行 vs LP 有界 | 可行仅说明至少一个满足约束的点存在；有界还需目标在可行域上不能无限改善。 |
| 单纯形法 vs 内点法 | 单纯形法沿基与极点结构换基；内点法以屏障或原始—对偶路径接近最优，均可解决大型 LP。 |
| 梯度下降 vs 牛顿法 | 梯度下降主要用一阶信息；牛顿法求解局部二阶模型并利用曲率，但会增加线性系统求解开销。 |
| BFGS vs L-BFGS | BFGS 更新并存储密集曲率近似；L-BFGS 仅保留少量历史向量，更适合高维变量。 |
| L1 vs L2 正则化 | L1 常促进解稀疏，L2 通常鼓励参数整体收缩但一般不使其恰好为零。 |
| SGD vs AdamW | SGD 使用随机梯度与统一或带动量步长；AdamW 用坐标自适应矩估计并解耦权重衰减。 |
| 全局最优 vs 局部最优 | 局部最优只在邻域中不可改善；全局最优要求整个可行域中不存在更好点。 |
| 鲁棒优化 vs 分布鲁棒优化 | 鲁棒优化对参数不确定集合内所有值保证约束；分布鲁棒优化对候选概率分布集合的最坏期望优化。 |
| Pareto 最优 vs 加权和最优 | Pareto 最优是非支配性质；加权和是生成一些 Pareto 解的标量化方法，非凸前沿可能无法完整覆盖。 |
| 在线遗憾 vs 随机训练损失 | 遗憾衡量累计在线决策相对于基准策略的差额；训练损失是具体数据或期望风险函数值。 |

## 中等难度面试题与答案

### 面试题 1. 为什么凸优化的局部最优点是全局最优点？

**参考答案：**若存在更好的另一可行点，则连接它与局部解的线段仍可行；凸性使线段上足够近的点也更好，与局部最优矛盾。

### 面试题 2. 在什么条件下 KKT 能够作为充分最优性条件？

**参考答案：**对于可微凸最小化问题，凸不等式约束、仿射等式与原始/对偶可行、驻点及互补性成立时，KKT 给出全局最优；资格条件主要用于必要性。

### 面试题 3. 为什么 2 阶海森半正定不能证明严格局部极小值？

**参考答案：**例如 f(x)=x^3 在 x=0 处梯度为零、二阶导也为零，却不是局部极小值。

### 面试题 4. 为什么整数规划往往比线性规划更难？

**参考答案：**整数约束使可行解离散、破坏连续凸结构；许多组合优化决策问题是 NP 困难的，通常依赖割与分支界。

### 面试题 5. 什么时候 L-BFGS 比完整 BFGS 更适合？

**参考答案：**当参数维度很大、无法承担 O(n²) 曲率矩阵存储时，L-BFGS 用固定历史步长与梯度差控制内存开销。

### 面试题 6. 为什么 0/1 约束的大 M 建模要特别谨慎？

**参考答案：**M 过小会误删合法方案，过大会削弱 LP 松弛和数值稳定性；应根据变量边界给出可验证的有效常数。

### 面试题 7. AdamW 与 Adam 直接加 L2 惩罚有何不同？

**参考答案：**在坐标自适应预条件器下，L2 梯度惩罚与参数乘性衰减不再等价；AdamW 单独处理权重衰减。

### 面试题 8. ADMM 是否总能收敛到任意非凸问题的全局解？

**参考答案：**不能；经典收敛保证依赖凸性、闭性、鞍点存在等条件，非凸 ADMM 通常需要额外假设且一般只能获得局部驻点保证。

### 面试题 9. 为什么贝叶斯优化适用于昂贵黑箱目标？

**参考答案：**概率代理模型根据有限评估估计均值和不确定性，采集函数权衡探索与利用，减少高成本的真实函数调用。

### 面试题 10. 什么是 Pareto 非支配，为什么一个多目标问题可能有多个解？

**参考答案：**不同目标之间存在冲突，一个解若无法在不损害任何目标下改善另一个目标，就可能位于 Pareto 前沿，通常不存在唯一的全面最好解。

## 中等难度考试题与解析

### 考试题 1. 对于 f(x)=x²+4x+7，求无约束最小点和最小值。

**解析：**f'(x)=2x+4=0 得 x*=-2；f''=2>0，代入得到 f(-2)=3。

### 考试题 2. 判断 f(x)=x⁴ 是否严格凸，以及是否在所有点都强凸。

**解析：**x⁴ 在实数域严格凸；但其二阶导 12x² 在零处为零，无法找到全域正的强凸参数。

### 考试题 3. 最小化 x²，约束 x≥1，写出最优解与对应 KKT 乘子。

**解析：**写 g(x)=1-x≤0，L=x²+λ(1-x)。x*=1，驻点 2-λ=0，故 λ*=2，互补成立。

### 考试题 4. 凸问题存在 Slater 点是否必然意味着有唯一最优解？

**解析：**不必然。Slater 常用于强对偶与乘子存在；唯一性通常需严格凸性及最优解存在等额外条件。

### 考试题 5. 函数 f(x)=x³ 在 x=0 处一阶和二阶必要条件是否成立，能否认定最小值？

**解析：**梯度和二阶导均为零，弱的一二阶必要形式满足，但任意邻域存在正负函数值，因此不是局部极小值。

### 考试题 6. 设 LP 的原始可行目标值为 12、对偶可行目标值为 10，最优值已知的界是什么？

**解析：**对最小化 LP，弱对偶给出 10≤p*≤12；差距 2 表示当前解未由该对偶证书证明最优。

### 考试题 7. 若梯度下降在 f(x)=0.5 x² 上使用固定步长 α，何时迭代收敛到 0？

**解析：**更新 x_{k+1}=(1-α)x_k；要求 |1-α|<1，即 0<α<2。

### 考试题 8. 目标为 f(x)=|x|，求 x=0 处的凸次微分。

**解析：**∂f(0)=[-1,1]；零属于该集合，验证 x=0 为全局最小点。

### 考试题 9. 一个 3 维密集 BFGS 海森近似矩阵有多少元素？

**解析：**3×3=9 个元素；一般密集表示需 O(n²) 存储。

### 考试题 10. 两个目标均需最小化，A=(2,5)、B=(3,4)，A 是否支配 B？

**解析：**不是：A 的第一目标较好但第二目标较差，B 也不支配 A；二者在该集合中互不支配。

## 权威来源与延伸阅读

以下书籍和技术资料用于术语边界和理论主题的参考；不代表作者逐条认可本项目译名与释义。

1. [Convex Optimization — Boyd & Vandenberghe (2004)](https://stanford.edu/~boyd/cvxbook/)
2. [Numerical Optimization — Nocedal & Wright (2nd ed.)](https://link.springer.com/book/10.1007/978-0-387-40065-5)
3. [Nonlinear Programming — Bertsekas](https://faculty.engineering.asu.edu/bertsekas/books/nonlinear-programming-convex-optimization)
4. [Proximal Algorithms — Parikh & Boyd (2014)](https://stanford.edu/~boyd/papers/prox_algs.html)
5. [Distributed Optimization and Statistical Learning via ADMM — Boyd et al. (2011)](https://stanford.edu/~boyd/papers/admm_distr_stats.html)
6. [NEOS Guide — Optimization Problems and Algorithms](https://neos-guide.org/guide/)
7. [CVXPY — Disciplined Convex Programming Tutorial](https://www.cvxpy.org/tutorial/dcp/)
8. [Introduction to Online Convex Optimization — Hazan](https://mitpress.mit.edu/9780262046985/introduction-to-online-convex-optimization/)

## 维护说明

- 原始数据：`data/optimization-theory/chapters/*.tsv`，每行 `en|zh|abbr|definition`。
- 汇总：`data/optimization-theory.tsv`；出版文件由专用渲染脚本生成。
- 可复现验证：`node scripts/render_optimization_theory.mjs --check`。
- 后续需额外审稿方可将词条用于专业 Wiki 的经过复核版本。
