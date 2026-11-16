# Tokens per Second（每秒词元数 · TPS）

> 学科：AI Infrastructure · 专题：推理与服务 · 所有性能指标必须注明计量口径与软件版本

## 1. 核心定义

每秒词元数（TPS）表示指定窗口内**输入或输出的 token 数**除以秒数。做服务容量规划时通常分别统计 prefill 输入 TPS 与 decode 输出 TPS；如声称总 TPS，必须注明是否把输入、输出、所有副本求和以及 tokenizer 版本。

## 2. 形象理解

像仓库一分钟处理多少件货，与某件货从进库到出库的等待完全不同。高 TPS 可能建立在深度批处理和高排队上，因此不能仅凭吞吐量承诺用户有更低 TTFT。

## 3. 技术原理与核心内容

对固定观察窗 Δt，输出 `TPS_out=C_out/Δt`，输入 `TPS_in=C_in/Δt`。请求存在起止跨窗口时，要按窗口内实际产生的 token 或 counter 增量计量，不应直接用“完成请求×平均输出长度”替代精确的流式时间数据。短期测试须说明暖机、首编译、prefix cache、并发和 sampling 参数，输入 token 的计算复杂度并不等同输出 decode token。

## 4. 工程实践与设计权衡

性能压测固定硬件/precision、input-output 长度分布、并发阶梯和缓存命中；报告 TPS_out、RPS、TTFT/TPOT P95 与 GPU KV 内存。连续批处理提高整体 TPS 但可能牺牲单用户长尾，可用同时满足 SLO 的 goodput 作为取舍指标。

## 5. 易混概念与边界

TPS 计 token，RPS 计 request；不同 tokenizer 下等长自然语言可能被切成不同 token 数。TPOT 近似单请求生成间隔，不能将所有 `1/TPOT` 简单求和当作系统稳态 TPS。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 TPS 上升不一定说明部署体验更好？** 答：更多并发可以提高聚合 token/s，却增加队列与 ITL 尾部；以相同 SLO 下完成的有效请求比较，避免吞吐指标掩盖拥塞。

2. **问：比较两个模型 output TPS 前需固定哪些变量？** 答：模型任务、tokenizer 或等价语义长度、输入/输出分布、采样参数、硬件、精度、并发、缓存与计时窗口。

## 7. 中等难度考试题（含解析）

1. **题：20 秒内集群输出 24,000 tokens，aggregate 输出 TPS？** 解：`24,000/20=**1,200 tokens/s**`，不表示某个请求每秒生成 1200 tokens。

2. **题：10 秒完成 200 次请求，平均每请求 40 输出 tokens，且均计入该时间窗，RPS 和 TPS？** 解：完成 RPS `200/10=**20**`，输出 TPS `200×40/10=**800**`；若请求跨窗口需换用实际 counter 增量。

## 8. 权威来源与延伸阅读

- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：所述指标定义、测量或工程实现的维护者说明。
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：所述指标定义、测量或工程实现的维护者说明。

> 示例中的具体数字是有声明前提的教学计算，不是硬件或线上集群的实测基准。
