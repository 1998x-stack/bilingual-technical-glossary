# Berkeley Function Calling Leaderboard (BFCL)（伯克利函数调用榜单 · BFCL）

> AI Agents · 专题：评测体系与常见基准 · 按最新基准版本与真实执行权限界定结论

## 1. 核心定义

**Berkeley Function Calling Leaderboard (BFCL)（伯克利函数调用榜单）**：Berkeley Function Calling Leaderboard（BFCL，伯克利函数调用榜单）是评估 LLM 和 Agent 选择函数、产生合法参数、处理多工具及多轮工具交互能力的公开评测体系。随基准版本演进，已从早期 AST 结构匹配扩展到更完整的多轮与 agentic 任务。

**适用边界：**BFCL 分数不能直接等同于 Agent 的端到端支付/部署安全性。不同版本的任务类别和评分权重不同，且 native function-calling 与 prompt-based 输出模式、成本和延迟不同；必须引用具体版本、运行配置与成绩发布时间。

## 2. 形象理解

像编程语言考试里让考生选择正确库函数并填参数，后来考试还加入多步骤流程，但它仍不是完整的生产上岗安全认证。

**类比的局限：**函数签名选择正确不意味着后端确实执行、数据库授权满足或数据源可靠。

## 3. 技术原理与核心内容

评测数据包含函数 schema、用户任务与参考调用。非 live 类别可能使用 AST/结构比较，live 类别执行实际工具或模拟执行验证效果，多轮任务检查连续工具使用与状态更新。当前官方 BFCL V4 页面包含 agentic、multi-turn、single-turn、hallucination measurement 与 format sensitivity 等类别。报告 overall accuracy 时应说明各类分数组合规则，不能用旧版评分器衡量新测试集并当排名。

## 4. 工程实践与设计权衡

**工程案例：**财务 Agent 需要查订单详细信息。候选输出函数名 `get_order` 正确，但参数把 tenant=A 写成 B，这既是 BFCL 类别可能捕捉的参数错误，也应在真实系统触发对象级 ACL 拒绝；不能因语法合法就评为完整安全成功。

**失败模式与验证：**工具名对但参数错、无可用函数却胡乱调用、模型记住公开 schema、跨版本 AST 解析规则差异、用 leaderboard 最高分代表产品风险。用 missing-function、irrelevant-function、parallel/multi-turn 和外部后置状态案例补评。

## 5. 关联知识与易混辨析

BFCL 强调函数调用与工具交互；SWE-bench 侧重真实代码修复；τ-bench 侧重带政策约束的业务对话；完整 Agent Evaluation 还需环境动作、安全与成本。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 BFCL 的 AST 正确不能直接证明真实业务成功？** 答：函数调用结构合法只是调用意图，真实 API 可能拒绝、超时或返回未提交，需要检查最终状态。
2. **问：比较 BFCL V3 与 V4 时要注意什么？** 答：类别、评分器、模型运行和汇总权重可能变化，需同版本重测或只在各自条件下报告。

## 7. 中等难度考试题（含解析）

1. **题：某 BFCL 子类 200 个调用中 166 次满足评分器，准确率？** 解：166/200=83%。
2. **题：两个类别各 70% 和 90%，按等权平均 overall？** 解：(70%+90%)/2=80%；现实官方 overall 需按发布评分规则计算。

## 8. 权威来源与延伸阅读

- [BFCL · Berkeley Official](https://gorilla.cs.berkeley.edu/leaderboard.html)：函数调用、multi-turn 与 agentic 类别。
- [BFCL · Evaluation code](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)：AST、工具执行与评分器。
