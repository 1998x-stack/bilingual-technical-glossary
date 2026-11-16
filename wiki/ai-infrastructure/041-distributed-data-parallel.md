# Distributed Data Parallel（分布式数据并行 · DDP）

> 学科：AI Infrastructure · 专题：分布式训练 · 内容范围：训练系统与工程实现（以所引官方资料的版本为准）

## 1. 核心定义

DDP 是一种多进程数据并行训练封装：各 rank 保存完整模型副本，计算各自样本的前向与反向，并对梯度执行跨进程归约，使各副本以一致的更新规则前进。PyTorch 的 `DistributedDataParallel` 并不自动把输入划分给设备，数据采样必须由使用者配置。

## 2. 形象理解

把同一本教材复印给四位学生，每人做不同习题，然后汇总各题的共同修改意见。所谓“汇总意见”是梯度同步，而不是每做一道题都互相传递整本教材。类比的边界：非线性优化器状态、BatchNorm 统计量、随机数和不等量数据会影响一致性。

## 3. 技术原理与核心内容

**关键路径：** `DistributedSampler → local forward → local backward → gradient buckets → all-reduce/平均 → optimizer.step()`。DDP 把部分梯度按 bucket 聚合，可在反向计算其余层时与 NCCL 通信重叠；参数不在每一步重新全量广播，而是假设各副本执行相同优化更新。若用 `no_sync()` 累积梯度，注意必须将前向与反向都置于上下文中，并仅在最后一次反向同步。对于各 rank 损失使用平均的常见配置，全局梯度是各 rank 的平均；样本量不同时直接 rank 等权平均**不等于**样本等权平均。

## 4. 工程实践与设计权衡

单机 8 卡先用每卡单独进程、固定设备、进程组初始化和 `DistributedSampler`；对比分布式吞吐与端到端 step 时延。若训练卡住，检查是否有 rank 少执行一次 forward/backward、是否有未使用参数、sampler 是否产生不等长度数据、通信 bucket 和网络错误。同步 BatchNorm 另有专用语义；梯度同步不意味着所有模型缓冲区状态自动一致。

## 5. 易混概念与边界

**DP** 是通用策略，**PyTorch DDP** 是具体的分布式实现；**FSDP** 进一步分片参数/优化器状态，换取显存但增加参数 all-gather；**TP** 拆开同一层，梯度归约的通信位置不同。DDP 不会自动平均未等权样本的损失贡献。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 8 张 GPU 上使用 DDP，吞吐没有达到单卡 8 倍？** 答：比较每 rank 的 backward 计算与 all-reduce 时间、跨机网卡速率及 CPU 数据供给。DDP 的通信与计算可部分重叠但不能完全消除，另有 rank 不均衡、global batch 变化、进程启动和 checkpoint 开销。应测同一任务总样本/秒而非只测一个 kernel。

2. **问：如何做四次梯度累积而只同步一次？** 答：前三个微批在 DDP 的 `no_sync()` 中执行前向和反向，每个 loss 按 4 缩放；最后一个微批正常反向，随后裁剪梯度并 `optimizer.step()`、清零。结合 AMP 时须保持 scale 不变至有效批完成；不要在每个微批都调用 step。

## 7. 中等难度考试题（含解析）

1. **题：四个 rank，每 rank 每个微批 16 样本，累积 2 次；每次更新的全局样本数？** 解：在各 rank 均处理完整不同样本、无丢弃的前提下，global batch = 4 × 16 × 2 = **128**。如含重复采样或最后不满批，实际唯一样本数可能不同。

2. **题：理想环形 all-reduce，4 个 rank，每 rank 梯度张量 200 MB；单 rank 的总传输量约多少？** 解：理想大消息 ring 的每 rank 传输量约 `2(p−1)S/p` = 2×3×200/4 = **300 MB**（收发阶段合计口径；按算法和网络实现可能不同）。不能把 300 MB 直接解释为总网络字节数。

## 8. 权威来源与延伸阅读

- [PyTorch DistributedDataParallel API](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)：说明梯度同步、输入分片责任、no_sync 与同步点。
- [PyTorch DDP Design Note](https://docs.pytorch.org/docs/stable/notes/ddp)：解释 reducer、梯度 bucket 与通信重叠；注明设计笔记的版本边界。

> 数值题均为明确的教学假设，不代表设备实际基准性能；版本敏感的接口与优化建议以对应官方文档为准。
