# Task（任务）

> AI Agents · 专题：基础概念与角色 · 适用范围：通用智能体系统设计；具体 SDK 与平台版本以对应文档为准

## 1. 核心定义

**Task（任务）**：Task 是具有输入、执行主体、可交付输出和验收规则的工作单元，可被安排、委派、重试或拆分为 Subtask。

**适用边界：**Task 的粒度可从一次工具调用到完整业务流程；与底层线程、进程或异步协程不必一一对应。

## 2. 形象理解

像项目看板的一张任务卡：写清谁负责、何时完成、交付什么、如何验收。

**类比的局限：**卡片数量不代表工作量，任务依赖与外部资源可能让并行执行无收益。

## 3. 技术原理与核心内容

任务模型可含 task_id、input、preconditions、dependencies、status、output、acceptance。状态从 pending→running→succeeded/failed/cancelled；依赖完成前不得启动，重复消费需要去重。

## 4. 工程实践与设计权衡

批量生成 40 份报告：按客户拆分 Task，生成与审核分开，审核失败只重做失败项；最终汇总应等待所有必需任务通过。用 task_id 与重试序号追溯每次执行。

## 5. 关联知识与易混辨析

Goal 是最终结果；Task 是推进目标的工作单元；Subtask 更细，但未必单独对外可见。

## 6. 中等难度面试题（含参考答案）

1. **问：什么时候应该把任务拆小？** 答：当其可独立验收/失败重试、依赖明确且交接成本可控时；切太碎会增加上下文与编排开销。
2. **问：多 Agent 处理 Task 时怎样保证一致性？** 答：统一 task_id、状态机与责任人，写入要求幂等，最终结果由明确验收节点确认；不同 Agent 的语言结论不能自动成为事务。

## 7. 中等难度考试题（含解析）

1. **题：题设 12 个相互独立任务，每个占 3 min，3 个工人并行且无开销，理想完成时间？** 解：总工作量 36 worker-min，理想下界为 36/3=12 min；现实受负载不均和依赖影响。
2. **题：Task A 结束后才能开始 B、C，B 与 C 都完成后启动 D，给出合法执行次序。** 解：先 A，再并行 B/C，最后 D；不能让 D 在任一依赖未完成时启动。

## 8. 权威来源与延伸阅读

- [OpenAI：Practical Guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)：工作流与任务完成。
- [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents)：任务拆解与编排模式。
