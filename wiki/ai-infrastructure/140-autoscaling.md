# Autoscaling（自动扩缩容）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 按 SLO、租户、资源约束与版本说明结论边界

## 1. 核心定义

自动扩缩容（Autoscaling）根据观测到或预测的负载/资源约束，自动调整应用副本、节点数量或资源规格。常见有水平扩 Pod（HPA/KEDA）、扩 Node（Cluster Autoscaler/Karpenter）和纵向调整资源 requests（VPA）；不同控制环的输入信号、动作对象、延迟与适用场景不同，不能笼统说“GPU utilization 高就自动有更多 GPU”。

## 2. 形象理解

像餐厅按排队人数加开收银窗口，但如果店里没有空柜台，新收银员也只能站着等；同时买一间新店比叫一个员工到岗慢得多。

## 3. 技术原理与核心内容

控制器定期读取 CPU/GPU/队列等指标，通过目标比例或阈值计算所需副本，再应用 min/max、副本扩容速率、冷却/稳定窗口和指标缺失策略。Kubernetes HPA 的基础公式 `desiredReplicas≈ceil(currentReplicas×currentMetric/targetMetric)`；GPU 级指标一般需要指标 adapter，GPU Node Pod Pending 可能促使 CA 调整底层池，但受 quota、云库存、taints/affinity 和节点预热影响。KEDA 提供事件源/队列驱动的 scaler；scale-to-zero 与 GPU 模型加载较长启动时延之间存在显著权衡。

## 4. 工程实践与设计权衡

对在线 LLM 使用排队 tokens、wait RPS、TTFT SLO 和 KV cache 指标设计副本级扩缩容，再与节点池 ready capacity 联动。评估采样周期、缺失指标、模型冷启动、GPU 驱动/权重下载、队列耗尽和 P99；设置平滑/滞回防止短促 burst 反复 scale。高成本 GPU 可设置基础 Reserved/On-demand 容量与弹性 Spot 池，但必须处理 Spot 中断及异构 GPU 资源匹配。

## 5. 易混概念与边界

HPA 扩应用副本，CA 扩节点，VPA 改 resource requests，KEDA 根据事件驱动扩副本；它们不总能在任意同一资源上同时无冲突工作。Autoscaling 不能替代 Capacity Planning 的长期采购与故障冗余。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 HPA 期望副本增长，用户延迟仍可能上升？** 答：新 Pod 可能 Pending 等 GPU 节点，或模型下载/初始化/readiness 迟迟未完成；控制器只改变期望副本，不保证立即增加有效处理容量。

2. **问：为什么 GPU 推理服务按 CPU utilization 扩缩容常失真？** 答：CPU 使用不能反映 GPU decode 的 KV 带宽和生成队列压力；可使用业务队列 tokens、goodput/TTFT SLI 与 GPU memory 等指标。

## 7. 中等难度考试题（含解析）

1. **题：现有 4 个副本、指标为目标的 2.2 倍，忽略限制，HPA 基本公式建议多少个？** 解：`ceil(4×2.2)=**9 个副本**`。

2. **题：实例最少2个、最多10个，控制算法建议16个，受硬性 max 上限限制后的目标？** 解：最终 **10 个**；但是否能被调度仍另取决于节点容量。

## 8. 权威来源与延伸阅读

- [Kubernetes HPA](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)：用于核对管理机制与性能边界的原始资料。
- [Kubernetes Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)：用于核对管理机制与性能边界的原始资料。
- [KEDA Scalers](https://keda.sh/docs/latest/scalers/)：用于核对管理机制与性能边界的原始资料。

> 例题是假设条件下的算术演示，不是对生产多租户安全性或容量的认证。
