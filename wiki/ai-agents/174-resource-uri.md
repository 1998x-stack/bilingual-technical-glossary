# Resource URI (URI)（资源标识符 · URI）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；旧版行为应分别核对

## 1. 核心定义

**Resource URI (URI)（资源标识符）**：Resource URI（资源标识符，URI）是在 MCP 中用于唯一识别和读取某个资源的统一资源标识字符串。URI 由 scheme 等部分组成，可以是通用 Web 地址，也可以是应用定义的 `schema://`、`file://` 或其他合法方案，实际解释由服务端和协议绑定决定。

**适用边界：**URI 不是授权 token，不等于可直接打开的公共 HTTPS URL；其格式也不自动避免目录遍历、越权或资源注入。`file://` 资源不意味着远端 Server 可以任意读取 Host 的本地磁盘。

## 2. 形象理解

像档案馆中每一份文件的馆藏编号，能说明应该找哪份，但还需要借阅资格与实体存储位置。

**类比的局限：**知道编号未必知道实际存放处，编号看起来相似的资源也可能属于不同客户。

## 3. 技术原理与核心内容

RFC 3986 定义 URI 的 scheme、authority、path、query、fragment 等语法；MCP 资源对象的 uri 字段应与 resources/read 请求严格关联。Server 对 URI 做规范化、scheme 白名单、路径边界和 ACL 检查，避免通过编码或别名访问非授权文件；可保留稳定 doc_id、version 与 MIME 元信息，确保引用可回溯。

## 4. 工程实践与设计权衡

**工程案例：**知识库 MCP Server 暴露 `kb://tenant-a/contracts/123`，只允许 tenant-a 具备项目权限的用户读取；客户 B 知道 URI 也不能读取。服务端不能仅依据字符串包含 `tenant-a` 就信任用户身份。

**失败模式与验证：**路径规范化前后 ACL 不一致、资源 URI 指向重定向的私有地址、命名空间重复、将用户传入 URI 解释成任意文件访问请求。做编码变体、路径穿越、跨租户、缓存键污染和引用完整性测试。

## 5. 关联知识与易混辨析

Resource URI 是资源标识字段；MCP Resource 是资源及其内容；URI scheme 只规定标识符形式，不能说明可靠性或读取权限；Tool URL 参数属于业务语义而非 MCP Resource URI 的同义词。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Resource URI 不能充当身份认证凭证？** 答：标识符可能被猜出或泄露；必须结合可信登录凭证做资源级授权。
2. **问：如何避免资源读取中的路径穿越？** 答：限制允许 scheme 和根目录、规范化路径并检查真实目标与 ACL，避免仅做字符串前缀判断。

## 7. 中等难度考试题（含解析）

1. **题：两个 URI 的 path 一样但 scheme 分别是 file 与 kb，是否必然指向同一资源？** 解：不一定，scheme 不同意味着标识符解释机制可不同。
2. **题：资源地址包含序号 123，客户端自增至 124 就能读取别人的数据吗？** 解：不能，服务端必须以当前主体做对象级授权，防止 IDOR。

## 8. 权威来源与延伸阅读

- [IETF RFC 3986 · URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)：URI scheme、authority、path 等标准语法。
- [MCP 2026-07-28 · Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)：资源 URI 与读取方式。
