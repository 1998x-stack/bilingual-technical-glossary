# Data Loader（数据加载器）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 数据读写、缓存和负载口径需明确环境及版本

## 1. 核心定义

数据加载器（Data Loader）是训练/推理程序负责从数据源读取样本、采样、转换、批处理、并将数据交给模型执行循环的组件。以 PyTorch `torch.utils.data.DataLoader` 为例，它封装 Dataset/Sampler、batching、collation、workers、prefetch 与 memory pinning；不是持久化数据湖或通用数据管道的替身。

## 2. 形象理解

像工厂生产线前的配料工：按订单挑选原料、清洗、组盘、提前准备下一盘，然后把盘子送到 GPU 计算工位。每次模型训练等待配料，都会使昂贵设备闲置。

## 3. 技术原理与核心内容

Map-style Dataset 通过索引返回样本，Sampler 决定遍历顺序；IterableDataset 直接产生流式样本，分布式/多 worker 要负责分片。`num_workers>0` 可启用多进程读取/转换，`prefetch_factor` 是每 worker 预加载的 batch 数（默认通常为 2）；`persistent_workers=True` 在 epoch 间保留进程；`pin_memory=True` 用页锁定主机内存改善可支持设备的异步 H2D 路径。collate_fn 把多个样本合成为 batch，执行顺序、随机种子和 worker 重启会影响复现。

## 4. 工程实践与设计权衡

在 GPU step 100ms、DataLoader 单批 150ms 的情况下，未做重叠时 GPU 可能受数据输入瓶颈限制。逐层测文件 I/O、decode/tokenize、augment、collate、H2D copy、GPU kernel 时间与 idle gaps，调整 worker 数、batch 大小、pin_memory 和 prefetch；不要一味提高 worker 数，过多进程可能耗尽 RAM、文件描述符或远程 NFS 带宽。多机 DDP 要配 DistributedSampler/set_epoch 或自定义 IterableDataset sharding，确保样本语义。

## 5. 易混概念与边界

Dataset 定义样本访问，Sampler 定义样本索引顺序，DataLoader 负责迭代和组 batch；`prefetch_factor` 的单位是每 worker 的**batch**，不是样本数。`pin_memory` 帮助主机到 GPU 的拷贝路径，不会自动提升远程对象存储的带宽。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么增加 num_workers 后 epoch 反而变慢？** 答：多进程初始化、Python IPC、重复文件读取、远程共享存储拥塞和 CPU oversubscription 可能超过并发收益；按 CPU、I/O、GPU waiting 与内存峰值定位。

2. **问：IterableDataset 在 8-GPU DDP 下如何避免重复？** 答：按 global rank 和 worker ID 建立互斥 shard/record 范围，约定 epoch/seed 与重启进度；否则每个 rank 的 workers 可能读取同一源。

## 7. 中等难度考试题（含解析）

1. **题：num_workers=6、prefetch_factor=3，假设持续有效且每 worker 保持上限，最多预取多少 batches？** 解：`6×3=**18 batches**`；不包括当前用于计算的 batch，也不保证所有时刻都已装满。

2. **题：10,000 个样本、batch_size=128、drop_last=False，忽略采样器变化，一个 epoch 需要多少 batches？** 解：`ceil(10000/128)=**79 batches**`，其中最后一批不足 128。

## 8. 权威来源与延伸阅读

- [PyTorch DataLoader reference](https://docs.pytorch.org/docs/stable/data.html)：用于核对资料机制、测量定义与实现约束的资料。
- [PyTorch Data Loading source](https://github.com/pytorch/pytorch/blob/main/torch/utils/data/dataloader.py)：用于核对资料机制、测量定义与实现约束的资料。
- [PyTorch DistributedSampler reference](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.distributed.DistributedSampler)：用于核对资料机制、测量定义与实现约束的资料。

> 示例计算使用明确的理想条件，不等于某个生产系统的实测结果。
