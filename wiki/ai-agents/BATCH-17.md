# AI Agents · Batch 17 · 源术语 321–332（候审稿）

> **内部知识学习路径。**本批为权威术语表 332 条的末批（共 12 篇）；保持原始连续编号与批次边界，不在公开 Explorer 露出批次页。所有正文为 GitHub 堆叠 PR 候审稿，尚未合并 main 或完成专家审核。

## 知识链路：编排到交付

**第一阶段：工作流控制（321–323）**：Orchestration Graph → Node → Edge。以 StateGraph 的状态更新、条件转移、并行汇合、循环退出和检查点恢复理解任务执行的真正机制。

**第二阶段：输入与权限（324–326）**：Prompt Template → Environment Variable → Secrets Management。把低信任引用、进程配置与敏感凭据分离，绝不把 Prompt 作为服务端授权机制。

**第三阶段：交付环境（327–329）**：Development Environment → Staging Environment → Production Environment。让同一不可变构建产物经隔离测试、发布候选验证与生产灰度，按 SLO 与副作用安全判定是否推广。

**第四阶段：可追溯发布（330–332）**：Version Control → Continuous Integration (CI) → Continuous Delivery (CD)。记录 Git commit、artifact digest、模型/Prompt/Schema 版本；自动验证和部署准备不替代独立专家审查和明确的生产发布决策。

## 本批 12 篇

- 321. [Orchestration Graph（编排图）](321-orchestration-graph.md)
- 322. [Node（节点）](322-node.md)
- 323. [Edge（边）](323-edge.md)
- 324. [Prompt Template（提示模板）](324-prompt-template.md)
- 325. [Environment Variable（环境变量）](325-environment-variable.md)
- 326. [Secrets Management（密钥管理）](326-secrets-management.md)
- 327. [Development Environment（开发环境）](327-development-environment.md)
- 328. [Staging Environment（暂存环境）](328-staging-environment.md)
- 329. [Production Environment（生产环境）](329-production-environment.md)
- 330. [Version Control（版本控制）](330-version-control.md)
- 331. [Continuous Integration (CI)（持续集成）](331-continuous-integration.md)
- 332. [Continuous Delivery (CD)（持续交付）](332-continuous-delivery.md)

## 贯穿型中等难度综合案例

设计一个含检索、自动汇总、用户审批与付款 API 的 Agent。要求：① 用图表示条件边与人工审批，证明没有绕过审批的写入路径；② 恢复流程不得重复付款；③ 用分级环境和动态凭据验证权限隔离；④ 以 commit/digest 记录模型、Prompt 与工具契约；⑤ CI 运行结构验证和 Chromium E2E，CD 构建候选并经过人工发布门槛；⑥ 以真实付款账本作为最终验收，不能由模型回答或流水线全绿推断业务成功。

**参考验证要点。**用 Node 隔离只读与写入，工具服务端按对象级授权和幂等键执行；隔离 staging 凭据、采用生产灰度；在 CI 验证图可达性、schema、知识内容与恢复；在 CD 留审核、回滚和对账机制。

## 专业审核状态

每篇均有 2 道中级面试题和 2 道中级考试题（含参考答案），且至少两项原始资料。**结构检查不等于对技术定义、引用与计算题的独立专家签核。**审稿台账新增 12 项，均标为 pending。
