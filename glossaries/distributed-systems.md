# 分布式系统 · Distributed Systems

> 中英双语专业技术术语手册 | Bilingual Technical Glossary

**400 条术语 · 16 章 · 2026-11-27**

覆盖分布式计算模型、网络与 RPC、故障模型、逻辑时钟、CAP 与一致性、复制、Raft/Paxos、事务、分片、分布式计算、消息系统、协调、SRE、安全、性能与形式化验证。中文定义是独立编写的学习用途简释，应结合相关论文的故障模型与适用假设阅读。

**编辑状态：**已完成格式、数量、英文主术语去重、技术边界抽样检查；尚未声称通过独立人类领域专家的逐条审稿。

## 章节目录

- 01. 分布式系统基础与体系结构（25 条）
- 02. 网络通信、RPC 与接口语义（25 条）
- 03. 故障模型与容错基础（25 条）
- 04. 时间、时钟与因果排序（25 条）
- 05. 一致性模型与 CAP 理论（25 条）
- 06. 副本、仲裁与冲突解决（25 条）
- 07. 分布式共识、Paxos 与 Raft（25 条）
- 08. 分布式事务与并发控制（25 条）
- 09. 分片、存储与分布式数据库（25 条）
- 10. 批处理、流处理与分布式计算（25 条）
- 11. 消息队列、事件驱动与日志系统（25 条）
- 12. 成员管理、发现与协调服务（25 条）
- 13. 可靠性工程、韧性与运维（25 条）
- 14. 分布式安全、身份与信任（25 条）
- 15. 性能、容量与资源调度（25 条）
- 16. 分布式测试、验证与形式化方法（25 条）

---

## 01. 分布式系统基础与体系结构

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributed System | 分布式系统 |  | 由多个通过网络通信的计算节点协作、对外提供共同服务的系统。 |
| 2 | Distributed Computing | 分布式计算 |  | 把计算任务安排到多个相互通信的节点执行的技术与研究领域。 |
| 3 | Node | 节点 |  | 参与分布式协议或承载服务的独立计算实体。 |
| 4 | Process | 进程 |  | 运行程序并拥有独立执行状态的操作系统抽象。 |
| 5 | Cluster | 集群 |  | 通过网络组织的一组计算机或服务实例。 |
| 6 | Data Center | 数据中心 |  | 集中承载服务器、网络、供电与存储设施的物理站点。 |
| 7 | Availability Zone | 可用区 |  | 云环境中具有一定故障隔离能力的部署区域，具体边界由提供方定义。 |
| 8 | Region | 区域 |  | 云服务商划定的地理部署范围，通常包括多个可用区。 |
| 9 | Shared-nothing Architecture | 无共享架构 |  | 各节点独立拥有计算和存储资源，通过消息协作。 |
| 10 | Shared-disk Architecture | 共享磁盘架构 |  | 多个计算节点共同访问存储设备的系统设计。 |
| 11 | Client-server Model | 客户端—服务器模型 |  | 客户端发出请求，服务器承担处理与响应的交互模型。 |
| 12 | Peer-to-peer Architecture | 对等网络架构 | P2P | 节点可同时作为服务消费者与提供者的分布式架构。 |
| 13 | Coordinator | 协调者 |  | 为多方操作组织决策、调度或状态推进的参与者。 |
| 14 | Worker | 工作节点 |  | 承担实际数据处理、执行任务或提供计算能力的节点。 |
| 15 | Control Plane | 控制平面 |  | 负责配置、编排、成员与策略决策的组件集合。 |
| 16 | Data Plane | 数据平面 |  | 实际承载用户流量、读写或计算操作的组件集合。 |
| 17 | Service Discovery | 服务发现 |  | 通过注册信息或查询机制找到可用服务实例的过程。 |
| 18 | Service Registry | 服务注册中心 |  | 保存服务实例地址、元数据及健康状态的组件。 |
| 19 | Horizontal Scaling | 水平扩展 |  | 增加同类节点或实例以扩展处理能力。 |
| 20 | Vertical Scaling | 垂直扩展 |  | 提高单节点计算、内存或存储资源的规模。 |
| 21 | Elasticity | 弹性伸缩 |  | 根据负载变化增减资源的能力。 |
| 22 | Location Transparency | 位置透明性 |  | 用户无需知道资源真实网络位置便可访问资源的特性。 |
| 23 | Replication Transparency | 复制透明性 |  | 客户端不必管理服务内部多个副本的抽象。 |
| 24 | Failure Transparency | 故障透明性 |  | 系统在一定故障范围内屏蔽故障细节并维持服务的能力。 |
| 25 | Distributed Middleware | 分布式中间件 |  | 为跨节点通信、协调或数据访问提供通用能力的软件层。 |

## 02. 网络通信、RPC 与接口语义

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Remote Procedure Call | 远程过程调用 | RPC | 将远端服务操作包装成类似本地函数调用的交互机制。 |
| 2 | Remote Method Invocation | 远程方法调用 | RMI | 面向对象环境中对远程对象方法发起调用的机制。 |
| 3 | Request-response Pattern | 请求—响应模式 |  | 由请求方发送请求并等待对应结果的交互方式。 |
| 4 | Message Passing | 消息传递 |  | 节点通过发送与接收消息交换数据或协调状态的通信模型。 |
| 5 | Synchronous Communication | 同步通信 |  | 发送方与接收方按特定时序阻塞或协同完成交互的模式。 |
| 6 | Asynchronous Communication | 异步通信 |  | 交互发起后不要求调用方持续阻塞等待完成的模式。 |
| 7 | Unary RPC | 一元 RPC |  | 每次调用只发送一个请求并接收一个响应的 RPC 形态。 |
| 8 | Streaming RPC | 流式 RPC |  | 一次调用中持续交换多个消息的远程通信方式。 |
| 9 | Serialization | 序列化 |  | 将结构化对象转换为可传输或存储的字节表示。 |
| 10 | Deserialization | 反序列化 |  | 将编码后的数据还原为程序可处理的结构。 |
| 11 | Wire Protocol | 线协议 |  | 规定网络消息的字节布局、字段编码与交互规则的协议。 |
| 12 | Interface Definition Language | 接口定义语言 | IDL | 以独立于实现语言的方式声明跨系统服务接口。 |
| 13 | Protocol Buffers | 协议缓冲区 | Protobuf | 使用模式定义消息并提供紧凑二进制编码的序列化技术。 |
| 14 | gRPC | gRPC 远程调用框架 | gRPC | 常基于 HTTP/2 与 Protobuf 提供多语言 RPC 的框架。 |
| 15 | HTTP/2 Multiplexing | HTTP/2 多路复用 |  | 允许多个逻辑流在同一连接上交错传输数据帧的能力。 |
| 16 | Connection Pooling | 连接池 |  | 复用已建立的网络连接以降低连接创建成本的机制。 |
| 17 | Keepalive | 保活机制 |  | 发送心跳或探测以维持连接或识别不可用对端的机制。 |
| 18 | Request Timeout | 请求超时 |  | 请求在规定时间内未完成时终止等待的控制策略。 |
| 19 | Deadline Propagation | 截止时间传播 |  | 跨多层服务传递剩余执行预算，避免下游无界等待。 |
| 20 | Retry Policy | 重试策略 |  | 指定失败后是否重发请求、重试次数及间隔的规则。 |
| 21 | Exponential Backoff | 指数退避 |  | 使连续重试间隔按指数增长以降低拥塞风险的机制。 |
| 22 | Retry Jitter | 重试随机抖动 |  | 在退避间隔中加入随机变化以避免大量客户端同步重试。 |
| 23 | Idempotent Request | 幂等请求 |  | 重复执行同一请求不会产生额外业务效果的请求语义。 |
| 24 | Request Identifier | 请求标识符 |  | 用于关联调用、重试和去重的唯一或范围内唯一标记。 |
| 25 | Duplicate Suppression | 重复请求抑制 |  | 根据请求标识或业务键避免重试导致重复执行的机制。 |

## 03. 故障模型与容错基础

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Fault | 故障根因 |  | 造成组件偏离预期行为的缺陷、条件或外部扰动。 |
| 2 | Error State | 错误状态 |  | 系统内部状态与正确状态发生偏离的情形。 |
| 3 | Failure | 服务失效 |  | 系统对外行为不再满足规定服务契约的情况。 |
| 4 | Crash Failure | 崩溃故障 |  | 节点停止执行或响应，但不继续发送任意错误消息的故障模型。 |
| 5 | Crash-stop Model | 停止崩溃模型 |  | 节点一旦崩溃便不会在同一执行中恢复的模型。 |
| 6 | Crash-recovery Model | 崩溃恢复模型 |  | 节点可能停止并重启，但部分持久状态可保留的模型。 |
| 7 | Omission Failure | 遗漏故障 |  | 应当发送或接收的消息被漏掉的故障。 |
| 8 | Timing Failure | 时序故障 |  | 节点或通信的响应时间超出模型允许边界的故障。 |
| 9 | Byzantine Failure | 拜占庭故障 |  | 节点可能任意偏离协议甚至向不同参与者发送矛盾信息的故障模型。 |
| 10 | Network Partition | 网络分区 |  | 节点群之间通信长期或暂时不可达、但局部节点仍可能运行的情况。 |
| 11 | Partial Failure | 局部故障 |  | 系统部分组件失效而其他部分继续工作的现象。 |
| 12 | Fail-stop Assumption | 可检测停止假设 |  | 故障节点停止且其失败可被可靠识别的理想化模型假设。 |
| 13 | Failover | 故障切换 |  | 将流量或主职责从失效实例转移到可用实例的过程。 |
| 14 | Failback | 故障回切 |  | 原故障资源恢复后将职责或负载迁回的过程。 |
| 15 | Redundancy | 冗余 |  | 部署额外组件或数据副本以抵抗故障的设计策略。 |
| 16 | Fault Tolerance | 容错 |  | 组件发生限定类型故障时仍能维持规定正确性或服务目标的能力。 |
| 17 | Fault Isolation | 故障隔离 |  | 限制故障影响范围以阻止错误传播的措施。 |
| 18 | Blast Radius | 故障影响半径 |  | 一个故障可能波及的用户、组件或业务范围。 |
| 19 | Single Point of Failure | 单点故障 | SPOF | 一个组件失效便足以导致整体关键能力不可用的依赖点。 |
| 20 | Failure Domain | 故障域 |  | 共享某类失效风险的一组资源或节点。 |
| 21 | Graceful Degradation | 优雅降级 |  | 资源不足或故障时保留核心功能并主动降低部分质量的策略。 |
| 22 | Self-healing | 自愈 |  | 自动检测失效并重启、迁移或替换异常组件的能力。 |
| 23 | Split Brain | 脑裂 |  | 原应唯一的协调者或主节点在不同分区中同时对外自认有效的情况。 |
| 24 | Fencing | 隔离屏障 |  | 阻止旧持有者或失效主节点继续访问共享资源的技术。 |
| 25 | Fencing Token | 隔离令牌 |  | 单调递增的访问世代编号，用于拒绝过期持有者的操作。 |

## 04. 时间、时钟与因果排序

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Physical Clock | 物理时钟 |  | 尝试表示现实时间的计算机时钟。 |
| 2 | Wall Clock | 墙上时钟 |  | 提供日期时间读数、可能因校时而跳变的时钟。 |
| 3 | Monotonic Clock | 单调时钟 |  | 用于测量时间间隔且不会因墙上时钟调整而倒退的计时源。 |
| 4 | Clock Skew | 时钟偏差 |  | 不同节点时钟在同一真实时刻的读数差异。 |
| 5 | Clock Drift | 时钟漂移 |  | 时钟相对于参考时间的速率偏差随时间积累的现象。 |
| 6 | Clock Synchronization | 时钟同步 |  | 通过协议减小不同节点时钟读数误差的过程。 |
| 7 | Network Time Protocol | 网络时间协议 | NTP | 通过网络估算时钟偏差与往返延迟的时间同步协议。 |
| 8 | Precision Time Protocol | 精确时间协议 | PTP | 利用网络硬件时间戳等机制进行高精度时钟同步的协议。 |
| 9 | Happens-before Relation | 先发生关系 |  | 由进程内顺序与消息发送接收关系传递闭包定义的因果偏序。 |
| 10 | Concurrent Events | 并发事件 |  | 在先发生关系下互不为因果先后的两个事件。 |
| 11 | Lamport Clock | Lamport 逻辑时钟 |  | 给事件分配满足因果先后蕴含时间戳递增的逻辑计数器。 |
| 12 | Logical Timestamp | 逻辑时间戳 |  | 用于表示事件顺序而非精确现实时间的标记。 |
| 13 | Vector Clock | 向量时钟 |  | 用多维计数器在固定进程集合中刻画事件因果偏序的机制。 |
| 14 | Version Vector | 版本向量 |  | 利用每副本计数表示数据版本因果关系的向量。 |
| 15 | Dotted Version Vector | 点式版本向量 |  | 以版本向量与单个事件标记精确表示更新因果上下文。 |
| 16 | Hybrid Logical Clock | 混合逻辑时钟 | HLC | 结合物理时间近似值与逻辑计数保持可比较事件顺序的时钟。 |
| 17 | TrueTime | TrueTime 时间 API |  | 以包含真实时间的误差区间表示时间估计的接口设计。 |
| 18 | Clock Uncertainty | 时钟不确定性 |  | 时钟读数与真实时间之间可能误差的界限。 |
| 19 | Commit Wait | 提交等待 |  | 提交操作等待时间不确定性窗口过去以确保特定外部顺序性质的机制。 |
| 20 | Global Snapshot | 全局快照 |  | 描述多节点局部状态与在途消息的一致系统截面。 |
| 21 | Consistent Cut | 一致切面 |  | 若截面包含某事件则也包含其所有因果前驱的事件集合。 |
| 22 | Chandy–Lamport Snapshot | Chandy–Lamport 快照算法 |  | 通过标记消息记录异步系统一致全局状态的算法。 |
| 23 | Causal Order | 因果顺序 |  | 要求按先发生关系保持消息或操作的先后处理次序。 |
| 24 | Total Order | 全序 |  | 任意两事件均可比较且满足传递性的顺序关系。 |
| 25 | Total-order Broadcast | 全序广播 |  | 让所有正确参与者按相同顺序交付同一组消息的广播抽象。 |

## 05. 一致性模型与 CAP 理论

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Consistency Model | 一致性模型 |  | 对并发读写历史允许出现哪些可观察结果的形式化约束。 |
| 2 | Linearizability | 线性一致性 |  | 每个操作可视为在调用与响应之间的瞬间生效，并遵守真实时间先后关系。 |
| 3 | Sequential Consistency | 顺序一致性 |  | 存在保留每个进程程序次序的全局串行执行，但不要求符合真实时间次序。 |
| 4 | Strict Serializability | 严格可串行化 |  | 事务执行等价于某串行次序且遵守无重叠事务的真实时间先后。 |
| 5 | Serializability | 可串行化 |  | 并发事务结果等价于某个合法串行事务执行。 |
| 6 | Snapshot Isolation | 快照隔离 | SI | 事务读取一致快照并通常阻止并发写同一项，却可能发生写偏斜。 |
| 7 | Read Committed | 读已提交 | RC | 每次读取不返回其他事务尚未提交的值的常见隔离级别。 |
| 8 | Repeatable Read | 可重复读 |  | 事务内重复读取相同行时不受其他已提交修改影响的隔离语义，具体实现有差异。 |
| 9 | Eventual Consistency | 最终一致性 |  | 在停止新更新且通信恢复后，副本最终收敛到相同可观察值的性质。 |
| 10 | Strong Consistency | 强一致性 |  | 泛指较强读取保证的非精确术语，须明确具体模型才可验证。 |
| 11 | Causal Consistency | 因果一致性 |  | 所有观察者须按因果先后关系感知相关操作更新。 |
| 12 | Causal+ Consistency | 因果加一致性 |  | 在因果一致性基础上通常包含收敛等附加要求的一类模型。 |
| 13 | PRAM Consistency | PRAM 一致性 |  | 所有进程都以发送者程序顺序观察该发送者的写入。 |
| 14 | FIFO Consistency | FIFO 一致性 |  | 同一进程发出的写入按其发送顺序被其他参与者看到的模型。 |
| 15 | Read-your-writes Consistency | 读己之写一致性 |  | 会话中后续读取至少看见该会话先前成功写入的效果。 |
| 16 | Monotonic Reads | 单调读 |  | 同一会话后续读取不会看到早于其已观察版本的状态。 |
| 17 | Monotonic Writes | 单调写 |  | 同一会话发出的写入在系统中保持先后次序。 |
| 18 | Writes-follow-reads | 写遵循读 |  | 会话后续写入在因果上排在该会话已观察读取对应版本之后。 |
| 19 | Session Consistency | 会话一致性 |  | 在客户端会话范围内提供读己之写等顺序性质的保证。 |
| 20 | Stale Read | 陈旧读取 |  | 读取返回落后于某些已完成更新的旧版本。 |
| 21 | Read Repair | 读修复 |  | 读请求发现副本不一致时将较新状态写回落后副本的机制。 |
| 22 | CAP Theorem | CAP 定理 |  | 发生网络分区时，具有线性一致性的读写服务不能同时保证所有请求都成功响应。 |
| 23 | Partition Tolerance | 分区容忍性 |  | 系统在部分节点间网络不可达时仍按指定性质工作的能力。 |
| 24 | Availability in CAP | CAP 可用性 |  | 每个非故障节点收到的请求最终获得响应，不保证响应内容一定是最新值。 |
| 25 | PACELC Model | PACELC 模型 |  | 讨论分区时可用性与一致性的取舍，并讨论正常情况下延迟与一致性的权衡。 |

## 06. 副本、仲裁与冲突解决

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Replication | 数据复制 |  | 在多个节点保存或传播相同逻辑数据以提升可用性或读吞吐。 |
| 2 | Replica | 副本 |  | 在某节点维护的数据或状态机拷贝。 |
| 3 | Replication Factor | 复制因子 |  | 为一份逻辑数据配置的副本数量。 |
| 4 | Leader-based Replication | 基于主节点的复制 |  | 由主节点负责接受写入并向追随者传播的复制方式。 |
| 5 | Leaderless Replication | 无主复制 |  | 客户端可将读写请求发送到多个副本并按策略汇聚结果。 |
| 6 | Multi-leader Replication | 多主复制 |  | 允许多个节点接受写入并处理跨主节点传播与冲突的模式。 |
| 7 | Synchronous Replication | 同步复制 |  | 在操作成功前等待约定数量的远端副本确认。 |
| 8 | Asynchronous Replication | 异步复制 |  | 主节点可先确认写入，再向其他副本传播更新。 |
| 9 | Semi-synchronous Replication | 半同步复制 |  | 等待部分副本满足确认条件、其余副本异步追赶的复制策略。 |
| 10 | Replication Lag | 复制延迟 |  | 源副本产生更新与目标副本应用更新之间的时差或日志差距。 |
| 11 | Replica Catch-up | 副本追赶 |  | 落后副本读取缺失日志或快照直至赶上目标进度。 |
| 12 | Anti-entropy | 反熵同步 |  | 副本通过周期性比较与交换状态减少分歧的机制。 |
| 13 | Merkle Tree | 默克尔树 |  | 利用分层哈希摘要高效比较大型数据集合差异的树结构。 |
| 14 | Quorum | 仲裁集合 |  | 满足协议决策所需成员数量及交集要求的节点集合。 |
| 15 | Majority Quorum | 多数派仲裁 |  | 包含严格超过半数投票成员的仲裁集合。 |
| 16 | Read Quorum | 读仲裁 |  | 读取时需收集足够多副本结果的集合要求。 |
| 17 | Write Quorum | 写仲裁 |  | 写入时需取得足够多副本确认的集合要求。 |
| 18 | Quorum Intersection | 仲裁交集 |  | 不同仲裁集合之间共享成员，以支持一致性证明的条件。 |
| 19 | Sloppy Quorum | 宽松仲裁 |  | 首选副本不可用时允许临时向其他节点写入的策略。 |
| 20 | Hinted Handoff | 提示移交 |  | 临时承接数据的节点在目标副本恢复后将更新转交回去的机制。 |
| 21 | Conflict Resolution | 冲突解决 |  | 对并发产生的不兼容版本选择、合并或人工处理的过程。 |
| 22 | Last-write-wins | 最后写入胜出 | LWW | 按照某种时间戳或版本顺序保留一个获胜值的规则。 |
| 23 | Multi-value Register | 多值寄存器 | MV-register | 保留多个因果并发写入值的复制数据类型。 |
| 24 | Read-modify-write | 读取—修改—写入 |  | 先读取旧状态、计算新状态再写回的操作组合。 |
| 25 | Replica Divergence | 副本分歧 |  | 同一逻辑数据在多个副本上出现不一致状态的现象。 |

## 07. 分布式共识、Paxos 与 Raft

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributed Consensus | 分布式共识 |  | 节点在规定故障模型下就同一决策值达成一致的任务。 |
| 2 | Agreement Property | 一致性性质 |  | 任意两个已决定的正确节点不会决定不同值。 |
| 3 | Validity Property | 有效性性质 |  | 共识决策值满足协议规定的输入或提议约束。 |
| 4 | Termination Property | 终止性性质 |  | 在规定网络与故障条件下正确参与者最终作出决定。 |
| 5 | Safety Property | 安全性性质 |  | 系统始终不进入协议禁止状态的性质。 |
| 6 | Liveness Property | 活性性质 |  | 满足约定公平性与环境假设时有益事件最终会发生的性质。 |
| 7 | FLP Impossibility | FLP 不可能性 |  | 完全异步网络下，允许一个崩溃进程时不存在保证总终止的确定性共识算法。 |
| 8 | Paxos | Paxos 共识算法 |  | 通过准备、接受阶段及交叉多数派保证决策安全性的协议族。 |
| 9 | Proposer | 提议者 |  | 在 Paxos 中发起带编号提案并尝试使其被接受的角色。 |
| 10 | Acceptor | 接受者 |  | 在 Paxos 中依据承诺规则接受或拒绝提案的角色。 |
| 11 | Learner | 学习者 |  | 在 Paxos 中获知已被选定决策值的参与者角色。 |
| 12 | Ballot Number | 选票编号 |  | 用于区分共识提议轮次并确定新旧优先关系的编号。 |
| 13 | Prepare Phase | 准备阶段 |  | Paxos 提议者获取接受者承诺及已接受值信息的阶段。 |
| 14 | Accept Phase | 接受阶段 |  | Paxos 提议者请求接受者接受选定提案的阶段。 |
| 15 | Multi-Paxos | Multi-Paxos |  | 通过稳定领导者优化连续多个日志槽位共识的 Paxos 方案。 |
| 16 | Raft | Raft 共识算法 |  | 基于领导者、任期与复制日志管理状态机复制的共识协议。 |
| 17 | Leader Election | 领导者选举 |  | 从候选节点中确定当前承担主职责节点的过程。 |
| 18 | Term Number | 任期编号 |  | Raft 中标识相继选举时期的单调递增编号。 |
| 19 | AppendEntries RPC | 追加日志 RPC |  | Raft 主节点用于复制日志及发送心跳的远程调用。 |
| 20 | RequestVote RPC | 请求投票 RPC |  | Raft 候选节点请求其他成员支持其竞选的调用。 |
| 21 | Log Matching Property | 日志匹配性质 |  | Raft 中同位置同任期条目相同意味着此前日志前缀相同。 |
| 22 | Commit Index | 提交索引 |  | 已确认满足协议提交规则的日志最高索引。 |
| 23 | Leader Completeness | 领导者完整性 |  | 已提交日志条目必须出现在后续任期领导者日志中的性质。 |
| 24 | Joint Consensus | 联合共识 |  | Raft 成员变更中让新旧配置投票规则在过渡期共同生效的方式。 |
| 25 | Replicated State Machine | 复制状态机 | RSM | 各副本以同一确定顺序执行命令以维护一致状态的架构。 |

## 08. 分布式事务与并发控制

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributed Transaction | 分布式事务 |  | 同时跨多个节点、分片或资源维护约定原子性与隔离语义的事务。 |
| 2 | Atomicity | 原子性 |  | 事务内部操作要么共同生效要么共同撤销的性质。 |
| 3 | Consistency Constraint | 一致性约束 |  | 数据库状态必须满足的业务或数据完整性规则。 |
| 4 | Isolation | 隔离性 |  | 事务并发执行对彼此观察结果施加的规则。 |
| 5 | Durability | 持久性 |  | 提交确认后变更在约定故障条件下不丢失的性质。 |
| 6 | Two-phase Commit | 两阶段提交 | 2PC | 协调者先收集参与者准备结果再统一发布提交或回滚决议的协议。 |
| 7 | Prepare-to-commit | 准备提交 |  | 事务参与者持久记录待决状态并表态能否提交的阶段。 |
| 8 | Commit Decision | 提交决议 |  | 协调者选择提交或中止事务的最终决定。 |
| 9 | Coordinator Blocking | 协调者阻塞 |  | 2PC 参与者在无法获知最终决议时可能长期等待的现象。 |
| 10 | Three-phase Commit | 三阶段提交 | 3PC | 引入额外阶段以在较强故障与时间假设下减少阻塞的协议。 |
| 11 | Saga Pattern | Saga 模式 |  | 把长事务拆为本地事务和补偿操作的业务协调方式。 |
| 12 | Compensating Transaction | 补偿事务 |  | 通过新操作抵消先前已提交业务动作影响的事务。 |
| 13 | Try-confirm-cancel | 尝试—确认—取消 | TCC | 业务方显式提供预留、确认与取消接口的分布式事务模式。 |
| 14 | Outbox Pattern | 事务发件箱模式 |  | 在同一本地事务内写业务数据与待发消息，再异步发布消息的模式。 |
| 15 | Inbox Pattern | 事务收件箱模式 |  | 在消费端记录已处理消息以避免重复执行业务副作用的模式。 |
| 16 | Two-phase Locking | 两阶段锁协议 | 2PL | 事务先增长锁集合再释放锁、释放后不再获取新锁的并发控制规则。 |
| 17 | Strict Two-phase Locking | 严格两阶段锁 | S2PL | 事务持有排他锁直到提交或中止的两阶段锁变体。 |
| 18 | Optimistic Concurrency Control | 乐观并发控制 | OCC | 先并行执行、提交时验证冲突并决定是否重试的策略。 |
| 19 | Multiversion Concurrency Control | 多版本并发控制 | MVCC | 维护多个已提交数据版本，使读写在不同快照上进行的机制。 |
| 20 | Write Skew | 写偏斜 |  | 并发事务分别基于同一快照读取约束后修改不同对象，合并结果破坏约束。 |
| 21 | Lost Update | 丢失更新 |  | 两个事务基于同一旧值更新，后写结果覆盖了先写效果的异常。 |
| 22 | Dirty Read | 脏读 |  | 事务读取其他事务尚未提交的数据。 |
| 23 | Phantom Read | 幻读 |  | 相同条件的两次查询因并发插入删除出现不同结果集合。 |
| 24 | Deadlock Detection | 死锁检测 |  | 检查等待图等结构识别循环等待的机制。 |
| 25 | Distributed Deadlock | 分布式死锁 |  | 跨节点锁或资源等待形成闭环而无法继续推进的状态。 |

## 09. 分片、存储与分布式数据库

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Partitioning | 数据分区 |  | 把数据集按规则拆分成可独立管理的多个部分。 |
| 2 | Sharding | 数据库分片 |  | 将逻辑数据库数据分散存储到多个物理分片的机制。 |
| 3 | Shard | 分片 |  | 分布式数据集中按路由规则管理的一部分数据。 |
| 4 | Partition Key | 分区键 |  | 确定记录应归属哪个分片的字段或字段组合。 |
| 5 | Hash Partitioning | 哈希分区 |  | 使用分区键哈希值把记录映射到目标分片的策略。 |
| 6 | Range Partitioning | 范围分区 |  | 按键值区间划分并分布数据的方法。 |
| 7 | Consistent Hashing | 一致性哈希 |  | 将键与节点映射到环形空间，减少成员变化时迁移数据量的技术。 |
| 8 | Virtual Node | 虚拟节点 |  | 在哈希环中为物理节点设置多个逻辑位置以改善负载分布。 |
| 9 | Rendezvous Hashing | 最高随机权重哈希 | HRW | 为每个键计算候选节点得分并选择得分最高节点的映射方法。 |
| 10 | Hot Partition | 热点分区 |  | 承载不成比例请求量或数据流量的分区。 |
| 11 | Hot Key | 热点键 |  | 被大量重复访问、容易导致单节点负载集中的键。 |
| 12 | Rebalancing | 重平衡 |  | 将分片或任务从高负载节点迁移到低负载节点的过程。 |
| 13 | Resharding | 重新分片 |  | 根据容量或访问特征调整数据分片数量及边界。 |
| 14 | Scatter-gather Query | 散射—收集查询 |  | 把查询发送到多个分片再合并各节点结果的处理方式。 |
| 15 | Secondary Index | 二级索引 |  | 按非主键字段建立的检索结构，在分片环境下可能本地或全局维护。 |
| 16 | Global Secondary Index | 全局二级索引 | GSI | 跨多个数据分片提供非主键检索能力的索引结构。 |
| 17 | Distributed Key-value Store | 分布式键值存储 |  | 在多节点保存键值数据并提供基于键访问接口的系统。 |
| 18 | Log-structured Merge Tree | 日志结构合并树 | LSM Tree | 通过内存结构、顺序写和分层合并优化写入的存储引擎结构。 |
| 19 | Write-ahead Log | 预写日志 | WAL | 在更新数据页或状态前先持久记录变更的恢复日志。 |
| 20 | Immutable SSTable | 不可变有序字符串表 | SSTable | LSM 存储中按键排序且落盘后不原位修改的文件。 |
| 21 | Compaction | 存储压实 |  | 合并有序文件、删除过期版本并整理数据布局的过程。 |
| 22 | Tombstone | 墓碑标记 |  | 代表逻辑删除、供复制和压实处理的删除记录。 |
| 23 | Distributed File System | 分布式文件系统 | DFS | 将文件块及元数据分布在多个服务器并提供统一文件接口的系统。 |
| 24 | Object Storage | 对象存储 |  | 用对象键与元数据管理非结构化数据并通过服务 API 访问的存储方式。 |
| 25 | Erasure Coding | 纠删码 |  | 将数据编码为含冗余的分片，以少于全部分片重建原数据的容错技术。 |

## 10. 批处理、流处理与分布式计算

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | MapReduce | MapReduce 编程模型 |  | 将任务组织为 Map 产生键值对、Shuffle 分组和 Reduce 聚合的分布式批处理模型。 |
| 2 | Map Function | 映射函数 |  | 把一条输入记录转换为零个或多个中间键值对的处理步骤。 |
| 3 | Reduce Function | 归约函数 |  | 对同键的中间结果进行聚合的处理步骤。 |
| 4 | Shuffle | 数据洗牌 |  | 根据键或分区规则跨工作节点传输并重新分组数据的过程。 |
| 5 | Combiner | 本地合并器 |  | 在数据洗牌前对可安全组合的中间结果执行局部聚合的优化。 |
| 6 | Data Parallelism | 数据并行 |  | 把同一操作应用于不同数据分区的并行执行方式。 |
| 7 | Task Parallelism | 任务并行 |  | 把相互独立或可并发的不同计算任务分配至多个工作节点。 |
| 8 | Directed Acyclic Graph Execution | 有向无环图执行 | DAG | 以无环依赖图描述任务执行顺序和数据流的调度方式。 |
| 9 | Execution Stage | 执行阶段 |  | 具有共同调度或数据依赖边界的一组计算任务。 |
| 10 | Task Scheduler | 任务调度器 |  | 将计算任务映射到工作节点并管理资源与重试的组件。 |
| 11 | Work Stealing | 工作窃取 |  | 空闲工作线程或节点从繁忙执行者队列获取待处理任务的策略。 |
| 12 | Speculative Execution | 推测执行 |  | 为缓慢任务启动冗余副本、优先采用先完成结果的策略。 |
| 13 | Straggler | 拖尾任务 |  | 显著慢于同批其他任务、延迟整体作业完成的任务。 |
| 14 | Checkpointing | 检查点 |  | 周期性持久化计算状态以便故障后恢复或重算的机制。 |
| 15 | Stateful Stream Processing | 有状态流处理 |  | 在连续事件上维护跨记录累计状态的流计算模式。 |
| 16 | Stateless Stream Processing | 无状态流处理 |  | 每条输入可独立处理而无需跨事件保存业务状态的模式。 |
| 17 | Event Time | 事件时间 |  | 事件在数据源实际发生的时间，而非被系统接收处理的时间。 |
| 18 | Processing Time | 处理时间 |  | 算子所在计算系统处理事件时的本地时间。 |
| 19 | Ingestion Time | 摄入时间 |  | 记录进入流处理系统的时间。 |
| 20 | Watermark | 水位线 |  | 对事件时间进度的估计，用于触发窗口计算并管理迟到数据。 |
| 21 | Tumbling Window | 滚动窗口 |  | 时间范围不重叠、按固定时长切分的窗口。 |
| 22 | Sliding Window | 滑动窗口 |  | 按固定步长移动且可能互相重叠的时间窗口。 |
| 23 | Session Window | 会话窗口 |  | 根据事件间空闲时间间隔划定的动态长度窗口。 |
| 24 | Late-arriving Data | 迟到数据 |  | 事件时间早于当前水位线或窗口关账点才到达的数据。 |
| 25 | Exactly-once State Processing | 状态恰好一次处理 |  | 在特定故障与恢复条件下确保状态更新效果不会因重放重复生效的处理保证。 |

## 11. 消息队列、事件驱动与日志系统

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Message Queue | 消息队列 |  | 用于缓存消息并解耦生产者与消费者的通信设施。 |
| 2 | Message Broker | 消息代理 |  | 负责接收、路由、暂存并转发消息的服务组件。 |
| 3 | Producer | 生产者 |  | 向消息系统发布记录或事件的应用角色。 |
| 4 | Consumer | 消费者 |  | 从消息系统读取并处理记录或事件的应用角色。 |
| 5 | Publish-subscribe Pattern | 发布—订阅模式 | Pub/Sub | 发布者按主题发送消息、订阅者接收相关消息的模式。 |
| 6 | Topic | 主题 |  | 对消息进行逻辑分类并承载发布订阅关系的标识。 |
| 7 | Partitioned Log | 分区日志 |  | 把顺序追加记录拆分为多个独立有序分区的日志结构。 |
| 8 | Offset | 偏移量 |  | 记录在特定日志分区中的位置标识。 |
| 9 | Consumer Group | 消费者组 |  | 多个消费者协调分配分区以共同处理消息的逻辑组。 |
| 10 | Consumer Lag | 消费积压 |  | 消费者已处理位置落后于日志最新位置的差额。 |
| 11 | At-most-once Delivery | 至多一次投递 |  | 消息不会被重复投递，但在故障时可能丢失的投递保证。 |
| 12 | At-least-once Delivery | 至少一次投递 |  | 在规定条件下确保消息最终被投递，但可能发生重复投递。 |
| 13 | Exactly-once Delivery | 恰好一次投递 |  | 对限定系统边界承诺每条消息的可观察交付效果恰好一次，须明确实现假设。 |
| 14 | Message Acknowledgment | 消息确认 | ACK | 消费者或接收端表明消息已收到或处理完成的信号。 |
| 15 | Negative Acknowledgment | 否定确认 | NACK | 接收端表明当前无法成功接受或处理消息的信号。 |
| 16 | Dead-letter Queue | 死信队列 | DLQ | 保存超过重试上限或无法正常处理消息的隔离队列。 |
| 17 | Poison Message | 毒消息 |  | 反复触发消费异常且不能靠普通重试解决的特定消息。 |
| 18 | Backpressure | 背压 |  | 下游消费能力不足时向上游限制生产速率或缓冲规模的机制。 |
| 19 | Event-driven Architecture | 事件驱动架构 | EDA | 组件通过发布与响应事件进行松耦合协作的架构。 |
| 20 | Event Sourcing | 事件溯源 |  | 以不可变业务事件序列为主要状态来源，并通过重放推导当前状态的设计。 |
| 21 | Command Query Responsibility Segregation | 命令查询职责分离 | CQRS | 将写入命令模型与读取查询模型分离以分别优化的架构模式。 |
| 22 | Transactional Messaging | 事务消息 |  | 协调本地状态变更与消息发布，以减少两者不一致的机制。 |
| 23 | Log Compaction | 日志压缩保留 |  | 按键保留较新记录、减少旧版本并控制日志存储的清理策略。 |
| 24 | Message Ordering | 消息有序性 |  | 系统对消息交付与消费顺序提供的保证，通常限于特定分区或键。 |
| 25 | Replay | 消息重放 |  | 重新读取历史日志记录以恢复状态、修复数据或重新计算的过程。 |

## 12. 成员管理、发现与协调服务

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Group Membership | 组成员关系 |  | 记录哪些节点属于特定服务组及其成员状态的机制。 |
| 2 | Membership View | 成员视图 |  | 某节点当前认可的参与者集合与版本信息。 |
| 3 | Failure Detector | 故障检测器 |  | 根据超时或探测输出节点可疑或可达判断的协议抽象。 |
| 4 | Perfect Failure Detector | 完美故障检测器 |  | 既不错误怀疑正确节点，又最终检测所有崩溃节点的理想化故障检测器。 |
| 5 | Eventually Perfect Failure Detector | 最终完美故障检测器 |  | 允许早期误判，但某时刻之后不再误判并检测故障的抽象。 |
| 6 | Heartbeat | 心跳 |  | 节点周期性发送以展示自身存活或可达性的轻量消息。 |
| 7 | Gossip Protocol | 流言协议 |  | 通过节点间周期性随机交换信息传播状态的协议族。 |
| 8 | SWIM Protocol | SWIM 成员协议 | SWIM | 通过直接及间接探测实现可扩展弱一致成员管理的协议。 |
| 9 | Phi Accrual Failure Detector | Phi 累积故障检测器 | φ | 根据心跳到达统计分布输出故障可疑程度的检测机制。 |
| 10 | Lease | 租约 |  | 赋予某方在限定时间内持有某项职责或资源访问权的协议。 |
| 11 | Distributed Lock | 分布式锁 |  | 跨节点协调同一逻辑资源互斥访问的机制。 |
| 12 | Lock Expiration | 锁过期 |  | 租约或锁在限定时间后不再有效的状态转移。 |
| 13 | Leader Lease | 领导者租约 |  | 授予某节点一段时间内履行主职责的权利并约束旧主操作。 |
| 14 | Ephemeral Node | 临时节点 |  | 与会话绑定、会话失效后自动删除的协调服务数据节点。 |
| 15 | Watch Notification | 观察通知 |  | 协调服务对已注册数据或成员变更发出的事件提示。 |
| 16 | ZooKeeper | ZooKeeper 协调服务 |  | 提供分层命名、顺序更新及观察机制的分布式协调系统。 |
| 17 | etcd | etcd 键值协调服务 |  | 基于 Raft 提供强一致键值操作的分布式协调存储。 |
| 18 | Consul | Consul 服务发现系统 |  | 提供服务注册、健康检查及协调等功能的基础设施软件。 |
| 19 | Service Mesh | 服务网格 |  | 将服务间流量管理、身份与策略能力放入基础设施层的架构。 |
| 20 | Sidecar Proxy | 边车代理 |  | 与应用实例共同部署、代理其网络通信的辅助进程。 |
| 21 | DNS-based Discovery | 基于 DNS 的服务发现 |  | 用 DNS 查询将逻辑服务名解析为当前实例地址的方式。 |
| 22 | Health Check | 健康检查 |  | 通过主动请求或被动信号判断实例能否正常服务的探测机制。 |
| 23 | Leader Lock | 领导者锁 |  | 依赖共享锁或租约协调唯一领导者身份的做法。 |
| 24 | Membership Churn | 成员抖动 |  | 节点频繁加入、退出或被误判造成成员集合不断变化的现象。 |
| 25 | Configuration Epoch | 配置世代 |  | 用于识别集群配置版本并拒绝旧配置操作的单调版本标识。 |

## 13. 可靠性工程、韧性与运维

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Reliability | 可靠性 |  | 系统在规定环境和时间范围内持续提供正确服务的能力。 |
| 2 | Availability | 可用性 |  | 服务在某段观察时间内能够响应有效请求的程度。 |
| 3 | Service Level Indicator | 服务等级指标 | SLI | 用于量化用户感知服务质量的具体测量指标。 |
| 4 | Service Level Objective | 服务等级目标 | SLO | 对某个 SLI 在统计窗口内规定的目标范围。 |
| 5 | Service Level Agreement | 服务等级协议 | SLA | 服务提供方与客户约定的可用性、性能及责任条款。 |
| 6 | Error Budget | 错误预算 |  | 由 SLO 允许的失败比例或故障时间推导的可消耗额度。 |
| 7 | Mean Time to Recovery | 平均恢复时间 | MTTR | 故障后恢复服务所需时间的统计均值。 |
| 8 | Mean Time Between Failures | 平均故障间隔 | MTBF | 连续两次失效之间正常工作时间的统计均值。 |
| 9 | Recovery Time Objective | 恢复时间目标 | RTO | 业务要求灾难发生后恢复服务所容许的最长时间。 |
| 10 | Recovery Point Objective | 恢复点目标 | RPO | 业务容许灾难恢复后最多丢失多长时间内数据的目标。 |
| 11 | High Availability | 高可用 | HA | 通过冗余、检测与切换降低关键服务停机时间的设计。 |
| 12 | Disaster Recovery | 灾难恢复 | DR | 发生严重故障后恢复业务系统与数据能力的计划和操作。 |
| 13 | Active-active Deployment | 双活部署 |  | 多个站点或实例同时承载生产业务流量的部署模式。 |
| 14 | Active-passive Deployment | 主备部署 |  | 主节点服务、备用节点通常待命并在故障时接管的模式。 |
| 15 | Health-based Routing | 基于健康状态的路由 |  | 根据后端健康检测结果选择流量目标的策略。 |
| 16 | Circuit Breaker | 熔断器 |  | 错误或超时达到阈值时暂时阻断对不健康依赖调用的机制。 |
| 17 | Bulkhead Isolation | 舱壁隔离 |  | 将线程池、连接池或资源划分独立配额以阻断故障连锁反应。 |
| 18 | Rate Limiting | 速率限制 |  | 控制单位时间允许请求量或操作频率的机制。 |
| 19 | Load Shedding | 负载卸载 |  | 系统过载时主动拒绝部分请求以保护关键服务的策略。 |
| 20 | Hedged Requests | 对冲请求 |  | 对慢请求延迟发起冗余请求以减少尾部延迟的技术。 |
| 21 | Chaos Engineering | 混沌工程 |  | 在受控环境主动注入故障以检验系统韧性的工程实践。 |
| 22 | Fault Injection | 故障注入 |  | 人为模拟节点失败、延迟或资源不足等条件的测试手段。 |
| 23 | Runbook | 操作手册 |  | 描述常见故障排查与恢复步骤的标准化文档。 |
| 24 | Postmortem | 故障复盘 |  | 分析事件时间线、技术原因、影响及改进措施的回顾过程。 |
| 25 | Observability | 可观测性 |  | 通过日志、指标与追踪等外部信号理解系统内部状态的能力。 |

## 14. 分布式安全、身份与信任

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Mutual TLS | 双向传输层安全 | mTLS | 客户端与服务端通过证书互相认证的 TLS 通信方式。 |
| 2 | Transport Layer Security | 传输层安全 | TLS | 为网络通信提供认证、机密性和完整性保护的标准协议。 |
| 3 | Public Key Infrastructure | 公钥基础设施 | PKI | 管理证书、信任链、签发与吊销的体系。 |
| 4 | Certificate Authority | 证书颁发机构 | CA | 对公钥与主体身份绑定关系进行签名证明的实体。 |
| 5 | Workload Identity | 工作负载身份 |  | 为运行中的服务或任务赋予可验证的机器身份。 |
| 6 | Service Account | 服务账号 |  | 代表非人类程序或服务执行操作的身份主体。 |
| 7 | Authentication | 身份认证 |  | 核实通信对端或调用方身份声明是否真实的过程。 |
| 8 | Authorization | 授权 |  | 依据策略决定已认证主体是否可以执行某项操作。 |
| 9 | Least Privilege | 最小权限原则 |  | 只赋予主体完成任务所需最小权限的安全策略。 |
| 10 | Zero Trust | 零信任 |  | 不因网络位置默认信任，持续校验身份、设备及访问条件的安全理念。 |
| 11 | Access Control List | 访问控制列表 | ACL | 列明哪些主体被允许或拒绝访问资源的规则表。 |
| 12 | Role-based Access Control | 基于角色的访问控制 | RBAC | 根据主体承担的角色集合分配资源权限的模型。 |
| 13 | Attribute-based Access Control | 基于属性的访问控制 | ABAC | 综合主体、资源、动作和环境属性评估授权的模型。 |
| 14 | Secrets Management | 机密信息管理 |  | 安全存储、分发、轮换和审计凭证或密钥的机制。 |
| 15 | Key Rotation | 密钥轮换 |  | 定期或在风险事件后替换加密或签名密钥的过程。 |
| 16 | Envelope Encryption | 信封加密 |  | 用数据密钥加密内容，再由主密钥封装数据密钥的方案。 |
| 17 | Encryption at Rest | 静态数据加密 |  | 对磁盘或对象存储中的持久化数据进行加密保护。 |
| 18 | Encryption in Transit | 传输中加密 |  | 保护数据在网络链路上传送时的机密性。 |
| 19 | Token-based Authentication | 基于令牌的认证 |  | 使用短期或签名令牌代表已认证主体及声明的方案。 |
| 20 | JSON Web Token | JSON Web 令牌 | JWT | 以紧凑格式传递声明、可签名或加密的标准令牌结构。 |
| 21 | Replay Attack | 重放攻击 |  | 攻击者重复发送合法请求或认证材料以引发非预期执行的攻击。 |
| 22 | Nonce | 一次性随机数 |  | 用于挑战或协议消息新鲜度验证的只用一次的值。 |
| 23 | Distributed Denial of Service | 分布式拒绝服务 | DDoS | 通过大量来源同时消耗服务资源致使合法请求受影响的攻击。 |
| 24 | Byzantine Fault Tolerance | 拜占庭容错 | BFT | 在部分参与者发送任意错误或恶意消息时仍满足共识安全条件的协议能力。 |
| 25 | Quorum Certificate | 法定人数证书 | QC | 由满足阈值的多方签名或投票组成的可验证决策证明。 |

## 15. 性能、容量与资源调度

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Latency | 延迟 |  | 从操作发起到获得结果经历的时间。 |
| 2 | Throughput | 吞吐量 |  | 单位时间内系统成功完成的请求、字节或事件数量。 |
| 3 | Tail Latency | 尾部延迟 |  | 请求延迟分布高百分位处的响应时间。 |
| 4 | P99 Latency | 第 99 百分位延迟 | P99 | 在样本分布中约 99% 请求不超过的响应时间。 |
| 5 | Service Time | 服务时间 |  | 请求实际占用执行资源进行处理的时间。 |
| 6 | Queueing Delay | 排队延迟 |  | 请求在待处理队列中等待获得服务资源的时间。 |
| 7 | End-to-end Latency | 端到端延迟 |  | 用户请求跨越全部依赖链路直至完成的总时长。 |
| 8 | Fan-out | 请求扇出 |  | 一个请求同时触发多个下游服务调用的结构。 |
| 9 | Fan-in | 结果扇入 |  | 多个并行下游计算或请求结果汇聚到一个节点的结构。 |
| 10 | Critical Path | 关键路径 |  | 依赖图中决定整体完成时间的最长串行路径。 |
| 11 | Amdahl Law | 阿姆达尔定律 |  | 描述固定工作量中可并行部分限制总体加速比的规律。 |
| 12 | Little Law | 利特尔定律 |  | 稳定系统中平均在系统请求数等于到达率乘平均停留时间的关系。 |
| 13 | Queueing Theory | 排队论 |  | 研究随机到达、服务能力与等待时间关系的数学理论。 |
| 14 | Utilization | 资源利用率 |  | 计算或存储资源在统计时间内实际被占用的比例。 |
| 15 | Saturation | 资源饱和 |  | 资源负载接近或超出可持续处理能力的状态。 |
| 16 | Autoscaling | 自动伸缩 |  | 根据负载、资源指标或预测结果自动调整实例数量的机制。 |
| 17 | Load Balancing | 负载均衡 |  | 将请求流量分配到多个后端以提升处理能力与稳定性的机制。 |
| 18 | Round-robin Scheduling | 轮询调度 |  | 按固定循环顺序选择后端实例的负载分配方式。 |
| 19 | Least-connections Routing | 最少连接路由 |  | 优先将新连接交给当前连接数较少的后端。 |
| 20 | Consistent Hash Routing | 一致性哈希路由 |  | 按键的哈希位置将请求稳定映射到节点的路由方式。 |
| 21 | Data Locality | 数据局部性 |  | 尽量在数据所在节点或邻近位置执行计算以降低网络传输的原则。 |
| 22 | Resource Scheduling | 资源调度 |  | 为任务分配 CPU、内存、存储、网络等受限资源的过程。 |
| 23 | Bin Packing | 装箱分配 |  | 将不同资源需求的任务放入尽可能少的节点或满足容量约束的节点的优化问题。 |
| 24 | Capacity Planning | 容量规划 |  | 估计未来负载与资源需求并预留适当系统容量的活动。 |
| 25 | Hotspot Mitigation | 热点缓解 |  | 通过拆分、缓存、复制或限流减轻负载过于集中的措施。 |

## 16. 分布式测试、验证与形式化方法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributed Tracing | 分布式追踪 |  | 通过跨服务上下文把一次请求的多个处理片段关联起来的技术。 |
| 2 | Trace | 调用链 |  | 描述某个请求在多个组件间传播和执行的端到端轨迹。 |
| 3 | Span | 追踪片段 |  | 记录一个局部操作的起止时间、属性和上下文的追踪单元。 |
| 4 | Trace Context Propagation | 追踪上下文传播 |  | 通过请求头或消息元数据传递链路标识和父子关系的机制。 |
| 5 | Correlation ID | 关联标识符 |  | 用于关联同一业务请求在不同系统中的日志或事件的标记。 |
| 6 | Structured Logging | 结构化日志 |  | 以字段化格式记录事件以方便搜索和自动分析的日志方式。 |
| 7 | Metrics Cardinality | 指标基数 |  | 监控维度标签不同组合数量，过高会增加时序数据库负担。 |
| 8 | Prometheus | Prometheus 监控系统 |  | 通过采集时序指标和查询语言支持监控告警的开源系统。 |
| 9 | OpenTelemetry | OpenTelemetry 可观测性标准 |  | 为指标、追踪与日志提供接口、语义约定和数据传输组件的标准项目。 |
| 10 | Jepsen Testing | Jepsen 一致性测试 |  | 通过故障注入和操作历史分析检查分布式系统一致性的测试方法。 |
| 11 | Linearizability Checking | 线性一致性检查 |  | 验证并发操作历史是否能映射为遵守真实时间顺序的合法串行历史。 |
| 12 | History Recording | 操作历史记录 |  | 记录调用、响应、异常及时间关系以分析并发行为的过程。 |
| 13 | Model Checking | 模型检验 |  | 穷举或系统搜索有限状态空间以验证形式化性质的方法。 |
| 14 | Formal Specification | 形式化规格说明 |  | 用数学语言精确定义系统状态、行为和不变量的文档。 |
| 15 | TLA+ | TLA+ 规约语言 |  | 以时序逻辑和状态动作描述并验证并发及分布式系统的形式化语言。 |
| 16 | PlusCal | PlusCal 算法语言 |  | 可翻译为 TLA+ 规格的类伪代码并发算法描述语言。 |
| 17 | Invariant | 不变量 |  | 系统所有允许执行路径中始终必须成立的状态性质。 |
| 18 | Liveness Verification | 活性验证 |  | 检查在环境假设下系统是否能最终完成规定进展的验证活动。 |
| 19 | Fault-tolerance Testing | 容错测试 |  | 主动触发节点或链路故障并验证服务目标的测试。 |
| 20 | Partition Testing | 网络分区测试 |  | 隔离节点间网络流量以验证一致性、可用性与恢复行为的实验。 |
| 21 | Deterministic Simulation | 确定性模拟 |  | 用可控调度与事件序列复现实例间竞争和网络行为的测试方法。 |
| 22 | Property-based Testing | 基于性质的测试 |  | 自动生成多类输入并检查普适不变量或业务性质的测试技术。 |
| 23 | Fuzz Testing | 模糊测试 |  | 自动构造大量异常或随机输入寻找协议与实现缺陷的测试方法。 |
| 24 | Rolling Upgrade Testing | 滚动升级测试 |  | 验证集群新旧版本混合运行和逐步替换时协议兼容性的测试。 |
| 25 | Disaster Recovery Drill | 灾难恢复演练 |  | 模拟重大故障并验证恢复步骤、RTO、RPO 与组织响应的演习。 |

## 易混淆概念辨析

| 概念 | 核心区别 |
|---|---|
| 线性一致性 vs 可串行化 | 线性一致性主要约束对象操作的单点生效及实时顺序；可串行化约束跨对象事务可等价为某串行次序。严格可串行化同时包含事务与实时顺序约束。 |
| CAP 可用性 vs 业务高可用 | CAP 可用性要求非故障节点对每个请求最终响应；工程上的高可用常用 SLO、故障时间与成功率衡量，不可混用。 |
| 最终一致性 vs 因果一致性 | 最终一致性强调无新更新时的最终收敛；因果一致性还要求观察结果遵守因果先后关系。 |
| Paxos vs Raft | 两者皆可实现复制状态机共识；Paxos 从提案仲裁出发，Raft 强调任期、主节点与日志复制的结构化设计。 |
| 复制 vs 分片 | 复制为同一逻辑数据保存多个副本；分片把不同数据子集分布在节点上，两者可以组合。 |
| 同步复制 vs 异步复制 | 同步策略在成功确认前等待规定数量副本；异步策略先响应再复制，吞吐和失效时数据丢失风险不同。 |
| 2PC vs Saga | 2PC 通过参与者准备与统一决议实现原子提交，但可能阻塞；Saga 通过本地提交和业务补偿处理跨服务流程，通常不提供同样强的隔离性。 |
| 至少一次投递 vs 恰好一次效果 | 至少一次可重试但可能重复；恰好一次状态效果依赖去重、事务提交或幂等业务端，并须说明保证边界。 |
| 事件时间 vs 处理时间 | 事件时间表示业务事件发生时刻；处理时间由流处理节点当前时钟决定，迟到数据会令窗口结果不同。 |
| 租约 vs 隔离令牌 | 租约靠有限时效授权，旧持有者暂停后可能复活；隔离令牌使受保护资源拒绝过期世代操作。 |
| 故障检测 vs 故障确定 | 异步网络中超时可能源于延迟而非崩溃，实用故障检测通常只能给出怀疑而不能证明。 |
| 吞吐量 vs 尾延迟 | 更高吞吐不代表更低 P99；排队和扇出可使高百分位延迟在资源饱和时迅速上升。 |

## 中等难度面试问题与答案

### 面试题 1：为何网络分区时不能同时保证线性一致性与 CAP 可用性？

**参考思路：**两个无法通信的分区若都必须立即完成读写，就无法就跨分区最新值协调；要守住实时顺序，一侧可能需要拒绝或等待。

### 面试题 2：Raft 中为何不能仅凭多数派复制就任意提交旧任期日志？

**参考思路：**Raft 提交规则需结合当前任期条目与日志匹配性质，否则不同任期选举可能让旧条目被覆盖；当前任期条目一旦按规则提交，其前缀也随之提交。

### 面试题 3：为什么仅有 N=3、R=2、W=2 的数量配置不一定得到线性一致性？

**参考思路：**需要明确同步确认、版本冲突、失败模型和读写路径；松散仲裁、并发写、节点临时承接等可破坏简单交集推理。

### 面试题 4：逻辑时钟能否推断真实经过了多少毫秒？

**参考思路：**不能；Lamport 时钟只保持一类因果顺序信息，不测量真实时间间隔。

### 面试题 5：如何避免带超时的分布式锁让旧主继续写入？

**参考思路：**由存储服务验证单调递增隔离令牌，拒绝旧令牌；仅靠租约客户端本地判断不足。

### 面试题 6：一次 RPC 超时后，客户端能否断言服务端未执行？

**参考思路：**不能；响应可能丢失或延迟。重试必须考虑幂等键、请求去重或业务补偿。

### 面试题 7：为什么快照隔离仍可能产生写偏斜？

**参考思路：**两个事务在同一快照下读到合法前置条件，却修改不同记录，双方不发生同键写冲突而联合结果破坏跨行约束。

### 面试题 8：2PC 的阻塞性体现在哪里？

**参考思路：**参与者完成准备并持久化锁定资源后，如果协调者失联，可能无法确定全局决议而必须等待恢复或外部协调。

## 中等难度考试题与解析

### 考试题 1：向量时钟 [2,1,0] 与 [1,2,0] 是否有因果先后？

**解析：**两向量分别在不同维度领先，既不逐分量小于等于对方，故可视为并发事件。

### 考试题 2：五节点 Raft 集群可承受几个崩溃节点仍继续提交？

**解析：**使用多数派投票时需至少三个节点在线并可互通，因此通常可承受两个节点崩溃。

### 考试题 3：N=5 的多数派大小是多少？

**解析：**floor(5/2)+1=3，任意两个大小为 3 的多数派必有至少一个共同成员。

### 考试题 4：三个后端延迟分别为 20、50、80ms 并行扇出，若汇总须等全部完成，理论最短完成时间？

**解析：**忽略网络与聚合开销时取最长依赖分支，即 80ms，而不是三者求和。

### 考试题 5：故障后允许最多丢失 15 分钟数据、2 小时内恢复，分别对应什么指标？

**解析：**RPO=15 分钟，RTO=2 小时；前者关注数据可恢复点，后者关注服务恢复时限。

### 考试题 6：若到达率 100 req/s、平均系统内停留时间 0.2s，平均在途请求数是多少？

**解析：**在满足稳定性等利特尔定律假设时，L=λW=100×0.2=20 个。

### 考试题 7：一个节点每秒处理 300 请求、到达 390 请求，队列会怎样？

**解析：**若持续超出服务能力且无丢弃或背压，队列期望持续增长，等待延迟无法长期稳定。

### 考试题 8：两阶段提交中的 prepare 阶段允许参与者提前释放全部锁吗？

**解析：**一般不能；参与者须保证最终提交决议可实现，提前释放可能破坏事务隔离或原子性前提。

## 核心参考文献

下列为原始论文、教材与官方技术资料；列出的资料并不意味着其作者认可本项目全部译名或参与审稿。

1. [Designing Data-Intensive Applications, 2nd ed. (Kleppmann & Riccomini)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
2. [Time, Clocks, and the Ordering of Events in a Distributed System (Lamport, 1978)](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/)
3. [Paxos Made Simple (Lamport, 2001)](https://www.microsoft.com/en-us/research/publication/paxos-made-simple/)
4. [In Search of an Understandable Consensus Algorithm (Ongaro & Ousterhout, 2014)](https://raft.github.io/)
5. [Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al., 2007)](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
6. [MapReduce: Simplified Data Processing on Large Clusters (Dean & Ghemawat, 2004)](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
7. [Spanner: TrueTime and external consistency (Google Cloud documentation)](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency)
8. [Jepsen: Consistency Models](https://jepsen.io/consistency/models)

## 使用与维护说明

- 原始稿：`data/distributed-systems/chapters/*.tsv`。
- 聚合词表：`data/distributed-systems.tsv`；Markdown、PDF 为单学科脚本生成的出版物。
- 原始四列为 `en|zh|abbr|definition`，第三列只用于真实缩写。
- 跨版本或供应商特有的语义需以官方文档及实现契约为准。
- 后续可将审稿确认的词条逐批接入网站检索与长篇 Wiki。
