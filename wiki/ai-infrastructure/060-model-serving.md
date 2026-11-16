# Model Serving（模型服务化）

> 学科：AI Infrastructure · 专题：推理与服务 · 学习内容与发布状态由统一 Explorer 管理

## 1. 核心定义

模型服务化（Model Serving）是将训练好的模型以稳定、安全、可观测、可管理版本的方式提供给在线或批处理应用，涵盖模型制品发布、请求路由、计算执行、扩缩容、监控、灰度、回滚和成本治理。它是端到端服务过程，不只是启动一个推理脚本。

## 2. 形象理解

把科研阶段的配方变成可持续经营的餐厅：除了会做菜，还要供应链、菜单版本、订单接口、排队管理、卫生检查、投诉与关店应急。模型“可运行”不等于服务“可稳定交付”。

## 3. 技术原理与核心内容

典型部署环为 `model artifact + tokenizer/config → registry/repository → validated deployment → API gateway → router/scheduler → inference runtime → metrics/traces → rollout/rollback`。对于在线生成服务，需协调 tokenizer/聊天模板与模型权重版本，确保多副本的缓存和参数一致；可以使用 HTTP/gRPC、Kubernetes、负载均衡和流量灰度。模型治理应记录输入数据权限、输出过滤/风险策略、服务级别目标（SLO）、模型降级/超时及版本可追溯性。引擎（如 Triton 或 vLLM）提供执行 API，但往往仍需外层认证、流量限制、审计和运维平台。

## 4. 工程实践与设计权衡

模型新版本上线前以固定样本集验证输出契约和回归指标，并在可控流量下进行 shadow/canary；逐步提升流量时观察 TTFT、TPOT、P99、OOM、取消请求、错误码与单位 token 成本。记录请求 ID、模型版本、tokenizer 版本和 feature flags 以定位事故。回滚要求旧模型/依赖与路由仍可用，且新版本未兼容输入/输出 schema 时必须提供明确迁移策略。

## 5. 易混概念与边界

**Model Serving** 面向完整服务生命周期，**Inference Server** 仅是执行组件；**Model Registry** 保存制品与版本并不自动承担实时推理，**Autoscaling** 调节副本数也不能替代模型验证。在线推理中不同版本可能无法仅靠切换 URL 保证兼容。

## 6. 中等难度面试题（含参考答案）

1. **问：如何安全地将新模型逐步发布到线上？** 答：先做离线契约/安全/效果回归，指定版本与 tokenizer；再部署隔离实例，做 shadow 或小比例 canary，观察业务质量、P95/P99、资源和错误率，符合门限后逐步放量。保留可测试的回滚路径。

2. **问：为什么在线服务需要把请求级日志与模型版本关联？** 答：模型权重、tokenizer、prompt 模板和配置都可能改变输出；故障或质量回退需要定位具体请求经过的版本与路由决策。日志采集还要防止泄露敏感用户数据。

## 7. 中等难度考试题（含解析）

1. **题：每台实例稳定容量 120 请求/秒，目标利用率不超过 75%，预计峰值 300 请求/秒；最少需要几台同构实例？** 解：每台预算 `120×0.75=90 RPS`；`ceil(300/90)=**4 台**`。忽略突发流量、故障冗余和队列的额外容量，实际部署通常更多。

2. **题：新版本灰度 5% 到总共 20,000 个请求，假设完全随机独立分流，期望有多少请求进入新版本？** 解：`20,000×0.05=**1000**` 个请求，这是期望值，实际数量有随机波动；不能仅以流量比例证明新模型质量达标。

## 8. 权威来源与延伸阅读

- [NVIDIA Triton Model Repository](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_repository.html)：模型版本目录、制品管理与配置。
- [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/)：模型运行与推理 API 能力及其认证边界。

> 示例值均为有明确前提的教学假设；不同运行时、模型和硬件条件下的实际量测结果可能变化。
