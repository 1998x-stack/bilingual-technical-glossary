# AI Agents · 第 12 批（221–240）知识路径与专业审稿清单

> 本页是 Wiki 内部生产/复核文档，不在 GitHub Pages 读者导航展示编辑进度。术语顺序与中文翻译以 [AI Agents 332 条原始词表](../../glossaries/ai-agents.md) 为准。第 12 批已完成 20/20 篇候审长文，独立专家签核仍 pending。

## 第一阶段：超时、重试与故障恢复（221–227）

**Exponential Backoff → Timeout → Deadline → Failover → Compensating Action → Transaction Boundary → Execution Log**。

- *Exponential Backoff* 采用 `min(cap,base×factor^(k−1))` 计算重试间隔，通常配合 jitter。对 401、403 等授权失败不盲重试，写操作收到超时先查 transaction_id。
- *Timeout* 仅说明等待超时，不能证明远端没有完成副作用；*Deadline* 是任务总时间预算，不能给每一次重试重置全局预算。
- *Failover* 需要租约/fencing、稳定 operation_id、备用节点状态版本，防止 split-brain 双主写入。
- *Compensating Action* 是跨服务 Saga 的合法业务补救，不是数据库 ROLLBACK；退款、撤回通知可能有不可逆费用。
- *Transaction Boundary* 在 PostgreSQL 的 BEGIN/COMMIT 内具备原子性，但多服务操作须配合 outbox、幂等、审计和补偿。
- *Execution Log* 应记录 trace_id、span_id、task_id、tool_call_id、operation_id、状态和资源版本；必须先执行数据脱敏才能出口，不拿模型成功文本当后端真实结果。

## 第二阶段：Agent 评测基础（228–230）

**Agent Evaluation → Benchmark → Evaluation Dataset (Eval Set)**。

Agent Evaluation 检查真实业务结果、工具行动、轨迹安全、费用、延迟；Benchmark 是包含统一任务、环境、评分协议的标准化体系；Eval Set 是实际样例集合，要隔离 train/dev/holdout、覆盖安全边界与失败场景。软件工程可以借鉴 SWE-bench 的 issue/测试环境，但必须锁定具体版本和数据许可，防止训练污染。

## 第三阶段：评测维度与指标（231–240）

| 指标 | 关注点 | 核心陷阱 |
|---|---|---|
| Task Success Rate | 已验证成功任务 / 全部有效任务 | 排除失败/未执行项会美化分母 |
| End-to-end Success Rate | 最终目标 + 授权 + 环境成功 | 工具返回 200 不等于事务完成 |
| Tool-call Accuracy | 工具、参数、时机和权限正确 | 工具名正确但参数越权 |
| Action Success Rate | 后置环境是否真正改变 | timeout 后状态不明 |
| Trajectory Evaluation | 执行序列与工具行为 | 最终正确却曾越权 |
| Trajectory | 可观察动作、工具结果和状态日志 | 不等于模型隐藏思维链 |
| Outcome Evaluation | 最终产物/后置条件 | 没有覆盖中间风险 |
| Process Evaluation | 规则、审批与安全路径 | 不必规定唯一固定路线 |
| Faithfulness | 回答断言是否有给定上下文支持 | 资料本身可能错误 |
| Factual Accuracy | 是否符合可靠外部真实事实 | 即使忠于旧文档也可能过时 |

特别注意：Ragas Faithfulness 按 claim 分解支持度，约等于 `supported_claims/all_claims`，并非真实世界事实正确率。评测必须记录来源时间与技术版本，保存不确定项，不因参考 URL 可点击便假定其支持断言。

## 综合工程案例：会创建 PR 的代码 Agent

用户提出“修复仓库性能回归、合并前保证安全”。验收必须涵盖：真实 GitHub PR 存在、目标 base/head 正确、测试和安全检查成功、写入文件范围符合授权。计划中的关键阶段如下：

1. 运行器从 checkpoint 恢复状态，先查已经提交的真实 PR/commit，而非重新创建重复对象。
2. 遇到 429 限速使用指数退避+jitter；若创建 PR 超时，用稳定 operation_id 查询真实状态。
3. 需要生产部署时必须经过 Human Approval，审批绑定 commit SHA、环境、操作与有效期。
4. 在固定 Eval Set 中复现权限拒绝、CI 失败、超时与错误资源，记录每步工具调用、外部结果和最终 Artifact。
5. 结果评测核对真实 PR/CI；过程评测阻断越权访问、重放副作用；忠实度与事实准确性分开审查文档总结。

## 中等难度面试题

**问：**Agent 的最终 GitHub PR 正确，是否足以认为所有评测指标成功？

**参考答案：**不够。Agent 可能在过程中读取其他用户私有资源、触发未经批准的生产部署或重复付款。Outcome Evaluation 可能通过，但 Process/Trajectory 需要依据真实 trace 与授权检查独立否决，并报告风险与成本。

## 中等难度考试题

**题：**某 Agent 完成了 50 个任务，40 个最终目标正确，但其中 2 个因越权而不满足端到端安全条件。另有一次报告包含 8 条可核验事实，只有 6 条从检索材料中得到支持。求严格 E2E 成功率及忠实度。

**解：**严格 E2E `(40−2)/50=76%`；Faithfulness 为 `6/8=75%`。后者仅证明与给定材料的相容程度，并不证明 6 条本身在现实中一定正确。

## 参考原始资料

- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph · Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [OpenAI Agents SDK · Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [AWS · Retry with Backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)
- [Amazon Builders' Library · Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- [PostgreSQL · Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [OpenTelemetry · Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)
- [SWE-bench](https://www.swebench.com/)
- [Ragas · Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)

## 审稿验收要求

逐篇核对英文术语、适用条件、来源支持度、例题的算术与边界条件。对版本敏感接口依据当前版本文档核查，不把写作阶段自动化 CI 当专家审核。所有词条仍为 `pending`；真实人工 reviewer_id、正文 SHA 与日期缺一不可。下一批从 **241–260** 的鲁棒性、复现性及评判模型等评测术语继续。
