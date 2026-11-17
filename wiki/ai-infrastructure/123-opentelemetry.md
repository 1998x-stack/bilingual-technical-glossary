# OpenTelemetry（开放遥测 · OTel）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 请按实际版本与观测口径核对技术边界

## 1. 核心定义

OpenTelemetry（OTel，开放遥测）是一套厂商中立的可观测性 API、SDK、语义约定、传输协议和 Collector 生态，用于生成、处理与输出 traces、metrics、logs 等信号。它**不是**时序数据库、日志检索引擎或完整 UI；应用可通过 OTLP 把遥测送往不同后端，具体稳定性与语言支持随信号、SDK 和版本而变化。

## 2. 形象理解

像给各种设备规定统一测量接口与运输箱格式：不同厂家都可以把读数按共同约定装箱，途中能过滤、聚合、转发；最终仪表板和长期存储仍由另一套系统完成。

## 3. 技术原理与核心内容

Instrumentation（自动/手工）通过 API 与 SDK 创建 Span、Metric instruments、Logs；Resource 描述服务名/版本、环境等属性，Instrumentation Scope 标识埋点来源；Semantic Conventions 规范 HTTP、DB 等字段。Collector 由 receivers、processors、exporters、connectors 组成 pipelines，可作为 agent 或 gateway；OTLP 有 gRPC/HTTP 形式。Baggage/trace context 跨请求传播需要控制边界，不能不加校验地信任客户端可注入属性。Collector 可能发生排队丢失、导出重试和高基数字段导致成本增长。

## 4. 工程实践与设计权衡

推理集群先建立服务命名和低基数维度，SDK 记录 request SLI histograms 与 traces，再由 Collector 批处理、限内存、删敏感字段、转发到 Prometheus/Tempo/Jaeger/日志后端；检查 exporter queue、dropped_spans 与 sampling policy。多进程 Python Worker 和跨池 prefill/decode 的 Context 传播尤其需实测，不能认为自动埋点覆盖所有 CUDA kernel 或远程 KV 传输。

## 5. 易混概念与边界

OpenTelemetry 是数据生成/采集标准与工具集，Prometheus 是 Metrics 存储和查询生态，Grafana 是可视化与告警平台。OTLP 是传输协议，不等于所有 OpenTelemetry SDK 生成的数据都永久存放在 Collector 中。

## 6. 中等难度面试题（含参考答案）

1. **问：为何部署了 OpenTelemetry Collector 不等于能查询历史 trace？** 答：Collector 通常负责接收、处理与导出，需要配置持久存储/trace backend 与查询 UI；否则 Collector 本身并不是完整的历史查询系统。

2. **问：OpenTelemetry Resource 与 Span Attributes 有何区别？** 答：Resource 描述产生数据的实体（如 service.name、deployment.environment），Span attributes 描述具体操作；将每次请求 ID 放入 Resource 可能扩大序列基数。

## 7. 中等难度考试题（含解析）

1. **题：某服务生成 80,000 spans/s，Collector 保留 25%，每秒向后端导出多少期望 spans？** 解：`80000×0.25=**20000 spans/s**`；忽略队列溢出和重试。

2. **题：每条遥测记录原始 500B，导出 20,000 条/s，持续 10s 未压缩体积？** 解：`500×20000×10=**100MB**`（十进制），不含传输协议开销。

## 8. 权威来源与延伸阅读

- [OpenTelemetry Concepts](https://opentelemetry.io/docs/concepts/)：可核查对应的原始规范、维护者文档及其版本。
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)：可核查对应的原始规范、维护者文档及其版本。
- [OTLP Specification](https://opentelemetry.io/docs/specs/otlp/)：可核查对应的原始规范、维护者文档及其版本。

> 例题计算使用明确假设，不是实际集群的压测或财务成本报告。
