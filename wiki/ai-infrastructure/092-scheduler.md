# Scheduler（调度器）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与调度插件语义为准

## 1. 核心定义

Kubernetes Scheduler（kube-scheduler）负责为尚未绑定节点的 Pod 选择一个可行 Node，并通过 API binding 将 Pod 绑定到所选节点。其工作不是启动容器，而是基于资源 requests、节点状态、亲和/反亲和、taints/tolerations、拓扑和扩展资源等约束进行过滤与打分。

## 2. 形象理解

像给航班分配登机口：先排除尺寸、时间或安全条件不匹配的登机口，再给剩余候选点打分并选一个；真正把飞机推出机位的是机场地勤与机组，不是登机口分配系统。

## 3. 技术原理与核心内容

调度框架包含 QueueSort、PreFilter、Filter、PostFilter、PreScore、Score、Reserve、Permit、PreBind、Bind、PostBind 等扩展点。Filter 找到 feasible nodes；Score 为候选节点评分并选最高分；Bind 将 Pod 与 Node 关联。默认插件实现资源适配、NodeAffinity、TaintToleration、PodTopologySpread 等。调度周期和绑定周期有不同阶段；Reserve/Permit 可用于插件协调。requests 用于资源可行性判断，真实瞬时利用率并非简单替代。

## 4. 工程实践与设计权衡

排查 Pending Pod 先看 `kubectl describe pod` Events、scheduler logs 与 `.status.conditions`，区分 Insufficient cpu/memory/extended resource、taint、affinity、PVC topology 和 admission。多 GPU 训练需额外考虑 NVLink/PCIe/NIC、NUMA 与同机/同 rack 约束，默认 scheduler 不会自动理解应用通信图；可用 scheduler profile/plugin、DRA 或 Kueue TAS 等扩展。

## 5. 易混概念与边界

Scheduler 选择已有 Node 并绑定 Pod；kubelet 在节点落实 Pod；Cluster Autoscaler 请求新 Node。Filter 是硬约束筛选，Score 是候选偏好评分；preferred affinity 不会变成必须满足的硬约束。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么一个 Node CPU 空闲很多，Pod 仍可能无法调度？** 答：Pod 的 request 可能超过该节点剩余 allocatable，或 GPU/存储/taint/affinity/拓扑等硬约束不满足；CPU 利用率低不代表所有资源可行。

2. **问：Filter 和 Score 在调度流程中分别做什么？** 答：Filter 删除不满足硬约束的节点，Score 对剩余可行节点按偏好打分；若无 feasible node，Pod 保持未绑定并等待后续重试或扩容。

## 7. 中等难度考试题（含解析）

1. **题：三个候选节点得分分别 71、88、82，忽略其它并列规则，scheduler 选择哪个？** 解：选择得分最高的 **Node B（88）**；前提是三个节点已通过 Filter。

2. **题：Pod request 4 GPU，节点 allocatable 8 GPU，已分配 requests 5 GPU；仅看 GPU 资源是否可行？** 解：剩余 `8−5=3 GPU`，小于请求 4，因此 **不可行**，即使 CPU/内存充足。

## 8. 权威来源与延伸阅读

- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)：用于核对 API 行为、调度机制与工程边界。
- [Scheduler Configuration and Plugins](https://kubernetes.io/docs/reference/scheduling/config/)：用于核对 API 行为、调度机制与工程边界。
- [Kubernetes Scheduling Framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)：用于核对 API 行为、调度机制与工程边界。

> 数值题是明确假设下的简化计算，不代表实际调度器决策或集群运行基准。
