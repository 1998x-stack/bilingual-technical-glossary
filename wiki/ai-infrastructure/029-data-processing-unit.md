# Data Processing Unit（数据处理单元 · DPU）

> TERM/ATLAS · AI Infra Wiki · Batch 02 · 029/142 · 专题：互连与网络 · 研究日期：2026-11-16

## 1. 核心定义

**Data Processing Unit**（数据处理单元，DPU）是指：卸载网络、存储与安全等基础设施任务的处理器。

**理解边界：** 该术语在实际使用中须结合互连架构、协议、硬件代际和测量方式，而不能仅据标称速率推断性能。

## 2. 形象理解

DPU 像在数据中心服务器旁边设置独立后勤主管：把虚拟交换、存储处理、安全策略等基础设施事务交给它，主 CPU 便更专心运行 AI 作业。但主管也有预算和算力上限。

## 3. 技术原理与核心内容

DPU 是用于处理基础设施数据面的可编程处理器类别，具体实现可能整合多核 CPU、网络接口、硬件加速模块和隔离域。典型用例为 vSwitch/OVS offload、存储协议加速、安全规则和多租户隔离。NVIDIA BlueField 采用 Arm 核心、网络引擎和 DOCA 软件栈；这是特定产品路线，不是 DPU 的唯一标准形态。

## 4. 工程实践与设计权衡

AI 集群把主机网络/存储工作卸载给 DPU 时，要测量端到端 CPU 节省、GPU 数据路径时延、资源隔离与管理开销，并设计 DPU 固件、安全更新和故障恢复。即使卸载成功，也需要对 DPU 自身形成的瓶颈与资源共享做容量规划。

## 5. 关联知识与易混辨析

DPU、SmartNIC、SuperNIC 的市场命名并非严格统一；关注功能实际在哪里执行、是否有独立 CPU/OS、控制面与数据面如何隔离，而不是只看标签。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么租户隔离或存储安全卸载可能需要 DPU 上独立控制域？** 答：有助于把基础设施管理和租户主机分离，提高策略实施的一致性与失陷边界；效果取决于具体信任架构。
2. **问：从 CPU 卸载网络数据面为何不等于模型训练一定更快？** 答：如果训练主要受 GPU/HBM 限制，CPU 卸载收益有限；还可能新增 DPU/链路瓶颈，因此要看整体 step time。

## 7. 中等难度考试题（含解析）

1. **题：CPU 原来每秒为网络处理花 12 核·秒，DPU 卸载后降到 3 核·秒，CPU 工作量相对减少多少？** 解：(12-3)/12=75%；这是 CPU 工作量下降，不可直接理解为训练速度提高 75%。
2. **题：租户工作负载必须在隔离的网路与存储路径运行，DPU 是否单凭硬件名称就满足？** 解：不能。需要验证访问控制配置、SR-IOV/virtio 等实现、固件信任与管理域边界。

## 8. 权威来源与延伸阅读

- [NVIDIA BlueField / DOCA Architecture](https://docs.nvidia.com/doca/sdk/bluefield-and-doca-user-types.pdf)：原始规范、维护者文档或公开技术说明。
- [NVIDIA Networking Troubleshooting (NCCL)](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)：原始规范、维护者文档或公开技术说明。

> 本文中示例速率、负载、时延和容量（如未指出具体设备）均为教学假设，不代表特定产品测量结果。涉及版本差异的结论以对应版本官方文档为准。

## 9. 知识导航

- [返回 AI Infra 批次索引](README.md)
- [返回 AI Infra 术语对照表](../../glossaries/ai-infrastructure.md)
