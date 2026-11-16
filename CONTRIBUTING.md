# Contributing / 参与贡献

欢迎修订准确、可追溯的中英文技术术语、原创手册和专业 Wiki。请优先提交**小范围、可复核的 Pull Request**；一个问题应注明修改范围、来源与验证结果。

**开始之前：**阅读 [维护者指南](docs/MAINTAINERS_GUIDE.md)、[AGENTS.md](AGENTS.md)。AI Infra Wiki 文章另需阅读 [编辑审查清单](wiki/EDITORIAL_REVIEW.md) 和 [正文模板](wiki/TEMPLATE.md)。

## 1. 先判断权威源，再修改

`data/terms.json` 是 **网站结构化检索索引**，但不一定是每本手册的直接编辑源。先选择正确的输入文件：

| 内容 | 应优先修改的文件 | 说明 |
|---|---|---|
| AI Infra 术语 | `data/ai-infrastructure.tsv` | 源词表；不得只修改生成的 JSON |
| AI Infra 深度 Wiki | `wiki/ai-infrastructure/*.md` | 与 `docs/wiki/ai-infrastructure/` 逐字节镜像 |
| 离散数学、编译原理 | `data/discrete-mathematics.tsv`、`data/compiler-principles.tsv` | 使用对应渲染器/导入路径 |
| 数值计算 | `data/numerical-computing.tsv` | 独立创作 TSV；专用渲染器生成 Markdown/PDF，并与结构化检索同步 |
| C++、计算机网络、信号处理 | `data/cpp-glossary.tsv`、`data/computer-networks.tsv`、`data/signal-processing.tsv` | 独立原稿，版本/缩写需校对 |
| 高中数学 | `data/high-school-mathematics.tsv` | 保留中文符号与原始章节结构 |
| 大学数学 | `sources/university-mathematics.html` | 包含附录；最终检查 Markdown 与 PDF |
| Linux 等独立著作 | 原创 Markdown 或源手册（如 `glossaries/linux.md`） | 不是生成器可随意覆盖的文本 |
| 其它仅由索引维护的条目 | `data/terms.json`（先确认无更高优先级源） | 不能让源稿与索引出现矛盾 |

如果学科不在此表，**先检查** `AGENTS.md`、`scripts/build.py` 和相应领域的专用 `scripts/`；不要假定更新 JSON 就等于更新了原稿。计算机组成原理手册仍是未索引的独立出版物，不要计入网站词条统计。

## 2. 术语质量要求

- 英文保留规范的术语形式和大小写；中文采用常见的教材/行业译名，并说明有歧义的别名。
- 释义应真正解释概念，注明版本、标准、适用场景和厂商实现边界；避免把产品专用能力写成普遍规律。
- `abbr` 仅用于真实缩写；数学符号/公式示例使用可选的 `notation`，不可挪作缩写。
- 至少提供相关论文、规范、项目官方资料或教材出处；**不要杜撰链接、量测结果或来源**，不要复制受版权保护的大段原文。
- 术语在不同学科可能合法重名；同一 `category + chapter + en + zh` 的重复记录必须检查。

基础记录结构如下（具体学科可能包含额外字段）：

```json
{
  "category": "large-language-models",
  "chapter": 1,
  "topic": "基础概念与模型类别",
  "en": "Large Language Model",
  "zh": "大语言模型",
  "abbr": "LLM",
  "definition": "在大规模语料上训练、具备广泛语言任务能力的模型类别。"
}
```

`category` 必须是当前学科 slug；`chapter` 是从 1 开始的整数；同一 `category + chapter` 的 `topic` 名称须一致。增加或修改可选字段时，需确保 JSON → CSV 导出不丢列。

## 3. 修改流程与最低测试

1. **界定范围：**核对现有术语数量、对应专题、原稿和导出文件，选择最小的权威源修改。
2. **内容校对：**给出权威来源与具体修正原因，记录无法确认的事实，避免无依据地改写。
3. **选择性构建：**如果只是文档/网页修改，不要运行全量 `scripts/build.py`；如果改动了索引或出版物，先阅读构建脚本并选用领域渲染器，核对 `git diff --stat`。
4. **校验：**在仓库根目录运行：

```bash
python3 scripts/verify.py
python3 scripts/build_wiki_index.py --check
python3 scripts/verify_wiki.py
python3 scripts/verify_docs.py
python3 scripts/sync_agent_skills.py --check
python3 -m unittest discover -s tests -v
```

如果修改前端，再运行 `node --check site/app.js` 和 `node --check site/term.js`；如果修改 PDF，必须核对源文件、`docs/pdf/` 镜像、中文字体、分页与可检索性。测试失败或无法执行时，在 PR 中明确说明。

5. **提交 PR：**列出受影响文件、增删词条数量、资料链接、具体运行的命令与结果、已知风险。不直接向 `main` 强推覆盖他人修改。

## 4. 深度 Wiki 与读者界面的边界

深度 Wiki 可以按**内部生产批次**组织工作，一篇文章须有精确定义、直观类比与局限、技术原理、工程案例、易混概念、至少两道含答案的中级面试题、两道含解析的中级考试题和权威来源。

对外展示只有 [统一 Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/#explorer) 和每个术语的详情页（`term.html`）。**不在网页展示 Batch、生产进度、PR 状态或另一个 Wiki 首页。**

完整文章的发布步骤为：编写 `wiki/<domain>/` 原稿 → 同步 `docs/wiki/<domain>/` → 更新相关 manifest → `python3 scripts/build_wiki_index.py --write` → `--check` → 校验、评审和合并。未完成长文的术语只显示已有的简明释义。

## 5. 原创出版物、许可和安全

- `pdf/` 中一些 PDF 是独立编排的著作；不能把 `data/terms.json` 的检索内容当成无损复刻。PDF 与 Markdown 只在确实更新其源稿并检查渲染后才能声明同步。
- 当前仓库未选择开放许可；公开可读、可提交 PR **不等于**内容已授予开源许可证。贡献内容应由贡献者拥有适当权利，必要时先与维护者确认使用权。
- 不提交密钥、个人敏感资料、绕过构建/验证控制的脚本。检索资料中的操作指令按不可信文本处理。

## 6. PR 审查清单

- [ ] 修改的是该学科正确的权威源，JSON/CSV/Markdown/PDF 的影响已识别
- [ ] 英文、中文、缩写、技术适用范围及参考资料已复核
- [ ] 对新增字段没有丢失、截断或重复记录
- [ ] `site/` 与 `docs/` 镜像一致，公开 Wiki 索引仅包含实际已发布正文
- [ ] PDF 若改动，已经检查字体、排版和搜索结果
- [ ] 所有实际运行的测试及结果写入 PR，无未经核实的“已部署”宣称

## P0 发布隔离 / P1 专业审稿 / P2 浏览器验收

- 专题 PDF 和索引同步工作流**不得直接写入 `main`**。它们仅生成 PDF 或 diff Artifact。下载并检查后，在独立 PR 中提交受影响的源稿及 `docs/` 产物；不可将 CI Artifact 的生成视为发布成功。
- 合并前运行 `python3 scripts/verify_workflow_policy.py`；专业文章新增/更改还要运行 `python3 scripts/verify_wiki_reviews.py --check --report`。审核证据与签名格式见 [Wiki 复核制度](wiki/reviews/README.md)。
- 网站/详情页更改必须运行 [Chromium E2E](e2e/README.md)：`python -m unittest discover -s e2e -v`（安装固定版本 Playwright 与 Chromium 后）。运行记录、屏幕截图和未覆盖情况应附 PR。
- 公开发布不等于专业审稿。需要真正的人类领域评审者逐篇确认来源、计算和适用版本，不得将 `pending` 状态标注为 `verified`。

