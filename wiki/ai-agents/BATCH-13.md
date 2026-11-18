# AI Agents · 第 13 批（241–260）学习路径与独立复核要点

> 该文件用于编辑、专业校验与学习路径编排，不在公开 GitHub Pages 的读者导航显示编辑批次状态。Canonical 源：[AI Agents 332 条](../../glossaries/ai-agents.md)。本批 20/20 篇已成稿，但独立专家技术审稿仍为 `pending`。

## 一、评测质量与人工标注（241–247）

从 **Robustness** 和 **Reproducibility** 入手：前者强调遇到环境扰动/工具失败后的能力和安全稳定性，后者要求模型、工具、环境、数据集、评分器和随机性均有明确记录。固定随机种子并不足以消除云端模型版本漂移或并行调度差异。

**LLM-as-a-Judge** 可以规模化评价开放文本，但会出现位置、长度偏好和对候选输出中恶意指令的易感性。需要先通过 **Human Annotation** 的可靠标签校准，报告与人工的一致性和分歧，而不能把 Judge 分数当支付/代码测试的真实 oracle。**Ground Truth** 是版本化参考事实或后置条件，不是模型生成的一句标准答案。

**Regression Test** 包含确定性的工具行为合约，以及真实服务/文件状态的 E2E 验证；**Scenario-based Evaluation** 应覆盖权限拒绝、服务故障和用户拒绝替代方案，而不是只放正常成功例。

## 二、五套著名 Agent 基准（248–253）

| 基准 | 主要挑战 | 判分侧重点 | 容易误解的地方 |
|---|---|---|---|
| GAIA | 通用、复杂多步检索/文件/推理任务 | 可核验的最终答案 | 并不证明真实业务系统写操作安全 |
| SWE-bench | 真实软件仓库 issue 修复 | 指定环境中的补丁与测试 | 通过现有测试不等于无安全回归 |
| WebArena | 网页长程浏览器交互 | 目标网站状态变化 | 页面布局/账号与 reset 方式显著影响结果 |
| OSWorld | 桌面 GUI、多应用操作 | 目标系统应用/文件状态 | 需要固定 OS 镜像、应用版本和分辨率 |
| τ-bench | 带真实风格政策约束的工具客服 | 目标业务数据库状态与 policy | 单次成功不等于多轮稳定完成 |
| BFCL | 函数/工具名、参数及多轮/agentic 能力 | AST/执行等类别评分 | 不能把 V4 overall 当作生产级授权保证 |

**版本警告：**BFCL 当前官方站点 V4 的汇总方式与最早 AST 评测类别已不同，比较分数必须带 dataset_version、模型执行模式和评分器版本。公开基准都可能出现答案泄漏与环境变更。

## 三、从评测进入安全治理（254–260）

- **Guardrail（护栏）**：输入、工具、输出各有不同保护位置。只在输出阶段检测会太迟，因为工具副作用可能早已发生。
- **Policy Constraint（策略约束）**：将组织规则建成可测试的执行层政策，而不是仅写进 prompt。默认拒绝未知身份或关键条件缺失的敏感动作。
- **PoLP（最小权限）**：模型只获得当前任务所必需的仓库、资源、动作和时间窗权限。对 Agent as Tool 和跨 MCP/A2A 连接尤需防止权限外溢。
- **Permission Scope**：OAuth scope 描述权限类别，但有 `orders:read` 并不意味着可以读取任意租户订单，仍需 owner/tenant ACL。
- **Access Control**：每次服务端动作都以可信 subject + resource + action + context 做 PEP/PDP 决策，不靠前端隐藏按钮。
- **AuthN / AuthZ**：前者确认‘主体是谁’，后者确认‘能对这个对象做什么’。审批决定、身份认证和业务后置条件也是彼此独立的事实。

## 综合案例：可信的代码维护 Agent

用户让 Agent 修改 Bug 并创建 Pull Request。系统在测试环境中用 SWE-bench 风格的问题和脚本化评测器验证真实 git diff/测试成功；回归集另外验证拒绝读取其他仓库的文件；输入包含恶意 README 时也必须由 Git API 的真实 read/write 权限阻止越权操作。最终报告同时给出任务成功率、权限违例率、测试版本及运行成本。只有模型说‘PR 已创建’而查询不到真实 PR 时，Outcome Evaluation 应判失败。

## 中等面试题

**问：**为什么一个 Agent 在 BFCL 得分很高也不能直接获得生产 GitHub merge 权限？

**参考答案：**BFCL 衡量工具选择和参数等能力，不能自动证明用户授权、仓库对象级 ACL、审批条件或外部事务正确性。真实 merge 需要服务端写权限、合规审批、CI gate 和当前 commit 版本检查。

## 中等考试题

**题：**同一模型在 100 个正常任务中成功 90 个，在等规模扰动任务中成功 72 个。求扰动下绝对成功率、相对保持率和相对下降比例。

**解：**绝对成功率 72%；相对保持率 72%/90%=80%；相对下降比例 20%（相对基线），或 18 个百分点的绝对差异。

## 官方资料

- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)
- [OpenAI Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
- [GAIA · Paper](https://arxiv.org/abs/2311.12983)
- [SWE-bench](https://www.swebench.com/)
- [WebArena](https://webarena.dev/)
- [OSWorld](https://os-world.github.io/)
- [τ-bench](https://github.com/sierra-research/tau-bench)
- [BFCL V4 Official Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [NIST SP 800-207 · Zero Trust](https://csrc.nist.gov/pubs/sp/800/207/final)

## 独立审稿 Checklist

逐篇验证基准英文名称、各基准评分标准与版本边界；核查数学例题的分母和独立性假设；检查 AuthN、AuthZ、scope、PoLP、Guardrail 的互斥/交集关系。禁止将自动化 CI 或 LLM Judge 的结果伪造为独立专家签核；审稿记录应包含 reviewer ID、正文哈希与日期。
