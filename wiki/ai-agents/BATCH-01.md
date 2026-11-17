# AI Agents 第 1 批 · 系统化学习路径（内部）

> 编辑研究路线与综合题，仅用于编审和教研；不在公开 Explorer 渲染任何 Batch 导航。

## 依赖关系

`Goal → Task → Subtask` 明确**做什么**；`LLM + Instruction + Tool + Agent Runtime` 提供**怎么决定和执行**；`Agent Loop → Observation → 下一步 Action` 负责**反馈闭环**；`Role / Capability / Autonomy / Agency` 定义**职责、可做范围和自由度**；`Environment` 是行动生效的外部世界。

## 可复现实例：采购助理

1. 把“购买符合条件的设备”写成 Goal（预算、数量、截止日期、成功判据）。
2. 拆成 Task：查询库存、核对规格、比较报价、生成审批提案；多个独立查询可并行。
3. Runtime 只给查询工具只读权限；超过额度的“提交采购单”必须先获得审批。
4. Tool Result 作为 Observation，校验时间戳、货币、商品 ID；过时价格必须重新核查。
5. 终止条件包括采购被确认、审批拒绝、接口故障、超过 token/时间预算；不能只凭模型说“已下单”判断成功。

## 综合面试案例

**问题：**运行器重启后 Agent 把同一采购单提交了两次，怎样设计修复？  
**参考答案：**设计业务幂等键与状态查询，在副作用调用前记录意图，恢复后核验已提交状态再决定是否重试。区分模型决策轨迹与实际外部事务，添加 trace_id 和失败注入测试；提示“不要重复提交”不是充分保护。

## 综合考试案例

**题目：**题设三个独立查询各需 2、3、4 s，审批固定需 5 s；审批必须等待所有查询。假设无限并行资源且忽略调度延迟，总时间下界与全部串行时间分别是多少？  
**解：**并行下界 `max(2,3,4)+5=9 s`；串行为 `2+3+4+5=14 s`。减少 5 s，但必须满足无写入冲突与独立性前提。

## 延伸阅读

- [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI：A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
