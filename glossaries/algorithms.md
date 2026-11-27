# 算法设计与分析 · Algorithm Design and Analysis
> 专业技术术语中英文对照表 | Bilingual Technical Glossary

**总量：500 条 · 15 个专题 · 2026-11-26**

中文定义由本项目原创撰写，面向算法课程、技术面试与专业考试。部分术语依赖计算模型或输入假设；请以参考教材与原论文为准。
**审稿状态：**已进行数量、结构和重复检查；尚未取得独立专家逐条事实审稿。

## 目录
- 01. 算法基础与计算模型（30 条）
- 02. 时间复杂度与空间复杂度（35 条）
- 03. 排序与查找算法（40 条）
- 04. 分治算法（25 条）
- 05. 贪心算法（30 条）
- 06. 动态规划（40 条）
- 07. 回溯与分支限界（25 条）
- 08. 图论算法（60 条）
- 09. 字符串算法（35 条）
- 10. 数论算法（30 条）
- 11. 随机化算法（25 条）
- 12. 近似算法（25 条）
- 13. 计算复杂性理论（35 条）
- 14. 网络流与匹配算法（35 条）
- 15. 高级数据结构与算法优化（30 条）

## 01. 算法基础与计算模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Algorithm | 算法 |  | 用于解决一类问题的有限、明确且可执行的步骤序列。 |
| 2 | Algorithm Design | 算法设计 |  | 构造满足正确性与资源约束的求解步骤。 |
| 3 | Algorithm Analysis | 算法分析 |  | 研究算法的正确性、时间与空间资源需求。 |
| 4 | Computational Problem | 计算问题 |  | 把输入实例映射到要求的输出或判定结果的任务。 |
| 5 | Problem Instance | 问题实例 |  | 给定问题的一组具体输入。 |
| 6 | Input Size | 输入规模 |  | 衡量实例大小的参数，如元素数或编码位数。 |
| 7 | Problem Specification | 问题规格 |  | 明确合法输入、期望输出和约束的形式描述。 |
| 8 | Precondition | 前置条件 |  | 算法开始前必须满足的输入条件。 |
| 9 | Postcondition | 后置条件 |  | 算法结束后应成立的输出性质。 |
| 10 | Correctness | 正确性 |  | 算法对规定输入产生符合规格结果的性质。 |
| 11 | Partial Correctness | 部分正确性 |  | 在算法终止的前提下，输出满足后置条件。 |
| 12 | Total Correctness | 完全正确性 |  | 算法会终止且结果符合规格。 |
| 13 | Termination | 终止性 |  | 算法对允许的输入能在有限步骤内结束。 |
| 14 | Loop Invariant | 循环不变式 |  | 每轮循环开始或结束时持续成立的断言。 |
| 15 | Inductive Proof | 归纳证明 |  | 由基础情形与归纳步骤证明所有规模的性质。 |
| 16 | Proof by Contradiction | 反证法 |  | 假定结论不成立并推出矛盾的证明方法。 |
| 17 | Proof by Exchange | 交换论证 |  | 通过交换局部选择证明另一解不劣的技巧。 |
| 18 | Counterexample | 反例 |  | 否定某个全称命题的具体实例。 |
| 19 | Pseudocode | 伪代码 |  | 忽略语言细节、突出算法控制逻辑的表示方法。 |
| 20 | Abstract Machine | 抽象机器 |  | 以有限操作与状态刻画计算过程的理论模型。 |
| 21 | Random-Access Machine | 随机访问机器 | RAM | 把基本访存及算术操作视为定成本的分析模型。 |
| 22 | Word-RAM Model | 字长 RAM 模型 |  | 在固定字长机器字上执行基本操作的计算模型。 |
| 23 | Comparison Model | 比较模型 |  | 算法只通过元素间比较来获取顺序信息的模型。 |
| 24 | Decision Tree Model | 决策树模型 |  | 把比较结果分支组织为树以推导算法下界的模型。 |
| 25 | Deterministic Algorithm | 确定性算法 |  | 相同输入与状态总是遵循相同计算路径的算法。 |
| 26 | Nondeterministic Algorithm | 非确定性算法 |  | 理论上可在多个计算分支中选择成功路径的模型。 |
| 27 | Recursive Algorithm | 递归算法 |  | 通过求解规模更小的同类实例解决原问题。 |
| 28 | Iterative Algorithm | 迭代算法 |  | 通过循环反复更新状态完成计算的算法。 |
| 29 | In-place Algorithm | 原地算法 |  | 通常只使用常数级额外工作空间修改输入的算法。 |
| 30 | Stable Algorithm | 稳定算法 |  | 在排序语境中保持相等关键字元素原先相对顺序的算法。 |

## 02. 时间复杂度与空间复杂度

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Time Complexity | 时间复杂度 |  | 计算步骤数量随输入规模增长的量级。 |
| 2 | Space Complexity | 空间复杂度 |  | 算法占用的内存随输入规模增长的量级。 |
| 3 | Auxiliary Space | 辅助空间 |  | 除输入与输出存储外额外使用的工作空间。 |
| 4 | Worst-case Complexity | 最坏情况复杂度 |  | 同规模全部输入中资源消耗的上界。 |
| 5 | Average-case Complexity | 平均情况复杂度 |  | 在指定输入分布下的期望资源消耗。 |
| 6 | Best-case Complexity | 最好情况复杂度 |  | 同规模允许输入中所需资源的最小值。 |
| 7 | Asymptotic Analysis | 渐近分析 |  | 忽略低阶项与常数系数研究大规模增长趋势。 |
| 8 | Big O Notation | 大 O 记号 | O | 给出函数增长的渐近上界。 |
| 9 | Big Omega Notation | 大 Ω 记号 | Ω | 给出函数增长的渐近下界。 |
| 10 | Big Theta Notation | 大 Θ 记号 | Θ | 给出函数增长的紧渐近界。 |
| 11 | Little o Notation | 小 o 记号 | o | 描述严格小于另一函数的渐近增长。 |
| 12 | Little Omega Notation | 小 ω 记号 | ω | 描述严格大于另一函数的渐近增长。 |
| 13 | Constant Time | 常数时间 |  | 操作成本与输入规模无关的量级。 |
| 14 | Logarithmic Time | 对数时间 |  | 时间随输入规模的对数增长。 |
| 15 | Linear Time | 线性时间 |  | 时间与输入规模成正比增长。 |
| 16 | Linearithmic Time | 线性对数时间 |  | 时间通常为 n log n 量级。 |
| 17 | Quadratic Time | 平方时间 |  | 时间通常随输入规模平方增长。 |
| 18 | Cubic Time | 立方时间 |  | 时间通常随输入规模立方增长。 |
| 19 | Polynomial Time | 多项式时间 |  | 时间由输入规模的某个固定次数多项式界定。 |
| 20 | Pseudopolynomial Time | 伪多项式时间 |  | 对输入数值大小多项式、但对其二进制编码长度可能指数级。 |
| 21 | Exponential Time | 指数时间 |  | 时间随输入规模按固定底数指数增长。 |
| 22 | Factorial Time | 阶乘时间 |  | 运行步骤随输入规模约呈阶乘增长。 |
| 23 | Recurrence Relation | 递推关系 |  | 用更小规模问题的成本表示当前规模成本。 |
| 24 | Master Theorem | 主定理 |  | 求解常见分治递推 T(n)=aT(n/b)+f(n) 的渐近界。 |
| 25 | Recursion Tree | 递归树 |  | 把递归调用及每层工作量展开成树进行求和。 |
| 26 | Substitution Method | 代入法 |  | 猜测递推边界并通过数学归纳验证。 |
| 27 | Akra–Bazzi Method | Akra–Bazzi 方法 |  | 分析规模不均匀分治递推的一种通用定理。 |
| 28 | Amortized Analysis | 摊还分析 |  | 对操作序列证明平均每次成本上界，不依赖随机输入。 |
| 29 | Aggregate Method | 聚合法 |  | 先界定整段操作的总成本，再按次数平均。 |
| 30 | Accounting Method | 记账法 |  | 给便宜操作记信用，以支付未来昂贵操作的摊还分析方法。 |
| 31 | Potential Method | 势能法 |  | 借助状态势能变化分摊多次操作成本的方法。 |
| 32 | Potential Function | 势函数 |  | 衡量数据结构状态中预存工作量的非负函数。 |
| 33 | Lower Bound | 下界 |  | 任何满足模型限制的算法都不能突破的资源消耗界。 |
| 34 | Upper Bound | 上界 |  | 特定算法或算法族资源消耗不超过的界。 |
| 35 | Tight Bound | 紧界 |  | 上下界在渐近量级上相匹配的界。 |

## 03. 排序与查找算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sorting | 排序 |  | 按关键字将元素重新排列为非降或非升序的任务。 |
| 2 | Comparison Sort | 比较排序 |  | 仅依据元素两两比较决定相对次序的排序算法。 |
| 3 | Non-comparison Sort | 非比较排序 |  | 利用关键字的结构或取值范围实现排序。 |
| 4 | Insertion Sort | 插入排序 |  | 逐一把当前元素插入已排序前缀的适当位置。 |
| 5 | Selection Sort | 选择排序 |  | 反复选取未排序部分的最小元素放入目标位置。 |
| 6 | Bubble Sort | 冒泡排序 |  | 不断比较并交换相邻逆序元素的排序方法。 |
| 7 | Merge Sort | 归并排序 |  | 递归划分序列并线性合并有序子序列。 |
| 8 | Quick Sort | 快速排序 |  | 围绕枢轴分区后递归排序各分区。 |
| 9 | Heap Sort | 堆排序 |  | 构建堆并反复取出极值完成排序。 |
| 10 | Shell Sort | 希尔排序 |  | 按递减间隔进行分组插入排序。 |
| 11 | Counting Sort | 计数排序 |  | 按有限整数关键字频次计算输出位置的稳定排序方法。 |
| 12 | Radix Sort | 基数排序 |  | 按关键字的数字位依次进行稳定排序。 |
| 13 | Bucket Sort | 桶排序 |  | 将元素分配到若干桶并分别排序后合并。 |
| 14 | TimSort | TimSort 排序 |  | 结合已排序运行段与归并策略的自适应稳定排序。 |
| 15 | IntroSort | 内省排序 |  | 快速排序递归过深时切换堆排序以控制最坏复杂度。 |
| 16 | External Sorting | 外部排序 |  | 数据不能完整放入内存时通过外存归并完成排序。 |
| 17 | K-way Merge | 多路归并 |  | 同时合并 k 个有序序列的过程。 |
| 18 | Stable Sorting | 稳定排序 |  | 相等关键字元素在排序后维持原有先后关系。 |
| 19 | Adaptive Sorting | 自适应排序 |  | 利用输入现有有序程度降低工作量的排序策略。 |
| 20 | Comparison Lower Bound | 比较排序下界 |  | 比较排序在最坏情况下需要 Ω(n log n) 次比较。 |
| 21 | Pivot | 枢轴 |  | 快速排序中用于划分较小与较大元素的参考元素。 |
| 22 | Partition | 划分操作 |  | 按照指定条件原地或非原地重排数据的步骤。 |
| 23 | Lomuto Partition | Lomuto 分区 |  | 常用单向扫描边界的快速排序分区方案。 |
| 24 | Hoare Partition | Hoare 分区 |  | 通过双向扫描交换不在对应分区元素的方案。 |
| 25 | Three-way Partition | 三路划分 |  | 将元素分为小于、等于和大于枢轴的三部分。 |
| 26 | Order Statistic | 顺序统计量 |  | 排序后第 k 个位置的元素值。 |
| 27 | Selection Problem | 选择问题 |  | 不必完整排序就找出第 k 小元素的任务。 |
| 28 | Quickselect | 快速选择 |  | 借助分区仅递归目标一侧寻找顺序统计量。 |
| 29 | Median of Medians | 中位数的中位数 |  | 通过分组选择良好枢轴以实现线性最坏时间选择。 |
| 30 | Binary Search | 二分查找 |  | 在有序搜索空间通过中点判定反复折半。 |
| 31 | Linear Search | 线性查找 |  | 逐项检查元素是否满足目标条件。 |
| 32 | Interpolation Search | 插值查找 |  | 基于关键字数值分布估计查询位置的查找算法。 |
| 33 | Exponential Search | 指数查找 |  | 指数扩大候选范围后再做二分查找。 |
| 34 | Jump Search | 跳跃查找 |  | 按固定块跳跃定位范围后进行局部线性查找。 |
| 35 | Lower Bound Search | 下界查找 |  | 在有序数组中查找首个不小于给定值的位置。 |
| 36 | Upper Bound Search | 上界查找 |  | 在有序数组中查找首个大于给定值的位置。 |
| 37 | Binary Search on Answer | 答案二分 |  | 通过单调可行性谓词二分求满足条件的最优阈值。 |
| 38 | Inversion Count | 逆序对计数 |  | 统计满足 i 小于 j 且 A[i] 大于 A[j] 的元素对。 |
| 39 | Coordinate Compression | 坐标压缩 |  | 保留相对大小关系并把离散值映射为连续整数。 |
| 40 | Partial Sorting | 部分排序 |  | 仅确定最小 k 个或某些目标位置的排序结果。 |

## 04. 分治算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Divide and Conquer | 分治法 |  | 把问题拆分为子问题、分别求解并合并结果的设计范式。 |
| 2 | Divide Step | 划分步骤 |  | 把原实例分成规模较小子实例的过程。 |
| 3 | Conquer Step | 求解步骤 |  | 递归或直接求解各子实例的过程。 |
| 4 | Combine Step | 合并步骤 |  | 将子问题解组织为原问题解的过程。 |
| 5 | Balanced Partition | 均衡划分 |  | 让子问题规模相近以降低递归深度的分解方式。 |
| 6 | Unbalanced Partition | 非均衡划分 |  | 子问题规模悬殊的划分方式，可能加深递归。 |
| 7 | Divide-and-Conquer Recurrence | 分治递推式 |  | 描述各子问题代价与合并成本的递推公式。 |
| 8 | Binary Divide and Conquer | 二路分治 |  | 每层拆分成两个较小子问题的分治结构。 |
| 9 | Multiway Divide and Conquer | 多路分治 |  | 每层拆分成三个或更多子问题的分治结构。 |
| 10 | Closest Pair of Points | 最近点对 |  | 求欧氏平面上距离最小的两个点。 |
| 11 | Plane Sweep | 扫描线算法 |  | 按坐标顺序处理事件并维护活跃集合的几何策略。 |
| 12 | Karatsuba Multiplication | Karatsuba 乘法 |  | 以三个半规模乘法代替四个来加速整数乘法。 |
| 13 | Strassen Algorithm | Strassen 矩阵乘法 |  | 通过七次子矩阵乘法减少递归乘法次数。 |
| 14 | Fast Fourier Transform | 快速傅里叶变换 | FFT | 利用对称性及分治结构高效计算离散傅里叶变换。 |
| 15 | Cooley–Tukey Algorithm | Cooley–Tukey 算法 |  | 按因子分解变换规模的经典 FFT 算法。 |
| 16 | Recursive Bisection | 递归二分 |  | 持续将搜索区间或问题区域分为两半。 |
| 17 | Fast Exponentiation | 快速幂 |  | 通过指数二进制分解以对数次乘法计算整数幂。 |
| 18 | Exponentiation by Squaring | 平方求幂 |  | 通过反复平方及条件乘法快速求幂。 |
| 19 | Block Decomposition | 分块分解 |  | 将数据拆为固定大小块以加速批量计算或查询。 |
| 20 | Cache-Oblivious Algorithm | 缓存无关算法 |  | 无需指定缓存大小与块大小仍优化多级存储访问的算法。 |
| 21 | Cache-Aware Algorithm | 缓存感知算法 |  | 利用已知缓存容量和块大小设计访问模式。 |
| 22 | Parallel Divide and Conquer | 并行分治 |  | 允许不同递归子问题并行求解的分治结构。 |
| 23 | Work | 总工作量 |  | 并行计算中执行的所有操作的总数。 |
| 24 | Span | 关键路径长度 |  | 并行计算的依赖图中最长串行路径的长度。 |
| 25 | Divide-and-Conquer Tree | 分治树 |  | 展示递归分解层级、子问题规模与成本的树形表示。 |

## 05. 贪心算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Greedy Algorithm | 贪心算法 |  | 反复选择局部最优动作构造全局解的算法范式。 |
| 2 | Greedy Choice | 贪心选择 |  | 基于当前状态作出不回退的局部决策。 |
| 3 | Greedy Choice Property | 贪心选择性质 |  | 存在以某个局部最优选择开头的整体最优解。 |
| 4 | Optimal Substructure | 最优子结构 |  | 最优解的组成部分也对应适当子问题的最优解。 |
| 5 | Exchange Argument | 交换论证 |  | 将候选最优解调整为贪心解而不使目标变差的证明方法。 |
| 6 | Stays-ahead Argument | 领先性论证 |  | 证明贪心部分解在每一步的评价指标不落后于任意解。 |
| 7 | Activity Selection | 活动选择问题 |  | 从相互冲突的活动中选出最大数量的兼容活动。 |
| 8 | Interval Scheduling | 区间调度 |  | 在时间区间资源冲突约束下选择任务的优化问题。 |
| 9 | Earliest Finish Time Rule | 最早结束时间规则 |  | 优先选择最早结束的兼容区间以最大化区间数量。 |
| 10 | Interval Partitioning | 区间划分 |  | 以尽可能少的资源容纳全部重叠区间。 |
| 11 | Fractional Knapsack | 分数背包 |  | 允许取物品部分比例的背包优化问题。 |
| 12 | Huffman Coding | 霍夫曼编码 |  | 反复合并最小权值节点构造最优前缀编码。 |
| 13 | Prefix-free Code | 前缀无歧义编码 |  | 没有任何码字是另一完整码字前缀的编码集合。 |
| 14 | Optimal Merge Pattern | 最优归并模式 |  | 通过优先合并代价最小的对象降低总合并成本。 |
| 15 | Matroid | 拟阵 |  | 满足遗传与交换公理的独立集系统。 |
| 16 | Matroid Greedy Theorem | 拟阵贪心定理 |  | 在拟阵上按权重贪心可求得最大权基的结论。 |
| 17 | Independence System | 独立集系统 |  | 子集封闭的可行元素集合族。 |
| 18 | Graphic Matroid | 图拟阵 |  | 以无环边集作为独立集构成的拟阵。 |
| 19 | Uniform Matroid | 均匀拟阵 |  | 至多选择指定数量元素构成独立集的拟阵。 |
| 20 | Minimum Spanning Tree | 最小生成树 | MST | 连接连通带权无向图全部顶点且边权和最小的生成树。 |
| 21 | Cut Property | 割性质 |  | 跨某割的安全最轻边可纳入某棵最小生成树。 |
| 22 | Cycle Property | 环性质 |  | 唯一最重边不会出现在任何最小生成树中。 |
| 23 | Kruskal Algorithm | Kruskal 算法 |  | 按边权从小到大选择不成环的边构造最小生成树。 |
| 24 | Prim Algorithm | Prim 算法 |  | 从已选顶点集合向外扩展最轻连接边构造最小生成树。 |
| 25 | Borůvka Algorithm | Borůvka 算法 |  | 每个连通分量反复选最轻外连边的最小生成树算法。 |
| 26 | Dijkstra Algorithm | Dijkstra 算法 |  | 在非负边权图中按最小暂定距离确定最短路。 |
| 27 | Shortest Processing Time | 最短处理时间优先 | SPT | 在单机所有任务同时可用时最小化完成时间之和的排序规则。 |
| 28 | Earliest Deadline First | 最早截止时间优先 | EDF | 按截止时间排序处理任务的调度策略。 |
| 29 | Job Sequencing with Deadlines | 带截止时间的作业排序 |  | 在截止时间与收益约束下选择可完成作业的任务。 |
| 30 | Greedy Failure Counterexample | 贪心失效反例 |  | 说明某局部规则不能保证整体最优的具体输入。 |

## 06. 动态规划

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Dynamic Programming | 动态规划 | DP | 通过记录重叠子问题的解避免重复计算的优化范式。 |
| 2 | Overlapping Subproblems | 重叠子问题 |  | 不同递归路径反复遇到相同状态的性质。 |
| 3 | State | 动态规划状态 |  | 完整表示一个子问题所需的信息。 |
| 4 | State Transition | 状态转移 |  | 根据较小或前置状态的答案推导当前状态答案。 |
| 5 | Transition Equation | 状态转移方程 |  | 用数学表达式描述状态间的求解关系。 |
| 6 | Base Case | 基础状态 |  | 无需继续分解即可直接确定的子问题答案。 |
| 7 | Memoization | 记忆化搜索 |  | 按需递归求解并缓存已计算状态。 |
| 8 | Tabulation | 表格法 |  | 按依赖顺序自底向上填写状态表。 |
| 9 | Top-down DP | 自顶向下动态规划 |  | 通过递归及缓存只访问需求驱动状态的方式。 |
| 10 | Bottom-up DP | 自底向上动态规划 |  | 按拓扑顺序迭代计算所有必需状态的方式。 |
| 11 | State Space | 状态空间 |  | 算法可能访问的全部状态集合。 |
| 12 | State Compression | 状态压缩 |  | 用更紧凑的表示减少 DP 内存或状态数量。 |
| 13 | Rolling Array | 滚动数组 |  | 只保留最近若干层状态以降低存储量。 |
| 14 | Bitmask DP | 状态压缩动态规划 |  | 用位掩码表示元素集合并进行状态转移。 |
| 15 | Interval DP | 区间动态规划 |  | 以子区间边界为状态组织转移。 |
| 16 | Tree DP | 树形动态规划 |  | 利用树的父子依赖关系计算子树状态。 |
| 17 | Digit DP | 数位动态规划 |  | 按数字位、边界紧致状态等计数满足条件的整数。 |
| 18 | Profile DP | 轮廓线动态规划 |  | 记录网格扫描边界的局部占用状态以减少维度。 |
| 19 | Knapsack DP | 背包动态规划 |  | 以容量及物品处理阶段定义优化状态。 |
| 20 | Zero-one Knapsack | 零一背包 |  | 每件物品最多选一次的容量约束价值最大化问题。 |
| 21 | Unbounded Knapsack | 完全背包 |  | 每类物品可重复选择任意次的背包问题。 |
| 22 | Bounded Knapsack | 多重背包 |  | 每类物品最多选择指定次数的背包问题。 |
| 23 | Subset Sum | 子集和问题 |  | 判断是否存在元素子集使其数值和等于目标值。 |
| 24 | Coin Change | 零钱兑换 |  | 按面额集合求最少硬币数或组合数的经典 DP 问题。 |
| 25 | Longest Common Subsequence | 最长公共子序列 | LCS | 两个序列中保持相对次序的最长共同子序列。 |
| 26 | Longest Increasing Subsequence | 最长递增子序列 | LIS | 从序列中抽取严格递增且长度最大的子序列。 |
| 27 | Edit Distance | 编辑距离 |  | 通过允许的编辑操作把一个字符串变为另一字符串的最小成本。 |
| 28 | Matrix Chain Multiplication | 矩阵链乘法 |  | 选择矩阵乘法括号顺序以最小化标量乘法次数。 |
| 29 | Optimal Binary Search Tree | 最优二叉搜索树 |  | 在给定查询频率下优化期望查找代价的树结构。 |
| 30 | Weighted Interval Scheduling | 加权区间调度 |  | 选取不重叠区间使权重总和最大化的问题。 |
| 31 | Bellman Optimality Principle | 贝尔曼最优性原理 |  | 最优策略后续决策对相应状态仍需最优的原理。 |
| 32 | Optimal Value Function | 最优价值函数 |  | 给出每个状态可达到的最优目标值的函数。 |
| 33 | Decision Reconstruction | 决策路径恢复 |  | 根据转移记录从 DP 结果还原实际选择序列。 |
| 34 | Parent Pointer | 前驱指针 |  | 记录某状态最优转移来源的辅助信息。 |
| 35 | Monotone Queue Optimization | 单调队列优化 |  | 利用窗口最值维护加速特定 DP 转移。 |
| 36 | Convex Hull Trick | 凸包优化 | CHT | 维护若干直线下包络以加速线性形式的最值查询。 |
| 37 | Divide-and-Conquer DP Optimization | 分治 DP 优化 |  | 在决策点单调性等条件下缩小转移搜索范围。 |
| 38 | Knuth Optimization | Knuth 优化 |  | 利用区间决策点单调性和四边形不等式优化 DP。 |
| 39 | Quadrangle Inequality | 四边形不等式 |  | 一类区间成本矩阵满足的次模式不等式条件。 |
| 40 | Aliens Trick | Alien 优化 |  | 通过拉格朗日惩罚调节选择数量等约束并结合 DP 求最优值。 |

## 07. 回溯与分支限界

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Backtracking | 回溯法 |  | 逐步扩展部分解，发现约束违反时撤销选择并探索其他分支。 |
| 2 | Search Tree | 搜索树 |  | 表示部分解状态及其可能扩展的树结构。 |
| 3 | State-space Tree | 状态空间树 |  | 把问题所有可能决策状态组织成树的模型。 |
| 4 | Partial Solution | 部分解 |  | 尚未完成但已满足部分条件的候选决策。 |
| 5 | Feasibility Pruning | 可行性剪枝 |  | 发现当前状态无法满足约束时停止探索。 |
| 6 | Optimality Pruning | 最优性剪枝 |  | 用当前界判断分支不可能改进已知最优解。 |
| 7 | Branch and Bound | 分支限界法 |  | 以可证上下界排除不可能产生最优解的分支。 |
| 8 | Branching Rule | 分支规则 |  | 决定在当前结点选择哪个变量或决策拆分状态。 |
| 9 | Bounding Function | 界函数 |  | 估计分支可达到的最优或最差目标值的函数。 |
| 10 | Incumbent Solution | 当前最好解 |  | 搜索过程中已发现的最佳可行解。 |
| 11 | Depth-first Search with Backtracking | 回溯深度优先搜索 |  | 沿一个决策路径探索到底后撤销选择回退。 |
| 12 | Best-first Branch and Bound | 最佳优先分支限界 |  | 优先扩展界值最有希望的未处理状态。 |
| 13 | Pruning | 剪枝 |  | 依据约束或界限提前舍弃部分搜索分支。 |
| 14 | Constraint Propagation | 约束传播 |  | 利用已确定变量缩小其他变量可取值范围。 |
| 15 | Variable Ordering Heuristic | 变量排序启发式 |  | 优先选择更易引起冲突或限制更强的变量。 |
| 16 | Value Ordering Heuristic | 取值排序启发式 |  | 决定候选变量各取值的尝试先后顺序。 |
| 17 | N-Queens Problem | N 皇后问题 |  | 在棋盘放置 N 个皇后使其互不攻击的约束问题。 |
| 18 | Sudoku Solver | 数独求解器 |  | 结合约束传播与搜索填写合法数独格局的算法。 |
| 19 | Exact Cover | 精确覆盖 |  | 选择若干集合使每个目标元素恰好被覆盖一次的问题。 |
| 20 | Algorithm X | X 算法 |  | Knuth 提出的精确覆盖递归回溯算法。 |
| 21 | Dancing Links | 舞蹈链 | DLX | 支持快速删除与恢复行列的双向链接结构，用于精确覆盖搜索。 |
| 22 | Hamiltonian Cycle Search | 哈密顿环搜索 |  | 寻找恰好访问所有顶点一次并回到起点的环的搜索任务。 |
| 23 | Subset Enumeration | 子集枚举 |  | 按决策位系统遍历给定集合的全部子集。 |
| 24 | Permutation Generation | 排列生成 |  | 系统生成给定元素集合所有排列的过程。 |
| 25 | Search Symmetry Breaking | 搜索对称性破除 |  | 增加约束消除等价状态以避免重复搜索。 |

## 08. 图论算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Graph | 图 |  | 由顶点集合与顶点间边关系构成的离散结构。 |
| 2 | Vertex | 顶点 |  | 图中表示实体或状态的基本节点。 |
| 3 | Edge | 边 |  | 连接两个顶点或表示有向关联的对象。 |
| 4 | Directed Graph | 有向图 |  | 边带方向、表示有序顶点对的图。 |
| 5 | Undirected Graph | 无向图 |  | 边不区分两端方向的图。 |
| 6 | Weighted Graph | 带权图 |  | 边或顶点附带数值权重的图。 |
| 7 | Adjacency List | 邻接表 |  | 按顶点存储相邻顶点及边信息的图表示。 |
| 8 | Adjacency Matrix | 邻接矩阵 |  | 用矩阵项表示任意顶点对是否相邻或其权值。 |
| 9 | Degree | 度 |  | 无向图顶点的关联边数；有向图区分入度与出度。 |
| 10 | Path | 路径 |  | 由连续相邻顶点与边构成的行走序列。 |
| 11 | Simple Path | 简单路径 |  | 顶点不重复出现的路径。 |
| 12 | Cycle | 环 |  | 起点与终点相同且内部顶点不重复的闭合路径。 |
| 13 | Connected Component | 连通分量 |  | 无向图中极大的两两可达顶点集合。 |
| 14 | Strongly Connected Component | 强连通分量 | SCC | 有向图中任意两点相互可达的极大顶点集合。 |
| 15 | Weakly Connected Component | 弱连通分量 |  | 有向图忽略边方向后的连通分量。 |
| 16 | Breadth-first Search | 广度优先搜索 | BFS | 按距起点边数从小到大遍历可达顶点。 |
| 17 | Depth-first Search | 深度优先搜索 | DFS | 沿未访问邻接顶点深入，再回溯继续探索。 |
| 18 | DFS Tree | 深度优先搜索树 |  | DFS 首次访问顶点所经树边组成的树。 |
| 19 | BFS Tree | 广度优先搜索树 |  | BFS 首次发现顶点形成的最少边数层次树。 |
| 20 | Topological Sorting | 拓扑排序 |  | 为有向无环图顶点建立满足所有有向边先后关系的线性序。 |
| 21 | Directed Acyclic Graph | 有向无环图 | DAG | 不存在有向环的有向图。 |
| 22 | Kahn Algorithm | Kahn 算法 |  | 不断移除入度为零的顶点得到 DAG 拓扑序。 |
| 23 | Tarjan SCC Algorithm | Tarjan 强连通分量算法 |  | 通过 DFS 时间戳与 low-link 值分解有向图强连通分量。 |
| 24 | Kosaraju Algorithm | Kosaraju 算法 |  | 用原图与转置图两轮 DFS 求强连通分量。 |
| 25 | Low-link Value | 最低可达时间戳 | low | DFS 树中子树经返祖边能到达的最小发现时间。 |
| 26 | Articulation Point | 割点 |  | 删除后使无向图连通分量数增加的顶点。 |
| 27 | Bridge | 桥 |  | 删除后使无向图连通分量数增加的边。 |
| 28 | Biconnected Component | 双连通分量 |  | 按指定顶点或边连通性定义的极大无割结构。 |
| 29 | Eulerian Trail | 欧拉迹 |  | 恰好经过图的每条边一次的迹。 |
| 30 | Eulerian Circuit | 欧拉回路 |  | 起点终点相同且经过每条边一次的闭合迹。 |
| 31 | Hierholzer Algorithm | Hierholzer 算法 |  | 通过拼接边不重复的回路构造欧拉迹或回路。 |
| 32 | Bipartite Graph | 二分图 |  | 顶点能划为两部分且每条边跨两部分的图。 |
| 33 | Bipartite Checking | 二分图判定 |  | 通过 BFS/DFS 二染色检测无向图是否二分。 |
| 34 | Graph Coloring | 图着色 |  | 为顶点分配颜色并满足相邻顶点颜色不同的约束任务。 |
| 35 | Shortest Path | 最短路径 |  | 在指定权重定义下总代价最小的起终点路径。 |
| 36 | Single-source Shortest Paths | 单源最短路径 | SSSP | 计算一个源点到所有可达顶点的最短距离。 |
| 37 | All-pairs Shortest Paths | 多源最短路径 | APSP | 计算所有顶点对之间的最短距离。 |
| 38 | Relaxation | 松弛操作 |  | 用经过中间顶点的候选路径更新已知距离上界。 |
| 39 | Bellman–Ford Algorithm | Bellman–Ford 算法 |  | 反复松弛边求单源最短路并检测可达负环。 |
| 40 | Floyd–Warshall Algorithm | Floyd–Warshall 算法 |  | 按中间顶点范围递增求所有点对最短路。 |
| 41 | Johnson Algorithm | Johnson 算法 |  | 通过重赋权加多次 Dijkstra 求稀疏图全源最短路。 |
| 42 | A* Search | A* 搜索 |  | 以当前路径代价与启发估计之和优先扩展结点的搜索方法。 |
| 43 | Admissible Heuristic | 可采纳启发函数 |  | 从不高估到目标真实剩余最优代价的启发估计。 |
| 44 | Consistent Heuristic | 一致启发函数 |  | 满足三角不等式型单调条件的 A* 启发函数。 |
| 45 | Bidirectional Search | 双向搜索 |  | 从起点和终点分别探索以缩小搜索区域。 |
| 46 | Zero-one BFS | 0-1 BFS |  | 使用双端队列求边权仅为 0 或 1 的最短路径。 |
| 47 | Shortest Path Tree | 最短路径树 |  | 连接源点及可达顶点且树路径均为最短路径的树。 |
| 48 | Negative-weight Cycle | 负权环 |  | 边权总和为负的有向环，使特定最短路问题无有限最优值。 |
| 49 | Graph Transpose | 转置图 |  | 将有向图所有边方向反转所得的图。 |
| 50 | Graph Condensation | 缩点图 |  | 把每个强连通分量收缩为单一顶点得到的 DAG。 |
| 51 | Minimum Cut | 最小割 |  | 在给定容量下划分顶点集合使跨割容量最小。 |
| 52 | Spanning Tree | 生成树 |  | 包含连通无向图全部顶点且无环的连通子图。 |
| 53 | Union-Find | 并查集 | DSU | 维护互不相交集合的合并与代表元查询结构。 |
| 54 | Path Compression | 路径压缩 |  | 查找集合代表元时直接连接祖先以缩短并查集路径。 |
| 55 | Union by Rank | 按秩合并 |  | 将并查集较浅树挂在较深树之下的策略。 |
| 56 | Union by Size | 按大小合并 |  | 将并查集较小集合挂到较大集合代表元之下。 |
| 57 | Minimum Spanning Forest | 最小生成森林 | MSF | 不连通图中每个连通分量的最小生成树集合。 |
| 58 | Offline Connectivity | 离线连通性 |  | 预先获得全部查询并通过重排操作高效回答连通关系。 |
| 59 | Dynamic Connectivity | 动态连通性 |  | 在边增删变化下维护或查询顶点连通性的任务。 |
| 60 | Graph Diameter | 图直径 |  | 所有可达顶点对最短距离的最大值，通常针对连通图定义。 |

## 09. 字符串算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | String Matching | 字符串匹配 |  | 在文本中寻找模式串全部或特定出现位置的任务。 |
| 2 | Pattern | 模式串 |  | 需要在文本序列中检索的目标字符序列。 |
| 3 | Text | 文本串 |  | 作为字符串匹配搜索范围的字符序列。 |
| 4 | Naive String Matching | 朴素字符串匹配 |  | 在每个候选位置逐字符比较模式串的算法。 |
| 5 | Prefix Function | 前缀函数 |  | 每个位置对应的最长真前缀且为后缀的长度。 |
| 6 | Knuth–Morris–Pratt Algorithm | KMP 算法 | KMP | 利用前后缀结构避免重复比较的线性时间字符串匹配算法。 |
| 7 | Failure Function | 失配函数 |  | 在匹配失败时指示下一可复用状态的辅助函数。 |
| 8 | Z-function | Z 函数 |  | 记录每个后缀与原字符串最长公共前缀的长度。 |
| 9 | Z Algorithm | Z 算法 |  | 线性时间计算 Z 函数的字符串算法。 |
| 10 | Rabin–Karp Algorithm | Rabin–Karp 算法 |  | 通过滚动哈希筛选匹配窗口并处理哈希冲突。 |
| 11 | Rolling Hash | 滚动哈希 |  | 根据已有窗口哈希快速计算相邻窗口哈希的技巧。 |
| 12 | Polynomial String Hash | 多项式字符串哈希 |  | 把字符序列映射为模整数的多项式求值结果。 |
| 13 | Hash Collision | 哈希碰撞 |  | 两个不同字符串取得相同哈希值的现象。 |
| 14 | Boyer–Moore Algorithm | Boyer–Moore 算法 |  | 从模式串尾部比较并利用失配规则跳过位置。 |
| 15 | Bad-character Rule | 坏字符规则 |  | 依据失配字符在模式串中的位置确定跳跃距离。 |
| 16 | Good-suffix Rule | 好后缀规则 |  | 利用已匹配后缀的重复结构计算移动距离。 |
| 17 | Aho–Corasick Automaton | AC 自动机 | AC | 结合 Trie 与失配链接实现多模式串同时匹配的自动机。 |
| 18 | Trie | 字典树 |  | 按字符逐层存储字符串前缀的树形索引。 |
| 19 | Suffix Array | 后缀数组 | SA | 按字典序排列文本所有后缀起始位置的数组。 |
| 20 | Suffix Tree | 后缀树 |  | 将字符串全部后缀以压缩 Trie 表示的索引结构。 |
| 21 | Suffix Automaton | 后缀自动机 | SAM | 识别某字符串全部子串的最小化有向无环确定自动机。 |
| 22 | Longest Common Prefix Array | 最长公共前缀数组 | LCP | 记录后缀数组相邻后缀最长公共前缀长度的数组。 |
| 23 | Kasai Algorithm | Kasai 算法 |  | 在线性时间内利用后缀数组计算 LCP 数组的算法。 |
| 24 | Burrows–Wheeler Transform | Burrows–Wheeler 变换 | BWT | 通过旋转排序构造易于压缩和索引的字符串变换。 |
| 25 | FM-index | FM 索引 |  | 基于 BWT 与秩查询支持压缩全文检索的索引。 |
| 26 | Palindromic Substring | 回文子串 |  | 正读与反读相同的连续字符片段。 |
| 27 | Manacher Algorithm | Manacher 算法 |  | 线性时间求字符串各中心最大回文半径的算法。 |
| 28 | Palindrome Tree | 回文树 | Eertree | 在线维护全部不同回文子串及其后缀关系的结构。 |
| 29 | Longest Palindromic Substring | 最长回文子串 |  | 寻找给定字符串中长度最大的连续回文片段。 |
| 30 | Lyndon Word | Lyndon 词 |  | 严格小于自身所有非平凡旋转的字符串。 |
| 31 | Duval Algorithm | Duval 算法 |  | 线性时间求字符串 Lyndon 分解的算法。 |
| 32 | Lexicographic Order | 字典序 |  | 按首个不同字符的次序比较字符串的全序。 |
| 33 | String Period | 字符串周期 |  | 使字符串在相应偏移位置重复一致的正整数。 |
| 34 | Minimal Rotation | 最小表示法 |  | 寻找字符串所有循环旋转中字典序最小的一种表示。 |
| 35 | Booth Algorithm | Booth 算法 |  | 线性时间求字符串字典序最小循环表示的算法。 |

## 10. 数论算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Greatest Common Divisor | 最大公约数 | GCD | 同时整除两个整数的最大正整数。 |
| 2 | Least Common Multiple | 最小公倍数 | LCM | 同时为两个整数倍数的最小正整数。 |
| 3 | Euclidean Algorithm | 欧几里得算法 |  | 通过反复取余求最大公约数。 |
| 4 | Extended Euclidean Algorithm | 扩展欧几里得算法 |  | 同时求 gcd 与贝祖等式的整数系数。 |
| 5 | Bézout Identity | 贝祖等式 |  | 整数 a,b 的最大公约数可表示为 ax+by。 |
| 6 | Modular Arithmetic | 模运算 |  | 按给定模数的同余类执行整数计算。 |
| 7 | Congruence Relation | 同余关系 |  | 两个整数之差可被给定模数整除的关系。 |
| 8 | Modular Inverse | 模逆元 |  | 满足 a×x 同余 1 的 x，仅在 gcd(a,m)=1 时存在。 |
| 9 | Modular Exponentiation | 模幂运算 |  | 高效计算大整数幂对指定模数取余的算法。 |
| 10 | Chinese Remainder Theorem | 中国剩余定理 | CRT | 在模数两两互素时合并同余约束并给出唯一同余类。 |
| 11 | Prime Number | 素数 |  | 恰有 1 与自身两个正因数的大于 1 的整数。 |
| 12 | Composite Number | 合数 |  | 大于 1 且存在非平凡因数的整数。 |
| 13 | Prime Factorization | 质因数分解 |  | 将正整数表示为若干素数幂的乘积。 |
| 14 | Trial Division | 试除法 |  | 枚举候选因数以判断素性或寻找因子。 |
| 15 | Sieve of Eratosthenes | 埃拉托斯特尼筛法 |  | 通过标记素数倍数找出范围内全部素数。 |
| 16 | Linear Sieve | 线性筛 |  | 使每个合数按最小素因子处理一次的筛法。 |
| 17 | Segmented Sieve | 分段筛 |  | 分批标记区间内合数以减小筛法内存开销。 |
| 18 | Euler Totient Function | 欧拉函数 | φ | 统计 1 到 n 中与 n 互素的正整数个数。 |
| 19 | Euler Theorem | 欧拉定理 |  | 在 a 与 n 互素时 a^φ(n) 对 n 同余于 1。 |
| 20 | Fermat Little Theorem | 费马小定理 |  | 若 p 为素数且 p 不整除 a，则 a^(p−1) 对 p 同余于 1。 |
| 21 | Miller–Rabin Primality Test | Miller–Rabin 素性检验 |  | 通过随机或选定底数检测强伪素数的算法。 |
| 22 | Probabilistic Primality Test | 概率素性检验 |  | 允许受控误判概率的素数判定方法。 |
| 23 | Pollard Rho Algorithm | Pollard Rho 分解算法 |  | 利用伪随机迭代及最大公约数寻找非平凡因子。 |
| 24 | Discrete Logarithm | 离散对数 |  | 在有限群中求使 g^x 等于目标元素的指数 x。 |
| 25 | Baby-step Giant-step | 大步小步算法 | BSGS | 利用时间空间折中求解离散对数。 |
| 26 | Modular Square Root | 模平方根 |  | 求满足 x² 同余 a（模 m）的整数同余类。 |
| 27 | Tonelli–Shanks Algorithm | Tonelli–Shanks 算法 |  | 在奇素数模数下求二次剩余平方根的算法。 |
| 28 | Multiplicative Order | 乘法阶 |  | 元素的幂首次回到单位元时的最小正指数。 |
| 29 | Mobius Function | 莫比乌斯函数 | μ | 基于整数素因子平方自由性定义的数论函数。 |
| 30 | Mobius Inversion | 莫比乌斯反演 |  | 由因子和形式恢复原算术函数的反演公式。 |

## 11. 随机化算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Randomized Algorithm | 随机化算法 |  | 在计算过程中使用随机比特或随机选择的算法。 |
| 2 | Las Vegas Algorithm | 拉斯维加斯算法 |  | 始终给出正确结果但运行时间受随机性影响的算法。 |
| 3 | Monte Carlo Algorithm | 蒙特卡洛算法 |  | 以受控错误概率换取确定计算预算的随机算法。 |
| 4 | Expected Running Time | 期望运行时间 |  | 对算法内部随机性或输入分布取平均的运行成本。 |
| 5 | Randomized Quick Sort | 随机化快速排序 |  | 随机选择枢轴以降低特定输入导致极端划分的风险。 |
| 6 | Randomized Selection | 随机选择算法 |  | 以随机枢轴反复划分寻找顺序统计量。 |
| 7 | Reservoir Sampling | 蓄水池抽样 |  | 从长度未知的数据流中等概率抽取固定数量样本。 |
| 8 | Fisher–Yates Shuffle | Fisher–Yates 洗牌 |  | 通过逐步均匀交换生成等概率随机排列。 |
| 9 | Random Permutation | 随机排列 |  | 从给定元素全部排列中按指定分布抽取一种排列。 |
| 10 | Pairwise Independent Hashing | 两两独立哈希 |  | 不同键的哈希值对满足成对独立条件的哈希族。 |
| 11 | Universal Hashing | 全域哈希 |  | 随机选择哈希函数以限制不同键碰撞概率的方法。 |
| 12 | Hash Family | 哈希函数族 |  | 可按规则选取的多个哈希映射的集合。 |
| 13 | Bloom Filter | 布隆过滤器 |  | 以少量位和多个哈希函数实现可能误报但不漏报的成员查询结构。 |
| 14 | Count–Min Sketch | Count–Min Sketch |  | 用多个哈希计数数组近似统计频次并给出单侧误差的流式概要。 |
| 15 | HyperLogLog | HyperLogLog |  | 利用哈希值前导零统计估计不同元素个数的算法。 |
| 16 | Skip List | 跳表 |  | 通过随机化多层索引提供期望对数查询与更新的数据结构。 |
| 17 | Random Walk | 随机游走 |  | 根据随机转移规则逐步移动状态的过程。 |
| 18 | Markov Chain | 马尔可夫链 |  | 下一状态分布只依赖当前状态的随机过程。 |
| 19 | MCMC | 马尔可夫链蒙特卡洛 | MCMC | 构造马尔可夫链以近似从复杂分布中采样的方法。 |
| 20 | Rejection Sampling | 拒绝采样 |  | 从易采样分布提议并按接受概率获得目标分布样本的方法。 |
| 21 | Importance Sampling | 重要性采样 |  | 从提议分布采样后通过权重估计目标分布期望。 |
| 22 | Chernoff Bound | Chernoff 界 |  | 给出独立随机变量和偏离期望的指数型尾概率界。 |
| 23 | Hoeffding Inequality | Hoeffding 不等式 |  | 控制有界独立随机变量均值偏差的概率上界。 |
| 24 | Probability Amplification | 概率放大 |  | 通过独立重复与投票降低随机算法错误概率。 |
| 25 | Random Seed | 随机种子 |  | 初始化伪随机数生成器状态以控制可复现序列的值。 |

## 12. 近似算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Approximation Algorithm | 近似算法 |  | 在多项式时间内寻找具有可证近似质量的可行解的算法。 |
| 2 | Approximation Ratio | 近似比 |  | 近似解目标值相对最优值的最坏质量保证指标。 |
| 3 | Approximation Guarantee | 近似保证 |  | 算法对所有合法输入给出的解质量下界或上界承诺。 |
| 4 | Constant-factor Approximation | 常数因子近似 |  | 近似比被与输入规模无关的常数界定。 |
| 5 | Polynomial-time Approximation Scheme | 多项式时间近似方案 | PTAS | 对每个固定精度参数可在多项式时间达到相应近似比的算法族。 |
| 6 | Fully Polynomial-time Approximation Scheme | 完全多项式时间近似方案 | FPTAS | 运行时间对输入规模与精度倒数均为多项式的近似方案。 |
| 7 | Vertex Cover Approximation | 顶点覆盖近似 |  | 为覆盖所有边选择顶点集合并保证相对于最优规模的上界。 |
| 8 | Set Cover Approximation | 集合覆盖近似 |  | 通过贪心等方法选择覆盖全部元素的近似最少集合。 |
| 9 | Metric TSP Approximation | 度量旅行商近似 |  | 利用三角不等式为最短巡回路线提供近似保证。 |
| 10 | Metric Space | 度量空间 |  | 配备非负、对称且满足三角不等式距离函数的集合。 |
| 11 | Triangle Inequality | 三角不等式 |  | 两点间距离不超过经任意第三点绕行的距离。 |
| 12 | Christofides Algorithm | Christofides 算法 |  | 对对称度量 TSP 给出 3/2 近似比的经典算法。 |
| 13 | Primal-dual Method | 原始—对偶方法 |  | 联合维护原问题和对偶问题的可行性或界以构造近似解。 |
| 14 | LP Relaxation | 线性规划松弛 |  | 放宽离散变量限制得到可多项式求解的线性规划。 |
| 15 | Integrality Gap | 整数性间隙 |  | 整数最优值与松弛最优值之间的最坏比值。 |
| 16 | Randomized Rounding | 随机舍入 |  | 按松弛解导出的概率将分数变量转化为离散决策。 |
| 17 | Deterministic Rounding | 确定性舍入 |  | 按确定规则将连续松弛解转换为离散可行解。 |
| 18 | Conditional Expectation Method | 条件期望法 |  | 通过逐项固定随机选择以保持期望目标界的去随机化技巧。 |
| 19 | Local Search Approximation | 局部搜索近似 |  | 反复改进局部邻域，并利用局部最优结构证明近似质量。 |
| 20 | Approximation-preserving Reduction | 保近似归约 |  | 将问题实例变换并控制近似解质量关系的归约。 |
| 21 | Max-Cut Approximation | 最大割近似 |  | 寻找跨割边权和接近最优的图划分算法。 |
| 22 | Submodular Function | 次模函数 |  | 满足边际收益递减性质的集合函数。 |
| 23 | Monotone Submodular Maximization | 单调次模最大化 |  | 在预算等约束下最大化非降次模集合函数的任务。 |
| 24 | Budgeted Maximum Coverage | 预算最大覆盖 |  | 在选择成本限制下尽可能覆盖最多加权元素。 |
| 25 | Bicriteria Approximation | 双准则近似 |  | 同时放松目标函数表现及约束满足程度的近似保证。 |

## 13. 计算复杂性理论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Computational Complexity Theory | 计算复杂性理论 |  | 研究不同计算问题所需资源与问题分类的理论。 |
| 2 | Decision Problem | 判定问题 |  | 要求对每个输入实例回答是或否的问题。 |
| 3 | Optimization Problem | 优化问题 |  | 在可行解集合中最小化或最大化目标函数的问题。 |
| 4 | Search Problem | 搜索问题 |  | 要求构造满足条件的对象而不仅回答是否存在的问题。 |
| 5 | Complexity Class | 复杂性类 |  | 依资源界限或计算模型定义的计算问题集合。 |
| 6 | Class P | P 类 | P | 可由确定性算法在多项式时间内解决的判定问题集合。 |
| 7 | Class NP | NP 类 | NP | 是实例具有可在多项式时间验证的证书的判定问题集合。 |
| 8 | Class co-NP | co-NP 类 | co-NP | 其补问题属于 NP 的判定问题集合。 |
| 9 | NP-hard | NP 困难 |  | 所有 NP 问题均可多项式时间归约到的问题的性质。 |
| 10 | NP-complete | NP 完全 |  | 同时属于 NP 且为 NP 困难的判定问题。 |
| 11 | Polynomial-time Reduction | 多项式时间归约 |  | 在多项式时间内将一个问题的实例转化为另一个问题的实例。 |
| 12 | Many-one Reduction | 多对一归约 |  | 通过单一计算变换将一个判定问题映射到另一问题。 |
| 13 | Turing Reduction | 图灵归约 |  | 可通过调用目标问题求解器若干次来解原问题的归约。 |
| 14 | Karp Reduction | Karp 归约 |  | 判定问题间可多项式计算的多对一归约。 |
| 15 | Cook–Levin Theorem | Cook–Levin 定理 |  | 证明布尔可满足性问题是 NP 完全问题的定理。 |
| 16 | Boolean Satisfiability | 布尔可满足性 | SAT | 判断布尔公式是否存在使其为真的赋值。 |
| 17 | 3-SAT | 三合取范式可满足性 | 3-SAT | 判断每个子句至多三个文字的合取范式是否可满足。 |
| 18 | Clique Problem | 团判定问题 |  | 判断图中是否存在至少 k 个顶点组成的完全子图。 |
| 19 | Independent Set Problem | 独立集判定问题 |  | 判断图中是否存在大小至少 k 的两两不相邻顶点集。 |
| 20 | Vertex Cover Problem | 顶点覆盖判定问题 |  | 判断图中是否存在至多 k 个顶点覆盖全部边。 |
| 21 | Hamiltonian Cycle Problem | 哈密顿环判定问题 |  | 判断图中是否存在访问每个顶点一次的环。 |
| 22 | Traveling Salesperson Problem | 旅行商问题 | TSP | 寻找访问指定城市并返回起点的最小代价巡回路线。 |
| 23 | Subset Sum Problem | 子集和判定问题 |  | 判断给定整数集合是否有子集的和为目标值。 |
| 24 | P versus NP Problem | P 与 NP 问题 |  | 询问可高效验证的判定问题是否都能高效求解的开放问题。 |
| 25 | Polynomial Hierarchy | 多项式层级 | PH | 通过交替存在与全称量词定义的一系列复杂性类。 |
| 26 | PSPACE | 多项式空间类 | PSPACE | 可用多项式空间解决的判定问题集合。 |
| 27 | EXPTIME | 指数时间类 | EXPTIME | 可由确定性算法在指数时间内求解的判定问题集合。 |
| 28 | Parameterized Complexity | 参数化复杂性 |  | 将问题成本表示为实例规模与附加参数函数的研究框架。 |
| 29 | Fixed-parameter Tractability | 固定参数可解性 | FPT | 可在 f(k)·n^O(1) 时间解决的参数化问题性质。 |
| 30 | W[1]-hardness | W[1] 困难性 |  | 参数化问题具有至少与 W[1] 类代表问题一样难的归约性质。 |
| 31 | Kernelization | 核化 |  | 在多项式时间内将实例压缩为大小仅依赖参数的等价实例。 |
| 32 | Fine-grained Complexity | 细粒度复杂性 |  | 研究多项式时间内部更精确的指数或幂次下界。 |
| 33 | Strong Exponential Time Hypothesis | 强指数时间假设 | SETH | 关于 k-SAT 随子句宽度增长无法统一突破特定指数底数的假设。 |
| 34 | Exponential Time Hypothesis | 指数时间假设 | ETH | 断言 3-SAT 不存在 2^o(n) 时间算法的常见复杂性假设。 |
| 35 | Communication Complexity | 通信复杂性 |  | 研究多个参与者分布持有输入时计算函数所需通信量的理论。 |

## 14. 网络流与匹配算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Flow Network | 流网络 |  | 边具有容量的有向图，通常指定源点与汇点。 |
| 2 | Flow | 网络流 |  | 满足容量限制和内部结点流量守恒的边上数值分配。 |
| 3 | Capacity | 容量 |  | 一条网络边允许通过的最大流量。 |
| 4 | Source Vertex | 源点 |  | 流从中进入网络的指定起始顶点。 |
| 5 | Sink Vertex | 汇点 |  | 流最终离开网络的指定终止顶点。 |
| 6 | Flow Conservation | 流量守恒 |  | 除源汇外每个顶点流入总量等于流出总量。 |
| 7 | Residual Network | 残量网络 |  | 表示沿边还能增加或撤回多少流量的网络。 |
| 8 | Residual Capacity | 残量容量 |  | 在给定流下沿残量边可额外推送的流量。 |
| 9 | Augmenting Path | 增广路径 |  | 残量网络中从源到汇的正残量路径。 |
| 10 | Ford–Fulkerson Method | Ford–Fulkerson 方法 |  | 反复沿增广路径增加流量直至无增广路的方法。 |
| 11 | Edmonds–Karp Algorithm | Edmonds–Karp 算法 |  | 通过 BFS 选最少边数增广路径求最大流。 |
| 12 | Dinic Algorithm | Dinic 算法 |  | 利用层次网络和阻塞流迭代求最大流。 |
| 13 | Level Graph | 层次图 |  | 按残量网络最短层数保留向下一层的可用边所得图。 |
| 14 | Blocking Flow | 阻塞流 |  | 使层次网络中不再存在源汇增广路径的流。 |
| 15 | Push–Relabel Algorithm | 推送重标记算法 |  | 通过预流、局部推送与高度标签求最大流。 |
| 16 | Preflow | 预流 |  | 允许内部顶点入流大于出流的中间流量配置。 |
| 17 | Maximum Flow | 最大流 |  | 在容量和守恒约束下可达到的最大源汇流量。 |
| 18 | Max-flow Min-cut Theorem | 最大流最小割定理 |  | 最大可行流量等于最小源汇割容量。 |
| 19 | Cut Capacity | 割容量 |  | 从割的源侧指向汇侧的全部边容量之和。 |
| 20 | Minimum-cost Flow | 最小费用流 |  | 在指定流量与容量约束下使运输成本最小的流。 |
| 21 | Successive Shortest Path Algorithm | 逐次最短路算法 |  | 反复在残量网络沿最小费用路径增广流量。 |
| 22 | Flow with Lower Bounds | 有下界网络流 |  | 对每条边同时给定允许流量下界与上界的流问题。 |
| 23 | Circulation | 循环流 |  | 没有净源汇、每个顶点满足流量守恒的可行流。 |
| 24 | Bipartite Matching | 二分图匹配 |  | 在二分图中选择顶点不重复的边集合。 |
| 25 | Maximum Matching | 最大匹配 |  | 在图中包含最多边的匹配。 |
| 26 | Perfect Matching | 完美匹配 |  | 覆盖图中所有顶点的匹配。 |
| 27 | Kőnig Theorem | Kőnig 定理 |  | 二分图的最大匹配边数等于最小顶点覆盖大小。 |
| 28 | Hall Marriage Theorem | Hall 婚配定理 |  | 二分图存在覆盖某侧全部顶点的匹配的充要条件。 |
| 29 | Hopcroft–Karp Algorithm | Hopcroft–Karp 算法 |  | 通过分层寻找多个最短增广路径求二分图最大匹配。 |
| 30 | Hungarian Algorithm | 匈牙利算法 |  | 利用势标与增广路径求解二分图加权指派问题。 |
| 31 | Assignment Problem | 指派问题 |  | 将任务与资源一一匹配并优化总成本的组合优化问题。 |
| 32 | Blossom Algorithm | 花算法 |  | 通过收缩奇环求一般无向图最大匹配。 |
| 33 | Alternating Path | 交替路 |  | 匹配边与非匹配边交替出现的路径。 |
| 34 | Matching Augmentation | 匹配增广 |  | 沿以未匹配顶点为端点的交替路翻转边成员提升匹配规模。 |
| 35 | Minimum Vertex Cover | 最小顶点覆盖 |  | 用最少顶点使每条边至少一个端点被选中的问题。 |

## 15. 高级数据结构与算法优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Segment Tree | 线段树 |  | 用树形层次组织区间聚合信息并支持更新与查询。 |
| 2 | Lazy Propagation | 懒标记下传 |  | 把区间更新延后记录、在需要访问子树时再传播的技巧。 |
| 3 | Fenwick Tree | 树状数组 | BIT | 以二进制最低位结构维护前缀可加总信息的数据结构。 |
| 4 | Sparse Table | 稀疏表 |  | 预处理固定区间的幂次长度答案以快速回答幂等区间查询。 |
| 5 | Range Minimum Query | 区间最小值查询 | RMQ | 查询数组指定区间中最小元素的任务。 |
| 6 | Range Sum Query | 区间求和查询 |  | 计算数组某个连续索引区间数值和的任务。 |
| 7 | Persistent Data Structure | 持久化数据结构 |  | 修改后仍可访问历史版本的数据结构。 |
| 8 | Persistent Segment Tree | 可持久化线段树 |  | 通过共享未变化节点保存多版本区间信息的线段树。 |
| 9 | Heavy-light Decomposition | 树链剖分 | HLD | 把树的路径划成对数条重链以进行区间查询。 |
| 10 | Lowest Common Ancestor | 最近公共祖先 | LCA | 根树中两个顶点共同祖先里深度最大的节点。 |
| 11 | Binary Lifting | 倍增法 |  | 预先维护 2 的幂次跳跃祖先以快速上跳或求 LCA。 |
| 12 | Euler Tour Technique | 欧拉序技巧 |  | 利用 DFS 进出时刻将树的子树映射到连续区间。 |
| 13 | Centroid Decomposition | 点分治 |  | 反复选择重心把树划分为较小子树以处理路径性质。 |
| 14 | Tree Diameter | 树的直径 |  | 树中任意两顶点之间最长简单路径的长度。 |
| 15 | Monotonic Stack | 单调栈 |  | 维护栈内元素单调性以快速求相邻更大或更小元素。 |
| 16 | Monotonic Deque | 单调双端队列 |  | 维护窗口候选元素单调性以快速求滑动最值。 |
| 17 | Sliding Window | 滑动窗口 |  | 维护随序列移动的连续区间及其统计信息。 |
| 18 | Two Pointers | 双指针 |  | 通过移动两个位置指针减少枚举或查找成本的技巧。 |
| 19 | Offline Algorithm | 离线算法 |  | 在已知全部输入或查询时重新排序处理以改善复杂度。 |
| 20 | Online Algorithm | 在线算法 |  | 在未来输入未知时按到达顺序即时进行计算或决策。 |
| 21 | Mo Algorithm | 莫队算法 |  | 按区间端点分块排序离线查询以减少窗口调整次数。 |
| 22 | Square Root Decomposition | 平方根分解 |  | 按约为 √n 的块大小平衡更新与查询成本。 |
| 23 | Disjoint Sparse Table | 不交稀疏表 |  | 预处理跨分块的前后缀合并值实现静态结合操作区间查询。 |
| 24 | Cartesian Tree | 笛卡尔树 |  | 同时满足原序列中序遍历次序与堆序性质的二叉树。 |
| 25 | Treap | 树堆 |  | 同时满足二叉搜索树键顺序和随机优先级堆性质的树。 |
| 26 | Splay Tree | 伸展树 |  | 通过旋转将近期访问元素移动至根并提供摊还对数操作的数据结构。 |
| 27 | Link-cut Tree | 动态树 | LCT | 用辅助伸展树维护动态森林路径聚合的结构。 |
| 28 | Binary Indexed Trie | 二进制字典树 |  | 按整数位组织键值，支持异或等按位查询的字典树。 |
| 29 | Li Chao Segment Tree | 李超线段树 |  | 维护一组直线或函数并回答指定横坐标极值查询的结构。 |
| 30 | Fractional Cascading | 分数级联 |  | 在相关有序表中共享定位信息以加速连续搜索的技巧。 |

## 核心概念辨析

| 概念 | 关键区别 |
|---|---|
| O / Ω / Θ | 分别表示渐近上界、下界与紧界。 |
| 贪心 / 动态规划 | 贪心依赖可证明的局部选择性质；动态规划比较并缓存子问题最优解。 |
| 分治 / 动态规划 | 分治子问题通常独立；动态规划利用重叠子问题。 |
| BFS / Dijkstra | BFS 用于等权或无权路径；Dijkstra 要求所有可用边权非负。 |
| NP-hard / NP-complete | NP 完全必须属于 NP 且 NP 困难；NP 困难不必属于 NP。 |
| 最短路径 / 最小生成树 | 前者优化指定路径代价；后者优化连通全部顶点的边权总和。 |
| 摊还 / 平均复杂度 | 摊还约束操作序列并不依赖随机分布；平均复杂度需指定输入分布。 |
| 最大流 / 最小割 | 最大流量与最小源汇割容量由最大流最小割定理联系。 |

## 中等难度面试与考试自测

### 1. 比较排序为何需要 Ω(n log n) 次比较？

参考答案：比较决策树需区分 n! 种排列，树高至少 log₂(n!)。

### 2. 0-1 背包的一维 DP 为什么逆序枚举容量？

参考答案：避免同一物品在本轮状态转移中被重复选择。

### 3. Dijkstra 为什么不能直接处理负边权？

参考答案：贪心确定当前最短距离的性质需要非负边权。

### 4. 如何证明 NP 完全性？

参考答案：证明属于 NP，再从已知 NP 完全问题给出保真假实例的多项式归约。

### 5. 最小生成树与最短路区别是什么？

参考答案：前者最小化连接全图的总边权；后者优化指定顶点间路径权值。

### 6. 二分图最大匹配怎样转成最大流？

参考答案：源到左侧、左右匹配边、右侧到汇点均赋单位容量，最大流即匹配规模。

## 参考资料

- Cormen, Leiserson, Rivest, Stein. *Introduction to Algorithms*, 4th ed. MIT Press, 2022.
- Kleinberg & Tardos. *Algorithm Design*. Pearson, 2005.
- Sedgewick & Wayne. *Algorithms*, 4th ed. Addison-Wesley, 2011.
- Skiena. *The Algorithm Design Manual*, 3rd ed. Springer, 2020.
- Princeton Algorithms: https://algs4.cs.princeton.edu/home/
- MIT OpenCourseWare: https://ocw.mit.edu/
- CP-Algorithms (补充材料): https://cp-algorithms.com/

> 本册为独立撰写的短定义和索引，不代表参考资料作者的审稿认可。
