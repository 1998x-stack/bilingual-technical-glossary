# Input/Output Operations per Second（每秒输入输出操作数 · IOPS）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 协议与性能口径以官方版本及实测边界为准

## 1. 核心定义

每秒输入输出操作数（Input/Output Operations per Second，IOPS）描述存储系统单位秒内完成的 I/O 操作次数，通常分别列出 read/write、随机/顺序与 block size。IOPS 是事务完成速率，不包含数据量大小信息；比较 IOPS 前须固定 I/O size、queue depth、读写比例、工作集和延迟分位。

## 2. 形象理解

像售票处每秒处理几张票：一张票可能只含一个座位，也可能关联一整个团，售票张数不等于服务的总人数。IOPS 数操作，吞吐量数这些操作累计传输了多少数据。

## 3. 技术原理与核心内容

若窗口 T 内完成 N 次请求，`IOPS=N/T`；若平均每次成功读/写 S 字节，`throughput≈IOPS×S`。一个未被充分并行化的队列可以用 Little 定律估算 `平均在途 I/O≈IOPS×平均 I/O latency(s)`；但需保证稳态、统计边界一致。QD=1 随机读的 IOPS 上限更接近单 I/O latency 的倒数，提升 QD 可能提高吞吐并拉高 tail latency，不能把厂商 QD=128 的峰值宣传为单请求速度。

## 4. 工程实践与设计权衡

数据库/训练 metadata 压测分别测 4KiB random read/write 与 1MiB sequential，给出 fio `iodepth`、jobs、direct、runtime、warmup、P99 latency 和磁盘使用率。云块存储与节点本地 NVMe 的峰值限制、burst credits、共享宿主噪声和网络可能明显不同。大量小文件会触发 open/stat/list 等 metadata ops，它们与块级 IOPS 是相关但不同的计数口径。

## 5. 易混概念与边界

IOPS 与吞吐之间可以通过 I/O 大小换算，却不能在未给定 size 的情况下比较。队列深度是平均或瞬时在途请求数，不是 IOPS；读写混合的 P95 时延不能直接相加，分布需要按请求集合合并。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 NVMe 在 QD=64 达到 500k IOPS，但单线程 DB 查询仍慢？** 答：QD=64 依赖大量并行在途请求；单次 DB 查询可能同步读、事务锁和 CPU 路径占主导。要测该查询对应的低 QD latency 而非仅设备峰值。

2. **问：如何区分存储系统瓶颈与应用数据处理瓶颈？** 答：对比应用发出的 IOPS、后端实际完成 IOPS、各级排队与 latency，附上 CPU 解码/反序列化和 GPU waiting；后端未饱和且应用 CPU 高可能是上层瓶颈。

## 7. 中等难度考试题（含解析）

1. **题：设备 40 秒完成 1,200,000 次 I/O，平均 IOPS 是多少？** 解：`1200000/40=**30000 IOPS**`。

2. **题：稳定 10,000 IOPS，平均 I/O latency=4ms，在稳态且边界一致条件下平均在途请求数？** 解：`L=10000×0.004=**40 个**`；不能由平均值推断 P99 queue depth。

## 8. 权威来源与延伸阅读

- [fio documentation](https://fio.readthedocs.io/en/latest/fio_doc.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Linux block layer docs](https://docs.kernel.org/block/index.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Amazon EBS performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-io-characteristics.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。

> 数值示例均为题设下的简化计算，不是生产集群的真实性能指标。
