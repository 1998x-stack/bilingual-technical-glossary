# Service Level Indicator（服务级别指标 · SLI）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 服务边界、窗口和用户可见性必须明确

## 1. 核心定义

服务级别指标（Service Level Indicator，SLI）是对服务表现某一维度的**可重复测量定义**。常见包括请求成功比例、低于阈值的延迟比例、数据新鲜度和正确结果比例。一个可操作的 SLI 必须指定事件集合、好事件判定、数据采集点、窗口和聚合方式；SLI 是实测值与定义，不是“目标是多少”。

## 2. 形象理解

像考试评分规则：先明确哪类题目纳入测评、正确标准是什么，才能计算得分率。得分率本身是指标；要求至少 95 分是 SLO，而不达标的奖惩属于合同/管理政策。

## 3. 技术原理与核心内容

比率类 SLI 可定义为 `good / valid`，其中 valid 是用户真正会感知的合格事件；例如成功返回且 E2E<2s 的请求同时满足功能与延迟条件。若将 HTTP 499/429、用户取消或健康检查排除，需要有明确业务规则。可用客户端 synthetic probe、ingress/mesh 观察、服务端指标或 RUM 收集，不同观测点会产生网络与重试边界差异。对于延迟 SLI，统计请求级阈值达标比例通常比只观察聚合平均值更稳健。

## 4. 工程实践与设计权衡

AI 服务建议按请求模型、区域、输入/输出长度分桶定义 TTFT 和完成时延 SLI，再把“有效响应”的错误语义纳入；使用 OpenTelemetry trace/metrics、Prometheus counters 建立同口径 numerator/denominator。避免一条请求的多个流式 token 被算成多个独立成功请求；测试流量/内部探针通常与真实客户流量分开。

## 5. 易混概念与边界

SLI 是测量定义与实际数值，SLO 是该测量值应达到的目标；低层 GPU metrics 是诊断指标，除非与用户体验直接映射，否则不应代替 SLI。P99 latency 与阈值达标率是两种不同统计方式，不能无条件等价。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么把 5xx 比例作为唯一 SLI 可能漏掉故障？** 答：成功 HTTP 状态仍可能返回业务错误、空响应或长时间阻塞；应在 good event 判定中包括内容正确性、完整流式完成及延迟。

2. **问：用请求级比例 SLI 时，如何避免多次重试造成分母虚高？** 答：明确是每次 HTTP 尝试还是最终用户操作，并用稳定 request/operation ID 关联重试；根据 SLO 用户体验口径选择同一单位计数。

## 7. 中等难度考试题（含解析）

1. **题：总 50,000 次有效请求中，48,750 次在 1s 内成功完成，阈值型 SLI 数值？** 解：`48750/50000=**97.5%**`。

2. **题：系统内 1,000 次 HTTP 成功里有 50 次返回空内容，业务要求非空才算好事件，业务成功 SLI？** 解：好事件 `1000−50=950`，SLI=**95%**；若还有超时请求，应进入统一分母另算。

## 8. 权威来源与延伸阅读

- [Google SRE Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)：用于核对服务目标、指标与统计约定的原始资料。
- [Google SRE Workbook Implementing SLOs](https://sre.google/workbook/implementing-slos/)：用于核对服务目标、指标与统计约定的原始资料。
- [OpenTelemetry Metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)：用于核对服务目标、指标与统计约定的原始资料。

> 计算题中的数值为条件明确的教学示例；不代表具体运营合同或实际 SLO。
