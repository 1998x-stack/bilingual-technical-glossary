# Blackboard（共享黑板）

> AI Agents · 专题：多智能体协作 · 多 Agent 协作模式与信任边界；SDK API 以版本文档为准

## 1. 核心定义

**Blackboard（共享黑板）**：Blackboard（共享黑板）是多 Agent/多知识源协作的一种架构：不同参与者围绕公共工作区读取当前问题状态、提出部分解或假设，并按条件贡献更新。它用于异构专家对复杂问题逐步求解，而不是普通文件夹共享的同义词。

**适用边界：**Blackboard 的控制器可以是事件驱动、规则或专门 Agent；公共黑板不是无限制写权限区。每个贡献应包含状态、来源、适用范围与冲突处理，且并发更新不保证自然收敛。

## 2. 形象理解

像不同学科专家围绕一面问题白板，分别写上事实、待确认假设、验证结果和下一步需求。

**类比的局限：**白板上写得多不等于接近真相，某人的猜测不能自动升级为经核验的结论。

## 3. 技术原理与核心内容

BlackboardState 可划为 goals、hypotheses、evidence、pending_tasks、accepted_facts；参与者观察变化触发可用规则，提交 `{author,task_id,revision,claim,status,source}`。控制器选择下一知识源并用版本/CAS 保持一致；状态项支持 proposed→verified/rejected/expired 迁移。对于不可逆动作，应使用独立 approval gate，不允许任意 Agent 写入黑板的‘批准’文字就获得执行权限。

## 4. 工程实践与设计权衡

**工程案例：**故障排障协作中，网络 Agent 写入丢包证据，数据库 Agent 写入连接池指标，协调者把二者时间戳对齐并提出‘故障是否由网络导致’的待验证假设。只有日志和指标交叉验证后才将假设提升为 accepted_fact。

**失败模式与验证：**知识源反复覆盖彼此结论、未分 proposed 和 verified、黑板无限增长、跨团队隐私泄漏、旧状态触发错误操作。使用状态版本、数据保留期、角色级写权限和冲突队列测试。

## 5. 关联知识与易混辨析

Blackboard 是以共享工作区促进协作的设计模式；Shared Memory 只是可共享的存储能力；Message Bus 通过事件交付而不要求单一公共状态；Consensus 讨论如何达成共同判断。

## 6. 中等难度面试题（含参考答案）

1. **问：黑板中的假设何时可升级为 accepted_fact？** 答：应具备可追溯证据、独立验证、时间/资源范围和必要的审批，不能仅因为多个 Agent 口头同意。
2. **问：Blackboard 如何避免高并发更新丢失？** 答：用版本号 CAS、事件日志、按字段 reducer 或串行协调器，定义状态冲突解决策略。

## 7. 中等难度考试题（含解析）

1. **题：黑板上有 12 条假设，4 条被证实、3 条被否定、其他仍待确认，待确认条数？** 解：12−4−3=5 条。
2. **题：两个 Agent 同时写 revision=7，其中一个先提交成 8，另一个也强制写 8，会导致什么问题？** 解：可能覆盖已提交内容；第二个应检测版本冲突并重读后合并。

## 8. 权威来源与延伸阅读

- [AutoGen · Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)：协作消息与共享上下文治理。
- [LangGraph · Add memory](https://docs.langchain.com/oss/python/langgraph/add-memory)：store namespace 与持久化状态管理。
