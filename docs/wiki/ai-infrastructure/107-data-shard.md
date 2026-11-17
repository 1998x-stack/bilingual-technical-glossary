# Data Shard（数据分片）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 数据读写、缓存和负载口径需明确环境及版本

## 1. 核心定义

数据分片（Data Shard）是把一个数据集按稳定规则切为多个可独立传输、处理或分配的子集/文件单元。目的通常是分布式读写并行、局部恢复、减少随机对象请求与保证各训练 rank 的样本范围可追踪；不同于把张量沿模型维度切分的 TP，也不同于存储副本。

## 2. 形象理解

像将一本巨型书按章节打成若干册，读者分组可以并行阅读；分册过小导致每次都要找书、借还，分册过大则单个读者工作不均，坏一册要重新处理很多页。

## 3. 技术原理与核心内容

分片可以按 key hash、时间、范围或固定大小打包；例如数据集 N 个样本分 K 个 shard，理想均匀时每 shard 约 N/K。分布式训练需协调 `world_size`、`rank`、worker IDs、epoch shuffle 和样本去重，确保数据分配不重叠且整体覆盖。PyTorch DistributedSampler 的 dataset size 常假设恒定且同序；若不能整除 world_size，常通过补样本或 drop_last 处理，这会影响确切“每样本一次”的保证。IterableDataset 多 worker 必须人工分配不同输入范围，避免复制数据。

## 4. 工程实践与设计权衡

WebDataset/tar shard、Parquet row group、对象存储 key shard 在大规模训练读取中常用于减少 metadata/open 开销。根据网络、GPU batch、解码 CPU 与失败重跑成本选择 128MiB–数 GiB 的实验范围，不能当成统一经验最佳值。建立 manifest 映射 `shard_id→checksum/record_count/size`，用 deterministic seed 决定 epoch 顺序；对 shard 内样本还可二次 shuffle，防止分片顺序偏差。

## 5. 易混概念与边界

数据 shard 是逻辑样本/文件划分；存储系统 striping 是同一文件跨多个磁盘目标的布局；replication 是多个副本，不能等同 shard。DDP 的 sample shard 和 ZeRO 的 optimizer-state shard 处于不同层级。

## 6. 中等难度面试题（含参考答案）

1. **问：IterableDataset 在 4 个 DataLoader workers 中为什么容易重复样本？** 答：每个 worker 得到数据集对象副本，若迭代逻辑没有按 worker_id/rank 过滤，四个进程可能从相同起点读完整流。应在 `get_worker_info()` 或 worker_init 中进行分片。

2. **问：世界大小改变后为什么旧 shard-to-rank 映射可能不能直接复用？** 答：原先的取模或连续分区会重新分配样本，可能重复/遗漏并破坏 checkpoint 的进度对应；需要统一 epoch/step cursor、稳定 shard IDs 或重平衡协议。

## 7. 中等难度考试题（含解析）

1. **题：有 12,288,000 样本，平均每 shard 2048 条，需多少 shard？** 解：`12288000/2048=**6000 shards**`。

2. **题：100 个 shard 按 `shard_id % 8` 赋予 8 个 ranks，最繁忙 rank 比最空闲 rank 多几个 shard？** 解：100=8×12+4，因此四个 rank 得到 13 个、四个得到 12 个，最多差 **1 个 shard**。

## 8. 权威来源与延伸阅读

- [PyTorch DistributedSampler](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.distributed.DistributedSampler)：用于核对资料机制、测量定义与实现约束的资料。
- [PyTorch IterableDataset](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.IterableDataset)：用于核对资料机制、测量定义与实现约束的资料。
- [WebDataset repository](https://github.com/webdataset/webdataset)：用于核对资料机制、测量定义与实现约束的资料。

> 示例计算使用明确的理想条件，不等于某个生产系统的实测结果。
