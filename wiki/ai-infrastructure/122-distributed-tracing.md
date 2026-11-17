# Distributed Tracing（分布式链路追踪）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 请按实际版本与观测口径核对技术边界

## 1. 核心定义

分布式链路追踪（Distributed Tracing）通过为一个端到端操作关联多个跨进程的 span，展示调用依赖、时间区间、错误和上下文，帮助定位跨网关、推理引擎、KV 传输与存储系统的长尾延迟。Trace 不是完整的系统调用录像：采样、异步边界、未埋点组件和时钟漂移都可能导致视图不完整。

## 2. 形象理解

快递包裹跨多个转运中心，每到一站记录扫描时间和车次。将所有扫描归到同一个包裹 ID，就能发现最长的等待发生在哪站，而只看某个城市的平均运输速度很难定位。

## 3. 技术原理与核心内容

W3C Trace Context 使用 `traceparent`、`tracestate` 传播追踪上下文；OpenTelemetry 中 trace 含多个 span，span 带 trace_id、span_id、parent/span links、name、attributes、events、status、start/end。父子关系支持调用路径，异步消息队列可通过 span links 关联不严格父子结构。Head-based sampling 提前决定是否留存，tail sampling 在收集更完整结果后按错误/延迟选择但有内存与延迟开销。跨度相加会在并行调用时双计，端到端 latency 应按关键路径或实际时间戳计算。

## 4. 工程实践与设计权衡

LLM 服务在 ingress、鉴权、tokenization、scheduler queue、prefill、首 decode、KV transfer 和 SSE flush 形成 spans；使用 model version、GPU pool、cache hit、request length 等有限属性。观测 trace 需与客户端 TTFT 时间戳对齐，确保 UTC/monotonic clock 边界；对包含 prompt、用户身份或密钥的 attributes 做脱敏。采样后的 traces 不应直接用来准确推算线上全量 P99，配合 histogram 与 SLO counter。

## 5. 易混概念与边界

Trace 是一次请求的跨组件链路，Log 是离散事件，Metric 是聚合测量。Span duration 不能简单全部相加，因为有重叠和并行；多个请求共用 batch 时也不应强行把整个 GPU kernel 归属到一个用户。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么所有 span 耗时相加往往大于客户端真实响应时间？** 答：父子 span、同级并发和重叠执行会重复计算相同墙钟时间；应重建关键路径并核对各服务时钟。

2. **问：如何追踪异步任务队列中消费端与生产端的关联？** 答：透传 W3C context，若跨批处理/异步消费不符合单父子模型可用 span links，并保留稳定业务 operation_id；明确重试与多次投递关系。

## 7. 中等难度考试题（含解析）

1. **题：请求总 180ms，两个子调用并行持续 80ms 与 120ms，忽略其它开销，并行区段墙钟最短时长？** 解：`max(80,120)=**120ms**`，不是 200ms；180ms 端到端仍包含其他阶段。

2. **题：每秒 20,000 请求，以固定独立 5% head sampling 采集，期望每秒保留多少条 trace？** 解：`20000×0.05=**1000 traces/s**`，并不保证尾部异常都被抽中。

## 8. 权威来源与延伸阅读

- [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)：可核查对应的原始规范、维护者文档及其版本。
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)：可核查对应的原始规范、维护者文档及其版本。
- [OpenTelemetry Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)：可核查对应的原始规范、维护者文档及其版本。

> 例题计算使用明确假设，不是实际集群的压测或财务成本报告。
