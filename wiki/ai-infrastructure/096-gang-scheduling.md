# Gang Scheduling（成组调度）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与存储服务实际语义为准

## 1. 核心定义

Gang Scheduling（成组调度）是面向多 Pod 协作工作负载的 all-or-nothing 调度策略：一组相互依赖的 Pod 只有在满足完整资源条件或定义的最小成员数 `minCount` 后，才作为整体进行调度/绑定，避免部分 worker 长期占用 GPU、等待其它 worker 而导致资源碎片或死锁。必须区分“队列准入”“物理放置”“Pod Ready”三个原子性边界。

## 2. 形象理解

一支 8 人划艇队必须同时到齐才能下水。若先让 4 人占着船等另外 4 人，另一支队伍也可能占着半条船，最终双方都无法训练。成组调度先确认团队整体能开始，再释放资源。

## 3. 技术原理与核心内容

传统逐 Pod scheduler 可能先绑定一部分 worker；对同步 AllReduce 训练，缺少 worker 就无法推进 collective step。Kubernetes v1.37 原生 PodGroup/Gang Scheduling 已进入 Beta，但默认关闭，需为相关组件启用 `GenericWorkload` feature gate 和 `scheduling.k8s.io/v1beta1` API；Gang policy 支持完整组或 `minCount`。Job 的 `.spec.scheduling` 到 Workload/PodGroup 集成在 v1.36 仍为 Alpha 且默认关闭，不能把它与普通 Job parallelism 混为一谈。Kueue 则通过 Workload quota reservation、可选 Topology-Aware Scheduling 与 `waitForPodsReady` 实现 all-or-nothing admission/恢复；Volcano 等也提供自己的 gang 插件，语义和 API 需按实现确认。

## 4. 工程实践与设计权衡

分布式训练应把 worker 数、每 Pod GPU 数、节点/机架拓扑、最小可运行成员数和启动超时一起提交队列。仅预留集群总 GPU 数并不足够：8 张 GPU 分布在两个 4-GPU 节点时，一个需要单节点 8-GPU 的 Pod 仍无法运行。启用 TAS 或拓扑约束，预热镜像与数据，并配置失败后 quota release、requeue 和 checkpoint。原生 Beta 功能默认关闭，启用前核对 API server、scheduler、controller 与 CRD/feature-gate 的版本一致性。

## 5. 易混概念与边界

Gang scheduling 关注多个 Pod 的整体调度；普通 parallel Job 只声明 parallelism/completions，并不自动保证所有 Pod 同时可调度。Kueue 是 workload queue/admission 系统，kube-scheduler 仍负责 Pod→Node 绑定；gang admission 不等于多个容器在同一纳秒启动。Kubernetes v1.37 原生能力为 Beta 但默认关闭，不应假设所有发行版都已启用。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么同步分布式训练特别需要 gang scheduling？** 答：所有 worker 必须参加 collective communication 才能推进 step；部分 worker 已占 GPU 却等待其余资源会形成资源碎片，甚至让多个作业相互持有部分资源而死锁。

2. **问：Kueue 预留了总共 8 张 GPU，为什么 gang workload 仍可能 Pending？** 答：总量 quota 不代表拓扑可放置性；若一个 8-GPU Pod 需要单节点 8 卡，而实际分散在两个 4 卡节点，物理布局不满足。应使用 TAS/拓扑检查或调整 Pod 分组。

## 7. 中等难度考试题（含解析）

1. **题：训练任务需要 8 个 worker，每个请求 4 GPU，总计需要多少 GPU？若每节点 8 GPU，至少多少节点？** 解：总量 `8×4=**32 GPU**`；每节点 8 GPU，至少 `32/8=**4 个节点**`，还须满足网络与拓扑要求。

2. **题：集群空闲 32 GPU，但每节点剩余 GPU 分别为 4、4、8、8、8；一个单 Pod 请求 8 GPU 是否有可放置节点？** 解：有；三个节点分别有 8、8、8 卡中的任一个可满足单 Pod 请求。总容量不是唯一条件，必须存在一个满足约束的单节点/拓扑域。

## 8. 权威来源与延伸阅读

- [Kubernetes Gang Scheduling (Beta v1.37)](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/)：用于核对服务保证、API 与架构边界的官方资料。
- [Kubernetes PodGroup Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/)：用于核对服务保证、API 与架构边界的官方资料。
- [Kueue All-or-nothing Scheduling](https://kueue.sigs.k8s.io/docs/concepts/all_or_nothing/)：用于核对服务保证、API 与架构边界的官方资料。

> 数值算例是明确假设下的教学推导，不构成生产集群性能或一致性承诺。
