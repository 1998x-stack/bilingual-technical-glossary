# Time per Output Token（每输出词元耗时 · TPOT）

> 学科：AI Infrastructure · 专题：推理与服务 · 所有性能指标必须注明计量口径与软件版本

## 1. 核心定义

每输出词元耗时（TPOT）通常衡量首个输出后的**平均**生成间隔。vLLM benchmark 的每请求口径是 `TPOT=(E2E−TTFT)/(N−1)`，其中 N 是输出 token 数，N>1；随后才汇总各请求的 TPOT。若日志统计的是 decode kernel 时间而不是用户可见事件时间，须另行命名。

## 2. 形象理解

第一道菜端上来后，后续每一道菜平均多久上桌。首菜等待可能很长，但不应混到后续平均间隔里；平均值也不能代表最慢一次上菜的体验。

## 3. 技术原理与核心内容

令输出 token 的客户端到达时间为 `t_1..t_N`，标准单 token 流式情形 `TPOT=(t_N−t_1)/(N−1)`。若服务一次发送多个 token（如 speculative decoding 或 SSE 合并），事件数不再等于 token 数，观察到的相邻事件间隔不同于严格 per-token 生成间隔。对单 token 的响应，N−1=0，数学上未定义，不应误将 zero 视为性能完美。

## 4. 工程实践与设计权衡

在稳定并发下，按请求长度分桶比较 per-request TPOT 分布，结合 GPU KV cache 使用率、decode scheduler 时间和抢占次数。总 token/s 上升同时 TPOT 恶化，通常表示吞吐与单请求延迟的取舍，应在 SLO 约束下分析，不单凭一个指标判定。

## 5. 易混概念与边界

TPOT 的倒数近似该请求首 token 后的单流速率，但不等于集群聚合 TPS。ITL 是逐个流式输出事件间隔的样本，跨请求聚合权重不同。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 ITL 直方图和 TPOT 分布可能不同？** 答：ITL 按输出事件/间隔聚合，而 TPOT 通常先按请求取平均；长/短请求权重不同，chunk 一次含多 token 时差异更大。

2. **问：提高 TPOT 是否必然提高服务器吞吐？** 答：不一定。少量并发能缩短单请求间隔，但总吞吐可能下降。需联合看 RPS、output TPS、KV cache 与排队时间。

## 7. 中等难度考试题（含解析）

1. **题：E2E=1.22s、TTFT=0.22s，输出 101 tokens，TPOT？** 解：`(1.22−0.22)/(101−1)=0.01s`，即 **10 ms/token**；不把首 token 重复计入分母。

2. **题：4 token 分别在 100、120、145、160 ms 到达，其 TPOT？** 解：三个间隔是 20、25、15 ms；`(160−100)/3=**20 ms/token**`。

## 8. 权威来源与延伸阅读

- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：所述指标定义、测量或工程实现的维护者说明。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：所述指标定义、测量或工程实现的维护者说明。

> 示例中的具体数字是有声明前提的教学计算，不是硬件或线上集群的实测基准。
