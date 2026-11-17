# Workload Consolidation（工作负载整合）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 按 SLO、租户、资源约束与版本说明结论边界

## 1. 核心定义

工作负载整合（Workload Consolidation）是把多个原本分散运行的应用、任务或租户通过调度、合批、资源共享和容量池化部署到更少的设备或实例，以降低空闲和基础设施开销。它通过提高资源复用率获益，却也可能增加争用、故障影响半径和长尾延迟，因此应在 SLO 与安全隔离约束下执行。

## 2. 形象理解

像把几个半空的会议室合并使用，让同样的人数占用更少房间；但如果所有团队同时开会，就可能排队，且一个房间的噪声会影响多个团队。

## 3. 技术原理与核心内容

整合策略包括 Kubernetes bin packing、多个推理模型共享 GPU、continuous batching、MIG partition/time slicing、CPU/GPU 不同资源需求的互补混部。调度要检查 GPU 显存、compute、PCIe/NVLink/NUMA、网络与存储带宽，不能只把平均 GPU utilization 相加。MIG 提供受硬件支持的物理分区，time slicing 通常不是等价隔离；高优先级在线推理与可中断训练混部还涉及 preemption、quota、延迟 SLO 和 checkpoint 成本。

## 4. 工程实践与设计权衡

先基于每个模型的 GPU busy、SM/HBM、KV cache、P99 latency、CPU decode、网络/磁盘和峰谷分布绘制资源需求曲线，再实验从 1→2→4 个服务/卡的并发与隔离。联合考核好请求 TPS、TTFT/ITL、OOM/preemption、功耗、GPU-hours 与设备故障时的受影响租户数，制定 QoS 和容量余量。对于高隐私/安全等级任务，宁愿牺牲部分利用率也应避免无授权共享权重/缓存。

## 5. 易混概念与边界

Consolidation 是工作负载布局与共享策略，不等同 Autoscaling（随负载调整容量）或 Quantization（减少表示字节数）。高资源平均使用率不证明没有高峰排队；多租户整合尤其需要权限与数据隔离。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么通过 bin packing 把 GPU 平均利用率提高到 95% 可能是坏事？** 答：预留空间不足会在 burst 时排队、触发 KV OOM 或损害 P99/SLO；共享故障域与性能隔离也可能恶化。

2. **问：MIG 与 GPU time slicing 的隔离语义为什么不同？** 答：MIG 在支持的 GPU 上划分硬件资源与显存容量隔离；time slicing 主要让多个上下文轮流执行，未必提供同等级资源/故障隔离。

## 7. 中等难度考试题（含解析）

1. **题：4 台设备原本每台平均使用率 25%，假设负载可完美无干扰合并且峰值不重叠，理论最少几台设备承载相同平均负载？** 解：总平均等效 `4×0.25=**1 台**`，但这仅是均值下界，不说明真实峰值和隔离可行。

2. **题：整合前每月 GPU 成本 120 万，整合后 90 万且 SLO 相同，节省比例？** 解：`(120−90)/120=**25%**`。

## 8. 权威来源与延伸阅读

- [Kubernetes Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)：用于核对管理机制与性能边界的原始资料。
- [NVIDIA MIG User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/)：用于核对管理机制与性能边界的原始资料。
- [NVIDIA Device Plugin](https://github.com/NVIDIA/k8s-device-plugin)：用于核对管理机制与性能边界的原始资料。

> 例题是假设条件下的算术演示，不是对生产多租户安全性或容量的认证。
