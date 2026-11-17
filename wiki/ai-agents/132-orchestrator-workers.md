# Orchestrator–Workers（编排者—工作者模式）

> AI Agents · 专题：工作流与编排模式 · 应用架构、状态恢复与工程权衡

## 1. 核心定义

**Orchestrator–Workers（编排者—工作者模式）**：Orchestrator–Workers（编排者—工作者模式）是由一个中心编排者动态判断任务需要哪些子任务，并把它们分配给多个 Worker 完成，最后收集和综合结果的多步骤协作模式。其核心是**子任务不能全部事先固定**，而非简单把独立工作并行运行。

**适用边界：**编排者可以是 LLM，也可以由程序与模型共同承担；Worker 可以是模型、工具或服务。中心编排者需要防止子任务爆炸、越权委派和未经验证的结果汇总。

## 2. 形象理解

像编辑总监接到未知主题的深度报道后，先分析问题，再临时指派法律、技术、财经记者调查，最后核对材料编成整篇报告。

**类比的局限：**总监派出的人越多不代表越可靠；每条原始材料都需要来源、版本和专业复核。

## 3. 技术原理与核心内容

流程 `task → orchestrator.decompose(task) → spawn(worker_i,scope_i,budget_i) → collect(result_i) → verify/synthesize`。动态派工时为每个 Worker 下发最小必要数据和工具权限，限制最大 worker_count、深度、token 和 deadline。编排者保存任务树与关联 ID，完成结果需经过 schema/来源校验，不允许 Worker 自行提升权限或宣称整体成功。

## 4. 工程实践与设计权衡

**工程案例：**代码迁移 Agent 收到未知复杂度的仓库升级任务，编排者先扫描模块依赖，再按实际模块创建 Worker 处理不同子项目，并由集成阶段运行完整测试。不得让两个 Worker 同时无协调写同一个核心配置。

**失败模式与验证：**中心编排器成为瓶颈、动态任务递归分裂无界、Worker 重复修改文件、汇总忽略错误、权限未按子任务限制。测试最大扇出、并发冲突和不同任务复杂度的成本曲线。

## 5. 关联知识与易混辨析

Orchestrator–Workers 动态决定工作划分；Parallelization 可基于固定静态任务；Manager Agent 是协作角色名称，不等同于所有动态派工系统；Aggregation Pattern 是结果汇总阶段。

## 6. 中等难度面试题（含参考答案）

1. **问：与固定并行三个 LLM 的方案相比，该模式最重要差别是什么？** 答：编排者根据输入动态确定任务数量、内容和分工，而不是总运行预先定义的三个相同/不同子任务。
2. **问：为什么 Worker 不应该默认继承编排者全部凭证？** 答：违反最小权限，子任务可能误操作其他资源或泄漏数据；应按任务发放受限工具与资源访问。

## 7. 中等难度考试题（含解析）

1. **题：编排任务分为 4 个 Worker，耗时 2、4、3、5 秒，分解耗时 1 秒、汇总 2 秒，Worker 理想并行，关键路径耗时？** 解：1+max(2,4,3,5)+2=8 秒；忽略资源限制。
2. **题：同一代码文件被两名 Worker 同时改写，哪类一致性机制最重要？** 解：需要基于版本的冲突检测/锁或合并审核，避免最后写入覆盖；具体数值答案无唯一值。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：编排者—工作者、评估者—优化者和常见工作流模式。
- [Anthropic · Agents cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/README.md)：多 Agent 编排和迭代反馈的原始例子。
