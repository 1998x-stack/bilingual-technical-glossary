# Device Plugin（设备插件）

> 学科：AI Infrastructure · 专题：调度与容器 · Kubernetes 与 GPU 组件行为应按部署版本验证

## 1. 核心定义

Kubernetes Device Plugin 是节点级扩展机制，让硬件厂商或集群组件向 kubelet 发布 GPU、FPGA、NIC 等专用设备，并在容器创建时执行设备分配。插件将设备以扩展资源名（例如 `nvidia.com/gpu`）暴露给调度系统；Pod 声明资源 limits 后，scheduler 可据 Node allocatable 进行整数设备数量调度。

## 2. 形象理解

像实验室设备管理员：先登记仪器清单与健康状态，调度系统根据可用数量安排实验，真正开门交接仪器时再执行权限、设备文件和环境注入。仅有登记表并不表示仪器硬件正常。

## 3. 技术原理与核心内容

Device Plugin 通常在节点以 DaemonSet 运行，通过 Unix socket `/var/lib/kubelet/device-plugins/` 向 kubelet gRPC 注册；`ListAndWatch` 持续上报设备 ID 与 Healthy/Unhealthy 状态；kubelet device manager 在容器创建时调用 `Allocate`，插件返回设备节点、环境变量、mount 或 CDI 相关配置。`GetPreferredAllocation` 可协助选择设备组合。扩展资源通常不可超卖且以整数计数；GPU request 需放在 limits，若 requests 与 limits 同时指定必须相等。

## 4. 工程实践与设计权衡

GPU 节点上排查 `nvidia.com/gpu` 不可见时，确认 plugin DaemonSet Running、socket 注册、驱动可见性、插件日志、节点 capacity/allocatable 与 Pod resource request。多 GPU 训练还要关注 NVLink/PCIe/NIC 拓扑；普通 device plugin 的整数资源分配并不保证跨 GPU 拓扑最优。共享 GPU、MIG、时间切片和 DRA 是不同资源管理路径，应明确插件具体实现。

## 5. 易混概念与边界

Device Plugin 是 kubelet 的节点设备扩展接口，不等于 scheduler、GPU Operator 或硬件虚拟化。它把资源发布给调度器，但是否满足 NUMA/NVLink/网络拓扑还可能需要额外调度插件或 DRA。

## 6. 中等难度面试题（含参考答案）

1. **问：ListAndWatch 与 Allocate 分别解决什么问题？** 答：ListAndWatch 向 kubelet持续报告设备清单和健康变化；Allocate 在容器创建时返回具体设备访问配置，二者分别偏向资源发现和实际注入。

2. **问：为什么请求 1 个 nvidia.com/gpu 不等于获得 1/8 GPU 显存？** 答：传统扩展资源以整数设备计数，不表达显存比例或算力份额；MIG/时间切片等需单独配置资源模型和隔离策略。

## 7. 中等难度考试题（含解析）

1. **题：节点注册 8 张 GPU，其中 2 张标记 Unhealthy，插件对 kubelet 上报的 Healthy 设备数是多少？** 解：`8−2=**6 张**`，理论上可分配的数量为 6；仍需考虑已分配设备。

2. **题：一个 Pod 同时 requests 与 limits `nvidia.com/gpu`，分别为 2 和 1，是否满足 Kubernetes GPU 资源约束？** 解：不满足；GPU 只能指定 limits，若同时指定 requests 和 limits，两者必须相等。

## 8. 权威来源与延伸阅读

- [Kubernetes Device Plugins KEP](https://www.kubernetes.dev/resources/keps/3573/)：用于核对官方 API、架构与调度语义。
- [Kubernetes Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)：用于核对官方 API、架构与调度语义。
- [NVIDIA Kubernetes Device Plugin](https://github.com/NVIDIA/k8s-device-plugin)：用于核对官方 API、架构与调度语义。

> 例题数据为教学假设，未考虑集群所有控制环与异常路径。
