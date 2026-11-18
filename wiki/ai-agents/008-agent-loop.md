# Agent Loop（智能体循环）

> AI Agents · 专题：基础概念与角色 · 适用范围：通用智能体系统设计；具体 SDK 与平台版本以对应文档为准

## 1. 核心定义

**Agent Loop（智能体循环）**：Agent Loop 是智能体为完成目标重复执行“观察状态→选择行动→执行→检查反馈”的控制循环；应有可验证的停止条件与资源上限。

**适用边界：**循环可以显式 while/状态机实现，也可嵌入框架；并非每一步都要调用模型。

## 2. 形象理解

像机器人清扫：先看房间、选路线、走一步、检查障碍，再决定下一步。

**类比的局限：**每次循环都获得新信息并非必然，盲目迭代可能重复错误甚至无限运行。

## 3. 技术原理与核心内容

简化伪代码：`while steps < max_steps and not done: observation = inspect(state); action = policy(observation); result = execute_if_allowed(action); state = update(state,result)`。必须分别处理最终回答、工具错误、预算超限、用户取消和需要人工确认。

## 4. 工程实践与设计权衡

网页表单自动化时，选择提交动作后必须读取页面/服务端状态确认是否成功；连续两轮相同错误则触发熔断或重新规划，不把重试次数当成功证据。

## 5. 关联知识与易混辨析

Agent Loop 是控制结构，ReAct 是其中一种把推理与行动交替组织的方法；循环也可以由规则策略实现。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么只设置 max_steps 仍不够？** 答：还要控制 wall-clock deadline、工具成本、累计 token、外部副作用数量和安全退出；单轮可能无限阻塞。
2. **问：怎样判断循环中发生了无效重复？** 答：记录状态摘要、工具参数与结果；连续重复且没有新增信息时触发停止、换策略或人工接管。

## 7. 中等难度考试题（含解析）

1. **题：题设总预算 12 次迭代，首次规划耗 2 次、每次查工具后再决策耗 2 次，最多完整查工具多少回？** 解：剩余 10 次，每回 2 次，最多 5 回；假定未额外消耗终止确认迭代。
2. **题：模型输出完成标志但外部订单仍为待处理，是否应终止？** 解：应使用业务验证条件，不能仅依赖语言声明；若核验失败则修正、报告失败或交接。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK：Running agents](https://openai.github.io/openai-agents-python/running_agents/)：运行循环与停止。
- [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents)：Agent 环境反馈循环。
