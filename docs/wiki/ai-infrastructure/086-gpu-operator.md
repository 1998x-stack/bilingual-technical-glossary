# GPU Operator（GPU 运维算子）

> 学科：AI Infrastructure · 专题：调度与容器 · Kubernetes 与 GPU 组件行为应按部署版本验证

## 1. 核心定义

GPU Operator 是在 Kubernetes 中以 Operator/Controller 方式自动部署、配置和维护 GPU 节点软件栈的控制面组件。以 NVIDIA GPU Operator 为例，它可协调驱动、Container Toolkit、Kubernetes Device Plugin、GPU Feature Discovery、DCGM Exporter，以及可选 MIG Manager 等组件，让 GPU 节点以一致方式进入集群。Operator 负责生命周期与配置协调，不是 GPU 本身，也不取代 kube-scheduler。

## 2. 形象理解

像 GPU 机房的自动化设备管理员：它检查驱动、设备登记、监控代理和分区管理组件是否符合期望版本，发现漂移后协调修复。真正把某张 GPU 分给 Pod 的动作仍经由 kubelet/device plugin 资源分配链路。

## 3. 技术原理与核心内容

Operator CRD/Helm values 描述期望安装状态，operator controller reconcile 生成并维护 DaemonSet、ConfigMap、ServiceAccount 和相关资源。驱动容器在支持的平台上可管理 host driver；Container Toolkit 配置容器 runtime 的 GPU 注入；device plugin 报告 `nvidia.com/gpu` 等扩展资源；GFD 生成 GPU 节点标签；DCGM Exporter 暴露监控指标；MIG Manager 监听 MIG 配置标签并协调重配。具体组件启用情况取决于 operator chart、平台和安装参数。

## 4. 工程实践与设计权衡

部署前核对 GPU 型号、宿主 OS/kernel、driver branch、CUDA runtime、containerd/CRI、Kubernetes 版本与 GPU Operator support matrix。生产升级先 cordon/drain 节点并检查训练 checkpoint、daemonset 滚动和驱动重启风险。排障按层检查 driver/device node、nvidia-container-toolkit、device plugin registration、node allocatable、Pod resource limits，再检查 DCGM。不要在节点上同时用 Operator 与另一套脚本争夺驱动安装所有权。

## 5. 易混概念与边界

GPU Operator 管理 GPU 软件栈生命周期；Device Plugin 负责向 kubelet 注册设备和分配；Scheduler 根据已发布的扩展资源放置 Pod。Operator 不会自动把一张 GPU 拆成多个独立显存配额；MIG 是特定 GPU 硬件支持的隔离分区能力。

## 6. 中等难度面试题（含参考答案）

1. **问：GPU Operator Ready，但 Pod 仍提示 Insufficient nvidia.com/gpu，优先检查什么？** 答：检查 Device Plugin Pod、kubelet 注册日志、节点 `Capacity/Allocatable` 中的资源名和设备健康状态；Operator 主控制器健康不代表设备插件已成功注册。

2. **问：为什么升级 GPU Operator 可能需要 drain 节点？** 答：驱动、MIG 配置或 runtime 组件更新可能要求重启节点/停止 GPU client，运行中的训练和推理进程可能失去设备。需做维护窗口、checkpoint 与回滚规划。

## 7. 中等难度考试题（含解析）

1. **题：一个节点有 8 张物理 GPU，Operator 正常、Device Plugin 报告其中 7 张 Healthy，节点 GPU allocatable 应按多少张设备估算？** 解：按插件上报的健康可分配设备估算为 **7 张**，而不是物理清单的 8 张；若启用 MIG，资源名与计数会按 MIG 策略变化。

2. **题：升级计划需滚动维护 12 个 GPU Node，每次最多 drain 3 个，至少分几批？** 解：`ceil(12/3)=**4 批**`；还需考虑 PodDisruptionBudget、训练恢复和可用容量，批次数不等于维护总时长。

## 8. 权威来源与延伸阅读

- [NVIDIA GPU Operator Architecture](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/)：用于核对官方 API、架构与调度语义。
- [NVIDIA GPU Operator Components](https://github.com/NVIDIA/gpu-operator/blob/main/CONTRIBUTING.md)：用于核对官方 API、架构与调度语义。
- [Kubernetes Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)：用于核对官方 API、架构与调度语义。

> 例题数据为教学假设，未考虑集群所有控制环与异常路径。
