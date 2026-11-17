# Roots（根目录）

> AI Agents · 专题：MCP：模型上下文协议 · 以 2026-07-28 规范为当前基准，区分 legacy 模式

## 1. 核心定义

**Roots（根目录）**：Roots（根目录）是旧版 MCP 中 Client 给 Server 列出相关文件系统工作范围的功能，传统方法 `roots/list`。该功能从 2026-07-28 起标记 deprecated，仍为兼容保留，但新实现优先使用明确的工具参数、资源 URI 或服务配置。

**适用边界：**Roots 只是一种工作范围提示，不是进程级沙箱、强制访问控制或自动的租户隔离；Client 告知某目录并不能改变 Server 本身持有的操作系统权限。

## 2. 形象理解

项目经理告诉工具承包商‘工作范围是仓库 A’，但这不是把仓库 B 的门锁起来。

**类比的局限：**如果进程有全盘权限，单靠协议里写 root 无法防止它读错路径。

## 3. 技术原理与核心内容

兼容旧版 Client 可以给出 root URI/name 列表及变更通知；现代优选将 `workspace_uri`/repo_id 写入工具参数，由 Server 用规范化路径、真实资源 ACL 与操作系统沙箱验证。解析符号链接、`..`、路径大小写和 URL 编码后必须确认目标仍在允许工作区。有限 MRTR 可请求相关工作路径信息，但仍不提升权限。

## 4. 工程实践与设计权衡

**工程案例：**代码审查 MCP Server 被限定 `/workspace/proj-a`，但用户参数传入 `../proj-b/secrets`。Server 对目标路径规范化并检查根目录及 tenant 后拒绝；最好只接受 repo_id 与相对文件路径。

**失败模式与验证：**把 roots 当真正授权、目录符号链接逃逸、缓存旧 workspaces、跨租户拼接路径、未做资源版本检查。使用 symlink、Unicode 路径、路径遍历和权限撤销负例测试。

## 5. 关联知识与易混辨析

Roots 是弃用中的 Client 范围提示；MCP Resource 提供 Server 可读内容；文件系统沙箱与 Server-side authorization 才实际限制访问。

## 6. 中等难度面试题（含参考答案）

1. **问：2026 版如何替代 roots/list ？** 答：以显式工具参数、资源 URI 或受控 Server 配置承载目录范围。
2. **问：Roots 为什么不等于沙箱？** 答：它不会限制 Server 进程真实 OS 权限，需要另外实施路径/ACL 检查。

## 7. 中等难度考试题（含解析）

1. **题：允许 `/a/project`，请求 `/a/project/../secret`，是否在允许范围？** 解：规范化后到 `/a/secret`，不在原根目录，应拒绝。
2. **题：列出两个 root 但用户只获授权第一个，可访问第二个吗？** 解：不能，列表不是授权。

## 8. 权威来源与延伸阅读

- [MCP · Roots](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)：旧版工作目录共享。
- [MCP SDK · Deprecated features](https://py.sdk.modelcontextprotocol.io/deprecated/)：新版迁移建议。
