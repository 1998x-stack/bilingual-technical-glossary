# Observability（可观测性）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 时间窗口、请求单位及故障定义须注明

## 1. 核心定义

可观测性（Observability）是依据系统向外输出的遥测数据推断内部状态、探索未知异常并验证因果假设的能力。云原生软件常依赖 metrics、logs、traces 三类主信号；OpenTelemetry 也定义 baggage、context propagation，并支持后续的 profiles/events。可观测性不等于日志量越大越好，而是能够把数据与真实用户问题联系起来。

## 2. 形象理解

像医生综合体温、问诊记录与检查影像来判断病因；一个指标告诉你哪里异常，细节记录和请求流转路径才能推断异常如何发生。

## 3. 技术原理与核心内容

Metrics 提供 counters/gauges/histograms 监测 TTFT、GPU 利用率、queue depth；logs 记录离散的错误、调度决策和异常上下文；distributed traces 通过 trace_id/span_id 串联网关、tokenizer、prefill、decode、存储与网络调用。上下文传播需要跨服务保留关联标识，时间同步、采样、隐私脱敏、OTLP collector 背压和标签 cardinality 都影响诊断质量。不能把无限增长的 request_id 当作 Prometheus metric label；应存于 traces/logs 或 exemplars。

## 4. 工程实践与设计权衡

线上排查 TTFT P99 暴涨时，先用 metrics 找到模型/区域/时间窗，再选 traces 分解排队、预填充和首包发送阶段，用 logs 查看 KV preemption、cache miss 或网络故障。训练侧将 DCGM GPU、NCCL、DataLoader、K8s events 与 checkpoint logs 对齐；对 prompt/用户身份先脱敏并建立留存期限和访问控制，防止可观测平台形成新的隐私风险。

## 5. 易混概念与边界

监控更侧重预定义告警；可观测性强调探索未知故障并把跨层证据链接起来。Traces 不是用于准确估算所有请求的分位数，metrics histogram 更适合聚合统计；收集数据也不自动提升可靠性，必须有响应闭环。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不建议把 request_id 作为 Prometheus 标签？** 答：每次请求一个新值会使时间序列数爆炸，增加内存、索引和查询成本。用 traces/logs 存 ID 并通过 exemplars 关联汇总指标。

2. **问：TTFT P99 飙升，三个信号分别起什么作用？** 答：Metrics 找出尾部波动与受影响维度，traces 展示跨服务阶段时间线，logs 记录调度、缓存或网络事件细节。

## 7. 中等难度考试题（含解析）

1. **题：1亿请求按独立均匀0.1%采样，期望 trace 数？** 解：`100000000×0.001=**100000**` 条；这不保证每个尾部故障被采到。

2. **题：每分钟500MiB日志，连续24h不压缩，存储占用约多少 TiB？** 解：`500×60×24/1048576≈**0.6866TiB**`，未含索引、元数据与副本。

## 8. 权威来源与延伸阅读

- [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/)：原始资料用于核对相关定义、假设与系统实践。
- [OpenTelemetry Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)：原始资料用于核对相关定义、假设与系统实践。
- [Prometheus Instrumentation](https://prometheus.io/docs/practices/instrumentation/)：原始资料用于核对相关定义、假设与系统实践。

> 例题仅用于理解公式，不是对任何线上系统可靠性的审定。
