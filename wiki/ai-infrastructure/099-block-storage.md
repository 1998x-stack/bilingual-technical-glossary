# Block Storage（块存储）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 实际 API、feature gate 与存储语义须按产品版本确认

## 1. 核心定义

块存储（Block Storage）向主机或虚拟机提供可寻址的固定大小数据块设备，操作系统可在其上创建分区、文件系统或直接由数据库管理原始块。它适合低延迟随机读写、数据库数据目录、虚拟机磁盘与需要持久卷语义的工作负载；应用需要自己处理文件系统/事务一致性。

## 2. 形象理解

像把一块可独立挂载的硬盘交给主机：存储服务负责把指定逻辑块读写到可靠介质，主机自己决定如何格式化、建目录和管理文件。

## 3. 技术原理与核心内容

块设备通过 LBA/offset 与长度发起读写，服务端映射到分布式后端；性能常以 IOPS、吞吐量、平均/P99 latency、queue depth、block size 和读写比例描述。云块卷通常可独立于实例生命周期持久存在，支持 snapshot/clone/resize；Multi-Attach 能力与并发写语义因产品/文件系统而异。Ceph RBD 把 block image 映射为 RADOS 对象，并提供快照、克隆等能力。普通块卷快照未必应用一致：文件系统缓存和数据库日志需要 flush/quiesce 或应用协调。

## 4. 工程实践与设计权衡

模型 checkpoint、数据库索引或高随机 I/O cache 可使用块卷/PVC；训练共享数据要评估卷访问模式、CSI driver、zone binding、attach/detach 时间和多 Pod 并发写安全。基准测试固定块大小、随机/顺序模式、读写比例、queue depth、预热与数据集工作集；报告 IOPS、MiB/s 与 P99 latency，不能只报峰值吞吐。快照恢复需验证 crash-consistency、文件系统和应用恢复流程。

## 5. 易混概念与边界

块存储交付原始 block device；文件系统在其上提供文件/目录；分布式文件系统为多客户端提供共享命名空间；对象存储直接以 object API 管理数据。一个 RBD 卷可格式化为文件系统，但卷本身不是共享文件系统。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么块存储通常比对象存储更适合数据库随机读写？** 答：块设备提供 offset/block 级 I/O，数据库可控制页布局、日志和缓存，适合随机读写延迟敏感路径；对象 API 的请求/对象语义不等同原生块 I/O。

2. **问：同一个块卷能否安全地被多个 Pod 同时挂载并以普通 ext4 并发读写？** 答：通常不能简单这样做。单写者文件系统如普通 ext4 不支持多个主机无协调并发挂载；需要受支持的 Multi-Attach 语义与集群文件系统/应用协调。

## 7. 中等难度考试题（含解析）

1. **题：块存储卷提供 12,000 IOPS，每次 I/O 平均 16KiB，理论顺序数据吞吐量是多少 MiB/s？** 解：`12000×16KiB=192000KiB/s=**187.5MiB/s**`，忽略协议与设备限制。

2. **题：一个 2TiB 卷每小时完整顺序扫描一次，忽略缓存和重试，所需平均吞吐量约多少 MiB/s？** 解：`2×1024×1024 MiB / 3600s ≈ **582.5MiB/s**`。

## 8. 权威来源与延伸阅读

- [Amazon EBS Volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)：用于核对协议语义、架构与版本边界的官方文档。
- [Ceph RADOS Block Device](https://docs.ceph.com/en/latest/rbd/)：用于核对协议语义、架构与版本边界的官方文档。
- [Ceph RBD Snapshots](https://docs.ceph.com/en/latest/rbd/rbd-snapshot/)：用于核对协议语义、架构与版本边界的官方文档。

> 数值算例是简化教学推导；不构成真实存储集群的吞吐、耐久性或可用性承诺。
