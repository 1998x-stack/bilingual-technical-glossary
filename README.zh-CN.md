# TERM/ATLAS｜中英双语专业术语库

> 覆盖数学基础、深度学习、大语言模型、智能体与 AI 基础设施的结构化中英文技术术语知识库。

[打开术语检索站点](https://1998x-stack.github.io/bilingual-technical-glossary/) · [English README](README.md) · [参与贡献](CONTRIBUTING.md)

## 项目定位

本仓库不只是“英文词—中文词”的平面表格，而是可持续维护的**技术术语知识基础设施**：同一份结构化数据可以发布为专题 Markdown、供程序使用的 JSON/CSV、可打印的 PDF，以及可视化检索网站。

## 术语领域

| 领域 | 结构化词条 | 专题 | Markdown | PDF |
|---|---:|---:|---|---|
| AI 基础设施 / AI Infrastructure / AI Infra | 142 | 8 | [阅读](glossaries/ai-infrastructure.md) | [下载](pdf/ai-infrastructure.pdf) |
| GPU Kernel / GPU 核函数 / GPU Kernel Engineering | 255 | 13 | [阅读](glossaries/gpu-kernel.md) | [下载](pdf/gpu-kernel.pdf) |
| AI 智能体 / AI Agents | 332 | 16 | [阅读](glossaries/ai-agents.md) | [下载](pdf/ai-agents.pdf) |
| 大语言模型 LLM / Large Language Models | 419 | 16 | [阅读](glossaries/large-language-models.md) | [下载](pdf/large-language-models.pdf) |
| 深度学习 / Deep Learning | 500 | 18 | [阅读](glossaries/deep-learning.md) | [下载](pdf/deep-learning.pdf) |
| 机器学习 / Machine Learning | 447 | 19 | [阅读](glossaries/machine-learning.md) | [下载](pdf/machine-learning.pdf) |
| 强化学习 / Reinforcement Learning | 305 | 14 | [阅读](glossaries/reinforcement-learning.md) | [下载](pdf/reinforcement-learning.pdf) |
| 微积分 / Calculus | 361 | 16 | [阅读](glossaries/calculus.md) | [下载](pdf/calculus.pdf) |
| 线性代数 / Linear Algebra | 289 | 12 | [阅读](glossaries/linear-algebra.md) | [下载](pdf/linear-algebra.pdf) |
| 编译原理 / Compiler Principles | 268 | 12 | [阅读](glossaries/compiler-principles.md) | [下载](pdf/compiler-principles.pdf) |
| 概率论 / Probability Theory | 405 | 16 | [阅读](glossaries/probability-theory.md) | [下载](pdf/probability-theory.pdf) |
| Apache Kafka / 事件流平台 | 283 | 16 | [阅读](glossaries/apache-kafka.md) | [下载](pdf/apache-kafka.pdf) |
| 数据结构 / Data Structures | 352 | 14 | [阅读](glossaries/data-structures.md) | [下载](pdf/data-structures.pdf) |
| **合计** | **4,358** | **190** | | |

### 新增独立手册（暂未纳入全文检索）

| 领域 | 词条数 | 章节 | Markdown | PDF |
|---|---:|---:|---|---|
| 计算机组成原理 / Computer Organization & Architecture | 678 | 15 | [阅读](glossaries/computer-organization.md) | [下载](pdf/computer-organization.pdf) |
| 并行计算 / Parallel Computing | 205 | 12 | [阅读](glossaries/parallel-computing.md) | [下载](pdf/parallel-computing.pdf) |

> **检索状态：**手册包含 678 条中英文术语、16 组易混概念辨析和缩写速查，保留原始 39 页 PDF。为避免引入未经核验的释义，这些术语**尚未加入**网站全文检索，也不计入上方结构化数据统计。

**并行计算专题：**以 Grama 等人的《Introduction to Parallel Computing》（第二版）作为知识结构参考，独立整理 205 条术语，覆盖 12 个主题。原版 Markdown 与 PDF 已发布，**暂未纳入网站搜索索引**。

**Kafka 专题新增：**283 条术语、16 个章节，Markdown 原稿和可检索 PDF 均已收录，且同步到网页、JSON 与 CSV 索引。

**数据说明：**此前制作的六本 PDF 均保留原始完整版本，共自述含 2,298 条术语；从版式 PDF 提取的可检索记录有 2,250 条，尚有 48 条因跨行排版未能自动恢复。原始 PDF 才是这些书册完整词条的权威副本。新增的 AI Infra 独立整理了 142 条术语，GPU Kernel 原创手册包含 255 条术语（13 章），现已同步纳入可检索索引；编译原理专题补充 268 条术语（12 章），涵盖词法、语法、SSA、优化与代码生成。网页中所有“词条数”均指真实可搜索索引条目，不将 PDF 封面数字直接冒充完整的数据导入数量。 机器学习新增 447 条原创术语、19 个专题，已同步纳入 Markdown、PDF 和搜索索引。

## GitHub Pages 展示

主题为专业技术知识库、研究数据门户的 UI，支持：

- **中英混合全文搜索：**英文、中文、缩写、专题和解释；
- **主题选择：**13 个学科、190 个专题；
- **覆盖可视化：**按学科展示真实术语数量及学习路线；
- **资料下载：**每个主题的 PDF、Markdown，以及搜索结果 CSV；
- **交互体验：**移动端布局、明暗主题、键盘快捷键、分享检索链接。

静态资源位于 `docs/`，无需后端、数据库或付费 API。仓库首次发布后，需要仓库管理员在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。无需生成新的工作流，现有 `.github/workflows/pages.yml` 已配置部署 `docs/`；随后在 **Actions → Publish TERM/ATLAS to GitHub Pages** 中重新运行之前失败的任务（或点击 Run workflow）。网页成功部署后，上方链接才会正常访问。详见 [部署说明](docs/PAGES_SETUP.md)。

微积分新增 361 条术语（16 个专题），并保留 `notation` 字段；源 Markdown 存放在 [`sources/calculus.md`](sources/calculus.md)。

## 更新与质量控制

编译原理词条请编辑 `data/compiler-principles.tsv` 并运行构建脚本；其余词条可按项目约定编辑 `data/terms.json`，字段包含 `category`、`chapter`、`topic`、`en`、`zh`、`abbr`、`definition`，然后执行：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/verify.py
python3 -m unittest discover -s tests -v
```

**注意：**现有六本 PDF 是独立排版的原件，不会因为修改 JSON 自动覆盖。若修改术语含义，需要同步检查原版 PDF 的版本一致性。详情参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [AGENTS.md](AGENTS.md)。

本项目用于研究、学习和工程阅读；不是任何标准组织发布的官方术语规范。仓库尚未选择开放许可，直到明确发布 License 之前请保留作者权利。