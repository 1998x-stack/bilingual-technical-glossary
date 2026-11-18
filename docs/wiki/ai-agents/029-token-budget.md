# Token Budget（词元预算）

> AI Agents · 专题：模型能力与推理 · 通用概念；产品特性以文档版本和模型接口为准

## 1. 核心定义

**Token Budget（词元预算）**：Token Budget（词元预算）是在一次模型请求或整个智能体任务中，为输入、可见输出、内部推理、工具上下文与多轮重试预先规划的用量上限和配额。它是运行策略，不是模型自身的物理容量。

**适用边界：**`max_output_tokens` 等字段通常控制一轮生成上限；整个 Agent 多轮总预算需要应用层额外累计与拦截。

## 2. 形象理解

像项目预算：即使会议室能坐 100 人，也可能只给某次会议 20 个座位，剩下的资源留给其他环节。

**类比的局限：**预算分配不会自动改善回答质量；过小配额可能在 JSON/推理完成前截断输出。

## 3. 技术原理与核心内容

定义总预算 `B_total`，分别追踪 `B_input`、`B_output`、`B_reasoning`（如可见）和每轮额外调用的预算。实际字段可能有包含关系，**不可把 output 与其内部 reasoning 子项重复相加**。运行器按 usage 累计 `used_total += usage.total_tokens`，对下一轮预留最坏输出空间，达到阈值就停止或压缩非关键上下文。

## 4. 工程实践与设计权衡

**工程案例：**批量分析 50 份合同，给每份固定上限，再按难度允许审批后的额外预算。监控总成本、完成率及 incomplete 比例；逐步减少无价值的历史对话而不丢失审计状态。

**失败模式与验证：**常见错误是将 token 预算仅设为模型的最大输出，而忽略重新发送的长历史、工具 schema、重复失败重试与隐藏推理 token。跨服务计费还可能区分缓存输入和标准输入价格。

## 5. 关联知识与易混辨析

Token Budget 是应用分配策略；Context Window 是单次容量限制；Rate Limit/Quota 是服务层按时间或账户控制的频率/资源约束。

## 6. 中等难度面试题（含参考答案）

1. **问：如何保证多轮 Agent 的总 token 不超出任务配额？** 答：在运行器逐轮读取实际 usage，拒绝可能突破余量的新请求或降低上下文/输出上限；处理不完整响应并保留取消/汇报余量。
2. **问：推理模型输出只有几行却花掉了大部分输出配额，如何解释？** 答：内部推理 token 可计入生成用量且占输出上限，不能用可见字符预测；查看服务 usage 的 reasoning details。

## 7. 中等难度考试题（含解析）

1. **题：某任务总预算 12000 token，前两轮 usage.total_tokens 为 3500、4200，第三轮拟上限 3000。理论上还有多少余量，是否够？** 解：余量 12000−3500−4200=4300 token；按题设第三轮最多 3000，能容纳，还余 1300。需注意真实 API 的输入/输出计数口径。
2. **题：某响应 output_tokens=1500，其中 reasoning_tokens=900，是否应将二者相加作为 2400 output token？** 解：不应。reasoning_tokens 是 output_tokens 中的子项；这轮总生成按 1500 统计，不能重复计数。

## 8. 权威来源与延伸阅读

- [OpenAI API · Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)：推理模型、推理 token、预算与上下文。
- [OpenAI API · Counting tokens](https://developers.openai.com/api/docs/guides/token-counting)：精确 token 统计与请求组件。
