# GPU Kernel / GPU 核函数 · GPU Kernel Engineering

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：255 条 · 专题：13 类**

CUDA, PTX, Triton, GPU programming and kernel performance

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与运行模型（16 条）
- 02. 硬件与线程执行层级（22 条）
- 03. 存储层级与硬件资源（24 条）
- 04. 访存行为与数据搬运（20 条）
- 05. 同步、并发与一致性（18 条）
- 06. 张量布局、分块与映射（20 条）
- 07. 矩阵运算与专用计算单元（19 条）
- 08. 数据精度与数值正确性（18 条）
- 09. 编译器、指令与代码生成（19 条）
- 10. Triton、CuTe 与 Kernel DSL（18 条）
- 11. 性能建模与优化指标（25 条）
- 12. 性能分析、诊断与调试（18 条）
- 13. 跨平台生态与 AI 常见核函数（18 条）

---

## 01. 基础概念与运行模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | GPU Kernel | GPU 核函数 |  | 在加速器设备端执行、由大量并行工作项共同运行的计算程序。 |
| 2 | Host | 主机端 |  | 通常指 CPU 侧代码，负责分配资源、准备数据及发起调用。 |
| 3 | Device | 设备端 |  | 指 GPU 等执行计算任务的加速器及其执行环境。 |
| 4 | Kernel Launch | 核函数启动 |  | 主机或设备将核函数提交给 GPU 执行的操作。 |
| 5 | Launch Configuration | 启动配置 |  | 指定网格、线程块、共享内存等运行参数。 |
| 6 | Execution Configuration | 执行配置 |  | CUDA 中描述网格维度和线程块维度等的配置。 |
| 7 | GPU Programming Model | GPU 编程模型 |  | 描述线程层次、存储空间和执行协作规则的抽象。 |
| 8 | Single Instruction, Multiple Threads (SIMT) | 单指令多线程 | SIMT | 多个逻辑线程以成组方式执行，线程可具有独立控制流。 |
| 9 | Single Instruction, Multiple Data (SIMD) | 单指令多数据 | SIMD | 单条指令对多个数据元素执行相同操作的计算方式。 |
| 10 | Data Parallelism | 数据并行 |  | 将同一计算应用到不同数据分片。 |
| 11 | Task Parallelism | 任务并行 |  | 同时执行不同任务或工作流。 |
| 12 | Throughput-oriented Architecture | 吞吐量导向架构 |  | 优先提高单位时间完成的总体工作量。 |
| 13 | Latency Hiding | 延迟隐藏 |  | 等待访存或依赖时切换到其他可运行工作以保持执行单元繁忙。 |
| 14 | Compute Capability | 计算能力版本 |  | NVIDIA 用于标识设备功能与指令支持范围的架构版本。 |
| 15 | Device Function | 设备函数 |  | 可在设备代码内调用、通常不能从主机直接启动的函数。 |
| 16 | Kernel Fusion | 核函数融合 |  | 把连续运算合并到一个核函数，减少中间数据和启动开销。 |

## 02. 硬件与线程执行层级

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Streaming Multiprocessor (SM) | 流式多处理器 | SM | NVIDIA GPU 的主要计算资源单元，包含调度器、寄存器及执行流水线。 |
| 2 | Compute Unit (CU) | 计算单元 | CU | AMD GPU 中与 SM 大致处于同一层级的硬件计算单元。 |
| 3 | Grid | 网格 |  | 一次 CUDA 核函数启动时包含的全部线程块。 |
| 4 | Thread Block | 线程块 |  | 可协作、共享块内共享内存并进行块级同步的线程集合。 |
| 5 | Cooperative Thread Array (CTA) | 协作线程阵列 | CTA | NVIDIA 文档中与线程块密切对应的术语。 |
| 6 | Thread Block Cluster | 线程块簇 |  | 在支持的架构上以簇组织多个线程块，提供更大协作范围。 |
| 7 | Warp | 线程束 |  | NVIDIA 中通常由 32 个线程组成的调度与执行分组。 |
| 8 | Wavefront | 波前 |  | AMD GPU 的执行分组；宽度可因架构而为 32 或 64。 |
| 9 | Lane | 通道／线程槽位 |  | 一个 Warp 或 Wavefront 中的逻辑线程位置。 |
| 10 | Lane ID | 通道编号 |  | 线程在其 Warp 或 Wavefront 内的位置索引。 |
| 11 | Thread ID | 线程编号 |  | 标识线程在线程块内部的位置。 |
| 12 | Block ID | 线程块编号 |  | 标识线程块在网格中的位置。 |
| 13 | Block Dimension | 线程块维度 |  | 线程块在 x、y、z 方向上的线程数。 |
| 14 | Grid Dimension | 网格维度 |  | 网格在 x、y、z 方向上的线程块数。 |
| 15 | Warp Scheduler | 线程束调度器 |  | 选择已就绪的 Warp 发射指令的硬件单元。 |
| 16 | Instruction Issue | 指令发射 |  | 调度器将指令交给执行流水线的过程。 |
| 17 | Resident Warp | 驻留线程束 |  | 已分配到 SM 资源、尚未结束的 Warp。 |
| 18 | Eligible Warp | 就绪线程束 |  | 操作数与执行条件满足、可发射下一条指令的 Warp。 |
| 19 | Active Mask | 活跃掩码 |  | 标识 Warp 中哪些 Lane 当前参与操作的位掩码。 |
| 20 | Thread Divergence | 线程分歧 |  | 同一 Warp 内不同线程走入不同分支，可能增加执行成本。 |
| 21 | Independent Thread Scheduling | 独立线程调度 |  | NVIDIA 特定架构起支持更灵活的 Warp 内线程执行状态管理。 |
| 22 | Persistent Kernel | 常驻式核函数 |  | 由有限工作块持续从任务队列取活的执行方式。 |

## 03. 存储层级与硬件资源

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Register | 寄存器 |  | 用于保存线程运算中的局部值，数量受硬件资源约束。 |
| 2 | Register File | 寄存器文件 |  | SM 或 CU 内承载寄存器状态的物理存储资源。 |
| 3 | Register Pressure | 寄存器压力 |  | 一个核函数的寄存器需求对驻留并行度形成的负担。 |
| 4 | Register Spill | 寄存器溢出 |  | 寄存器不够时，编译器将部分值放到较慢的存储位置。 |
| 5 | Local Memory (CUDA) | 局部内存（CUDA） |  | 线程私有的地址空间，常由设备内存承载；并非必然在片上。 |
| 6 | Shared Memory (CUDA) | 共享内存（CUDA） |  | 同一线程块内线程可共享的片上、软件管理存储。 |
| 7 | Local Data Share (LDS) | 本地数据共享存储 | LDS | AMD GPU 中类似 CUDA 共享内存的片上存储资源。 |
| 8 | Distributed Shared Memory (DSM) | 分布式共享内存 | DSM | 在支持线程块簇的架构上访问簇内其他块共享内存的机制。 |
| 9 | Global Memory | 全局内存 |  | 设备侧大容量地址空间，可由不同线程块访问。 |
| 10 | Device Memory | 设备内存 |  | GPU 可访问的设备侧内存，常由显存提供。 |
| 11 | High Bandwidth Memory (HBM) | 高带宽内存 | HBM | 用于高吞吐 GPU 的高带宽堆叠式存储技术。 |
| 12 | L1 Cache | 一级缓存 |  | 靠近计算单元的较小缓存，具体结构随架构变化。 |
| 13 | L2 Cache | 二级缓存 |  | 多个计算单元共享的缓存层，减少对外部显存的访问。 |
| 14 | Cache Line | 缓存行 |  | 缓存管理与数据传送的一种基本粒度。 |
| 15 | Shared Memory Bank | 共享内存存储体 |  | 共享内存被划分的并行访问单元，访问冲突会影响吞吐。 |
| 16 | Bank Conflict | 存储体冲突 |  | 并行线程访问映射到同一 Bank 的不同位置所造成的冲突。 |
| 17 | Memory Hierarchy | 存储层级 |  | 从寄存器、片上缓存到外部显存的多级组织。 |
| 18 | Memory Footprint | 内存占用规模 |  | 运算实际需要驻留或访问的数据大小。 |
| 19 | Memory Alignment | 内存对齐 |  | 数据地址符合访问或传输的边界要求。 |
| 20 | Pinned Host Memory | 页锁定主机内存 |  | 固定在物理内存中的主机缓冲区，常用于加速异步传输。 |
| 21 | Unified Memory | 统一内存 |  | 通过统一地址空间和迁移机制简化主机／设备数据管理。 |
| 22 | Page Migration | 页面迁移 |  | 内存页面在 CPU 与 GPU 等处理器之间转移。 |
| 23 | Memory Pool | 内存池 |  | 对分配的内存块进行缓存和复用，以减小频繁分配开销。 |
| 24 | Scratchpad Memory | 暂存存储器 |  | 软件可显式安排数据放置和复用的片上缓冲空间。 |

## 04. 访存行为与数据搬运

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Memory Coalescing | 合并访存 |  | 将同一 Warp 的多个相邻访问合并成较少内存事务。 |
| 2 | Coalesced Access | 合并式访问 |  | 地址布局有利于降低访存事务数的线程访问模式。 |
| 3 | Uncoalesced Access | 非合并式访问 |  | 地址分散，通常需要更多事务的访问模式。 |
| 4 | Strided Access | 跨步访问 |  | 相邻线程访问地址按固定间隔跳跃。 |
| 5 | Contiguous Access | 连续访问 |  | 相邻逻辑元素位于连续存储地址。 |
| 6 | Memory Transaction | 内存事务 |  | GPU 存储系统执行的一次数据读取或写入请求单位。 |
| 7 | Memory Sector | 内存扇区 |  | 某些 NVIDIA 缓存指标中的数据传输或访问粒度。 |
| 8 | Memory Bandwidth | 内存带宽 |  | 单位时间可传输的数据量，常以 GB/s 表示。 |
| 9 | Memory Latency | 内存访问延迟 |  | 从发起访存到数据可用所经历的时间。 |
| 10 | Effective Bandwidth | 有效带宽 |  | 根据有效读写字节数与实测耗时计算的传输速率。 |
| 11 | Global Load | 全局内存读取 |  | 从全局地址空间读取数据到线程执行资源。 |
| 12 | Global Store | 全局内存写入 |  | 将数据写回全局地址空间。 |
| 13 | Vectorized Load/Store | 向量化读写 |  | 单次指令搬运多个相邻元素的访存方法。 |
| 14 | Asynchronous Copy | 异步拷贝 |  | 发起数据传输后可与后续计算重叠，完成前需满足同步要求。 |
| 15 | Double Buffering | 双缓冲 |  | 用两组缓冲区交替加载与计算，减少等待。 |
| 16 | Multi-stage Pipeline | 多级流水线 |  | 在不同阶段并行组织加载、计算与写回。 |
| 17 | Prefetching | 预取 |  | 在实际使用之前提前请求数据。 |
| 18 | Data Reuse | 数据复用 |  | 多次使用已载入数据，减少重复访存。 |
| 19 | Cache Hit Rate | 缓存命中率 |  | 被目标缓存直接满足的访问比例。 |
| 20 | Read-Modify-Write (RMW) | 读改写 | RMW | 先读原值、计算新值再写回的操作模式。 |

## 05. 同步、并发与一致性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Barrier | 屏障 |  | 让参与线程在指定执行点等待，直至同步条件满足。 |
| 2 | Block Synchronization | 线程块同步 |  | 同一个线程块内线程在某同步点协调执行。 |
| 3 | Warp Synchronization | 线程束同步 |  | 对 Warp 范围内参与线程进行同步或顺序约束。 |
| 4 | Memory Fence | 内存栅栏 |  | 对存储操作的可见顺序施加约束，不等同于线程屏障。 |
| 5 | Memory Ordering | 内存顺序 |  | 描述不同线程之间读写操作允许的观察顺序。 |
| 6 | Memory Scope | 内存作用域 |  | 限定同步或原子操作影响的线程范围。 |
| 7 | Atomic Operation | 原子操作 |  | 对共享位置执行不可分割的读改写操作。 |
| 8 | Atomic Add | 原子加 |  | 在并发修改同一变量时原子地进行加法。 |
| 9 | Compare-and-Swap (CAS) | 比较并交换 | CAS | 当旧值满足比较条件时原子地写入新值。 |
| 10 | Race Condition | 竞态条件 |  | 结果依赖于不同线程操作时序的情形。 |
| 11 | Data Race | 数据竞争 |  | 缺少必要同步、对同一位置发生冲突访问的错误情形。 |
| 12 | Deadlock | 死锁 |  | 相互等待条件无法满足而导致执行无法推进。 |
| 13 | Asynchronous Execution | 异步执行 |  | 调用返回与任务实际完成可发生在不同时间。 |
| 14 | CUDA Stream | CUDA 流 |  | 规定提交命令之间顺序关系的执行队列。 |
| 15 | CUDA Event | CUDA 事件 |  | 用于流间依赖、时间测量或执行完成通知的标记。 |
| 16 | Concurrent Kernel Execution | 并发核函数执行 |  | 允许不同核函数在设备上重叠运行，受硬件与资源限制。 |
| 17 | CUDA Graph | CUDA 图 |  | 复用预先构建的操作依赖图，降低重复提交开销。 |
| 18 | Cooperative Groups | 协作线程组 |  | CUDA 中描述多种粒度线程协作的编程接口。 |

## 06. 张量布局、分块与映射

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Tensor | 张量 |  | 有形状、数据类型和存储布局的多维数据对象。 |
| 2 | Shape | 形状 |  | 张量各维度的元素数量。 |
| 3 | Stride | 步长 |  | 沿某维增加一个索引时，地址按元素或字节移动的距离。 |
| 4 | Row-major Layout | 行主序布局 |  | 一般把行内相邻元素连续存放的布局。 |
| 5 | Column-major Layout | 列主序布局 |  | 一般把列内相邻元素连续存放的布局。 |
| 6 | Contiguous Layout | 连续布局 |  | 元素按约定顺序紧密排列、没有额外间隔的布局。 |
| 7 | Blocked Layout | 分块布局 |  | 将逻辑数据分割后按线程或硬件层级分配的布局。 |
| 8 | Memory Swizzle | 存储重排／交错映射 |  | 改变地址映射，以改善访存或减少存储体冲突。 |
| 9 | Tiling | 分块计算 |  | 把大问题划分为适合缓存或片上存储的小块。 |
| 10 | Tile | 数据块／计算块 |  | 一次由线程组或矩阵指令处理的局部数据区域。 |
| 11 | Block Size | 块大小 |  | 描述线程数量或数据分块尺寸；需结合上下文区分。 |
| 12 | Tile Size | 分块尺寸 |  | 一次计算处理的数据块在各维度上的大小。 |
| 13 | Loop Tiling | 循环分块 |  | 重排循环结构以提升局部性和数据复用。 |
| 14 | Thread Mapping | 线程映射 |  | 把数据元素或计算任务映射到线程与 Warp 的方法。 |
| 15 | Thread Coarsening | 线程粗粒化 |  | 让每个线程承担更多元素或操作以降低调度开销。 |
| 16 | Vectorization | 向量化 |  | 将多次标量操作组合为向量指令或向量化访问。 |
| 17 | Broadcast | 广播 |  | 根据规则把较小形状的数据扩展参与逐元素计算。 |
| 18 | Reduction | 归约 |  | 按结合规则把一组元素合并为较少结果，例如求和。 |
| 19 | Scan / Prefix Sum | 扫描／前缀和 |  | 计算各位置之前元素的累积聚合结果。 |
| 20 | Transpose | 转置 |  | 交换张量的两个或多个维度，常涉及布局与搬运。 |

## 07. 矩阵运算与专用计算单元

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | General Matrix Multiply (GEMM) | 通用矩阵乘法 | GEMM | 计算矩阵乘积及可选加权累加的核心算子族。 |
| 2 | Matrix Multiply-Accumulate (MMA) | 矩阵乘加 | MMA | 专用指令完成矩阵块乘法并累加到结果。 |
| 3 | Fused Multiply-Add (FMA) | 融合乘加 | FMA | 在一次舍入语义下执行乘法和加法的组合操作。 |
| 4 | Tensor Core | 张量核心 |  | NVIDIA GPU 上面向矩阵运算的专用执行单元。 |
| 5 | Matrix Core | 矩阵核心 |  | AMD 等 GPU 文档中对矩阵计算专用硬件的称呼。 |
| 6 | MFMA | 矩阵融合乘加 |  | AMD GPU 指令体系中的矩阵乘加指令族。 |
| 7 | WMMA | Warp 级矩阵乘加 |  | NVIDIA 提供的 Warp 粒度矩阵运算接口／指令体系。 |
| 8 | WGMMA | Warpgroup 矩阵乘加 |  | 特定 NVIDIA 架构上的 Warpgroup 级矩阵乘加指令。 |
| 9 | Tensor Memory Accelerator (TMA) | 张量内存加速器 | TMA | 特定 NVIDIA 架构上支持张量块数据搬运的硬件机制。 |
| 10 | Warpgroup | 线程束组 |  | 由多个 Warp 组成、服务于某些矩阵指令的执行分组。 |
| 11 | Accumulator | 累加器 |  | 保存部分和或矩阵乘加中间结果的存储对象。 |
| 12 | Epilogue | 尾处理阶段 |  | 主计算完成后，对结果执行偏置、激活、缩放等操作。 |
| 13 | Prologue | 前处理阶段 |  | 核心计算前完成输入装载、变换或准备的阶段。 |
| 14 | Split-K | K 维拆分 |  | 将矩阵乘法的归约维拆成多个部分并行计算。 |
| 15 | Batched GEMM | 批量矩阵乘法 |  | 对一批矩阵对执行同类乘法计算。 |
| 16 | Grouped GEMM | 分组矩阵乘法 |  | 将尺寸或任务分布不同的多组矩阵乘法合并调度。 |
| 17 | Matrix Fragment | 矩阵片段 |  | 分配到线程／Warp 寄存器中的矩阵局部表示。 |
| 18 | Tensor Core Utilization | 张量核心利用率 |  | 反映矩阵专用执行资源使用程度的性能指标。 |
| 19 | Arithmetic Throughput | 算术吞吐量 |  | 单位时间可完成或实际完成的计算操作量。 |

## 08. 数据精度与数值正确性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | FP64 / Double Precision | 双精度浮点 |  | 通常指 IEEE 754 binary64 浮点格式。 |
| 2 | FP32 / Single Precision | 单精度浮点 |  | 通常指 IEEE 754 binary32 浮点格式。 |
| 3 | FP16 / Half Precision | 半精度浮点 |  | 常见的 16 位浮点格式，动态范围相对有限。 |
| 4 | BF16 / BFloat16 | 脑浮点 16 位 |  | 指数范围近似 FP32、尾数精度更低的 16 位格式。 |
| 5 | TF32 / TensorFloat-32 | TensorFloat-32 格式 |  | NVIDIA 用于矩阵计算的一类精度模式；并非普通 32 位存储类型。 |
| 6 | FP8 | 8 位浮点 |  | 一组低精度浮点编码格式，具体指数与尾数配置可不同。 |
| 7 | E4M3 | 4 指数 3 尾数格式 |  | 常见 FP8 变体之一，具体特殊值语义依实现或标准而定。 |
| 8 | E5M2 | 5 指数 2 尾数格式 |  | 常见 FP8 变体之一，强调较大的可表示范围。 |
| 9 | INT8 | 8 位整数 |  | 量化算子常用的 8 位整数类型。 |
| 10 | INT4 | 4 位整数 |  | 常用于压缩模型参数或低比特计算的整数表示。 |
| 11 | Mixed Precision | 混合精度 |  | 在不同阶段使用不同数值精度以兼顾速度与误差。 |
| 12 | Quantization | 量化 |  | 将连续或高精度数值映射到较低精度表示。 |
| 13 | Dequantization | 反量化 |  | 将量化表示依据比例尺等参数恢复到计算表示。 |
| 14 | Quantization Scale | 量化比例因子 |  | 建立量化值与实际数值关系的缩放参数。 |
| 15 | Rounding Mode | 舍入模式 |  | 控制不可精确表示结果如何取近似值的规则。 |
| 16 | Numerical Stability | 数值稳定性 |  | 算法面对舍入误差和输入扰动时保持可靠结果的能力。 |
| 17 | Accumulation Precision | 累加精度 |  | 归约或矩阵乘加中累积中间结果时使用的精度。 |
| 18 | ULP (Unit in the Last Place) | 末位单位 |  | 衡量相邻可表示浮点数间隔与误差的常用尺度。 |

## 09. 编译器、指令与代码生成

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | CUDA C++ | CUDA C++ |  | NVIDIA 用于编写设备程序的 C++ 扩展与运行时生态。 |
| 2 | PTX (Parallel Thread Execution) | 并行线程执行虚拟指令集 |  | NVIDIA 提供的 GPU 中间层虚拟 ISA 与汇编表示。 |
| 3 | SASS | GPU 原生机器指令 |  | NVIDIA GPU 目标架构上的实际机器指令表示。 |
| 4 | Instruction Set Architecture (ISA) | 指令集架构 | ISA | 软件可见的指令语义、编码和执行模型定义。 |
| 5 | Intermediate Representation (IR) | 中间表示 | IR | 编译优化与代码生成时使用的程序表达形式。 |
| 6 | LLVM IR | LLVM 中间表示 |  | LLVM 编译基础设施中的通用中间表示。 |
| 7 | MLIR | 多层级中间表示框架 |  | 可表达多种抽象层级和方言的编译器基础设施。 |
| 8 | NVVM IR | NVVM 中间表示 |  | NVIDIA CUDA 设备端编译链使用的一种 LLVM 系 IR。 |
| 9 | Triton IR | Triton 中间表示 |  | Triton 编译器用于表示及优化 Kernel 的中间层。 |
| 10 | JIT Compilation | 即时编译 |  | 程序运行阶段针对具体输入或设备生成可执行代码。 |
| 11 | AOT Compilation | 提前编译 |  | 在程序运行前生成目标代码或可部署编译产物。 |
| 12 | Specialization | 特化 |  | 针对形状、常量或硬件条件生成优化代码。 |
| 13 | Loop Unrolling | 循环展开 |  | 将循环迭代展开以减少控制开销并暴露优化机会。 |
| 14 | Instruction Scheduling | 指令调度 |  | 安排指令顺序以改善依赖与流水线利用。 |
| 15 | Instruction-Level Parallelism (ILP) | 指令级并行 | ILP | 同一线程或指令流中可独立推进的操作并行度。 |
| 16 | Peephole Optimization | 窥孔优化 |  | 针对一小段指令进行局部替换和简化。 |
| 17 | Constant Folding | 常量折叠 |  | 编译期计算已知常量表达式以减少运行时工作。 |
| 18 | Kernel Binary | 核函数二进制 |  | 可由驱动加载或执行的设备机器码及相关元数据。 |
| 19 | Disassembly | 反汇编 |  | 把机器码转为可阅读指令文本以检查实际执行路径。 |

## 10. Triton、CuTe 与 Kernel DSL

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Triton | Triton |  | 面向 GPU Kernel 的编程语言与编译工具链。 |
| 2 | Triton Kernel | Triton 核函数 |  | 以 Triton 编写、由编译器映射到目标 GPU 的核函数。 |
| 3 | Program Instance | 程序实例 |  | Triton 的独立执行实例，常处理一个逻辑数据块。 |
| 4 | program_id | 程序实例编号 |  | Triton 中获取当前程序实例在指定轴上编号的操作。 |
| 5 | num_programs | 程序实例数量 |  | Triton 中查询指定网格轴程序实例数的操作。 |
| 6 | arange | 连续索引生成 |  | Triton 中构造连续整数索引张量的操作。 |
| 7 | load / store | 加载／存储 |  | Triton 中显式从地址读取、向地址写入张量数据的操作。 |
| 8 | Masking | 掩码访问 |  | 用布尔条件屏蔽越界或不应参与的元素访问。 |
| 9 | constexpr | 编译期常量注解 |  | Triton 中标识可在编译期求值的参数或表达式。 |
| 10 | num_warps | Warp 数量参数 |  | Triton 常见的编译或启动配置，指定每程序实例的 Warp 数。 |
| 11 | num_stages | 流水阶段数参数 |  | 控制特定 Triton 流水化操作采用的阶段数量。 |
| 12 | tl.dot | 块矩阵乘法 |  | Triton 提供的矩阵块乘法操作。 |
| 13 | Autotuning | 自动调优 |  | 测试多组配置并选择实测表现较优方案的流程。 |
| 14 | Kernel DSL | 核函数领域专用语言 |  | 为 GPU 算子表达和优化设计的语言或高级接口。 |
| 15 | CUTLASS | CUTLASS |  | NVIDIA 的高性能矩阵运算模板与组件库。 |
| 16 | CuTe | CuTe 布局与张量抽象 |  | CUTLASS 体系中的布局代数、张量及算法抽象。 |
| 17 | Layout Algebra | 布局代数 |  | 用数学化映射描述逻辑坐标和物理存储分配。 |
| 18 | JIT Cache | 即时编译缓存 |  | 保存特化编译产物以避免相同配置反复编译。 |

## 11. 性能建模与优化指标

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Occupancy | 驻留率 |  | SM 中活跃 Warp 数与硬件最大可驻留 Warp 数之比。 |
| 2 | Theoretical Occupancy | 理论驻留率 |  | 由线程块规模与资源约束推算的驻留率上限。 |
| 3 | Achieved Occupancy | 实测驻留率 |  | 运行时采集的活跃 Warp 比例；可能低于理论值。 |
| 4 | GPU Utilization | GPU 利用率 |  | 设备忙碌程度的统计量，不能与 Occupancy 等同。 |
| 5 | Compute-bound | 计算受限 |  | 性能主要受计算执行资源或算术吞吐限制。 |
| 6 | Memory-bound | 访存受限 |  | 性能主要受访存带宽、延迟等存储系统因素限制。 |
| 7 | Launch-bound | 启动开销受限 |  | 核函数本身工作少，提交或调度开销占比显著。 |
| 8 | Arithmetic Intensity | 算术强度 |  | 计算操作量与数据搬运量之比，常用 FLOP/Byte。 |
| 9 | Roofline Model | 屋顶线模型 |  | 用峰值算力、存储带宽和算术强度推断性能上界。 |
| 10 | Peak FLOPS | 峰值浮点算力 |  | 理论上单位时间可执行的浮点操作量上限。 |
| 11 | Achieved FLOPS | 实际浮点吞吐量 |  | 依据运行时间与运算量计算的实测浮点性能。 |
| 12 | Throughput | 吞吐量 |  | 单位时间处理的数据、操作或任务数量。 |
| 13 | Latency | 时延 |  | 单次请求、核函数或操作从开始到结束的耗时。 |
| 14 | Speedup | 加速比 |  | 基线耗时与优化后耗时的比值。 |
| 15 | Memory Traffic | 内存流量 |  | 实际在指定存储层级发生的数据传输总量。 |
| 16 | Occupancy Limiter | 驻留率限制因素 |  | 寄存器、共享内存、线程数或块数等容量约束。 |
| 17 | Warp Stall | 线程束停顿 |  | Warp 因依赖、资源或同步条件未满足而不能发射。 |
| 18 | Stall Reason | 停顿原因 |  | 分析线程束等待内存、执行依赖或屏障等的类别。 |
| 19 | Instruction Dependency | 指令依赖 |  | 指令等待先前运算结果或状态满足的关系。 |
| 20 | Pipeline Utilization | 流水线利用率 |  | 执行流水线被有效使用的程度。 |
| 21 | Load Balancing | 负载均衡 |  | 尽量均匀地向执行资源分配工作。 |
| 22 | Kernel Launch Overhead | 核函数启动开销 |  | 提交、排队和调度核函数的额外时间成本。 |
| 23 | Benchmark Warm-up | 基准预热 |  | 正式计时前运行任务以减小编译或初始化等干扰。 |
| 24 | Microbenchmark | 微基准测试 |  | 聚焦测量单个算子、访问模式或微小代码片段。 |
| 25 | Performance Regression | 性能回退 |  | 变更后在相同测量条件下性能变差的现象。 |

## 12. 性能分析、诊断与调试

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Profiler | 性能分析器 |  | 收集时间、硬件计数器及执行轨迹的工具。 |
| 2 | Nsight Compute | Nsight Compute |  | NVIDIA 面向单个 GPU Kernel 的详细性能分析工具。 |
| 3 | Nsight Systems | Nsight Systems |  | NVIDIA 面向 CPU／GPU 时间线与系统交互的分析工具。 |
| 4 | Kernel Timeline | 核函数时间线 |  | 按时间展示提交、执行及并发情况的视图。 |
| 5 | Hardware Performance Counter | 硬件性能计数器 |  | 记录设备事件、事务和执行状态的硬件统计机制。 |
| 6 | Roofline Chart | 屋顶线图 |  | 展示算术强度与性能上界、实测点关系的图。 |
| 7 | Speed of Light (SOL) | 理论峰值利用指标 | SOL | Nsight Compute 中比较资源吞吐与理论峰值的分析视图。 |
| 8 | Memory Workload Analysis | 存储负载分析 |  | 通过访问数、缓存、带宽等指标定位存储瓶颈。 |
| 9 | Warp State Statistics | 线程束状态统计 |  | 分析就绪、发射和停顿状态及其比例。 |
| 10 | Source-level Profiling | 源码级性能分析 |  | 将性能数据映射到源代码行或指令。 |
| 11 | Sanitizer | 动态检查工具 |  | 检测越界、竞态或其他运行时正确性问题的工具。 |
| 12 | Compute Sanitizer | Compute Sanitizer |  | NVIDIA 的设备程序内存与同步错误检测工具。 |
| 13 | Racecheck | 竞态检查 |  | 对共享内存等访问中的数据竞争进行检测的检查器。 |
| 14 | Memcheck | 内存错误检查 |  | 发现越界、非法访问或其他内存使用问题的检查器。 |
| 15 | Assertion | 断言 |  | 运行时验证条件，不满足时报告失败。 |
| 16 | Golden Reference | 黄金参考实现 |  | 通常更直观、正确性优先的对照计算实现。 |
| 17 | Correctness Test | 正确性测试 |  | 验证输出、边界条件与数值容差是否满足要求。 |
| 18 | Reproducibility | 可复现性 |  | 记录软硬件版本、输入与测试条件，确保结果可重现。 |

## 13. 跨平台生态与 AI 常见核函数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | ROCm | ROCm |  | AMD 提供的 GPU 计算软件平台与工具链。 |
| 2 | HIP | HIP |  | 面向 AMD/NVIDIA 等 GPU 的 C++ 异构编程接口体系。 |
| 3 | Work-item | 工作项 |  | OpenCL 等模型中对应一个逻辑执行线程的工作单元。 |
| 4 | Work-group | 工作组 |  | OpenCL／HIP 等模型中可进行组内协作的工作项集合。 |
| 5 | Subgroup | 子组 |  | 图形与异构计算模型中小于工作组的协作分组。 |
| 6 | Wave32 / Wave64 | 32／64 通道波前 |  | AMD 不同架构或模式下的 Wavefront 宽度。 |
| 7 | VGPR | 向量通用寄存器 |  | AMD GPU 上保存各工作项私有向量数据的寄存器。 |
| 8 | SGPR | 标量通用寄存器 |  | AMD GPU 上存放波前共享标量状态的寄存器。 |
| 9 | VALU (Vector ALU) | 向量算术逻辑单元 |  | AMD GPU 中执行按通道并行算术运算的执行资源。 |
| 10 | SALU (Scalar ALU) | 标量算术逻辑单元 |  | AMD GPU 中处理波前共享标量运算的单元。 |
| 11 | Elementwise Kernel | 逐元素核函数 |  | 对张量每个元素分别进行相同运算的核函数。 |
| 12 | Softmax Kernel | Softmax 核函数 |  | 计算指数归一化，常结合分块归约与数值稳定处理。 |
| 13 | Layer Normalization | 层归一化 |  | 对选定维度统计均值方差后进行归一化的算子。 |
| 14 | RMS Normalization | 均方根归一化 |  | 用平方均值的根进行缩放的归一化算子。 |
| 15 | Attention Kernel | 注意力核函数 |  | 实现注意力得分、归一化与加权聚合的 GPU 核函数。 |
| 16 | FlashAttention | FlashAttention |  | 通过分块与片上复用减少中间注意力矩阵读写的算法族。 |
| 17 | KV Cache | 键值缓存 |  | 自回归推理中缓存历史注意力键和值的机制。 |
| 18 | Fused Operator | 融合算子 |  | 将多个计算阶段合并，以降低中间访存或调度开销。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/gpu-kernel.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
