# Distributed File System（分布式文件系统 · DFS）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 实际 API、feature gate 与存储语义须按产品版本确认

## 1. 核心定义

分布式文件系统（Distributed File System，DFS）通过网络把多个存储节点组织为一个文件/目录命名空间，让客户端像访问文件系统一样访问跨机器数据。它通常将元数据管理与数据块/对象存储路径分开，并通过副本、纠删码、缓存、租约或锁等机制提供可用性和并发语义。不同 DFS 对 POSIX 兼容性、写入一致性与故障恢复保证差异很大。

## 2. 形象理解

像一个跨多栋仓库的统一图书馆：读者看到一套目录和书名，目录服务告诉客户端数据在哪些仓库，客户端再从合适节点读取书页。目录服务和数据节点分别扩展，也分别可能成为瓶颈。

## 3. 技术原理与核心内容

HDFS 采用 NameNode 管理 namespace 与 block 元数据，DataNode 存储数据 block；客户端先向 NameNode 获取 block locations，再直接与 DataNode 传输数据。NameNode 通过 heartbeat/block report 监控节点，按 replication factor 与 rack awareness 管理副本。CephFS 则在 RADOS 上提供 POSIX 文件接口：MDS 管理目录/inode 元数据，客户端可直接访问 RADOS 读写文件数据。两种架构都把 metadata/control 与 data path 分离，但故障模型、缓存一致性和写入语义不同。

## 4. 工程实践与设计权衡

AI 训练选择 DFS 时，测试数据集文件数量、平均文件大小、metadata ops/s、并发 reader 数、顺序/随机访问、跨机架流量、缓存命中和小文件负载。HDFS 擅长大文件流式扫描与数据本地性，但大量小文件会压迫 NameNode metadata；CephFS 提供 POSIX 语义和共享目录，需评估 MDS 与客户端缓存。训练数据常需打包 shard、预取到本地 NVMe，避免每个 step 都被远程 metadata 和网络 I/O 限制。

## 5. 易混概念与边界

DFS 提供文件与目录接口；对象存储通过 bucket/key API；块存储提供原始设备。HDFS 的 block 是文件系统内部的数据分片，不等于用户可直接挂载的 block device；CephFS 的数据落在 RADOS 对象存储上，但其客户端接口仍是文件系统。

## 6. 中等难度面试题（含参考答案）

1. **问：HDFS NameNode 与 DataNode 的职责如何分工？** 答：NameNode 维护文件系统 namespace、文件到 block 的映射和副本调度元数据；DataNode 保存实际 block 数据并响应客户端数据读写。

2. **问：为什么 AI 训练数据集包含数百万个小文件时，DFS 可能遇到 metadata 瓶颈？** 答：每个文件/目录都需元数据创建、查询、权限和缓存管理，元数据请求量可能远高于数据字节吞吐；打包成较大的 shard 能减少 metadata ops。

## 7. 中等难度考试题（含解析）

1. **题：一个 HDFS 文件大小 1.2TiB，block size=256MiB，忽略最后一块不足，需多少 block？** 解：`1.2×1024×1024/256=**4915.2**`，向上取整需 **4916 blocks**。

2. **题：文件数据块共 120TiB，replication factor=3，忽略元数据与压缩，理论原始存储占用多少？** 解：`120×3=**360TiB**`；若使用 erasure coding，物理开销计算方式不同。

## 8. 权威来源与延伸阅读

- [Apache Hadoop HDFS Architecture](https://hadoop.apache.org/docs/r3.4.3/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)：用于核对协议语义、架构与版本边界的官方文档。
- [CephFS Architecture](https://docs.ceph.com/en/latest/cephfs/)：用于核对协议语义、架构与版本边界的官方文档。
- [Ceph Architecture: RADOS and Clients](https://docs.ceph.com/en/latest/architecture/)：用于核对协议语义、架构与版本边界的官方文档。

> 数值算例是简化教学推导；不构成真实存储集群的吞吐、耐久性或可用性承诺。
