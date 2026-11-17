# AI Infrastructure：观测、韧性与 GPU 成本治理

> **内部编辑研究路线**，不放入 `docs/` 的公开生产导航。完整 Wiki 仍从 TERM/ATLAS Explorer 术语详情页阅读。

## 可观测性：从一次请求到跨集群诊断

[Logs](121-logs.md)、[Distributed Tracing](122-distributed-tracing.md) 和 [OpenTelemetry](123-opentelemetry.md) 分别强调记录事件、跨进程 span 因果与统一的遥测协议/Collector；[Prometheus](124-prometheus.md) 负责 scrape/TSDB/PromQL，[Grafana](125-grafana.md) 负责跨源可视化。链接 [Alerting](126-alerting.md) 的 Alertmanager 分组、去重、抑制、silence 以及 SLO burn-rate 告警，避免把所有 CPU 高负载变成值班紧急通知。

## 可靠性工程：实验要可控

[Load Testing](127-load-testing.md) 区分开放环与闭环负载和 coordinated omission，严格报告 TTFT、ITL、成功 goodput 与失效；[Chaos Engineering](128-chaos-engineering.md) 则在批准、故障半径、恢复与停止条件约束下验证跨节点/存储/网络韧性。

## 资金与资产：定义成本分母

[Total Cost of Ownership](129-total-cost-of-ownership.md) 分析完整生命周期；[Capital Expenditure](130-capital-expenditure.md) 与 [Operating Expenditure](131-operating-expenditure.md) 不等同于一次性现金流或每月账单的简单分类。[Cost per Million Tokens](136-cost-per-million-tokens.md) 用有效输出/输入/请求定义单位经济性，必须附 SLO 与模型质量约束。

## 硬件指标与有效工作

[GPU Utilization](132-gpu-utilization.md) 的 busy ratio 不等于 FLOPs 利用率；[GPU Memory Utilization](133-gpu-memory-utilization.md) 的已用容量与内存控制器忙碌率不是同一个指标；[Compute Efficiency](134-compute-efficiency.md) 可用 MFU 或 SLO goodput 说明有效计算效率；[Energy per Token](135-energy-per-token.md) 必须说明 GPU/节点/机房与输入/输出 token 的边界。

## 排程与租户

[Workload Consolidation](137-workload-consolidation.md) 混部时需要避免 GPU KV OOM 与延迟长尾；[Multi-Tenancy](138-multi-tenancy.md) 需要 RBAC、网络、存储、KV cache 和硬件隔离；[Capacity Planning](139-capacity-planning.md) 以峰值 goodput、故障余量与 GPU 获取提前期做规划；[Autoscaling](140-autoscaling.md) 把短期应用副本扩容和节点/硬件供给链路分开。

## 专业审稿重点

1. Metrics 与 logs/traces 中是否存在高基数或敏感字段？
2. GPU busy、FB used、memory activity、MFU 是否混写？
3. P99 / error budget 和 goodput 是否属于同一请求集合与窗口？
4. Unit cost 是否把 input 与 output token 混合且遗漏闲置成本？
5. 混沌实验是否定义 blast radius、审批和自动终止条件？

## 原始资料

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/)
- [Prometheus concepts](https://prometheus.io/docs/introduction/overview/)
- [NVIDIA DCGM reference](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html)
- [FinOps unit economics](https://www.finops.org/framework/capabilities/unit-economics/)
