# Node（集群节点）

> 学科：AI Infrastructure · 专题：调度与容器 · 技术边界按 Kubernetes、OCI 与运行时官方规范核对

## 1. 核心定义

Node 是 Kubernetes 集群中的工作机器，可以是物理机或虚拟机，负责承载 Pod。Node API 对象记录机器身份、labels、taints、capacity/allocatable、conditions 与地址等信息；节点代理 kubelet 通过 API Server 报告状态并管理本机 Pod，容器运行时负责容器执行。

## 2. 形象理解

Node 像一座可被调度系统管理的仓库：有总面积、可供租用的有效面积、设备清单、健康状态与地理标签。调度器根据 Pod 请求和仓库条件分配工作，而不是只看 CPU 空闲百分比。

## 3. 技术原理与核心内容

典型节点组件包含 kubelet、CRI 兼容 container runtime，以及网络代理/数据面（传统 kube-proxy，也可能由 eBPF CNI 替代）。`capacity` 表示节点资源总量，`allocatable` 是可供 Pod 分配的量，通常扣除了系统与 kubelet 保留。Node conditions 如 Ready、MemoryPressure、DiskPressure 反映健康状况；labels 用于 affinity/selector，taints 用于排斥不匹配 Pod。节点可能自注册，也可由管理员或云控制器创建；控制面通过 Lease/心跳检测失联。

## 4. 工程实践与设计权衡

GPU Node 除 CPU/内存外还应记录 GPU 型号、显存、MIG profile、驱动/CUDA 兼容、拓扑（NVLink/PCIe/NUMA）和网络带宽等标签；Device Plugin 将可调度 GPU 数量注册给 kubelet。升级驱动或变更 MIG 前应 cordon/drain，检查 PDB 与训练 checkpoint，避免直接终止分布式作业。区分 node allocatable 与 nvidia-smi 的物理显存余量：Kubernetes GPU count 不等于 GPU memory quota。

## 5. 易混概念与边界

Node 是 API 中的集群工作机器对象，不等于 Pod 或容器。Node `capacity` 与 `allocatable` 不同；GPU extended resource 表示可分配设备数，不天然表示显存份额或 GPU utilization。kube-proxy 并非每种集群网络实现都必须使用。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Pod request 总和不能直接与 Node capacity 比较？** 答：调度器主要依据 allocatable 与已分配 requests 进行资源可行性判断；系统预留、kubelet 预留和驱逐阈值使 allocatable 通常小于 capacity。

2. **问：Node Ready=True 是否代表 GPU 一定可用于调度？** 答：不一定。GPU 驱动、Device Plugin、资源注册、设备健康和扩展资源 allocatable 仍可能异常；应检查节点资源、plugin DaemonSet 与设备健康状态。

## 7. 中等难度考试题（含解析）

1. **题：Node capacity CPU=64、系统预留=4、kubelet预留=2，忽略其它扣减，allocatable CPU 是多少？** 解：`64−4−2=**58 CPU**`。

2. **题：一个 Node allocatable 有 8 张 GPU，已有 Pod requests 5 张，理论剩余多少张可调度 GPU？** 解：`8−5=**3 张**`，假设没有其它设备隔离、MIG 切分或健康异常。

## 8. 权威来源与延伸阅读

- [Kubernetes Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)：用于核对规范、架构与实现语义的官方资料。
- [Kubernetes Node Status](https://kubernetes.io/docs/reference/node/node-status/)：用于核对规范、架构与实现语义的官方资料。
- [Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)：用于核对规范、架构与实现语义的官方资料。

> 数字算例均为题设下的简化教学推导，不是某个集群的性能承诺。
