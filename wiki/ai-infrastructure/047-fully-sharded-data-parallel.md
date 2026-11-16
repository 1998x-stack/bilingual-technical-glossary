# Fully Sharded Data Parallel（全分片数据并行 · FSDP）

> 学科：AI Infrastructure · 专题：分布式训练 · 注意区分概念本身与具体训练框架的版本差异

## 1. 核心定义

全分片数据并行（FSDP）在数据并行 rank 之间切分模型状态，通常包括参数、梯度与优化器状态；计算某个模块时按需聚合其完整参数，再将结果以分片形式保存。它用更密集的通信换取较低的单 rank 模型状态内存。

## 2. 形象理解

四位研究者平时只保管一本大书各自四分之一的原稿，编辑某章时暂时收集相应页码，编辑完成后只保留所属片段。这不是四个人各保留整本书的 DDP；收集页面带来时间和缓冲成本。

## 3. 技术原理与核心内容

典型 full-shard 路径：存储期只保留本 rank 参数 shard → 前向对当前模块 `all-gather` 参数 → 完成计算后按策略 reshard → 反向需要时再次 unshard → 将梯度 `reduce-scatter` 给对应分片所有者 → 每 rank 更新本地 optimizer shard。不同实现可在 forward/backward 前预取下一模块。PyTorch 新代码推荐 `torch.distributed.fsdp.fully_shard()`（FSDP2）；旧 `FullyShardedDataParallel` 的 API 和 state_dict 格式不可盲目互换。总峰值还包括当前解分片参数、激活、梯度、通信 buffer 与显存碎片。

## 4. 工程实践与设计权衡

在 8 卡上训练单卡模型状态放不下的模型时，先测无分片基线，再选模块 wrap 粒度；太细会产生大量小 all-gather，太粗会让 unsharded 峰值过大。用 profiler 定位参数预取、reduce-scatter、CPU offload 和 checkpoint 写入热点。恢复时使用与 sharded state_dict 匹配的分布式 checkpoint API，而不是假定单进程 `torch.save` 自动适配不同 rank 数。

## 5. 易混概念与边界

FSDP 主要解决**复制的模型状态**问题；TP 改变每层计算本身，PP 改变层位置。FSDP 与 ZeRO-3 的模型状态分片思想接近但不是同一套代码和 API。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 FSDP 比 DDP 更省显存，却不一定更快？** 答：FSDP 需要在前向/反向阶段做参数 all-gather 和梯度 reduce-scatter，通信频率可能增大，且会临时展开参数；DDP 主要同步梯度。测显存峰值和 step time，同时调 wrap 粒度、预取与重叠。

2. **问：为何 FSDP 的训练恢复要特殊处理 checkpoint？** 答：参数和 optimizer 状态分布在各 rank，单 rank 可能无法持有全部权重；应使用可分片存取和 reshard 的 state dict / distributed checkpoint 方法，测试跨设备数量恢复的一致性。

## 7. 中等难度考试题（含解析）

1. **题：模型原始参数体积 16 GiB，理想在 8 个 rank 均匀 full-shard，静态参数持有量每 rank 是多少？** 解：`16/8 = **2 GiB**`，不含临时 all-gather（当前模块需全参数）、梯度、优化器和激活，因此不能推断总峰值只有 2 GiB。

2. **题：单层完整 BF16 权重 800 MiB，FSDP=4；每 rank 持久分片与进入该层计算时该层参数可能临时展开的体积分别多少？** 解：持久参数分片 `800/4=**200 MiB**`；该层执行时若 all-gather 完整参数，临时完整表示可达 **800 MiB**，实际峰值依缓冲复用和 wrap 策略而变。

## 8. 权威来源与延伸阅读

- [PyTorch FullyShardedDataParallel / FSDP2](https://docs.pytorch.org/docs/main/fsdp.html)：FSDP 新旧 API 取舍及策略边界。
- [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html)：分片 state_dict 的保存、恢复与跨拓扑 reshard。

> 所有数值演算均以题设为准，不是特定 GPU、网络或框架版本的实测结果。
