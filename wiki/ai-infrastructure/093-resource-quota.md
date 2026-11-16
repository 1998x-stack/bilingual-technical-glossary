# Resource Quota（资源配额）

> 学科：AI Infrastructure · 专题：调度与容器 · 以 Kubernetes 当前 API 与调度插件语义为准

## 1. 核心定义

ResourceQuota 是 Kubernetes 的命名空间级准入控制机制，用于限制一组资源对象的累计消耗或对象数量，例如 requests.cpu、requests.memory、limits.memory、PVC 存储总量、Pod 数以及扩展资源 `requests.nvidia.com/gpu`。当创建/更新资源会超过 hard quota 时，API 准入阶段拒绝请求；Quota 不会自动为某个 Pod 找到节点。

## 2. 形象理解

像部门年度预算：每个团队有总额度，提交采购单时先检查余额，超预算就拒绝新单；预算额度不代表仓库里现在一定有对应型号的实物库存。

## 3. 技术原理与核心内容

ResourceQuota 对 namespace 中匹配 scope 的对象累计计量，`.spec.hard` 定义上限，`.status.used` 记录已使用量。资源 quota 可限制 requests/limits、PVC storage、对象计数与 extended resources。GPU quota 通常写 `requests.nvidia.com/gpu`，扩展资源不可超卖且不同时设置 requests 与 limits quota。若 namespace 对 CPU/memory 启用配额，Pod 通常必须声明相应 requests 或 limits；LimitRange 可补默认值。quota 在 API admission 阶段生效，已创建对象不会因额度变化而被自动杀掉。

## 4. 工程实践与设计权衡

多租户 AI 平台可按 namespace 设置 GPU、CPU、memory、PVC 和 Job 数量上限，并结合 RBAC 限制用户修改配额。区分 namespace quota、集群物理 capacity 和 Kueue 的队列 quota：ResourceQuota 管对象累计消耗，不提供按团队公平排队、跨队列借用或 all-or-nothing GPU admission。设置配额时还需检查 ResourceQuota 与 LimitRange 的默认值交互。

## 5. 易混概念与边界

ResourceQuota 是 namespace 范围的 API 准入上限，不是 scheduler 的节点容量、不等同 Priority/Fair Share，也不直接扩容。Kueue ClusterQueue 管工作负载准入与队列配额；两者可组合。

## 6. 中等难度面试题（含参考答案）

1. **问：ResourceQuota 未超限，为什么 Pod 仍可能 Pending？** 答：Quota 只允许 API 对象通过准入；节点可能没有足够 allocatable、GPU 型号不匹配、PVC 未绑定或 taints/affinity 不满足，scheduler 仍无法绑定。

2. **问：为什么 GPU quota 通常使用 requests.nvidia.com/gpu 而不是同时写 requests 与 limits？** 答：扩展资源不允许 overcommit；Kubernetes quota 仅接受 `requests.` 前缀的扩展资源计量，避免重复统计同一设备资源。

## 7. 中等难度考试题（含解析）

1. **题：某 namespace GPU hard quota=12，已使用 9，提交一个请求 4 GPU 的 Pod 是否能通过 quota admission？** 解：剩余 `12−9=3 GPU`，请求 4 超出 1，API 准入将拒绝该请求。

2. **题：CPU requests quota=80 cores，当前使用 53 cores，新建 6 个 Pod 每个 request=4 cores，创建后是否超限？** 解：新增 `6×4=24`，总计 `53+24=77 cores`，小于 80，**不会因该 CPU quota 超限**。

## 8. 权威来源与延伸阅读

- [Kubernetes Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)：用于核对 API 行为、调度机制与工程边界。
- [Kubernetes LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/)：用于核对 API 行为、调度机制与工程边界。
- [Kueue ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/)：用于核对 API 行为、调度机制与工程边界。

> 数值题是明确假设下的简化计算，不代表实际调度器决策或集群运行基准。
