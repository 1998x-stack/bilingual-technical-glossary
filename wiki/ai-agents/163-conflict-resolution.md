# Conflict Resolution（冲突解决）

> AI Agents · 专题：多智能体协作 · 多 Agent 通信、一致性与独立业务验收

## 1. 核心定义

**Conflict Resolution（冲突解决）**：Conflict Resolution（冲突解决）是面对多个 Agent、文档或系统对同一任务给出矛盾结论、状态或写入时，依据来源、版本、权限与业务规则消除或显式保留冲突的处理过程。冲突不必然通过选一方结束，也可能触发重新验证或人工升级。

**适用边界：**内容冲突与并发写入冲突属于不同层次：前者比较事实证据，后者可能需 CAS、锁或事务。不能只按‘最新返回’或‘措辞更有信心’选择赢家。

## 2. 形象理解

像两份不同日期的地图对道路开放情况给出相反说明，需要查当前官方封路公告，而非随意采用其中一份。

**类比的局限：**较新的文件也可能是草稿；来源权威与生效日期必须一起判断。

## 3. 技术原理与核心内容

分类冲突类型 semantic_disagreement、schema_mismatch、version_conflict、write_race。对事实核对 provenance、valid_at、confidence_scope；对共享状态采用 expected_version、compare-and-swap 或串行化更新；对不可判定事实返回 conflict/unknown。冲突解决记录 decision_reason、candidate_sources、chosen_version 与 reviewer，而不覆盖原始矛盾证据。

## 4. 工程实践与设计权衡

**工程案例：**两个 Agent 分别称某服务部署为 v2 和 v3。协调器查询部署平台的实际 image digest、区域和更新时间，发现一个引用测试环境、另一个引用生产环境；保留作用域后冲突自然分解，不能统一写成 v3。

**失败模式与验证：**旧资料覆盖新版本、两 Agent 并发写订单状态导致最后写入赢、强行平均互斥结论、冲突被摘要隐藏。以对抗性来源、时间/环境错配、CAS 失败及未确认分支进行测试。

## 5. 关联知识与易混辨析

Conflict Resolution 是处理不一致的方法；Consensus 在可用证据和规则下形成共同意见；Reviewer Agent 检查个别产物；Coordinator Agent 负责调度冲突处理。

## 6. 中等难度面试题（含参考答案）

1. **问：两个 Agent 对生产版本有冲突，优先看哪个？** 答：不应按角色决定；从当前生产发布系统读取可验证部署 ID、环境/区域和版本，再比较两份断言的适用范围。
2. **问：为什么对相互冲突的数值答案取平均可能危险？** 答：数值可能指不同币种、日期或对象，平均会制造不存在的业务事实；必须先对齐语义、单位与来源。

## 7. 中等难度考试题（含解析）

1. **题：A 更新共享记录 version=9→10 已成功，B 仍用 expected_version=9 写入，应发生什么？** 解：CAS 冲突，B 需重读并重新解决冲突。
2. **题：两个 Agent 分别返回 200 USD 和 200 CNY，可以直接当相同的 200 元吗？** 解：不能，货币单位不同，必须明确汇率与适用日期。

## 8. 权威来源与延伸阅读

- [W3C · PROV-O](https://www.w3.org/TR/prov-o/)：实体、活动、责任与溯源记录。
- [AutoGen · Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)：多 Agent 通信和协作架构。
