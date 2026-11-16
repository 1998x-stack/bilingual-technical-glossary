# Elastic Training（弹性训练）

> 学科：AI Infrastructure · 专题：分布式训练 · 学习内容与发布状态由统一 Explorer 管理

## 1. 核心定义

弹性训练（Elastic Training）指分布式训练作业可以在工作进程/节点失败或资源可用数量变化后，通过重新协调成员关系和恢复状态继续完成训练。它并不代表进程可以在任意一条 GPU kernel 中途无损迁移，也不自动保证改变 worker 数之后学习率和样本顺序的语义不变。

## 2. 形象理解

施工队人数从 8 人变成 4 人时，必须重新划分任务并从准确的施工记录恢复，而不是直接把手上的半成品无缝转移。团队人数改变后，任务完成总量和工作速度都可能变化。

## 3. 技术原理与核心内容

弹性启动器（如 `torchrun --nnodes=min:max --rdzv-backend=c10d`）协调成员加入、退出和进程重启；`RANK`、`WORLD_SIZE` 可能重排。程序必须能重新初始化 process group、重新建立分布式采样器并根据最新保存状态恢复。若本轮进程发生故障，通常重新启动 worker 并从最近成功 checkpoint 重做部分工作，而非保持失败前内存中的所有激活。固定 microbatch 和 accumulation 不变时，DP world size 变化会改变 global batch；需明确是否按目标值调整累积步数或采样策略。

## 4. 工程实践与设计权衡

共享/可扩缩容 GPU 池中用带 `min:max` 的 rendezvous 测试增加/删除节点；通过模拟 rank 故障验证通信重组、数据去重或重复、checkpoint 原子性、训练 loss 轨迹和重新分片开销。记录 membership event、restart count、丢失 step、effective batch 以及恢复后吞吐。对 TP/PP 固定组且仅 DP 弹性变化的实现更容易管理；并非任意混合并行维度都支持动态伸缩。

## 5. 易混概念与边界

**Elastic Training** 是动态成员/容错训练能力，**Autoscaling** 是资源控制策略，可触发弹性但本身不能恢复梯度或优化器状态。**Fault tolerance** 还可能采用固定 rank 重启，并不一定支持 world size 变化。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么弹性训练修改 world size 后不能直接继续按旧 global batch 参数工作？** 答：若每 rank 的样本数与累积步数固定，DP 副本数变化会改变每次更新所见样本；loss 归约和 LR schedule 语义改变。还须重建采样器和通信组，验证 checkpoint 是否能 reshard。

2. **问：torchrun 弹性重启时怎样尽可能避免重复消耗训练样本？** 答：把训练进度、采样器状态和数据版本随 checkpoint 持久化；恢复时按新 rank 分配尚未完成的数据片段，必要时做幂等处理并记录重复样本。只记录 epoch 不足以处理流式数据的精确位置。

## 7. 中等难度考试题（含解析）

1. **题：初始 DP=4，每 rank microbatch=2、累积 K=4；扩成 DP=8 时保持其它不变，global batch 变为多少？** 解：初始 `4×2×4=**32**`；扩容后 `8×2×4=**64**`。如果目标始终是 32，则需把 K 降为 `32/(8×2)=**2**`。

2. **题：每 10 分钟成功保存 checkpoint，某次故障发生在保存后第 7 分钟，且没有其它持久进度；至少需重新计算多久的工作？** 解：简化理想情况下丢失最近 **7 分钟** 的未保存训练；另有 worker 重启、读取 checkpoint 和重新 rendezvous 的额外耗时。

## 8. 权威来源与延伸阅读

- [PyTorch torchrun Elastic Launch](https://docs.pytorch.org/docs/stable/elastic/run.html)：可变 nnodes、rendezvous 和失败重启。
- [PyTorch Elastic Train Script](https://docs.pytorch.org/docs/main/distributed/elastic/train_script.html)：成员变化后的 checkpoint 恢复与进程组重新初始化。

> 示例值均为有明确前提的教学假设；不同运行时、模型和硬件条件下的实际量测结果可能变化。
