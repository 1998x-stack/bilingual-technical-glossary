# Kubernetes（容器编排系统）

> 学科：AI Infrastructure · 专题：调度与容器 · 技术边界按 Kubernetes、OCI 与运行时官方规范核对

## 1. 核心定义

Kubernetes（K8s）是面向容器化工作负载的声明式编排系统。用户提交 API 对象描述期望状态，控制器持续观察实际状态并协调差异；scheduler 为尚未绑定节点的 Pod 选择合适 Node，kubelet 在节点上落实 Pod。集群由 control plane 与 worker nodes 构成，目标是自动化部署、扩缩容、服务发现、调度和自愈，而不是替代应用本身的分布式协调。

## 2. 形象理解

像一个大型物流调度网络：用户提交目标订单，控制中心记录期望结果，调度器选择仓库，节点代理负责执行，控制器不断核对货物数量与目标是否一致。系统不是执行一次命令就结束，而是持续 reconcile。

## 3. 技术原理与核心内容

核心控制面包括 kube-apiserver（API 入口与认证/准入）、etcd（持久化集群状态）、kube-scheduler（Pod→Node 绑定）、kube-controller-manager（各类控制器）。节点运行 kubelet、容器运行时及网络组件；Service/CNI/CSI 分别承担服务访问、Pod 网络与存储集成。Deployment/ReplicaSet/StatefulSet/Job 等控制器创建或维护 Pod。API watch、resourceVersion 和 controller work queue 构成事件驱动控制循环；系统最终一致，故障恢复需要时间。

## 4. 工程实践与设计权衡

AI 集群中要分别建模 GPU 节点池、训练 Job 队列、在线推理 Deployment、模型数据卷和观测栈。通过 namespace/RBAC/ResourceQuota 做租户隔离，requests/limits 影响调度与资源控制，node labels/taints 约束异构 GPU，Kueue/Volcano 等可补足批任务队列与 gang admission。生产升级需考虑 API 兼容、CRD/controller 版本、CNI/CSI、GPU driver 与 kubelet 的兼容矩阵。

## 5. 易混概念与边界

Kubernetes 是控制与编排系统，不是容器镜像格式、容器 runtime 或单一调度算法。Scheduler 只负责选节点与绑定，不负责创建云主机；Cluster Autoscaler/Karpenter 才可对接基础设施扩容。声明式控制器的 reconcile 与一次性脚本执行不同。

## 6. 中等难度面试题（含参考答案）

1. **问：Kubernetes 为什么采用声明式 API 和 reconciliation，而不是只执行用户发来的命令？** 答：控制器可从实际状态反复向期望状态收敛，进程重启、节点故障和短暂 API 失败后仍能恢复；命令式一次操作难以持续处理漂移。

2. **问：Pod Pending 时，为什么不能只查看 kube-scheduler？** 答：Pending 可能由镜像拉取、PVC 未绑定、准入、配额、调度资源、网络或容器启动失败造成。需按 Pod conditions/events、PVC、节点状态和控制器事件逐层定位。

## 7. 中等难度考试题（含解析）

1. **题：期望 replicas=12，当前只有 9 个可用 Pod，控制器需要补建多少个？** 解：目标差值 `12−9=**3 个**`；实际创建还受配额、调度与镜像拉取影响。

2. **题：控制面由 3 个组件分别负责 API、持久状态和 Pod 放置，它们分别是什么？** 解：分别是 **kube-apiserver、etcd、kube-scheduler**；控制器管理器负责其它期望状态协调。

## 8. 权威来源与延伸阅读

- [Kubernetes Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/)：用于核对规范、架构与实现语义的官方资料。
- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)：用于核对规范、架构与实现语义的官方资料。
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)：用于核对规范、架构与实现语义的官方资料。

> 数字算例均为题设下的简化教学推导，不是某个集群的性能承诺。
