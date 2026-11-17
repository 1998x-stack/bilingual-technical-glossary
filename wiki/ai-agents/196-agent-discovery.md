# Agent Discovery（智能体发现）

> AI Agents · 专题：A2A：智能体间协议 · 按 A2A 正式规范定义，不将旧版示例当作唯一序列化方式

## 1. 核心定义

**Agent Discovery（智能体发现）**：Agent Discovery（智能体发现）是 A2A Client 查找可协作的远程 Agent、获取 Agent Card 并判断是否匹配任务、协议、能力与安全要求的过程。发现机制包括标准 Well-Known URI、可信 Registry/Catalog 及私有直接配置。

**适用边界：**发现仅说明有候选服务，不意味着它被审计、认证、具有所需数据权限或当前在线。A2A 规范定义 Agent Card 格式，但并未强制统一注册表查询 API，使用第三方 Registry 的查询语义需要额外契约。

## 2. 形象理解

像企业采购先查询合格供应商名录，查看其业务范围和联系方式，再检查资质与实际合同授权。

**类比的局限：**出现在供应商目录里并不表示其任一声明都真实或与当前客户有合作合同。

## 3. 技术原理与核心内容

Client 可向 `https://domain/.well-known/agent-card.json` 获取卡片，也可以向受控 Registry 或私有配置读取。解析 capabilities、skills、supportedInterfaces 后，按 client 支持的 binding 与输入输出媒体类型过滤，最后验证 TLS、发行者、签名/信任域和真实权限。缓存遵循 HTTP Cache-Control/ETag，敏感技能使用经身份验证的 Extended Agent Card，不向匿名用户泄漏内部 Agent。

## 4. 工程实践与设计权衡

**工程案例：**客服总 Agent 寻找会中文退货政策查询的远程 Agent，Registry 返回五个候选。先过滤中文 text/plain、身份凭据与可用性，最后执行最小权限的只读测试，不能把注册表排名第一当授权批准。

**失败模式与验证：**DNS 或卡片伪造、缓存旧版本、技能描述不实、注册表返回内网服务地址、未按租户过滤候选。以过期卡片、假签名、同名 Agent、多版本绑定和敏感字段泄露测验。

## 5. 关联知识与易混辨析

Agent Discovery 是找到 Agent 的过程；Agent Card 是机器可读的能力描述；MCP Tool Listing 发现某服务里的工具；Task Delegation 则是在选择 Agent 之后实际派发工作。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 Well-Known URL 可发现不代表远端可直接信任？** 答：任何站点都可发布文本；要核验域名、凭证、卡片来源、服务资质和权限。
2. **问：A2A 是否规定唯一的企业 Agent Registry API？** 答：没有。它规范 Card 表示，目录索引仍按部署环境选择和另行约定。

## 7. 中等难度考试题（含解析）

1. **题：10 个候选中 4 个支持所需协议、其中 2 个还满足授权，最终可以优先进入验证的有几个？** 解：2 个，仍要进一步检查真实可用性。
2. **题：ETag 显示内容没变时，能否不检查用户权限就执行工具？** 解：不能，卡片缓存与业务授权是不同层次。

## 8. 权威来源与延伸阅读

- [A2A · Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)：Well-known、注册表与私有配置。
- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Task、Message、Part 的规范结构。
