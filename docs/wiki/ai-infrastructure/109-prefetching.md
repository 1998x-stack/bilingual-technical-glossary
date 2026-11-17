# Prefetching（预取）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 数据读写、缓存和负载口径需明确环境及版本

## 1. 核心定义

预取（Prefetching）是在消费者真正需要数据之前，依据预测或已知顺序提前发起读取、解码或传输，以便将 I/O 等待与当前计算重叠。预取可应用于操作系统 page cache、训练 DataLoader、对象存储 shard 缓存和 GPU H2D 拷贝。它优化的是**等待链路与重叠**，并不凭空增加存储介质带宽。

## 2. 形象理解

厨师炒当前一道菜时，助手提前洗好下一道菜的蔬菜；如果订单稳定，厨师几乎无需等待。若助手准备了大量后来取消的菜，则浪费材料、桌面与水电。

## 3. 技术原理与核心内容

设当前 batch 的计算时间 C、下个 batch 的预取+解码+传输耗时 I。理想双缓冲、无资源竞争且已填满流水线的稳态 step 下界约 `max(C,I)`，而串行执行约 `C+I`。实际重叠依赖 CPU workers、线程/进程队列、pinned memory、GPU stream dependency 和同步边界。预取窗口越大，RAM/NVMe cache 与在途请求越多；过深可能形成无用读取、过时输入和长尾阻塞。

## 4. 工程实践与设计权衡

对训练管道逐层监控 prefetch queue depth、batch ready 时间、H2D DMA、GPU idle、cache misses、readahead 命中和内存/文件描述符占用。通过双缓冲、多 DataLoader workers、异步 I/O 或有界 shard 缓存实现受控预取；同一节点多个训练作业并发时设置总读带宽/内存预算，防止大家预取造成共享 NFS/对象存储拥塞。

## 5. 易混概念与边界

Prefetching 是**提前请求**，Caching 是**保留已取得的数据用于复用**；二者可以组合。CPU page cache readahead 与模型 autoregressive speculative decoding 都是预测工作，但前者预读字节、后者预测 token，不能混为一谈。

## 6. 中等难度面试题（含参考答案）

1. **问：何时深度预取反而降低性能？** 答：I/O 带宽有限、数据访问不稳定、prefetch 缓存挤占其它工作集或 queue 太深导致头部阻塞时，未被使用的数据浪费带宽并拉高 P99。

2. **问：为什么 DataLoader 预取已满时 GPU 仍可能空闲？** 答：H2D copy、同步 CUDA stream、最后一批 collate、CPU 解码瓶颈或 DDP collective 可能仍在关键路径上；预取队列仅证明数据在某个层级准备就绪。

## 7. 中等难度考试题（含解析）

1. **题：单批数据准备 70ms、GPU 计算 100ms，理想完全重叠与完全串行的稳态 step 分别多少？** 解：重叠为 `max(70,100)=**100ms**`，串行为 `70+100=**170ms**`，理论最多节省 70ms/step。

2. **题：预取窗口 12 batches，每 batch 80MiB，忽略元数据与共享，理论在途缓冲多少 MiB？** 解：`12×80=**960MiB**`；实际还可能有重复 pinned buffers 和 worker 进程内存。

## 8. 权威来源与延伸阅读

- [PyTorch DataLoader prefetch_factor](https://docs.pytorch.org/docs/stable/data.html)：用于核对资料机制、测量定义与实现约束的资料。
- [Linux block device read-ahead](https://docs.kernel.org/admin-guide/blockdev/index.html)：用于核对资料机制、测量定义与实现约束的资料。
- [NVIDIA CUDA Runtime API async memory copies](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__MEMORY.html)：用于核对资料机制、测量定义与实现约束的资料。

> 示例计算使用明确的理想条件，不等于某个生产系统的实测结果。
