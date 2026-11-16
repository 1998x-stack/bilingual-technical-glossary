# Container（容器）

> 学科：AI Infrastructure · 专题：调度与容器 · 具体实现应核对官方接口及版本

## 1. 核心定义

容器（Container）是利用操作系统内核提供的进程、文件系统、网络等隔离机制以及资源控制，把应用及其运行依赖组成可部署执行单元的技术。Linux 容器通常共享宿主机内核，与完整虚拟机分别运行独立内核不同。容器镜像是创建容器的静态模板，**镜像不是运行中的容器**。

## 2. 形象理解

把每个团队安置在隔断明显的共享写字楼：有独立房间、门牌、网络接入和配额，但共用大楼的基础结构。隔间并非和整栋楼的安全边界一样强，隔墙设计、门禁权限和楼宇管理仍重要。

## 3. 技术原理与核心内容

典型 Linux 容器 runtime 利用 namespaces（PID、mount、network、user 等）隔离可见性，用 cgroups 控制 CPU/内存资源，结合 rootfs/overlay 文件层、capabilities、seccomp、AppArmor/SELinux 等减少权限与攻击面。OCI 运行时规范定义创建/启动容器的低层接口。Kubernetes 的 Pod 可以包含多个共享网络命名空间的容器，Pod 并不是“只有一个容器”。AI GPU 容器还依赖宿主驱动和 NVIDIA Container Toolkit/device plugin 的适当配置，不能把 GPU 驱动简单打包到镜像就假定设备可用。

## 4. 工程实践与设计权衡

构建模型推理容器时，固定不可变镜像 digest、最小非 root 用户、只读 rootfs、资源 requests/limits、健康检查与机密注入方式，验证内核/驱动兼容。生产运行不要默认 privileged、hostNetwork 或挂载宿主 Docker socket；为日志、指标和 volume 提供受控路径。诊断 OOMKilled 区分 cgroup memory limit 与 GPU device OOM，两者表现和处理方式不同。

## 5. 易混概念与边界

Container 与 VM 的隔离层级不同；**Container Image** 是可分发的只读层结构，**Pod** 是 Kubernetes 调度单位，可能包含一个或多个容器；**Docker** 是常用构建/运行工具，非容器概念本身。

## 6. 中等难度面试题（含参考答案）

1. **问：容器里看到 root 是否意味着具有宿主 root 权限？** 答：不一定。user namespace 可以映射容器内 UID，capabilities、seccomp 和宿主映射决定权限；但 privileged/host mount 等配置可能破坏隔离，所以要实施最小权限。

2. **问：为什么容器镜像包含 CUDA 库却不一定能使用 GPU？** 答：GPU 访问仍依赖宿主驱动、设备节点和 runtime device injection，Kubernetes 中还需 device plugin/operator 申请资源，版本兼容必须验证。

## 7. 中等难度考试题（含解析）

1. **题：某容器 cgroup memory limit=4 GiB，常驻匿名内存 3 GiB，再申请 1.5 GiB 且没有释放/其它回收空间，是否越限？** 解：总需求 `3+1.5=**4.5 GiB**`，超过上限 **0.5 GiB**，可能遭受 OOMKill 或分配失败，具体受内存回收机制影响。

2. **题：每个推理 Pod 请求 2 CPU、8 GiB 内存；节点可分配 16 CPU、48 GiB，忽略其它限制最多放几个相同 Pod？** 解：CPU 允许 `16/2=8`，内存 `48/8=6`，瓶颈内存，最多 **6 个 Pod**；实际还要计 daemonset、GPU/拓扑和碎片。

## 8. 权威来源与延伸阅读

- [Kubernetes Containers Concepts](https://kubernetes.io/docs/concepts/containers/)：用于核对相关技术机制与版本边界的官方资料。
- [Open Container Initiative Runtime Specification](https://github.com/opencontainers/runtime-spec)：用于核对相关技术机制与版本边界的官方资料。

> 题中数字为教学假设，不是任何设备、服务或容器环境的真实压测结果。
