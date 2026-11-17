# Storage Throughput（存储吞吐量）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 协议与性能口径以官方版本及实测边界为准

## 1. 核心定义

存储吞吐量（Storage Throughput）是某个时间窗内成功传输的数据字节数除以秒数，常分别统计读取/写入、单客户端/聚合、逻辑字节/物理字节以及持续/峰值速率。常见单位 MB/s（10^6）和 MiB/s（2^20），二者不可混用；高吞吐不代表小随机 I/O 时延低。

## 2. 形象理解

像水管每秒运输多少升水，是水流总量指标；拧开水龙头到第一滴水需要多久是延迟，管道每秒开关多少次则更接近 IOPS。大流量不能独立说明每个请求都快。

## 3. 技术原理与核心内容

设区间 `T` 秒、实际已完成逻辑读字节 `B_read`、写字节 `B_write`，则 `read_throughput=B_read/T`、`write_throughput=B_write/T`。I/O size、queue depth、随机/顺序比例影响能达到的吞吐；简化情况下 `吞吐≈IOPS×平均请求大小`，但需要同窗口、相同读写类型和已完成请求统计。压缩、去重、纠删码会使应用有效字节与设备物理字节不同；Linux page cache 命中可能把“应用读吞吐”误认成远程存储带宽。

## 4. 工程实践与设计权衡

训练数据读取可分别报告文件系统 backend、DataLoader、PCIe Host→GPU 三段的 MiB/s 与 step 读取时长。用 fio 和训练实流量在统一 block size/qd/numjobs 下测稳态，区分 warmed page cache 与 drop-caches 的冷读。对于分布式训练，还需监控 storage NIC、单 OST/OSS 热点、metadata latency 与 GPU idle wait；提升存储吞吐必须最终减少 GPU pipeline stall 才有业务意义。

## 5. 易混概念与边界

Throughput 按字节量度，IOPS 按操作次数量度，latency 按单次响应时间量度。文件系统观察到的速率可能包含缓存，而磁盘/网络设备实际发送量不同。MB/s 与 MiB/s 相差约 4.86%。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 fio 显示 12GiB/s，但远程存储网卡只有 1GiB/s？** 答：可能测试数据命中 Linux page cache、客户端 SSD 缓存或计数处于不同层级。要核对 direct I/O、工作集大小和服务端实际字节计数。

2. **问：为什么增大 block size 会提高 MB/s 却降低 IOPS？** 答：每次 I/O 搬运更多字节、固定事务开销相对减少；设备可能单位时间完成更少操作，但单位秒数据量更大。

## 7. 中等难度考试题（含解析）

1. **题：10 秒内完成读取 80GiB 数据，平均应用读吞吐是多少 GiB/s？** 解：`80/10=**8GiB/s**`；不能由此断言全量数据来自后端物理磁盘。

2. **题：设备完成 25,000 IOPS，平均 I/O 大小 32KiB，求理想数据吞吐 MiB/s。** 解：`25000×32/1024=**781.25MiB/s**`，前提是所有 I/O 都按此大小成功完成。

## 8. 权威来源与延伸阅读

- [Linux fio documentation](https://fio.readthedocs.io/en/latest/fio_doc.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Ceph performance benchmark guidance](https://docs.ceph.com/en/latest/rados/operations/monitoring/)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Lustre manual performance guidance](https://doc.lustre.org/lustre_manual.pdf)：用于核对上述协议、性能口径或数据管理机制的一手资料。

> 数值示例均为题设下的简化计算，不是生产集群的真实性能指标。
