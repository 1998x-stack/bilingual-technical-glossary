# Microbatch（微批次）

> 学科：AI Infrastructure · 专题：分布式训练 · 相关框架实现请核对所引用版本

## 1. 核心定义

微批次（Microbatch）是把一次逻辑训练 batch 拆成更小、逐次执行的样本子集，控制单次前向/反向的激活内存和流水线调度颗粒度。在流水线并行中它尤其是让 stage 交错运行的工作单位，而不是“每次训练最终参数更新只处理这么多样本”。

## 2. 形象理解

一批 1000 件货物拆成 10 小车逐个进入多工位生产线，既降低每个工位的即时占用，也让前后工位同时忙起来。小车太小会导致搬运次数过多、利用率差；小车不直接等于整批货物总数。

## 3. 技术原理与核心内容

定义 per-rank microbatch 大小 b、数据并行副本数 d、每次优化更新累积的 microbatch 数 m，则常见等长样本配置中 `global_batch = b × d × m`。注意 **PP stage 数 p 不应额外乘入**，因为所有 stage 处理的是同一批不同阶段的数据。对流水线调度，每个微批需在 stage 边界传送激活/梯度；调度 m 越大，可减少理想空泡比例，却可能增加控制开销和内存中同时驻留的微批。对非流水线训练，也可用 microbatch+gradient accumulation 实现显存受限的大有效 batch。

## 4. 工程实践与设计权衡

调参时固定 global batch，减小微批大小并相应增加累积步数，可对比峰值 activation 和每秒样本数。测量 GEMM 的算术强度、GPU kernel launch、每微批通信次数、stage idle 和 OOM。若固定累积步数、改动 microbatch，会改变有效 batch，学习率与收敛对比必须重新定义。

## 5. 易混概念与边界

**Microbatch** 是执行颗粒度；**mini-batch** 常指优化器更新使用的一批样本；**Gradient Accumulation** 负责把多个微批的梯度整合为一次更新；**PP** 用微批交错 stage，不必让 PP stage 数成为 batch 倍数。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么降低 microbatch 能解决 OOM 却可能降低吞吐？** 答：更少的样本在单次前向中占用更少激活，但矩阵运算规模变小、kernel launch 与集合通信次数上升；流水线也可能因 m 变化导致空泡。应在固定全局样本数下比较端到端。

2. **问：PP 与 DP 结合时为什么不能把 PP stage 数乘进 global batch？** 答：同一个微批顺序流经多个 stage，stage 是模型分段而非不同样本副本。只有数据并行副本实际处理独立数据，才能按其数量扩展 global batch。

## 7. 中等难度考试题（含解析）

1. **题：DP=2、PP=4，每 rank 计算当前微批 b=8，每次更新共有 m=4 个微批，global batch 是多少？** 解：`2×8×4=**64**` 样本/更新；4 个 PP stage 对同一微批分层处理，**不**把全局 batch 再乘 4。

2. **题：总需要 512 个样本/更新、DP=8、microbatch=4，必须累积几个等大 microbatch？** 解：`m=512/(8×4)=**16**` 个；前提无样本重复/不满批及其它 batch 汇总规则。

## 8. 权威来源与延伸阅读

- [Megatron Core Pipeline/Parallelism Guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)：微批在 PP 中的调度与并行组定义。
- [PyTorch AMP Gradient Accumulation](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)：有效批与多微步参数更新关系。

> 示例值为题设下的教学计算；硬件、数值格式和框架实现的实测结果以可复现实验为准。
