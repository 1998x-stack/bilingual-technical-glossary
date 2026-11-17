# Security Boundary（安全边界）

> AI Agents · 专题：安全防护与治理 · 防止不可信内容跨越执行授权与信任边界

## 1. 核心定义

**Security Boundary（安全边界）**：Security Boundary（安全边界）是系统中强制隔离不同主体、进程、资源或权限域的界限，如容器/虚拟机边界、网络分区、API 授权点及生产与测试环境之间的控制界面。对 Agent 而言，低信任模型输出跨越这些界限必须经过可信检查。

**适用边界：**安全边界需要依赖真实操作系统、网络和服务端权限实现，不能凭‘把工具写在不同文件里’或‘使用不同 system prompt’就形成隔离。业务对象 ACL 和物理/进程隔离是相互补充的控制。

## 2. 形象理解

像实验室之间的隔离门和空气过滤系统，安全不来自墙上‘禁止进入’的告示，而来自可验证的门禁和物理阻断。

**类比的局限：**隔离门如果有共享通风管道或备用钥匙漏洞，仍可能被绕过，需要端到端建模。

## 3. 技术原理与核心内容

明确 boundary_map: `user/browser → Host → MCP Client → tool server → tenant resources`。在每条边界落实身份验证、最小权限、输入验证、内容标记与输出脱敏；对执行代码加入 seccomp/namespace/eBPF 网络限制和只读挂载。低信任检索文本不能修改工具调用权限、审批条件或代码执行的实际安全策略。采用 threat modeling 识别跨边界的数据流、secret 和 capability reuse，逐一设计防护和测试证据。

## 4. 工程实践与设计权衡

**工程案例：**一个 Agent 允许访问公共网页并总结代码片段，但浏览器渲染器在沙箱中运行、不挂载宿主密钥；访问私有 GitHub 仓库的服务端独立验证 token 和 repo ACL，网页上出现‘合并 main’也无法直接触发 Git 写入。

**失败模式与验证：**宿主 Docker socket 被挂入沙箱、不同租户共享可写缓存、把检索文本直接解释为工具参数、权限检查只在 UI。测试越界文件访问、内网 SSRF、跨租户查询和低信任输入尝试。

## 5. 关联知识与易混辨析

Security Boundary 是强制权限与隔离边界；Trust Boundary 描述信任级别变化的位置；Guardrail 是检查机制；Sandbox 是其中一类执行环境边界。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不同 prompt role 不构成真正的系统安全边界？** 答：模型可能受注入或错误推理影响，真实授权与隔离必须在不受模型控制的后端实现。
2. **问：如何识别 MCP Tool 的真实安全边界？** 答：从 Host、Client、Server 到资源系统逐层审视 token、身份、网络隔离及对象 ACL，而不只看工具描述。

## 7. 中等难度考试题（含解析）

1. **题：系统经过 Host、Tool Server、DB 三个安全域，至少需要对哪些跨域调用进行可信验证？** 解：每个实际跨域调用都需按对应身份/权限策略校验，而非只在第一层认证。
2. **题：沙箱只读挂载代码，但允许带 admin token 调数据库，能认为系统已最小权限吗？** 解：不能，网络/API 权限仍可造成严重副作用。

## 8. 权威来源与延伸阅读

- [NIST SP 800-207 · Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)：不可隐式信任、连续访问判断。
- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：默认拒绝和执行端对象级授权。
