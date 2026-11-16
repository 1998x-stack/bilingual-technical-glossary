# Key-Value Cache（键值缓存 · KV Cache）

> 学科：AI Infrastructure · 专题：推理与服务 · 推理服务实现需核对引擎版本、请求与测量边界

## 1. 核心定义

键值缓存（KV Cache）保存 Transformer 各层先前 token 的注意力 K/V 表示，使后续自回归 decode 不必为每个历史 token 从头计算相同的线性投影。它是**推理时动态增长的状态**，并不是模型权重或普通 HTTP 内容缓存；对架构、分片和缓存复用策略有依赖。

## 2. 形象理解

在阅读长书时留下每一页的关键词索引，下一次答问题直接查索引而不再重新整理全书。索引会占存储空间，书越长索引越大；如果索引对应的版本或阅读权限变化，就不能盲目重用。

## 3. 技术原理与核心内容

标准 dense decoder 层，单序列 L 个 tokens、N_layers 层、H_kv 个 KV heads、head_dim=d、每元素 b 字节时，理论 KV 字节约 `2×N_layers×L×H_kv×d×b`。这里使用 **KV 头数**而非 query head 数，GQA/MQA 减少 KV heads 可降低缓存。还要加 block 对齐、元数据、模型权重、临时 workspace，TP/PP 切分后的每 rank 显存不能简单等于整模型量。Prefix caching 只有在相同模型权重、token IDs、位置/配置及适当安全隔离时才可复用。

## 4. 工程实践与设计权衡

排查长上下文请求 OOM 应把模型权重、KV allocated、KV reserved 与实际 token 形状分别计量。观察活跃请求数、最大上下文、GQA、KV precision、block_size 与抢占频次；针对可重用系统前缀的工作负载测真实 cache hit，而非只宣称缓存一定节省计算。跨租户缓存更应遵循数据隔离。

## 5. 易混概念与边界

KV Cache 是前向计算的历史状态，PagedAttention 管理 KV 的物理块映射，prefix cache 复用已有内容，模型权重缓存则是不同对象。GQA 的 KV head 数可能明显少于 Q head 数。

## 6. 中等难度面试题（含参考答案）

1. **问：GQA 模型的 KV 内存为何不能用 attention 总 query heads 估算？** 答：GQA 中多个 query heads 共享一组 K/V heads，应按配置的 num_key_value_heads 计算。若按 query_heads 计算会高估，而多层/多实例分片仍需处理。

2. **问：为什么升级模型版本后不能无条件复用旧 KV？** 答：KV 值由旧权重、tokenization、位置编码和运行配置生成，新模型不一定等价；错配可能导致错误输出甚至数据隔离问题。应通过版本键和请求权限严格管理缓存。

## 7. 中等难度考试题（含解析）

1. **题：32 层、8 KV heads、head_dim=128，BF16=2 bytes，单序列 4096 tokens，未分片的理论 KV 大小？** 解：`2×32×4096×8×128×2 = 536,870,912 B = **512 MiB**`；不含 block 碎片、模型权重和 allocator。

2. **题：如果输出新增长度从 4096 增加 1024，在上述条件下 KV 理论额外增长？** 解：每 4096 tokens 为 512 MiB；额外 1024 tokens 为四分之一，即 **128 MiB**。

## 8. 权威来源与延伸阅读

- [vLLM KV Cache Manager](https://docs.vllm.ai/en/latest/design/hybrid_kv_cache_manager/)：可用于核对上述机制的维护者文档或原始研究。
- [PagedAttention 原论文](https://arxiv.org/abs/2309.06180)：可用于核对上述机制的维护者文档或原始研究。

> 所有数字示例均为题设下计算，不是生产集群性能承诺。
