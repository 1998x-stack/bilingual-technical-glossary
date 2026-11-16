# TERM/ATLAS · 文档与维护流程审计（2026-11-16）

> 本报告针对 `main` 基线提交 `41699f36e19cc668eee098a4d4617f093202e01b` 的仓库文档、构建/发布脚本和页面数据契约；它补充而不重写 [历史代码质量审计](QUALITY_AUDIT.md)。审计方法为源码、结构数据、Workflow 与 Markdown 交叉核对。**未完成逐条术语的学术同行审稿、外部 URL 批量存活性验证或浏览器截图视觉验收。**

## 基线事实（应从结构化文件核对）

- `data/terms.json` 和 `docs/data/catalog.json`：**8,889 条可检索术语，25 个学科，381 个专题**。按领域计数，非全站语义去重。
- `glossaries/computer-organization.md` / 原版 PDF：**678 条的独立手册**，尚未入结构化检索总数。
- `docs/data/wiki-index.json`：**40 篇已建立映射的 AI Infra 深度 Wiki**，其余已索引术语在详情页显示简明释义。40 是出版文件/索引的覆盖数，**不是 40 篇已完成独立技术同行评审的证明**。
- 当前浏览入口为 `/?category=<slug>#explorer`，从任意英/中术语链接进入 `term.html`；`docs/wiki/ai-infrastructure/index.html` 是旧地址兼容跳转，**不是**应推广的第二个 Wiki 首页。
- `scripts/build.py` 会导入多个学科，生成 JSON/CSV/部分 Markdown、调用多个 PDF 渲染器并更新 Pages 镜像；仅修改单条词条时不应未经检查直接运行总构建。
- `.github/workflows/pages.yml` 在 main 的 `docs/**` 变化后部署 Pages。纯文档或仓库根目录修改并不自动导致 Pages 重新发布。

## 本次发现与修复范围

| 优先级 | 文件/范围 | 已确认的问题 | 本次处理 |
|---|---|---|---|
| P0 | `CONTRIBUTING.md`、README 构建说明 | 一律优先改 `data/terms.json` 和运行总构建，会覆盖独立源稿的编排语义或触发无关 PDF 构建 | 建立按学科权威源选择的贡献流程与安全命令；区分编辑、渲染与只读校验 |
| P1 | `README.zh-CN.md` | GitHub Pages 章节的“23 学科、347 专题”与 25/381 当前目录不一致 | 改为真实数据口径并在 CI 增加文档统计校验 |
| P1 | `docs/QUALITY_AUDIT.md` | 历史基线 7,554/21/313 与当前版本不同；“恢复独立 Wiki 导航”建议已过时 | 明确标记为历史快照，链接当前审计与统一术语详情架构 |
| P1 | `wiki/TEMPLATE.md` | 公共正文模板混入 Batch/序号/编辑 checklist；未来复制后可能泄露生产字段 | 改为仅读者可见的八章节模板；内部检查单独维护 |
| P1 | `docs/PAGES_SETUP.md` | 缺少统一术语详情页、发布索引、旧入口跳转和详情页常见故障说明 | 补充从 Explorer → term.html → Wiki 的数据与排错流程 |
| P2 | README 中/英文、`AGENTS.md`、`wiki/README.md`、Skills 指南 | 缺少统一的“数据原稿 → 结构化索引 → 已发布正文 → Pages”维护图 | 新增维护者手册、领域规则、内部编辑验收和真实校验命令 |
| P2 | 文档自动验证 | 只校验 README 中是否包含术语总数字符串，无法发现旧的学科/专题数字或本地 Markdown 死链 | 新增文档检查器和回归测试；仅校验本地链接，避免 PR CI 每次依赖外网 |

## 仍需后续处理：不能靠改文档冒充已解决

1. **发布作业并发与直接写 main（P1）：**多个专题出版 Workflow 可能提交自动重新生成的 PDF/Markdown。最新基线提交本身涉及多本 PDF 的同步。建议限制自动化写入范围、对产物做确定性检查、通过 PR 审查及按领域并发串行化。此次不改工作流权限和发布架构。
2. **Wiki 学术质量与深度（P1）：**目前自动验收主要检验章节、两道面试题/两道考试题、镜像一致、基本 URL 存在。它**不能判断定义是否权威、例题是否正确、文字深度是否充足或引用是否真的支持结论**。引入领域审稿人、证据登记与逐条复核后才可宣称技术审稿完成。
3. **当前 Markdown 阅读器与复杂格式（P2）：**`site/term.js` 使用轻量渲染方法，仍应针对 LaTeX、长代码块、复杂表格、图片、语法边界与安全性做专项测试。文档不得暗示它支持完整 Markdown 或数学排版。
4. **浏览器端 E2E 和无障碍（P2）：**CI 包含 JavaScript 语法与文件回归测试，并不等价于 Chrome/Firefox/移动端的端到端交互、截图和屏幕阅读器验证。
5. **版权/许可证（P1）：**仓库尚未发布覆盖所有内容的许可证；公开阅读、下载与 PR 协作不等同于有明确授权。应由仓库所有者单独决定适宜许可，并核查既有资料的引用/改编权。
6. **外部引用健康度（P2）：**目前没有受缓存与速率限制约束的定期链接检查。建议周期性、非阻塞地检查权威参考资料，避免将随机网络故障变成日常 PR 失败原因。
7. **跨领域 Markdown/CSV/PDF 再现性（P2）：**总构建可能重排无关 PDF，需要按领域拆分发布并为关键手册记录可复核的渲染环境和手动排版抽样结果。

## 建议的后续维护级别

**必须持续自动校验：**结构化总数与目录、JSON/CSV 字段、源站/Pages 镜像、Skill 同步、Wiki 发布映射、内部 Markdown 链接与代码语法。

**必须人工审查：**词义的权威程度和语境、题目/答案推理、数学量纲、厂商代际指标、PDF 字体与页码、界面的可访问性、第三方许可。

## 复核命令

```bash
python3 scripts/verify_docs.py
python3 scripts/verify.py
python3 scripts/build_wiki_index.py --check
python3 scripts/verify_wiki.py
python3 scripts/sync_agent_skills.py --check
python3 -m unittest discover -s tests -v
```

完整决策树见 [维护者指南](MAINTAINERS_GUIDE.md)。当前 Wiki 内容的内部写作规则见 [编辑审核清单](../wiki/EDITORIAL_REVIEW.md)；读者入口仍是 [TERM/ATLAS Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/#explorer)。
