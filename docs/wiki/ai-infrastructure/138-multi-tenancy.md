# Multi-Tenancy（多租户）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 按 SLO、租户、资源约束与版本说明结论边界

## 1. 核心定义

多租户（Multi-Tenancy）是在共享基础设施上为多个独立用户/组织/业务单元提供服务，同时保证约定的身份、访问控制、配额、性能与数据隔离。Kubernetes namespace、RBAC、NetworkPolicy、ResourceQuota、Pod Security 与节点池/MIG 等可构成隔离层，但任何单层都不能自动提供完整的安全边界。

## 2. 形象理解

像多家公司共用一栋写字楼：大堂与供电共享，门禁、独立办公室、配额和防火分区保障不同公司的空间与数据。看不见隔壁会议室不等于物理上不能进入。

## 3. 技术原理与核心内容

控制面按租户身份与 RBAC 限制 Kubernetes API，对工作负载用 namespace/labels/quota 划分对象；数据面通过 CNI NetworkPolicy、service authN/authZ、挂载/卷权限和 secret isolation 约束访问。GPU 共享还有显存残留、KV prefix cache 跨租户复用、模型服务日志、CDN cache key、侧信道和 noisy neighbor 的风险。强隔离负载可能选择不同节点、MIG 或独立集群；共享缓存键应包括模型版本、token/配置与授权边界，不允许仅按“相同提示词”跨租户复用。计费层需要租户级 GPU-seconds、token 与存储/流量用量。

## 4. 工程实践与设计权衡

设计租户 A/B 的安全与性能验收：A 不能读取 B 的对象/secret/log/traces/缓存，不能访问 B 的推理管理 API，也不能靠不限流流量剥夺 B 的服务 SLO。验证 quota/priority、namespace RBAC、网络默认拒绝、存储权限和监控后端 multi-tenancy；建立审计轨迹、密钥轮换与跨租户事件响应流程。对 GPU time slicing 必须在文档明示没有与 MIG 等价的强隔离保证。

## 5. 易混概念与边界

Namespace 是 Kubernetes 对象隔离与管理作用域，不是强安全容器；RBAC 管 API 权限，NetworkPolicy 管 pod 网络连通性（且依赖 CNI 支持），ResourceQuota 管资源上限，MIG 管部分 GPU 硬件分区，各自职责不同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Kubernetes namespace 不足以证明 GPU 多租户安全？** 答：共享节点内核、GPU 驱动、缓存、模型服务、网络和日志仍可能形成跨租户路径；需要层层权限与隔离测试。

2. **问：如何防止一个 tenant 的高并发请求拖垮所有 tenant？** 答：按租户设请求/token quota、公平调度与队列上限，保留资源/SLO 预算并观察 noisy-neighbor，必要时用独立 GPU/MIG/节点池。

## 7. 中等难度考试题（含解析）

1. **题：集群总共 64 张 GPU，按配额给 A 24 张、B 16 张、平台保留 8 张，未分配 GPU 配额？** 解：`64−24−16−8=**16 张**`，配额不等于实际同时已占用。

2. **题：租户每秒最多处理 4000 个 tokens，突发 10s 持续请求 5000 tokens/s，无额外突发额度，理论超额 tokens？** 解：`(5000−4000)×10=**10,000 tokens**`，需要拒绝/延迟/整形，具体取决于限流实现。

## 8. 权威来源与延伸阅读

- [Kubernetes Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)：用于核对管理机制与性能边界的原始资料。
- [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)：用于核对管理机制与性能边界的原始资料。
- [Kubernetes Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)：用于核对管理机制与性能边界的原始资料。

> 例题是假设条件下的算术演示，不是对生产多租户安全性或容量的认证。
