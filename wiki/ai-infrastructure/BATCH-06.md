# AI 数据读写链路、SRE 服务目标与可观测性

> **内部研究与编辑路线。** 读者仍通过 TERM/ATLAS Explorer 的学科→术语→详情页访问，不显示批次、编辑台账或内部 PR 进度。

## 1. 从文件协议到实际吞吐

先理解 [Network File System](101-network-file-system.md) 的 RPC、租约与缓存一致性，再学习 [Parallel File System](102-parallel-file-system.md) 的 MDS/MDT 和 OST 条带布局。区分 [Storage Throughput](103-storage-throughput.md) 的字节/s 与 [IOPS](104-input-output-operations-per-second.md) 的操作/s，任何 benchmark 必须记录 block size、queue depth、数据冷热、随机/顺序与统计窗口。

## 2. 训练数据产品与 GPU 进料路径

[Data Lake](105-data-lake.md) 提供 raw/processed/curated 层、元数据目录和版本治理；[Data Pipeline](106-data-pipeline.md) 负责采集、验证、幂等变换与快照发布。[Data Shard](107-data-shard.md) 是逻辑样本分片，既要避免 worker 复制，也要兼顾文件大小；[Data Loader](108-data-loader.md) 提供采样、合批、worker、pinned memory；[Prefetching](109-prefetching.md) 把 I/O 与 GPU 计算重叠。[Cache Hit Rate](110-cache-hit-rate.md) 需区别请求/字节口径；[CDN](111-content-delivery-network.md) 需要正确的 key、TTL 与权限边界。

## 3. SRE 从指标到用户承诺

先定义 [SLI](113-service-level-indicator.md) 的好事件与分母，再设置 [SLO](112-service-level-objective.md) 的目标/窗口/错误预算，最后理解对外 [SLA](114-service-level-agreement.md) 的合同语义。对照 [Availability](115-availability.md) 与 [Reliability](116-reliability.md)：请求型可用率不能直接换成精确停机分钟数，也不能将平均故障间隔误当无故障保证。[MTBF](117-mean-time-between-failures.md) 和 [MTTR](118-mean-time-to-recovery.md) 应注明故障与修复的计时边界。

## 4. 打通运行时诊断证据

[Observability](119-observability.md) 串联 traces、logs、metrics 与 context propagation，[Metrics](120-metrics.md) 区分 Counter、Gauge、Histogram、Summary；跨实例 P99 不可直接算术平均。以一次 TTFT P99 激增为例，用 SLI 告警→指标维度→trace 阶段分解→logs 调度记录→恢复验证，形成可复现的 on-call runbook。

## 核心问题

1. 为什么 NFS lease 不是缓存一致性保证？Lustre 的 stripe count 增大为何可能适得其反？
2. 为什么 IO 吞吐、IOPS 与单请求 P99 延迟不能用一个数字表示？
3. DataLoader 的 prefetch_factor 与 worker 数如何影响预取内存？DDP 如何保证 shard 不重复？
4. 99.9% 请求成功率 SLO 为什么不能直接变成 28 天精确停机分钟数？
5. MTBF、MTTR、RTO、RPO 的统计单位与目标含义分别是什么？
6. 为什么不能平均每个 Pod 的 P99，或把 request_id 放入 Prometheus 高基数标签？

## 权威资料入口

- [NFSv4.1 RFC 8881](https://www.rfc-editor.org/rfc/rfc8881.html)
- [Lustre Operations Manual](https://doc.lustre.org/lustre_manual.pdf)
- [PyTorch DataLoader](https://docs.pytorch.org/docs/stable/data.html)
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Prometheus Metric Types](https://prometheus.io/docs/concepts/metric_types/)
- [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/)
