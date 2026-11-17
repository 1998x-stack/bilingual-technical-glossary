# Parallel File System（并行文件系统）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 协议与性能口径以官方版本及实测边界为准

## 1. 核心定义

并行文件系统（Parallel File System）在多客户端与多存储服务器之间分散文件数据或元数据操作，允许大文件的不同条带（stripe）由多个存储目标并行提供，追求高聚合带宽和高并发 I/O。典型系统包括 Lustre、IBM Storage Scale（GPFS）与 BeeGFS；不同产品的缓存一致性、锁、容错与条带粒度不应混同。

## 2. 形象理解

像一本巨型图册按章节分放到多个阅览室，读者可同时向多个房间领取不同页，避免所有人排在一个服务窗口；但要先定位章节，过小文件可能花更多时间在查目录和往返上。

## 3. 技术原理与核心内容

以 Lustre 为例，MDS/MDT 管 metadata，OSS/OST 提供文件数据；客户端根据文件 layout 将 stripe 按 stripe size/count 分布到多个 OST，并发 I/O 可绕开单 data server 的带宽上限。条带太少可能无法充分利用并行通道，太多则提高元数据、RPC、锁和网络放大成本。多个 I/O 进程对大文件按不重叠 offset 并行读取，与多个 GPU 同时读同一条训练数据不是等价问题；每层网络与客户端 page cache 仍可能限制有效带宽。

## 4. 工程实践与设计权衡

大模型训练应按 shard 规模、并行节点数、batch data loader 读模式配置条带；用顺序吞吐、随机 IOPS、metadata create/open/s、p95 延迟、OSS/OST 热点和单客户端/集群总带宽做冷热压测。海量小文件需要打包成 tar/WebDataset 或 Parquet shard；专用 GPU 训练集群还要关注 RDMA/网络拓扑、权限、容灾副本和监控。不能根据理论 OST 数量线性外推实际带宽。

## 5. 易混概念与边界

并行文件系统强调**多存储目标同时服务数据路径**；普通 NFS 可扩展为多服务器但并非默认分布条带；对象存储提供 object API 而非通用 POSIX 路径。文件的 stripe count 不等于副本数：Lustre 的数据镜像/冗余需另配置。

## 6. 中等难度面试题（含参考答案）

1. **问：Lustre 大文件只有一个 OST 热点，优先检查哪些参数？** 答：检查文件实际 stripe_count/stripe_size、OST 分布、客户端并行请求、网络带宽与后端磁盘；仅增加客户端 worker 不会自动改变已建文件的 layout。

2. **问：为什么把所有小文件设为 100 个 OST 条带可能更慢？** 答：每个文件可能增加 layout/metadata、RPC 和锁开销，远超过少量数据的实际传输工作。应按文件大小选用尽可能少且满足吞吐的条带。

## 7. 中等难度考试题（含解析）

1. **题：4 个 OST 各能稳定提供 1.5GiB/s，忽略其它瓶颈并均匀条带，单文件理论带宽上界？** 解：`4×1.5=**6GiB/s**`；实际受网络、客户端、锁和 layout 限制。

2. **题：48GiB 文件以 6GiB/s 理想速度读取，至少需要多少秒？** 解：`48/6=**8s**`，前提是一直保持满带宽且没有 I/O 准备开销。

## 8. 权威来源与延伸阅读

- [Lustre operations manual](https://doc.lustre.org/lustre_manual.pdf)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Lustre Architecture](https://wiki.lustre.org/Lustre_Architecture_for_Admins)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [BeeGFS Documentation](https://doc.beegfs.io/latest/)：用于核对上述协议、性能口径或数据管理机制的一手资料。

> 数值示例均为题设下的简化计算，不是生产集群的真实性能指标。
