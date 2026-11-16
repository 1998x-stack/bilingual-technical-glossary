# Checkpoint（训练检查点）

> 学科：AI Infrastructure · 专题：分布式训练 · 学习内容与发布状态由统一 Explorer 管理

## 1. 核心定义

训练检查点（Checkpoint）是训练过程中持久化一组足以恢复进度的模型及运行状态的文件/对象集合，包括参数、优化器状态、学习率调度、混合精度 scaler、随机数状态和必要的数据迭代位置。只保存权重可用于推理或微调起点，通常**不能保证精确恢复同一条优化轨迹**。

## 2. 形象理解

长途旅行记录地点、车辆状态、燃油、路线和导航进度，下一次才能从原位置继续；只拍一张车辆外观照片不足以知道剩余油量或已走过的道路。分布式训练还要把多台车的状态保持在同一个逻辑时刻。

## 3. 技术原理与核心内容

典型完整恢复需 `model.state_dict`、`optimizer.state_dict`、LR scheduler、`GradScaler`（如用 AMP）、训练 step/epoch、CPU/GPU RNG、采样器/数据迭代状态以及模型/词表配置。分布式 checkpoint 允许每个 rank 并行写入 shard，并可在加载时按新 rank 布局重新分片；写入期间必须保证逻辑一致的全局步骤。实际文件写出宜采用临时目录 → 完整性校验 → 原子性发布 manifest 或目录指针的方式，避免故障时载入半写完的文件；对象存储的发布可见性应遵循对应存储语义。

## 4. 工程实践与设计权衡

长训练作业选择频率时，要权衡写入 I/O、存储保留量、故障概率和可接受的重算窗口。把 checkpoint 目录与代码提交、数据版本、tokenizer 和 optimizer 配置关联；实际演练从不同 GPU 数量恢复、校验模型参数 hash 与前几步损失一致性。对于 FSDP/TP 的模型，不要假设单 rank 的 `torch.save` 能独立保存全部模型。

## 5. 易混概念与边界

**Checkpoint（训练恢复快照）**与**Gradient Checkpointing（训练期激活重计算）**用途不同：前者消耗存储和 I/O 换容错，后者消耗额外计算换激活显存。训练 checkpoint 也不必与生产部署的模型快照/推理权重格式一致。

## 6. 中等难度面试题（含参考答案）

1. **问：仅保存模型权重是否足以精确恢复 Adam 训练？** 答：通常不足够。Adam 的一阶/二阶矩和 step 影响下一次更新，LR scheduler、GradScaler、RNG 和 sampler 状态也影响后续轨迹。只加载参数一般是从一个初始化状态继续优化，而非恢复完整训练。

2. **问：分布式 checkpoint 如何避免某一 rank 写失败导致全局文件损坏？** 答：采用协调后的逻辑 step、每 rank shard 的写入确认及统一 manifest 发布，只有所有必要 shard 成功后将 checkpoint 标记可用。存储后端需支持相应原子性/一致性协议，恢复时验证完整性。

## 7. 中等难度考试题（含解析）

1. **题：8 个 rank 各保存 1.5 GiB 的互不重叠 shard，忽略冗余和元数据，一次 checkpoint 原始总体积是多少？** 解：`8×1.5=**12 GiB**`。单个 rank 的 1.5 GiB 文件不能独立恢复全部模型。

2. **题：故障发生位置在相邻两次 checkpoint 间服从均匀分布，checkpoint 间隔 20 分钟；期望损失的重算时间是多少？最大损失多少？** 解：期望 `20/2=**10 分钟**`，最大接近 **20 分钟**。这是在题设故障均匀且无额外持久日志下的简化结果。

## 8. 权威来源与延伸阅读

- [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html)：多 rank shard 保存/加载、reshard 与 API 语义。
- [PyTorch Elastic Train Script](https://docs.pytorch.org/docs/main/distributed/elastic/train_script.html)：故障重启后恢复模型与训练进度的必要逻辑。

> 示例值均为有明确前提的教学假设；不同运行时、模型和硬件条件下的实际量测结果可能变化。
