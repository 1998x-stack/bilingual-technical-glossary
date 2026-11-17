# Total Cost of Ownership（总体拥有成本 · TCO）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 具体告警、性能或会计口径需按环境与约定核对

## 1. 核心定义

总体拥有成本（Total Cost of Ownership，TCO）是在明确分析周期与服务边界内，购买、使用、维护和退役某项基础设施/服务的所有相关成本总和。AI Infrastructure TCO 不只包含 GPU 采购价或云实例账单，还可能涉及 CPU、内存、网络、存储、电力、制冷、机房、运维人工、许可、备件、故障损失和残值；需避免重复计入共享成本。

## 2. 形象理解

买车成本不只是标价，还包含油费、保险、维修、停车位、税费和未来转售价格。两辆车购入价相同，在五年使用周期内可能有截然不同的总体成本。

## 3. 技术原理与核心内容

简化五年自建成本 `TCO=CapEx+Σ_t(OpEx_t+repair_t+energy_t+labor_t)−residual_value`；若做贴现现金流比较，必须统一折现率、现金流时间点、税务假设和币种。云托管方案通常更偏 OpEx，但实际还有预付、网络出区、存储、日志、闲置容量、服务支持和迁移成本。FinOps 的 unit economics 把 TCO 分摊到有效工作量，例如有效百万 tokens、训练 GPU-hours 或成功请求；若把输入 token 与输出 token 混算，需要注明加权计费与质量/SLO 边界。

## 4. 工程实践与设计权衡

比较 H100/H200/B200 自建与云租用时，需统一工作负载模型、训练 MFU/在线 goodput、预留容量、峰谷负载、可中断率、节点使用寿命和运维规模；使用多个场景进行敏感性分析，而非拿某一天的 Spot 低价与长期自建平均成本直接比较。共享平台需按租户记录可归属成本与分摊规则，并明确空闲 GPU 与平台 overhead 如何分摊。

## 5. 易混概念与边界

TCO 是完整生命周期成本，不等于 CapEx 或 OpEx 单项，也不等同 ROI（回报率）和每 token 单位成本（后者是 TCO 或选定成本池的分母归一化）。单纯提高 GPU utilization 也不保证 TCO 下降，因为功耗和失败风险可能同时上升。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能只比较自建 GPU 一次性购置成本与云 GPU 每小时单价？** 答：自建还含折旧、能源、网络、机柜、人工和空闲成本；云还有出站流量、服务费和预付承诺。必须按同一时间边界与有效工作量归一。

2. **问：如何设计 AI Infra TCO 的成本分摊？** 答：先区分可直接归属的实例/存储/流量与共享平台服务，再按 GPU-hours、保留容量或实际 goodput 建立透明规则，避免多项目重复报销同一成本池。

## 7. 中等难度考试题（含解析）

1. **题：3 年内采购/机房初始投入 600 万元，年度运营费 120 万元，期末残值 60 万元，忽略贴现，总 TCO？** 解：`600+120×3−60=**900 万元**`。

2. **题：同一周期 TCO=900 万元、完成 30 亿个有效输出 tokens，单位百万输出 token 成本？** 解：`9000000/(3000000000/1000000)=**3000 元/百万输出 token**`；忽略质量差异与输入 token。

## 8. 权威来源与延伸阅读

- [FinOps Unit Economics](https://www.finops.org/framework/capabilities/unit-economics/)：供独立核对上述机制、公式与实施前提的一手资料。
- [FinOps Allocation](https://www.finops.org/framework/capabilities/allocation/)：供独立核对上述机制、公式与实施前提的一手资料。
- [AWS Cloud Financial Management](https://docs.aws.amazon.com/whitepapers/latest/aws-cost-optimization-pillar/welcome.html)：供独立核对上述机制、公式与实施前提的一手资料。

> 数值题仅为学习示例，不是生产硬件压测或会计处理意见。
