# Node Affinity（节点亲和性）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与调度插件语义为准

## 1. 核心定义

Node Affinity 是 Pod 的调度约束，依据 Node labels 表达 Pod 对节点集合的硬性要求或软性偏好。`requiredDuringSchedulingIgnoredDuringExecution` 是必须满足的过滤条件；`preferredDuringSchedulingIgnoredDuringExecution` 是评分偏好，匹配不到时仍可调度到其它可行节点。

## 2. 形象理解

像找房时的筛选条件：必须靠近实验室是硬条件，最好有电梯是软偏好。满足硬条件的房源先进入候选集，再按软偏好排序；如果入住后房屋标签改变，当前租客不会因为这个字段自动被赶走。

## 3. 技术原理与核心内容

规则位于 `.spec.affinity.nodeAffinity`，通过 `nodeSelectorTerms`、`matchExpressions`、`matchFields` 描述。常用 operator 有 In、NotIn、Exists、DoesNotExist、Gt、Lt；同一个 term 内表达式 AND，不同 nodeSelectorTerms 之间 OR。preferred 规则使用 1–100 weight，scheduler 将偏好权重用于节点评分。`IgnoredDuringExecution` 表示绑定后 Node label 改变不触发自动驱逐。

## 4. 工程实践与设计权衡

GPU 工作负载可按 `nvidia.com/gpu.product`、机型、显存、NVLink、区域、机架和网络标签选择节点；标签值必须由可信节点管理组件维护。硬性约束过多可能造成 GPU 碎片和长期 Pending，软偏好可提高利用率与调度成功率。涉及安全边界的节点标签应保护免受 kubelet 自行伪造，不能仅把普通 label 当作强安全控制。

## 5. 易混概念与边界

nodeSelector 是简单等值匹配；Node Affinity 更具表达力并支持软偏好。Pod Affinity/Anti-Affinity 根据其它 Pod 的位置约束，而 Node Affinity 根据 Node labels。Affinity 负责吸引/约束，taint 是 Node 排斥机制。

## 6. 中等难度面试题（含参考答案）

1. **问：required 与 preferred Node Affinity 最大的调度语义差别是什么？** 答：required 是硬过滤，不匹配就不可调度；preferred 是软评分偏好，找不到偏好节点时仍可选择其它满足硬条件的节点。

2. **问：IgnoredDuringExecution 表示节点标签变更后 Pod 会自动迁移吗？** 答：不会。它表示调度后忽略标签变化，不会仅因该亲和规则失效就驱逐已运行 Pod。

## 7. 中等难度考试题（含解析）

1. **题：3 个节点中，只有 A 与 C 满足 required affinity；preferred 评分 A=10、C=80，scheduler 更倾向哪个？** 解：倾向 **Node C**，因为 A/C 都通过硬约束，C 的偏好得分更高。

2. **题：有 4 个节点，其中 1 个满足 required 条件，其余不满足；该节点剩余 GPU 不足，Pod 是否可以退回其余节点？** 解：不可以；required 是硬约束，只有 1 个节点符合标签，但资源不足时 Pod 保持 Pending。

## 8. 权威来源与延伸阅读

- [Assign Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)：用于核对 API 行为、调度机制与工程边界。
- [Node Affinity Task](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)：用于核对 API 行为、调度机制与工程边界。
- [Scheduler Configuration](https://kubernetes.io/docs/reference/scheduling/config/)：用于核对 API 行为、调度机制与工程边界。

> 数值题是明确假设下的简化计算，不代表实际调度器决策或集群运行基准。
