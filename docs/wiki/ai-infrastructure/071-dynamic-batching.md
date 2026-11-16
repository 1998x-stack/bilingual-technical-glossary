# Dynamic Batching（动态批处理）

> 学科：AI Infrastructure · 专题：推理与服务 · 以维护者文档及具体引擎版本为准

## 1. 核心定义

动态批处理（Dynamic Batching）根据请求到达时间、形状和可兼容执行策略，积累多个请求再合成为一个 batch 进行模型执行。NVIDIA Triton 的动态批处理器尤其适用于可合批的无状态模型，并在等待延迟与更高吞吐之间做取舍；它不是自回归 LLM 每轮允许请求进出的连续批处理。

## 2. 形象理解

一辆接驳车最多载 8 人，司机可以多等几毫秒把车坐满，但先来的乘客多等了时间。固定一次发车的乘客不能随时更换，和每站都能上下人的电梯不同。

## 3. 技术原理与核心内容

在 Triton 中可配置 `max_batch_size`、`preferred_batch_size`、`max_queue_delay_microseconds` 及队列策略。请求入队后，scheduler 在形状/后端允许的情况下选择一组样本交给模型实例；batch 可能按 GPU 计算效率获益，同时增加排队与临时激活占用。`max_queue_delay` 不等于强制所有请求都等待满指定时间；超时、优先级和服务负载决定实际调度。

## 4. 工程实践与设计权衡

对图片分类与 embedding 服务，固定模型和负载，以 batch=1、4、8、16 观察实测执行时延、queue P95、吞吐和内存；稀疏到达时避免为了满批牺牲 SLA。存在 variable shapes、sequence state 或多模型实例时要验证能否安全合批。调大队列窗口后应同时看完成 RPS 与端到端 P99，不能只看 GPU kernel 提速。

## 5. 易混概念与边界

普通 dynamic batching 组装完整模型执行；continuous batching 在生成式模型的每个迭代调度点入退请求。两个机制可以用于不同场景，但不能将 Triton 的动态合批配置直接解释为 LLM token-level scheduler。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么动态合批能提高吞吐却恶化小流量延迟？** 答：较大 batch 能摊薄 kernel 启动开销，但小流量下凑批等待更长。需要按请求到达率对比 queue + compute 总时间。

2. **问：动态合批时所有请求能随意混在一起吗？** 答：不能；形状、后端支持、状态一致性、最大 batch 和优先级都有限制。部分有状态模型需要 sequence batcher，而不是普通 dynamic batcher。

## 7. 中等难度考试题（含解析）

1. **题：19 个兼容请求、最大 batch 8，忽略其它限制，至少多少次模型执行？** 解：`ceil(19/8)` = **3 次**，例如 8、8、3；这不保证调度一定产生此分组。

2. **题：某请求凑批等待 6ms、模型运行 9ms、网络回传 2ms，无重叠，总响应时延？** 解：`6+9+2=**17ms**`，未计前后处理。

## 8. 权威来源与延伸阅读

- [NVIDIA Triton Batchers](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html)：具体机制、实施边界与计算语义的原始或维护者资料。
- [NVIDIA Model Configuration](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html)：具体机制、实施边界与计算语义的原始或维护者资料。

> 所有数值算例均为声明假设下的教学推导，不能替代线上基准或外部领域专家核验。
