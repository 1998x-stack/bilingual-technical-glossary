# Inference-time Compute（推理时计算）

> AI Agents · 专题：模型能力与推理 · 通用概念；产品特性以文档版本和模型接口为准

## 1. 核心定义

**Inference-time Compute（推理时计算）**：Inference-time Compute（推理时计算）指模型在推理阶段为处理输入和产生输出而消耗的计算量，包含预填充和逐 token 解码等工作，某些推理模型还包含内部推理计算。通常用 FLOPs、token/请求、GPU 时间或成本近似表征。

**适用边界：**模型推理消耗不等于训练成本；仅用输出 token 数不能无损反映真实 FLOPs，缓存、批处理、硬件和隐藏推理都会改变估算。

## 2. 形象理解

像餐厅做一份菜需要的锅灶时间：原材料预处理与烹饪都耗资源，出菜张数只是粗略线索。

**类比的局限：**在不同硬件或并发下，相同 token 数的耗时和能耗可能差很多。

## 3. 技术原理与核心内容

可拆成 prefill（对输入及历史上下文做前向计算）和 decode（逐步生成新 token）；对注意力架构，长上下文与 KV cache 行为影响两者开销。为教学可定义 `C_total≈C_prefill+C_decode+C_reasoning`，但计量项的可观测性依供应商实现。评估算法可在相同硬件、相同批量/精度下报告每请求计算量。

## 4. 工程实践与设计权衡

**工程案例：**推理服务遭遇慢查询，先查输入长度分布、批次、输出长度、缓存命中与队列等待；避免单纯降低模型思考时间而丢失必要质量。测量应覆盖 TTFT、TPOT、总体 GPU 秒和任务成功率。

**失败模式与验证：**把端到端网络等待全算作模型 FLOPs、或仅根据参数量推算实际费用，都会误导工程决策。量化与批处理降低成本的效果也要在真实负载下测量。

## 5. 关联知识与易混辨析

Inference-time Compute 是推理阶段所有计算；Test-time Compute 常特指有意增加的搜索、验证、多样本或长推理预算以提升准确性。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么增加 output token 上限不必然增加实际 FLOPs？** 答：上限是可用配额，不等于实际生成长度；只有输出达到更长轨迹时才可能增加解码工作，且模型实现和缓存会影响实际量。
2. **问：怎样报告两个服务的推理成本比较才公平？** 答：固定任务集、模型版本、输入输出长度分布、硬件与并发，记录总用量、吞吐、尾延迟和准确率；单独报告缓存与工具费用。

## 7. 中等难度考试题（含解析）

1. **题：教学假设 prefill 需要 4×10^11 FLOPs，decode 需要 6×10^11 FLOPs，总计算量多少 TFLOPs？** 解：合计 10^12 FLOPs=1 TFLOP 的计算量，不能混淆为 TFLOPS（每秒的性能单位）。
2. **题：两个模型输出均 100 token，一个输入 500 token，一个输入 5000 token，推理计算量必然相同吗？** 解：不必然；长输入增加 prefill 与相关上下文处理，KV 缓存及注意力实现还会影响 decode 成本。

## 8. 权威来源与延伸阅读

- [OpenAI API · Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)：推理模型、推理 token、预算与上下文。
- [OpenAI API · Counting tokens](https://developers.openai.com/api/docs/guides/token-counting)：精确 token 统计与请求组件。
