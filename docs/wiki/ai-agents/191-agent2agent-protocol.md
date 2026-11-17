# Agent2Agent Protocol (A2A)（智能体间协议）

> AI Agents · 专题：A2A：智能体间协议 · 以 A2A 最新正式规范为依据，和旧版消息模型须区分

## 1. 核心定义

**Agent2Agent Protocol (A2A)（智能体间协议）**：Agent2Agent Protocol（A2A，智能体间协议）是独立 Agent 系统之间发现彼此能力、交换消息、委派任务、跟踪状态和获取产物的开放互操作协议。它强调跨厂商/框架协作，不要求参与者暴露内部提示词、记忆或推理细节。

**适用边界：**A2A 与 MCP 互补而非替代：MCP 面向工具/资源/提示接入；A2A 描述 Agent 与 Agent 之间的通信和状态协作。A2A 协议兼容多种底层绑定，不能把某一 SDK 的 URL 或方法视为唯一实现。

## 2. 形象理解

像不同公司的项目团队共享统一工单协议：一方提出需求，另一方报告进度和交付文件，不必公开内部所有工作笔记。

**类比的局限：**格式一致并不确保代理可信、授权合法或任务真实完成；需要核验远端身份和业务结果。

## 3. 技术原理与核心内容

核心参与者为 A2A Client 与 A2A Server（Remote Agent）。服务端发布 Agent Card，声明 supportedInterfaces、skills、capabilities 和 securitySchemes；客户端选择兼容绑定并发出 SendMessage。远端可返回 Message 或带 id/contextId/status/artifacts 的 Task，客户端以 GetTask、streaming 或 webhook 跟踪。对长任务设置幂等请求、访问控制、task owner 和版本约束。

## 4. 工程实践与设计权衡

**工程案例：**业务 Agent 需要法律审查，将合同最小必要引用通过 A2A 交给独立法务 Agent；服务返回 task ID，随后提供带出处的审查 Artifact。原业务系统仍负责核实资质与授权，不能因远端说‘合规’便自动签署合同。

**失败模式与验证：**Agent Card 伪造、客户端未检查 supportedInterfaces、任务状态与产物版本错配、把远端消息当系统指令、异步重试重复提交。做互操作、鉴权、请求重复和断线任务恢复测试。

## 5. 关联知识与易混辨析

A2A 对外暴露远程 Agent 的任务接口；MCP Server 对 Host 暴露 tools/resources/prompts；普通 HTTP API 可被 Agent 调用，但并不自动满足 A2A 的状态、卡片与内容协议。

## 6. 中等难度面试题（含参考答案）

1. **问：A2A 为什么不要求暴露 Agent 内部推理？** 答：互操作只需明确可用能力、输入输出、状态与产物；暴露内部提示与记忆不是协议必要条件。
2. **问：为什么 A2A 不等于 MCP？** 答：前者是代理之间的工作协作，后者是应用调用外部工具和资源的标准，职责边界不同。

## 7. 中等难度考试题（含解析）

1. **题：三个 Agent 各处理 4 项互不重复任务，成功交付 10 项，总完成率？** 解：10/(3×4)=83.3%，仍需按真实产物验收。
2. **题：服务端回复 task_id 而没有 Artifact，可以宣称交付文档已完成吗？** 解：不能，须查询任务状态并检验对应 Artifact。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：核心概念、操作与服务绑定。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：Client/Remote Agent、Message、Task、Artifact。
