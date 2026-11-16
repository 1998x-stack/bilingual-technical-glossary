# Object Storage（对象存储）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 以 Kubernetes 当前 API 与存储服务实际语义为准

## 1. 核心定义

对象存储（Object Storage）以 object 为基本数据单元，通常由 payload、系统/用户 metadata 和唯一 key 组成，并通过 bucket 与 HTTP API 管理。对象服务适合海量非结构化数据、模型权重、训练语料、checkpoint、日志与数据湖；它不等同于本地 POSIX 文件系统或可直接格式化的块设备。

## 2. 形象理解

像一个带唯一编号和标签的包裹仓库：每个包裹有内容、属性和对象编号，客户端按编号上传/读取，不需要知道包裹具体放在哪台磁盘或哪个机架。

## 3. 技术原理与核心内容

典型接口包含 PUT/GET/HEAD/LIST/DELETE、multipart upload、versioning、lifecycle、bucket policy 与 presigned URL。对象 key 通常是平面命名空间中的字符串，`a/b/c` 多为前缀约定，不一定是 POSIX 目录。底层可通过副本或 erasure coding 实现耐久性，元数据索引与对象数据路径分离。Amazon S3 在成功 PUT/DELETE 后提供强 read-after-write consistency，但这是 S3 的服务保证，不能推断所有 S3-compatible 实现都相同。

## 4. 工程实践与设计权衡

训练数据集可用不可变 manifest 与版本化 object key 固定样本清单；checkpoint 上传采用 multipart、checksum 和完成标记，防止任务读取半成品。大量小文件会增加请求与 list 开销，可打包为 shard（Parquet/WebDataset 等），训练时按顺序并行读取。用缓存/本地 NVMe 做热数据层，评估网络带宽、请求速率、跨区流量、对象大小分布、并发和一致性。

## 5. 易混概念与边界

对象存储按 object key/API 访问；块存储提供可寻址块设备；分布式文件系统提供目录、文件与 POSIX-like 接口。对象 key 前缀模拟目录不等于真正的文件系统 rename/locking 语义；服务商一致性、最大对象大小和费用需逐一核实。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么对象存储常适合大规模训练数据与 checkpoint？** 答：对象按 key 独立管理、可横向扩展并通过 HTTP API 并发访问，适合大文件和不可变数据集；通过 multipart、版本和生命周期可治理上传、回滚与成本。

2. **问：S3 强 read-after-write consistency 能否推广到任意 S3-compatible 服务？** 答：不能。Amazon S3 的一致性承诺是其服务特性，兼容 API 不自动保证相同实现语义；需查看具体供应商文档并测试 GET/LIST/overwrite 行为。

## 7. 中等难度考试题（含解析）

1. **题：训练数据 2.4TB，单对象 shard 设为 200GB，忽略尾部不足，至少需要多少对象？** 解：`ceil(2400/200)=**12 个对象**`（以十进制 GB 计）。

2. **题：对象 96GB，multipart 每 part 8GB，至少需要多少个 part？** 解：`96/8=**12 个 part**`；实际服务还会限制 part 数、最小 part 大小与最大对象大小。

## 8. 权威来源与延伸阅读

- [Amazon S3 Overview and Consistency](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)：用于核对服务保证、API 与架构边界的官方资料。
- [Ceph Object Gateway](https://docs.ceph.com/en/latest/radosgw/)：用于核对服务保证、API 与架构边界的官方资料。
- [Ceph Storage Architecture](https://docs.ceph.com/en/latest/architecture/)：用于核对服务保证、API 与架构边界的官方资料。

> 数值算例是明确假设下的教学推导，不构成生产集群性能或一致性承诺。
