# Persistence（持久化）

> AI Agents · 专题：执行状态、持久化与恢复 · 以真实运行状态、外部副作用对账和授权范围为工程边界

## 1. 核心定义

**Persistence（持久化）**：Persistence（持久化）是把 Agent 的运行状态、长期事实或审计记录保存在进程生命周期之外，使重启、切换节点或不同请求能够继续读取的能力。它是支持恢复的基础设施，但不能单靠保存一段对话文本就保证持久执行正确。

**适用边界：**持久化的‘保存’与‘长期记忆’并不等同；有些数据按 thread_id 管理短期上下文，另一些需按 tenant/user 的 Store namespace 访问。数据库副作用与 Agent 存储之间通常没有一个统一的 ACID 事务。

## 2. 形象理解

像医院既保存此次问诊的流程记录，也单独保存跨次复诊的合法病历资料；两种存储范围与访问权限不同。

**类比的局限：**档案存在不代表内容永远正确；已撤权人员不能因为旧缓存仍有数据就继续读取。

## 3. 技术原理与核心内容

区分 checkpointer（图状态 snapshots）和 store（跨线程 KV/语义记忆）。设计主键 `(tenant_id, thread_id, version)`、保留时间 TTL、加密、用户删除与审计字段；重要写入使用事务提交、唯一约束与乐观锁，确保不会由重复请求创建相同记录。读取时验证当前 ACL 和 schema 版本，密钥轮换与备份恢复也应纳入演练。LangGraph InMemorySaver 适合样例，不等同生产级持久化后端。

## 4. 工程实践与设计权衡

**工程案例：**客服 Agent 在数据库持久保存工单进度，在合法的 tenant namespace 保存经用户确认的语言偏好；切换机器后从稳定 thread_id 恢复待办，但不能把某客户数据错误载入另一客户的会话。

**失败模式与验证：**依赖内存缓存导致宕机丢失、跨用户命名空间冲突、备份含未脱敏隐私、schema 升级导致旧记录不可解析。通过重启、备份恢复、权限撤销与版本迁移测试验收。

## 5. 关联知识与易混辨析

Persistence 是数据存活能力；Checkpointing 专门保存可恢复执行状态；Memory 是数据用于后续推理的语义；Durable Execution 是容错的行为保证。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么生产持久化不能只用 InMemorySaver？** 答：内存存储随进程消失且难支持多实例一致性，生产需要可靠数据库及权限和恢复机制。
2. **问：能否把所有 Agent 记忆都放同一个 thread_id？** 答：不应；跨用户和跨任务信息需要租户隔离、用途限定及恰当 Store namespace。

## 7. 中等难度考试题（含解析）

1. **题：某服务单实例内存每次重启清零，连续重启两次后还能凭内存恢复第一个会话吗？** 解：不能，除非快照已写入外部稳定存储。
2. **题：10 条记录中 3 条已过 TTL、2 条已撤权，假设集合不重叠，当前最多可用多少条？** 解：10−3−2=5 条，仍须满足其他访问规则。

## 8. 权威来源与延伸阅读

- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：thread-scoped checkpoint 与跨线程 store 区别。
- [LangGraph · Checkpointer vs Store](https://docs.langchain.com/oss/python/langgraph/persistence#checkpointer-vs-store)：短期状态快照与长期数据存储。
