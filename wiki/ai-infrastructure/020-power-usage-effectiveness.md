# Power Usage Effectiveness（电源使用效率 · PUE）

> AI Infra Wiki · Batch 01 · 术语 020/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Power Usage Effectiveness**（**电源使用效率**，PUE）：数据中心总能耗与 IT 设备能耗之比。

**适用边界：** PUE=数据中心总设施能耗÷IT 设备能耗。解释该术语时应指明具体架构、设备代际或测量口径，不能将理论指标直接等同工程表现。

## 2. 形象理解

PUE 衡量机房除了真正运行计算机，还为散热、配电等附属服务额外花了多少能量。理想值趋近 1，但不表示服务器工作效率高。

## 3. 技术原理与核心内容

PUE=数据中心总设施能耗÷IT 设备能耗。通常二者应使用相同边界和测量周期；PUE 更低通常表示设施支持开销更小，但不直接刻画模型计算效率、碳排或水耗。

## 4. 工程实践与设计权衡

长期评估优先使用边界明确且时间覆盖充分的数据，避免用某一瞬间极低的 PUE 代表全年；同一机房改进也须核对 IT 负载变化。AI 集群还应同时统计每 token 能耗和资源利用率。

## 5. 易混概念与边界

PUE 与 GPU 性能/瓦不同：前者是设施级能耗分配指标，后者是计算效率指标；PUE 越接近 1 不代表模型越好。

## 6. 中等难度面试题（含参考答案）

1. **问：PUE 由 1.5 降到 1.2 一定表示总碳排下降 20% 吗？** 答：不能；IT 负载、电力来源和总用电量均可能变化。
2. **问：为什么不能比较两家数据中心的瞬时 PUE 就断定谁更优秀？** 答：测量边界、天气、IT 负载、季节和统计周期不一致。

## 7. 中等难度考试题（含解析）

1. **题：某设施年总耗电 15 GWh，IT 设备耗电 10 GWh，PUE？** 解：15/10=1.5。
2. **题：若 IT 耗电不变而 PUE 从 1.5 降至 1.3，年总耗电减少多少？** 解：从 15 GWh 降至 13 GWh，减少 2 GWh。

## 8. 参考资料与延伸学习

- [官方或行业技术资料](https://intelligence.uptimeinstitute.com/sites/default/files/2023-10/Keynote%20report%2069_Glossary.pdf)。请核对所用硬件与文档版本。
- [NVIDIA CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：了解性能度量与优化（不意味着本术语仅适用于 NVIDIA）。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 说明：题目中的规格与时间均为演示假设，未标注设备型号时不应视为产品实测指标。
