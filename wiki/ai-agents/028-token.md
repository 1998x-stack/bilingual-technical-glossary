# Token（词元）

> AI Agents · 专题：模型能力与推理 · 通用概念；产品特性以文档版本和模型接口为准

## 1. 核心定义

**Token（词元）**：Token（词元）是模型 tokenizer 使用的离散序列单位。一个 token 可能是完整词、词的一部分、标点、空格相关片段或其他编码片段，并不与汉字、英文单词或字节一一对应。

**适用边界：**不同 tokenizer 对同一段文字的 token 数可能不同；图像、音频、工具 schema 等也可能引入额外计数。

## 2. 形象理解

像拼乐高所需的积木块：一句话会拆为不同大小的小块，模型按块处理而非按自然语言单词边界处理。

**类比的局限：**积木块长度不固定，不能把“一个汉字=一个 token”作为普适估算。

## 3. 技术原理与核心内容

Tokenizer 把输入映射为 token ID 序列，然后模型预测条件分布 `P(token_t | token_<t, context)`；decode 将生成的 token ID 组合为文本。请求用量通常区分 input、output、cached 与（部分模型的）reasoning token。真实调用前可使用相应模型的计数 API。

## 4. 工程实践与设计权衡

**工程案例：**优化多语言客服 Agent 预算时，对中英文请求分别统计 token 消耗；工具参数、JSON schema、历史消息的结构性开销也纳入成本估算，不能只数用户可见文字。

**失败模式与验证：**以英语字符/4 估算中文 token、把用户看到的输出字符数当计费 token 数、或忽略模型隐藏推理 token，可能造成预算不足。

## 5. 关联知识与易混辨析

Token 是离散计量单元；Context Window 是可处理 token 容量；Token Budget 是任务对各类 token 的分配策略。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么两个不同模型处理同一篇中文文章可能产生不同 token 数？** 答：分词器的词表和编码不同，中文与混合符号的拆分粒度会变化；应使用目标模型的官方计数器而非固化比例。
2. **问：API 请求 1000 个 input token，输出只显示 50 个单词，为什么 output_tokens 可能明显更大？** 答：token 不等于词数；还可能含不可见推理/格式 token，具体以 usage 对象的定义为准。

## 7. 中等难度考试题（含解析）

1. **题：题设某模型把“hello world”切成 2 个 token，把中文短语切成 5 个 token，两段同时输入共多少 token？** 解：2+5=7 token（忽略消息结构开销）；该数是题设 tokenizer 的结果，不能推广到其他模型。
2. **题：为什么不能以 UTF-8 字节数除以固定常数精确计算模型 token 用量？** 解：Tokenizer 的编码合并规则、词表、语言与格式不同，UTF-8 字节边界也与 token 边界不一致。需用模型的具体 tokenizer。

## 8. 权威来源与延伸阅读

- [OpenAI Help · Understanding tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)：token 定义、缓存与推理 token。
- [OpenAI API · Counting tokens](https://developers.openai.com/api/docs/guides/token-counting)：精确 token 统计与请求组件。
