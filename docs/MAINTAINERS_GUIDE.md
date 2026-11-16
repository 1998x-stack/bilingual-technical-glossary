# TERM/ATLAS · 维护者架构与发布手册

> 维护文档；非读者界面。若本页与代码不同，以仓库当前实际源文件、构建脚本和校验为准。编辑总则见 [AGENTS.md](../AGENTS.md)，贡献流程见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 1. 四种不同的“源”

术语库不是简单的“一份 JSON 生成全部内容”。应区分：

| 层次 | 代表文件 | 是谁维护它 | 职责 |
|---|---|---|---|
| 学科原稿 / 专业资料 | `data/*.tsv`、`sources/*.html`、`glossaries/*.md` | 人工/领域工具 | 术语定义、章节、原始出版内容 |
| 结构化检索数据 | `data/terms.json`、`data/terms.csv` | 部分学科手工、部分学科导入/重建 | 全站搜索，CSV/JSON 数据分发 |
| 专业 Wiki 内容 | `wiki/<domain>/*.md` | 专家写作与审校 | 精确定义、原理、案例、面试与考试 |
| 网站静态发布 | `site/`、`docs/` | 源代码与构建脚本 | 读者交互、检索、下载、Wiki 展示 |

并非每个学科都从同一种输入生成。**先读 `AGENTS.md` 的学科专用规则，再选入口文件。** `docs/` 中的 PDF 与 Markdown 有出版物镜像，但不应把它们当作原稿直接编辑。

## 2. 唯一读者入口与术语链接

```text
浏览器 /?category=reinforcement-learning#explorer
    │
    ▼
docs/index.html + docs/app.js
    │  fetch docs/data/catalog.json + terms.json
    │  click English / 中文
    ▼
docs/term.html?category=…&chapter=…&en=…&zh=…
    │
    ├─ 始终展示 data/terms.json 的简明释义
    │
    └─ docs/data/wiki-index.json 存在对应映射?
         ├─ 是：加载 docs/wiki/<domain>/<article>.md 的完整技术解析
         └─ 否：只展示真实简明释义，绝不假装已有长文
```

- `term.html` 的查询键由 `category + chapter + en + zh` 构成，不应使用全局行号代替稳定身份。
- 已发布 Wiki 引用原始 `data/ai-infrastructure.tsv` 时，`docs/data/ai-infrastructure.tsv` 须由 `scripts/build.py` 同步并通过字节级一致性校验。
- `docs/data/wiki-index.json` 是**公共文章映射，不是内部生产计划**。由 `scripts/build_wiki_index.py` 根据 `docs/wiki/*/manifest.json` 的发布标志、结构化词条身份、原稿及 Pages 镜像生成。
- AI Infra 当前的 `wiki/ai-infrastructure/batches.json`、`wiki/ai-infrastructure/README.md` 可保留内部生产批次；**对外 UI 不出现批次名称、数字、看板或另建的 `/wiki` 主页**。
- 历史 `docs/wiki/ai-infrastructure/index.html` 用于旧链接重定向。不要把旧入口再设为站点导航。
- 网站源码资产 `site/index.html`、`site/app.js`、`site/styles.css`、`site/term.html`、`site/term.js`、`site/term.css` 必须与 `docs/` 中对应文件一致。

## 3. 修改场景与安全操作

### A. 仅修改文档或 Agent 指令

只改相关 Markdown；如果修改 Skills，先改 `.agents/skills/` 再运行：

```bash
python3 scripts/sync_agent_skills.py --sync
python3 scripts/sync_agent_skills.py --check
python3 scripts/verify_docs.py
```

无需因此触发全量 PDF 渲染。

### B. 发布新的专业 Wiki

1. 在正确的 `wiki/<domain>/` 下创作一篇准确的长文，按 [正文模板](../wiki/TEMPLATE.md) 撰写、按 [编辑审查清单](../wiki/EDITORIAL_REVIEW.md) 验收。
2. 同步相同字节至 `docs/wiki/<domain>/`，更新该领域可用的 manifest，只有经过校对且准备发布的文章才标记为 `ready`。
3. 运行 `python3 scripts/build_wiki_index.py --write`，核对新映射与术语身份、文件路径。**不要在公开主页增添专题 Wiki 面板或 Batch 导航。**
4. 运行下述只读测试，并提交 PR；在合并后观察 `main` 分支的 Pages 工作流。

### C. 校订双语术语或独立手册

1. 先读 [贡献规则](../CONTRIBUTING.md) 的权威源对应表。
2. 判断是否需要改变结构化搜索数据；注意跨领域同名、缩写、数学记号、章节与可选字段。
3. 需要重建时先阅读 `scripts/build.py`，**不要把它当成通用无副作用的验证命令**。目前它会导入多个学科、重建索引与文稿、运行多个 PDF 渲染器并覆盖镜像。应优先选择领域专用命令，检查 `git diff --stat` 和二进制变化。
4. 若确需重排 PDF，检查中文字体、公式、表格、页数、文内搜索和 `docs/pdf/` 镜像；避免无意义地重写其它学科文件。

## 4. 合并前的只读验证

在仓库根目录运行：

```bash
python3 -m compileall -q scripts tests
node --check site/app.js
node --check site/term.js
python3 scripts/sync_agent_skills.py --check
python3 scripts/verify.py
python3 scripts/build_wiki_index.py --check
python3 scripts/verify_wiki.py
python3 scripts/verify_docs.py
python3 -m unittest discover -s tests -v
```

`node` 未安装时应在 PR 中说明跳过，GitHub Actions 会执行相应校验。上述命令只检查已提交文件，**不替代学术正确性、引用有效性、跨版本准确性或 PDF 人工分页检查**。

## 5. PR → CI → Pages → 复核

- 使用聚焦的 PR；确认 HEAD/BASE 与最新 `main`，不要混入自动化流程提交的无关 PDF 重生成。
- 先检查 `Validate glossary corpus` 的对应 commit 的运行结果，再合并。
- `.github/workflows/pages.yml` 只在 `main` 的 `docs/**` 或 workflow 文件变化时自动部署（也可手动触发）。仅改 `README.md` 不等于部署了新前端。
- 部署后访问 [主页 Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/#explorer)，至少抽检一个已有长文的术语和一个只有简明释义的术语，核对移动端、深色模式与返回筛选状态。
- **CI 通过 ≠ 浏览器视觉验收 ≠ 学科事实审稿。** 在交付报告中分别说明。

## 6. 数据覆盖与出版物边界

网站术语数、学科数、专题数分别从 `data/terms.json` 与 `docs/data/catalog.json` 计算；覆盖率是**已索引记录数量**，不是所有 PDF 词条的无损转录，也不是完整 Wiki 的覆盖率。计算机组成原理独立手册未进入结构化搜索，不得计入总数。

遗留 PDF 包含不能可靠自动提取的版面内容。保持原始出版物，不得因 JSON 与 PDF 数量不等就擅自删改原稿。

当前尚未发布适用于全部仓库内容的开源许可；项目公开可浏览并不自动赋予复用或再发布权。新增资料需核验版权和出处。

## 7. 相关索引

- [GitHub Pages 配置与排障](PAGES_SETUP.md)
- [历史结构审计（保留原基线）](QUALITY_AUDIT.md)
- [本轮文档核查](DOCUMENTATION_AUDIT_2026-11-16.md)
- [Agent Skills 使用与同步](agent-skills.md)
- [Wiki 内部写作规则](../wiki/README.md)
