# Data Parallelism（数据并行 · DP）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 040/142 · 专题：分布式训练 · 研究日期：2026-11-16

## 1. 核心定义

**Data Parallelism**（数据并行，DP）：多个设备处理不同训练样本并同步模型参数或梯度。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

数据并行就像让四个小组各拿相同的教材（模型），分别批改不同的试卷（样本），再把各组的修改建议（梯度）汇总，下一轮所有小组仍持有一致的新教材。

## 3. 技术原理与核心内容

Data Parallelism 将输入训练样本切分到多个工作节点，各节点持有一个完整模型副本并运行前向/反向；常规同步 DP 在更新参数前聚合梯度。若各 rank 的 microbatch 相同、每个样本等权且 loss 是样本平均，平均梯度可与单机的全局 batch 梯度等价。PyTorch DDP 把梯度划分为 bucket 并触发 all-reduce，可与部分 backward 计算重叠。数据并行与模型/张量并行的资源结构不同。

## 4. 工程实践与设计权衡

8 卡 DDP，每卡 microbatch=4、梯度累积 2 次，则一次 optimizer step 的 global batch=8×4×2=64（若无其它分片语义）。用 DistributedSampler 防止每个 rank 重复读取同样样本；对 batchnorm、随机种子、loss normalization、uneven inputs、梯度裁剪和最后不满 batch 等情形需仔细核对。

## 5. 关联知识与易混辨析

DP 不等于 DDP：前者是并行策略，后者是具体分布式框架/实现。DP 复制模型，会受每卡显存约束；FSDP/ZeRO 通过分片降低冗余而不是简单的纯副本式 DP。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么一份模型复制到更多 GPU 后，单卡显存占用不一定下降？** 答：每卡依然存全量参数及相关梯度/优化器状态，增加 GPU 主要分摊数据与计算；显存优化常需分片、量化或重计算。
2. **问：如果各卡局部 batch 数不同，直接平均 rank 梯度是否等同全局样本平均？** 答：不一定。应按每卡有效样本数加权，否则小 batch 的 rank 被过度加权；还要处理 loss reduction 和 padding 口径。

## 7. 中等难度考试题（含解析）

1. **题：8 张 GPU，每张每 microbatch 6 个样本，累积 3 个 microbatch 后更新，全局 batch 大小？** 解：8×6×3=144 个样本/step；假设每个 rank 样本数相同且累积只更新一次。
2. **题：两卡分别用 batch 2 与 batch 6，得到样本平均梯度 g1=2、g2=6。正确全局样本平均梯度？** 解：按样本数加权 `(2×2+6×6)/(2+6)=5`，不能直接 `(2+6)/2=4`。

## 8. 权威来源与延伸阅读

- [PyTorch DistributedDataParallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)：用于校对通信定义、技术条件与实现范围。
- [PyTorch DDP Internals Design Note](https://docs.pytorch.org/docs/stable/notes/ddp.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
