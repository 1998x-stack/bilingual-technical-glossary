# 计算机组成原理：专有名词中英文对照表

> Computer Organization & Architecture — Bilingual Technical Glossary

> 版本：2026.11 · 共 15 个专题、678 条术语 · 编辑原则：中文优先，遵循通行英文教材和硬件文档表述。

## 目录

- 01 计算机系统与体系结构（Architecture & System Organization）— 41 条
- 02 数字逻辑与电路（Digital Logic & Circuits）— 44 条
- 03 数据表示与编码（Data Representation & Encoding）— 56 条
- 04 算术逻辑与运算器（Arithmetic & Logic Operations）— 43 条
- 05 指令系统与寻址方式（Instruction Set & Addressing）— 53 条
- 06 CPU 结构与数据通路（CPU Organization & Datapath）— 37 条
- 07 控制单元与异常中断（Control Unit & Exceptions）— 36 条
- 08 流水线、预测与乱序执行（Pipelining & Out-of-Order Execution）— 58 条
- 09 主存与存储器器件（Main Memory & Memory Devices）— 40 条
- 10 缓存与存储层次（Cache & Memory Hierarchy）— 54 条
- 11 虚拟存储与地址转换（Virtual Memory & Address Translation）— 41 条
- 12 总线、互连与 I/O 系统（Interconnects & I/O）— 45 条
- 13 并行计算、多核与一致性（Parallelism, Multicore & Coherence）— 49 条
- 14 性能评估与功耗（Performance & Power）— 41 条
- 15 可靠性、安全与现代架构（Reliability, Security & Modern Architecture）— 40 条

---

## 01 计算机系统与体系结构
*Architecture & System Organization · 41 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 计算机组成原理 | Computer Organization |
| 计算机体系结构 | Computer Architecture |
| 微体系结构 | Microarchitecture |
| 指令集体系结构 | Instruction Set Architecture (ISA) |
| 硬件 | Hardware |
| 软件 | Software |
| 固件 | Firmware |
| 计算机系统 | Computer System |
| 通用计算机 | General-Purpose Computer |
| 专用计算机 | Special-Purpose Computer |
| 嵌入式系统 | Embedded System |
| 片上系统 | System on a Chip (SoC) |
| 中央处理器 | Central Processing Unit (CPU) |
| 图形处理器 | Graphics Processing Unit (GPU) |
| 加速器 | Accelerator |
| 主存储器 | Main Memory |
| 辅助存储器 | Secondary Storage |
| 外部设备 | Peripheral Device |
| 输入设备 | Input Device |
| 输出设备 | Output Device |
| 存储程序概念 | Stored-Program Concept |
| 冯·诺依曼体系结构 | von Neumann Architecture |
| 哈佛体系结构 | Harvard Architecture |
| 改进型哈佛体系结构 | Modified Harvard Architecture |
| 冯·诺依曼瓶颈 | von Neumann Bottleneck |
| 数据通路 | Datapath |
| 控制通路 | Control Path |
| 内存层次结构 | Memory Hierarchy |
| 抽象层次 | Level of Abstraction |
| 硬件描述语言 | Hardware Description Language (HDL) |
| 寄存器传输级 | Register-Transfer Level (RTL) |
| 逻辑门级 | Gate Level |
| 晶体管级 | Transistor Level |
| 制程工艺 | Process Technology |
| 工艺节点 | Process Node |
| 芯片面积 | Die Area |
| 时钟周期 | Clock Cycle |
| 时钟频率 | Clock Frequency |
| 系统时钟 | System Clock |
| 同步电路 | Synchronous Circuit |
| 异步电路 | Asynchronous Circuit |

## 02 数字逻辑与电路
*Digital Logic & Circuits · 44 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 布尔代数 | Boolean Algebra |
| 布尔函数 | Boolean Function |
| 逻辑门 | Logic Gate |
| 与门 | AND Gate |
| 或门 | OR Gate |
| 非门 | NOT Gate / Inverter |
| 与非门 | NAND Gate |
| 或非门 | NOR Gate |
| 异或门 | XOR Gate |
| 同或门 | XNOR Gate |
| 真值表 | Truth Table |
| 逻辑表达式 | Logic Expression |
| 组合逻辑电路 | Combinational Logic Circuit |
| 时序逻辑电路 | Sequential Logic Circuit |
| 加法器 | Adder |
| 半加器 | Half Adder |
| 全加器 | Full Adder |
| 多路选择器 | Multiplexer (MUX) |
| 解复用器 | Demultiplexer (DEMUX) |
| 译码器 | Decoder |
| 编码器 | Encoder |
| 优先编码器 | Priority Encoder |
| 比较器 | Comparator |
| 三态门 | Tri-State Gate |
| 触发器 | Flip-Flop |
| 锁存器 | Latch |
| D 触发器 | D Flip-Flop |
| JK 触发器 | JK Flip-Flop |
| 寄存器 | Register |
| 移位寄存器 | Shift Register |
| 计数器 | Counter |
| 有限状态机 | Finite-State Machine (FSM) |
| 状态转换 | State Transition |
| 建立时间 | Setup Time |
| 保持时间 | Hold Time |
| 传播延迟 | Propagation Delay |
| 时钟偏斜 | Clock Skew |
| 时钟抖动 | Clock Jitter |
| 关键路径 | Critical Path |
| 亚稳态 | Metastability |
| 时钟域交叉 | Clock Domain Crossing (CDC) |
| 同步器 | Synchronizer |
| 复位信号 | Reset Signal |
| 流水线寄存器 | Pipeline Register |

## 03 数据表示与编码
*Data Representation & Encoding · 56 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 比特 | Bit |
| 字节 | Byte |
| 字 | Word |
| 字长 | Word Length |
| 机器字 | Machine Word |
| 位宽 | Bit Width |
| 最高有效位 | Most Significant Bit (MSB) |
| 最低有效位 | Least Significant Bit (LSB) |
| 大端序 | Big-Endian |
| 小端序 | Little-Endian |
| 字节序 | Endianness |
| 地址对齐 | Address Alignment |
| 非对齐访问 | Unaligned Access |
| 二进制 | Binary |
| 八进制 | Octal |
| 十进制 | Decimal |
| 十六进制 | Hexadecimal |
| 基数 | Radix / Base |
| 位模式 | Bit Pattern |
| 有符号整数 | Signed Integer |
| 无符号整数 | Unsigned Integer |
| 原码 | Sign-Magnitude Representation |
| 反码 | Ones' Complement |
| 补码 | Two's Complement |
| 符号位 | Sign Bit |
| 符号扩展 | Sign Extension |
| 零扩展 | Zero Extension |
| 截断 | Truncation |
| 溢出 | Overflow |
| 上溢 | Overflow (Out of Range) |
| 下溢 | Underflow |
| 进位 | Carry |
| 借位 | Borrow |
| 定点数 | Fixed-Point Number |
| 浮点数 | Floating-Point Number |
| 尾数 / 有效数 | Significand / Mantissa |
| 指数 | Exponent |
| 偏置指数 | Biased Exponent |
| 规格化数 | Normalized Number |
| 非规格化数 | Subnormal Number |
| 机器精度 | Machine Precision |
| 舍入模式 | Rounding Mode |
| 就近舍入 | Round to Nearest |
| 向零舍入 | Round Toward Zero |
| IEEE 754 浮点标准 | IEEE 754 Floating-Point Standard |
| 单精度浮点数 | Single-Precision Floating Point (binary32) |
| 双精度浮点数 | Double-Precision Floating Point (binary64) |
| 半精度浮点数 | Half-Precision Floating Point (binary16) |
| 脑浮点格式 | Brain Floating Point (bfloat16) |
| 非数值 | Not a Number (NaN) |
| 无穷大 | Infinity |
| 奇偶校验位 | Parity Bit |
| 格雷码 | Gray Code |
| 二进制编码的十进制 | Binary-Coded Decimal (BCD) |
| 美国信息交换标准代码 | American Standard Code for Information Interchange (ASCII) |
| 统一码 | Unicode |

## 04 算术逻辑与运算器
*Arithmetic & Logic Operations · 43 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 算术逻辑单元 | Arithmetic Logic Unit (ALU) |
| 浮点运算单元 | Floating-Point Unit (FPU) |
| 整数运算单元 | Integer Execution Unit |
| 加法运算 | Addition |
| 减法运算 | Subtraction |
| 乘法运算 | Multiplication |
| 除法运算 | Division |
| 模运算 | Modulo Operation |
| 逻辑左移 | Logical Left Shift |
| 逻辑右移 | Logical Right Shift |
| 算术右移 | Arithmetic Right Shift |
| 循环移位 | Rotate / Circular Shift |
| 按位与 | Bitwise AND |
| 按位或 | Bitwise OR |
| 按位异或 | Bitwise XOR |
| 按位取反 | Bitwise NOT |
| 逻辑与 | Logical AND |
| 逻辑或 | Logical OR |
| 算术标志位 | Arithmetic Status Flag |
| 零标志 | Zero Flag (ZF) |
| 进位标志 | Carry Flag (CF) |
| 溢出标志 | Overflow Flag (OF) |
| 符号标志 | Sign Flag (SF) |
| 条件码 | Condition Code |
| 进位传播 | Carry Propagation |
| 行波进位加法器 | Ripple-Carry Adder |
| 超前进位加法器 | Carry-Lookahead Adder |
| 进位保存加法器 | Carry-Save Adder |
| 前缀加法器 | Prefix Adder |
| 布斯乘法算法 | Booth's Multiplication Algorithm |
| 阵列乘法器 | Array Multiplier |
| 部分积 | Partial Product |
| 恢复余数除法 | Restoring Division |
| 不恢复余数除法 | Non-Restoring Division |
| 移位加法乘法 | Shift-and-Add Multiplication |
| 浮点异常 | Floating-Point Exception |
| 取消误差 | Cancellation Error |
| 舍入误差 | Rounding Error |
| 保护位 | Guard Bit |
| 舍入位 | Round Bit |
| 粘滞位 | Sticky Bit |
| 融合乘加 | Fused Multiply-Add (FMA) |
| 饱和算术 | Saturating Arithmetic |

## 05 指令系统与寻址方式
*Instruction Set & Addressing · 53 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 机器指令 | Machine Instruction |
| 指令集 | Instruction Set |
| 操作码 | Opcode |
| 操作数 | Operand |
| 源操作数 | Source Operand |
| 目的操作数 | Destination Operand |
| 指令格式 | Instruction Format |
| 指令长度 | Instruction Length |
| 定长指令 | Fixed-Length Instruction |
| 变长指令 | Variable-Length Instruction |
| 立即数 | Immediate |
| 寄存器操作数 | Register Operand |
| 指令编码 | Instruction Encoding |
| 指令译码 | Instruction Decoding |
| 指令类型 | Instruction Type |
| 数据传送指令 | Data Movement Instruction |
| 算术指令 | Arithmetic Instruction |
| 逻辑指令 | Logical Instruction |
| 移位指令 | Shift Instruction |
| 分支指令 | Branch Instruction |
| 条件分支 | Conditional Branch |
| 无条件跳转 | Unconditional Jump |
| 函数调用 | Function Call |
| 返回指令 | Return Instruction |
| 加载指令 | Load Instruction |
| 存储指令 | Store Instruction |
| 空操作指令 | No Operation (NOP) |
| 特权指令 | Privileged Instruction |
| 系统调用 | System Call |
| 陷入指令 | Trap Instruction |
| 寻址方式 | Addressing Mode |
| 有效地址 | Effective Address (EA) |
| 立即寻址 | Immediate Addressing |
| 直接寻址 | Direct Addressing |
| 间接寻址 | Indirect Addressing |
| 寄存器寻址 | Register Addressing |
| 寄存器间接寻址 | Register-Indirect Addressing |
| 基址寻址 | Base Addressing |
| 变址寻址 | Indexed Addressing |
| 基址加变址寻址 | Base-Indexed Addressing |
| 相对寻址 | Relative Addressing |
| 程序计数器相对寻址 | PC-Relative Addressing |
| 隐含寻址 | Implied Addressing |
| 栈寻址 | Stack Addressing |
| 复杂指令集计算机 | Complex Instruction Set Computer (CISC) |
| 精简指令集计算机 | Reduced Instruction Set Computer (RISC) |
| 加载-存储体系结构 | Load-Store Architecture |
| 零地址指令 | Zero-Address Instruction |
| 一地址指令 | One-Address Instruction |
| 二地址指令 | Two-Address Instruction |
| 三地址指令 | Three-Address Instruction |
| 向量指令 | Vector Instruction |
| 单指令多数据 | Single Instruction, Multiple Data (SIMD) |

## 06 CPU 结构与数据通路
*CPU Organization & Datapath · 37 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 处理器核 | Processor Core |
| 处理器封装 | Processor Package |
| 逻辑处理器 | Logical Processor |
| 程序计数器 | Program Counter (PC) |
| 指令寄存器 | Instruction Register (IR) |
| 存储器地址寄存器 | Memory Address Register (MAR) |
| 存储器数据寄存器 | Memory Data Register (MDR) |
| 通用寄存器 | General-Purpose Register (GPR) |
| 专用寄存器 | Special-Purpose Register |
| 寄存器堆 | Register File |
| 栈指针 | Stack Pointer (SP) |
| 帧指针 | Frame Pointer (FP) |
| 状态寄存器 | Status Register |
| 程序状态字 | Program Status Word (PSW) |
| 控制寄存器 | Control Register |
| 指令指针 | Instruction Pointer (IP) |
| 取指单元 | Instruction Fetch Unit |
| 译码单元 | Decode Unit |
| 执行单元 | Execution Unit |
| 加载存储单元 | Load/Store Unit (LSU) |
| 地址生成单元 | Address Generation Unit (AGU) |
| 分支单元 | Branch Unit |
| 提交单元 | Retirement Unit |
| 内部总线 | Internal Bus |
| 单总线数据通路 | Single-Bus Datapath |
| 多总线数据通路 | Multi-Bus Datapath |
| 单周期处理器 | Single-Cycle Processor |
| 多周期处理器 | Multi-Cycle Processor |
| 硬连线数据通路 | Hardwired Datapath |
| 微操作 | Micro-Operation (µop) |
| 寄存器传送 | Register Transfer |
| 指令周期 | Instruction Cycle |
| 取指阶段 | Instruction Fetch Stage |
| 译码阶段 | Instruction Decode Stage |
| 执行阶段 | Execute Stage |
| 访存阶段 | Memory Access Stage |
| 写回阶段 | Writeback Stage |

## 07 控制单元与异常中断
*Control Unit & Exceptions · 36 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 控制单元 | Control Unit (CU) |
| 控制信号 | Control Signal |
| 控制字 | Control Word |
| 控制存储器 | Control Store |
| 硬布线控制 | Hardwired Control |
| 微程序控制 | Microprogrammed Control |
| 微程序 | Microprogram |
| 微指令 | Microinstruction |
| 微地址 | Microaddress |
| 微程序计数器 | Microprogram Counter |
| 水平型微指令 | Horizontal Microinstruction |
| 垂直型微指令 | Vertical Microinstruction |
| 组合逻辑控制 | Combinational Control Logic |
| 指令执行顺序 | Instruction Execution Sequence |
| 中断 | Interrupt |
| 异常 | Exception |
| 故障 | Fault |
| 陷阱 | Trap |
| 中止 | Abort |
| 外部中断 | External Interrupt |
| 内部异常 | Internal Exception |
| 可屏蔽中断 | Maskable Interrupt |
| 不可屏蔽中断 | Non-Maskable Interrupt (NMI) |
| 中断向量 | Interrupt Vector |
| 中断向量表 | Interrupt Vector Table (IVT) |
| 中断服务程序 | Interrupt Service Routine (ISR) |
| 中断优先级 | Interrupt Priority |
| 中断屏蔽 | Interrupt Masking |
| 中断延迟 | Interrupt Latency |
| 精确异常 | Precise Exception |
| 非精确异常 | Imprecise Exception |
| 异常处理程序 | Exception Handler |
| 特权级 | Privilege Level |
| 用户态 | User Mode |
| 内核态 | Kernel Mode |
| 上下文切换 | Context Switch |

## 08 流水线、预测与乱序执行
*Pipelining & Out-of-Order Execution · 58 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 指令流水线 | Instruction Pipeline |
| 流水线级 | Pipeline Stage |
| 流水线深度 | Pipeline Depth |
| 流水线吞吐量 | Pipeline Throughput |
| 流水线延迟 | Pipeline Latency |
| 流水线填充 | Pipeline Fill |
| 流水线排空 | Pipeline Drain |
| 流水线气泡 | Pipeline Bubble |
| 流水线停顿 | Pipeline Stall |
| 结构冒险 | Structural Hazard |
| 数据冒险 | Data Hazard |
| 控制冒险 | Control Hazard |
| 写后读相关 | Read After Write (RAW) |
| 读后写相关 | Write After Read (WAR) |
| 写后写相关 | Write After Write (WAW) |
| 真相关 | True Dependency |
| 反相关 | Anti-Dependency |
| 输出相关 | Output Dependency |
| 操作数转发 | Operand Forwarding |
| 旁路技术 | Bypassing |
| 互锁 | Interlock |
| 冒险检测单元 | Hazard Detection Unit |
| 分支预测 | Branch Prediction |
| 静态分支预测 | Static Branch Prediction |
| 动态分支预测 | Dynamic Branch Prediction |
| 分支目标缓冲器 | Branch Target Buffer (BTB) |
| 分支历史表 | Branch History Table (BHT) |
| 全局历史寄存器 | Global History Register (GHR) |
| 返回地址栈 | Return Address Stack (RAS) |
| 分支预测失误 | Branch Misprediction |
| 错误路径执行 | Wrong-Path Execution |
| 推测执行 | Speculative Execution |
| 超标量处理器 | Superscalar Processor |
| 多发射 | Multiple Issue |
| 发射宽度 | Issue Width |
| 指令级并行 | Instruction-Level Parallelism (ILP) |
| 乱序执行 | Out-of-Order Execution (OoO) |
| 顺序执行 | In-Order Execution |
| 乱序发射 | Out-of-Order Issue |
| 顺序提交 | In-Order Retirement |
| 寄存器重命名 | Register Renaming |
| 重命名映射表 | Rename Map Table |
| 物理寄存器 | Physical Register |
| 架构寄存器 | Architectural Register |
| 重排序缓冲区 | Reorder Buffer (ROB) |
| 保留站 | Reservation Station |
| 发射队列 | Issue Queue |
| 加载队列 | Load Queue |
| 存储队列 | Store Queue |
| 加载存储队列 | Load/Store Queue (LSQ) |
| 动态调度 | Dynamic Scheduling |
| 记分牌算法 | Scoreboarding |
| 托马苏洛算法 | Tomasulo's Algorithm |
| 操作数就绪 | Operand Readiness |
| 提交 / 退役 | Commit / Retirement |
| 流水线冲刷 | Pipeline Flush |
| 微操作融合 | Micro-Operation Fusion |
| 宏操作融合 | Macro-Fusion |

## 09 主存与存储器器件
*Main Memory & Memory Devices · 40 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 存储单元 | Memory Cell |
| 存储地址 | Memory Address |
| 存储字 | Memory Word |
| 存储容量 | Memory Capacity |
| 存储器访问时间 | Memory Access Time |
| 存储器周期 | Memory Cycle Time |
| 读操作 | Read Operation |
| 写操作 | Write Operation |
| 随机访问存储器 | Random-Access Memory (RAM) |
| 只读存储器 | Read-Only Memory (ROM) |
| 静态随机访问存储器 | Static RAM (SRAM) |
| 动态随机访问存储器 | Dynamic RAM (DRAM) |
| 同步动态随机访问存储器 | Synchronous DRAM (SDRAM) |
| 双倍数据速率存储器 | Double Data Rate SDRAM (DDR SDRAM) |
| 高带宽存储器 | High Bandwidth Memory (HBM) |
| 非易失性存储器 | Non-Volatile Memory (NVM) |
| 易失性存储器 | Volatile Memory |
| 闪存 | Flash Memory |
| 与非型闪存 | NAND Flash |
| 或非型闪存 | NOR Flash |
| 电可擦可编程只读存储器 | Electrically Erasable Programmable ROM (EEPROM) |
| 存储阵列 | Memory Array |
| 存储体 | Memory Bank |
| 存储通道 | Memory Channel |
| 存储器控制器 | Memory Controller |
| 行缓冲区 | Row Buffer |
| 行地址选通 | Row Address Strobe (RAS) |
| 列地址选通 | Column Address Strobe (CAS) |
| 预充电 | Precharge |
| 刷新 | Refresh |
| 自动刷新 | Auto-Refresh |
| 突发传输 | Burst Transfer |
| 内存交叉编址 | Memory Interleaving |
| 内存映射 | Memory Mapping |
| 内存地址映射 | Memory Address Mapping |
| 地址译码 | Address Decoding |
| 内存带宽 | Memory Bandwidth |
| 内存延迟 | Memory Latency |
| 纠错码存储器 | Error-Correcting Code Memory (ECC Memory) |
| 双列直插式内存模块 | Dual In-Line Memory Module (DIMM) |

## 10 缓存与存储层次
*Cache & Memory Hierarchy · 54 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 高速缓存 | Cache |
| 一级缓存 | Level 1 Cache (L1 Cache) |
| 二级缓存 | Level 2 Cache (L2 Cache) |
| 三级缓存 | Level 3 Cache (L3 Cache) |
| 指令缓存 | Instruction Cache (I-Cache) |
| 数据缓存 | Data Cache (D-Cache) |
| 统一缓存 | Unified Cache |
| 缓存行 | Cache Line |
| 缓存块 | Cache Block |
| 缓存组 | Cache Set |
| 缓存路 | Cache Way |
| 缓存标签 | Cache Tag |
| 有效位 | Valid Bit |
| 脏位 | Dirty Bit |
| 缓存命中 | Cache Hit |
| 缓存未命中 | Cache Miss |
| 命中率 | Hit Rate |
| 未命中率 | Miss Rate |
| 命中时间 | Hit Time |
| 未命中代价 | Miss Penalty |
| 平均存储器访问时间 | Average Memory Access Time (AMAT) |
| 直接映射缓存 | Direct-Mapped Cache |
| 全相联缓存 | Fully Associative Cache |
| 组相联缓存 | Set-Associative Cache |
| 相联度 | Associativity |
| 容量未命中 | Capacity Miss |
| 冲突未命中 | Conflict Miss |
| 强制性未命中 | Compulsory Miss / Cold Miss |
| 一致性未命中 | Coherence Miss |
| 最近最少使用 | Least Recently Used (LRU) |
| 伪最近最少使用 | Pseudo-LRU (PLRU) |
| 先进先出替换 | First-In, First-Out (FIFO) Replacement |
| 随机替换 | Random Replacement |
| 写直达策略 | Write-Through Policy |
| 写回策略 | Write-Back Policy |
| 写分配策略 | Write-Allocate Policy |
| 非写分配策略 | No-Write-Allocate Policy |
| 写缓冲区 | Write Buffer |
| 存储缓冲区 | Store Buffer |
| 预取 | Prefetching |
| 硬件预取器 | Hardware Prefetcher |
| 软件预取 | Software Prefetching |
| 缓存污染 | Cache Pollution |
| 缓存颠簸 | Cache Thrashing |
| 多级缓存 | Multilevel Cache |
| 包含式缓存 | Inclusive Cache |
| 排他式缓存 | Exclusive Cache |
| 非包含式缓存 | Non-Inclusive Cache |
| 非阻塞缓存 | Non-Blocking Cache |
| 未完成缺失状态寄存器 | Miss Status Holding Register (MSHR) |
| 写合并 | Write Combining |
| 时间局部性 | Temporal Locality |
| 空间局部性 | Spatial Locality |
| 引用局部性 | Locality of Reference |

## 11 虚拟存储与地址转换
*Virtual Memory & Address Translation · 41 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 虚拟内存 | Virtual Memory |
| 虚拟地址 | Virtual Address (VA) |
| 物理地址 | Physical Address (PA) |
| 地址空间 | Address Space |
| 虚拟地址空间 | Virtual Address Space |
| 物理地址空间 | Physical Address Space |
| 地址转换 | Address Translation |
| 内存管理单元 | Memory Management Unit (MMU) |
| 页 | Page |
| 页框 | Page Frame |
| 页大小 | Page Size |
| 页表 | Page Table |
| 页表项 | Page Table Entry (PTE) |
| 多级页表 | Multilevel Page Table |
| 页表基址寄存器 | Page Table Base Register (PTBR) |
| 转换检测缓冲区 | Translation Lookaside Buffer (TLB) |
| 指令 TLB | Instruction TLB (ITLB) |
| 数据 TLB | Data TLB (DTLB) |
| TLB 命中 | TLB Hit |
| TLB 未命中 | TLB Miss |
| 页表遍历 | Page Table Walk |
| 缺页异常 | Page Fault |
| 按需分页 | Demand Paging |
| 页面置换 | Page Replacement |
| 工作集 | Working Set |
| 页面抖动 | Page Thrashing |
| 交换空间 | Swap Space |
| 交换进出 | Swapping |
| 大页 | Huge Page / Large Page |
| 页内偏移 | Page Offset |
| 虚拟页号 | Virtual Page Number (VPN) |
| 物理页号 | Physical Page Number (PPN) |
| 虚拟索引物理标记缓存 | Virtually Indexed, Physically Tagged (VIPT) Cache |
| 物理索引物理标记缓存 | Physically Indexed, Physically Tagged (PIPT) Cache |
| 虚拟索引虚拟标记缓存 | Virtually Indexed, Virtually Tagged (VIVT) Cache |
| TLB 刷新跨核广播 | TLB Shootdown |
| 地址空间标识符 | Address Space Identifier (ASID) |
| 进程上下文标识符 | Process-Context Identifier (PCID) |
| 内存保护 | Memory Protection |
| 页级权限 | Page-Level Permission |
| 执行禁止位 | Execute-Never Bit (XN / NX) |

## 12 总线、互连与 I/O 系统
*Interconnects & I/O · 45 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 总线 | Bus |
| 系统总线 | System Bus |
| 地址总线 | Address Bus |
| 数据总线 | Data Bus |
| 控制总线 | Control Bus |
| 总线宽度 | Bus Width |
| 总线周期 | Bus Cycle |
| 总线仲裁 | Bus Arbitration |
| 总线主设备 | Bus Master |
| 总线从设备 | Bus Slave / Target |
| 总线事务 | Bus Transaction |
| 总线突发传输 | Bus Burst Transfer |
| 互连网络 | Interconnect Network |
| 点对点互连 | Point-to-Point Interconnect |
| 交叉开关 | Crossbar Switch |
| 环形互连 | Ring Interconnect |
| 网格互连 | Mesh Interconnect |
| 片上网络 | Network on Chip (NoC) |
| 外围组件互连快速通道 | Peripheral Component Interconnect Express (PCIe) |
| 高级微控制器总线架构 | Advanced Microcontroller Bus Architecture (AMBA) |
| 高级可扩展接口 | Advanced eXtensible Interface (AXI) |
| 输入 / 输出 | Input/Output (I/O) |
| I/O 接口 | I/O Interface |
| I/O 端口 | I/O Port |
| 内存映射 I/O | Memory-Mapped I/O (MMIO) |
| 独立编址 I/O | Isolated I/O / Port-Mapped I/O |
| 程序查询 I/O | Programmed I/O (PIO) |
| 轮询 | Polling |
| 中断驱动 I/O | Interrupt-Driven I/O |
| 直接存储器访问 | Direct Memory Access (DMA) |
| DMA 控制器 | DMA Controller |
| I/O 内存管理单元 | I/O Memory Management Unit (IOMMU) |
| 设备控制器 | Device Controller |
| 设备寄存器 | Device Register |
| 命令寄存器 | Command Register |
| 状态寄存器（设备） | Device Status Register |
| 数据寄存器（设备） | Device Data Register |
| 设备驱动程序 | Device Driver |
| 缓冲区 | Buffer |
| 双缓冲 | Double Buffering |
| 零拷贝 | Zero-Copy |
| 存储控制器 | Storage Controller |
| 非易失性存储器快速协议 | Non-Volatile Memory Express (NVMe) |
| 串行 ATA | Serial ATA (SATA) |
| 通用串行总线 | Universal Serial Bus (USB) |

## 13 并行计算、多核与一致性
*Parallelism, Multicore & Coherence · 49 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 并行计算 | Parallel Computing |
| 并发 | Concurrency |
| 并行 | Parallelism |
| 多核处理器 | Multicore Processor |
| 多处理器系统 | Multiprocessor System |
| 共享内存 | Shared Memory |
| 分布式内存 | Distributed Memory |
| 对称多处理 | Symmetric Multiprocessing (SMP) |
| 非统一内存访问 | Non-Uniform Memory Access (NUMA) |
| 统一内存访问 | Uniform Memory Access (UMA) |
| 同时多线程 | Simultaneous Multithreading (SMT) |
| 硬件线程 | Hardware Thread |
| 线程级并行 | Thread-Level Parallelism (TLP) |
| 数据级并行 | Data-Level Parallelism (DLP) |
| 任务级并行 | Task-Level Parallelism |
| 单指令单数据 | Single Instruction, Single Data (SISD) |
| 单指令多数据 | Single Instruction, Multiple Data (SIMD) |
| 多指令单数据 | Multiple Instruction, Single Data (MISD) |
| 多指令多数据 | Multiple Instruction, Multiple Data (MIMD) |
| 单指令多线程 | Single Instruction, Multiple Threads (SIMT) |
| 向量处理器 | Vector Processor |
| 向量寄存器 | Vector Register |
| 向量长度 | Vector Length |
| 向量化 | Vectorization |
| GPU 线程束 | Warp |
| GPU 线程块 | Thread Block |
| 内存一致性 | Memory Consistency |
| 缓存一致性 | Cache Coherence |
| 缓存一致性协议 | Cache Coherence Protocol |
| MESI 协议 | Modified, Exclusive, Shared, Invalid (MESI) Protocol |
| MOESI 协议 | Modified, Owned, Exclusive, Shared, Invalid (MOESI) Protocol |
| 失效协议 | Invalidation Protocol |
| 更新协议 | Update Protocol |
| 窥探协议 | Snooping Protocol |
| 目录协议 | Directory-Based Protocol |
| 伪共享 | False Sharing |
| 内存一致性模型 | Memory Consistency Model |
| 顺序一致性 | Sequential Consistency |
| 弱内存序 | Weak Memory Ordering |
| 内存屏障 | Memory Barrier / Fence |
| 读屏障 | Read Barrier |
| 写屏障 | Write Barrier |
| 原子操作 | Atomic Operation |
| 比较并交换 | Compare-and-Swap (CAS) |
| 加载链接 / 条件存储 | Load-Linked / Store-Conditional (LL/SC) |
| 获取语义 | Acquire Semantics |
| 释放语义 | Release Semantics |
| 竞争条件 | Race Condition |
| 数据竞争 | Data Race |

## 14 性能评估与功耗
*Performance & Power · 41 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 性能 | Performance |
| 执行时间 | Execution Time |
| 响应时间 | Response Time |
| 吞吐量 | Throughput |
| 延迟 | Latency |
| 时钟频率 | Clock Frequency |
| 时钟周期时间 | Clock Period |
| 时钟周期数 | Clock Cycles |
| 每条指令平均周期数 | Cycles Per Instruction (CPI) |
| 每周期指令数 | Instructions Per Cycle (IPC) |
| 指令数 | Instruction Count (IC) |
| 每秒百万条指令 | Million Instructions Per Second (MIPS) |
| 每秒浮点运算次数 | Floating-Point Operations Per Second (FLOPS) |
| 峰值性能 | Peak Performance |
| 持续性能 | Sustained Performance |
| 基准测试 | Benchmark |
| 微基准测试 | Microbenchmark |
| 性能计数器 | Performance Counter |
| 硬件性能监控单元 | Performance Monitoring Unit (PMU) |
| 性能剖析 | Profiling |
| 热点 | Hotspot |
| 加速比 | Speedup |
| 阿姆达尔定律 | Amdahl's Law |
| 古斯塔夫森定律 | Gustafson's Law |
| 屋顶线模型 | Roofline Model |
| 运算强度 | Arithmetic Intensity |
| 算力瓶颈 | Compute Bound |
| 内存带宽瓶颈 | Memory-Bandwidth Bound |
| 延迟瓶颈 | Latency Bound |
| 能耗 | Energy Consumption |
| 功耗 | Power Consumption |
| 静态功耗 | Static Power |
| 动态功耗 | Dynamic Power |
| 漏电功耗 | Leakage Power |
| 热设计功耗 | Thermal Design Power (TDP) |
| 每瓦性能 | Performance per Watt |
| 动态电压频率调整 | Dynamic Voltage and Frequency Scaling (DVFS) |
| 功耗门控 | Power Gating |
| 时钟门控 | Clock Gating |
| 降频 | Throttling |
| 散热 | Heat Dissipation |

## 15 可靠性、安全与现代架构
*Reliability, Security & Modern Architecture · 40 terms*

| 中文术语 | English Term |
| :--- | :--- |
| 可靠性 | Reliability |
| 可用性 | Availability |
| 容错 | Fault Tolerance |
| 单比特错误 | Single-Bit Error |
| 多比特错误 | Multi-Bit Error |
| 错误检测 | Error Detection |
| 错误纠正 | Error Correction |
| 错误检测与纠正 | Error Detection and Correction (EDAC) |
| 纠错码 | Error-Correcting Code (ECC) |
| 海明码 | Hamming Code |
| 单错纠正双错检测 | Single-Error Correction, Double-Error Detection (SECDED) |
| 奇偶校验 | Parity Check |
| 硬件故障 | Hardware Fault |
| 软错误 | Soft Error |
| 位翻转 | Bit Flip |
| 检查点 | Checkpoint |
| 冗余 | Redundancy |
| 锁步执行 | Lockstep Execution |
| 可信执行环境 | Trusted Execution Environment (TEE) |
| 安全启动 | Secure Boot |
| 可信平台模块 | Trusted Platform Module (TPM) |
| 侧信道攻击 | Side-Channel Attack |
| 缓存侧信道 | Cache Side Channel |
| 推测执行漏洞 | Speculative-Execution Vulnerability |
| 熔断漏洞 | Meltdown |
| 幽灵漏洞 | Spectre |
| 存储器保护密钥 | Memory Protection Keys (MPK) |
| 内存标签 | Memory Tagging |
| 硬件虚拟化 | Hardware Virtualization |
| 虚拟机监控器 | Hypervisor |
| 第二级地址转换 | Second-Level Address Translation (SLAT) |
| 嵌套页表 | Nested Page Table (NPT) |
| 扩展页表 | Extended Page Table (EPT) |
| RISC-V 指令集体系结构 | RISC-V Instruction Set Architecture |
| Arm 指令集体系结构 | Arm Architecture |
| x86 指令集体系结构 | x86 Instruction Set Architecture |
| 微代码更新 | Microcode Update |
| 芯片组 | Chipset |
| 现场可编程门阵列 | Field-Programmable Gate Array (FPGA) |
| 专用集成电路 | Application-Specific Integrated Circuit (ASIC) |

## 易混术语辨析

- **计算机体系结构 / 微体系结构**：Architecture 通常关注软件可见的 ISA 等规范；Microarchitecture 是实现 ISA 的内部组织方式。
- **指令集 / 指令集体系结构**：Instruction Set 指令集合；ISA 还包含寄存器、寻址、异常及内存语义等架构契约。
- **寄存器 / 缓存 / 主存**：Register 位于处理器核心的快速存储资源；Cache 利用局部性；Main Memory 通常指 DRAM。
- **字节序 / 位序**：Endianness 主要描述多字节数据在内存中的字节排列，不等同于每字节内部的比特传输顺序。
- **进位 / 溢出**：Carry 常用于无符号运算判断；Overflow Flag 通常用于有符号运算的溢出判断。
- **浮点尾数 / 有效数**：Significand 更精确地指有效数；Mantissa 是常见旧称，严格场合不建议混用。
- **中断 / 异常 / 陷阱**：Interrupt 常由外部异步事件触发；Exception 是处理器执行相关事件的总称；Trap 在不同 ISA / 教材中定义有差异。
- **延迟 / 吞吐量**：Latency 描述一次操作完成耗时；Throughput 描述单位时间的完成数量。
- **RAW / WAR / WAW**：RAW 是真数据相关；WAR 为反相关；WAW 为输出相关，重命名可消除后两种名字相关。
- **发射 / 执行 / 提交**：Issue、Execute、Retire/Commit 是不同阶段；乱序 CPU 可乱序执行但通常按序提交。
- **直接映射 / 全相联 / 组相联**：三者按缓存块可映射到的候选位置不同区分；组相联度是每组的路数。
- **Cache Miss / Page Fault**：Cache Miss 是缓存层级未命中；Page Fault 是地址翻译或页权限等机制触发的异常，不是同一事件。
- **缓存一致性 / 内存一致性模型**：Coherence 关注同一地址的副本关系；Consistency 约束跨地址内存操作的可观察顺序。
- **并发 / 并行**：Concurrency 指多任务进展的组织方式；Parallelism 指物理上同时执行。
- **功耗 / 能耗**：Power 的单位为瓦特 W；Energy 的单位为焦耳 J；降低运行时间不必然降低瞬时功耗。
- **RISC-V / Arm / x86**：它们是不同 ISA 家族；RISC-V 是开放的 ISA 规范，并不特指某一颗处理器。

## 常见缩写速查

| 缩写 | English Full Form | 中文 |
| :--- | :--- | :--- |
| ALU | Arithmetic Logic Unit | 算术逻辑单元 |
| AMAT | Average Memory Access Time | 平均存储器访问时间 |
| AGU | Address Generation Unit | 地址生成单元 |
| BTB | Branch Target Buffer | 分支目标缓冲器 |
| CAS | Compare-and-Swap | 比较并交换 |
| CISC | Complex Instruction Set Computer | 复杂指令集计算机 |
| CPI | Cycles Per Instruction | 每条指令平均周期数 |
| DMA | Direct Memory Access | 直接存储器访问 |
| DRAM | Dynamic RAM | 动态随机访问存储器 |
| ECC | Error-Correcting Code | 纠错码 |
| FMA | Fused Multiply-Add | 融合乘加 |
| FPU | Floating-Point Unit | 浮点运算单元 |
| HBM | High Bandwidth Memory | 高带宽存储器 |
| ILP | Instruction-Level Parallelism | 指令级并行 |
| IPC | Instructions Per Cycle | 每周期指令数 |
| ISA | Instruction Set Architecture | 指令集体系结构 |
| LSQ | Load/Store Queue | 加载存储队列 |
| LRU | Least Recently Used | 最近最少使用 |
| MMIO | Memory-Mapped I/O | 内存映射 I/O |
| MMU | Memory Management Unit | 内存管理单元 |
| MSHR | Miss Status Holding Register | 未完成缺失状态寄存器 |
| NUMA | Non-Uniform Memory Access | 非统一内存访问 |
| OoO | Out-of-Order | 乱序 |
| PC | Program Counter | 程序计数器 |
| PTE | Page Table Entry | 页表项 |
| RISC | Reduced Instruction Set Computer | 精简指令集计算机 |
| ROB | Reorder Buffer | 重排序缓冲区 |
| SIMD | Single Instruction, Multiple Data | 单指令多数据 |
| SMT | Simultaneous Multithreading | 同时多线程 |
| SRAM | Static RAM | 静态随机访问存储器 |
| TLB | Translation Lookaside Buffer | 转换检测缓冲区 |
| VIPT | Virtually Indexed, Physically Tagged | 虚拟索引物理标记 |
| VPN | Virtual Page Number | 虚拟页号 |

---

说明：不同教材、芯片架构手册与行业语境可能采用不同译法；本表以常用译法为主。开放编辑时建议提供权威来源、使用语境和术语差异说明。
