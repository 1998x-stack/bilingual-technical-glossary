# Cluster Autoscaler（集群自动扩缩容器 · CA）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与调度插件语义为准

## 1. 核心定义

Cluster Autoscaler（CA）是集群级容量控制器，观察 Kubernetes 中无法调度的 Pod，并在新增一个合适 Node 能让 Pod 有机会运行时扩展底层 Node Group；当节点长期未充分使用且其 Pod 可安全迁移时，尝试缩容。CA 通常通过云厂商/基础设施提供的 node group 接口调整机器数量，而不是直接修改 Pod 副本数。

## 2. 形象理解

像仓库扩建与合并：当订单因为没有空仓位而积压，系统判断新建某种规格仓库能解决问题后申请扩建；空仓库长期闲置且货物能搬走时才关停。只看平均 CPU 低，并不足以判断仓库能否关闭。

## 3. 技术原理与核心内容

CA 监控 unschedulable Pod 条件，模拟候选 node group 新节点的资源与 labels/taints/拓扑，若新节点可容纳积压 Pod 则发起 scale-up。scale-down 评估节点利用率、Pod 是否可迁移、PDB、DaemonSet、local storage、系统 Pod 和节点组最小/最大规模。扩容后仍需云 API 创建 VM、节点启动、驱动安装、kubelet 注册和 GPU Device Plugin 就绪，因此容量不是立即可用。CA 与云 provider/node group template 耦合，且算法和时间阈值依版本与配置变化。

## 4. 工程实践与设计权衡

GPU 集群要把不同 GPU 型号、显存、网络拓扑、MIG profile 设计成不同 node group，确保 CA 模拟出的新节点 labels/taints/extended resources 与真实节点一致。观察 unschedulable reason、node group max、配额、云容量、启动时间和 GPU plugin readiness。缩容前配置 PDB、checkpoint、可迁移数据卷和 scale-down delay；长训练作业或 local PV 可能阻止节点删除。

## 5. 易混概念与边界

CA 调整 Node 数量；HPA 调整 Pod 副本数；scheduler 将 Pod 绑定到现有 Node。CA 依赖 Pod 已不可调度信号，不是按 GPU utilization 直接扩容的通用预测器；Karpenter 等替代方案的供给模型不同。

## 6. 中等难度面试题（含参考答案）

1. **问：HPA 已扩 Pod，但它们一直 Pending，CA 为什么可能没有扩容？** 答：CA 只在新增某个 node group 节点能帮助调度时扩容；若请求的 GPU 型号/标签/taint/存储拓扑无法由现有 node group 提供，或组已达 max/云容量不足，就不会产生有效 scale-up。

2. **问：GPU Node 使用率低，为什么 CA 仍不删除？** 答：可能存在无法迁移的 Pod、严格 PDB、local storage、DaemonSet/system Pod、节点组最小数量或近期扩容保护窗口。

## 7. 中等难度考试题（含解析）

1. **题：当前有 5 个 Node，每个 allocatable 8 GPU；CA 将该 node group 扩到 7 个，理论 GPU 总容量增加多少？** 解：增加 `2×8=**16 GPU**`，前提是新节点规格完全相同且设备插件成功注册。

2. **题：某节点 CPU requests 合计 24 核、allocatable 64 核，按 requests/allocatable 估算的利用率？** 解：`24/64=**37.5%**`；这是 request-based utilization 示例，不等同实时 CPU 使用率，也不保证满足缩容所有条件。

## 8. 权威来源与延伸阅读

- [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)：用于核对 API 行为、调度机制与工程边界。
- [Cluster Autoscaler repository](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)：用于核对 API 行为、调度机制与工程边界。
- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)：用于核对 API 行为、调度机制与工程边界。

> 数值题是明确假设下的简化计算，不代表实际调度器决策或集群运行基准。
