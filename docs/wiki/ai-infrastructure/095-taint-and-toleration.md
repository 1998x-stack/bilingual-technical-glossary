# Taint and Toleration（污点与容忍）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与调度插件语义为准

## 1. 核心定义

Taint and Toleration 是 Kubernetes 的节点排斥与 Pod 例外机制。Node taint 标记节点不应接纳某些 Pod；Pod toleration 与污点匹配时，表示该 Pod 可以容忍相应 taint，但并不保证会被调度到该节点。若要只使用专用节点，还需配合 node affinity/selector。

## 2. 形象理解

节点像有门禁的实验室，门上写着“仅 GPU 训练团队进入”。toleration 相当于允许某团队通过门禁，但它并不强制这个团队必须进该实验室；若想只在这里工作，还需额外指定目的地。

## 3. 技术原理与核心内容

Taint 结构为 `key[=value]:effect`。`NoSchedule` 阻止新 Pod 调度；`PreferNoSchedule` 是尽量避开；`NoExecute` 不仅阻止新调度，也会驱逐不容忍的已绑定 Pod。Toleration 通过 key/operator/value/effect 匹配，`Exists` 可忽略 value；`tolerationSeconds` 可限制 NoExecute 容忍时长。系统会根据 Node conditions 自动加 memory-pressure、disk-pressure、not-ready 等污点。

## 4. 工程实践与设计权衡

将 GPU 节点标记 `dedicated=training:NoSchedule`，并给训练 Pod 添加匹配 toleration 与 required node affinity，避免普通服务占用昂贵 GPU 节点。升级驱动时可用 `NoExecute` 或 cordon/drain 配合维护流程，但需关注 tolerationSeconds、PDB 与训练 checkpoint。不要把 toleration 当作 RBAC 或安全隔离的唯一机制。

## 5. 易混概念与边界

Taint 施加在 Node，Toleration 施加在 Pod；toleration 允许而不吸引。Node Affinity 将 Pod 吸引/限制到节点集合。cordon 设置 Node unschedulable，不等同 taint；drain 会请求迁移/终止 Pod。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么只给 Pod 加 GPU toleration 仍可能被调度到 CPU 节点？** 答：toleration 只消除匹配 taint 带来的排斥，并不提供必须选择 GPU 节点的吸引条件；需同时配置 node affinity/selector 与 GPU resource request。

2. **问：NoSchedule 与 NoExecute 有什么区别？** 答：NoSchedule 只阻止新 Pod 调度，不主动驱逐已运行 Pod；NoExecute 会阻止新调度并驱逐不匹配的现有 Pod（可由 tolerationSeconds 延迟）。

## 7. 中等难度考试题（含解析）

1. **题：Node 有 `dedicated=gpu:NoSchedule` taint，Pod 有 key=dedicated、value=gpu、effect=NoSchedule 的 Equal toleration，是否匹配？** 解：匹配，因此该 taint 不再阻止此 Pod 调度；但还需满足其它资源和调度条件。

2. **题：Pod 对 `node.kubernetes.io/unreachable:NoExecute` 设置 tolerationSeconds=120，节点持续 unreachable，超出该时间后可能发生什么？** 解：容忍窗口结束后，Pod 可被 taint-based eviction controller 驱逐；具体还受控制器状态与其它规则影响。

## 8. 权威来源与延伸阅读

- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)：用于核对 API 行为、调度机制与工程边界。
- [Assign Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)：用于核对 API 行为、调度机制与工程边界。
- [Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)：用于核对 API 行为、调度机制与工程边界。

> 数值题是明确假设下的简化计算，不代表实际调度器决策或集群运行基准。
