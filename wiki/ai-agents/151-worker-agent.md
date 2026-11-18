# Worker Agent（工作者智能体）

> AI Agents · 专题：多智能体协作 · 工程角色定义；职责、权限与真实验收依具体系统为准

## 1. 核心定义

**Worker Agent（工作者智能体）**：Worker Agent（工作者智能体）是从管理者或任务调度器接收范围明确的子任务，利用自身模型、工具和局部状态执行工作，并返回标准化结果的 Agent。它关注可验收的任务产出，而不是自动拥有总任务的最终决策权。

**适用边界：**Worker 不必是独立进程，也可能由同一模型实例以不同指令运行；是否可向用户答复、能否交接工具和读写共享状态由编排契约决定。任务完成的自述不能取代真实测试或工具结果。

## 2. 形象理解

如施工队的一支专业班组收到‘完成第 3 层电路检查’工单，输出检查记录给总负责人。

**类比的局限：**班组说‘检查完成’并不代表设备已经通过权威验收，经理仍须核实安全测试。

## 3. 技术原理与核心内容

工作者接口定义 TaskRequest={task_id,goal,input_refs,scope,deadline,budget,allowed_tools}，返回 TaskResult={task_id,status,artifacts,evidence,error}。管理者应分派最小必要上下文，Worker 独立执行、记录 tool_call_id 和外部副作用，并在状态未知时返回 unknown。多 Worker 并行时通过任务 ID、文件版本与冲突检查确保结果可重放和合并。

## 4. 工程实践与设计权衡

**工程案例：**大仓库升级流程中，编排者按独立模块创建三名 Worker，分别修改不同目录并运行单测；每人返回 commit SHA、测试结果、受影响文件。集成节点重新跑全仓测试并检查变更重叠，不因 Worker 自评而直接合并。

**失败模式与验证：**任务边界模糊造成重复写同一文件，Worker 继承经理全部管理员凭证，超时被当成功，模型伪造测试运行编号。验收需检查 artifact 存在、owner/ACL、资源版本和真实 CI 记录，设置并发上限。

## 5. 关联知识与易混辨析

Worker Agent 偏重执行被委派的子任务；Specialist Agent 偏重领域知识；Coordinator Agent 管理消息与同步；Supervisor Agent 监控执行。一个 Worker 可以同时是 Specialist，但角色划分不等价。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Worker 输出 done 不应使经理直接宣布整体任务成功？** 答：要核对真实 artifact、工具状态、测试和整体业务成功谓词；不同子任务可能互相冲突或失败。
2. **问：Worker 权限应怎样配置？** 答：基于任务和身份采用最小权限 tool_allowlist、资源范围和时效限制，禁止自动继承管理者全权凭证。

## 7. 中等难度考试题（含解析）

1. **题：4 个 Worker 各完成 3 个互不重复任务，最终合计多少任务？** 解：4×3=12，前提是任务 ID 不重复且确实完成。
2. **题：某 Worker 报告写文件成功但仓库中无对应 commit，系统应标记成功吗？** 解：不应；须验证文件或 commit 证据，缺失时保持 failed/unknown 并重新核查。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：编排者—工作者与评估者—优化者工作流。
- [OpenAI Agents SDK · Agents as tools](https://openai.github.io/openai-agents-python/tools/)：受限工作者由经理调用的模式。
