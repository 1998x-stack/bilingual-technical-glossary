# Artifact（任务产物）

> AI Agents · 专题：A2A：智能体间协议 · A2A Task、Message 和 Artifact 的版本化语义

## 1. 核心定义

**Artifact（任务产物）**：Artifact（任务产物）是 A2A Agent 完成任务后提供的有名称或标识的输出资料，如文档、报告、图片或结构化 JSON。一个 Task 可以包含多个 Artifacts，每个 Artifact 由一个或多个 Part 组成，并可以通过流式事件逐步产生或补充。

**适用边界：**Artifact 是任务输出，不是聊天消息：A2A 建议将最终交付放入 artifacts 而非只写在 Message 中。Artifact 真实存在、签名有效和外部业务成功是不同问题；文件 URL、数据大小及访问权限均需验证。

## 2. 形象理解

像工单完成后交付正式检验报告及测试原始数据附件，而对话里的‘已处理’只是沟通。

**类比的局限：**收到文件名或链接不能证明文件内容正确，更不能保证真实机器已恢复正常。

## 3. 技术原理与核心内容

Task.artifacts[] 每项含 `artifactId` 与至少一个 `parts`，可带 name、description、metadata。Part 承载 text、raw、url 或 data；流式 `TaskArtifactUpdateEvent` 可提供更新片段，客户端必须按 taskId/contextId/artifactId 关联，并在 `append` 语义下正确拼接，不能把新版本覆盖旧版本。验证 Artifact 的来源、mediaType、数据完整性/哈希、文档 ACL 与任务适用范围。

## 4. 工程实践与设计权衡

**工程案例：**法律审查 Agent 交付条款风险 CSV 和逐条来源 PDF，共两个 Artifact。上游先核实这两份文件关联当前合同版本，校验 MIME 和访问权限；风险清单中写‘低风险’也不代表签署已获正式批准。

**失败模式与验证：**同名 Artifact 覆盖、任务 A 文件链接被串到任务 B、流式 append 次序错误、下载 URL SSRF、仅凭文件名推断正确类型。用大文件、分段、权限撤回和冲突 ID 进行测试。

## 5. 关联知识与易混辨析

Artifact 是完整交付对象；Message 表达交互与澄清；Part 是最小内容单元；Task State 记录执行进度，不替代最终产物验收。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能以 Agent 最后一条 Message 作为全部成果？** 答：A2A 建议用 Task 的 Artifact 保存交付数据，才能独立检索、审计和校验版本。
2. **问：一个 Artifact 的 PDF URL 来自未知内网域名应怎么办？** 答：不能直接抓取，先做域名/权限/SSRF 保护、内容类型和哈希核验。

## 7. 中等难度考试题（含解析）

1. **题：一个 Task 有 2 个 Artifact，分别 3 和 2 个 Part，总共有多少内容片段？** 解：3+2=5 个 Part。
2. **题：两个事件都更新 artifactId=5，第二个 append=true，能直接只保留第二片段吗？** 解：不能，应根据协议 append 规则合并并验证顺序。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Artifact、TaskState、事件与通知规则。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：Task、Message 与 Artifact 职责。
