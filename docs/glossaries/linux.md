# Linux 专有名词中英文对照表

> v1.0 · 2026-11-16 · 394 条术语 · 16 个主题模块

> 说明：按技术领域编排，提供英文术语、中文常用译名与简要释义；具体含义以 Linux 内核版本及官方文档为准。

## 目录

- [01 Linux 基础与体系结构](#s01)（26 条）
- [02 Shell 与命令行](#s02)（22 条）
- [03 目录、文件与文件系统](#s03)（30 条）
- [04 进程、线程与信号](#s04)（24 条）
- [05 CPU 调度、并发与同步](#s05)（25 条）
- [06 内存管理](#s06)（28 条）
- [07 I/O、设备和内核接口](#s07)（25 条）
- [08 Linux 网络](#s08)（30 条）
- [09 用户、权限与安全](#s09)（25 条）
- [10 启动、服务与系统管理](#s10)（25 条）
- [11 容器与虚拟化](#s11)（25 条）
- [12 系统性能与可观测性](#s12)（28 条）
- [13 eBPF 与内核开发](#s13)（22 条）
- [14 存储、磁盘与可靠性](#s14)（24 条）
- [15 构建、工具链与调试](#s15)（20 条）
- [16 故障排查与常见状态](#s16)（15 条）

<a id="s01"></a>
## 01 Linux 基础与体系结构

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Linux kernel | Linux 内核 | 操作系统核心，管理硬件与系统资源 |
| GNU/Linux | GNU/Linux 系统 | 使用 Linux 内核及 GNU 等用户空间组件的系统 |
| Distribution (distro) | 发行版 | 内核与工具、软件包集成的操作系统 |
| User space | 用户空间 | 普通应用程序主要运行的空间 |
| Kernel space | 内核空间 | 内核代码和特权资源运行的空间 |
| Kernel mode | 内核态 | CPU 运行具有特权的内核代码时的状态 |
| User mode | 用户态 | CPU 运行非特权应用代码时的状态 |
| System call (syscall) | 系统调用 | 用户程序请求内核服务的接口 |
| System call interface | 系统调用接口 | 系统调用编号及调用约定等集合 |
| Application Binary Interface (ABI) | 应用二进制接口 | 程序与系统在二进制层面的约定 |
| Application Programming Interface (API) | 应用程序编程接口 | 提供给程序调用的函数或服务接口 |
| GNU C Library (glibc) | GNU C 标准库 | 常用 C 库及系统调用封装实现 |
| POSIX | 可移植操作系统接口 | 规定兼容性接口与行为的标准族 |
| Linux Standard Base (LSB) | Linux 标准规范基础 | 历史性的发行版兼容规范体系 |
| Monolithic kernel | 宏内核 | 核心服务主要在内核地址空间执行 |
| Kernel module | 内核模块 | 可按需加载到内核的代码单元 |
| Loadable Kernel Module (LKM) | 可加载内核模块 | 不重启即可装入的模块形式 |
| Kernel configuration (Kconfig) | 内核配置系统 | 声明配置选项及其依赖的机制 |
| Kernel image | 内核镜像 | 用于引导装载的内核二进制文件 |
| Initramfs | 初始内存文件系统 | 引导早期加载的临时根文件系统 |
| Firmware | 固件 | 设备或平台上的低层控制程序 |
| UEFI | 统一可扩展固件接口 | 现代计算机固件启动接口标准 |
| Bootloader | 引导加载程序 | 加载内核并传递启动参数的软件 |
| GRUB | GNU GRUB 引导器 | 常用的多系统引导加载程序 |
| Device tree | 设备树 | 描述嵌入式硬件拓扑的数据结构 |
| Kernel command line | 内核启动参数 | 引导时传递给内核的参数字符串 |

<a id="s02"></a>
## 02 Shell 与命令行

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Shell | 命令解释器 | 交互执行命令及脚本的程序 |
| Bash | Bourne Again Shell | 广泛使用的命令解释器 |
| Zsh | Z Shell | 支持丰富补全与扩展的 Shell |
| Command-line interface (CLI) | 命令行界面 | 通过文本命令交互的界面 |
| Terminal emulator | 终端模拟器 | 图形环境下模拟文本终端的软件 |
| TTY | 电传打字机终端 | 历史名称，现泛指字符终端接口 |
| Pseudo-terminal (PTY) | 伪终端 | 终端主从设备对，支持远程会话 |
| Standard input (stdin) | 标准输入 | 进程的默认输入流，文件描述符 0 |
| Standard output (stdout) | 标准输出 | 进程的默认输出流，文件描述符 1 |
| Standard error (stderr) | 标准错误 | 进程的错误输出流，文件描述符 2 |
| Pipe | 管道 | 将一个进程输出连接到另一个进程输入 |
| Redirection | 重定向 | 改变输入输出的来源或目的地 |
| Here-document | 此处文档 | 在脚本中内嵌多行输入数据 |
| Here-string | 此处字符串 | 把字符串作为命令标准输入 |
| Environment variable | 环境变量 | 传给子进程的键值配置 |
| PATH | 可执行文件搜索路径 | Shell 查找命令的目录列表 |
| Exit status | 退出状态码 | 进程结束时返回的状态值 |
| Wildcard globbing | 通配符展开 | 按文件名模式展开匹配项 |
| Command substitution | 命令替换 | 将子命令输出插入表达式 |
| Process substitution | 进程替换 | 把子命令流表示成路径供命令使用 |
| Job control | 作业控制 | 管理前台和后台作业的机制 |
| Shebang | 解释器声明行 | 脚本首行的 #! 解释器指令 |

<a id="s03"></a>
## 03 目录、文件与文件系统

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Filesystem | 文件系统 | 组织和访问文件及元数据的机制 |
| Filesystem Hierarchy Standard (FHS) | 文件系统层次结构标准 | 约定常用系统目录的用途 |
| Root directory (/) | 根目录 | Unix 目录树的顶层 |
| Home directory | 家目录 | 用户个人文件的默认目录 |
| Working directory | 工作目录 | 进程当前相对路径基准 |
| Absolute path | 绝对路径 | 从根目录开始的完整路径 |
| Relative path | 相对路径 | 相对于某目录的路径 |
| Inode | 索引节点 | 保存文件元数据与数据块引用的对象 |
| Directory entry (dentry) | 目录项 | 将文件名与文件系统对象关联 |
| File descriptor (FD) | 文件描述符 | 进程使用的已打开文件整数句柄 |
| Open file description | 打开文件描述项 | 内核保存的文件偏移及状态对象 |
| Hard link | 硬链接 | 指向同一 inode 的另一目录项 |
| Symbolic link (symlink) | 符号链接 | 记录目标路径的特殊文件 |
| Mount | 挂载 | 将文件系统接入目录树 |
| Mount point | 挂载点 | 被用于挂载的目录位置 |
| Bind mount | 绑定挂载 | 把已有目录或文件映射到另一位置 |
| Read-only filesystem | 只读文件系统 | 不允许修改写入的挂载状态 |
| Virtual Filesystem (VFS) | 虚拟文件系统层 | 为不同文件系统提供统一接口 |
| Extended filesystem (ext4) | 第四代扩展文件系统 | Linux 常用通用文件系统 |
| XFS | XFS 文件系统 | 适合大容量和并行 I/O 的日志文件系统 |
| Btrfs | B 树文件系统 | 支持写时复制和快照等特性的文件系统 |
| OverlayFS | 叠加文件系统 | 组合上下层目录呈现统一视图 |
| procfs (/proc) | 进程信息伪文件系统 | 暴露进程及内核运行信息 |
| sysfs (/sys) | 系统设备伪文件系统 | 以文件形式暴露内核设备模型 |
| /dev | 设备目录 | 设备节点的常见存放目录 |
| /etc | 系统配置目录 | 主机相关配置文件的常见位置 |
| /var/log | 日志目录 | 许多程序保存日志文件的位置 |
| /run | 运行时数据目录 | 启动后动态状态数据的常见位置 |
| /tmp | 临时文件目录 | 存放临时文件，清理策略依系统而定 |
| /usr | 用户空间软件层次 | 系统工具、库和共享数据的常见位置 |

<a id="s04"></a>
## 04 进程、线程与信号

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Process | 进程 | 拥有资源与执行上下文的程序实例 |
| Thread | 线程 | 进程中的可调度执行流 |
| Task | 任务 | 内核调度与管理的执行实体 |
| Process ID (PID) | 进程标识符 | 标识某 PID 命名空间内进程的编号 |
| Parent Process ID (PPID) | 父进程标识符 | 父进程在相应命名空间的编号 |
| Thread ID (TID) | 线程标识符 | 标识单个任务的编号 |
| Process group | 进程组 | 便于终端作业和信号管理的进程集合 |
| Session | 会话 | 关联进程组与控制终端的集合 |
| Daemon | 守护进程 | 长期提供后台服务的进程 |
| Zombie process | 僵尸进程 | 已退出但尚未被父进程回收的进程 |
| Orphan process | 孤儿进程 | 父进程退出而被重新指定父进程的子进程 |
| Fork (fork()) | 创建子进程 | 复制调用进程以形成子进程 |
| Exec (execve()) | 执行新程序 | 用新程序映像替换当前进程内容 |
| Wait (waitpid()) | 等待子进程 | 取得子进程状态并回收退出信息 |
| Context switch | 上下文切换 | CPU 在执行上下文之间切换 |
| Signal | 信号 | 对进程异步事件的通知机制 |
| SIGTERM | 终止请求信号 | 通常用于请求进程正常退出 |
| SIGKILL | 强制终止信号 | 不可捕获或忽略的终止信号 |
| SIGINT | 中断信号 | 通常由终端 Ctrl+C 触发 |
| SIGCHLD | 子进程状态信号 | 通知父进程子进程状态变化 |
| Signal handler | 信号处理函数 | 程序注册的特定信号处理逻辑 |
| Core dump | 核心转储 | 保存进程异常退出时的内存状态 |
| Process state | 进程状态 | 运行、睡眠、停止等内核记录状态 |
| Nice value | nice 值 | 影响普通调度类任务权重的值 |

<a id="s05"></a>
## 05 CPU 调度、并发与同步

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Scheduler | 调度器 | 决定何时由哪个任务运行的内核组件 |
| Preemption | 抢占 | 高优先级任务或内核机制打断当前执行 |
| Time slice | 时间片 | 任务在一次调度中的时间配额概念 |
| Completely Fair Scheduler (CFS) | 完全公平调度器 | 历史上用于普通任务公平调度的机制 |
| Earliest Eligible Virtual Deadline First (EEVDF) | 最早合格虚拟截止期优先 | 面向公平与交互延迟的调度方法 |
| Virtual runtime (vruntime) | 虚拟运行时间 | 按任务权重归一化的运行时间 |
| Run queue | 运行队列 | 等待被 CPU 调度的可运行任务集合 |
| Scheduling policy | 调度策略 | 规定任务优先级和调度行为 |
| SCHED_FIFO | 先进先出实时调度策略 | 非时间片轮转的实时调度策略 |
| SCHED_RR | 轮转实时调度策略 | 为同优先级任务提供时间片轮转 |
| CPU affinity | CPU 亲和性 | 限制或偏好任务可运行的 CPU 集合 |
| Load balancing | 负载均衡 | 在 CPU 之间分配可运行任务 |
| Race condition | 竞态条件 | 执行时序影响正确性的情形 |
| Critical section | 临界区 | 访问共享状态需互斥的代码区域 |
| Mutual exclusion (mutex) | 互斥锁 | 保证同一时刻互斥访问的同步原语 |
| Spinlock | 自旋锁 | 等待期间循环检查锁状态的锁 |
| Semaphore | 信号量 | 通过计数管理并发访问或事件的原语 |
| Condition variable | 条件变量 | 供线程等待条件并被唤醒的原语 |
| Atomic operation | 原子操作 | 对并发观察表现为不可分割的操作 |
| Memory barrier | 内存屏障 | 约束某些内存访问重排的同步机制 |
| Read-Copy-Update (RCU) | 读取-复制-更新 | 优化读多写少共享数据访问的机制 |
| Grace period | 宽限期 | RCU 等机制等待既有读侧访问完成的阶段 |
| Deadlock | 死锁 | 参与者循环等待而无法继续执行 |
| Livelock | 活锁 | 任务持续活动但未取得有效进展 |
| Priority inversion | 优先级反转 | 高优先级任务被低优先级任务间接阻塞 |

<a id="s06"></a>
## 06 内存管理

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Virtual memory | 虚拟内存 | 通过地址映射隔离并管理进程内存 |
| Virtual address | 虚拟地址 | 程序使用、需经页表转换的地址 |
| Physical address | 物理地址 | 内存硬件视角的地址 |
| Address space | 地址空间 | 进程可使用的虚拟地址范围 |
| Memory Management Unit (MMU) | 内存管理单元 | 执行虚实地址转换与权限检查 |
| Page table | 页表 | 保存虚拟页到物理页映射的结构 |
| Page | 内存页 | 虚拟内存管理的基本粒度 |
| Page frame | 物理页帧 | 物理内存中的页大小块 |
| Page fault | 缺页异常 | 访问未映射或不满足权限的页时的异常 |
| Minor page fault | 次缺页 | 通常无需从磁盘读取数据的缺页 |
| Major page fault | 主缺页 | 通常需要存储 I/O 的缺页 |
| Translation Lookaside Buffer (TLB) | 快表 | 缓存虚拟地址翻译结果的硬件结构 |
| Huge pages | 大页 | 采用比基础页更大的内存页 |
| Transparent Huge Pages (THP) | 透明大页 | 内核自动使用大页的机制 |
| Resident Set Size (RSS) | 常驻内存集大小 | 进程当前驻留物理内存的度量 |
| Virtual Memory Size (VMS) | 虚拟内存大小 | 进程虚拟地址空间占用的度量 |
| Shared memory | 共享内存 | 多个进程可映射的同一内存区域 |
| Memory mapping (mmap) | 内存映射 | 将文件或匿名对象映射进地址空间 |
| Anonymous memory | 匿名内存 | 不直接由普通文件支持的内存 |
| Copy-on-write (COW) | 写时复制 | 首次写入前共享同一数据页的策略 |
| Swap | 交换空间 | 用于存放从内存换出的页面内容的空间 |
| Out of Memory (OOM) | 内存不足 | 系统或限制范围内无法满足内存需求 |
| OOM killer | 内存不足终止器 | 必要时选择终止进程以回收资源 |
| Slab allocator | Slab 分配器 | 基于对象缓存的内核内存分配机制 |
| Buddy allocator | 伙伴分配器 | 按 2 的幂次块管理物理页的分配器 |
| NUMA | 非一致性内存访问 | 访问本地与远程内存代价不同的架构 |
| Memory pressure | 内存压力 | 可用内存紧张导致回收和延迟的程度 |
| Page cache | 页缓存 | 缓存文件数据的内存页集合 |

<a id="s07"></a>
## 07 I/O、设备和内核接口

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Input/output (I/O) | 输入输出 | 与外部设备或数据流交换信息的操作 |
| Blocking I/O | 阻塞式 I/O | 操作未满足条件时调用者可能等待 |
| Nonblocking I/O | 非阻塞式 I/O | 无法立即完成时通常及时返回 |
| Synchronous I/O | 同步 I/O | 调用与完成语义关联的 I/O 方式 |
| Asynchronous I/O | 异步 I/O | 发起与结果完成可分离的 I/O 方式 |
| Direct I/O (O_DIRECT) | 直接 I/O | 尝试绕过常规页缓存的 I/O 模式 |
| Buffered I/O | 缓冲 I/O | 通常通过内核页缓存执行的文件 I/O |
| io_uring | io_uring 异步 I/O 接口 | 通过共享环队列提交与获取完成事件 |
| Submission Queue (SQ) | 提交队列 | io_uring 中提交请求的环形队列 |
| Completion Queue (CQ) | 完成队列 | io_uring 中接收完成结果的环形队列 |
| System call entry | 系统调用入口 | CPU 从用户程序进入内核的路径 |
| Interrupt | 中断 | 硬件或软件触发的异步事件处理机制 |
| Interrupt Request (IRQ) | 中断请求 | 设备等实体触发的中断事件标识 |
| Softirq | 软中断 | 内核延后执行的一类底半部处理机制 |
| Workqueue | 工作队列 | 将工作交给内核工作线程执行的机制 |
| Device driver | 设备驱动程序 | 控制或抽象硬件设备的内核软件 |
| Character device | 字符设备 | 以字节流语义提供访问的设备类型 |
| Block device | 块设备 | 提供可寻址数据块访问的设备类型 |
| Direct Memory Access (DMA) | 直接内存访问 | 设备不经 CPU 逐字节拷贝而访问内存 |
| I/O scheduler | I/O 调度器 | 对块 I/O 请求排序与调节的机制 |
| poll() | poll 事件轮询接口 | 等待多个文件描述符就绪 |
| select() | select 复用接口 | 等待多个文件描述符状态变化 |
| epoll | epoll 事件通知机制 | Linux 高并发 I/O 就绪事件接口 |
| Event file descriptor (eventfd) | 事件文件描述符 | 用于事件通知的计数器型文件描述符 |
| File descriptor table | 文件描述符表 | 进程管理 FD 到内核文件引用的映射 |

<a id="s08"></a>
## 08 Linux 网络

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Network stack | 网络协议栈 | 内核中实现网络协议的组件 |
| Network interface | 网络接口 | 操作系统发送和接收网络数据的端点 |
| Network Interface Card (NIC) | 网络接口卡 | 物理或虚拟网络适配器 |
| Loopback interface | 环回接口 | 主机与自身通信的接口，如 lo |
| IP address | IP 地址 | 网络层识别接口或节点的地址 |
| Subnet mask | 子网掩码 | 确定 IPv4 网络前缀范围的掩码 |
| CIDR | 无类别域间路由 | 用前缀长度表示地址块的方法 |
| Default gateway | 默认网关 | 无更具体路由时使用的下一跳 |
| Routing table | 路由表 | 用于选择数据包转发路径的信息表 |
| Domain Name System (DNS) | 域名系统 | 将域名解析为记录的分布式系统 |
| Socket | 套接字 | 应用进行网络或本地进程通信的端点 |
| TCP | 传输控制协议 | 面向连接且可靠的字节流协议 |
| UDP | 用户数据报协议 | 无连接的报文传输协议 |
| IP | 网际协议 | 负责网络层编址和数据包转发的协议 |
| ICMP | 互联网控制消息协议 | 用于错误反馈和诊断的网络协议 |
| ARP | 地址解析协议 | 在 IPv4 局域网解析链路层地址的协议 |
| Neighbor Discovery (NDP) | 邻居发现协议 | IPv6 邻居与路由发现机制 |
| Three-way handshake | 三次握手 | TCP 建立连接的同步过程 |
| Four-tuple | 四元组 | 源地址、源端口、目的地址、目的端口 |
| Listen backlog | 监听积压队列 | 待接受连接相关队列的容量概念 |
| Socket buffer | 套接字缓冲区 | 内核用于收发网络数据的缓冲区 |
| Maximum Transmission Unit (MTU) | 最大传输单元 | 链路层可承载的最大网络层报文大小 |
| Network Address Translation (NAT) | 网络地址转换 | 改写报文 IP 地址或端口的机制 |
| Conntrack | 连接跟踪 | 记录网络流量连接状态的子系统 |
| Netfilter | 网络过滤框架 | 内核包过滤、NAT 等处理钩子框架 |
| nftables | nftables 防火墙框架 | Linux 新一代包过滤规则体系 |
| iptables | iptables 规则工具 | 配置传统 Netfilter 规则的用户空间工具 |
| tc (traffic control) | 流量控制工具 | 配置队列规则、分类器和整形策略 |
| qdisc (queueing discipline) | 排队规则 | 网络包队列管理与调度机制 |
| Virtual Ethernet (veth) | 虚拟以太网设备对 | 常用于连接容器与主机网络的接口对 |

<a id="s09"></a>
## 09 用户、权限与安全

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Root user | 超级用户 | 通常拥有用户标识符 0 的账户 |
| User ID (UID) | 用户标识符 | 标识用户身份的数字 ID |
| Group ID (GID) | 组标识符 | 标识用户组的数字 ID |
| File mode | 文件权限模式 | 控制读写执行权限的位字段 |
| Read permission | 读权限 | 允许读取文件或目录内容的权限 |
| Write permission | 写权限 | 允许修改文件或目录项的权限 |
| Execute permission | 执行权限 | 允许执行文件或进入目录的权限 |
| Set-user-ID (setuid) | 设置用户 ID 位 | 执行时按文件所有者身份设置有效 UID |
| Set-group-ID (setgid) | 设置组 ID 位 | 执行时按文件组身份设置有效 GID 等 |
| Sticky bit | 粘滞位 | 目录上限制删除或重命名他人文件的位 |
| Access Control List (ACL) | 访问控制列表 | 提供比传统权限位更细的授权规则 |
| Discretionary Access Control (DAC) | 自主访问控制 | 由对象所有者等决定授权的模型 |
| Mandatory Access Control (MAC) | 强制访问控制 | 由系统安全策略强制执行的访问控制 |
| Security-Enhanced Linux (SELinux) | 安全增强型 Linux | 基于策略的强制访问控制框架 |
| AppArmor | AppArmor 安全框架 | 以配置文件限制程序资源访问 |
| Linux capabilities | Linux 权能 | 把部分超级用户权限分解为独立权能 |
| Least privilege | 最小权限原则 | 只授予完成任务所必需的权限 |
| Privilege escalation | 权限提升 | 获得超出原有授权的权限 |
| seccomp | 安全计算模式 | 限制进程可使用的系统调用 |
| seccomp-BPF | seccomp BPF 过滤 | 按过滤规则限制系统调用 |
| Pluggable Authentication Modules (PAM) | 可插拔认证模块 | 提供可配置的身份认证框架 |
| SSH | 安全外壳协议 | 用于安全远程登录和执行命令 |
| Public key authentication | 公钥认证 | 使用公私钥对验证身份的方法 |
| Sudo | 特权命令执行工具 | 按策略以其他用户身份执行命令 |
| Audit subsystem | 审计子系统 | 记录安全相关系统活动的机制 |

<a id="s10"></a>
## 10 启动、服务与系统管理

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Init process | 初始化进程 | 系统启动后承担初始用户空间管理的进程 |
| PID 1 | 一号进程 | PID 命名空间中的首个进程，通常负责回收孤儿 |
| systemd | systemd 系统管理器 | 提供服务和系统状态管理的套件 |
| Unit | systemd 单元 | systemd 管理的服务、挂载等对象 |
| Service unit | 服务单元 | 描述一个服务及其运行方式的配置 |
| Socket activation | 套接字激活 | 由连接事件按需启动服务的机制 |
| Target unit | 目标单元 | 用于组合其他单元的同步点 |
| systemctl | systemd 控制命令 | 检查、启动和管理 systemd 单元 |
| journalctl | 日志查询命令 | 读取 systemd journal 中的日志 |
| journald | systemd 日志服务 | 收集并管理结构化系统日志 |
| Syslog | 系统日志协议及机制 | 系统消息的标准化记录与传输概念 |
| Cron | 定时任务守护程序 | 根据时间表达式执行任务 |
| Cron expression | Cron 时间表达式 | 描述定时任务触发时刻的语法 |
| System timer | systemd 定时器 | 基于时钟或启动事件触发单元 |
| Package manager | 软件包管理器 | 安装、更新与卸载软件的软件 |
| APT | 高级软件包工具 | Debian 系发行版的软件包管理体系 |
| DPKG | Debian 包管理工具 | 处理 .deb 软件包的底层工具 |
| RPM | RPM 包管理器 | 管理 RPM 软件包的工具及格式 |
| DNF | DNF 软件包管理器 | RPM 系发行版的依赖管理前端 |
| Environment file | 环境配置文件 | 保存服务运行环境变量的文件 |
| Hostname | 主机名 | 系统在网络或本地环境中的名称 |
| NTP | 网络时间协议 | 用于在网络上同步时钟的协议 |
| Time zone | 时区 | 本地民用时间与 UTC 的规则关系 |
| Log rotation | 日志轮转 | 按周期或大小切换并保留日志文件 |
| Runlevel | 运行级别 | 传统 SysV init 使用的系统运行状态 |

<a id="s11"></a>
## 11 容器与虚拟化

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Container | 容器 | 通过内核隔离与资源控制运行的进程环境 |
| Namespace | 命名空间 | 隔离进程所见系统资源的内核机制 |
| PID namespace | PID 命名空间 | 隔离进程编号与进程树视图 |
| Mount namespace | 挂载命名空间 | 隔离挂载点及目录树视图 |
| Network namespace | 网络命名空间 | 隔离接口、路由和部分网络状态 |
| User namespace | 用户命名空间 | 隔离用户及组 ID 映射 |
| IPC namespace | IPC 命名空间 | 隔离部分进程间通信资源 |
| UTS namespace | UTS 命名空间 | 隔离主机名和域名等标识 |
| Cgroup namespace | 控制组命名空间 | 隔离 cgroup 路径视图 |
| Time namespace | 时间命名空间 | 隔离部分内核时钟偏移视图 |
| Control groups (cgroups) | 控制组 | 对进程组进行资源计量、限制与管理 |
| cgroup v2 | 第二版控制组 | 统一层级结构的 cgroup 接口 |
| CPU quota | CPU 配额 | 限制一组任务可消耗的 CPU 时间 |
| Memory limit | 内存限制 | 约束进程组可用内存的上限 |
| Container image | 容器镜像 | 用于创建容器的分层文件系统与配置 |
| Image layer | 镜像层 | 容器镜像可复用的文件系统增量层 |
| Container runtime | 容器运行时 | 负责创建与运行容器的组件 |
| OCI | 开放容器倡议 | 制定镜像与运行时相关规范的组织 |
| runc | runc 运行时 | 实现 OCI 运行时规范的低层容器工具 |
| containerd | containerd 容器运行时 | 管理容器生命周期的运行时服务 |
| chroot | 改变根目录 | 改变进程路径解析的根目录；非完整隔离 |
| Pivot root | 切换根文件系统 | 将挂载树根切换到新目录的操作 |
| Virtual machine (VM) | 虚拟机 | 通过虚拟化运行独立客户机操作系统 |
| Kernel-based Virtual Machine (KVM) | 基于内核的虚拟机 | Linux 内核的硬件辅助虚拟化功能 |
| Hypervisor | 虚拟机监控器 | 创建和管理虚拟机的底层软件 |

<a id="s12"></a>
## 12 系统性能与可观测性

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Observability | 可观测性 | 通过系统输出推断内部运行状态的能力 |
| Telemetry | 遥测数据 | 从系统收集的指标、日志和追踪数据 |
| Metrics | 指标 | 用于量化状态或性能的数值序列 |
| Tracing | 追踪 | 记录系统事件与调用路径的观测方法 |
| Profiling | 性能剖析 | 统计程序时间或资源消耗分布的方法 |
| Sampling | 采样 | 按频率或事件抽取部分观测数据 |
| Flame graph | 火焰图 | 汇总调用栈热点的可视化图表 |
| Latency | 延迟 | 完成一次操作所需的时间 |
| Throughput | 吞吐量 | 单位时间内处理的工作量 |
| QPS | 每秒查询数 | 单位时间内完成的查询数量 |
| P99 latency | P99 延迟 | 99% 样本不超过的延迟值 |
| CPU utilization | CPU 使用率 | CPU 在观察时间内执行工作的比例 |
| Load average | 平均负载 | 一定时段可运行及不可中断任务数的平滑值 |
| I/O wait | I/O 等待 | CPU 空闲且存在待完成 I/O 时的一类记账时间 |
| Context switch rate | 上下文切换率 | 单位时间内发生的上下文切换次数 |
| Page fault rate | 缺页率 | 单位时间内发生的缺页次数 |
| Performance counters | 性能计数器 | 由硬件或软件记录的性能事件计数 |
| Performance Monitoring Unit (PMU) | 性能监控单元 | CPU 提供的硬件性能事件采集单元 |
| perf | Linux perf 工具 | 利用内核性能事件接口进行分析的工具 |
| strace | 系统调用跟踪工具 | 观察程序系统调用与返回结果 |
| ftrace | 内核函数跟踪框架 | Linux 内核自带的事件与函数跟踪框架 |
| tracepoint | 静态跟踪点 | 在内核代码中预定义的观测事件 |
| kprobe | 内核探针 | 在运行时动态探测内核代码位置 |
| uprobes | 用户空间探针 | 动态探测用户程序代码位置 |
| BPF trace | BPF 追踪 | 使用 BPF 程序观测内核运行事件 |
| Pressure Stall Information (PSI) | 资源压力停顿信息 | 统计 CPU、内存、I/O 等资源停顿时间 |
| Bottleneck | 性能瓶颈 | 限制系统整体能力的关键资源或环节 |
| Benchmark | 基准测试 | 在可控条件下测量系统性能 |

<a id="s13"></a>
## 13 eBPF 与内核开发

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Extended Berkeley Packet Filter (eBPF) | 扩展伯克利包过滤器 | 可在受约束的内核执行环境中运行的程序机制 |
| BPF virtual machine | BPF 虚拟机 | 执行 BPF 指令集的抽象运行环境 |
| BPF verifier | BPF 验证器 | 静态检查 BPF 程序安全属性的组件 |
| BPF map | BPF 映射 | 供 BPF 与用户态交换或存储数据的结构 |
| BPF helper | BPF 辅助函数 | 内核向 BPF 程序提供的特定调用 |
| BPF program type | BPF 程序类型 | 决定程序挂载位置及能力的类别 |
| BPF ring buffer | BPF 环形缓冲区 | BPF 事件向用户态传输的共享缓冲 |
| XDP | 快速数据路径 | 在网络驱动早期路径执行 BPF 程序的机制 |
| AF_XDP | AF_XDP 套接字 | 支持高性能包收发的套接字地址族 |
| BPF CO-RE | 一次编译到处运行 | 基于 BTF 等实现跨内核类型适配的方法 |
| BPF Type Format (BTF) | BPF 类型格式 | 提供紧凑类型及调试元数据的格式 |
| libbpf | libbpf 开发库 | 加载和管理 BPF 程序的用户空间库 |
| BPF JIT | BPF 即时编译器 | 将 BPF 指令编译为本机指令的机制 |
| Kernel source tree | 内核源码树 | Linux 内核源文件和构建配置的目录结构 |
| Kbuild | 内核构建系统 | 负责编译内核及模块的构建机制 |
| Kconfig | 内核配置语言及工具 | 表示配置选项与依赖关系的系统 |
| Kernel patch | 内核补丁 | 用于修改内核源码的变更集合 |
| Upstream kernel | 上游内核 | Linux 主线开发社区维护的代码基线 |
| Stable kernel | 稳定版内核 | 面向修复和维护的稳定分支 |
| Longterm kernel (LTS) | 长期维护内核 | 获得较长维护周期的稳定分支 |
| Kernel oops | 内核异常报告 | 内核执行遇到错误时的诊断输出 |
| Kernel panic | 内核恐慌 | 无法安全继续运行时的严重错误状态 |

<a id="s14"></a>
## 14 存储、磁盘与可靠性

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Disk partition | 磁盘分区 | 在块设备上划分出的逻辑区域 |
| Partition table | 分区表 | 描述磁盘分区位置和大小的元数据 |
| GUID Partition Table (GPT) | 全局唯一标识分区表 | 现代磁盘分区表格式 |
| Master Boot Record (MBR) | 主引导记录 | 传统引导和分区记录格式 |
| Logical Volume Manager (LVM) | 逻辑卷管理器 | 对物理存储进行抽象与弹性分配的工具 |
| Physical volume (PV) | 物理卷 | LVM 管理的底层存储成员 |
| Volume group (VG) | 卷组 | LVM 中由一个或多个物理卷组成的资源池 |
| Logical volume (LV) | 逻辑卷 | 从卷组分配的逻辑块设备 |
| RAID | 独立磁盘冗余阵列 | 通过磁盘组合改善冗余或性能的技术 |
| Software RAID | 软件 RAID | 由操作系统软件实现的 RAID |
| Device mapper | 设备映射器 | 内核块设备映射与虚拟化框架 |
| LUKS | Linux 统一密钥设置 | 常用的块设备加密格式及标准 |
| DM-Crypt | 设备映射加密目标 | 通过 device-mapper 提供块级加密 |
| Journaling | 日志式文件系统机制 | 先记录变更以便崩溃恢复的技术 |
| Write-ahead logging (WAL) | 预写式日志 | 更新数据前先记录恢复日志的策略 |
| Writeback | 回写 | 将缓存中的脏数据写入持久存储 |
| Dirty page | 脏页 | 已修改但尚未同步到后端存储的页面 |
| fsync() | 文件同步系统调用 | 请求将文件相关修改刷至持久存储 |
| I/O operations per second (IOPS) | 每秒 I/O 操作数 | 衡量存储随机操作能力的指标 |
| Sequential I/O | 顺序 I/O | 按相邻偏移连续访问数据的模式 |
| Random I/O | 随机 I/O | 在不同偏移位置离散访问数据的模式 |
| Solid State Drive (SSD) | 固态硬盘 | 以闪存等介质存储数据的设备 |
| Non-Volatile Memory Express (NVMe) | 非易失性存储器高速接口 | 主要用于高速存储设备的访问协议 |
| Snapshot | 快照 | 保存某时点逻辑数据状态的机制 |

<a id="s15"></a>
## 15 构建、工具链与调试

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Compiler | 编译器 | 将源代码转换为目标代码的工具 |
| GNU Compiler Collection (GCC) | GNU 编译器套件 | 支持多语言和架构的编译器集合 |
| Clang | Clang 编译器 | 基于 LLVM 的 C/C++ 等语言前端 |
| Linker | 链接器 | 将目标文件和库组合为可执行文件 |
| Assembler | 汇编器 | 把汇编指令转为机器码的工具 |
| Executable and Linkable Format (ELF) | 可执行与可链接格式 | Linux 常用可执行文件和目标文件格式 |
| Dynamic linker | 动态链接器 | 运行时装载共享库并进行符号解析的组件 |
| Shared library | 共享库 | 由多个程序在运行时复用的代码库 |
| Static library | 静态库 | 链接时被复制进目标程序的代码集合 |
| Symbol | 符号 | 编译与链接阶段用于标识对象或函数的名称 |
| Debug symbol | 调试符号 | 帮助将机器地址映射到源码信息的元数据 |
| GNU Debugger (GDB) | GNU 调试器 | 支持断点、单步和内存检查的调试工具 |
| DWARF | DWARF 调试信息格式 | 广泛用于保存源级调试元数据的格式 |
| Core file | 核心文件 | 保存进程崩溃状态用于离线分析的文件 |
| Makefile | Make 构建规则文件 | 描述目标、依赖及构建命令的文件 |
| Cross-compilation | 交叉编译 | 为不同于编译主机的平台构建软件 |
| Build system | 构建系统 | 自动执行编译、链接和产物生成的工具链 |
| Toolchain | 工具链 | 编译器、链接器和相关开发工具的集合 |
| Package dependency | 软件包依赖 | 运行或构建某软件所需的其他软件包 |
| Reproducible build | 可复现构建 | 相同输入及环境产生可验证一致产物的实践 |

<a id="s16"></a>
## 16 故障排查与常见状态

| English / abbreviation | 中文术语 | 简明释义 |
|---|---|---|
| Segmentation fault (SIGSEGV) | 段错误 | 访问不允许的内存地址引发的异常 |
| Permission denied | 权限被拒绝 | 资源访问未通过权限检查 |
| Operation not permitted (EPERM) | 操作不被允许 | 因权限或策略限制导致的错误码 |
| No such file or directory (ENOENT) | 文件或目录不存在 | 指定路径或对象无法找到的错误码 |
| Out of memory (ENOMEM) | 内存不足错误 | 分配内存失败的错误码 |
| Resource temporarily unavailable (EAGAIN) | 资源暂时不可用 | 操作当前不能完成，可能适合重试 |
| Too many open files (EMFILE) | 打开文件过多 | 进程达到文件描述符数量限制 |
| File descriptor leak | 文件描述符泄漏 | 未及时关闭 FD 使资源持续累积 |
| Memory leak | 内存泄漏 | 不再需要的内存仍长期无法释放 |
| Disk full (ENOSPC) | 磁盘空间不足 | 无法获得所需存储空间的错误 |
| Read-only filesystem (EROFS) | 只读文件系统错误 | 尝试写入只读文件系统引发的错误 |
| Kernel taint | 内核污点标记 | 记录特定环境或事件的内核诊断状态 |
| Soft lockup | 软锁死 | CPU 长时间未能完成必要的调度进展 |
| Hard lockup | 硬锁死 | CPU 长时间没有响应预期的硬件监测事件 |
| Watchdog | 看门狗机制 | 监测系统卡顿并触发告警或恢复的机制 |

## 附录 A：容易混淆的概念

- **Kernel vs Distribution**：内核是硬件与资源管理核心；发行版是在内核之上集成用户空间程序、包管理及默认配置的完整系统。
- **User space vs User mode**：用户空间是软件运行与地址空间概念；用户态是 CPU 权限级别概念。二者相关但不等同。
- **Process vs Thread**：进程是资源与地址空间的主要边界；线程共享同一进程的多种资源，但每条线程有自己的执行上下文。
- **PID vs TID**：PID 通常指线程组 ID；TID 标识特定任务。在 Linux 中主线程的 PID 与 TID 常相同。
- **File descriptor vs Inode**：FD 是进程局部整数句柄；inode 表示文件系统对象的元数据。不同 FD 可以访问同一 inode。
- **Hard link vs Symlink**：硬链接是同一 inode 的不同名称；符号链接是保存路径的独立文件，可能成为悬空链接。
- **Page cache vs Buffer cache**：现代 Linux 中页缓存负责大量文件数据缓存；“缓冲缓存”常泛指块设备元数据等历史及实现概念。
- **RSS vs VMS**：RSS 表示驻留物理内存的量；VMS 表示虚拟地址空间范围，不能直接看作实际内存消耗。
- **Load average vs CPU utilization**：平均负载是任务数量的时间平滑统计；CPU 使用率是 CPU 时间占比，高负载并不总意味高 CPU 使用率。
- **OOM vs Memory leak**：OOM 是资源分配失败的状态；内存泄漏是一种潜在原因，也可能由流量峰值、限制配置等导致 OOM。
- **Mutex vs Spinlock**：互斥锁等待时通常可以睡眠；自旋锁等待时忙等，适合特定短临界区和内核上下文。
- **CFS vs EEVDF**：CFS 是长期使用的公平调度方案；Linux 自 6.6 版本起逐步向 EEVDF 演进，不能视为同时并行的两个默认调度器。
- **Blocking vs Synchronous I/O**：阻塞描述调用是否等待；同步描述完成语义。同步操作可以设置为非阻塞。
- **Container vs Virtual machine**：容器通常共享宿主内核；虚拟机通常拥有独立客户机内核，并通过虚拟化抽象硬件。
- **Namespace vs Cgroups**：命名空间主要隔离“看见什么”；cgroups 主要计量、限制与控制“能用多少”。
- **iptables vs nftables**：iptables 是传统用户空间规则工具；nftables 是新一代规则体系，发行版可能通过兼容后端提供 iptables 命令。
- **I/O wait vs Storage latency**：iowait 是 CPU 时间记账维度，不是单次磁盘请求耗时，不能仅凭 iowait 推断设备延迟。
- **syscall vs glibc function**：系统调用直接进入内核；glibc 函数可能封装一个或多个系统调用，也可能完全在用户态完成。

## 附录 B：参考资料

- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/)
- [EEVDF Scheduler - Linux Kernel documentation](https://www.kernel.org/doc/html/latest/scheduler/sched-eevdf.html)
- [RCU Concepts - Linux Kernel documentation](https://www.kernel.org/doc/html/latest/RCU/)
- [Linux man-pages project](https://man7.org/linux/man-pages/)
- [Filesystem Hierarchy Standard 3.0 (freedesktop.org)](https://specifications.freedesktop.org/fhs/latest/)
- [systemd Manual Pages](https://www.freedesktop.org/software/systemd/man/)
- [eBPF Documentation](https://docs.ebpf.io/)
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)

> 本文档按技术实践常见含义整理，非官方标准全文。

---

[项目首页](../README.zh-CN.md) · [下载 PDF](../pdf/linux.pdf) · [结构化索引](../data/terms.json)
