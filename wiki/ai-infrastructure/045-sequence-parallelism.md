# Sequence Parallelism（序列并行 · SP）

> 学科：AI Infrastructure · 专题：分布式训练 · 内容范围：训练系统与工程实现（以所引官方资料的版本为准）

## 1. 核心定义

序列并行（SP）在 Megatron 等框架的**张量并行组内**，把 LayerNorm、Dropout 等适合按 token 独立处理的部分激活沿序列维切分，以降低复制激活带来的显存开销；它不表示任意注意力层都可以不通信地沿序列切开。

## 2. 形象理解

一篇长文章分给四名编辑，各自完成不依赖其它段落的排版检查；需要理解整篇上下文的推理仍必须共享信息。SP 的切分只对可独立处理的部分算子成立，不能误推为注意力完全局部。

## 3. 技术原理与核心内容

以形状 `[B,S,H]` 的 token 激活为例，TP 组内把序列 `S` 等分，LayerNorm/Dropout 等仅依赖各 token 的特征维，可在局部 shard 上执行。与 TP 的列/行矩阵计算相接时需要 all-gather 和 reduce-scatter 等布局变换；这引入通信，但减少被多个 rank 重复保存的中间激活。**Context Parallelism (CP)** 可在整个 Transformer 更多模块上分片完整序列，注意力需要额外通信获取 KV；SP 不能和 CP 的范围混同。

## 4. 工程实践与设计权衡

超大模型叠加 TP 时，先定位 LayerNorm/Dropout 及残差路径的显存峰值是否被多 rank 复制，再用框架的 sequence-parallel 选项测试。记录 activated bytes、AG/RS 时间、梯度数值一致性及各 TP 组的通信拓扑。若序列长度不能整除 SP 度，需做序列 padding 或采用框架支持的不均匀切法；空序列位置必须正确 mask。

## 5. 易混概念与边界

SP 常与 TP 紧密绑定，CP 是更全面的长上下文序列分片；**TP** 分片权重/输出特征，**PP** 分片层。模型是否支持 SP 和其具体节点规则须按 Megatron Core/PyTorch 实现版本核对。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 SP 对 LayerNorm 可行，却不能照样让常规 self-attention 不通信？** 答：LayerNorm 对每个 token 的隐藏特征归一化，不依赖其它 token；self-attention 的一个 query 需要访问可见范围内的 key/value。序列切分后必须通过 gather、ring attention 或等效通信取得远端 KV 信息。

2. **问：启用 SP 后显存下降但吞吐变慢，如何判断是否值得？** 答：测量节省的激活内存和新增 AG/RS 的字节与次数。如果通信阻塞且原本没有 OOM，可降低 TP 度或改善重叠；若省出的显存支持更长序列/更大 batch，则需比较相同任务的端到端结果。

## 7. 中等难度考试题（含解析）

1. **题：BF16 激活 `[B=2,S=4096,H=2048]`，按每元素 2 字节且没有额外布局开销，完整大小多少 MiB？SP=4 时每 shard 多少？** 解：完整字节 `2×4096×2048×2=33,554,432`=**32 MiB**；均匀四分后每 rank **8 MiB**。这是单张激活，未计其它缓存与 all-gather。

2. **题：SP=4，序列长度 S=4096，且可以四等分，单 rank 接收多少 token 位置？** 解：`4096/4=**1024**` 个位置。如果另有 batch 维 B=2，则这个 shard 共含 2048 个 token 实例；不可把 1024 误读为所有 batch 的合计。

## 8. 权威来源与延伸阅读

- [Megatron Core Parallelism Strategies](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)：SP 与 TP 配合的训练策略。
- [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198)：序列并行和激活内存优化研究。

> 数值题均为明确的教学假设，不代表设备实际基准性能；版本敏感的接口与优化建议以对应官方文档为准。
