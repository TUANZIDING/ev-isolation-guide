# 细胞外囊泡提取方法与优化指南 · EV Isolation Methods Guide

**中文** | [English](#english)

一份中文、可交互的细胞外囊泡（EV）提取方法学指南：七种主流方法的原理、典型参数、优缺点与优化要点，按“样本来源 × 下游用途 × 优先指标”给出起点方案的推荐器，依据 MISEV2023 的质控清单，以及 45 篇经 PubMed 与 Crossref 核验的参考文献。

- 在线阅读（GitHub Pages）：<https://tuanziding.github.io/ev-isolation-guide/>
- aiai-academy.com 版本：<https://aiai-academy.com/lessons/ev-isolation-guidev1.0.html>（经作者审核后上线，姊妹篇为“外泌体与细胞外囊泡漫游”）
- 版本 1.0.0 · 最后核验 2026-11-13

## 仓库里有什么

| 路径 | 内容 |
|---|---|
| `index.html` + `assets/` | 互动网页（系统字体、无外部 CDN，可离线打开；支持手机与打印） |
| `docs/content-zhv1.0.md` | 指南全文，**唯一事实来源**；网页与下列 Markdown 都由它生成 |
| `protocols/` | 按方法拆分的 7 份方法说明，以及组合思路、横向对比、标准流程、原代细胞示例、分样本要点、常见坑，每份附所引文献 |
| `checklists/qc-checklistv1.0.md` | 依据 MISEV2023 的可勾选质控清单 |
| `references/` | `referencesv1.0.json`（含 DOI、PMID、PMCID、核验方式）与 `references.bib` |
| `evidence/` | `claimsv1.0.json`（逐条陈述的证据分级与原文引语）与 `auditv1.0.md`（审核报告） |
| `assets/data/` | 推荐器规则 `recommender-rulesv1.0.json`（5 种样本 × 4 种用途 × 4 种优先级 = 80 条，每条带引用）与文献数据 |
| `tools/` | 生成网页和 Markdown 的脚本，以及无头浏览器检查脚本 |

## 陈述如何核验

1. 从原稿逐条拆出事实性陈述，共 106 条，记录在 `evidence/claimsv1.0.json`。
2. 每条陈述用 PubMed E-utilities 检索原始文献，读 PMC 开放全文或摘要，记录支持它的原文引语。
3. 用 Crossref API 核对每条文献的 DOI、卷、页、年份和第一作者。45 条文献全部通过（OK 45 / MISMATCH 0 / FABRICATED 0）。35 篇读过全文，10 篇只核对了摘要，这 10 篇只用来支撑摘要里明确写到的内容（名单见 `evidence/auditv1.0.md`）。
4. 分级结果：有原文支持 44 条；方向正确但表述过度或数字不准、已改写 52 条（其中 14 条为实质性纠错）；无可核验文献 10 条，已删除或保留并标注。
5. 网页中凡标注【实验室惯例】、【估算】或【作者判断】的内容，没有直接的文献测定值支持。方法卡上的评分点数是“定性共识”，不是测量值。

每个事实句后的 [n] 都链接到参考文献表，表中每条都有 DOI 与 PubMed 链接。

## 如何引用

请同时引用本指南和你实际依据的原始文献。仓库根目录的 `CITATION.cff` 可被 GitHub 识别（页面右侧 “Cite this repository”）。

> Ding H. 细胞外囊泡提取方法与优化指南（Extracellular Vesicle Isolation Methods: An Interactive Chinese Guide）. Version 1.0.0. 2026-11-13. https://github.com/TUANZIDING/ev-isolation-guide

## 声明

本指南为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。

## 许可

- **文字与数据**：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)（`docs/`、`protocols/`、`checklists/`、`evidence/`、`references/`、`assets/data/`、本 README 以及网页中的文字）。全文见 `LICENSE-CC-BY-4.0.txt`。
- **代码**：MIT（`index.html` 的页面结构、`assets/*.css`、`assets/*.js`、`tools/`）。见 `LICENSE`。
- 页面插图由 AI 生成，仅作装饰示意，不代表真实实验装置。
- 参考文献条目只是书目信息，本仓库不分发被引论文本身。

## 本地查看与重新生成

```bash
python3 -m http.server 8000          # 然后打开 http://localhost:8000/
python3 tools/build-sitev1.0.py github index.html assets   # 由 docs/content-zhv1.0.md 重新生成网页
python3 tools/build-docsv1.0.py .                          # 重新生成 protocols/ 与 checklists/
```

---

<a id="english"></a>
## English

An interactive, Chinese-language guide to isolating extracellular vesicles (EVs). It covers the principles, typical parameters, strengths, limits and optimisation points of seven common methods; a recommender that suggests a starting route from **sample type × downstream use × priority**; a MISEV2023-based QC checklist; and 45 references verified against PubMed and Crossref.

- Read online (GitHub Pages): <https://tuanziding.github.io/ev-isolation-guide/>
- aiai-academy.com edition: <https://aiai-academy.com/lessons/ev-isolation-guidev1.0.html> (goes live after the author's review; companion to the “Exosomes & EVs” explorer)
- Version 1.0.0 · last verified 2026-11-13

### How the claims were verified

- 106 factual statements were extracted from the original draft (`evidence/claimsv1.0.json`). Each was checked against the primary literature through PubMed E-utilities (PMC open-access full text or abstract), with the supporting quotation recorded.
- Every reference's DOI, volume, pages, year and first author was checked against the Crossref API: 45 of 45 OK, none mismatched or fabricated. 35 papers were read in full text; 10 were checked at abstract level only and are used only for what their abstracts state (listed in `evidence/auditv1.0.md`).
- Outcome: 44 statements supported as written, 52 softened or corrected (14 substantive corrections), 10 without a verifiable source removed or kept with an explicit label.
- Content labelled 【实验室惯例】 (lab convention), 【估算】 (estimate) or 【作者判断】 (author's judgement) has no direct literature measurement behind it. The dot ratings on the method cards are a qualitative consensus, not measurements.

`docs/content-zhv1.0.md` is the single source of truth; the web page, the per-method protocols and the QC checklist are generated from it by the scripts in `tools/`.

### How to cite

Cite this guide together with the primary studies you rely on. GitHub reads `CITATION.cff` (“Cite this repository”).

> Ding H. Extracellular Vesicle Isolation Methods: An Interactive Chinese Guide (细胞外囊泡提取方法与优化指南). Version 1.0.0. 2026-11-13. https://github.com/TUANZIDING/ev-isolation-guide

### Disclaimer

This is a methods reference and literature review, not a protocol or conclusion for any specific project. Parameters are values reported in published studies or ISEV guidance; follow the manuals of your own instruments, rotors and commercial products, and pilot-test on your own samples before formal experiments.

### Licence

- **Text and data**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (`docs/`, `protocols/`, `checklists/`, `evidence/`, `references/`, `assets/data/`, this README, and the prose in the web page). Legal code in `LICENSE-CC-BY-4.0.txt`.
- **Code**: MIT (`index.html` markup, `assets/*.css`, `assets/*.js`, `tools/`). See `LICENSE`.
- The illustrations are AI-generated decorative images, not depictions of real lab equipment.
- Reference records are bibliographic metadata only; the cited articles are not redistributed.
