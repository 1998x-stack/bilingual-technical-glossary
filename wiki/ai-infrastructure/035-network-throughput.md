# Network Throughput（网络吞吐量）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 035/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**Network Throughput**（网络吞吐量）：单位时间网络实际传输的数据量。

**精确定义补充：** 该术语需要结合网络拓扑、通信语义、具体软件实现和度量口径理解；不能只凭理论峰值推断真实任务表现。

## 2. 形象理解

吞吐量是‘每秒真正送达多少货物’，不是道路上画着的最高车速。带宽像道路能力上限，吞吐还取决于货物大小、队列拥堵和调度。

## 3. 技术原理与核心内容

Network throughput 常指在指定窗口成功传输的字节数或比特数除以时间；应区分物理线速、链路帧吞吐、L3/L4 payload goodput，以及针对请求完成数的应用吞吐。实测值由 packet size、拥塞、丢包/重传、窗口大小、并发流数、接收端处理等共同决定。

## 4. 工程实践与设计权衡

验证 200GbE 网络不能只写‘200G’：采用 `iperf3` 或 RDMA benchmark，报告消息大小、流数、MTU、CPU 占用、网卡 counters、时间窗口及是否加密；训练集群另用 nccl-tests 测每类 collective 的 bus bandwidth。对比历史版本需保持测试口径。

## 5. 关联知识与易混辨析

Throughput 是达成的实际处理速率，Bandwidth 常是理论或可用能力；Goodput 排除协议头及重传等无效部分。高吞吐不保证低延迟，接近饱和时队列延迟可能迅速变大。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么单条 TCP 流测不满 400GbE 不足以判定网卡有问题？** 答：单流可能受窗口、CPU、核亲和、拥塞控制、hash 路径和上游链路限制，应对比多流和点对点网卡 benchmark。
2. **问：为什么发送端显示 40 Gb/s，接收端业务只有 32 Gb/s？** 答：可能统计口径不同，发送端含重传/协议开销，接收端只统计有效应用载荷；也可能存在丢包或接收处理限制。

## 7. 中等难度考试题（含解析）

1. **题：10 s 内应用成功收到 25 GB（十进制）的数据，平均 goodput 为多少 Gb/s？** 解：25×8 /10 =20 Gb/s，假设 25 GB 全是有效应用数据。
2. **题：发送端发送 12 GB，其中 2 GB 为协议/重传等不计入有效载荷，传输历时 4 s，goodput 为多少 GB/s？** 解：(12−2)/4=2.5 GB/s；发送侧总流量速率为 3 GB/s。

## 8. 权威来源与延伸阅读

- [IETF RFC 2544 Benchmark Methodology](https://www.rfc-editor.org/rfc/rfc2544)：用于校对通信定义、技术条件与实现范围。
- [NVIDIA NCCL Networking Troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)：用于校对通信定义、技术条件与实现范围。

> 题中的速率、节点数与流量均为教学设定。区分十进制 GB 与二进制 GiB，注明方向与统计口径；设备实测值应另附测试环境。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
