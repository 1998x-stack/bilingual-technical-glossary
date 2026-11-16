# 分布式训练与在线推理的工程知识链

> **内部研究路径，仅用于作者整理前后依赖；不是公开站点导航。** 公开读者一律从 TERM/ATLAS 的 Explorer 点击术语进入详情；本文件中的组号仅对应仓库内的研究组织。

## 从并行维度建立训练系统

1. 先阅读 [DDP](041-distributed-data-parallel.md)，确认 DP 将不同样本交给复制模型；再读 [TP](042-tensor-parallelism.md)、[PP](043-pipeline-parallelism.md)、[EP](044-expert-parallelism.md)、[SP](045-sequence-parallelism.md)，区分按参数、层深度、专家、序列切分的边界。
2. 组合为 [Hybrid Parallelism](046-hybrid-parallelism.md)，以每 rank 权重、激活和通信估算规划设备组；不要未经证明就把所有维度当成完全正交。
3. 比较 [FSDP](047-fully-sharded-data-parallel.md) 和 [ZeRO](048-zero-redundancy-optimizer.md) 的权重、梯度和优化器状态分片；结合网络 bandwidth/bucket profiler 诊断通信成本。

## 训练显存、数值与容错

4. 解释 [梯度累积](049-gradient-accumulation.md)、[梯度检查点](050-gradient-checkpointing.md)、[激活重计算](051-activation-recomputation.md) 解决的分别是更新频率与激活峰值，避免将这些都写成“分片参数”。
5. 对比 [混合精度训练](052-mixed-precision-training.md)、[损失缩放](053-loss-scaling.md) 的 FP16/BF16 数值边界，再计算 [微批次](054-microbatch.md) 与 [全局批量](055-global-batch-size.md) 的样本数；特别检查 DP/TP/PP 的倍数关系。
6. 通过 [训练检查点](056-checkpoint.md) 和 [弹性训练](057-elastic-training.md) 设计可恢复作业；定位同步并行中的 [慢节点](058-straggler.md)。

## 从训练走向推理服务

7. [Inference Server](059-inference-server.md) 负责请求队列、后端执行和监控；[Model Serving](060-model-serving.md) 额外涉及版本路由、安全、灰度与回滚。后续延伸到 TTFT、TPOT、KV Cache 和持续批处理。

## 需要答对的五个工程问题

- 64 GPU 在 TP=4、PP=2 时，DP 为 8；为何 global batch 不应再乘 64？
- ZeRO-3/FSDP 在参数内存下降后，为什么仍可能在 all-gather 或激活处 OOM？
- BF16 是否与 FP16 具有相同动态范围？为什么 FP16 往往需要 loss scaling？
- 当一张 GPU 比其它 7 张慢 60 ms，诊断该 rank 的计算与网络等待该如何区分？
- 为什么推理服务器能返回推理输出，却不等于完整的模型服务生命周期？

## 权威资料

- [Megatron Core Parallelism Strategies](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)
- [PyTorch DistributedDataParallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)
- [PyTorch FSDP](https://docs.pytorch.org/docs/main/fsdp.html)
- [DeepSpeed ZeRO](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/_tutorials/zero.md)
- [PyTorch AMP](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)
- [Triton Inference Server Architecture](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html)
