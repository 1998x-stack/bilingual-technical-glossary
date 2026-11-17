# AI Agents · Batch 15 内部学习路径（281–300）

> 仅限编辑者，当前 281–290 为候审稿，291–300 仍为 planned，后续补齐。不属于公开独立 Wiki 导航。

## 第一阶段：攻击面与系统治理（281–285）

从功能、权限、自主性三维理解 Excessive Agency，延伸至 Supply Chain Attack、Tool Poisoning、Prompt Leakage 和 Denial of Wallet；用带预算与审批的工具链构建安全验证案例。

## 第二阶段：Agent 可观测性（286–290）

从 Observability → Tracing → Trace → Span → Distributed Tracing 建立跨模型与服务的执行关系；区分关键路径延迟、Span 总时长、真实业务提交和权限判定。

- [Excessive Agency（过度代理权限）](281-excessive-agency.md)
- [Supply Chain Attack（供应链攻击）](282-supply-chain-attack.md)
- [Tool Poisoning（工具投毒）](283-tool-poisoning.md)
- [Prompt Leakage（提示词泄漏）](284-prompt-leakage.md)
- [Denial of Wallet (DoW)（成本耗尽攻击）](285-denial-of-wallet.md)
- [Observability（可观测性）](286-observability.md)
- [Tracing（追踪）](287-tracing.md)
- [Trace（追踪记录）](288-trace.md)
- [Span（跨度）](289-span.md)
- [Distributed Tracing（分布式追踪）](290-distributed-tracing.md)

## 综合实践

构造从网页检索、模型推断到远程工具写入的 Agent，在没有真实敏感数据的隔离环境验证工具投毒、预算耗尽、traceparent 丢失、异步错误恢复。记录模型意图、执行器允许/拒绝、实际后置状态和成本。第 291–300 条的 Logging / Monitoring / Latency / Quota 等将在下一轮接入。
## 第二阶段补齐：291–300（候审稿）

完善日志、指标、结构化日志与跨组件关联，再衔接 Latency、Throughput、Concurrency、Parallelism、Rate Limiting、Quota。实践要求明确平均值与尾延迟、逻辑任务与重试调用、速率限制与配额的区别。

- [Logging（日志记录）](291-logging.md)
- [Metrics Monitoring（指标监控）](292-metrics-monitoring.md)
- [Structured Logging（结构化日志）](293-structured-logging.md)
- [Correlation ID（相关标识符）](294-correlation-id.md)
- [Latency（延迟）](295-latency.md)
- [Throughput（吞吐量）](296-throughput.md)
- [Concurrency（并发）](297-concurrency.md)
- [Parallelism（并行）](298-parallelism.md)
- [Rate Limiting（速率限制）](299-rate-limiting.md)
- [Quota（请求配额）](300-quota.md)
