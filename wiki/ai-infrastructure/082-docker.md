# Docker（Docker 容器平台）

> 学科：AI Infrastructure · 专题：调度与容器 · 技术边界按 Kubernetes、OCI 与运行时官方规范核对

## 1. 核心定义

Docker 是一套用于构建、分发和运行容器化应用的工具与平台生态，包含 Docker CLI、Docker Engine/daemon、镜像构建能力、镜像仓库交互、网络和 volume 等管理接口。现代 Docker Engine 通常借助 containerd 与 OCI runtime（如 runc）创建容器；Docker 不是 Linux 容器隔离机制本身，也不是 Kubernetes 的同义词。

## 2. 形象理解

Docker 像软件装配与运输工厂：Dockerfile 是装配工序，image 是标准化包装，registry 是仓库，container 是从包装中启动的运行实例。Kubernetes 更像管理多台工厂的排班与运维系统。

## 3. 技术原理与核心内容

典型路径：CLI 通过 Engine API 与 dockerd 交互；BuildKit 执行 Dockerfile 构建、生成 OCI 兼容镜像；Engine 调用 containerd 管理镜像/容器生命周期，再由 OCI runtime 按 bundle 配置、namespaces、cgroups 启动进程。Docker volume 将数据放在容器可写层之外；bridge/overlay 等网络模式提供连接。Build cache 按指令与输入校验复用步骤，前置依赖安装步骤通常应先于频繁变化的源代码 COPY。

## 4. 工程实践与设计权衡

生产环境优先采用多阶段构建、非 root 用户、最小基础镜像、固定 digest、只读 root filesystem 与受限 capabilities；secret 应通过 BuildKit secret mount 或运行时 secret 注入，不要写入 Dockerfile ARG/ENV 或 layer。注意 Docker socket 几乎等同宿主高权限控制面，不能随意挂入不可信容器。Kubernetes 运行时可以是 containerd/CRI-O，不要求安装 Docker Engine。

## 5. 易混概念与边界

Docker 是工具/产品生态；OCI 定义镜像与运行时标准；containerd 是容器生命周期管理组件；runc 是常见 OCI runtime。Docker image 是制品，Docker container 是运行实例；Docker Compose 管理多容器应用，但不是 Kubernetes 调度器。

## 6. 中等难度面试题（含参考答案）

1. **问：Docker Engine、containerd、runc 的职责如何区分？** 答：Engine 提供 Docker 管理 API/体验；containerd 管理镜像、快照与容器生命周期；runc 按 OCI runtime spec 创建并启动底层容器进程。不同版本具体组件集成方式会变化。

2. **问：为什么不应把 /var/run/docker.sock 挂载进普通业务容器？** 答：拥有 Docker socket 的进程往往可请求宿主 daemon 创建特权容器、挂载宿主根文件系统等，等价于获得接近宿主 root 的控制能力。

## 7. 中等难度考试题（含解析）

1. **题：一个 Dockerfile 有 9 个构建步骤，第 4 步输入变化导致后续步骤缓存失效；第 1–3 步未变，最多重跑几步？** 解：需要重跑第 **4–9 步，共 6 步**；第 1–3 步可复用缓存（前提是构建上下文和基础镜像未变化）。

2. **题：同一镜像启动 7 个容器，每个容器可写层新增 250MB，忽略共享与压缩，额外可写层空间多少？** 解：`7×250MB=**1750MB**`，即约 **1.75GB** 十进制；镜像只读层仍可共享。

## 8. 权威来源与延伸阅读

- [Docker Engine overview](https://docs.docker.com/engine/)：用于核对规范、架构与实现语义的官方资料。
- [Docker build cache and layers](https://docs.docker.com/learn/content/how-image-layers-and-the-build-cache-work/)：用于核对规范、架构与实现语义的官方资料。
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)：用于核对规范、架构与实现语义的官方资料。

> 数字算例均为题设下的简化教学推导，不是某个集群的性能承诺。
