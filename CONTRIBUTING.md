# Contributing / 参与贡献

欢迎贡献准确、可追溯的双语术语。请优先提交 **小范围、可复核的 Pull Request**。

## 提交流程

1. 在 `data/terms.json` 中定位词条（或新增符合现有字段约定的条目）。
2. 推荐写法：英文规范词形、中文常用译名、缩写、一句话说明、适用专题。
3. 在 PR 描述中给出支持该译法的资料（学术论文、教材、项目官方文档、规范），并解释可疑歧义。
4. 运行 `python3 scripts/build.py`，同步提交生成的 Markdown、CSV 和 `docs/data`。
5. 运行 `python3 scripts/verify.py` 和 `python3 -m unittest discover -s tests -v`。
6. 数据结构专题有独立维护的 `glossaries/data-structures.md` 和 `sources/data-structures.html`；修订后请同步 JSON 索引和 PDF，避免网页与手册不一致。
7. 如果源 PDF 的内容也需要改变，须说明版本及排版方案；不可假装只修改 Markdown 就等于已更新 PDF。

## 词条质量门槛

- 英文和中文都必须非空；缩写可以为空。
- 释义应解释概念，不应仅重复中文译名。
- 区分通用概念与具体实现、产品或协议版本。
- 避免凭空创造标准缩写和唯一官方译名。
- 允许一个英文名在不同语境下具有不同中文译法，但应标记差异。
- 不要复制受版权保护教材中的长段原文。

## Data schema

```json
{
  "category": "large-language-models",
  "chapter": 1,
  "topic": "基础概念与模型类别",
  "en": "Large Language Model (LLM)",
  "zh": "大语言模型",
  "abbr": "LLM",
  "definition": "以大规模参数与数据训练的语言模型。"
}
```

`category` 必须选自仓库当前主题 slug。`chapter` 为从 1 开始的整数；同一个 `category + chapter` 必须始终使用相同的中文专题名称。

## Review checklist

- [ ] 中英文规范与适用语境已核验
- [ ] JSON 字段齐全、无同章节重复
- [ ] 导出的 Markdown / CSV / Pages JSON 已同步
- [ ] 字符转义及 PDF 中文显示正常
- [ ] 测试通过、PR 写明来源及变化范围
