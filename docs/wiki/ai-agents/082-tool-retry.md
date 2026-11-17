# Tool Retry（工具调用重试）

> AI Agents · 专题：工具使用与环境交互 · 适用范围：通用工程概念；具体服务协议以官方文档和版本为准

## 1. 核心定义

**Tool Retry（工具调用重试）**：Tool Retry（工具调用重试）是对符合可重试条件的失败或不确定调用，在受控预算下重新发出请求的恢复机制。它需要同时考虑**瞬时故障可恢复性、业务幂等性、重试次数、超时与系统负载**，不能把所有错误都交给重试。

**适用边界：**只读操作通常较易重试；写操作若无后端幂等保证，应先核对上次执行结果。4xx 往往不能原样重试，429/某些 5xx/连接中断是否重试需依据 API 契约和限流提示。

## 2. 形象理解

像电话占线时隔一会再拨，而不是一分钟内不停连拨；转账指令则必须确认前一次是否成功。

**类比的局限：**拨电话没有转账副作用；对金额转移等操作，一次“无响应”可能已经执行。

## 3. 技术原理与核心内容

工程上设置 max_attempts、per_attempt_timeout、overall_deadline 与 retryable(error)。使用指数退避并加入 jitter，例如第 k 次基础延迟 min(cap,base·2^k)，再从允许范围抽样抖动；若收到 Retry-After 且 API 允许，应遵守。重试分层避免每层放大流量，例如三个层次各重试 3 次可能最多触发 3^3=27 次底层请求。

## 4. 工程实践与设计权衡

**工程案例：**航班查询 Agent 遇到 503 可有限重试；机票支付接口遭遇断连时先查 payment_id/幂等键，再决定是否重试。记录每次 attempt 的成本、延迟、状态和最终终止原因。

**失败模式与验证：**重试风暴放大故障、重复创建订单、所有客户端同步重试形成尖峰、重试耗尽仍报告成功。评测要覆盖持续 503、429、半成功写入和 deadline 被突破。

## 5. 关联知识与易混辨析

Tool Retry 是故障后的再次请求策略；Idempotent Operation 是允许重复而无额外预期效果的操作语义；Backoff 是等待时间控制；Replanning 是后续步骤结构的改变。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么指数退避还需要 jitter？** 答：同一时刻发生故障的客户端若采用相同确定性退避，会在相同时间重试形成集体冲击；jitter 将请求分散。
2. **问：写操作超时后如何判断能否重试？** 答：先查权威状态，若服务提供幂等键则以同键同参数重试；否则不可直接重复非幂等动作。

## 7. 中等难度考试题（含解析）

1. **题：base=0.5 秒、倍增且 cap=4 秒，不含 jitter，k=0、1、2、3 的延迟分别为多少？** 解：min(4,0.5·2^k)：0.5、1、2、4 秒；总等待 7.5 秒。
2. **题：一个系统的三层服务各最多尝试 3 次，最坏情况下同一顶层请求可能触发多少底层调用？** 解：3×3×3=27 次，因此应集中重试责任与整体预算，避免级联放大。

## 8. 权威来源与延伸阅读

- [AWS Builders' Library · Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)：重试放大、退避抖动及超时设计。
- [AWS Builders' Library · Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)：幂等键、同键同参和执行去重。
