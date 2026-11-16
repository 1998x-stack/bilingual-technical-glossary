# TERM/ATLAS｜中英双语专业术语库

> 覆盖数学基础、深度学习、大语言模型、智能体与 AI 基础设施的结构化中英文技术术语知识库。

[打开术语检索站点](https://1998x-stack.github.io/bilingual-technical-glossary/) · [English README](README.md) · [参与贡献](CONTRIBUTING.md)

## 项目定位

本仓库不只是“英文词—中文词”的平面表格，而是可持续维护的**技术术语知识基础设施**：同一份结构化数据可以发布为专题 Markdown、供程序使用的 JSON/CSV、可打印的 PDF，以及可视化检索网站。

## 术语领域

| 领域 | 结构化词条 | 专题 | Markdown | PDF |
|---|---:|---:|---|---|
| AI 基础设施 / AI Infrastructure | 142 | 8 | [阅读](glossaries/ai-infrastructure.md) | [下载](pdf/ai-infrastructure.pdf) |
| AI 智能体 / AI Agents | 332 | 16 | [阅读](glossaries/ai-agents.md) | [下载](pdf/ai-agents.pdf) |
| 大语言模型 / LLM | 419 | 16 | [阅读](glossaries/large-language-models.md) | [下载](pdf/large-language-models.pdf) |
| 深度学习 / Deep Learning | 500 | 18 | [阅读](glossaries/deep-learning.md) | [下载](pdf/deep-learning.pdf) |
| 强化学习 / Reinforcement Learning | 305 | 14 | [阅读](glossaries/reinforcement-learning.md) | [下载](pdf/reinforcement-learning.pdf) |
| 线性代数 / Linear Algebra | 289 | 12 | [阅读](glossaries/linear-algebra.md) | [下载](pdf/linear-algebra.pdf) |
| 概率论 / Probability Theory | 405 | 16 | [阅读](glossaries/probability-theory.md) | [下载](pdf/probability-theory.pdf) |
| 大学数学 / University Mathematics | 627 | 17 | [阅读](glossaries/university-mathematics.md) | [下载](pdf/university-mathematics.pdf) |
| **合计** | **3,019** | **117** | | |

**数据说明：**此前制作的六本 PDF 均保留原始完整版本，共自述含 2,298 条术语；从版式 PDF 提取的可检索记录有 2,250 条，尚有 48 条因跨行排版未能自动恢复。原始 PDF 才是这些书册完整词条的权威副本。新增的 AI Infra 则独立整理了 142 条结构化术语；大学数学卷另外提供 17 个章节、627 条原创整理词条与 3 份附录，保留可重新排版的 HTML 源文件。大学数学与已有线性代数、概率论专题存在概念交叉，统计口径按专题卷分开计数。网页中所有“词条数”均指真实可搜索索引条目，不将 PDF 封面数字直接冒充完整的数据导入数量。

## GitHub Pages 展示

主题为专业技术知识库、研究数据门户的 UI，支持：

- **中英混合全文搜索：**英文、中文、缩写、专题和解释；
- **主题选择：**8 个学科、117 个专题；
- **覆盖可视化：**按学科展示真实术语数量及学习路线；
- **资料下载：**每个主题的 PDF、Markdown，以及搜索结果 CSV；
- **交互体验：**移动端布局、明暗主题、键盘快捷键、分享检索链接。

静态资源位于 `docs/`，无需后端、数据库或付费 API。仓库首次发布后，需要仓库管理员在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。无需生成新的工作流，现有 `.github/workflows/pages.yml` 已配置部署 `docs/`；随后在 **Actions → Publish TERM/ATLAS to GitHub Pages** 中重新运行之前失败的任务（或点击 Run workflow）。网页成功部署后，上方链接才会正常访问。详见 [部署说明](docs/PAGES_SETUP.md)。

## 更新与质量控制

编辑 `data/terms.json` 中的词条，字段包含 `category`、`chapter`、`topic`、`en`、`zh`、`abbr`、`definition`，然后执行：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/verify.py
python3 -m unittest discover -s tests -v
```

**注意：**现有六本 PDF 是独立排版的原件，不会因为修改 JSON 自动覆盖。若修改术语含义，需要同步检查原版 PDF 的版本一致性。大学数学卷请优先修改 [`sources/university-mathematics.html`](sources/university-mathematics.html)，再运行构建器以同步更新 627 条索引、Markdown、PDF 和站点。详情参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [AGENTS.md](AGENTS.md)。

本项目用于研究、学习和工程阅读；不是任何标准组织发布的官方术语规范。仓库尚未选择开放许可，直到明确发布 License 之前请保留作者权利。