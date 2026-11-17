# A2A Client（A2A 客户端）

> AI Agents · 专题：A2A：智能体间协议 · 以 A2A 最新正式规范为依据，和旧版消息模型须区分

## 1. 核心定义

**A2A Client（A2A 客户端）**：A2A Client（A2A 客户端）是代表用户或上游 Agent 向远端符合 A2A 的 Server 发起消息、任务与状态查询的一方。它需要处理 Agent Card 发现、协议绑定选择、认证信息、安全输入及异步响应关联。

**适用边界：**A2A Client 不必使用某一特定语言 SDK；它可以是另一个 Agent、业务 Web 服务或编排器。Client 拥有发送任务的能力不等于对所有远端资源有授权，也不意味着任务在请求发出时已完成。

## 2. 形象理解

像项目发包单位的事务接口，先寻找合适承包商、确认合同和交付格式，再提交任务并跟踪进度。

**类比的局限：**收到工单号并不等于承包商已经完成工作；信息泄漏或错误发包也可能带来风险。

## 3. 技术原理与核心内容

客户端通过可靠 Agent Card 获取 `supportedInterfaces` 优先级和 URL、协议版本与身份要求，选择自己真正支持的 binding。发送 Message 可以设置 task/context 关联字段；收到 Task 记录 id、contextId 和当前 status，响应断连后用 GetTask 恢复。若返回直接 Message，应按协议识别其不一定创建 Task。对重试维持幂等语义并使用最小必要上下文。

## 4. 工程实践与设计权衡

**工程案例：**企业采购 Client 接到询价需求，先找能返回报价表的远端 Agent Skill，验证证书/授权后发送不含无关用户隐私的参数。若响应是 TASK_STATE_WORKING，安排查询状态而非直接按报价已生成执行付款。

**失败模式与验证：**信任未验证的 card URL，选错绑定，响应 task ID 丢失、错误处理分页、重复发单。用卡片过期、连接中断、权限撤销、同名 Agent 和不支持格式测试。

## 5. 关联知识与易混辨析

A2A Client 发起协作请求；A2A Server 提供 Agent 能力；MCP Client 发起工具/资源协议请求，二者技术职责相似但消息和状态语义不同。

## 6. 中等难度面试题（含参考答案）

1. **问：远端返回 Task 与直接 Message，客户端应如何区别？** 答：Task 可通过 ID 查询状态、获取产物；直接 Message 只是当前交互回复，不一定有可跟踪任务。
2. **问：为什么要按 supportedInterfaces 选择协议绑定？** 答：服务可能有不同协议和 endpoint，不能假设所有端点用同一 JSON-RPC 语法。

## 7. 中等难度考试题（含解析）

1. **题：Client 向 5 个 Agent 请求报价，最终 4 个返回可验证 Artifact，交付覆盖率？** 解：4/5=80%，剩余须标记未知或失败。
2. **题：同一个 task_id 返回旧状态和新状态，能仅按到达先后选最终状态吗？** 解：不应，应核对权威任务状态和事件版本/时间。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：核心概念、操作与服务绑定。
- [A2A · Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)：Agent Card 发现、安全与缓存。
