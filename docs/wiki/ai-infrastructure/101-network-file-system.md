# Network File System（网络文件系统 · NFS）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 协议与性能口径以官方版本及实测边界为准

## 1. 核心定义

网络文件系统（Network File System，NFS）是一组允许客户端经网络以文件/目录接口访问服务端共享存储的协议与实现。NFSv4 提供有状态的 open/lock、客户端身份、租约与 compound RPC；客户端可缓存数据/属性以减少往返，但必须按协议一致性规则处理共享写入。它不是共享块设备，也不保证任何部署都能像本地 NVMe 一样低延迟。

## 2. 形象理解

像多人共享远程资料室：查阅书页时可把副本暂存自己桌上，但有人修订后，何时能看到新版取决于缓存验证与文件协议；远程资料室的距离和通道拥塞也会影响翻页速度。

## 3. 技术原理与核心内容

客户端通过 NFS 操作访问服务器 namespace。NFSv4.1（RFC 8881）定义 session、open state、lock、lease、delegation 与重试/恢复语义；常用 RPC over TCP，实际 NFSv4.1 可支持 pNFS 布局，由元数据服务器协调客户端直接访问多个数据服务器。客户端 page cache 与 attribute cache 可显著提高重复读取，但共享写/rename/lock 的一致性应以协议与挂载配置为准。网络失败后的重试、server failover、硬/软挂载策略会改变可用性与应用的错误语义；租约续约本身**不是**缓存一致性协议。

## 4. 工程实践与设计权衡

AI 集群常用 NFS 共享小规模数据、脚本、checkpoint 元数据或用户 home；多节点同时顺序读取 TB 级训练 shard 时，单 server 的网络、磁盘和 RPC 并发可能成为瓶颈。测 p50/p99 read latency、metadata ops、读写吞吐、服务端 NIC 和缓存冷热差异，警惕单文件锁竞争与小文件风暴。容器挂载通过 Kubernetes PVC/CSI 与安全权限管理，确认 root_squash、UID/GID、跨租户数据隔离和故障重连。

## 5. 易混概念与边界

NFS 是网络共享**文件**协议，不是 iSCSI/RBD 类块协议；NFS server 可由 NAS 或分布式后端提供。pNFS 允许布局并行访问，不代表所有 NFS 挂载天然具有 Lustre 同等级并行条带能力。缓存命中可掩盖原始网络瓶颈，必须区分冷热测试。

## 6. 中等难度面试题（含参考答案）

1. **问：NFS 客户端看到旧文件内容，如何定位？** 答：确认 NFS 版本、属性/数据缓存、应用是否 close/reopen、服务端写入是否提交、是否由其它客户端并发改写；结合 GETATTR/OPEN 和服务端 trace 判定，而非笼统关闭全部缓存。

2. **问：为何 NFS lease 不等于“租约期间文件内容保证不变”？** 答：RFC 8881 的 client lease 保留锁等状态并处理客户端失联，并非缓存一致性保证。delegation 和一致性规则是另一套语义，应明确区分。

## 7. 中等难度考试题（含解析）

1. **题：文件 640GiB，经稳定 4GiB/s 有效吞吐连续读取，忽略缓存与元数据，理想最短耗时？** 解：`640/4=**160s**`；实际还受 RPC、客户端 CPU、服务器磁盘与并发影响。

2. **题：8 个 worker 各以 300MiB/s 从同一 NFS server 稳态读取，忽略协调开销，服务端出口至少需要多少 GiB/s？** 解：`8×300/1024≈**2.34GiB/s**`；若出口只有 2GiB/s，无法同时达到每 worker 300MiB/s。

## 8. 权威来源与延伸阅读

- [NFSv4.1 RFC 8881](https://www.rfc-editor.org/rfc/rfc8881.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Linux NFS documentation](https://docs.kernel.org/filesystems/nfs/index.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Kubernetes NFS volume](https://kubernetes.io/docs/concepts/storage/volumes/#nfs)：用于核对上述协议、性能口径或数据管理机制的一手资料。

> 数值示例均为题设下的简化计算，不是生产集群的真实性能指标。
