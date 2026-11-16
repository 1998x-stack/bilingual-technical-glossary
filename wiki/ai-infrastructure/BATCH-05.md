# Kubernetes 调度、GPU 集群与存储基础设施

> 仓库作者内部学习路线，不是读者导航；公开入口始终是统一 TERM/ATLAS Explorer 的术语详情页。

## 一、镜像与容器运行时

先读 [Container Image](081-container-image.md) 与 [Docker](082-docker.md)，理解 OCI manifest、layer digest、多架构 index、BuildKit 缓存和 Docker Engine/containerd/runc 的分工。随后读 [Kubernetes](083-kubernetes.md)、[Pod](084-pod.md)、[Node](085-node.md)，把镜像、运行单元、工作节点和控制面串成一条生命周期。

## 二、GPU 如何进入 Kubernetes 调度

[GPU Operator](086-gpu-operator.md) 管理驱动、Toolkit、Device Plugin、GFD、DCGM 和 MIG 组件；[Device Plugin](087-device-plugin.md) 通过 kubelet gRPC 接口注册设备、报告健康状态并分配容器设备。再读 [Scheduler](092-scheduler.md)、[Resource Quota](093-resource-quota.md)、[Node Affinity](094-node-affinity.md) 与 [Taint and Toleration](095-taint-and-toleration.md)，理解资源声明、硬约束、软偏好和节点排斥如何共同决定 Pod 放置。

## 三、批任务、自动扩缩容与抢占

[Job](088-job.md) 管理有限任务，[CronJob](089-cronjob.md) 按时创建 Job；[HPA](090-horizontal-pod-autoscaler.md) 调整 Pod 副本，[Cluster Autoscaler](091-cluster-autoscaler.md) 调整节点池。对同步训练，重点阅读 [Gang Scheduling](096-gang-scheduling.md) 与 [Preemption](097-preemption.md)：Kubernetes v1.37 原生 PodGroup/Gang Scheduling 已进入 Beta，但默认关闭，启用前需确认 GenericWorkload feature gate 和 API 版本；Kueue 的 all-or-nothing admission 与物理拓扑检查是另一层工作负载准入能力。

## 四、AI 数据存储

[Object Storage](098-object-storage.md) 以 object key/API 管理数据，适合模型权重、语料与 checkpoint；[Block Storage](099-block-storage.md) 提供原始块设备，适合随机 I/O、数据库与持久卷；[Distributed File System](100-distributed-file-system.md) 提供跨节点文件/目录接口，需理解 HDFS NameNode/DataNode 与 CephFS MDS/RADOS 的元数据和数据路径差异。

## 研究时必须回答

1. OCI image tag、manifest digest、platform-specific digest 分别锁定什么？
2. 为什么 GPU Operator Ready 不等于 `nvidia.com/gpu` 已进入 Node Allocatable？
3. Scheduler、HPA、Cluster Autoscaler 与 Kueue 的职责边界是什么？
4. Gang Scheduling 的 all-or-nothing 到底发生在准入、放置还是 Pod Ready 阶段？
5. 对象、块、文件三类存储如何映射到训练数据集、模型 checkpoint 和数据库？
6. HDFS 的 NameNode 元数据瓶颈为何会被数百万小文件放大？

## 一手资料

- [Kubernetes v1.37 Gang Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/)
- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/)
- [Kueue All-or-nothing Scheduling](https://kueue.sigs.k8s.io/docs/concepts/all_or_nothing/)
- [OCI Image Specification](https://github.com/opencontainers/image-spec)
- [Apache HDFS Architecture](https://hadoop.apache.org/docs/r3.4.3/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [CephFS](https://docs.ceph.com/en/latest/cephfs/)
