# Prefill（预填充阶段）

> 学科：AI Infrastructure · 专题：推理与服务 · 推理服务实现需核对引擎版本、请求与测量边界

## 1. 核心定义

预填充（Prefill）是自回归 Transformer 推理中处理已有输入上下文的阶段：将 prompt tokens 并行送过模型，产生后续生成所需的中间状态，典型情况下建立各层 KV Cache。它可能包含生成首 token 所需的 logits，但**prefill 结束不等同于完整生成结束**。

## 2. 形象理解

读完整份任务说明并做索引卡，再开始逐句回答；读得越长，首个回答往往越迟。类比仅解释执行阶段：具有前缀缓存的请求可复用已计算的 KV，不必从头重读相同前缀。

## 3. 技术原理与核心内容

对注意力模型，prefill 处理 Q/K/V 投影、注意力和 FFN 等层，生成缓存的每层 key/value。未采用优化算法的完整 attention 计算会涉及输入长度 S 的二次 token 交互，而 FlashAttention 等可改善 HBM 访存，模型仍需处理输入 token 的前向算术。Chunked prefill 将长上下文拆分多个调度单位，便于与活跃 decode 交错；不同实现能否每次增量处理或共享 prefix KV 要检查 backend。

## 4. 工程实践与设计权衡

长 prompt 的 TTFT P99 高时，按输入长度、缓存命中、tokenization、queue、GPU prefill 时间分桶。设置 prompt 128/2K/16K tokens、固定输出长度，观察 latency 与系统 TPS。减少输入有效长度、前缀缓存或预填充分离可能改善服务目标，但缓存隔离、KV 容量和网络传输会约束收益。

## 5. 易混概念与边界

**Prefill** 主要处理已有输入并建立 KV；**Decode** 每轮根据上下文生成新的 token。Prefill TPS 与 decode TPS 性能特征不同；在 PD 分离部署中两个阶段可处于不同资源池，不代表两个模型权重版本可以随意不一致。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么长 prompt 更可能影响 TTFT 而不是每个 decode step 的固定算术？** 答：prefill 要处理更多输入 token，且首响应之前通常必须完成必要上下文处理；decode 单步只追加新 token，但其读取的 KV 长度也会增加，所以不能声称 decode 时延与上下文长度无关。

2. **问：为什么 chunked prefill 能减小调度阻塞却未必提升总 prefill 速度？** 答：拆成小块使 scheduler 在长 prompt 中间安排其他请求，改善公平性；但多次调度及算子拆分可能增加开销，须实测在相同 SLO 下的吞吐和 ITL。

## 7. 中等难度考试题（含解析）

1. **题：一个 prompt 2048 tokens，已缓存连续前缀 1536 tokens，忽略校验和 mask 变化，仍需 prefill 多少新 tokens？** 解：`2048−1536=**512 tokens**`；不能把已缓存 tokens 当成新 GPU 计算。

2. **题：prefill 使用 120 ms，输入 2400 tokens，定义仅 GPU prefill 计算速率，求 tokens/s。** 解：`2400/0.12=**20,000 tokens/s**`。这是该阶段的简化处理率，不等于整机输出 TPS。

## 8. 权威来源与延伸阅读

- [vLLM Chunked Prefill](https://docs.vllm.ai/en/latest/features/chunked_prefill/)：可用于核对上述机制的维护者文档或原始研究。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：可用于核对上述机制的维护者文档或原始研究。

> 所有数字示例均为题设下计算，不是生产集群性能承诺。
