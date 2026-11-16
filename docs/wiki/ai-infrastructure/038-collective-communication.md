# Collective Communication（集合通信）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 038/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**Collective Communication**（集合通信）：多个计算参与者协作完成的数据交换操作。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

集合通信像一组乐手按统一指挥完成协同：有人负责把信号广播给全体，有人把各声部汇总，再把结果发回。所有参与者需要按兼容的步骤出场，否则可能陷入互相等待。

## 3. 技术原理与核心内容

Collective Communication 是进程/设备群体共同参与的通信原语，典型操作有 Broadcast、Reduce、All-Reduce、All-Gather、Reduce-Scatter、All-to-All 与 Barrier。操作语义规定每个 rank 需要交付/接收的数据及同步关系；具体实现可采用树、环、分层或拓扑感知算法。通信成本常以固定延迟 α、每字节传输成本 β 和规约计算成本 γ 近似分析。

## 4. 工程实践与设计权衡

在混合并行系统中，先为每个 process group 明确成员与 rank 顺序，再确认 collective 调用序列一致。调试 hang 需检查某个 rank 是否没进入操作、count/dtype 不匹配，或进程在通信之前发生异常；还需核对网络、驱动和调度超时。

## 5. 关联知识与易混辨析

集合通信强调多参与者协作，不等于点对点 send/recv。Barrier 主要协调执行进度，不传输模型梯度；All-Reduce 既传输又规约，而 Broadcast 只复制 root 数据。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么某个 rank 早退会导致其它 rank 在集合通信中挂住？** 答：参与者需要按相容顺序发起操作；缺失一方可能让其余 rank 等待无法完成的通信。
2. **问：如何在 NCCL 和 MPI 中思考 collective 的区别？** 答：二者均提供部分集合原语，但适配设备/通信栈及 API 不同；NCCL 对 GPU 通信/拓扑优化突出，MPI 更通用。

## 7. 中等难度考试题（含解析）

1. **题：6 个 rank，每个都有 1 MB 数据，希望所有 rank 拿到相同拼接后的 6 MB 数据，选哪个操作？** 解：All-Gather；若想把相同位置相加得到 1 MB 则用 All-Reduce。
2. **题：想把 root 的 256 KiB 配置分发到其它 7 个 rank，选哪种 collective？** 解：Broadcast；Root 本就持有源数据，广播后其他 rank 收到相同配置。

## 8. 权威来源与延伸阅读

- [NVIDIA NCCL Collective Operations Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)：用于校对通信定义、技术条件与实现范围。
- [NVIDIA NCCL Collective APIs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/colls.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
