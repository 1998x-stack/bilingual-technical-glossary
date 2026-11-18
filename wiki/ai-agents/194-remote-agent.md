# Remote Agent（远程智能体）

> AI Agents · 专题：A2A：智能体间协议 · 以 A2A 最新正式规范为依据，和旧版消息模型须区分

## 1. 核心定义

**Remote Agent（远程智能体）**：Remote Agent（远程智能体）是通过网络接口对外提供可调用能力的 Agent，A2A 中通常表现为具备 Agent Card 和服务 endpoint 的服务端。它可独立维护任务状态、访问自身授权工具，并返回消息或产物。

**适用边界：**远程不一定意味着跨公司，也不等于一定使用 A2A；只有满足 A2A 的卡片、绑定和消息/任务语义才可称 A2A 合规。远端的工具权限与上游 Agent 的权限必须分别验证，不能隐式继承。

## 2. 形象理解

像跨城市协作的实验室，发包方通过标准接口提出实验要求，实验室内部流程由其负责，最后返回报告。

**类比的局限：**距离远不意味着专业可信，也不能把远端声称的结果当实际物理实验记录。

## 3. 技术原理与核心内容

Remote Agent 暴露 URL、协议 binding、skills 与 security schemes；客户端采用受信任发现渠道、TLS 与所需认证 token 建立交互。远端处理请求返回 Task/Message，需记录 input mode、output mode 和数据位置，必要时支持 streaming/push。对于跨域数据，最小化消息中的个人信息并在业务范围内限制 Artifact 下载。

## 4. 工程实践与设计权衡

**工程案例：**研发 Agent 把 OCR 解析任务发给另一个团队的远程图像处理 Agent，约束只能处理指定公开测试图片。远端返回文件 Artifact 的 URL 后，Client 验证域名、hash、mimeType 与下载权限，避免任意网络抓取。

**失败模式与验证：**伪造远端地址/证书、未校验 webhook 来源、错误假设双方时区或数据保留政策、使用远端返回的不可信命令。测试协议版本、身份信任、敏感数据最小化与资源撤回。

## 5. 关联知识与易混辨析

Remote Agent 强调部署/交互位置；A2A Server 是标准协议服务角色；Specialist Agent 强调领域能力；Agent as Tool 强调经理调用专家但保持对话控制权。

## 6. 中等难度面试题（含参考答案）

1. **问：远程 Agent 给出下载链接时应核对哪些因素？** 答：来源身份、允许域名、资源级权限、内容类型、哈希与文件大小，避免不可信 URL 和敏感泄漏。
2. **问：一个普通 REST 服务是否天然就是 A2A Remote Agent？** 答：不是，须实现必要的 Agent Card、消息、Task/Artifact 语义和支持绑定。

## 7. 中等难度考试题（含解析）

1. **题：向两个远端 Agent 各发一个任务，一个状态 working、一个 completed，完成率？** 解：1/2=50%，不能把 working 当成功。
2. **题：远端返回同名文件但 SHA256 与预期不一致，能直接纳入交付吗？** 解：不能，需核对来源和文件完整性。

## 8. 权威来源与延伸阅读

- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：Client/Remote Agent、Message、Task、Artifact。
- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：核心概念、操作与服务绑定。
