# TERM/ATLAS · 深度 Wiki 建设路线图

## 目标与数据层

- **L0 术语索引**：保持 `data/terms.json`、各原始 TSV/Markdown 和 PDF 的术语权威关系，不擅自改动定义与统计。
- **L1 技术 Wiki**：每个术语一篇独立 Markdown，覆盖定义、形象理解、机制、实际取舍、易混知识与答题训练。
- **L2 知识路径**：通过专题索引、前置依赖与关联术语串联形成课程路线。

## 读者入口与作者入口

读者唯一的正常入口为 [TERM/ATLAS Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/#explorer)：点击英文或中文术语，进入统一的 `term.html` 详情；已发布的完整文章从 `docs/data/wiki-index.json` 自动映射到该页。**批次、验收表和排期仅用于作者内部协调，不出现在公开网页。**

每篇的正文模板见 [TEMPLATE.md](TEMPLATE.md)，生产审核要求见 [EDITORIAL_REVIEW.md](EDITORIAL_REVIEW.md)，数据流、校验与发布命令见 [维护者指南](../docs/MAINTAINERS_GUIDE.md)。

## 分批实施

**每批恰好 20 个术语，末批不足 20 则按实际余量。** 按原始词表顺序分组，避免增删、跳号和重复。每批执行“来源审读→正文与图解→面试/考试题→答案复核→引用/链接复核→独立 PR→审核合并”，并严格区分 *planned*、*drafted_in_pr*、*merged*。

**当前研究对象：** [AI Infra（142 条、8 批）](ai-infrastructure/README.md)，Batch 01/02 共 40 篇已发布，Batch 03–08（剩余 102 篇）待研究。

之后依照同一方法覆盖仓库其他类别，包括 GPU Kernel、LLM、AI Agent、机器学习、深度学习、强化学习、Linux、操作系统、数据库、编译与数学等。各域的计划数量以真实源文件核对后生成，不预估未核查的覆盖率。

## 完成验收（Definition of Done）

1. 术语中英文、缩写、定义与适用范围无明显错误；技术事实注明厂商/版本与可靠来源。
2. 至少 2 个中等难度面试题（含答案）、2 个中等难度考试题（含详细解析）。
3. 附实际案例、常见误区与至少一条可信参考文献；数值题写明假设与单位。
4. 源稿与 Pages 镜像相同、`docs/data/wiki-index.json` 映射准确、编号/数量/内链校验通过；PR 合并且部署成功后才称为线上可读。
5. 发布文章不含 Batch、生产进度、待办清单或 PR 状态；这些属于 [内部审稿流程](EDITORIAL_REVIEW.md)。

## 证据验收与上线边界

专业文章的上线文件检查和人类技术签核是两个不同状态。已发布正文来自 `docs/data/wiki-index.json`，独立专家复核记录在 [reviews/README.md](reviews/README.md) 和审稿台账中；现有 40 篇初始为 pending。不能用结构验证掩盖引用的真实性、数值推导或适用范围缺陷。

