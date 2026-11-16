# Network Interface Card（网络接口卡 · NIC）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 028/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**Network Interface Card**（网络接口卡，NIC）是指：服务器接入计算机网络的硬件接口。

**理解边界：** 该术语在实际使用中须结合互连架构、协议、硬件代际和测量方式，而不能仅据标称速率推断性能。

## 2. 形象理解

NIC 是服务器面向网络的‘港口’：港口能做卸载、排队和流量调度，但一台船的运输速度还受海峡（交换机）、航道（拓扑）和目的港影响。

## 3. 技术原理与核心内容

NIC 将主机经 PCIe 等接口连接至网络介质，完成链路收发、DMA、队列管理、校验和等部分卸载。高性能网卡可能具备 RSS、多队列、SR-IOV、RDMA、TSO 或可编程数据平面。驱动、CPU NUMA、PCIe 带宽和中断亲和影响数据到达应用的实际路径。

## 4. 工程实践与设计权衡

训练网络的实际吞吐低时，检查 `ethtool -i/-S`、`ip -s link`、NUMA 绑定、网卡/PCIe 带宽、队列数与网络拥塞统计，区分 NIC/驱动与网络 fabric 的问题。高吞吐多连接场景可评估队列分布，而单个大流可能受 hash/端口映射约束。

## 5. 关联知识与易混辨析

NIC 是通用网络接口；SmartNIC 在此基础上强调可编程/卸载能力；DPU 往往还有通用控制处理器和更复杂基础设施隔离能力。类别边界因厂商而异。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么相同 200GbE NIC，两个 NUMA 节点的通信表现可能不同？** 答：NIC 的 PCIe 归属、CPU 内存亲和性和跨 socket 访问路径不同；将接收线程与缓冲内存绑在本地 NUMA 通常更易获得稳定表现。
2. **问：网卡 offload 总是越多越好吗？** 答：不是。不同 offload 对虚拟交换、抓包、内核协议栈、延迟/吞吐影响不同，需确保支持并在目标场景实测。

## 7. 中等难度考试题（含解析）

1. **题：单个端口 200 Gb/s，若所有链路字节都可用于有效载荷，理想吞吐上界多少 GB/s？** 解：200/8=25 GB/s（十进制）；注意有效业务数据通常达不到。
2. **题：4 条独立链路各 100 Gb/s，是否保证单 TCP 连接达到 400 Gb/s？** 解：不能。链路聚合/ECMP 通常按流哈希分配，单流往往落在单条路径；多流和应用并行度决定利用。

## 8. 权威来源与延伸阅读

- [NVIDIA Networking Troubleshooting (NCCL)](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)：原始规范、维护者文档或公开技术说明。
- [IEEE 802.3 Ethernet Working Group](https://www.ieee802.org/3/)：原始规范、维护者文档或公开技术说明。

> 本文中示例速率、负载、时延和容量（如未指出具体设备）均为教学假设，不代表特定产品测量结果。涉及版本差异的结论以对应版本官方文档为准。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
