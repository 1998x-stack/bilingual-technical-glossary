# Decode（逐词元解码阶段）

> 学科：AI Infrastructure · 专题：推理与服务 · 推理服务实现需核对引擎版本、请求与测量边界

## 1. 核心定义

逐词元解码（Decode）是在模型处理完初始输入后，根据当前上下文反复预测下一个 token、采样或选择、把它加入序列，并更新后续注意力所用 KV Cache 的阶段。自回归依赖使常规实现的多个输出步骤通常顺序发生，直到 EOS、长度上限或其他停止条件。

## 2. 形象理解

先读完题目后逐句起草答案：写下一句之前需要参考已有文字；同时多个读者可共用一台服务调度，但同一条答案的第 10 词通常依赖第 9 词。推测解码可能在验证通过时一次接受多个 token，这是传统单步描述的例外。

## 3. 技术原理与核心内容

每个普通 decode step 以本次新增 token 为 query，读取此前缓存的 keys/values，产生 logits 后按 temperature/top-k/top-p 等采样策略确定下一 token，并把对应 KV 写回缓存。注意力 KV 读流量随历史 token 数增长，动态 batch 大小与并发也改变访问形态。计算中可能使用 CUDA Graph、专用 attention kernel、量化权重和 speculative validation，不应把单 token kernel 时间等同客户端 ITL。

## 4. 工程实践与设计权衡

线上测量应将 decode GPU 时间、每个 token 的调度间隔、KV cache 块数、cache preemption、streaming flush 关联。长输出、长上下文、低并发与高并发分别跑基准；模型速度下降时优先确认是不是 memory bandwidth 或访存不规则而非盲目追求额外理论 FLOPs。

## 5. 易混概念与边界

Prefill 处理初始 prompt，并建立 KV；Decode 继续追加输出。TPOT 是从首 token 后统计的平均输出延迟，不是所有 decode 层算子的累积纯计算时间。Speculative decoding 的批量验证可减少目标模型串行调用次数，但不总能加速。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 decode 往往更受显存带宽影响？** 答：单步每请求 token 数少，却要读取大量模型权重及长度增长的 KV；算术强度与 batch 大小决定瓶颈。更大并发能提高复用但也增加 KV 内存压力。

2. **问：在 decode 途中请求频繁被 preempt，会发生什么？** 答：可能暂停或重新计算/交换部分 KV，导致 ITL 长尾；应检查 KV 容量、请求优先级、长短序列混排和分配器管理。不同引擎的抢占策略有差异。

## 7. 中等难度考试题（含解析）

1. **题：常规无推测解码，初始 prompt 100 tokens，最终再生成 20 tokens；假设首 token 在 prefill 后的第一次 decode 得出，需要几次串行生成选择？** 解：约 **20 次**新 token 的选择；实现的首 token 位置和核拆分不同，不能由此推定 20 次完全相同的 kernel 启动。

2. **题：单请求首 token 后的 100 次间隔平均 12 ms，估算这部分 decode 时间。** 解：`100×12=**1200 ms**`，未含 TTFT、网络缓冲与非均匀尾部延迟。

## 8. 权威来源与延伸阅读

- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：可用于核对上述机制的维护者文档或原始研究。
- [vLLM Engine/Model Execution](https://docs.vllm.ai/en/latest/design/)：可用于核对上述机制的维护者文档或原始研究。

> 所有数字示例均为题设下计算，不是生产集群性能承诺。
