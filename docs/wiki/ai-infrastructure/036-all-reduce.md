# All-Reduce（全归约通信）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 036/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**All-Reduce**（全归约通信）：分布式工作节点共同归约数据并获得结果的集合通信操作。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

四名同学各自算出一部分梯度，先把四份答案加起来，再让每个人拿到同一份总结果，这就是 All-Reduce；它既要‘合并’，又要‘把结果送回所有人’。

## 3. 技术原理与核心内容

All-Reduce 对所有 rank 的同形状张量应用一个规约运算（如 sum）后，将结果分发回每个 rank。经典 Ring All-Reduce 可以概念上分为 Reduce-Scatter + All-Gather；对 p 个 rank、每 rank 输入消息大小 S，忽略其它因素，环算法单 rank 的发送字节量约为 `2(p−1)S/p`，通信阶段数为 `2(p−1)`；低消息量时延项较重要，大消息时带宽项重要。

## 4. 工程实践与设计权衡

在 DDP 梯度同步中，All-Reduce 是关键通信模式之一。排查时先确认 rank 数、bucket 大小、每步参与的梯度字节数、网络拓扑与 overlap，使用 NCCL tests 测实际吞吐。浮点求和由于计算顺序不同，结果不一定 bitwise 可复现；还需保证相同 datatype/count 和 collective 调用顺序。

## 5. 关联知识与易混辨析

All-Reduce ≠ Reduce：后者只在 root 获得结果；All-Reduce ≠ All-Gather：后者拼接所有数据而不做规约。Ring 仅是一种算法，NCCL 可能按拓扑/消息大小选择其他实现。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 All-Reduce 的小消息优化与大消息优化策略不同？** 答：小消息主要看启动与轮次数，减少步骤/合并消息有帮助；大消息主要看链路带宽、分片流水和拓扑映射。
2. **问：为什么 DDP 训练可以使用平均梯度而不仅仅使用求和？** 答：各 rank 计算局部批次梯度，按全局批次样本数加权合并后获得等效平均；必须考虑每卡样本数与 loss reduction 口径，不能一概直接除 world_size。

## 7. 中等难度考试题（含解析）

1. **题：4 个 rank 各提交标量 1、2、3、4，sum All-Reduce 后每个 rank 的输出？** 解：四个 rank 都得到 1+2+3+4=10；若要平均则每个 rank 再除以 4。
2. **题：环 All-Reduce，p=8、S=800 MiB，按 `2(p−1)S/p` 计算每 rank 发送字节量？** 解：2×7/8×800=1400 MiB（约 1.367 GiB），忽略协议开销与可能重传。

## 8. 权威来源与延伸阅读

- [NVIDIA NCCL Collective Operations Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)：用于校对通信定义、技术条件与实现范围。
- [PyTorch DDP Internals Design Note](https://docs.pytorch.org/docs/stable/notes/ddp.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
