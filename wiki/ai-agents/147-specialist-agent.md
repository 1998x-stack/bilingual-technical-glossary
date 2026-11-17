# Specialist Agent（专业智能体）

> AI Agents · 专题：多智能体协作 · 多智能体角色和可复核的工程能力边界

## 1. 核心定义

**Specialist Agent（专业智能体）**：Specialist Agent（专业智能体）是被配置用于特定领域、任务或能力集合的 Agent，例如法务条款审查、代码测试或账单查询，通常拥有聚焦的指令、相关工具与领域评估标准。它的价值在于职责分离，不等于模型拥有专业执照或判断一定正确。

**适用边界：**专业 Agent 的能力边界依底层模型、知识源和工具权限确定。角色名称不能赋予法律、医疗或金融专业资质，也不能允许越权读取或执行高风险业务动作。

## 2. 形象理解

像医院的影像科专家专注识读某类检查，而综合治疗仍需其他科室和可信验收。

**类比的局限：**专注特定任务提高效率并不保证诊断正确，跨学科结论仍需协作与必要的专业审查。

## 3. 技术原理与核心内容

配置可包含 instructions(domain), tool_allowlist, output_schema, evaluation_set 和 handoff_policy。经理可以将 specialist 暴露为受限工具并自己综合结论；另一种方式是 handoff 让专业 Agent 接管后续对话。对专业领域记忆与检索做 tenant/ACL 限制，评估领域准确率、越权拦截率和拒绝不确定问题的能力。

## 4. 工程实践与设计权衡

**工程案例：**售后平台提供退款查询 Specialist，只拥有只读 get_refund_status 接口和帮助文档；创建退款要进入另一个有审批的业务流程。模型看到用户催促也不能凭 Specialist 角色获得新付款权限。

**失败模式与验证：**专业指令过拟合、知识过期、工具列表权限过宽、从经理处转发了不必要的私人上下文。使用专业标注数据、同名工具对抗题与权限负例评估。

## 5. 关联知识与易混辨析

Specialist Agent 强调单领域深度与受限工具；Generalist Agent 跨任务广度；Manager Agent 负责调度与最终答案；专业 Agent 可以是 Worker，但并非所有 Worker 都是专家。

## 6. 中等难度面试题（含参考答案）

1. **问：专业 Agent 与仅在提示词写‘你是专家’有什么不同？** 答：可靠设计还需受限工具、相关文档、结构化输出和独立领域评测；单句角色扮演不能提供资质或保证。
2. **问：何时应该通过 handoff 将对话交给 Specialist？** 答：当该领域需要不同工具、政策或专门指令且确实需要专家持有后续用户响应控制时；否则可作为 manager 的工具。

## 7. 中等难度考试题（含解析）

1. **题：专业 Agent 在 40 道已标注领域题中答对 34 道，准确率？** 解：34/40=85%；需再评估关键高风险错误与测试集代表性。
2. **题：只读 Specialist 收到用户要求直接创建退款，是否可以执行？** 解：不可以，超出工具权限；应说明限制或转交受控审批流程。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Agents](https://openai.github.io/openai-agents-python/agents/)：Agent 配置、工具与 handoff。
- [OpenAI Agents SDK · Handoffs](https://openai.github.io/openai-agents-python/handoffs/)：专员接管、输入过滤与控制权转移。
