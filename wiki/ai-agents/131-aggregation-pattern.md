# Aggregation Pattern（汇总模式）

> AI Agents · 专题：工作流与编排模式 · 应用架构、状态恢复与工程权衡

## 1. 核心定义

**Aggregation Pattern（汇总模式）**：Aggregation Pattern（汇总模式）是把来自多个执行分支、模型或工具的部分结果归并为统一结果的处理模式。它既可以做确定性集合运算与统计，也可以用受约束的模型生成综合结论。汇总要处理缺失、冲突、重复和不同来源可靠性。

**适用边界：**汇总不是机械拼接，更不意味着多数模型一致就是真实。对于数值、交易和安全结论，应保留原始证据并使用独立可检查的合并规则。

## 2. 形象理解

像新闻编辑收集多个记者的报道，核对报道对象、时间与出处，再组织最终专题，而不是简单把所有稿件连起来。

**类比的局限：**多个记者可能抄同一条错误消息，一致意见不等于独立证实；错误重复票数不能成为事实。

## 3. 技术原理与核心内容

对于任务集 {t_i}，先收集 `result_i=(task_id,version,status,payload,source)`，再按 aggregation function F 验证类型与去重，处理失败/超时与不完全结果。数值汇总可使用 sum、weighted mean；文本汇总先做 evidence alignment，再根据规则统一。对不同结果质量要保存 provenance、conflict flag 与 coverage，不能把未返回分支算成零贡献。

## 4. 工程实践与设计权衡

**工程案例：**安全扫描 Agent 并行得到依赖漏洞、密钥检测和静态分析报告，汇总者按统一 severity schema 合并，重复同一 CVE 去重但保留各扫描器来源。对某个扫描器超时应报告检查未覆盖，而非得出‘无漏洞’。

**失败模式与验证：**结果乱序配错 task_id、重复计数、汇总器用语言模型改写数值、把缺失当成功。用已知重叠/冲突样本、类型错误与失败分支模拟测试准确性。

## 5. 关联知识与易混辨析

Aggregation Pattern 关注结果合并算法；Fan-in 是汇合拓扑；Parallelization 是并发调度；Voting 是一种汇总方法，但不必然提供真实事实保证。

## 6. 中等难度面试题（含参考答案）

1. **问：两个扫描器都报同一 CVE，如何避免重复计数又保留证据？** 答：按漏洞 ID、资产和版本去重，并保存多源 scan_id、时间和证据；不可直接把重复项删除到无来源。
2. **问：某一关键分支超时，汇总能否仍报告全部成功？** 答：除非成功谓词允许该分支缺失，否则应标注 partial/failed 和未覆盖范围，不能伪装成完整通过。

## 7. 中等难度考试题（含解析）

1. **题：三个独立工单统计分别为 12、8、5 件，无交集时合计多少？** 解：12+8+5=25 件；若有重叠需要先去重。
2. **题：两个分支结果分别含 6 和 7 个 ID，其中 3 个相同，汇总唯一 ID 数量多少？** 解：6+7−3=10 个。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：编排者—工作者、评估者—优化者和常见工作流模式。
- [LangGraph · Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)：状态、编排与图执行。
