# NVLink（高速 GPU 互连 · NVLink）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 022/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**NVLink**（高速 GPU 互连，NVLink）是指：NVIDIA 提供的高带宽设备互连技术。

**理解边界：** 该术语在实际使用中须结合互连架构、协议、硬件代际和测量方式，而不能仅据标称速率推断性能。

## 2. 形象理解

如果 PCIe 是连接公司各部门的公共走廊，NVLink 更像多台 GPU 之间专门修建的高速货运通道：运算中经常互换的数据可走更宽、更近的路径。不过通道多并不保证应用就能快，仍要看软件是否使用。

## 3. 技术原理与核心内容

NVLink 是 NVIDIA 的专有高速互连技术，面向多 GPU/部分 CPU-GPU 系统的设备间数据传输和内存访问。具体代际在链路数量、带宽与拓扑上差异很大；连接可以是直连，也可经 NVSwitch 组成交换网络。GPU P2P 通信常依赖运行时、拓扑、权限和驱动。高带宽常用于张量并行激活/权重分片交换与模型多卡协作。

## 4. 工程实践与设计权衡

部署模型张量并行时，先用拓扑工具检查 GPU 对间是直连、NVSwitch 还是经 PCIe；用 NCCL 测试验证实际跨卡带宽和不同消息尺寸的吞吐。若 GPU 间出现 P2P 降级，单看 GPU 算力不会揭示根因。还需将每层通信量乘以调用次数，估计是否会压过计算。

## 5. 关联知识与易混辨析

NVLink 是链路/互连机制，NVSwitch 是让多条 NVLink 组成交换 fabric 的设备；InfiniBand/RoCE 一般用作跨服务器 scale-out 网络，但新系统也可能提供跨节点 NVLink，不能绝对称‘NVLink 只能机内’。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么增加 GPU 数却不能让张量并行吞吐线性增加？** 答：各 GPU 计算可分摊，但每层可能要 all-reduce / all-gather；若通过 NVLink 的通信或同步消耗随卡数增加，收益递减。
2. **问：两台 GPU 标称 NVLink 速度一致，是否可推断实测互访速度一致？** 答：不可。需看连接代际、拓扑路径、链路是否全部启用、请求大小、缓存行为及实际 P2P 配置。

## 7. 中等难度考试题（含解析）

1. **题：数据量为 30 GB，假定有效单向互连带宽 150 GB/s，理想传输时间？** 解：30/150=0.2 秒；未计启动延迟、计算重叠、协议开销。
2. **题：为什么跨 GPU 内存访问不能简单当作本地 HBM 访问？** 解：两者走不同物理路径、延迟和带宽不同；远端访问还可能受一致性、地址转换、并发与硬件能力影响。

## 8. 权威来源与延伸阅读

- [NVIDIA NVLink Network Overview](https://docs.nvidia.com/multi-node-nvlink-systems/imex-guide/overview.html)：原始规范、维护者文档或公开技术说明。
- [NVIDIA Fabric Manager User Guide](https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/)：原始规范、维护者文档或公开技术说明。

> 本文中示例速率、负载、时延和容量（如未指出具体设备）均为教学假设，不代表特定产品测量结果。涉及版本差异的结论以对应版本官方文档为准。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
