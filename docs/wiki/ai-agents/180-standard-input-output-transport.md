# Standard Input/Output Transport (stdio)（标准输入输出传输）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；legacy initialize 行为按旧版单独说明

## 1. 核心定义

**Standard Input/Output Transport (stdio)（标准输入输出传输）**：Standard Input/Output Transport（stdio，标准输入输出传输）是 MCP 的一种本地进程通信绑定：Client 启动 Server 子进程，通过其 stdin 发送 JSON-RPC 消息、通过 stdout 读取回复和通知。每条协议消息采用 UTF-8 单行 JSON、以换行分隔，日志应写向 stderr。

**适用边界：**stdio 是传输/进程通信方式，不是 MCP 工具、资源或授权机制。它通常适合受控本地集成，不意味着子进程沙箱隔离或自动安全；对远程服务可采用 Streamable HTTP。2026 版与旧版共享 stdio 基本 framing，但生命周期和消息方向规则随版本不同。

## 2. 形象理解

像两程序之间的专门传送管道，一端送请求、一端收标准化响应，错误日志走另一条旁路。

**类比的局限：**管道物理上可传数据不等于两端消息正确，stdout 混入调试文本会破坏协议解析。

## 3. 技术原理与核心内容

stdio Server 持续读取 stdin 的完整单行 JSON-RPC 消息，并向 stdout 写回相同规范格式的响应。换行是帧分隔符，消息内部不可包含原始换行（字符串中应 JSON 转义）。Client 用 request id 匹配响应；日志、调试和警告必须写 stderr，不能混进 stdout。modern 2026 的所有请求内包含 `_meta`，不需要 legacy initialize；取消通知、进程退出和重启需遵守对应绑定规定。

## 4. 工程实践与设计权衡

**工程案例：**IDE 从可信安装包启动本地代码索引 MCP Server，把 `resources/read` 请求写入 stdin，解析 stdout 中单行结果；Server 用 stderr 输出扫描进度日志。执行 shell 工具前要限制工作目录、环境变量与命令参数，不能因为 stdio 在本机就跳过授权。

**失败模式与验证：**stdout 打印 DEBUG 破坏消息 framing、协议 JSON 含真实多行、子进程继承过度环境凭证、意外进程退出造成工具响应未知。用日志污染、崩溃、请求乱序、未授权文件访问与重启恢复测试。

## 5. 关联知识与易混辨析

stdio 是 MCP 标准传输之一；Streamable HTTP 使用单一 HTTP endpoint 与请求范围响应流；JSON-RPC 是承载的消息格式；Client/Server 分别是协议角色而非固定网络主机。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 MCP stdio Server 不能把调试 print 写入 stdout？** 答：stdout 只能发送 MCP 协议消息，额外文本会破坏单行 JSON-RPC framing，应改用 stderr。
2. **问：使用 stdio 是否说明工具调用可以安全访问宿主所有文件？** 答：不能，子进程可能有宿主权限，仍须最小化权限、限制根目录与资源级授权。

## 7. 中等难度考试题（含解析）

1. **题：Client 写入 10 条合法 JSON-RPC 请求，每条占一行，Server 返回 10 条结果，在无额外通知的题设下 stdout 应有多少条结果帧？** 解：10 条，逐条以换行分隔，日志不计入 stdout 协议帧。
2. **题：某 Server 将业务日志 `INFO started` 写到 stdout，客户端按 JSON 解析，最可能出什么问题？** 解：解析失败或消息流失步；应把日志写 stderr 并对协议帧做验证。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)：子进程 stdin/stdout、换行 framing 与 stderr 日志。
- [MCP · Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)：stdio 和 Streamable HTTP 绑定对比。
