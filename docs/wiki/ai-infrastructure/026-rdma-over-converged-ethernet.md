# RDMA over Converged Ethernet（融合以太网上的 RDMA · RoCE）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 026/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**RDMA over Converged Ethernet**（融合以太网上的 RDMA，RoCE）是指：在以太网基础设施上实现 RDMA 的协议族。

**理解边界：** 该术语在实际使用中须结合互连架构、协议、硬件代际和测量方式，而不能仅据标称速率推断性能。

## 2. 形象理解

RoCE 可以理解为‘在现有以太网公路上提供 RDMA 的专门货运服务’，基础道路仍是 Ethernet，但要求更精心地治理拥塞；否则车越多反而排得越久。

## 3. 技术原理与核心内容

RoCE 把 RDMA 传输映射到以太网。RoCEv1 基于二层，不支持通常的 L3 路由跨网段；RoCEv2 采用 UDP/IP 封装，能够经过三层路由。生产网络常通过 ECN、CNP、PFC 与 QoS 协调拥塞控制；‘必须全网完全无丢包’不是描述所有 RoCE 部署的准确说法，具体取决于网卡与交换机能力及拥塞方案。

## 4. 工程实践与设计权衡

训练时长尾上升，若是 RoCE fabric，先看网卡/交换机的丢包、ECN 标记、PFC pause、重传和队列排队统计，再和 all-reduce latency 关联。排查时避免把 PFC 全局打开当作万能修复，因为可能触发 pause storm、头阻塞或死锁风险。

## 5. 关联知识与易混辨析

RoCE 是在 Ethernet 上实现 RDMA 的协议族，不是与 Ethernet 对立的另一种物理线路；RoCE 与 InfiniBand 都可支持 RDMA，但网络管理/链路协议与调优方式不同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 RoCEv2 能跨三层网络，而 RoCEv1 往往不行？** 答：v2 使用 UDP/IP 封装，可以由 IP 网络转发；v1 在链路层承载，不是一般的可路由 IP 流量。
2. **问：只看网卡链路 100% up，为什么仍需调查 PFC/ECN？** 答：链路正常不等于无拥塞；排队和选择性暂停可让 p99 延迟陡升甚至吞吐抖动。

## 7. 中等难度考试题（含解析）

1. **题：一条流每秒欲发 40 GB，端到端可用有效带宽只有 32 GB/s，持续 2 s（忽略丢包）积压字节数？** 解：增长率为 8 GB/s，2 s 后约积压 16 GB；若缓冲不足可能丢包或反压。
2. **题：部署 RoCEv2 横跨三层，指出至少三个排查维度。** 解：IP 路由/可达性、MTU 一致性、ECN/CNP 与 PFC 策略、网卡与交换机错误/丢包统计、QoS 映射，任选三项并说明为何需要。

## 8. 权威来源与延伸阅读

- [NVIDIA Cumulus Linux RoCE Guide](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-40/Network-Solutions/RDMA-over-Converged-Ethernet-RoCE/)：原始规范、维护者文档或公开技术说明。
- [NVIDIA Networking Troubleshooting (NCCL)](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)：原始规范、维护者文档或公开技术说明。

> 本文中示例速率、负载、时延和容量（如未指出具体设备）均为教学假设，不代表特定产品测量结果。涉及版本差异的结论以对应版本官方文档为准。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
