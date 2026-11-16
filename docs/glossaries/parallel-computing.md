# 并行计算专有名词中英文对照表

# Parallel Computing · Chinese–English Technical Glossary

> TERM/ATLAS · 双语技术术语手册 · 2026-11-16

**205 条术语 · 12 个主题 · Markdown / PDF 对齐版本**

## 编写说明

以 Ananth Grama、Anshul Gupta、George Karypis、Vipin Kumar 的 *Introduction to Parallel Computing*（第二版，2003）为**知识结构参考**，围绕并行计算基础、体系结构、并行算法设计、通信、性能建模、MPI、共享内存与经典并行算法组织术语。GPU/CUDA、现代 MPI、OpenMP、集群可靠性等内容标注为扩展主题。**所有中文释义均为独立编写，不是对教材内容的逐句翻译或摘录。**

### 译名约定

- 中文优先采用高校教材与 HPC 工程文献中常见的译法；存在分歧时用斜杠保留常见异译。
- 缩写列可能是英文缩写、符号、API 名称；空白表示无统一缩写。
- `process`（进程）与 `processor`（处理器）、`concurrency`（并发）与 `parallelism`（并行）必须区分。
- MPI 标准、OpenMP 指令以及 CUDA 硬件术语以各自规范及具体实现版本为准。

## 目录

- 01. 并行计算基础与计算模型 / Foundations and Models（18 条；经典基础）
- 02. 并行体系结构与内存层次 / Architectures and Memory（18 条；经典基础）
- 03. 任务分解、映射与负载均衡 / Decomposition and Mapping（18 条；经典基础）
- 04. 通信、拓扑与数据交换 / Communication and Interconnects（19 条；经典基础）
- 05. 性能分析与可扩展性 / Performance and Scalability（18 条；经典基础）
- 06. MPI 消息传递编程 / MPI Programming（19 条；经典 + 规范扩展）
- 07. 共享内存编程与同步 / Shared Memory and Synchronization（19 条；经典 + 规范扩展）
- 08. 并行矩阵与数值计算 / Numerical Linear Algebra（15 条；经典算法）
- 09. 排序、图与组合搜索 / Sorting Graphs and Search（18 条；经典算法）
- 10. 并行 FFT 与频域算法 / FFT and Transform Algorithms（10 条；经典算法）
- 11. GPU、SIMD 与异构并行 / GPU and Heterogeneous Parallelism（17 条；现代扩展）
- 12. 分布式执行、可靠性与存储 / Distributed Execution and I/O（16 条；现代扩展）

## 常用性能公式

| 术语 | 公式 | 含义 |
|---|---|---|
| 加速比 Speedup | `S_p = T_1 / T_p` | 与等价串行执行时间比较的加速倍数。 |
| 并行效率 Efficiency | `E_p = S_p / p` | 使用 p 个处理器时的相对效率。 |
| 并行开销 Overhead | `T_o = p T_p - T_1` | 额外的处理器时间总量。 |
| 代价 Cost | `C_p = p T_p` | 并行计算的处理器时间总量。 |
| 阿姆达尔定律 Amdahl | `S_p <= 1 / (f + (1-f)/p)` | f 为不可并行比例，忽略额外并行开销。 |
| 工作量—跨度下界 | `T_p >= max(W/p, T_infinity)` | W 为总工作量，T_infinity 为关键路径长度。 |

> 注意：这些关系的适用前提需结合算法、测量方法与工作负载解释；不应把理论模型与硬件实测结果混为一谈。

---

## 01. 并行计算基础与计算模型（Foundations and Models）

> 经典基础 · 18 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Parallel Computing | 并行计算 | — | 多个计算资源同时协作解决计算问题。 |
| 2 | Concurrency | 并发 | — | 多个任务在时间上重叠推进，不要求同时执行。 |
| 3 | Parallelism | 并行性 | — | 多个操作在同一时刻实际执行。 |
| 4 | Sequential Computation | 顺序计算 | — | 按依赖顺序使用单个执行流计算。 |
| 5 | Parallel Algorithm | 并行算法 | — | 明确任务划分、依赖和协作方式的算法。 |
| 6 | Parallel Program | 并行程序 | — | 在并行平台执行的程序及其同步通信逻辑。 |
| 7 | Process | 进程 | — | 具有独立地址空间等资源的执行实体。 |
| 8 | Thread | 线程 | — | 进程内可被调度的执行流。 |
| 9 | Processing Element | 处理单元 | PE | 参与执行并行工作的抽象计算资源。 |
| 10 | Degree of Parallelism | 并行度 | — | 同一时刻可运行的任务数量。 |
| 11 | Task | 任务 | — | 可单独调度或分配的计算工作单元。 |
| 12 | Work | 总工作量 | W | 算法完成问题所执行的总体操作量。 |
| 13 | Span | 跨度 / 关键路径长度 | T∞ | 无限处理器条件下受依赖约束的最短执行时间。 |
| 14 | Work-Span Model | 工作量—跨度模型 | — | 用总工作量与关键路径刻画并行算法。 |
| 15 | PRAM | 并行随机访问机 | PRAM | 假设共享内存与同步访问的抽象并行模型。 |
| 16 | EREW PRAM | 互斥读互斥写 PRAM | EREW | 任一存储位置不能被并发读或写。 |
| 17 | CREW PRAM | 并发读互斥写 PRAM | CREW | 允许并发读同一位置，写操作互斥。 |
| 18 | CRCW PRAM | 并发读并发写 PRAM | CRCW | 允许并发读写，需规定写冲突的仲裁规则。 |

## 02. 并行体系结构与内存层次（Architectures and Memory）

> 经典基础 · 18 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Shared-Memory Architecture | 共享内存体系结构 | — | 多个执行单元通过共享地址空间交换数据。 |
| 2 | Distributed-Memory Architecture | 分布式内存体系结构 | — | 计算节点拥有独立内存，经通信网络交换数据。 |
| 3 | Hybrid-Memory Architecture | 混合内存体系结构 | — | 节点内共享内存、节点间消息通信的组合。 |
| 4 | Symmetric Multiprocessing | 对称多处理 | SMP | 多个处理器平等访问共享主存的系统设计。 |
| 5 | Non-Uniform Memory Access | 非统一内存访问 | NUMA | 访问延迟随处理器和内存位置而变化。 |
| 6 | Cache Coherence | 缓存一致性 | — | 保证不同缓存对共享位置的观察符合一致性协议。 |
| 7 | Memory Consistency Model | 内存一致性模型 | — | 规定不同线程内存操作可观察到的顺序。 |
| 8 | False Sharing | 伪共享 | — | 线程访问不同变量却落在同一缓存行，导致额外一致性流量。 |
| 9 | Cache Line | 缓存行 | — | 缓存与内存之间传输数据的基本粒度。 |
| 10 | Memory Hierarchy | 存储层次结构 | — | 寄存器、缓存、主存与外存等层次的组织。 |
| 11 | Memory Bandwidth | 内存带宽 | — | 单位时间内存子系统可传输的数据量。 |
| 12 | Memory Latency | 内存延迟 | — | 完成一次存储访问所需时间。 |
| 13 | Interconnection Network | 互连网络 | — | 连接并行处理器、节点与存储资源的通信基础设施。 |
| 14 | Network Topology | 网络拓扑 | — | 节点及连接链路的逻辑或物理结构。 |
| 15 | Hypercube | 超立方体网络 | — | 以二进制地址相邻关系连接节点的拓扑。 |
| 16 | Mesh Topology | 网格拓扑 | — | 节点按二维或更高维规则网格互连。 |
| 17 | Torus Topology | 环面拓扑 | — | 在网格基础上增加环绕连接的拓扑。 |
| 18 | Bisection Bandwidth | 二分带宽 | — | 网络被划为两部分时跨割边可提供的总带宽。 |

## 03. 任务分解、映射与负载均衡（Decomposition and Mapping）

> 经典基础 · 18 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Decomposition | 任务分解 | — | 把问题划分为可并行执行的子任务。 |
| 2 | Domain Decomposition | 区域分解 | — | 按输入数据或计算域的位置划分任务。 |
| 3 | Data Decomposition | 数据分解 | — | 依据数据子集分派计算。 |
| 4 | Functional Decomposition | 功能分解 | — | 按不同计算功能或阶段划分任务。 |
| 5 | Recursive Decomposition | 递归分解 | — | 递归拆分问题并生成子任务。 |
| 6 | Exploratory Decomposition | 搜索空间分解 | — | 将候选搜索路径分配给多个任务。 |
| 7 | Speculative Decomposition | 推测式分解 | — | 预先执行可能有用、但结果未必采用的分支。 |
| 8 | Task Graph | 任务图 | — | 以顶点表示任务、边表示依赖的有向图。 |
| 9 | Dependency Graph | 依赖图 | — | 描述操作间先后制约关系的图。 |
| 10 | Critical Path | 关键路径 | — | 任务图中决定最短完成时间的最长依赖链。 |
| 11 | Task Granularity | 任务粒度 | — | 每个任务承担计算工作的规模。 |
| 12 | Fine-Grained Parallelism | 细粒度并行 | — | 任务较小，调度与通信相对频繁。 |
| 13 | Coarse-Grained Parallelism | 粗粒度并行 | — | 任务较大，通信同步相对较少。 |
| 14 | Task Mapping | 任务映射 | — | 把任务分配到处理器或节点上的过程。 |
| 15 | Static Scheduling | 静态调度 | — | 运行前预先确定任务与计算资源的分配。 |
| 16 | Dynamic Scheduling | 动态调度 | — | 运行时依据负载和任务进展进行分配。 |
| 17 | Load Balancing | 负载均衡 | — | 让计算资源承担接近的工作量以减小空闲。 |
| 18 | Work Stealing | 工作窃取 | — | 空闲工作线程从其他线程的任务队列取得工作。 |

## 04. 通信、拓扑与数据交换（Communication and Interconnects）

> 经典基础 · 19 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Message Passing | 消息传递 | — | 进程间显式发送和接收数据的通信模型。 |
| 2 | Point-to-Point Communication | 点对点通信 | — | 两个参与进程之间交换消息。 |
| 3 | Collective Communication | 集合通信 | — | 某个通信组内多个进程共同参与的操作。 |
| 4 | Broadcast | 广播 | Bcast | 一个进程将同一数据发送给组内其他进程。 |
| 5 | Scatter | 散发 | Scatter | 根进程将不同数据片段分配给各进程。 |
| 6 | Gather | 聚集 | Gather | 多个进程将数据片段汇集至根进程。 |
| 7 | All-Gather | 全聚集 | Allgather | 所有进程获取每个进程提供的数据片段。 |
| 8 | Reduction | 归约 | Reduce | 按指定运算合并多个进程的数据。 |
| 9 | All-Reduce | 全归约 | Allreduce | 所有进程获得同一个归约结果。 |
| 10 | Reduce-Scatter | 归约后散发 | Reduce_scatter | 归约数组后将结果片段分给各进程。 |
| 11 | All-to-All | 全互换 | Alltoall | 每个进程向组内其他进程发送相应数据片段。 |
| 12 | Prefix Scan | 前缀扫描 | Scan | 每个进程获得其之前元素的累计归约结果。 |
| 13 | Exclusive Scan | 排他前缀扫描 | Exscan | 前缀结果排除当前进程的数据。 |
| 14 | Barrier Synchronization | 屏障同步 | Barrier | 参与者到达同步点后才继续推进。 |
| 15 | Halo Exchange | 边界 / 幽灵区交换 | — | 相邻域之间交换边界所需数据。 |
| 16 | Communication Latency | 通信延迟 | α | 消息通信的启动与固定开销。 |
| 17 | Per-Word Transfer Time | 单位字传输时间 | β | 常见 α–β 模型中的单位数据传输成本。 |
| 18 | Communication Volume | 通信数据量 | — | 通信过程传输的总数据大小。 |
| 19 | Communication-Computing Overlap | 通信与计算重叠 | — | 同时推进数据传输和独立计算以隐藏延迟。 |

## 05. 性能分析与可扩展性（Performance and Scalability）

> 经典基础 · 18 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Serial Execution Time | 串行执行时间 | T₁ | 完成同一工作负载的单处理器运行时间。 |
| 2 | Parallel Execution Time | 并行执行时间 | Tₚ | 使用 p 个处理器完成任务的运行时间。 |
| 3 | Speedup | 加速比 | Sₚ | 串行时间与并行时间之比 T₁/Tₚ。 |
| 4 | Parallel Efficiency | 并行效率 | Eₚ | 加速比除以处理器数 Sₚ/p。 |
| 5 | Total Parallel Overhead | 总并行开销 | Tₒ | pTₚ−T₁，反映通信、空闲和同步等额外代价。 |
| 6 | Cost of Parallel Algorithm | 并行算法代价 | — | 处理器数与并行运行时间的乘积 pTₚ。 |
| 7 | Cost-Optimality | 代价最优性 | — | 并行总代价与最优串行工作量同阶。 |
| 8 | Amdahl's Law | 阿姆达尔定律 | — | 固定工作负载加速比受不可并行部分限制。 |
| 9 | Gustafson's Law | 古斯塔夫森定律 | — | 在处理器数增加时扩大问题规模分析加速。 |
| 10 | Strong Scaling | 强扩展 | — | 固定问题规模，增加资源考察时间缩短程度。 |
| 11 | Weak Scaling | 弱扩展 | — | 每处理器负载近似固定，随处理器数量扩大问题。 |
| 12 | Scalability | 可扩展性 | — | 增加资源与问题规模时持续保持有效效率的能力。 |
| 13 | Isoefficiency Function | 等效率函数 | — | 为维持固定效率，问题规模应如何随处理器数增长。 |
| 14 | Overhead Function | 开销函数 | — | 描述并行附加开销随问题规模、处理器数的变化。 |
| 15 | Workload | 工作负载 | — | 程序需要处理的数据规模和计算需求。 |
| 16 | Load Imbalance | 负载不均衡 | — | 部分处理器因工作分配不均而等待。 |
| 17 | Superlinear Speedup | 超线性加速 | — | 观察到加速比大于处理器数，常由缓存等效应造成。 |
| 18 | Asymptotic Complexity | 渐近复杂度 | — | 刻画规模增长时工作量或时间的数量级。 |

## 06. MPI 消息传递编程（MPI Programming）

> 经典 + 规范扩展 · 19 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Message Passing Interface | 消息传递接口 | MPI | 定义进程间消息通信接口的标准。 |
| 2 | MPI Rank | MPI 进程编号 | rank | 进程在通信器内的编号，不等于物理节点编号。 |
| 3 | MPI Communicator | MPI 通信器 | comm | 定义通信组与隔离消息上下文的对象。 |
| 4 | MPI Group | MPI 进程组 | group | 一组有序进程标识，可用于创建通信器。 |
| 5 | MPI_Init | 初始化 MPI 环境 | MPI_Init | 启动 MPI 运行环境的函数。 |
| 6 | MPI_Finalize | 结束 MPI 环境 | MPI_Finalize | 完成 MPI 程序的运行时清理。 |
| 7 | MPI_Send | 阻塞发送 | MPI_Send | 发送缓冲区可再次使用前返回，具体协议依实现与模式。 |
| 8 | MPI_Recv | 阻塞接收 | MPI_Recv | 接收匹配消息并完成缓冲区的数据写入。 |
| 9 | MPI_Isend | 非阻塞发送 | MPI_Isend | 启动发送并返回请求句柄，完成需后续检测。 |
| 10 | MPI_Irecv | 非阻塞接收 | MPI_Irecv | 启动异步接收并返回请求句柄。 |
| 11 | MPI_Wait | 等待通信请求完成 | MPI_Wait | 等待指定非阻塞操作完成。 |
| 12 | MPI_Test | 测试通信请求 | MPI_Test | 查询通信是否完成而不必一直阻塞。 |
| 13 | MPI_Request | MPI 请求句柄 | MPI_Request | 代表非阻塞操作等待完成的对象。 |
| 14 | MPI_Status | MPI 通信状态 | MPI_Status | 记录接收来源、标签及错误等状态信息。 |
| 15 | MPI_Bcast | MPI 广播 | MPI_Bcast | 让根进程的数据分发到通信器内所有进程。 |
| 16 | MPI_Reduce | MPI 归约 | MPI_Reduce | 将组内数据合并到指定根进程。 |
| 17 | MPI_Allreduce | MPI 全归约 | MPI_Allreduce | 各进程得到归约后的结果。 |
| 18 | MPI Cartesian Topology | MPI 笛卡尔拓扑 | — | 按多维网格组织进程逻辑邻接关系。 |
| 19 | MPI One-Sided Communication | MPI 单边通信 | RMA | 通过远程内存访问操作读写其他进程窗口。 |

## 07. 共享内存编程与同步（Shared Memory and Synchronization）

> 经典 + 规范扩展 · 19 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Shared Address Space | 共享地址空间 | — | 线程可通过共同地址访问同一数据。 |
| 2 | Thread Creation | 线程创建 | — | 创建新的并发执行流。 |
| 3 | Mutex | 互斥锁 | mutex | 控制同一时刻仅一个线程进入受保护区域。 |
| 4 | Critical Section | 临界区 | — | 访问共享可变状态时须互斥执行的代码区。 |
| 5 | Race Condition | 竞态条件 | — | 程序结果依赖不可控的执行时序。 |
| 6 | Data Race | 数据竞争 | — | 未有足够同步的冲突内存访问，至少一个为写。 |
| 7 | Deadlock | 死锁 | — | 参与者相互等待资源，导致没有一个可以推进。 |
| 8 | Livelock | 活锁 | — | 参与者不断响应彼此但无法完成有效进展。 |
| 9 | Starvation | 饥饿 | — | 某任务长期得不到运行或所需资源。 |
| 10 | Atomic Operation | 原子操作 | — | 对并发观察者不可分割的操作。 |
| 11 | Compare-and-Swap | 比较并交换 | CAS | 按预期值条件原子更新共享位置。 |
| 12 | Memory Fence | 内存屏障 | — | 限制特定内存操作跨越屏障的重排。 |
| 13 | Condition Variable | 条件变量 | — | 线程等待共享状态满足条件的同步机制。 |
| 14 | Semaphore | 信号量 | — | 用计数许可约束并发访问或资源数量。 |
| 15 | Read-Write Lock | 读写锁 | RW lock | 允许多个读者或一个写者访问受保护资源。 |
| 16 | OpenMP | 开放多处理 | OpenMP | 共享内存并行编程指令、库与环境变量接口。 |
| 17 | Parallel Region | 并行区域 | — | OpenMP 创建团队执行的代码区域。 |
| 18 | Reduction Clause | 归约子句 | reduction | 为并行工作提供私有副本并合并其结果。 |
| 19 | Scheduling Clause | 调度子句 | schedule | 指定循环迭代如何分配给线程。 |

## 08. 并行矩阵与数值计算（Numerical Linear Algebra）

> 经典算法 · 15 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Dense Matrix | 稠密矩阵 | — | 多数元素需显式存储的矩阵表示。 |
| 2 | Sparse Matrix | 稀疏矩阵 | — | 零元素占大多数，常采用压缩存储。 |
| 3 | Matrix-Vector Multiplication | 矩阵—向量乘法 | SpMV / GEMV | 将矩阵作用于向量的线性代数运算。 |
| 4 | Matrix-Matrix Multiplication | 矩阵—矩阵乘法 | GEMM | 并行数值计算中常见的密集计算内核。 |
| 5 | Block Matrix Multiplication | 分块矩阵乘法 | — | 按子块组织乘法以改善数据局部性与并行性。 |
| 6 | Cannon's Algorithm | 坎农算法 | — | 二维处理器网格上的分块矩阵乘法方法。 |
| 7 | SUMMA | 可扩展通用矩阵乘法算法 | SUMMA | 通过行列广播实现分布式矩阵乘法。 |
| 8 | Matrix Transpose | 矩阵转置 | — | 交换矩阵行列，经常涉及跨节点数据重排。 |
| 9 | One-Dimensional Partitioning | 一维划分 | — | 沿矩阵某一个维度把数据分给计算单元。 |
| 10 | Two-Dimensional Partitioning | 二维划分 | — | 沿矩阵行列两个维度联合分布数据块。 |
| 11 | Row-Major Order | 行主序 | — | 以行连续的方式在内存存放二维数组。 |
| 12 | Column-Major Order | 列主序 | — | 以列连续的方式在内存存放二维数组。 |
| 13 | LU Factorization | LU 分解 | — | 将矩阵分解为下三角与上三角矩阵。 |
| 14 | Parallel Prefix Sum | 并行前缀和 | Scan | 计算全部前缀聚合结果的基础并行原语。 |
| 15 | Stencil Computation | 模板计算 | stencil | 按局部邻域访问规则更新数组网格点。 |

## 09. 排序、图与组合搜索（Sorting Graphs and Search）

> 经典算法 · 18 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Parallel Sorting | 并行排序 | — | 多个计算资源协同完成关键字排序。 |
| 2 | Bitonic Sort | 双调排序 | — | 通过固定比较交换网络对双调序列排序。 |
| 3 | Odd-Even Transposition Sort | 奇偶转置排序 | — | 交替比较相邻奇偶位置元素的并行排序。 |
| 4 | Sample Sort | 样本排序 | — | 基于采样枢轴分桶并行排序数据。 |
| 5 | Parallel Merge | 并行归并 | — | 并行合并两个有序序列。 |
| 6 | Graph Traversal | 图遍历 | — | 按图结构系统性地访问顶点和边。 |
| 7 | Breadth-First Search | 广度优先搜索 | BFS | 逐层扩展图中的未访问邻居。 |
| 8 | Depth-First Search | 深度优先搜索 | DFS | 沿分支深入并在必要时回溯。 |
| 9 | Parallel BFS | 并行广度优先搜索 | — | 并行处理前沿集合和邻接关系。 |
| 10 | Frontier | 搜索前沿 | — | 当前迭代待扩展的顶点或状态集合。 |
| 11 | Graph Partitioning | 图划分 | — | 把顶点划为子集，同时尽量减少跨分区连接。 |
| 12 | Edge Cut | 割边数 | — | 不同图分区之间连接边的数量。 |
| 13 | Single-Source Shortest Path | 单源最短路径 | SSSP | 计算一个源点到可达顶点的最短距离。 |
| 14 | Minimum Spanning Tree | 最小生成树 | MST | 连通加权无向图的最小总权生成树。 |
| 15 | Branch and Bound | 分支定界 | — | 利用上下界剪除不可能得到更优解的搜索分支。 |
| 16 | Backtracking | 回溯 | — | 逐步尝试候选决策，失败时撤销并返回。 |
| 17 | Dynamic Programming | 动态规划 | DP | 利用重叠子问题与最优子结构复用结果。 |
| 18 | Wavefront Computation | 波前计算 | — | 按依赖对角线等前沿逐层并行推进状态。 |

## 10. 并行 FFT 与频域算法（FFT and Transform Algorithms）

> 经典算法 · 10 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Discrete Fourier Transform | 离散傅里叶变换 | DFT | 把离散序列映射到频域的线性变换。 |
| 2 | Fast Fourier Transform | 快速傅里叶变换 | FFT | 利用分治结构降低 DFT 计算复杂度。 |
| 3 | Inverse FFT | 逆快速傅里叶变换 | IFFT | 将频域系数高效还原到时域。 |
| 4 | Butterfly Operation | 蝶形运算 | — | FFT 分治阶段组合两个子变换结果的基本操作。 |
| 5 | Cooley–Tukey Algorithm | 库利—图基算法 | — | 通过分解变换规模实现 FFT 的算法族。 |
| 6 | Radix-2 FFT | 基 2 FFT | — | 每阶段按二路分解的 FFT 实现。 |
| 7 | Bit-Reversal Permutation | 位逆序置换 | — | 按二进制下标位顺序反转以重排数据。 |
| 8 | Twiddle Factor | 旋转因子 | — | FFT 中用于组合子变换的复指数系数。 |
| 9 | Distributed FFT | 分布式 FFT | — | 把 FFT 数据与计算分布到多个进程执行。 |
| 10 | All-to-All Transpose | 全互换转置 | — | 分布式多维 FFT 中常见的全局数据重排。 |

## 11. GPU、SIMD 与异构并行（GPU and Heterogeneous Parallelism）

> 现代扩展 · 17 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | Single Instruction Multiple Data | 单指令多数据 | SIMD | 一条指令对多个数据元素执行同类运算。 |
| 2 | Single Instruction Multiple Threads | 单指令多线程 | SIMT | GPU 以线程组组织并执行相同内核代码的模型。 |
| 3 | GPU Kernel | GPU 内核函数 | kernel | 由加速设备上大量线程执行的计算函数。 |
| 4 | Thread Block | 线程块 | block | GPU 中协作执行、共享块内资源的线程集合。 |
| 5 | Grid | 线程网格 | grid | 一次 GPU 内核启动创建的线程块集合。 |
| 6 | Warp | 线程束 | warp | NVIDIA GPU 上以 32 个线程组织的调度执行组。 |
| 7 | Warp Divergence | 线程束分歧 | — | 同一 warp 内线程选择不同控制流，可能降低效率。 |
| 8 | Occupancy | 占用率 | — | 活跃线程束数相对硬件最大可驻留线程束数的比例。 |
| 9 | Coalesced Memory Access | 合并内存访问 | — | 相邻线程的访问被整合为高效内存事务。 |
| 10 | Shared Memory on GPU | GPU 共享内存 | — | 线程块内用于低延迟交换数据的片上存储。 |
| 11 | Global Memory on GPU | GPU 全局内存 | — | 对设备上多个线程块可访问的设备内存。 |
| 12 | Host-Device Transfer | 主机—设备传输 | — | CPU 内存与加速器内存之间的数据拷贝。 |
| 13 | Asynchronous Kernel Launch | 异步内核启动 | — | 启动后主机无需等待内核完成即可继续执行。 |
| 14 | CUDA Stream | CUDA 流 | stream | 设备操作的有序队列，可实现并发与重叠。 |
| 15 | Tensor Core | 张量核心 | — | 针对矩阵乘加等运算优化的 GPU 计算单元。 |
| 16 | Roofline Model | 屋顶线模型 | — | 用计算强度、带宽与峰值算力分析性能上限。 |
| 17 | Arithmetic Intensity | 计算强度 | — | 浮点运算量与数据传输字节数之比。 |

## 12. 分布式执行、可靠性与存储（Distributed Execution and I/O）

> 现代扩展 · 16 条术语

| # | English term | 中文译名 | 缩写 / 符号 | 简明释义 |
|---:|---|---|---|---|
| 1 | High-Performance Computing | 高性能计算 | HPC | 以高吞吐、低时延和大规模数值处理为目标的计算。 |
| 2 | Compute Cluster | 计算集群 | — | 通过网络连接的一组协同计算节点。 |
| 3 | Compute Node | 计算节点 | — | 集群中负责运行计算任务的机器。 |
| 4 | Job Scheduler | 作业调度器 | — | 为批处理任务分配集群资源并管理队列。 |
| 5 | Batch Job | 批处理作业 | — | 以非交互方式提交并由调度系统执行的任务。 |
| 6 | Checkpointing | 检查点保存 | — | 周期性保存运行状态以便失败后恢复。 |
| 7 | Fault Tolerance | 容错性 | — | 硬件或软件部分故障后继续提供正确结果的能力。 |
| 8 | Resilience | 韧性 / 抗故障能力 | — | 系统从扰动与故障中维持或恢复服务的能力。 |
| 9 | Parallel I/O | 并行输入输出 | — | 多个进程协同读写存储以提高吞吐。 |
| 10 | MPI-IO | MPI 并行 I/O | MPI-IO | MPI 标准提供的并行文件操作接口。 |
| 11 | Collective I/O | 集合 I/O | — | 多个进程协调文件访问以减少碎片化操作。 |
| 12 | HDF5 | 层次化数据格式 5 | HDF5 | 科学数据管理的格式与库，可用于并行 I/O。 |
| 13 | Performance Profiling | 性能剖析 | — | 记录函数、内核或通信开销以定位瓶颈。 |
| 14 | Tracing | 运行轨迹采集 | — | 记录事件时间线以分析任务依赖与通信重叠。 |
| 15 | Benchmarking | 基准测试 | — | 通过可重复负载比较实现或硬件的性能。 |
| 16 | Reproducibility | 可复现性 | — | 在明确环境与配置下重现可验证的实验结果。 |

---

## 术语辨析（易混淆项）

- **并发 vs 并行：** 并发描述任务推进时间相互重叠；并行要求在同一时刻实际执行多个操作。
- **进程 vs 线程 vs 处理器：** 进程/线程是软件执行抽象；处理器或处理单元是计算资源，映射不必一一对应。
- **共享内存 vs 分布式内存：** 区别在于是否共享地址空间，而不只是是否运行在同一机柜。
- **阻塞 vs 非阻塞通信：** 非阻塞调用通常先返回请求句柄；不代表操作已经完成，也不保证自动通信与计算重叠。
- **加速比 vs 效率 vs 可扩展性：** 分别度量时间改善、资源利用相对程度、以及规模变化下的性能变化。
- **竞态条件 vs 数据竞争：** 数据竞争是一类涉及未正确同步的冲突内存访问；竞态条件含义更广。
- **SIMD vs SIMT：** SIMD 用一条指令操作多个数据元素；SIMT 用多个线程执行内核，允许不同线程具有各自控制流。

## 参考来源

1. Grama, A.; Gupta, A.; Karypis, G.; Kumar, V. *Introduction to Parallel Computing*, 2nd ed. Addison-Wesley, 2003. 章节范围参考：[Purdue CS525 课程](https://www.cs.purdue.edu/homes/ayg/CS525/lectures.html)。
2. MPI Forum. [MPI 官方标准文档](https://www.mpi-forum.org/docs/)（查看当前适用版本）。
3. OpenMP ARB. [OpenMP API Specifications](https://www.openmp.org/specifications/)。
4. NVIDIA. [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)。

## 贡献方式

欢迎在 [1998x-stack/bilingual-technical-glossary](https://github.com/1998x-stack/bilingual-technical-glossary) 通过 Issue / Pull Request 提出译名、定义、分类和规范引用建议。建议提交：英文原词、中文译名、参考出处、所在章节及修改理由。

**发布文件：** [Markdown](../glossaries/parallel-computing.md) · [PDF](../pdf/parallel-computing.pdf)  |  **维护状态：** 社区共建草案（非官方规范）
