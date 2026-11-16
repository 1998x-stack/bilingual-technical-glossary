# InfiniBand（无限带宽网络 · IB）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 024/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**InfiniBand**（无限带宽网络，IB）是指：常用于高性能计算集群的低延迟网络技术。

**理解边界：** 该术语在实际使用中须结合互连架构、协议、硬件代际和测量方式，而不能仅据标称速率推断性能。

## 2. 形象理解

InfiniBand 像专门为高性能计算集群规划的‘低等待专线网络’，传输大量小消息时很重视时延与可靠的端到端行为。不过不能把‘专线’误解为绝不会排队或故障。

## 3. 技术原理与核心内容

InfiniBand 是交换式互连体系，涵盖主机通道适配器（HCA）、交换网络、链路管理与 RDMA 传输。Subnet Manager 参与发现拓扑和配置转发表；分区等功能可用于隔离。采用 QP、CQ、MR 等 verbs 概念来组织工作队列与完成通知。部署中流控、路由与 QoS 也影响性能。

## 4. 工程实践与设计权衡

跨节点 All-Reduce 性能抖动时，先检查 IB 端口状态、链路速率、错误/重传计数、Subnet Manager 及交换路径，之后再观察 NCCL、MPI 应用层指标。多租户场景还须规划分区和访问权限，不能把‘RDMA 可以直接访存’当作无需授权。

## 5. 关联知识与易混辨析

InfiniBand 是互连架构/网络体系；RDMA 是远端内存访问能力，既可由 IB 承载，也可由 RoCE 等承载。IB 与 Ethernet 是不同网络技术，不能把‘InfiniBand = RoCE’。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 RDMA 不代表完全不使用 CPU？** 答：控制面仍需初始化 QP、注册内存和处理完成通知；硬件主要卸载数据搬运路径，并不是消除所有 CPU 工作。
2. **问：IB 网络低时延为何仍会出现训练长尾？** 答：链路拥塞、路径热点、重传、节点尾部计算延迟和同步屏障都会拉长端到端 step。

## 7. 中等难度考试题（含解析）

1. **题：传输 1 MiB 数据，假设网络有效 100 Gib/s、固定时延 3 μs，采用理想模型 T=α+bytes/B。总时间约多少？** 解：1 MiB=8,388,608 bit，带宽 100×2³⁰ bit/s，则序列化约 78.1 μs，总计约 81.1 μs；题设忽略协议/排队。
2. **题：Sub­net Manager 崩溃意味着现有 IB 通信立即全部中断吗？** 解：不必然。现有转发表与连接可能继续服务一段时间，但拓扑变更、恢复与管理可能受影响，依实现和故障形态判断。

## 8. 权威来源与延伸阅读

- [NVIDIA InfiniBand Switching Documentation](https://docs.nvidia.com/networking/display/NVIDIANVOSUserManualforInfiniBandSwitchesv25027002/InfiniBand-Switching)：原始规范、维护者文档或公开技术说明。
- [NVIDIA RDMA-Aware Networks Programming Guide](https://docs.nvidia.com/rdma-aware-networks-programming-user-manual-1-7.pdf)：原始规范、维护者文档或公开技术说明。

> 本文中示例速率、负载、时延和容量（如未指出具体设备）均为教学假设，不代表特定产品测量结果。涉及版本差异的结论以对应版本官方文档为准。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
