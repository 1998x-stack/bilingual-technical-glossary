# All-to-All（全互换通信）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 037/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**All-to-All**（全互换通信）：参与节点彼此交换各自数据块的集合通信操作。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

All-to-All 不只是让大家收到相同通知，而是 4 个仓库互相给不同目的地寄包：每个仓库对每个其它仓库的包裹都不一样。MoE 专家路由的数据交换常属于这一类。

## 3. 技术原理与核心内容

在 All-to-All 中，每个 rank 把输入分成发往每个目标 rank 的分片，并从所有源 rank 接收相应片段。Equal-split 形式通常要求每个进程发送/接收相同规格的数据块，变长 token 路由可使用支持不同 split size 的框架接口。通信对数随进程数增长，有向跨 rank 消息对数为 `p(p−1)`，但具体物理发送量与聚合策略需区分。

## 4. 工程实践与设计权衡

MoE 模型在 expert parallelism 下通常通过 All-to-All 分发 token 到专家，再交换输出。要测单步 token 数、专家负载均衡、每个 rank 最大接收量与 p99，避免某些专家过热导致队列和显存峰值。调优路径包括路由负载均衡、top-k 策略、分组通信、拓扑感知放置。

## 5. 关联知识与易混辨析

All-to-All 的每位接收者拿到的是不同发送者的指定数据，不等同 All-Reduce 的聚合同结果，也不同于 All-Gather 的全量相同拼接结果。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 MoE 使用 All-to-All 时，即使网络总带宽充足也可能慢？** 答：token 分配可能不均，使某个目标 rank 成为接收热点；同步阶段由最慢 rank 决定，还受流控与内存峰值限制。
2. **问：All-to-All 和 All-Gather 哪个更适合把不同 token 分配到专家？** 答：All-to-All 能将不同 token 发到指定 rank；All-Gather 会向所有 rank 复制所有数据，通常造成不必要的数据复制。

## 7. 中等难度考试题（含解析）

1. **题：p=4，按有向进程对统计（不计自己发给自己），共有多少发送方向？** 解：p(p−1)=4×3=12 个有向方向。
2. **题：4 个 rank 每个给其它 3 个 rank 发送 32 MiB，有效跨 rank 发送总量是多少？** 解：4×3×32=384 MiB；每 rank 对外发送 96 MiB，不包含本地自拷贝。

## 8. 权威来源与延伸阅读

- [NVIDIA NCCL Collective Operations Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)：用于校对通信定义、技术条件与实现范围。
- [NVIDIA NCCL Collective APIs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/colls.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
