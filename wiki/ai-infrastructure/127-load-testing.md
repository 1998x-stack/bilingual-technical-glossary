# Load Testing（负载测试）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 具体告警、性能或会计口径需按环境与约定核对

## 1. 核心定义

负载测试（Load Testing）是通过有控制的请求到达率、并发、数据规模和任务复杂度，对服务的吞吐、延迟、错误率、资源利用率与容量极限进行测量。LLM 推理尤其要区分输入/输出 token 长度、缓存命中、首 token 延迟、TPOT/ITL 与真实流式完成；仅报告总 TPS 或端口连接数不能代表用户体验。

## 2. 形象理解

像对新桥梁逐步增加车辆、货车比例和高峰时间流量，观察通行速度、排队以及何时出现封路；只让空车匀速通过不能预测节假日货运高峰。

## 3. 技术原理与核心内容

闭环压测中每个客户端等待响应后再发送，系统变慢会降低到达压力，可能发生 coordinated omission。开放环按预定到达曲线生成请求，更适合暴露队列堆积和超载；必须区分 offered load、accepted RPS、completed RPS 和成功 RPS。LLM benchmark 应固定模型版本、tokenizer、prompt/output 长度分布、batch 配置、temperature、缓存、硬件与 warmup；报告 TTFT P50/P95/P99、ITL/TPOT、goodput、KV cache preemption、GPU power 和成本。工作负载饱和后，更多并发不等于更高有效吞吐。

## 4. 工程实践与设计权衡

在线服务以阶梯式 arrival RPS 和并发执行测试，模拟短问答、长输入、长输出、多租户 burst、故障恢复与缓存冷热；建立停止条件防止实际用户受影响。压测从 staging 开始，真实生产影子流量必须删敏感信息且隔离副作用。生成负载器也可能 CPU/网络饱和，需分别测客户端发送时间与服务端 ingress；在同一 SLO 下比较好请求数/秒（goodput），而非仅比理论 TPS。

## 5. 易混概念与边界

Load testing 测预期负载下性能；Stress testing 逼近/突破极限，Soak testing 测长时稳定，Chaos Engineering 主动注入故障验证恢复。流式 TTFT 是首 token 前时间，E2E 是完整输出完成时间，不应混写。

## 6. 中等难度面试题（含参考答案）

1. **问：什么是 coordinated omission，为什么会美化 P99？** 答：闭环负载器在服务器变慢时停止产生本应到达的新请求，遗漏了排队等待中的大量高延迟事件，使结果低估过载带来的用户体验。

2. **问：LLM A 比 B 最高 TPS 高，为什么未必值得上线？** 答：如果 A 的 TTFT P99 或错误率突破 SLO，吞吐峰值并不能变成更多有效请求。需比较相同 token 分布、硬件与 SLO 下的 goodput 和成本。

## 7. 中等难度考试题（含解析）

1. **题：30s 内客户端计划发送 3000 次请求，但服务实际只完成 2400 次，offered arrival RPS 与 completion RPS？** 解：分别 `3000/30=**100 RPS**` 与 `2400/30=**80 RPS**`，积压可能持续增长。

2. **题：10min 内完成 6000 次请求，其中 5400 次满足端到端延迟和成功条件，goodput？** 解：`5400/600=**9 good req/s**`，并非全部完成的 10 RPS。

## 8. 权威来源与延伸阅读

- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：供独立核对上述机制、公式与实施前提的一手资料。
- [Google SRE Load Testing](https://sre.google/sre-book/handling-overload/)：供独立核对上述机制、公式与实施前提的一手资料。
- [k6 Open and Closed Models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/)：供独立核对上述机制、公式与实施前提的一手资料。

> 数值题仅为学习示例，不是生产硬件压测或会计处理意见。
