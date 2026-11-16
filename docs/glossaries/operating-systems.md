# 操作系统专有名词中英文对照表

> Operating Systems · Bilingual Technical Glossary

**版本：** 1.0 · **更新日期：** 2026-11-16 · **章节：** 18 · **术语：** 396

## 使用说明

- 中文列优先采用计算机系统课程、Unix/Linux 文档中的常见译名；存在多个译名时采用“主译名 / 常见别名”。
- “简明释义”用于区分概念，不是标准规范的完整定义；缩写以英文原词为准。
- Linux 工具、API 与具体内核机制会随版本变化；阅读实现时应结合相应版本的文档和源码。

## 目录

- [01 操作系统基础与内核](#01-操作系统基础与内核)
- [02 启动、异常与系统调用](#02-启动-异常与系统调用)
- [03 进程、线程与执行上下文](#03-进程-线程与执行上下文)
- [04 CPU 调度与执行策略](#04-CPU-调度与执行策略)
- [05 并发、同步与内存一致性](#05-并发-同步与内存一致性)
- [06 死锁与资源分配](#06-死锁与资源分配)
- [07 内存管理基础](#07-内存管理基础)
- [08 分页、虚拟内存与地址转换](#08-分页-虚拟内存与地址转换)
- [09 文件系统与命名空间](#09-文件系统与命名空间)
- [10 输入输出与设备管理](#10-输入输出与设备管理)
- [11 磁盘、存储与持久性](#11-磁盘-存储与持久性)
- [12 隔离、保护与系统安全](#12-隔离-保护与系统安全)
- [13 进程间通信与网络接口](#13-进程间通信与网络接口)
- [14 虚拟化、容器与云原生](#14-虚拟化-容器与云原生)
- [15 Unix / Linux 关键概念](#15-Unix-Linux-关键概念)
- [16 实时系统与嵌入式系统](#16-实时系统与嵌入式系统)
- [17 性能分析与可观测性](#17-性能分析与可观测性)
- [18 分布式操作系统与高级机制](#18-分布式操作系统与高级机制)

---

## 01 操作系统基础与内核

*Operating System Fundamentals · 22 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Operating System (OS) | 操作系统 | 管理硬件资源并为应用程序提供抽象和服务的软件系统 |
| Kernel | 内核 | 运行于特权级、提供操作系统核心机制的程序部分 |
| Kernel Space | 内核空间 | 内核代码和数据所在的受保护地址空间范围 |
| User Space | 用户空间 | 普通应用程序运行的非特权执行环境 |
| User Mode | 用户态 | CPU 处于非特权执行模式的状态 |
| Kernel Mode | 内核态 | CPU 可执行特权指令的运行模式 |
| Privilege Level | 特权级 | 处理器对不同执行环境设置的权限层级 |
| Supervisor Mode | 监管模式 | 处理器架构中的特权执行模式名称之一 |
| Hardware Abstraction | 硬件抽象 | 向软件屏蔽具体硬件实现细节 |
| Resource Management | 资源管理 | 分配与回收 CPU、内存、设备等资源 |
| Multiprogramming | 多道程序设计 | 让多个程序驻留内存并交替利用处理器 |
| Multitasking | 多任务处理 | 在多个任务之间调度执行资源 |
| Time Sharing | 分时 | 以时间片轮转等机制提高交互性 |
| Batch Processing | 批处理 | 按批次自动执行作业、通常减少人工干预 |
| Monolithic Kernel | 宏内核 | 大部分操作系统服务运行于内核空间 |
| Microkernel | 微内核 | 将内核功能缩至少量基础机制的架构 |
| Hybrid Kernel | 混合内核 | 结合宏内核与微内核设计特征的架构 |
| Exokernel | 外核 | 尽量安全地将硬件资源控制权交给应用的架构 |
| Kernel Module | 内核模块 | 可按需加载的内核功能组件 |
| Application Binary Interface (ABI) | 应用程序二进制接口 | 规定调用约定、数据布局等二进制兼容规则 |
| Application Programming Interface (API) | 应用程序编程接口 | 供程序调用的软件接口规范 |
| Portability | 可移植性 | 软件适配不同硬件和操作系统的能力 |

## 02 启动、异常与系统调用

*Boot, Traps & System Calls · 20 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Boot Process | 启动过程 | 从上电到操作系统可提供服务的执行流程 |
| Firmware | 固件 | 存储在设备中的低层控制程序 |
| BIOS | 基本输入输出系统 | 传统 PC 固件接口与启动环境 |
| UEFI | 统一可扩展固件接口 | 现代计算机固件与引导接口规范 |
| Bootloader | 引导加载程序 | 定位并加载操作系统内核的程序 |
| Secure Boot | 安全启动 | 对引导链中的组件实施签名验证的机制 |
| Kernel Image | 内核映像 | 供引导程序加载的内核二进制文件 |
| Initial RAM Disk (initrd) | 初始内存磁盘 | 在早期启动阶段提供临时文件系统的映像 |
| Initial RAM Filesystem (initramfs) | 初始内存文件系统 | 内核早期启动使用的临时根文件系统 |
| System Initialization | 系统初始化 | 建立驱动、服务和用户态环境的阶段 |
| System Call | 系统调用 | 用户程序请求内核服务的受控入口 |
| System Call Interface | 系统调用接口 | 系统调用编号、参数与返回约定 |
| Trap | 陷入 | 同步地转入特权处理程序的控制转移 |
| Exception | 异常 | 由当前指令执行引起的同步事件 |
| Interrupt | 中断 | 硬件等异步事件触发的处理器控制转移 |
| Interrupt Handler | 中断处理程序 | 响应中断并执行相应处理的代码 |
| Interrupt Vector | 中断向量 | 用于定位中断或异常处理入口的信息 |
| Interrupt Service Routine (ISR) | 中断服务例程 | 处理中断事件的例程 |
| Fault | 故障型异常 | 通常可在处理后重试引发异常的指令 |
| Double Fault | 双重故障 | 处理异常期间再次发生特定异常的情况 |

## 03 进程、线程与执行上下文

*Processes, Threads & Context · 26 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Program | 程序 | 存储的指令和数据，本身不等于正在执行的进程 |
| Process | 进程 | 拥有独立资源与执行状态的程序实例 |
| Thread | 线程 | 进程内部可独立调度的执行流 |
| Task | 任务 | 系统中可调度执行实体的泛称 |
| Process Identifier (PID) | 进程标识符 | 操作系统分配给进程的标识 |
| Thread Identifier (TID) | 线程标识符 | 标识线程的编号，具体作用域依系统而异 |
| Process Control Block (PCB) | 进程控制块 | 记录进程状态和调度信息的内核数据结构 |
| Thread Control Block (TCB) | 线程控制块 | 记录线程执行上下文的管理结构 |
| Process State | 进程状态 | 运行、就绪、阻塞等生命周期状态 |
| Ready State | 就绪态 | 具备运行条件、等待 CPU 调度的状态 |
| Running State | 运行态 | 当前正在处理器上执行的状态 |
| Blocked State | 阻塞态 | 等待事件、资源或 I/O 完成的状态 |
| Zombie Process | 僵尸进程 | 已终止但退出状态尚未被父进程回收的进程 |
| Orphan Process | 孤儿进程 | 父进程退出后由其他进程接管的子进程 |
| Parent Process | 父进程 | 创建子进程的进程 |
| Child Process | 子进程 | 由其他进程创建的进程 |
| Process Creation | 进程创建 | 建立新进程及其管理信息的过程 |
| Process Termination | 进程终止 | 结束执行并释放或待回收资源的过程 |
| Context Switch | 上下文切换 | 保存一个执行实体状态并恢复另一个的过程 |
| CPU Context | CPU 上下文 | 寄存器、程序计数器等执行状态 |
| Stack | 栈 | 支持函数调用、局部变量等的后进先出存储区域 |
| Kernel Stack | 内核栈 | 线程在内核态执行时使用的栈 |
| User-Level Thread | 用户级线程 | 主要由用户态运行时管理的线程 |
| Kernel-Level Thread | 内核级线程 | 由内核直接感知与调度的线程 |
| Thread-Local Storage (TLS) | 线程局部存储 | 为每个线程单独保存变量的机制 |
| Reentrancy | 可重入性 | 代码在执行未结束时再次调用仍能正确工作 |

## 04 CPU 调度与执行策略

*CPU Scheduling · 24 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Scheduler | 调度器 | 决定哪个任务获得处理器时间的组件 |
| Dispatcher | 派遣器 | 执行任务切换并将控制权交给选中任务的机制 |
| Scheduling Policy | 调度策略 | 选择执行实体的规则与目标 |
| Preemption | 抢占 | 操作系统主动中断当前任务以调度其他任务 |
| Non-preemptive Scheduling | 非抢占式调度 | 任务通常自行让出 CPU 才发生切换 |
| Time Slice / Quantum | 时间片 | 任务一次被分配的连续 CPU 时间额度 |
| Round Robin (RR) | 时间片轮转 | 就绪任务按轮转次序分享 CPU |
| First Come, First Served (FCFS) | 先来先服务 | 按进入就绪队列先后顺序执行 |
| Shortest Job First (SJF) | 最短作业优先 | 优先执行估计运行时间最短的作业 |
| Shortest Remaining Time First (SRTF) | 最短剩余时间优先 | 抢占式的最短作业优先策略 |
| Priority Scheduling | 优先级调度 | 根据优先级选择任务 |
| Multilevel Queue Scheduling | 多级队列调度 | 将任务分组到不同调度队列 |
| Multilevel Feedback Queue (MLFQ) | 多级反馈队列 | 根据行为动态调整任务所处队列 |
| Completely Fair Scheduler (CFS) | 完全公平调度器 | Linux 曾长期采用的公平调度框架 |
| Earliest Eligible Virtual Deadline First (EEVDF) | 最早合格虚拟截止时间优先 | Linux 公平调度采用的虚拟截止时间选择方法 |
| CPU Affinity | CPU 亲和性 | 限制或偏好任务运行的处理器集合 |
| Load Balancing | 负载均衡 | 在多个处理器之间重新分配任务负载 |
| Scheduling Latency | 调度延迟 | 任务变为可运行到实际获得 CPU 的等待时间 |
| Turnaround Time | 周转时间 | 从作业提交到完成所经历的时间 |
| Response Time | 响应时间 | 从请求发出到首次得到响应的时间 |
| Waiting Time | 等待时间 | 任务在就绪队列中等待的累计时间 |
| Throughput | 吞吐量 | 单位时间内完成的任务或工作数量 |
| Fairness | 公平性 | 调度资源分配在任务间的均衡程度 |
| Starvation | 饥饿 | 任务长期无法获得需要的执行机会或资源 |

## 05 并发、同步与内存一致性

*Concurrency & Synchronization · 28 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Concurrency | 并发 | 多个任务在重叠时间区间内推进 |
| Parallelism | 并行 | 多个任务在同一时刻于不同执行资源上运行 |
| Critical Section | 临界区 | 访问共享状态、需要协调保护的代码区域 |
| Race Condition | 竞态条件 | 结果依赖未恰当约束的事件先后顺序 |
| Data Race | 数据竞争 | 未同步的冲突内存访问，且至少一个为写入 |
| Mutual Exclusion | 互斥 | 同一时刻仅允许一个执行实体进入指定区域 |
| Mutex | 互斥锁 | 提供互斥访问的同步原语 |
| Spinlock | 自旋锁 | 通过循环检查锁状态等待的锁 |
| Semaphore | 信号量 | 使用计数与等待/唤醒操作管理资源的同步原语 |
| Binary Semaphore | 二元信号量 | 取值通常为 0 或 1 的信号量 |
| Counting Semaphore | 计数信号量 | 用计数表示多个可用资源的信号量 |
| Condition Variable | 条件变量 | 配合互斥锁等待某个共享条件变化 |
| Monitor | 管程 | 封装共享状态、互斥访问和条件等待的抽象 |
| Reader-Writer Lock (RWLock) | 读写锁 | 允许多读或单写的锁 |
| Barrier | 屏障 | 等待一组参与线程到达同步点的机制 |
| Atomic Operation | 原子操作 | 从并发观察角度不可分割的操作 |
| Compare-and-Swap (CAS) | 比较并交换 | 仅在值匹配预期时原子更新的操作 |
| Test-and-Set | 测试并设置 | 原子读取旧值并写入指定状态的操作 |
| Memory Ordering | 内存顺序 | 约束并发程序中内存操作可观察顺序的规则 |
| Memory Barrier / Fence | 内存屏障 | 限制某些内存操作重排的指令或机制 |
| Happens-Before | 先行发生关系 | 用于描述并发操作可见性与顺序的偏序关系 |
| Sequential Consistency | 顺序一致性 | 执行看起来遵循某个保序的全局交错顺序 |
| Acquire Semantics | 获取语义 | 阻止后续相关内存操作越过获取操作 |
| Release Semantics | 释放语义 | 阻止先前相关内存操作越过释放操作 |
| Lock-Free | 无锁 | 系统级保证某个线程能持续取得进展的并发算法性质 |
| Wait-Free | 无等待 | 每个操作可在有限步骤内完成的并发算法性质 |
| Read-Copy-Update (RCU) | 读-复制-更新 | 读侧开销低、通过延迟回收协调更新的机制 |
| Futex | 快速用户态互斥机制 | Linux 以用户态原子操作结合内核等待/唤醒的原语 |

## 06 死锁与资源分配

*Deadlocks & Resource Allocation · 15 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Deadlock | 死锁 | 一组任务互相等待资源而均无法继续推进 |
| Livelock | 活锁 | 任务持续活动但整体无法取得有效进展 |
| Deadlock Prevention | 死锁预防 | 通过破坏必要条件避免死锁产生 |
| Deadlock Avoidance | 死锁避免 | 仅允许进入可保持安全性的资源分配状态 |
| Deadlock Detection | 死锁检测 | 分析当前资源等待关系以识别死锁 |
| Deadlock Recovery | 死锁恢复 | 通过终止、回滚或抢占资源打破死锁 |
| Mutual Exclusion Condition | 互斥条件 | 资源不可同时被多个任务独占使用 |
| Hold and Wait | 占有并等待 | 任务持有资源时继续请求其他资源 |
| No Preemption Condition | 不可抢占条件 | 已分配资源无法被强制收回 |
| Circular Wait | 循环等待 | 任务之间形成闭环资源等待关系 |
| Resource Allocation Graph | 资源分配图 | 用图表示进程和资源间的请求/分配关系 |
| Wait-For Graph | 等待图 | 表示任务之间等待依赖的有向图 |
| Banker's Algorithm | 银行家算法 | 依据安全状态判定资源请求可否获批 |
| Priority Inversion | 优先级反转 | 高优先级任务被持锁的低优先级任务间接阻塞 |
| Priority Inheritance | 优先级继承 | 临时提升持锁者优先级以缓解优先级反转 |

## 07 内存管理基础

*Memory Management Fundamentals · 21 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Physical Memory | 物理内存 | 由实际内存硬件提供的存储空间 |
| Logical Address | 逻辑地址 | 程序运行中使用、需按系统规则解释的地址 |
| Virtual Address | 虚拟地址 | 进程虚拟地址空间中的地址 |
| Physical Address | 物理地址 | 定位实际物理内存或物理地址空间的地址 |
| Address Space | 地址空间 | 进程或系统可引用的地址集合 |
| Address Translation | 地址转换 | 将虚拟地址映射到物理地址的过程 |
| Memory Management Unit (MMU) | 内存管理单元 | 执行地址转换和访问权限检查的硬件 |
| Memory Allocation | 内存分配 | 为程序或内核提供可用内存区域 |
| Memory Deallocation | 内存释放 | 将不再使用的内存归还分配器或系统 |
| Heap | 堆 | 通常用于动态分配对象的内存区域 |
| Stack Frame | 栈帧 | 一次函数调用在栈中占用的记录区域 |
| Fragmentation | 碎片化 | 内存可用空间因分布或内部浪费而利用率下降 |
| Internal Fragmentation | 内部碎片 | 已分配块内未被使用的空间 |
| External Fragmentation | 外部碎片 | 空闲空间分散导致大块分配困难 |
| Contiguous Allocation | 连续分配 | 将对象放在连续地址范围中的分配方式 |
| Buddy Allocator | 伙伴分配器 | 按 2 的幂次划分和合并内存块的分配算法 |
| Slab Allocator | Slab 分配器 | 为特定内核对象缓存可复用内存块的机制 |
| NUMA | 非一致性内存访问 | 不同处理器访问不同内存节点的延迟不同 |
| Memory Locality | 内存局部性 | 程序访问集中在时间或空间邻近区域的性质 |
| Cache Line | 缓存行 | CPU 缓存与内存传输和一致性的基本数据单位 |
| False Sharing | 伪共享 | 不同线程修改同一缓存行的不同数据造成额外争用 |

## 08 分页、虚拟内存与地址转换

*Virtual Memory & Paging · 28 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Virtual Memory | 虚拟内存 | 通过地址映射与按需管理提供独立地址空间的机制 |
| Paging | 分页 | 把地址空间和物理内存划分为固定大小页的机制 |
| Page | 页 | 虚拟地址空间中固定大小的基本管理单元 |
| Page Frame | 页框 | 物理内存中存放一个页面的固定大小区域 |
| Page Table | 页表 | 保存虚拟页到物理页映射和权限的结构 |
| Page Table Entry (PTE) | 页表项 | 描述页面映射、权限、状态等信息的条目 |
| Multilevel Page Table | 多级页表 | 分层组织页表以减少稀疏空间开销的结构 |
| Translation Lookaside Buffer (TLB) | 地址转换后备缓冲器 | 缓存最近地址转换结果的硬件结构 |
| TLB Miss | TLB 未命中 | 所需地址映射未命中 TLB 的事件 |
| TLB Shootdown | TLB 失效广播 | 同步使其他 CPU 的相关 TLB 条目失效的操作 |
| Page Fault | 缺页异常 | 页面访问无法由当前有效映射完成而触发的异常 |
| Minor Page Fault | 次缺页 | 一般不必从磁盘读取页面即可解决的缺页 |
| Major Page Fault | 主缺页 | 通常需要存储 I/O 才能完成的缺页 |
| Demand Paging | 请求分页 | 页面在实际访问时才装入或映射的策略 |
| Page Replacement | 页面置换 | 内存紧张时选择页淘汰或回收的策略 |
| Least Recently Used (LRU) | 最近最少使用 | 优先淘汰最长时间未被访问页面的思想 |
| Clock Algorithm | 时钟置换算法 | 借助访问位近似 LRU 的页面替换算法 |
| Working Set | 工作集 | 进程在一段时间窗口内活跃使用的页面集合 |
| Thrashing | 抖动 | 系统因频繁换页而大幅降低有效工作效率 |
| Swap Space | 交换空间 | 用于存放换出内存页面的辅助存储空间 |
| Swap In / Swap Out | 换入 / 换出 | 在内存与交换空间之间迁移页面 |
| Copy-on-Write (CoW) | 写时复制 | 先共享数据，写入时才复制私有副本 |
| Memory-Mapped File (mmap) | 内存映射文件 | 将文件内容映射到进程虚拟地址空间的机制 |
| Shared Memory | 共享内存 | 多个进程或执行实体访问同一片内存的机制 |
| Huge Page | 大页 | 尺寸大于基础页的内存映射页面 |
| Transparent Huge Pages (THP) | 透明大页 | 系统自动尝试使用大页优化地址转换的机制 |
| Address Space Layout Randomization (ASLR) | 地址空间布局随机化 | 随机化关键内存区域位置以提高攻击难度 |
| Out-of-Memory (OOM) | 内存耗尽 | 系统无法满足内存分配或回收需求的状态 |

## 09 文件系统与命名空间

*Filesystems & Namespaces · 27 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| File | 文件 | 具有名称、元数据与内容的持久化数据对象 |
| Directory | 目录 | 组织文件和子目录命名关系的结构 |
| Filesystem (FS) | 文件系统 | 组织、存储、检索文件及元数据的机制 |
| Path | 路径 | 在命名空间中定位文件或目录的字符串 |
| Absolute Path | 绝对路径 | 从根位置开始描述资源位置的路径 |
| Relative Path | 相对路径 | 以当前工作目录等为基准的路径 |
| Root Directory | 根目录 | 文件系统路径层级的起始目录 |
| Mount | 挂载 | 将文件系统接入目录树中的操作 |
| Mount Point | 挂载点 | 文件系统接入现有目录树的位置 |
| Inode | 索引节点 | 类 Unix 文件系统中存储文件元数据的结构 |
| Directory Entry (Dentry) | 目录项 | 路径名与文件对象之间关联的目录记录或缓存对象 |
| Metadata | 元数据 | 描述文件属性、位置、权限等的数据 |
| File Descriptor (FD) | 文件描述符 | 进程用来引用已打开文件等对象的整数标识 |
| Open File Description | 打开文件描述 | 内核维护的文件打开状态及偏移量等共享信息 |
| File Offset | 文件偏移量 | 读写操作在文件中的当前位置 |
| Hard Link | 硬链接 | 多个目录项引用同一文件对象的链接关系 |
| Symbolic Link (Symlink) | 符号链接 | 内容指向另一条路径的特殊文件 |
| Virtual Filesystem (VFS) | 虚拟文件系统 | 统一不同文件系统访问操作的抽象层 |
| Superblock | 超级块 | 记录文件系统整体参数和状态的元数据结构 |
| Block Group | 块组 | 将文件系统的块与元数据分组管理的结构 |
| Extent | 区段 | 用起始位置与长度描述连续存储块的映射 |
| Journaling Filesystem | 日志文件系统 | 通过记录更新日志辅助崩溃恢复的文件系统 |
| Copy-on-Write Filesystem | 写时复制文件系统 | 通过写入新数据块再更新引用维护一致性 |
| Filesystem Check (fsck) | 文件系统检查 | 检测并在可能时修复文件系统结构问题的工具/过程 |
| Filesystem Snapshot | 文件系统快照 | 记录文件系统某一时间点状态的视图 |
| Page Cache | 页缓存 | 用于缓存文件数据等内存页面的机制 |
| Cache Coherence | 缓存一致性 | 多个副本所见数据保持约定一致的性质 |

## 10 输入输出与设备管理

*I/O & Device Management · 24 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Input/Output (I/O) | 输入/输出 | 处理器、内存与外设之间的数据交换操作 |
| Device Driver | 设备驱动程序 | 管理硬件设备并向系统提供接口的内核组件 |
| Device Controller | 设备控制器 | 执行设备操作并与主机通信的硬件组件 |
| Device File | 设备文件 | 通过文件接口暴露设备的特殊文件 |
| Character Device | 字符设备 | 按字节流等方式提供访问的设备类型 |
| Block Device | 块设备 | 按固定块或扇区地址访问的设备类型 |
| Programmed I/O (PIO) | 程序控制 I/O | 由 CPU 显式读写设备寄存器传输数据的方式 |
| Memory-Mapped I/O (MMIO) | 内存映射 I/O | 以地址空间中的寄存器映射访问设备 |
| Port-Mapped I/O | 端口映射 I/O | 通过独立 I/O 端口空间访问设备的方式 |
| Direct Memory Access (DMA) | 直接内存访问 | 设备无需 CPU 逐字节搬运即可与内存传输数据 |
| Interrupt-Driven I/O | 中断驱动 I/O | 通过设备中断通知 CPU 完成或处理事件 |
| Polling | 轮询 | 主动反复检查设备或事件状态的方式 |
| Busy Waiting | 忙等待 | 持续消耗执行资源以等待条件变化的方式 |
| Blocking I/O | 阻塞式 I/O | 操作完成前调用线程通常等待的 I/O 模式 |
| Nonblocking I/O | 非阻塞式 I/O | 当前无法立即完成时及时返回的 I/O 模式 |
| Asynchronous I/O (AIO) | 异步 I/O | 请求提交与完成通知相分离的 I/O 模式 |
| Synchronous I/O | 同步 I/O | 操作调用与完成按同步语义衔接的 I/O 方式 |
| I/O Multiplexing | I/O 多路复用 | 单个执行流监视多个 I/O 事件源 |
| select / poll | select / poll 机制 | 用于监视多个文件描述符就绪状态的接口 |
| epoll | epoll 事件通知机制 | Linux 上可扩展的 I/O 事件通知接口 |
| io_uring | io_uring 异步 I/O 接口 | Linux 使用共享环形队列提交与完成 I/O 的接口 |
| Buffering | 缓冲 | 暂存数据以协调处理速率与传输粒度的机制 |
| Spooling | 假脱机 | 通过队列或磁盘暂存设备任务以便异步处理 |
| Zero-Copy | 零拷贝 | 减少数据在内核与用户空间等层间复制的技术统称 |

## 11 磁盘、存储与持久性

*Storage & Durability · 20 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Persistent Storage | 持久性存储 | 断电后仍可保存数据的存储介质或层级 |
| Hard Disk Drive (HDD) | 机械硬盘 | 通过磁性盘片记录和读取数据的存储设备 |
| Solid-State Drive (SSD) | 固态硬盘 | 以闪存等非机械介质为主的存储设备 |
| Sector | 扇区 | 存储介质上寻址或组织数据的基本单元之一 |
| Logical Block Addressing (LBA) | 逻辑块寻址 | 使用线性逻辑块编号访问存储设备的方法 |
| Storage Stack | 存储栈 | 应用到文件系统、块层和设备的 I/O 处理层次 |
| I/O Scheduler | I/O 调度器 | 决定块设备 I/O 请求分配和排序的组件 |
| Seek Time | 寻道时间 | 机械磁头移动到目标磁道所需时间 |
| Rotational Latency | 旋转延迟 | 盘片旋转至目标扇区位置的等待时间 |
| Write Amplification | 写放大 | 实际物理写入量高于逻辑写入量的现象 |
| Flash Translation Layer (FTL) | 闪存转换层 | SSD 中逻辑地址到闪存物理位置的映射层 |
| Wear Leveling | 磨损均衡 | 将闪存擦写负担分散到不同存储单元的技术 |
| TRIM | TRIM 指令 | 通知 SSD 某些逻辑块数据已不再需要的指令 |
| Redundant Array of Independent Disks (RAID) | 独立磁盘冗余阵列 | 组合多个磁盘实现性能或冗余目标的技术 |
| Write-Ahead Logging (WAL) | 预写式日志 | 正式修改目标数据前先记录可恢复的变更信息 |
| Writeback Cache | 回写缓存 | 先在缓存更新、之后再写入后端存储的策略 |
| Write-through Cache | 直写缓存 | 写入缓存时同步更新后端存储的策略 |
| Crash Consistency | 崩溃一致性 | 意外断电/崩溃后仍满足约定存储不变量的性质 |
| Durability | 持久性 | 已确认的数据在故障后仍能保留的性质 |
| fsync | 文件同步调用 | 请求将文件相关待写数据及必要元数据同步到存储 |

## 12 隔离、保护与系统安全

*Protection & Security · 22 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Protection | 保护机制 | 控制进程对系统资源合法访问的机制 |
| Security Boundary | 安全边界 | 划分不同信任等级或权限域的界限 |
| Authentication | 身份认证 | 确认请求方身份的过程 |
| Authorization | 访问授权 | 判定已识别主体是否可执行指定操作 |
| Access Control | 访问控制 | 限制主体对对象可用操作的策略与机制 |
| Access Control List (ACL) | 访问控制列表 | 按主体或规则记录资源访问权限的结构 |
| Discretionary Access Control (DAC) | 自主访问控制 | 对象拥有者等可决定访问权限的模型 |
| Mandatory Access Control (MAC) | 强制访问控制 | 由系统统一执行安全策略的模型 |
| Role-Based Access Control (RBAC) | 基于角色的访问控制 | 通过角色汇聚并分配访问权限的模型 |
| Principle of Least Privilege | 最小权限原则 | 仅授予完成任务所需最少权限 |
| Privilege Escalation | 权限提升 | 获得超出原有授权的更高权限 |
| Kernel Attack Surface | 内核攻击面 | 可被外部输入或调用触达的内核功能范围 |
| Sandbox | 沙箱 | 限制程序可访问资源和行为的隔离执行环境 |
| System Call Filtering | 系统调用过滤 | 允许或拒绝特定系统调用的控制机制 |
| seccomp | 安全计算模式 | Linux 限制进程可使用的系统调用的机制 |
| Capabilities | 能力机制 | 将传统超级用户权限拆分为可独立授予的权限单元 |
| SELinux | 安全增强型 Linux | Linux 的强制访问控制安全框架 |
| AppArmor | AppArmor 安全框架 | Linux 使用配置文件约束程序访问的安全模块 |
| Stack Canary | 栈保护值 | 用于辅助检测部分栈溢出破坏的防护机制 |
| Data Execution Prevention (DEP/NX) | 数据执行保护 / 不可执行位 | 限制数据页面执行指令的硬件/系统机制 |
| Kernel Address Space Layout Randomization (KASLR) | 内核地址空间布局随机化 | 随机化内核映射位置以增加利用难度 |
| Trusted Computing Base (TCB) | 可信计算基 | 必须可信、负责实施系统安全策略的组件集合 |

## 13 进程间通信与网络接口

*IPC & Networking · 20 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Inter-Process Communication (IPC) | 进程间通信 | 不同进程交换数据并协调行为的机制 |
| Pipe | 管道 | 用于进程间单向字节流通信的机制 |
| Named Pipe (FIFO) | 命名管道 | 以文件系统名字访问的管道对象 |
| Message Queue | 消息队列 | 按消息边界或队列语义传递数据的 IPC 机制 |
| Shared Memory Segment | 共享内存段 | 供多个进程映射的共享数据区域 |
| Signal | 信号 | 用于异步通知进程事件的软件机制 |
| Signal Handler | 信号处理函数 | 进程收到指定信号时执行的用户态处理逻辑 |
| Unix Domain Socket | Unix 域套接字 | 同一主机进程间使用套接字接口的通信方式 |
| Socket | 套接字 | 应用使用网络或本机通信协议的端点抽象 |
| Socket API | 套接字 API | 创建、绑定、连接、收发数据等接口的集合 |
| TCP | 传输控制协议 | 提供面向连接、可靠字节流的传输协议 |
| UDP | 用户数据报协议 | 提供无连接数据报传输的协议 |
| Port Number | 端口号 | 在传输协议中区分通信端点的标识之一 |
| Network Stack | 网络协议栈 | 实现协议分层、封装、路由和传输的系统组件 |
| Network Interface | 网络接口 | 系统中发送、接收网络数据的逻辑或物理端点 |
| Packet | 数据包 | 网络分层传输中携带首部和负载的数据单元统称 |
| Zero-Copy Networking | 零拷贝网络传输 | 尽量减少网络数据路径内存复制的技术 |
| Remote Procedure Call (RPC) | 远程过程调用 | 以类似函数调用的方式请求远端服务 |
| Loopback Interface | 回环接口 | 将网络流量送回本机协议栈的虚拟接口 |
| Network Namespace | 网络命名空间 | 隔离网络设备、路由等网络资源视图的机制 |

## 14 虚拟化、容器与云原生

*Virtualization & Containers · 22 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Virtualization | 虚拟化 | 将底层资源抽象为隔离的虚拟运行环境 |
| Virtual Machine (VM) | 虚拟机 | 具有虚拟硬件与独立客户机系统的运行环境 |
| Hypervisor / VMM | 虚拟机监控器 | 创建、运行和管理虚拟机的控制层 |
| Type 1 Hypervisor | 第一类虚拟机监控器 | 直接运行在硬件上的虚拟化管理层 |
| Type 2 Hypervisor | 第二类虚拟机监控器 | 运行在宿主操作系统之上的虚拟化软件 |
| Host OS | 宿主操作系统 | 承载虚拟机管理软件或容器环境的操作系统 |
| Guest OS | 客户机操作系统 | 在虚拟机内部运行的操作系统 |
| Hardware-Assisted Virtualization | 硬件辅助虚拟化 | 利用处理器虚拟化扩展执行虚拟机的技术 |
| Paravirtualization | 半虚拟化 | 客户机与虚拟化层协作以降低模拟开销的技术 |
| Full Virtualization | 完全虚拟化 | 提供可运行未针对虚拟化修改的客户机的环境 |
| Virtual CPU (vCPU) | 虚拟 CPU | 分配给虚拟机的逻辑处理器执行资源 |
| Nested Virtualization | 嵌套虚拟化 | 在虚拟机内部继续运行虚拟机监控器的能力 |
| Container | 容器 | 共享宿主内核、通过隔离机制运行的进程集合 |
| Operating-System-Level Virtualization | 操作系统级虚拟化 | 复用同一内核创建隔离用户空间的方式 |
| Namespace | 命名空间 | 为进程提供部分系统资源的独立视图 |
| Control Groups (cgroups) | 控制组 | Linux 对进程组资源用量进行限制、统计与管理的机制 |
| Mount Namespace | 挂载命名空间 | 隔离进程所见挂载点集合的机制 |
| PID Namespace | 进程标识符命名空间 | 隔离进程编号空间和进程树视图的机制 |
| User Namespace | 用户命名空间 | 隔离用户与组 ID 映射及相关权限的机制 |
| Overlay Filesystem | 叠加文件系统 | 将多个目录层合成统一可写文件系统视图的技术 |
| Container Image | 容器镜像 | 打包文件系统内容与运行元数据的模板 |
| Container Runtime | 容器运行时 | 负责创建和管理容器生命周期的软件 |

## 15 Unix / Linux 关键概念

*Unix & Linux Essentials · 23 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Unix | Unix 操作系统家族 | 具有多用户、多任务和统一文件接口传统的系统家族 |
| POSIX | 可移植操作系统接口 | 定义类 Unix 操作系统接口和行为的标准族 |
| Shell | 命令解释器 | 解析并执行用户输入的命令或脚本的程序 |
| Terminal | 终端 | 提供交互式文本输入输出的设备或软件界面 |
| Pseudo-Terminal (PTY) | 伪终端 | 在软件中模拟终端设备的通信机制 |
| Daemon | 守护进程 | 通常在后台运行并提供系统服务的进程 |
| init Process | 初始化进程 | 负责启动并管理部分用户态系统服务的首个进程 |
| systemd | systemd 系统与服务管理器 | Linux 上常用的初始化和服务管理系统 |
| fork() | fork 进程复制调用 | 创建新进程，子进程初始状态基于父进程 |
| execve() | execve 程序执行调用 | 将当前进程的程序映像替换为指定可执行文件 |
| wait() / waitpid() | 进程等待调用 | 等待子进程状态变化并回收退出信息 |
| getpid() | 获取进程号调用 | 返回调用进程的进程标识符 |
| kill() | 发送信号调用 | 向进程或进程组发送信号，并非必然终止进程 |
| nice Value | nice 值 | 影响 Linux 普通任务调度权重的用户可调参数 |
| /proc | proc 伪文件系统 | 暴露进程与内核状态信息的虚拟文件系统 |
| /sys | sysfs 伪文件系统 | 暴露设备模型及部分内核属性的虚拟文件系统 |
| /dev | 设备目录 | 通常放置设备节点和设备相关接口文件的目录 |
| /proc/self | 当前进程信息入口 | 指向访问者自身进程 proc 信息的特殊路径 |
| chroot | 改变根目录 | 改变进程解析绝对路径所用根目录的操作 |
| umask | 权限掩码 | 影响新建文件和目录默认权限的掩码 |
| File Permission Bits | 文件权限位 | 类 Unix 中文件读、写、执行访问控制位 |
| Standard Input / Output / Error | 标准输入 / 输出 / 错误 | 进程通常使用的三个标准数据流 |
| Exit Status | 退出状态码 | 进程终止时向父进程提供的结果值 |

## 16 实时系统与嵌入式系统

*Real-Time & Embedded Systems · 16 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Real-Time Operating System (RTOS) | 实时操作系统 | 以可预测时限响应为核心目标的操作系统 |
| Hard Real-Time | 硬实时 | 错过截止时间被视为系统正确性失败的实时约束 |
| Soft Real-Time | 软实时 | 偶发超时降低服务质量但不必然使系统失效 |
| Deadline | 截止时间 | 任务必须完成的时间约束点 |
| Worst-Case Execution Time (WCET) | 最坏情况执行时间 | 任务在约定条件下的执行时间上界 |
| Worst-Case Response Time (WCRT) | 最坏情况响应时间 | 任务从释放到完成的最坏响应时间 |
| Determinism | 确定性 | 相同条件下表现出可预测时间和行为的性质 |
| Jitter | 抖动 / 时间抖动 | 事件发生时间与理想时间之间的波动 |
| Rate Monotonic Scheduling (RMS) | 速率单调调度 | 周期越短静态优先级越高的实时调度算法 |
| Earliest Deadline First (EDF) | 最早截止时间优先 | 动态优先执行绝对截止时间最近任务的算法 |
| Priority Ceiling Protocol | 优先级上限协议 | 控制共享资源访问以限制阻塞与反转的机制 |
| Interrupt Latency | 中断延迟 | 中断发出到处理程序开始执行的延迟 |
| Preemption Latency | 抢占延迟 | 可抢占条件满足到实际切换任务的时间 |
| Tickless Kernel | 无周期时钟滴答内核 | 避免不必要周期性时钟中断的内核模式 |
| Watchdog Timer | 看门狗定时器 | 在系统未按预期更新时触发恢复动作的计时机制 |
| Embedded System | 嵌入式系统 | 为特定设备或功能设计的计算机系统 |

## 17 性能分析与可观测性

*Performance & Observability · 22 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| CPU Utilization | CPU 利用率 | 处理器处于忙碌状态的时间占比 |
| Load Average | 平均负载 | Linux 一定时间窗口内可运行及不可中断任务数量的平滑指标 |
| Latency | 延迟 | 从请求发出到特定完成事件之间的时间 |
| Bandwidth | 带宽 | 单位时间内可传输的数据量上限或能力 |
| IOPS | 每秒输入输出操作数 | 衡量存储设备随机或混合 I/O 处理能力的指标 |
| Context Switch Rate | 上下文切换频率 | 单位时间发生的上下文切换次数 |
| Cache Hit Ratio | 缓存命中率 | 可由缓存直接满足的访问所占比例 |
| Page Fault Rate | 缺页率 | 单位时间或单位访问中缺页异常的发生数量或比例 |
| System Call Overhead | 系统调用开销 | 陷入内核、执行服务并返回所需的附加成本 |
| Profiling | 性能剖析 | 采集程序或系统资源消耗分布的方法 |
| Sampling Profiler | 采样式分析器 | 定期采样执行状态以估计热点的工具 |
| Tracing | 事件追踪 | 按时间线记录系统运行事件的分析技术 |
| Flame Graph | 火焰图 | 聚合调用栈采样并展示热点路径的可视化方式 |
| perf | perf 性能分析工具 | Linux 性能计数、采样和事件分析工具集 |
| Extended Berkeley Packet Filter (eBPF) | 扩展伯克利包过滤器 | 在内核受验证执行环境运行受控程序的技术 |
| kprobe / uprobe | 内核 / 用户探针 | 动态挂载到内核或用户程序指定位置的探针 |
| ftrace | ftrace 跟踪框架 | Linux 内核函数与事件跟踪基础设施 |
| strace | 系统调用跟踪工具 | 观察进程系统调用及信号活动的工具 |
| Bottleneck | 性能瓶颈 | 限制整体吞吐量或延迟的关键资源或环节 |
| Contention | 资源争用 | 多个执行实体竞争同一资源的状态 |
| Tail Latency | 长尾延迟 | 延迟分布中靠后分位数所反映的慢请求表现 |
| Performance Counter | 性能计数器 | 硬件或软件统计特定运行事件的计数机制 |

## 18 分布式操作系统与高级机制

*Distributed & Advanced OS Topics · 16 terms*

| English | 中文 | 简明释义 |
|---|---|---|
| Distributed Operating System | 分布式操作系统 | 跨多台计算机协调资源并提供系统抽象的操作系统设计 |
| Distributed Shared Memory (DSM) | 分布式共享内存 | 为分布节点提供共享地址空间抽象的机制 |
| Remote Direct Memory Access (RDMA) | 远程直接内存访问 | 网络适配器支持的远端内存直接数据传输能力 |
| Microservices | 微服务 | 将系统拆分为可独立部署服务的架构方式 |
| Checkpointing | 检查点 | 保存执行状态以便后续恢复或迁移的机制 |
| Process Migration | 进程迁移 | 将运行中的进程状态转移到其他执行环境的技术 |
| Live Migration | 热迁移 | 在业务持续运行期间转移虚拟机或工作负载的技术 |
| Fault Tolerance | 容错性 | 发生故障时仍能维持约定服务的能力 |
| High Availability (HA) | 高可用性 | 通过冗余、故障转移等减少服务中断的设计目标 |
| Split-Brain | 脑裂 | 分布系统中出现多个互不协调的主控视图的状态 |
| Consistency Model | 一致性模型 | 规定并发或分布式操作可观察顺序的规则 |
| Linearizability | 线性一致性 | 每个操作看起来在调用与响应间某一瞬间生效的性质 |
| Eventual Consistency | 最终一致性 | 停止更新后各副本最终收敛到一致状态的模型 |
| Distributed Lock | 分布式锁 | 跨多个节点协调互斥访问的机制 |
| Kernel Bypass | 内核旁路 | 让部分数据路径绕开传统内核协议处理的技术 |
| Unikernel | 专用单地址空间内核镜像 | 把应用与所需系统组件编译为专用镜像的部署模型 |

## 附录：易混淆概念速辨

| 概念对 | 区别 |
|---|---|
| Program vs Process | 程序是静态代码与数据；进程是正在执行、拥有运行时状态和资源的实例。 |
| Process vs Thread | 进程通常提供资源和地址空间边界；线程是进程内的执行流。 |
| Concurrency vs Parallelism | 并发强调时间范围内交错推进；并行强调同一时刻真正同时执行。 |
| Trap vs Interrupt | 陷入通常指同步进入特权处理路径；中断通常指异步外部事件。 |
| Exception vs Page Fault | 异常是处理器事件的大类；缺页异常是与页面映射相关的具体异常。 |
| Race Condition vs Data Race | 竞态条件是更宽泛的顺序依赖问题；数据竞争特指无适当同步的冲突内存访问。 |
| Deadlock vs Livelock | 死锁是互相等待而不动；活锁是仍在活动但没有实质进展。 |
| Mutex vs Semaphore | 互斥锁侧重排他访问和持有者语义；信号量侧重计数与资源协调。 |
| Virtual Memory vs Swap | 虚拟内存是地址空间与映射机制；交换空间只是页面管理可能使用的存储。 |
| Page vs Page Frame | 页是虚拟地址空间的单元；页框是物理内存中对应大小的区域。 |
| Hard Link vs Symbolic Link | 硬链接引用同一文件对象；符号链接保存另一条路径。 |
| Blocking vs Nonblocking I/O | 阻塞调用可能等待条件满足；非阻塞调用在暂不能完成时及时返回。 |
| Buffer vs Cache | 缓冲主要协调数据流和速率；缓存主要复用已有结果以减少重复访问。 |
| Kernel vs Hypervisor | 内核管理操作系统进程和资源；虚拟机监控器管理虚拟硬件与客户机。 |
| Container vs Virtual Machine | 容器通常共享宿主内核；虚拟机通常有独立客户机内核。 |
| Authentication vs Authorization | 认证确认是谁；授权确认能做什么。 |

## 参考阅读

- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- [The Linux man-pages project](https://www.kernel.org/doc/man-pages/)
- [Linux kernel documentation](https://docs.kernel.org/)
- [The Open Group Base Specifications](https://pubs.opengroup.org/onlinepubs/9799919799/)

> 说明：本对照表为学习与检索用途，非官方标准术语的逐条摘录；中文译法可能因语境而异。
