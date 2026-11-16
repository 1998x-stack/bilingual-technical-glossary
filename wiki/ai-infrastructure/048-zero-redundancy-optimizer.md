# Zero Redundancy Optimizer（零冗余优化器 · ZeRO）

> 学科：AI Infrastructure · 专题：分布式训练 · 注意区分概念本身与具体训练框架的版本差异

## 1. 核心定义

零冗余优化器（ZeRO）由 DeepSpeed 推广，通过在数据并行进程之间分片原本重复保存的训练模型状态减少显存占用。不同 stage 分片范围不同；它不是把梯度直接置零，也不是零内存开销。

## 2. 形象理解

四位会计不再各自复制整套账本：ZeRO-1 分摊 optimizer 账目，ZeRO-2 再分摊汇总后的梯度，ZeRO-3 连日常保管的参数也分配给各人。工作时仍要交换账目；阶段越高，一般通信与状态管理越复杂。

## 3. 技术原理与核心内容

**ZeRO-1：**分片优化器状态。**ZeRO-2：**进一步分片约化后的梯度。**ZeRO-3：**再分片参数，需要按层进行参数 gather 和更新后的重新分片。此处的划分针对训练状态，而不是让 layer 的矩阵乘自动并行。可选 CPU/NVMe offload 进一步减轻 GPU 压力，但带来总线/存储带宽和恢复时延约束。跨版本的 offload、阶段配置与分区策略应查具体 DeepSpeed 文档，不能将 ZeRO-3 与 FSDP 的性能行为视作完全一致。

## 4. 工程实践与设计权衡

用 Adam 在多卡训练中，先分别统计 BF16 参数、FP32 master weights、两个 Adam 矩量、梯度、激活与优化器临时状态，选择性打开 ZeRO stage。若慢在参数 gather，比较 all-gather buffer、跨机网络与 overlap；若 CPU offload 慢，量测 PCIe/NUMA 与主存压力。检查优化器 step、权重更新与恢复 checkpoint 的所有 rank 一致性。

## 5. 易混概念与边界

ZeRO 是按分布式训练状态定义的一族内存优化阶段；**gradient accumulation** 仅改变更新频率，**activation checkpointing** 降低激活内存，**TP** 改变单层计算分片。不能把 ZeRO-3 简化为“梯度分片”，那只覆盖更早阶段的一部分能力。

## 6. 中等难度面试题（含参考答案）

1. **问：ZeRO-1/2/3 的主要差别在哪里？** 答：1 分片 optimizer，2 进一步分片梯度，3 再分片模型参数；每一层降低不同重复模型状态，带来不同的 gather/reduce 与 offload 取舍。不要说阶段越大必然端到端更快。

2. **问：ZeRO-3 GPU 显存仍可能 OOM，原因是什么？** 答：前向层级 gather 产生峰值完整参数、激活未被分片、通信缓冲、临时重计算与碎片仍需空间；还可能因为模型包裹粒度过大导致预取阶段同时展开多个模块。

## 7. 中等难度考试题（含解析）

1. **题：四个 rank，某 optimizer 状态共 16 GiB、可理想均匀划分；ZeRO-1 静态每 rank 存多少？** 解：`16/4 = **4 GiB**` 的 optimizer shard，省去重复保存的其它三份 optimizer 状态；模型参数和梯度仍有其自身开销。

2. **题：理想总计 24 GiB 的可分片参数+梯度+优化器状态，ZeRO-3 在 8 rank 上平均持有多少？** 解：`24/8=**3 GiB**` 仅代表平均静态可分片状态；真实显存要加临时参数 all-gather、激活、通信与预取 buffer。

## 8. 权威来源与延伸阅读

- [DeepSpeed ZeRO Tutorial](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/_tutorials/zero.md)：ZeRO-1、2、3 分片模型状态的官方教程。
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054)：提出 ZeRO 状态冗余分析的原始论文。

> 所有数值演算均以题设为准，不是特定 GPU、网络或框架版本的实测结果。
