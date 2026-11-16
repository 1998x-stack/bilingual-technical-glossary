# Global Batch Size（全局批量大小）

> 学科：AI Infrastructure · 专题：分布式训练 · 相关框架实现请核对所引用版本

## 1. 核心定义

全局批量大小（Global Batch Size）表示**一次实际参数更新**汇聚的、所有数据并行副本处理的训练样本总数。在均匀样本、固定 microbatch 且每次更新累积相同步数的配置下，常用 `GBS = DP_degree × per_rank_microbatch × accumulation_steps`。

## 2. 形象理解

多家分店（数据并行副本）各做若干小批次统计，最后总部合并为一次制定价格的决策。只需数独立分店处理的样本，不需要把一件商品经过的每条流水线工位都数一次；一个样本被重复采样时也不自动算作新的唯一数据。

## 3. 技术原理与核心内容

设 DP 维 d、每 rank 每微步 b 个样本、累积 K 次，则 `GBS=d·b·K`。模型还可能有 TP/PP/EP/CP 维，它们处理同一份模型或某一份数据的不同片段，**不能直接用物理 GPU 总数替代 DP_degree**。对可变长 token、序列 packing 和数据 padding，GBS 的“样本数”不能直接等于“有效 token 数”；优化目标与梯度归一化需要定义样本/词元权重。尾部不满批、sample repeats、dynamic batch 和 rank 失衡都应在日志标记。

## 4. 工程实践与设计权衡

扩容后保持学习率实验可比时，应同时记录 GBS、local batch、DP 度、K、序列长度和每次更新的有效 token 数。如果 GPU 总数翻倍但新增 GPU 都分配给 TP，GBS 未必变化。训练吞吐应同时报告 tokens/s、updates/s 和 samples/step；数据规模和训练步数的估算由 GBS 决定，不应把优化器 step 次数误当 microstep。

## 5. 易混概念与边界

**Global batch** 是优化语义；**Microbatch** 是执行颗粒度。**Local batch** 常指单个数据副本一次处理多少样本，但不同文档可能指累积前或累积后规模，必须标明。**World size** 是进程总数，不一定等于 DP rank 数。

## 6. 中等难度面试题（含参考答案）

1. **问：把模型从 8 GPU 扩到 64 GPU 时，为什么 GBS 不一定扩大 8 倍？** 答：若额外 GPU 用来增加 TP/PP 或 EP，而不是 DP 副本数，处理独立训练样本的副本数不按物理 GPU 数增加；还可能调整 microbatch 或 K 保持 GBS 不变。

2. **问：只记录 GBS 为什么不够分析训练效率？** 答：同一 GBS 可由更小 microbatch+更多累积得到，kernel 大小、通信同步次数、内存峰值和 optimizer step 时延可能不同；还须记录序列长度及 token padding。

## 7. 中等难度考试题（含解析）

1. **题：64 GPU，正交 TP=4、PP=2，则 DP=8。每 DP rank 微批 2、梯度累积 4 步，GBS 是多少？** 解：`DP=64/(4×2)=8`；`GBS=8×2×4=**64**` 个样本/优化更新，不乘 TP、PP 度。

2. **题：固定 1,024,000 条样本、GBS=256 且完整遍历一次，每 epoch 有多少次参数更新？** 解：`1,024,000 / 256 = **4000**` 次，假设整除且全量样本恰使用一次。若动态 packing 或丢弃尾批则实际不同。

## 8. 权威来源与延伸阅读

- [Megatron Core Parallelism Strategies](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)：多维并行与 global/microbatch 配置。
- [PyTorch DistributedDataParallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)：DP rank 处理独立样本、梯度同步及损失归一化语义。

> 示例值为题设下的教学计算；硬件、数值格式和框架实现的实测结果以可复现实验为准。
