# Container Image（容器镜像）

> 学科：AI Infrastructure · 专题：调度与容器 · 技术边界按 Kubernetes、OCI 与运行时官方规范核对

## 1. 核心定义

容器镜像（Container Image）是供容器运行时创建容器 root filesystem 与默认执行配置的不可变制品。OCI Image 将镜像表示为配置对象与有序文件系统 layer；manifest 引用 config 和 layers 的 digest，multi-platform image index 再指向不同 OS/CPU 平台的 manifest。镜像是静态交付物，运行时创建的容器才具有可写层、进程与运行状态。

## 2. 形象理解

像一份分层装订、带有启动说明的应用发行包：基础系统、运行库和应用文件按层叠加，多个版本可共享相同底层。启动一个容器相当于用这份发行包创建独立运行实例，而不是直接在镜像上运行。

## 3. 技术原理与核心内容

OCI manifest 中 descriptor 以 mediaType、digest、size 描述 config/layers；image config 保存 architecture、OS、Env、Entrypoint、Cmd、WorkingDir 等运行参数。layer 是相对父层的文件系统 changeset，删除文件需用 whiteout 表达。digest 对内容寻址，tag 是可移动的命名指针；生产发布应使用 digest 固定内容，并验证签名、SBOM、provenance。多架构 index 允许同一 tag/digest index 根据 linux/amd64 或 linux/arm64 选择子 manifest。Dockerfile 指令与 BuildKit cache 会影响构建层和缓存命中。

## 4. 工程实践与设计权衡

AI 推理镜像应分离 build/runtime stage，固定基础镜像 digest，避免将数据集、模型权重、云凭证打进 image；把大模型权重放入受控对象存储或模型卷，减少重复拉取与镜像层膨胀。关注 registry 拉取、解压、磁盘 inode、imageGC 和节点本地缓存。GPU 镜像内的 CUDA 用户态库需与宿主 NVIDIA driver 兼容；镜像本身不会带来宿主内核驱动。用 SBOM、漏洞扫描、签名验证和可复现构建治理供应链。

## 5. 易混概念与边界

镜像不是容器；tag 不是不可变版本标识；layer digest 与最终 image manifest digest 不是同一层级。镜像层只读，容器运行时通常在其上叠加可写层；volume 数据生命周期独立于容器层。

## 6. 中等难度面试题（含参考答案）

1. **问：为何生产环境更推荐 image@sha256 digest 而不是仅使用 :latest？** 答：tag 可以被重新指向不同 manifest，导致不同节点或不同时间拉取到不同内容。digest 锁定内容寻址对象；多架构 index digest 仍会按平台选择子 manifest，因此还应记录运行平台与实际子 digest。

2. **问：为什么把 80GB 模型权重直接 COPY 进推理镜像通常不是最佳方案？** 答：会放大镜像拉取、解压、节点磁盘和版本分发成本；权重更新也会使大 layer 失效。若权重需独立版本、权限和缓存，使用对象存储/持久卷并做校验通常更合适。

## 7. 中等难度考试题（含解析）

1. **题：镜像由 4 个 layer 组成，节点已缓存其中 3 个，剩余 layer 压缩后 600MB；忽略并行和解压，至少需从 registry 下载多少？** 解：仅缺失的 layer 需要下载，因此至少 **600MB**；若 registry 或节点缓存校验失败、平台 manifest 不同，实际传输量会更大。

2. **题：一个 multi-platform index 包含 amd64 与 arm64 两个 manifest，二者分别 1.8GB 与 1.2GB；节点为 arm64，拉取镜像时选择哪个平台 manifest？** 解：选择 **arm64 的 1.2GB manifest** 及其 layers，而不是同时拉取两套完整平台镜像；实际下载仍取决于本地 layer cache。

## 8. 权威来源与延伸阅读

- [OCI Image Specification: Manifest](https://github.com/opencontainers/image-spec/blob/main/manifest.md)：用于核对规范、架构与实现语义的官方资料。
- [OCI Image Configuration](https://github.com/opencontainers/image-spec/blob/main/config.md)：用于核对规范、架构与实现语义的官方资料。
- [Docker multi-platform builds](https://docs.docker.com/build/building/multi-platform/)：用于核对规范、架构与实现语义的官方资料。

> 数字算例均为题设下的简化教学推导，不是某个集群的性能承诺。
