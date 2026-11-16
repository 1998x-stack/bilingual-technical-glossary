# Apache Kafka 专有名词中英文对照表

> Apache Kafka Technical Glossary · 中英文术语、简明释义与核心概念辨析
>
> 版本说明：参考 Apache Kafka 官方文档，以 Kafka 4.x 语境为主。KRaft 为 4.x 的元数据管理模式；Share Groups 在 Kafka 4.2 达到生产可用（GA）。部分功能依赖版本和具体配置。

## 如何阅读

- **英文术语**：尽可能保留官方写法、缩写及常见 API／配置项拼写。
- **中文译名**：优先使用工程社区常见译法；同一术语可能存在其他译法。
- **一句话解释**：帮助检索和区分概念，不替代官方语义与实现细节。
- **资料性质**：学习与工程速查资料；实际生产配置以所用 Kafka 版本文档为准。

## 核心概念一图读懂

```text
Producer ──[Record / Key / Value]──▶ Topic / Partition ──▶ Consumer Group
                      Broker Cluster (Replica / ISR)
                           │
                           ▼
                   KRaft Controller Quorum
                Metadata / Leadership / Configuration
```

## 高频易混淆概念

| 概念 A | 概念 B | 关键区别 |
|---|---|---|
| Topic | Partition | Topic 是逻辑事件流；Partition 是可排序、复制、并行处理的具体日志。 |
| Offset | Committed Offset | Offset 是分区内位置；Committed Offset 是消费组保存的下次读取位置。 |
| LEO | High Watermark | LEO 是本地下一条写入位置；HW 是复制同步进度相关的可读边界。 |
| High Watermark | LSO | HW 与复制同步有关；LSO 进一步限定 `read_committed` 下事务可见范围。 |
| Replication Factor | min.insync.replicas | 前者是配置副本总数；后者影响 `acks=all` 写入的最低 ISR 要求。 |
| Idempotence | Transaction | 幂等性主要解决 Producer 重试重复；事务可原子组合跨分区写入与偏移量提交。 |
| At-least-once | Exactly-once | 前者允许重复；后者需要限定支持范围和端到端的处理链路。 |
| Consumer Group | Share Group | 传统组对同一分区通常单成员独占；共享组允许多个成员协作处理记录。 |
| KStream | KTable | KStream 视为事件流；KTable 把相同 Key 的新记录视为表行更新。 |
| Log Retention | Log Compaction | 前者按时间／空间删除旧数据；后者按 Key 清理过期版本。 |
| Controller | Group Coordinator | 前者管理集群元数据和领导权；后者管理消费者组状态。 |

## 推荐官方资料

1. [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
2. [Kafka Design](https://kafka.apache.org/44/design/)
3. [Kafka Operations](https://kafka.apache.org/44/operations/)
4. [Kafka Streams](https://kafka.apache.org/44/streams/)
5. [Kafka Connect](https://kafka.apache.org/44/connect/)
6. [Kafka Security](https://kafka.apache.org/44/security/)
7. [Kafka 4.2.0 Release Announcement — Share Groups GA](https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/)

---

## 01 核心概念与事件流 · Fundamentals & Event Streaming

| English | 中文 | 释义 |
|---|---|---|
| Apache Kafka | Apache Kafka 分布式事件流平台 | 用于发布、持久化、处理和传输事件流的分布式平台。 |
| Event | 事件 | 表示一件已发生事实的数据单元；在 Kafka 文档中常与 Record 互用。 |
| Record | 记录 | 写入主题分区的基本数据单元，包含键、值、时间戳等。 |
| Message | 消息 | 对 Record 的常见称呼；日常讨论中经常互换使用。 |
| Event Streaming | 事件流处理／事件流传输 | 持续采集、存储、传输并处理事件的技术范式。 |
| Publish/Subscribe | 发布／订阅 | 生产者向主题发布记录，消费者订阅并读取记录。 |
| Producer | 生产者 | 向 Kafka 主题写入记录的客户端。 |
| Consumer | 消费者 | 从 Kafka 主题分区拉取记录的客户端。 |
| Broker | 代理节点 | 承载数据分区、处理客户端读写请求的 Kafka 服务器。 |
| Cluster | 集群 | 协同提供 Kafka 服务的一组 Broker 和相关节点。 |
| Topic | 主题 | 记录的逻辑分类和发布订阅入口，实际由分区组成。 |
| Partition | 分区 | 主题的有序日志分片，也是并行处理与复制的单位。 |
| Key | 消息键 | 可用于决定分区归属，也用于压缩日志时识别同一键。 |
| Value | 消息值 | 记录承载的主要业务内容，可为任意字节序列。 |
| Header | 消息头 | 随记录附带的键值元数据集合。 |
| Timestamp | 时间戳 | 记录携带的创建时间或 Broker 追加时间。 |
| Schema | 数据模式 | 约定事件载荷的数据结构与字段类型；常由外部系统管理。 |
| Serialization | 序列化 | 将应用对象编码为 Kafka 传输的字节数组。 |
| Deserialization | 反序列化 | 将 Kafka 中的字节数组还原为应用对象。 |

## 02 集群与网络架构 · Cluster & Networking

| English | 中文 | 释义 |
|---|---|---|
| Bootstrap Server | 引导服务器 | 客户端初始连接的 Broker 地址；不是固定代理入口。 |
| Metadata | 集群元数据 | 描述主题、分区、Leader、Broker 等信息的数据。 |
| Metadata Refresh | 元数据刷新 | 客户端重新获取集群拓扑和分区 Leader 信息。 |
| Node ID | 节点标识 | Kafka 节点的数字身份，常见配置项为 node.id。 |
| Broker ID | Broker 标识 | 用于识别 Broker 的编号；新部署通常使用 node.id。 |
| Listener | 监听器 | Broker 接受某类网络连接的端点及协议配置。 |
| Advertised Listener | 对外公布的监听地址 | 返回给客户端供其后续直连的地址，需可达。 |
| Inter-broker Communication | Broker 间通信 | 副本同步及节点间请求所使用的通信路径。 |
| Controller | 控制器 | 负责集群元数据管理、分区领导权等控制任务的角色。 |
| Active Controller | 活动控制器 | 当前承担集群控制职责的 Controller。 |
| Controller Quorum | 控制器法定多数集群 | 在 KRaft 中复制元数据日志的一组控制器投票节点。 |
| Rack Awareness | 机架感知 | 按机架拓扑分布副本，降低同机架故障风险。 |
| Rack ID | 机架标识 | 用于机架感知分配的逻辑故障域标签。 |
| Request Handler | 请求处理线程 | Broker 处理网络请求的执行资源。 |
| Network Thread | 网络线程 | 负责处理连接及网络收发的线程资源。 |

## 03 KRaft 与元数据管理 · KRaft & Metadata Management

| English | 中文 | 释义 |
|---|---|---|
| KRaft | Kafka Raft 元数据模式 | Kafka 基于 Raft 的元数据管理机制，替代 ZooKeeper 模式。 |
| Raft | Raft 共识算法 | 用于维护控制器日志复制和领导者选举的一致性算法。 |
| Metadata Log | 元数据日志 | KRaft 中以复制日志形式记录集群元数据变更。 |
| Metadata Record | 元数据记录 | 描述主题、配置、授权等集群状态变更的记录。 |
| Metadata Snapshot | 元数据快照 | 用于压缩状态恢复成本的元数据状态快照。 |
| Quorum | 法定多数 | 确保共识决策所需的足够投票者集合。 |
| Voter | 投票节点 | 参与控制器 Quorum 选举与提交判定的节点。 |
| Observer | 观察者节点 | 复制元数据但不参与 Quorum 投票的节点。 |
| Controller Leader | 控制器领导者 | KRaft Quorum 当前当选的领导控制器。 |
| Leader Epoch | 领导任期编号 | 标识领导权更迭的单调递增纪元信息。 |
| Cluster ID | 集群标识 | 创建集群时生成的唯一标识。 |
| Storage Formatting | 存储格式化 | 初始化 Kafka 数据目录与集群标识的过程。 |
| Combined Mode | 混合角色模式 | 同一进程同时承担 Broker 与 Controller 角色。 |
| Dedicated Controller | 独立控制器 | 只运行 Controller 角色而不承担数据代理职责。 |
| Process Roles | 进程角色 | process.roles 配置决定 broker、controller 或两者。 |
| Static Quorum | 静态法定多数配置 | 使用预先指定的控制器投票节点集合。 |
| Dynamic Quorum | 动态法定多数配置 | 支持通过管理流程调整控制器投票节点集合。 |
| ZooKeeper Mode | ZooKeeper 模式（旧） | 早期 Kafka 使用 ZooKeeper 管理元数据；Kafka 4.x 已移除。 |

## 04 主题、分区与路由 · Topics, Partitions & Routing

| English | 中文 | 释义 |
|---|---|---|
| Topic Name | 主题名称 | 标识业务事件流的逻辑名称。 |
| Topic Partition | 主题分区 | 由主题名称与分区编号共同唯一标识的日志。 |
| Partition ID | 分区编号 | 同一主题下用于区分分区的整数编号。 |
| Partition Count | 分区数量 | 影响主题并行度、吞吐能力及键分布的分片数。 |
| Partitioner | 分区器 | 生产者决定记录应写入哪个主题分区的逻辑。 |
| Key-based Partitioning | 按键分区 | 根据 Key 的哈希或配置策略选择目标分区。 |
| Sticky Partitioning | 粘性分区 | 无键记录在一段时间内集中发送到某个分区以利批处理。 |
| Custom Partitioner | 自定义分区器 | 实现特定业务路由规则的分区选择逻辑。 |
| Ordering Guarantee | 顺序保证 | 同一分区内记录具备确定顺序；跨分区不保证全局顺序。 |
| Partition Reassignment | 分区重新分配 | 将分区副本迁移至不同 Broker 的管理操作。 |
| Preferred Leader | 首选领导副本 | 副本分配顺序中优先成为 Leader 的副本。 |
| Leader Election | 领导副本选举 | 在可用副本中选出处理读写的领导副本。 |
| Topic Configuration | 主题级配置 | 覆盖部分 Broker 默认值的主题参数。 |
| Internal Topic | 内部主题 | Kafka 自身用于协调、状态与事务等目的的主题。 |
| Topic Deletion | 主题删除 | 删除主题元数据及其相关数据的管理操作。 |

## 05 日志、偏移量与存储 · Log, Offset & Storage

| English | 中文 | 释义 |
|---|---|---|
| Append-only Log | 追加式日志 | 分区记录按逻辑顺序追加，既有位置不随消费移动。 |
| Offset | 偏移量 | 记录在某个分区中的位置标识；不同分区互不比较。 |
| Log End Offset (LEO) | 日志末端偏移量 | 本地日志下一条待写记录的位置，并非最后一条的编号。 |
| High Watermark (HW) | 高水位 | 副本同步进度相关边界，通常用于限制可见记录。 |
| Log Start Offset | 日志起始偏移量 | 当前仍可读取的最早记录位置。 |
| Last Stable Offset (LSO) | 最后稳定偏移量 | read_committed 模式下事务可见范围的上界。 |
| Log Segment | 日志段 | 分区日志按大小或时间切分的磁盘文件组。 |
| Active Segment | 活动日志段 | 当前正在追加记录的日志段。 |
| Segment Roll | 日志段滚动 | 创建新活动日志段以继续追加数据。 |
| Offset Index | 偏移量索引 | 从逻辑 Offset 快速定位日志段内物理位置的索引。 |
| Time Index | 时间索引 | 辅助依据时间戳定位记录的索引。 |
| Log Retention | 日志保留策略 | 按保留时间或大小清理可删除的数据。 |
| Retention Time | 保留时长 | 数据在满足清理条件前的时间配置。 |
| Retention Bytes | 保留容量 | 分区日志可保留数据量的配置阈值。 |
| Log Compaction | 日志压缩清理 | 依据 Key 保留较新版本记录的后台清理机制。 |
| Delete Retention | 删除标记保留时长 | 压缩主题中 Tombstone 被保留的相关时长。 |
| Tombstone | 墓碑消息 | 值为 null、用来表示某 Key 删除语义的记录。 |
| Cleanup Policy | 清理策略 | 常见 delete、compact，亦可按配置组合使用。 |
| Page Cache | 页缓存 | 操作系统缓存日志文件页，改善 Kafka 顺序读写性能。 |
| Zero-copy | 零拷贝 | 利用系统调用减少从磁盘到网络发送时的数据拷贝。 |
| Tiered Storage | 分层存储 | 将部分较旧日志段卸载到远端存储的功能体系。 |
| Remote Log Segment | 远端日志段 | 启用分层存储后保存在远端层的日志数据段。 |

## 06 生产者、批处理与发送 · Producer & Batching

| English | 中文 | 释义 |
|---|---|---|
| Producer API | 生产者 API | 用于向主题发送记录的客户端编程接口。 |
| Record Accumulator | 记录累积器 | 在 Producer 内部按分区暂存待批量发送记录。 |
| Producer Batch | 生产者批次 | 合并发送至某个分区的多条记录。 |
| Batch Size | 批次大小 | batch.size 配置的每分区目标批量上限。 |
| Linger | 等待聚合时间 | linger.ms 控制为凑批可增加的发送等待时间。 |
| Buffer Memory | 发送缓冲内存 | buffer.memory 限制 Producer 内部可用缓冲空间。 |
| Compression Type | 压缩算法类型 | 例如 gzip、snappy、lz4、zstd 或 none。 |
| Acks | 确认级别 | acks 配置控制生产者请求的成功确认条件。 |
| Acks=all | 全部所需同步副本确认 | Leader 在满足当前 ISR 复制条件后确认写入。 |
| Delivery Timeout | 交付超时 | 交付重试的总体时间上限，由 delivery.timeout.ms 控制。 |
| Request Timeout | 请求超时 | 等待单次请求响应的最长时间配置。 |
| Retry | 重试 | 可恢复错误发生后重新发起发送请求。 |
| Retry Backoff | 重试退避 | 在重试之间插入等待，避免持续立即重试。 |
| In-flight Requests | 在途请求 | 已发送但尚未收到结果的请求集合。 |
| Callback | 回调函数 | 异步发送完成后接收结果或错误的函数。 |
| Future | 异步结果对象 | 表示提交的发送操作最终完成状态的对象。 |
| Producer Interceptor | 生产者拦截器 | 在发送前后扩展观察或变换逻辑的组件。 |
| Serialization Error | 序列化错误 | 对象编码失败造成的客户端发送问题。 |

## 07 消费者、分组与协调 · Consumer & Group Coordination

| English | 中文 | 释义 |
|---|---|---|
| Consumer API | 消费者 API | 用于订阅主题、拉取和处理记录的客户端接口。 |
| Consumer Group | 消费者组 | 通过同一 group.id 共享分区处理任务的一组消费者。 |
| Group ID | 组标识 | 标识消费者组、提交 Offset 命名空间的字符串。 |
| Group Coordinator | 组协调器 | 管理消费者组成员、状态及 Offset 提交的 Broker 角色。 |
| Partition Assignment | 分区分配 | 将已订阅的主题分区分配给组内消费者。 |
| Assignment Strategy | 分配策略 | 决定组内成员各自负责哪些分区的策略。 |
| Rebalance | 再均衡 | 成员变化或订阅拓扑变化后重新调整分区归属。 |
| Eager Rebalance | 全量再均衡 | 先收回分区，再重新统一分配的流程。 |
| Cooperative Rebalance | 协作式再均衡 | 以增量方式撤销并迁移部分分区，减少停顿。 |
| Heartbeat | 心跳 | 消费者向协调器报告仍然存活的周期性机制。 |
| Session Timeout | 会话超时 | 协调器判定成员失联所允许的时长。 |
| Max Poll Interval | 最大轮询间隔 | 消费者调用 poll() 的允许最大间隔限制。 |
| Poll | 轮询 | 消费者调用 poll() 获取可用记录及驱动相关协调处理。 |
| Fetch | 拉取请求 | 消费者向 Broker 请求分区数据的网络操作。 |
| Fetch Minimum Bytes | 最小拉取字节数 | fetch.min.bytes 设定返回拉取请求前期望的数据量。 |
| Auto Offset Reset | 初始偏移量重置策略 | 无有效已提交位置时可选 earliest、latest 等处理方式。 |
| Auto Commit | 自动提交偏移量 | 客户端按配置自动周期性提交处理位置。 |
| Manual Commit | 手动提交偏移量 | 应用显式控制何时提交消费进度。 |
| Committed Offset | 已提交偏移量 | 某组为某分区保存的下次准备读取的位置。 |
| Consumer Lag | 消费滞后量 | 消费者进度相对分区目标末端位置的差距。 |
| Pause / Resume | 暂停／恢复拉取 | 临时控制已分配分区是否继续返回记录。 |
| Seek | 定位偏移量 | 将消费者某个分区的下一次读取位置重置为指定值。 |
| Static Membership | 静态成员身份 | 借助 group.instance.id 降低短暂重启造成的分组抖动。 |
| Consumer Group Protocol | 消费者组协议 | 规定成员协调和分区分配的协议；新旧协议行为存在差异。 |

## 08 副本、容错与高可用 · Replication & Availability

| English | 中文 | 释义 |
|---|---|---|
| Replication | 副本复制 | 将分区数据复制至多台 Broker 以提高容错能力。 |
| Replication Factor (RF) | 副本因子 | 一个分区配置的副本总数，含 Leader 副本。 |
| Leader Replica | 领导副本 | 处理该分区正常读写请求的副本。 |
| Follower Replica | 跟随副本 | 从 Leader 拉取并复制分区数据的副本。 |
| In-sync Replicas (ISR) | 同步副本集合 | 复制进度满足同步条件的副本集合。 |
| Out-of-sync Replica | 失同步副本 | 因落后等原因不属于当前 ISR 的副本。 |
| Min In-sync Replicas | 最小同步副本数 | min.insync.replicas 为 acks=all 写入规定最低 ISR 要求。 |
| Under-replicated Partition | 副本同步不足的分区 | 当前 ISR 副本数少于配置的副本因子。 |
| Under-min-ISR Partition | 低于最小 ISR 的分区 | 当前同步副本数量低于 min.insync.replicas 的分区。 |
| Offline Partition | 离线分区 | 当前没有可服务的 Leader 的分区。 |
| Unclean Leader Election | 非同步副本领导选举 | 允许从 ISR 外选 Leader，可能导致已确认数据丢失。 |
| Leader Failover | 领导副本故障切换 | 当前 Leader 不可用后由其他副本接管。 |
| Replica Fetcher | 副本拉取线程 | Follower 使用的分区数据同步机制或线程。 |
| Replica Lag | 副本落后量 | Follower 相对 Leader 的复制进度差距。 |
| Availability | 可用性 | 发生部分故障时系统继续提供服务的能力。 |
| Durability | 持久性 | 写入成功后数据在故障下保持不丢失的能力。 |

## 09 一致性、事务与交付语义 · Delivery Semantics & Transactions

| English | 中文 | 释义 |
|---|---|---|
| At-most-once | 至多一次 | 处理可能丢失，但按特定提交方式避免重复交付。 |
| At-least-once | 至少一次 | 通过重试避免遗漏，但发生故障时可能重复处理。 |
| Exactly-once Semantics (EOS) | 恰好一次语义 | 在支持的事务性 Kafka 处理链路中避免重复的最终影响。 |
| Idempotent Producer | 幂等生产者 | 对单个生产者会话中的重试写入进行去重保护。 |
| Producer ID (PID) | 生产者标识 | Broker 用于识别生产者及其幂等状态的编号。 |
| Producer Epoch | 生产者纪元 | 用于区分同一事务生产者的不同代，阻止旧实例写入。 |
| Sequence Number | 序列号 | Producer 对分区写入排序并辅助检测重复请求的编号。 |
| Transaction | 事务 | 将多个分区写入及可选 Offset 提交组织成原子操作。 |
| Transactional ID | 事务标识 | 跨生产者实例恢复并维护事务身份的稳定字符串。 |
| Transaction Coordinator | 事务协调器 | 维护事务状态并协调提交或中止的 Broker 角色。 |
| Commit Transaction | 提交事务 | 使事务成功写入的数据对已提交读取模式可见。 |
| Abort Transaction | 中止事务 | 标记事务失败，使其写入不对 read_committed 读者可见。 |
| Transaction Marker | 事务标记 | 写入分区日志以表示事务提交或中止的控制记录。 |
| Read Committed | 只读已提交数据 | 消费者隔离级别，屏蔽已中止及未完成事务数据。 |
| Read Uncommitted | 允许读取未提交数据 | 消费者隔离级别，可读取尚未最终完成的事务数据。 |
| Fencing | 旧实例隔离 | 通过 Epoch 等机制拒绝过期生产者或成员继续操作。 |

## 10 Share Group 与队列式消费 · Share Groups & Queue Semantics

| English | 中文 | 释义 |
|---|---|---|
| Share Group | 共享组 | 允许多个成员协作处理同一分区记录的 Kafka 4.x 消费模型。 |
| Share Consumer | 共享消费者 | 使用 Share Group 协议拉取、处理并确认记录的客户端。 |
| Record-level Acknowledgement | 记录级确认 | 可以按记录而非按分区连续 Offset 进行处理确认。 |
| Acquisition | 记录获取／占有 | 共享消费者暂时取得某记录处理权的机制。 |
| Acquisition Lock | 获取锁 | 避免同一时刻多方重复处理同一已占有记录的锁定状态。 |
| Acknowledgement | 处理确认 | 共享消费者反馈记录已成功或失败处理等结果。 |
| Delivery Attempt | 投递尝试次数 | 统计记录被交付处理的次数以支持失败治理。 |
| Release | 释放记录 | 共享消费者放弃处理权，使记录可能被再次交付。 |
| Reject | 拒绝记录 | 共享消费者报告记录不应再次正常投递的处理结果。 |
| Renew | 续期确认 | 延长共享记录获取锁的有效处理时间，取决于版本支持。 |
| Share Coordinator | 共享组协调器 | 负责 Share Group 状态、成员和记录确认的协调角色。 |
| Share Partition | 共享分区 | 针对 Share Group 的分区级获取、确认和进度跟踪单元。 |

## 11 Kafka Connect 数据集成 · Kafka Connect & Integration

| English | 中文 | 释义 |
|---|---|---|
| Kafka Connect | Kafka Connect 数据集成框架 | 提供可配置的外部系统与 Kafka 之间数据导入导出机制。 |
| Connector | 连接器 | 定义对某一外部系统进行读写的集成组件。 |
| Source Connector | 源连接器 | 从外部系统读取数据并写入 Kafka 主题。 |
| Sink Connector | 汇连接器 | 从 Kafka 主题消费数据并写入外部系统。 |
| Task | 任务 | 连接器划分的实际并行执行单元。 |
| Worker | 工作节点 | 运行 Connector 和 Task 的 Connect 服务进程。 |
| Standalone Mode | 单机模式 | 由单个 Worker 执行 Connect 任务的运行方式。 |
| Distributed Mode | 分布式模式 | 由多个 Worker 协同管理任务的运行方式。 |
| Converter | 数据转换器 | 在 Kafka 字节数据与 Connect 内部数据模型间转换。 |
| Single Message Transform (SMT) | 单消息变换 | 在进入或离开 Connect 管道前对单条消息做轻量变换。 |
| Connect Schema | Connect 模式 | Connect 内部用于描述数据字段和结构的模式对象。 |
| Source Offset | 源端进度位置 | 源连接器记录已读取外部数据位置的检查点。 |
| Connector Configuration | 连接器配置 | Connector 的插件类、任务数、连接参数等配置。 |
| Connector Plugin | 连接器插件 | 用于扩展 Connect 数据源或目标系统的插件包。 |
| Dead Letter Queue (DLQ) | 死信队列 | 用于接收无法正常转换或处理记录的备用主题／管道。 |
| Exactly-once Source Support | 源端恰好一次支持 | 满足指定条件时 Connect Source 侧的事务性传输能力。 |

## 12 Kafka Streams 流处理 · Kafka Streams & Stateful Processing

| English | 中文 | 释义 |
|---|---|---|
| Kafka Streams | Kafka Streams 流处理库 | 基于 Kafka 构建客户端流计算应用的 Java/Scala 库。 |
| Topology | 处理拓扑 | 定义源、处理节点、状态与输出边之间关系的有向图。 |
| Source Processor | 源处理器 | 从输入主题读取记录并送入拓扑的节点。 |
| Sink Processor | 汇处理器 | 将处理结果写入 Kafka 输出主题的节点。 |
| Processor API | 处理器 API | 定义自定义处理节点及状态交互的低层接口。 |
| DSL | 领域特定语言 | 以高层算子描述流过滤、聚合、联结等业务逻辑的 API。 |
| KStream | 事件流 | 表示逐条到达的连续记录流抽象。 |
| KTable | 更新表 | 将相同 Key 的最新值解释为表行更新的抽象。 |
| GlobalKTable | 全局表 | 在每个 Streams 实例维护完整副本的表抽象。 |
| Stream-table Join | 流表联结 | 将流事件与表的当前状态按键关联。 |
| Stream-stream Join | 流流联结 | 按指定窗口条件联结两条事件流。 |
| Windowing | 窗口化 | 按照时间范围将事件分组计算。 |
| Tumbling Window | 滚动窗口 | 固定长度且互不重叠的窗口。 |
| Hopping Window | 跳跃窗口 | 按固定步长推进、允许重叠的窗口。 |
| Session Window | 会话窗口 | 根据事件间的空闲间隔划分的动态窗口。 |
| Event Time | 事件时间 | 事件本身产生时刻的时间语义。 |
| Processing Time | 处理时间 | 处理程序实际执行某条记录时的时间语义。 |
| Grace Period | 迟到宽限期 | 窗口接受一定迟到记录的额外时间。 |
| Aggregation | 聚合 | 对分组或窗口中的记录计算累计结果。 |
| State Store | 状态存储 | 用于保存联结、聚合等有状态算子局部状态的组件。 |
| RocksDB State Store | RocksDB 状态存储 | 使用嵌入式 RocksDB 持久化本地状态的常见实现。 |
| Changelog Topic | 变更日志主题 | 将状态存储更新写回 Kafka 以支持故障恢复。 |
| Repartition Topic | 重新分区主题 | 在按新 Key 分组或联结前重分布记录的内部主题。 |
| Task | 流处理任务 | Streams 中由输入分区组合决定的处理并行单位。 |
| Stream Thread | 流处理线程 | 运行 Streams 任务并驱动处理拓扑的线程。 |
| Interactive Queries | 交互式查询 | 访问 Streams 应用本地状态存储的能力。 |

## 13 安全、认证与授权 · Security & Authorization

| English | 中文 | 释义 |
|---|---|---|
| Authentication | 身份认证 | 验证客户端或服务器连接者身份的过程。 |
| Authorization | 访问授权 | 判定身份是否被允许执行特定资源操作的过程。 |
| Encryption in Transit | 传输加密 | 使用 TLS 保护连接传输中的数据。 |
| TLS / SSL | 传输层安全协议 | 为 Kafka 连接提供加密与可选证书认证。 |
| Mutual TLS (mTLS) | 双向 TLS | 客户端和服务端都通过证书验证对方身份。 |
| SASL | 简单认证与安全层 | Kafka 支持的可插拔认证协议框架。 |
| SASL/PLAIN | 明文口令机制 | 使用用户名和口令的 SASL 机制，应与 TLS 配合。 |
| SASL/SCRAM | 加盐挑战响应认证 | 基于 SCRAM-SHA-256 / 512 的认证方式。 |
| SASL/OAUTHBEARER | OAuth 令牌认证 | 基于 Bearer Token 的 SASL 认证机制。 |
| Kerberos / GSSAPI | Kerberos 认证 | 面向既有 Kerberos 身份体系的认证机制。 |
| ACL | 访问控制列表 | 针对资源、操作、主体及来源地址定义权限规则。 |
| Principal | 安全主体 | 被认证的用户或服务标识。 |
| Super User | 超级用户 | 可绕过常规 ACL 检查的特权主体。 |
| Keystore | 密钥库 | 用于保管本地证书和私钥的密钥容器。 |
| Truststore | 信任库 | 用于存储受信任 CA 或对端证书的容器。 |

## 14 性能、容量与可观测性 · Performance & Observability

| English | 中文 | 释义 |
|---|---|---|
| Throughput | 吞吐量 | 单位时间内生产或消费的数据量或记录数。 |
| Latency | 延迟 | 一次操作从发起至完成所经历的时间。 |
| End-to-end Latency | 端到端延迟 | 从事件产生到下游完成处理的总体耗时。 |
| P99 Latency | 第 99 百分位延迟 | 99% 请求不超过的延迟统计阈值。 |
| Backpressure | 背压 | 下游处理能力不足时限制上游供给速度的机制。 |
| Batching | 批处理 | 将多条记录合并处理以减少请求和系统开销。 |
| Compression Ratio | 压缩比 | 衡量压缩前后数据大小差异的比例。 |
| JMX Metrics | JMX 指标 | 通过 Java 管理扩展暴露的 Kafka 运行指标。 |
| Bytes In / Out | 输入／输出字节速率 | Broker 入口和出口的流量监测指标。 |
| Messages In | 消息写入速率 | 进入 Broker 的记录数量变化率。 |
| Request Queue | 请求队列 | Broker 尚未处理的网络请求积压位置。 |
| Fetch Latency | 拉取延迟 | 消费者 Fetch 请求在服务端或客户端的耗时。 |
| Consumer Lag Monitoring | 消费滞后监控 | 跟踪消费者进度与分区末端之间的差距。 |
| Under-replicated Partitions | 同步不足分区数 | 监控当前没有完全保持预期副本同步的分区数量。 |
| Offline Partitions Count | 离线分区数 | 监控没有可用 Leader 的分区数量。 |
| Disk Utilization | 磁盘使用率 | Broker 日志数据占用存储容量的比例。 |

## 15 配置、管理工具与运维 · Configuration & Operations

| English | 中文 | 释义 |
|---|---|---|
| Admin API | 管理 API | 创建、删除、查询主题和其他 Kafka 资源的客户端接口。 |
| AdminClient | 管理客户端 | 实现 Kafka 管理 API 的客户端组件。 |
| server.properties | Broker 配置文件 | Kafka 服务端使用的典型属性配置文件名。 |
| bootstrap.servers | 引导地址配置 | 客户端启动时用于发现集群的 Broker 地址列表。 |
| acks | 写入确认参数 | 生产者确认策略配置：0、1 或 all 等。 |
| enable.idempotence | 启用幂等性 | 生产者控制重试去重能力的配置项。 |
| min.insync.replicas | 最小同步副本配置 | 与 acks=all 共同影响写入安全性和可用性。 |
| auto.offset.reset | 无效位置重置策略 | 规定没有有效已提交 Offset 时的初始消费位置。 |
| isolation.level | 隔离级别 | 可配置 read_uncommitted 或 read_committed。 |
| retention.ms | 日志保留时长配置 | 按时间控制旧数据清理的主题／Broker 参数。 |
| cleanup.policy | 清理策略配置 | 用于指定 delete、compact 或其组合。 |
| log.segment.bytes | 日志段大小配置 | 控制分区日志段滚动的典型参数。 |
| kafka-topics.sh | 主题管理命令 | 列出、创建、修改、描述和删除主题的 CLI。 |
| kafka-console-producer.sh | 命令行生产者 | 从终端输入或管道读取内容并向主题写入。 |
| kafka-console-consumer.sh | 命令行消费者 | 从主题读取记录并打印到终端。 |
| kafka-consumer-groups.sh | 消费者组管理命令 | 查询消费者组状态、成员及消费滞后等。 |
| kafka-configs.sh | 动态配置命令 | 管理部分可动态调整的 Broker、主题等配置。 |
| kafka-reassign-partitions.sh | 分区迁移命令 | 辅助执行和检查分区副本迁移。 |
| kafka-storage.sh | 存储初始化命令 | 格式化数据目录并设置 KRaft 存储元数据。 |
| kafka-metadata-quorum.sh | 元数据 Quorum 管理命令 | 检查和维护 KRaft 控制器法定多数状态。 |

## 16 生态组件与工程实践 · Ecosystem & Engineering Patterns

| English | 中文 | 释义 |
|---|---|---|
| Change Data Capture (CDC) | 变更数据捕获 | 从数据库日志等来源持续提取数据变更事件。 |
| Outbox Pattern | 事务发件箱模式 | 将业务数据库更新和待发布事件放在同一数据库事务中。 |
| Schema Registry | 模式注册中心 | 用于共享和演进事件 Schema 的外部服务类别。 |
| Avro | Avro 序列化格式 | 面向数据序列化及 Schema 演进的常见格式。 |
| Protocol Buffers | Protocol Buffers 数据格式 | 基于 .proto 定义的紧凑结构化消息格式。 |
| JSON Schema | JSON 模式 | 定义和验证 JSON 结构的 Schema 规范。 |
| Dead Letter Topic (DLT) | 死信主题 | 存放无法正常处理消息的专用 Kafka 主题。 |
| Replay | 重放 | 通过重设 Offset 重新读取历史事件。 |
| Event Sourcing | 事件溯源 | 以不可变业务事件重建领域对象状态的架构模式。 |
| CQRS | 命令查询职责分离 | 分离写入侧与读取侧数据模型的架构模式。 |
| MirrorMaker 2 | MirrorMaker 2 跨集群复制 | 基于 Connect 的 Kafka 集群之间数据复制工具。 |
| Cross-cluster Replication | 跨集群复制 | 在不同 Kafka 集群之间同步主题记录的过程。 |
| Data Contract | 数据契约 | 明确事件 Schema、语义、兼容性及生产消费责任的约定。 |
| Idempotent Consumer | 幂等消费者 | 重复处理同一事件也不会产生重复业务副作用的消费者。 |
| Poison Pill | 毒丸消息（非正式） | 持续触发下游解析或处理失败的异常记录。 |

---

生成日期：2026-11-16 · 本资料非 Apache Software Foundation 官方出版物。Apache Kafka 是 Apache Software Foundation 的商标。