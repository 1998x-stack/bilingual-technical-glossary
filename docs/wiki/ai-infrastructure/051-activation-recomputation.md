# Activation Recomputation（激活重计算）

> 学科：AI Infrastructure · 专题：分布式训练 · 相关框架实现请核对所引用版本

## 1. 核心定义

激活重计算（Activation Recomputation）是在训练时不永久保存某些前向中间张量，而在反向求导真正需要时重新执行选定算子或片段。它是**用计算换内存**的通用机制；具体软件配置可能称 activation checkpointing、selective recomputation 或 rematerialization。

## 2. 形象理解

把计算结果看成可重新生成的草稿，内存有限时不归档每张草稿，必要时重新做一次演算。若重新演算本身昂贵，省下的空间可能不抵增加的时间；若依赖了会变化的随机或外部状态，重新做出的草稿也可能不同。

## 3. 技术原理与核心内容

反向传播需要某些前向激活来计算局部导数。重计算策略为这些中间结果选择保存或丢弃：**完整区段重算**在 backward 再执行整个区段；**选择性重算**保留昂贵的中间结果，仅重做廉价且占显存较大的部分。对 Transformer，可权衡注意力 softmax、RMSNorm、dropout 和 MLP 激活；具体层中哪些操作适合重算由算子融合和实现决定。正确性要求保留计算图边界、RNG/掩码和必要的输入状态，不能把有副作用的函数当成纯函数。

## 4. 工程实践与设计权衡

当模型序列长度增长使 peak activation 成为瓶颈时，先测每层激活显存占比和重算 FLOPs，再选择重算 granularity。若 attention 已使用内存高效 kernel，重算其内部中间张量的收益可能不同于朴素 attention。训练中记录 `max_memory_allocated`、实际 recompute kernel 时间、梯度差异、dropout RNG 再现性；结合 TP/SP/CP 不同 layout 的输入生命周期进行调试。

## 5. 易混概念与边界

**Gradient Checkpointing** 通常是激活重计算的一种具体 API/策略；**训练 Checkpoint** 是写磁盘的恢复状态；**Activation Offloading** 则把激活移到 CPU/NVMe 再读回，不是重新执行算子。

## 6. 中等难度面试题（含参考答案）

1. **问：如何选择重算 attention 还是 MLP？** 答：比较两段保存激活字节、重算 FLOPs 和融合算子的实际临时内存。重点看 OOM 热点而非凭印象选择；长上下文 attention 的存储结构可能已由 FlashAttention 等优化改变。

2. **问：启用重计算后 loss 轨迹明显变化，怎样排查？** 答：检查 dropout RNG、自动混合精度策略、前向函数是否读取会变化的全局变量、checkpoint 区域是否跨设备移动、并行通信与梯度数值。用固定 seed 与小输入做前/反向差分，再放大到训练集群。

## 7. 中等难度考试题（含解析）

1. **题：某区段原来保存 12 张各 40 MiB 的激活，理想策略只保留其中 3 张，估算节省的驻留内存？** 解：原 `12×40=480 MiB`，保留 `3×40=120 MiB`，理想减少 **360 MiB**；不含重算瞬间工作区和其它模型状态。

2. **题：一个训练 step 原耗时 800 ms，选择性重计算额外执行 160 ms 算子，假设完全串行且无其它变化，时间与相对增幅？** 解：新 step `800+160=**960 ms**`；额外占 `160/800=**20%**`。如果有通信重叠，此估算不精确。

## 8. 权威来源与延伸阅读

- [PyTorch Activation Checkpointing](https://docs.pytorch.org/docs/stable/checkpoint.html)：官方描述重算的计算-内存交换与 RNG 风险。
- [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198)：Transformer 的选择性重算与序列并行技术研究。

> 示例值为题设下的教学计算；硬件、数值格式和框架实现的实测结果以可复现实验为准。
