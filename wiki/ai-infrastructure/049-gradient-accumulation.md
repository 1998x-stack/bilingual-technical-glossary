# Gradient Accumulation（梯度累积）

> 学科：AI Infrastructure · 专题：分布式训练 · 注意区分概念本身与具体训练框架的版本差异

## 1. 核心定义

梯度累积是在多个前向/反向微步中将梯度相加或正确加权平均，延迟执行优化器更新，使较小显存容量可模拟更大的**每次参数更新有效 batch**。它通常不能直接减少一次微批的峰值激活内存，但不必同时装下所有样本。

## 2. 形象理解

把四次小测的成绩意见先收集齐，再统一修改一次教学方案。每次测验后都修改方案，就不是“等价于四次意见的一次更新”；数学上要求在累积期间参数保持不变。

## 3. 技术原理与核心内容

每个微步执行 forward/backward，默认 `.grad` 在不清零时累加；在 K 个等大微批、损失按各自样本均值计算的情况下，可把每步 loss 除以 K 再 backward，K 次后更新一次。对不等样本量的最后微批，应按该微批的样本数/总样本数加权，而不是均匀除以 K。DDP 可以对非最后微步使用 `no_sync()` 降低重复 all-reduce；AMP `GradScaler` 的 scale 在有效批完成前不应随微步改变，梯度剪裁应在最终 unscale 以后执行。

## 4. 工程实践与设计权衡

训练显存不足时，可把 per-device microbatch 从 32 降为 8、累积 4 步，尽量维持 global batch；但每次更新的 wall-clock 时间可能延长，且 Dropout/BatchNorm、随机数、动态样本长度可能破坏严格数值等价。日志明确区分 `micro_step` 与 `optimizer_step`；学习率调度与 checkpoint 的 step 口径应按真正的 optimizer update 计算。

## 5. 易混概念与边界

梯度累积不是 DDP：前者是**时间维累积**，后者是**跨进程同步**；也不同于 PP 的 microbatch pipeline，虽可组合使用。累积并不自动保证与大 batch 完全一致，尤其在含 batch-dependent 操作时。

## 6. 中等难度面试题（含参考答案）

1. **问：为何梯度累积训练的损失要除以 K？** 答：若每个等大微批计算的 loss 已是均值，直接相加 K 次会把平均梯度放大 K 倍；除以 K 后得到该有效 batch 的样本平均梯度。若最后微批大小不等，应按样本数量而非微批个数加权。

2. **问：DDP + AMP + 梯度累积应如何排列通信、裁剪、step？** 答：同一有效 batch 内保持 GradScaler scale 不变；前 K-1 步用 no_sync，最后同步，累积完成后 unscale 再裁剪，scaler.step/ update 后才清零。对 skipped optimizer step 的学习率调度和 checkpoint 步数做额外记录。

## 7. 中等难度考试题（含解析）

1. **题：4 个 rank、每 rank 每次微批 8 样本、累积 4 次；global batch 是多少？** 解：`4 × 8 × 4 = **128**` 样本/更新，假设各 rank 等样本量且没有 drop_last/重复样本。

2. **题：单参数在两次微批平均梯度分别为 2 和 6，两个微批样本数相同；一次有效 batch 的平均梯度是多少？若大小是 3 与 1 呢？** 解：等大：`(2+6)/2=**4**`；大小为 3 与 1 且各值是各自样本均值时：`(3×2+1×6)/4=**3**`，直接平均两微步会错误得到 4。

## 8. 权威来源与延伸阅读

- [PyTorch AMP Gradient Accumulation Examples](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)：正确累积、AMP scale 更新与梯度裁剪顺序。
- [PyTorch DDP API](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)：使用 no_sync 降低重复同步的条件。

> 所有数值演算均以题设为准，不是特定 GPU、网络或框架版本的实测结果。
