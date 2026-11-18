# Tool Registry（工具注册表）

> AI Agents · 专题：工具使用与环境交互 · 具体工具行为、权限与版本以官方规范为准

## 1. 核心定义

**Tool Registry（工具注册表）**：Tool Registry（工具注册表）是集中存储和查询工具名称、版本、描述、schema、路由信息、能力范围等受管理元数据的目录。它帮助 Agent 工具生态避免重名冲突、过期接口和随意拼接执行地址。

**适用边界：**注册表是发现与路由的元信息源，不替代服务端 AuthZ、业务审批和运行时健康检查。注册表可以是静态配置或动态服务目录，并非某一种协议固定要求。

## 2. 形象理解

像企业通讯录与岗位权限清单：记录谁负责何种事务、如何联系，但通讯录记录本身不是通行证。

**类比的局限：**登记了某项能力不代表用户有资格使用，也不确保目标服务当下健康。

## 3. 技术原理与核心内容

常见记录可由 tool_id、namespace、version、description、input_schema、endpoint_ref、auth_scopes、risk_level、owner 组成。发现器从注册表查询候选，路由器解析受信任 endpoint_ref，执行器最终做身份校验。热更新和版本弃用需要一致的缓存失效、审计和兼容性窗口。

## 4. 工程实践与设计权衡

**工程案例：**公司注册 sales.get_order v2 和 finance.get_order v1，同名短名称必须加命名空间避免错路由；停用财务工具时撤销注册与访问凭证并刷新发现缓存。

**失败模式与验证：**注册表遭污染会将 Tool Call 路由到攻击者服务；旧 schema 与新后端不兼容会导致大量失败。需要严格发布审批、版本管理、签名/来源检验与访问最小化。

## 5. 关联知识与易混辨析

Tool Registry 是工具定义与路由的持久目录；Discovery 是查询可用工具的过程；Tool Adapter 是将异构服务接口转换为统一调用契约的实现层。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么工具注册表需要工具版本与命名空间？** 答：避免不同团队同名工具冲突，支持旧调用兼容、灰度变更和可追溯的参数/语义升级。
2. **问：如何防止攻击者注册一个伪装成 payroll.read 的工具？** 答：注册与发布过程需认证审批，工具端点受可信配置限制，调用时校验服务身份和权限。

## 7. 中等难度考试题（含解析）

1. **题：某租户有 18 个已注册工具，其中 5 个停用、4 个对该租户无权限（且集合不重叠），最多可发现几个？** 解：18−5−4=9 个。实际发现还受健康和配置过滤影响。
2. **题：同名工具 v1 参数 orderId，v2 参数 order_id。未加版本识别的主要风险？** 解：客户端与服务器 schema 不一致导致调用失败或语义误用；须版本化并做兼容/迁移测试。

## 8. 权威来源与延伸阅读

- [MCP · Tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)：tools/list、tools/call 与工具结构。
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：工具调用、工作流与失败模式。
