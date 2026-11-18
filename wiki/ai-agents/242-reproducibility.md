# Reproducibility（可复现性）

> AI Agents · 专题：评测体系与常见基准 · 依据独立证据、实际任务状态与明确的评价边界

## 1. 核心定义

**Reproducibility（可复现性）**：Reproducibility（可复现性）是研究者在明确模型版本、输入、工具、环境、随机性和评分过程的条件下，能够再次得到相近评测观察或相同确定性结果的程度。Agent 由于涉及外部工具和多阶段状态，复现要求往往高于单轮问答。

**适用边界：**设定 temperature=0 并不足以保证严格逐 token 相同：服务端版本、并行调度、搜索索引、GPU 数值计算和远端 API 状态可能变化。可复现应明示是 deterministic replay 还是多次运行的统计分布一致。

## 2. 形象理解

像化学实验必须记录温度、材料批次、操作顺序和仪器版本，重复实验的条件才有可比较性。

**类比的局限：**再准确的实验步骤也不保证有随机噪声的结果完全一致，合理评价需要给出波动范围。

## 3. 技术原理与核心内容

保存 run_manifest={model_id,revision,prompt_sha,tool_schema_sha,repo_sha,dataset_version,seed,temperature,environment_image,grader_version,run_time}，并保留真实 task/trace。对单元测试使用 ScriptedModel 和固定 fixture；对端到端在线工具测评可快照环境、提供可重复 mock 和明确不可控因素。相同配置重复 n 次报告成功率均值、标准差与置信区间，避免只报告最好一次。

## 4. 工程实践与设计权衡

**工程案例：**代码修复 Agent 对同一 commit 运行三次，分别通过 42、44、40 道（共 50）；审稿记录每次结果、运行容器 SHA、依赖锁文件及 grader，确认实验波动，而不是只报告 44/50。

**失败模式与验证：**没有记录外部搜索时间、测试数据被改写、环境版本漂移、选择最优运行的幸存者偏差、随机 seed 重复却错误宣称完全确定。通过跨机器复跑、缓存失效和 oracle 版本锁定测试。

## 5. 关联知识与易混辨析

Reproducibility 强调结果可以再现；Replicability 可指不同团队/方法重复验证；Determinism 是同条件单次结果严格一致；Benchmark 是组织这种实验的规范。

## 6. 中等难度面试题（含参考答案）

1. **问：固定 seed 为什么不能单独保证 Agent 复现？** 答：网络、模型服务、工具数据、并行顺序和评分器都可能变化，必须记录并控制更多变量。
2. **问：如何公平比较两个 Agent 的表现？** 答：共享任务、环境、工具预算与 grader，运行多次并报告差异及不确定性，不能只选最好的一次。

## 7. 中等难度考试题（含解析）

1. **题：三轮同一 50 题分别通过 42、44、40，平均成功数及平均成功率？** 解：(42+44+40)/3=42 题，42/50=84%。
2. **题：模型版本固定但评测器版本变更，能认为两个分数完全可直接比较吗？** 解：不能，应重评分或说明 grader 变更的影响。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)：脚本化模型、隔离工具与可重复性。
- [LangSmith · Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)：数据集、实验、重复运行与比较。
