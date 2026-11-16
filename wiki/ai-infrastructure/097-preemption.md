# Preemption（抢占）

> 学科：AI Infrastructure · 专题：调度与容器 · 实际 API、feature gate 与存储语义须按产品版本确认

## 1. 核心定义

Kubernetes Pod Preemption 是 scheduler 在高优先级 Pod 无法找到可行节点时，尝试驱逐一个或多个低优先级 Pod 以腾出资源的机制。它依赖 PriorityClass 和节点可行性模拟；只有当移除低优先级 Pod 后目标 Pod 才可能放置时才有意义。抢占不是节点压力驱逐，也不保证目标 Pod 立即启动。

## 2. 形象理解

机场有紧急任务时，调度系统可请优先级较低的航班让出登机口，但飞机需要安全离场和地勤清理，因此不会在发出通知的一刻就腾出机位。

## 3. 技术原理与核心内容

Pod 设置 `priorityClassName` 后获得整数 priority；若 Pending Pod P 在所有节点都不可调度，scheduler 评估候选节点，尝试移除低于 P 的 victim Pods，计算是否足以让 P 通过资源/调度约束。成功时 P 的 `nominatedNodeName` 可记录候选节点；victims 按 terminationGracePeriodSeconds 优雅退出，期间节点资源尚未完全释放。PDB 在选择 victim 时尽力遵守，但 Kubernetes 明确说明 best effort，并非绝对禁止违反。PodGroup preemption 在 Kubernetes v1.37 是 Beta 且默认关闭，需启用 GenericWorkload feature gate。

## 4. 工程实践与设计权衡

AI 平台应谨慎定义 PriorityClass：在线推理控制面、关键服务、训练 worker 和可中断 batch 的优先级层级要明确，并结合 PDB、SIGTERM checkpoint、terminationGracePeriodSeconds 与 Job podFailurePolicy。抢占后观察被驱逐 Pod、victim 选择、nominatedNodeName、重新排队和 GPU 释放时间。高优先级不应授予所有租户，否则低优先级训练会饥饿；可配合 ResourceQuota 限制 PriorityClass 使用。

## 5. 易混概念与边界

Scheduler preemption 由 Pod priority 触发；node-pressure eviction 由 kubelet 在内存/磁盘等压力下驱逐；Cluster Autoscaler scale-up 创建新 Node。PDB 是自愿中断预算，不是对所有抢占场景的硬保护。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 PDB 不能绝对阻止 Kubernetes scheduler preemption？** 答：scheduler 在 victim 选择时尽量避免违反 PDB，但官方定义为 best effort；若没有满足 PDB 的可行 victim 集合，仍可能抢占以满足更高优先级 Pod。

2. **问：被抢占 Pod 发出 SIGTERM 后，为什么高优先级 Pod 仍不能立刻运行？** 答：victim 需要完成 termination grace period 并释放 GPU、CPU、volume 等资源；终止未完成时调度器不能假定资源已空闲。

## 7. 中等难度考试题（含解析）

1. **题：Pending Pod priority=100，节点上有 3 个 Pod，priority 分别 10、40、120；哪些 Pod 可作为低优先级 victim 候选？** 解：priority **10 和 40** 低于 100；priority 120 不能被该 Pod 抢占。最终是否驱逐还取决于可行性与 victim 集合。

2. **题：被抢占 Pod terminationGracePeriodSeconds=45，假设完整等待后才释放资源，最短需预留多少秒退出时间？** 解：最多按题设需等待 **45 秒**；这不包括 scheduler 重试、资源清理和容器启动时间。

## 8. 权威来源与延伸阅读

- [Kubernetes Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)：用于核对协议语义、架构与版本边界的官方文档。
- [Kubernetes Scheduling and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/)：用于核对协议语义、架构与版本边界的官方文档。
- [Kubernetes Job Pod Failure Policy](https://kubernetes.io/docs/tasks/job/pod-failure-policy/)：用于核对协议语义、架构与版本边界的官方文档。

> 数值算例是简化教学推导；不构成真实存储集群的吞吐、耐久性或可用性承诺。
