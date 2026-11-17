# Application Programming Interface (API)（应用程序接口 · API）

> AI Agents · 专题：工具使用与环境交互 · 具体工具行为、权限与版本以官方规范为准

## 1. 核心定义

**Application Programming Interface (API)（应用程序接口）**：Application Programming Interface（API，应用程序接口）是软件组件之间公开的调用契约，规定可使用的操作、输入输出、错误和行为。Agent 常通过 HTTP、RPC 或本地库 API 访问业务系统；接口契约比自由网页操作通常更容易自动校验。

**适用边界：**API 是一般软件工程概念，不专属于 Agent，也不意味着公开网络或没有权限边界；HTTP 200 也可能对应业务层失败或异步任务尚未完成。

## 2. 形象理解

像餐厅的点餐窗口：规定可以点哪些菜、怎么付费和如何取得订单结果，后厨实现细节被隐藏。

**类比的局限：**点餐窗口遵循流程不保证食材有货、订单已送达或客户有付款权限。

## 3. 技术原理与核心内容

HTTP API 通常定义 method、path、headers/auth、request body、status codes 与 response schema；OpenAPI 可描述接口。对 GET/POST/PUT 等方法的幂等与安全语义须依 RFC 和实际服务约定：不能仅因方法名就认为业务操作可重复。客户端应管理版本、认证、限流、重试、请求 ID 与实际业务验收。

## 4. 工程实践与设计权衡

**工程案例：**库存 Agent 调用 GET /inventory 查数量，再向受控 POST /reservations 发送创建请求。创建接口使用 Idempotency-Key（如果后端支持），并在超时后以 reservation_id 查询权威结果；库存条件需在服务端事务内验证。

**失败模式与验证：**错误使用未授权凭证、将非幂等写入无条件重试、忽略分页/限流、把接口状态码当完整业务状态，都会造成数据不一致。开展合约、故障与并发测试。

## 5. 关联知识与易混辨析

API 是组件间的调用契约；Function Tool 是让模型使用能力的一种包装；Tool Adapter 在二者之间做协议及数据转换；CLI 与 GUI 可以是同一底层 API 的不同客户端。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 REST API 的 202 Accepted 不代表任务已完成？** 答：202 通常表示请求已被接受处理，业务可能异步进行；需查任务状态或回调确认最终结果。
2. **问：为何幂等性不能靠客户端认为‘这是 PUT’就自动成立？** 答：HTTP 方法有规范语义，但具体业务实现仍需验证；服务可能有非预期副作用，必须按文档/事务记录检查实际重试安全性。

## 7. 中等难度考试题（含解析）

1. **题：一个 HTTP 202 的创建请求在 2 秒后状态仍为 pending，能汇报创建完成吗？** 解：不能，最多说已被接受或仍处理中；须等待权威完成状态或适当终止。
2. **题：库存 API 当前返回 7 件，客户端想预留 8 件。应由谁最终拒绝该请求？** 解：服务端事务和库存业务规则必须拒绝；客户端可先提示，但不能替代服务端原子校验。

## 8. 权威来源与延伸阅读

- [IETF RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)：HTTP 方法、响应与状态语义。
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)：HTTP API 契约与服务描述。
