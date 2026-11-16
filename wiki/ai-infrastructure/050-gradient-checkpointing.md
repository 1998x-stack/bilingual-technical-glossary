# Gradient Checkpointing（梯度检查点）

> 学科：AI Infrastructure · 专题：分布式训练 · 注意区分概念本身与具体训练框架的版本差异

## 1. 核心定义

梯度检查点（Gradient Checkpointing，又称激活检查点）在前向传播时只保存部分必要中间状态，在反向传播需要某个区间的激活时再运行其前向计算。其目的在于用额外的计算换取较低的激活显存需求；它**不是**保存断点供进程崩溃后恢复的训练 checkpoint。

## 2. 形象理解

徒步队不必拍摄沿路每一步的照片，只保留若干关键路标；回程需要细节时再从最近路标走一段。保存路标少了，回走增加了。与真实徒步不同，随机计算可能需要恢复 RNG 状态才能重现同一条路径。

## 3. 技术原理与核心内容

自动求导默认保留反向所需 tensor；包裹某个 function/layer 为 checkpoint region 后，仅保留输入/边界等少量张量，backward 时重新执行该区域 forward，得到反向所需的中间量。PyTorch 提供 `torch.utils.checkpoint.checkpoint`，通常建议 `use_reentrant=False`。若 dropout、全局状态或跨设备随机数在重算与原前向不一致，可能产生错误或不同梯度；保留 RNG 状态或在纯函数约束下明确允许不同随机流。计算增加量由 checkpoint 粒度、重用和非重入实现决定，并非固定“翻倍”。

## 4. 工程实践与设计权衡

对 Transformer 的注意力和 FFN block 以不同粒度分区测试：记录 peak allocated/reserved、forward/backward 时间、每秒 token 与训练 loss 变化。对长序列特别关注 flash attention 之类内存高效算子和重计算是否重复优化；不要在存在副作用或输入跨设备移动的函数里直接假定确定性。出错时比较启用前后的梯度和 RNG 同步而非只看是否 OOM。

## 5. 易混概念与边界

**激活检查点**是训练期重算策略；**训练检查点（Checkpoint）**是把模型、优化器和 RNG 等状态持久化供恢复。**Activation Recomputation** 指重算行为本身，与梯度检查点通常是同一策略的两种视角。

## 6. 中等难度面试题（含参考答案）

1. **问：为何梯度检查点可能使训练慢却仍是合理优化？** 答：减少保存的激活，避免 OOM 并允许更大序列/微批；代价是反向时重算部分前向。需要比较可完成的任务规模、吞吐与显存，而非只比较单 step 速度。

2. **问：为何 checkpoint 区域含 dropout 时要关注 RNG？** 答：重算必须在与原 forward 一致的随机行为下恢复梯度数学语义。PyTorch 默认尝试保存恢复相关 RNG 状态，但跨设备迁移、外部副作用和非确定行为仍需验证。

## 7. 中等难度考试题（含解析）

1. **题：示意模型有 10 个等大中间激活，各 100 MiB，全部保存需要多少？若按题设仅保留其中 5 个并在 backward 重算另 5 个，保留体积多少？** 解：全部为 `10×100=**1000 MiB**`；只留 5 个则 **500 MiB**，不含重算时临时激活、输入/梯度、参数或 allocator 开销。这是简化的存储记账模型。

2. **题：一轮反向对 3 个选定区段各额外重算一次 forward，每段 30 ms，假设无重叠且其它开销不变，新增计算耗时？** 解：额外时间 `3×30=**90 ms**`。真实训练时间可能因重叠、缓存、kernel 调度和不同重算路径而不同。

## 8. 权威来源与延伸阅读

- [PyTorch torch.utils.checkpoint](https://docs.pytorch.org/docs/stable/checkpoint.html)：激活重计算、RNG 语义与 use_reentrant 模式。
- [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174)：经典激活检查点的计算—内存权衡研究。

> 所有数值演算均以题设为准，不是特定 GPU、网络或框架版本的实测结果。
