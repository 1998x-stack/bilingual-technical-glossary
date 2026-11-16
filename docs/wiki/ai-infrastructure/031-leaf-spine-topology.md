# Leaf-Spine Topology（叶脊网络拓扑）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 031/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**Leaf-Spine Topology**（叶脊网络拓扑）：数据中心常见的多路径、低跳数网络架构。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

把 Leaf 看成接入服务器的街区出口，把 Spine 看成连通所有街区的快速干道。Leaf 通常不直接横连其它 Leaf，同一 Leaf 下的主机本地交换；跨 Leaf 的包经上层 Spine 转发。多个 Spine 让路径选择更丰富。

## 3. 技术原理与核心内容

典型双层 Clos/Leaf-Spine 网络由接入服务器的 Leaf 交换机和提供 Leaf 间互连的 Spine 交换机构成，常见做法是每个 Leaf 连接每个 Spine。通过 ECMP 可在多个等价下一跳分摊流量，但通常以五元组哈希做逐流分流，单个巨流未必平衡分摊。下行与上行总带宽的比值决定过订阅程度；Leaf-Spine 不保证天然无阻塞。

## 4. 工程实践与设计权衡

AI 训练网络规划先列节点的 NIC 速率与流量矩阵，再决定 Leaf 上下行端口数/速率，检查 oversubscription ratio、ECMP entropy、端口缓冲、PFC/ECN 和多平面冗余。多机 All-to-All 常出现持续大流，可用端口占用热力图而非只看平均利用率。

## 5. 关联知识与易混辨析

Leaf-Spine 是典型两层 Clos 拓扑的一种部署模式，不等于‘所有 Fat-tree’，也不等于 VLAN 或 VXLAN。拓扑描述物理/逻辑连接关系，路由与拥塞控制是另外的层面。

## 6. 中等难度面试题（含参考答案）

1. **问：相同链路带宽下，为什么增加 Spine 可以提高网络弹性但不总提升单流速度？** 答：多 Spine 增加可选路径和上行聚合容量，但单流常被 ECMP 哈希固定到一条路径。吞吐受其所在路径与端口限制，改善主要体现在多流聚合和故障绕行。
2. **问：为什么按平均 40% 链路利用率判断网络不拥塞可能是错的？** 答：集合通信存在同步突发，部分特定 Leaf↔Spine 链路/队列可能瞬间跑满，导致排队、ECN 和 tail latency；应看热点和高分位数。

## 7. 中等难度考试题（含解析）

1. **题：每台 Leaf 下联 8×100 Gb/s，上联到 4 台 Spine 各 100 Gb/s，忽略开销，过订阅比（下行总带宽:上行总带宽）？** 解：(8×100):(4×100)=800:400=2:1；表示所有主机同时跨 Leaf 发包时可能争用上联。
2. **题：在上述网络中 4 台 Spine 中故障 1 台，其余速率不变，Leaf 上联总容量如何变化？** 解：从 400 降到 300 Gb/s，降幅 25%，过订阅比由 2:1 变为 800:300≈2.67:1；还要考虑重收敛。

## 8. 权威来源与延伸阅读

- [NVIDIA Cumulus Leaf-Spine Clos Topology](https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/Introduction/)：用于校对通信定义、技术条件与实现范围。
- [NVIDIA NCCL Networking Troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
