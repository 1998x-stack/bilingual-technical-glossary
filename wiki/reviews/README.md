# 深度 Wiki · 专业证据审稿制度

> 面向研究者、学科审稿人和维护者的内部质量控制流程。自动测试通过 ≠ 技术事实审查通过 ≠ 外部来源真实支持所有段落。

## 三个独立质量层次

1. **结构一致性：** `verify_wiki.py`、`build_wiki_index.py --check` 验证文章、术语、内容镜像、公开映射与章节。
2. **自动证据审计：** `verify_wiki_reviews.py --report --check` 扫描链接、空泛引用措辞、题目/定义区段、每篇审稿记录，输出 `wiki-evidence-report.json`（CI Artifact）。
3. **真实人工专家复核：** 针对定义、原论文/标准的具体条款、版本适用性、工程结论、两类题目和数学推导给出逐条论证，随后在受审查 PR 中做署名签核。

## 全部已发布 Wiki 的复核状态

`wiki/reviews/ai-infrastructure.json` 列出 `docs/data/wiki-index.json` 中当前全部 **60 篇**，尚未由真实审稿人签核的条目均为 `status: pending`；**不得**将结构检查误称为专业审稿完成。审稿者应依照 [内部编辑清单](../EDITORIAL_REVIEW.md) 对照原论文/标准逐篇核对。对于“官方技术资料”之类宽泛来源、跨技术主题的通用引用和题目中未注明的精度口径，优先要求补正。

## 签核流程

对于完成事实审校的一篇条目：

- 保留 `path`，将 `status` 改为 `verified`。
- `reviewer` 为真实 GitHub 评审人 handle；`reviewed_at` 为实际审核日期（YYYY-MM-DD）；`sha256` 为**所审 Markdown 当前字节 SHA256**。
- `attestations` 包括 `definitions`、`mechanisms`、`examples`、`interview_answers`、`exam_answers`、`version_scope`、`copyright`，需要每项确实审核才可设为 `true`。
- `claims` 至少两条，包括有意义的技术断言 `claim`、原始资料的 HTTPS `url`、页/节/代码位置 `locator`、如何对应断言的 `rationale`。
- 审稿人通过 GitHub PR 评论说明审阅了具体文件和引用，合并前由其他维护者复核。更新文章内容后旧 SHA 不再匹配，必须重新审阅。

### 记录结构示意（**非真实审核结果**）

```json
{
  "path": "wiki/ai-infrastructure/001-graphics-processing-unit.md",
  "status": "verified",
  "reviewer": "example-reviewer",
  "reviewed_at": "2026-11-16",
  "sha256": "64-character-hex-digest-of-reviewed-file",
  "attestations": {
    "definitions": true, "mechanisms": true, "examples": true,
    "interview_answers": true, "exam_answers": true,
    "version_scope": true, "copyright": true
  },
  "claims": [
    {
      "claim": "具体且可证的技术定义",
      "url": "https://example.org/actual-primary-source",
      "locator": "Section 3.1",
      "rationale": "这段实际资料如何支持该断言"
    }
  ]
}
```

以上是格式示例，**不代表已有人签核**。实际签核记录须包含两条以上真实资料核验。

## 常用命令

```bash
python3 scripts/verify_wiki_reviews.py --check --report
python3 scripts/verify_wiki.py
python3 scripts/build_wiki_index.py --check
```

若 CI 报告有 pending 条目，说明仍需人工领域审核，属于**明确追踪的审稿债务**，不是技术审稿完成。新增正文必须提供可核验、与术语匹配的一手来源；避免统一复制无关文档链接。
