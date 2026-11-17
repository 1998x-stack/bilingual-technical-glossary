# Cost per Million Tokens（每百万词元成本）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 按 SLO、租户、资源约束与版本说明结论边界

## 1. 核心定义

每百万词元成本（Cost per Million Tokens）是把定义明确的 AI 推理服务成本归一化到一百万个计费或有效 token 的单位经济指标。其分子可为 GPU-only、基础设施、或全量 TCO 成本池；分母可按 input、output、total token 或具有任务价值的有效响应 token 计算。必须明确口径，尤其不能将供应商面向客户的每百万 tokens 售价直接等同内部推理成本。

## 2. 形象理解

像物流每送达一百万件合格包裹的平均成本：若一半包裹退回或服务时间不达标，不应简单把处理量增加当作降低单位履约成本。

## 3. 技术原理与核心内容

若窗口总归属成本 C、有效输出 token 总量 N_out，计算 `unit_cost_out = C×10^6/N_out`。对于输入/输出计算强度不同的 LLM，可分别建模 `C=C_prefill+C_decode+C_idle+C_network+C_storage+C_shared` 并按 token 类型/请求分配；多模型共池可按 GPU-seconds、预约容量或可验证的调度时长分摊。供应商 API 账单可能按 prompt cache 命中、推理加速层、tokenizer 或不同价格档计费；这些**收费口径**与内部实际 GPU 成本不一定相等。应对比相同质量、SLO、模型和业务流量结构，防止通过降低服务质量“优化”数字。

## 4. 工程实践与设计权衡

为真实线上服务记录 model/version、input/output token、request completion、排队、有效 token、GPU-hours 与总账单，按同一结算窗口做集群级与单模型级报表。做 batch size、量化、prefix cache、PD 分离等优化时，联合观察成本/百万有效 token、TTFT/ITL P99、用户成功率与错误预算；只有在质量/SLO不退化时才宣称成本效率提升。结算周期、折扣覆盖、闲置预留资源和跨区域传输必须完整纳入选定成本池。

## 5. 易混概念与边界

Cost per Million Tokens 是单位成本，不是 API 售价、收入、毛利、GPU 利用率或 Energy per Token。若两个模型 tokenizer 不同、输出语义长度差异显著或质量不同，直接比较 token 数成本会失真。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么生产单位 token 成本应考虑空闲 GPU？** 答：为满足峰值与 SLO 而预留的容量在低流量时仍花钱；若成本只按实际 decode 时间算，会低估真实服务成本。

2. **问：为什么输入和输出 token 不能总按相同成本估算？** 答：prefill 可并行处理输入，decode 往往逐步访问模型权重/KV，两阶段的算力、显存带宽和服务约束不同；成本分摊需声明策略。

## 7. 中等难度考试题（含解析）

1. **题：某集群月成本 48 万元，月有效输出 12 亿 tokens，成本/百万输出 token？** 解：`480000/(1200000000/1000000)=**400 元/百万输出 token**`。

2. **题：方案 A 每百万有效输出 token 成本 600 元，方案 B 450 元，SLO/质量相同，单位成本降低百分比？** 解：`(600−450)/600=**25%**`。

## 8. 权威来源与延伸阅读

- [FinOps Unit Economics](https://www.finops.org/framework/capabilities/unit-economics/)：用于核对管理机制与性能边界的原始资料。
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：用于核对管理机制与性能边界的原始资料。
- [Google SRE SLOs](https://sre.google/workbook/implementing-slos/)：用于核对管理机制与性能边界的原始资料。

> 例题是假设条件下的算术演示，不是对生产多租户安全性或容量的认证。
