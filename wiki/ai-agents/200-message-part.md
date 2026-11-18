# Message Part（消息片段）

> AI Agents · 专题：A2A：智能体间协议 · 按 A2A 正式规范定义，不将旧版示例当作唯一序列化方式

## 1. 核心定义

**Message Part（消息片段）**：Message Part（消息片段）是 A2A Message 或 Artifact 中最小的内容承载单元，可表示文本、文件字节/URL 或结构化 JSON 数据。当前正式规范通过字段本身辨别内容类型，不应不加版本判断地复用旧版 `kind:text/file/data` 封装方式。

**适用边界：**当前 `Part` **必须恰有一项** `text`、`raw`、`url` 或 `data`，其它如 filename、mediaType、metadata 属辅助元数据。不能把 URL 当安全文件位置，也不能假设 raw 的 Base64 字节无大小限制。

## 2. 形象理解

像一个多媒体邮件中的每个附件或正文段落，各段的文件类型和实际数据需要单独标注。

**类比的局限：**文件名写着 invoice.pdf 不能证明内容是 PDF；不可信链接也可能指向内网地址。

## 3. 技术原理与核心内容

协议 OneOf 可以表示 `{"text":"hello"}` 或 `{"data":{"total":5},"mediaType":"application/json"}`，文件二选一使用 raw 字节或 url 载荷，必要时指定 filename 和 mediaType。Client 按实际内容和 MIME sniffing 验证，限制 Base64 解码大小，拒绝危险 URL 的 SSRF 和信息泄露。对组合消息使用 parts[] 次序承载多模态，但每个 Part 自身只选择一种内容分支。

## 4. 工程实践与设计权衡

**工程案例：**报表 Agent 返回三个 Part：一句说明文本、结构化 JSON 统计、PDF 文件 URL。Client 验证统计项币种、文件来源和 hash，未经授权不去抓任意文件；UI 下载前检查文件大小和媒体类型。

**失败模式与验证：**同一 Part 同时包含 text 和 url、旧版 `kind` 解析失败、URL 私有地址导致 SSRF、Base64 巨大内容内存耗尽、媒体类型与实际字节不符。以 OneOf、无效链接、文件大小上限及跨租户资源测试。

## 5. 关联知识与易混辨析

Part 是消息/产物的片段；Message 是交互回合；Artifact 是完整任务交付对象；MCP Content Block 是另一协议的结构，不能凭字段近似直接互换。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Part 中 text 与 raw 不能同时设置？** 答：A2A 当前 Part 使用 OneOf，要求恰有一个承载分支，避免数据类型歧义。
2. **问：文件 Part 的 URL 能否直接交给任意下载器？** 答：不能，必须做目标来源、授权、SSRF、防重定向和文件完整性校验。

## 7. 中等难度考试题（含解析）

1. **题：一个 Artifact 中含 2 个 text Part、1 个 data Part，共多少？** 解：3 个 Part；各自满足 OneOf。
2. **题：Part 有 text 和 data 两个承载字段且其它合法，能通过规范校验吗？** 解：不能，违反恰有一项的约束。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Task、Message、Part 的规范结构。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：卡片、消息、产物与工作单元。
