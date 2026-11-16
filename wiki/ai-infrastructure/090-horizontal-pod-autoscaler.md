# Horizontal Pod Autoscaler（Pod 水平自动伸缩器 · HPA）

> 学科：AI Infrastructure · 专题：调度与容器 · Kubernetes 与 GPU 组件行为应按部署版本验证

## 1. 核心定义

Horizontal Pod Autoscaler（HPA）是 Kubernetes 控制器，根据 CPU、内存或自定义/外部指标周期性调整目标 workload 的副本数。HPA 更新目标对象的 scale 子资源，使 Deployment/StatefulSet 等增加或减少 Pod；它不负责创建 Node，也不保证新 Pod 一定能被调度。

## 2. 形象理解

像餐厅根据当前每位服务员的工作负荷增加或减少班组人数。HPA 决定需要多少服务员，集群是否有足够桌椅和店面空间则由节点容量与 Cluster Autoscaler 等系统处理。

## 3. 技术原理与核心内容

基本计算为 `desiredReplicas=ceil(currentReplicas×currentMetric/desiredMetric)`，随后受 min/max replicas、tolerance、missing metrics、not-ready Pod、stabilization window 和 scaling policies 调整。CPU utilization 通常是相对于 Pod CPU requests 的百分比；未配置 requests 时 CPU utilization 可能无法计算。多指标同时使用时，HPA 取各指标推荐副本数中的最大值。Resource metrics 通过 metrics-server，custom/external metrics 通过相应 adapter 提供。

## 4. 工程实践与设计权衡

在线推理服务可按并发请求数、队列深度、token backlog、GPU utilization 或每副本 QPS 扩缩容；单纯 CPU 可能无法代表 GPU 推理负载。自定义指标需正确处理 per-pod 与 external metric 语义，并设置 scale-up/down stabilization 防止抖动。HPA 扩容后若 GPU Node 无余量，Pod 会 Pending，需与 Cluster Autoscaler/节点池和模型加载时间一起建模。

## 5. 易混概念与边界

HPA 扩缩 Pod 副本；Cluster Autoscaler 扩缩 Node 数量；VPA 调整 Pod 资源 request/limit。HPA 的指标控制环有采样和启动延迟，不等同瞬时反应；GPU 指标需要监控采集与 adapter，不是所有集群默认可用。

## 6. 中等难度面试题（含参考答案）

1. **问：HPA 的 CPU utilization 为什么依赖 CPU requests？** 答：利用率定义为当前 CPU 使用量相对 request 的比例；request 缺失会使该容器/Pod 的 CPU utilization 无法正确计算。

2. **问：HPA 已将副本从 4 扩到 12，但服务容量没增加，常见原因是什么？** 答：新 Pod 可能因 GPU/CPU 配额、节点容量、镜像拉取、模型加载或 readiness probe 未就绪而不能提供服务；HPA 改的是期望副本数，不是物理容量。

## 7. 中等难度考试题（含解析）

1. **题：当前 6 个副本，平均 CPU 指标为目标值的 1.5 倍，按基本公式建议副本数是多少？** 解：`ceil(6×1.5)=**9 个**`，实际结果还会受 min/max、tolerance 与稳定窗口影响。

2. **题：HPA minReplicas=3、maxReplicas=20，公式建议 27 个副本，最终允许的目标数是多少？** 解：被 maxReplicas 限制为 **20 个**；若建议低于 3 则被 minReplicas 限制。

## 8. 权威来源与延伸阅读

- [Kubernetes Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)：用于核对官方 API、架构与调度语义。
- [Kubernetes Resource Metrics Pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)：用于核对官方 API、架构与调度语义。
- [NVIDIA DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter)：用于核对官方 API、架构与调度语义。

> 例题数据为教学假设，未考虑集群所有控制环与异常路径。
