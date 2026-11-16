# Model Sharding（模型分片）

> 学科：AI Infrastructure · 专题：推理与服务 · 具体实现应核对官方接口及版本

## 1. 核心定义

模型分片（Model Sharding）指把一个模型的参数、层或专家切分到多设备/进程/存储位置，使单设备不必保存或执行整个模型。推理系统中常见的是张量并行、流水线并行或专家并行，训练系统还可能将梯度和优化器状态纳入分片。仅分割文件在磁盘上的位置，不自动意味着运行计算也跨设备分布。

## 2. 形象理解

一套大型百科书分配给四家图书馆保存，单馆只管一部分；若查阅一篇文章横跨几馆，就必须协调借书和结果组合。减少单馆存储压力的同时增加跨馆通信，这种代价与分片维度密切相关。

## 3. 技术原理与核心内容

按 Transformer 层切分（PP）时，激活需在 stage 之间发送；按单层权重/输出通道切分（TP）时，需 all-gather/reduce-scatter/all-reduce 等通信还原结果；按专家切分（EP）时，token 路由经 all-to-all 抵达对应 expert。推理期权重分片与训练期 FSDP/ZeRO 的优化器状态分片不是同一问题。理论每 rank 原始权重可降到 `W/p`，但显存还含 KV cache、跨分片 buffer、activation 和某些复制的 embedding/heads。

## 4. 工程实践与设计权衡

在 4 台 GPU 单台放不下 40 GiB 权重时，优先测是否有足够高速互连与 backend 支持的 TP=2/4，再考虑按层 PP；检查模型尺寸是否满足分片轴整除、并行组初始化、Tokenizer/权重版本一致与 checkpoint 格式。记录每卡 allocated 峰值、跨设备发送字节、输出吞吐和尾时延；分片数增大不保证线性加速。

## 5. 易混概念与边界

Model sharding 是总称，不只等于 TP 或模型文件拆分。DP 会复制相同模型处理不同数据；FSDP 可能训练时按需 all-gather 参数，推理 TP 则每一步都共同参与同一层计算。

## 6. 中等难度面试题（含参考答案）

1. **问：模型放不进单卡但跨机带宽低，应如何选择分片方式？** 答：先评估层间 activation 体积与 TP 每层集合通信体积；同机高速链路更适合频繁 TP，跨机可考虑 PP，实际仍需根据模型层数与网络拓扑 benchmark。

2. **问：为什么四卡分片后每卡显存未降为原来的四分之一？** 答：embedding、输出头、临时通信和 KV Cache 不一定均分；kernel workspace、block allocator 与不等分层也产生峰值。

## 7. 中等难度考试题（含解析）

1. **题：原始权重 48 GiB，假设精确均匀切到 6 GPU 且无复制，平均每 GPU 权重体积？** 解：`48/6=**8 GiB**`，不包括激活/KV 和通信。

2. **题：模型有 24 层、每层理想同成本，PP=4 且整层切分，平均每 stage 几层？** 解：`24/4=**6 层**`。实际层计算/显存通常不完全相等。

## 8. 权威来源与延伸阅读

- [vLLM Distributed Serving](https://docs.vllm.ai/en/latest/serving/distributed_serving/)：用于核对相关技术机制与版本边界的官方资料。
- [Megatron Core Parallelism Guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)：用于核对相关技术机制与版本边界的官方资料。

> 题中数字为教学假设，不是任何设备、服务或容器环境的真实压测结果。
