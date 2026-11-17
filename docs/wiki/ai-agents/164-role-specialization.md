# Role Specialization（角色分工）

> AI Agents · 专题：多智能体协作 · 多 Agent 通信、一致性与独立业务验收

## 1. 核心定义

**Role Specialization（角色分工）**：Role Specialization（角色分工）是按领域知识、工具能力、数据权限或质量目标，为多个 Agent 分配不同职责的架构方法。它追求能力聚焦、降低上下文干扰并使子任务可评测，不是简单给同一模型换几个角色称谓。

**适用边界：**角色分工并不保证每个 Agent 具备相应专业资质；专员角色与真实执行权限必须分离。职责切分过细可能增加通信成本、上下文碎片和交接错误。

## 2. 形象理解

像软件团队分为架构、开发、测试和安全岗位，各自负责有明确边界的工作。

**类比的局限：**岗位名称不意味着专员一定拥有对应技能或能通过全部验收，合作还需要共同数据契约。

## 3. 技术原理与核心内容

可以建立 role_matrix={role,goal,allowed_tools,documents,output_schema,acceptance_tests,escalation_path}，由 Router/Manager 决定任务分配。对不同角色限制可见文件和工具，不共享无必要的完整聊天；按专业指标测 precision、recall、误操作率与整体完成率。职责重叠时由 Coordinator 设定最终事实来源和冲突审查机制。

## 4. 工程实践与设计权衡

**工程案例：**客户平台分别配置账单查询专家、退货政策专家和用户沟通经理。账单专家只读实时交易记录，政策专家引用生效规范，经理综合答复；正式退款必须通过有审批的独立写入 API。

**失败模式与验证：**角色越多成本越大、重复检索造成不一致、同一个隐藏提示泄漏所有专员权限、专家对跨域问题过度自信。做跨角色边界测试、工具拒绝用例和协作 A/B 评估。

## 5. 关联知识与易混辨析

Role Specialization 是设计原则；Specialist Agent 是按该原则形成的角色；Generalist Agent 覆盖多类任务；Manager/Coordinator 表示组织职责而非专业方向。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么拆成 5 个角色不一定优于单 Agent？** 答：存在协调成本和错误传递，需通过真实任务质量、成本和权限风险比较，不能只看角色数量。
2. **问：如何证明某角色确实受限于职责？** 答：检测工具允许列表、资源 ACL、输出契约、越权拒绝和可复核的运行 trace。

## 7. 中等难度考试题（含解析）

1. **题：三个专业 Agent 分别花 2、3、4 秒且串行执行、经理汇总 1 秒，总延迟？** 解：2+3+4+1=10 秒。
2. **题：账单只读角色被请求直接付款，应该怎样处理？** 解：拒绝越权并提供符合授权的受控审批路径，不把角色名称当凭证。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：经理式编排与专家交接。
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：专业角色分工与结果汇总。
