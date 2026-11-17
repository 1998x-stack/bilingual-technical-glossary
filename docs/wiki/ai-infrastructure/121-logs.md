# Logs（日志）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 请按实际版本与观测口径核对技术边界

## 1. 核心定义

日志（Logs）是软件或基础设施产生的离散事件记录，通常带事件发生时间、严重度、来源、消息体与上下文字段。结构化日志具稳定字段/类型语义，便于检索、聚合和与 traces 关联；仅把任意文本序列化成 JSON 不保证语义结构化。日志记录的是事件，不应被当作准确的全量用户请求速率或延迟直方图。

## 2. 形象理解

像飞机黑匣子的事件记录：每次异常、模式切换和人工操作都有时间与背景。只有“飞机有问题”这种一句话难以诊断，而记录部件、时间、错误码和关联飞行编号才可与仪表读数联查。

## 3. 技术原理与核心内容

OpenTelemetry LogRecord 包含 Timestamp/ObservedTimestamp、SeverityText/Number、Body、Resource、Attributes，可能带 TraceId、SpanId。应用使用 JSON schema 或 OTLP logs，经 SDK/Collector receiver、processor、exporter 发送后端。日志时间通常来自多台机器，应校时并保留源时钟与采集时钟区别；异步队列的丢失、重复和乱序需要监测。异常堆栈、tokenizer 失败、GPU Xid、KV 抢占和路由决策应使用可查询字段；prompt、token 和 Authorization header 属敏感数据，需脱敏、权限控制和保留期限。

## 4. 工程实践与设计权衡

LLM API 日志可采用 `event_name, service, model_version, request_id, trace_id, error_code, stage, duration_ms` schema，通过 request_id 与 trace/span 关联；避免在生产 INFO 级别输出原始用户提示词。设计分级采样、降噪、压缩、索引生命周期和成本预算，记录日志丢弃 counter。高流量事件以 metrics counter/histogram 聚合，异常细节才写日志，防止每 token 打一条日志拖慢推理。

## 5. 易混概念与边界

日志记录离散事件，Metrics 是聚合数值时间序列，Traces 展示跨服务请求的 span 因果/时间关系。日志级别 WARN/ERROR 不等同 SLO 故障严重度；后端日志丢失不代表事件从未发生。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么“有效 JSON”仍可能不是可靠的结构化日志？** 答：同一字段时而是字符串时而是数组、缺少稳定 event_name 或时间单位，后端仍难以解析聚合；需要正式 schema 和字段类型约束。

2. **问：如何在追踪某个请求的同时避免 Prometheus 高基数？** 答：在日志/trace 中保留 request_id、trace_id，Metrics 使用低基数 model、region、status；通过 exemplars 或查询链路关联，而非把每个 request_id 变成 metric label。

## 7. 中等难度考试题（含解析）

1. **题：每秒 5,000 条日志、每条压缩前平均 600B，持续 1 小时原始数据量约多少 GB（十进制）？** 解：`5000×600×3600/10^9=**10.8 GB**`，不含索引、复制和压缩。

2. **题：某日志管道 100,000 条事件中丢弃 250 条，丢失率？** 解：`250/100000=**0.25%**`。该数字应与应用日志事件总数边界一致。

## 8. 权威来源与延伸阅读

- [OpenTelemetry Logs](https://opentelemetry.io/docs/concepts/signals/logs/)：可核查对应的原始规范、维护者文档及其版本。
- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)：可核查对应的原始规范、维护者文档及其版本。
- [Google SRE Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)：可核查对应的原始规范、维护者文档及其版本。

> 例题计算使用明确假设，不是实际集群的压测或财务成本报告。
