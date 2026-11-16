# Disaggregated Prefill and Decode（预填充与解码分离 · PD Disaggregation）

> 学科：AI Infrastructure · 专题：推理与服务 · 以维护者文档及具体引擎版本为准

## 1. 核心定义

预填充与解码分离（PD Disaggregation）把处理输入上下文的 prefill 与持续生成 token 的 decode 部署在不同实例/资源池，让两类工作负载能分别优化 TTFT 和 ITL。阶段交接时需要准确传输 KV Cache、token IDs、模型与分片元信息；不是随意把同一模型前后层分到两个节点。

## 2. 形象理解

备菜和出菜由两个不同厨房承担：备菜有大批重活，出菜强调连续性。两处必须交接准确的原料与订单信息；交接搬运慢，可能抵消分开的好处。

## 3. 技术原理与核心内容

协调层首先把请求分派到 prefill 池构建 KV，之后将缓存交到 decode 池接着生成。跨池需要一致模型版本、tokenizer、位置编码与 KV layout；传输时延受字节数、有效网络带宽、协议开销影响。简化下界 `T_transfer ≥ bytes/bandwidth`，不能遗漏固定成本。vLLM 当前的 disaggregated prefilling 文档明确标为 experimental，相关接口可能调整。

## 4. 工程实践与设计权衡

部署对照需固定 prompt/output 分布与硬件：一体化、chunked prefill、PD 分离三种模式分别测 TTFT、ITL P99、KV transfer 字节和时延、池利用率及故障恢复。分离可隔离长 prompt 干扰，但还会引入跨池排队/负载均衡与缓存迁移。若模型小、请求短，网络成本可能使分离更差。

## 5. 易混概念与边界

PD 是按**推理阶段**切资源，TP 是层内张量切分，PP 是按层切模型；三者可能组合但依赖关系不同。Chunked prefill 可在同一池中与 decode 交错，并不要求独立资源池。

## 6. 中等难度面试题（含参考答案）

1. **问：PD 分离为什么可能降低 decode 的 ITL 长尾？** 答：长 prefill kernel 不再在同一设备与活跃 decode 竞争执行槽位；但仍需检查 decode 池自身的排队、KV 传输和吞吐上限。

2. **问：为什么 PD 池的模型版本必须一致？** 答：KV 是特定模型权重和位置语义下计算的结果，若 decode 使用不兼容的权重/配置，输出将错误或难以解释，应校验版本锁和缓存格式。

## 7. 中等难度考试题（含解析）

1. **题：传输 512MiB KV，链路有效带宽 8GiB/s，忽略固定开销，理想耗时？** 解：`0.5GiB/8GiB/s=**0.0625s=62.5ms**`。

2. **题：prefill=140ms、KV 传输=20ms、首个 decode=15ms，阶段不重叠的首输出最短时间？** 解：`140+20+15=**175ms**`，仍未包括网络响应和队列。

## 8. 权威来源与延伸阅读

- [vLLM Disaggregated Prefilling](https://docs.vllm.ai/en/latest/features/disagg_prefill/)：具体机制、实施边界与计算语义的原始或维护者资料。
- [vLLM Scheduling Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：具体机制、实施边界与计算语义的原始或维护者资料。

> 所有数值算例均为声明假设下的教学推导，不能替代线上基准或外部领域专家核验。
