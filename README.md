# 细胞外囊泡提取方法与优化指南 · EV Isolation Methods Guide

**中文** | [English](#english)

一份中文、可交互的细胞外囊泡（EV）提取方法学指南：七种主流方法的原理、典型参数、优缺点与优化要点，按“样本来源 × 下游用途 × 优先指标”给出起点方案的推荐器，依据 MISEV2023 的质控清单，17 张开放许可（CC BY 4.0）的文献原图和 12 张 AI 原理示意图，以及 49 篇经 PubMed 与 Crossref 核验的参考文献。

- 在线阅读（GitHub Pages）：<https://tuanziding.github.io/ev-isolation-guide/>
- aiai-academy.com 版本：<https://aiai-academy.com/lessons/ev-isolation-guidev1.0.html>（经作者审核后上线，姊妹篇为“外泌体与细胞外囊泡漫游”）
- 版本 1.1.0 · 最后核验 2026-11-13（v1.1 新增图片，见下文“图片”）

## 仓库里有什么

| 路径 | 内容 |
|---|---|
| `index.html` + `assets/` | 互动网页（系统字体、无外部 CDN，可离线打开；支持手机与打印） |
| `docs/content-zhv1.1.md` | 指南全文，**唯一事实来源**；网页与下列 Markdown 都由它生成 |
| `protocols/` | 按方法拆分的 7 份方法说明，以及组合思路、横向对比、标准流程、原代细胞示例、分样本要点、常见坑，每份附所引文献和相关图片 |
| `checklists/qc-checklistv1.1.md` | 依据 MISEV2023 的可勾选质控清单 |
| `references/` | `referencesv1.1.json`（49 条，含 DOI、PMID、PMCID、核验方式）与 `references.bib` |
| `figures/` | 17 张文献原图（`fig-*.webp`）与 12 张 AI 示意图（`schem-*.webp`），`-sm.webp` 为网页用缩略图；`figures-realv1.0.json`（每张图的出处、原文图注、许可核验记录）、`schematicsv1.1.json`（示意图标注坐标） |
| `FIGURES-LICENSES.md` | 文献原图逐张的授权与署名表 |
| `evidence/` | `claimsv1.0.json`（逐条陈述的证据分级与原文引语）与 `auditv1.0.md`（审核报告） |
| `assets/data/` | 推荐器规则 `recommender-rulesv1.0.json`（5 种样本 × 4 种用途 × 4 种优先级 = 80 条，每条带引用）与文献数据 |
| `tools/` | 生成网页和 Markdown 的脚本，以及无头浏览器检查脚本 |

## 陈述如何核验

1. 从原稿逐条拆出事实性陈述，共 106 条，记录在 `evidence/claimsv1.0.json`。
2. 每条陈述用 PubMed E-utilities 检索原始文献，读 PMC 开放全文或摘要，记录支持它的原文引语。
3. 用 Crossref API 核对每条文献的 DOI、卷、页、年份和第一作者。v1.0 的 45 条文献全部通过（OK 45 / MISMATCH 0 / FABRICATED 0）；v1.1 新增的 [46]–[49] 同样经 PubMed、Crossref 与 PMC OA 元数据核验，只作为转载图片的出处，不支撑正文陈述。35 篇读过全文，10 篇只核对了摘要，这 10 篇只用来支撑摘要里明确写到的内容（名单见 `evidence/auditv1.0.md`）。
4. 分级结果：有原文支持 44 条；方向正确但表述过度或数字不准、已改写 52 条（其中 14 条为实质性纠错）；无可核验文献 10 条，已删除或保留并标注。
5. 网页中凡标注【实验室惯例】、【估算】或【作者判断】的内容，没有直接的文献测定值支持。方法卡上的评分点数是“定性共识”，不是测量值。

每个事实句后的 [n] 都链接到参考文献表，表中每条都有 DOI 与 PubMed 链接。

## 图片（v1.1）

- **文献原图（17 张，标“文献原图 · CC BY 4.0”）**：全部来自 CC BY 4.0 开放获取论文，逐篇在 PMC OA 元数据、文章 XML 与 Europe PMC 三处核对许可，图注中没有第三方版权限制。内容未作修改，仅转换为 WebP 并缩小尺寸。每张图都附中文“怎么读这张图”、原文图注引语和署名（Reproduced from …, CC BY 4.0, no changes）及 DOI、PMC 链接。网页里按仪器（NTA、TEM/冷冻电镜、Western blot、SEC 洗脱曲线、密度梯度、方法对比）分组，可按样本类型筛选。
- **AI 示意图（12 张，标“AI 示意图 · 非实验数据”）**：AI 生成的原理示意图，帮助理解装置和流程，不是实验数据。图中编号标注由网页叠加，坐标逐张核对。
- **缺口**：exomere 的 AF4 洗脱曲线（Zhang 2018 [30]）和尿液 DTT 处理前后对比（Fernández-Llama 2010 [38]）没有找到开放许可的原图，未转载，网页中给出原文链接。

## 如何引用

请同时引用本指南和你实际依据的原始文献。仓库根目录的 `CITATION.cff` 可被 GitHub 识别（页面右侧 “Cite this repository”）。

> Ding H. 细胞外囊泡提取方法与优化指南（Extracellular Vesicle Isolation Methods: An Interactive Chinese Guide）. Version 1.1.0. 2026-11-13. https://github.com/TUANZIDING/ev-isolation-guide

## 声明

本指南为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。

## 许可

- **文字与数据**：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)（`docs/`、`protocols/`、`checklists/`、`evidence/`、`references/`、`assets/data/`、本 README 以及网页中的文字）。全文见 `LICENSE-CC-BY-4.0.txt`。
- **代码**：MIT（`index.html` 的页面结构、`assets/*.css`、`assets/*.js`、`tools/`）。见 `LICENSE`。
- **第三方图片不适用本仓库的许可**：`figures/fig-*.webp` 这 17 张文献原图的版权归原作者，仍按各自原论文的 CC BY 4.0 许可使用，再使用时须按 `FIGURES-LICENSES.md` 中的署名语注明原作者和出处。
- 团子插图与 `figures/schem-*.webp` 示意图由 AI 生成，仅作示意，不代表真实实验装置或实验数据。
- 参考文献条目只是书目信息，本仓库不分发被引论文本身。

## 本地查看与重新生成

```bash
python3 -m http.server 8000          # 然后打开 http://localhost:8000/
python3 tools/build-sitev1.1.py github index.html assets   # 由 docs/content-zhv1.1.md 重新生成网页
python3 tools/build-docsv1.1.py .                          # 重新生成 protocols/ 与 checklists/
python3 tools/check-pagev1.1.py http://localhost:8000/ shots/gh   # 无头检查（需 Playwright）
```

---

<a id="english"></a>
## English

An interactive, Chinese-language guide to isolating extracellular vesicles (EVs). It covers the principles, typical parameters, strengths, limits and optimisation points of seven common methods; a recommender that suggests a starting route from **sample type × downstream use × priority**; a MISEV2023-based QC checklist; 17 openly licensed (CC BY 4.0) figures reproduced from the literature plus 12 AI-generated schematics; and 49 references verified against PubMed and Crossref.

- Read online (GitHub Pages): <https://tuanziding.github.io/ev-isolation-guide/>
- aiai-academy.com edition: <https://aiai-academy.com/lessons/ev-isolation-guidev1.0.html> (goes live after the author's review; companion to the “Exosomes & EVs” explorer)
- Version 1.1.0 · last verified 2026-11-13 (v1.1 adds figures)

### How the claims were verified

- 106 factual statements were extracted from the original draft (`evidence/claimsv1.0.json`). Each was checked against the primary literature through PubMed E-utilities (PMC open-access full text or abstract), with the supporting quotation recorded.
- Every reference's DOI, volume, pages, year and first author was checked against the Crossref API: 45 of 45 OK in v1.0, none mismatched or fabricated; the four references added in v1.1 ([46]–[49]) were verified the same way plus PMC OA metadata and are cited only as figure sources. 35 papers were read in full text; 10 were checked at abstract level only and are used only for what their abstracts state (listed in `evidence/auditv1.0.md`).
- Outcome: 44 statements supported as written, 52 softened or corrected (14 substantive corrections), 10 without a verifiable source removed or kept with an explicit label.
- Content labelled 【实验室惯例】 (lab convention), 【估算】 (estimate) or 【作者判断】 (author's judgement) has no direct literature measurement behind it. The dot ratings on the method cards are a qualitative consensus, not measurements.

`docs/content-zhv1.1.md` is the single source of truth; the web page, the per-method protocols and the QC checklist are generated from it by the scripts in `tools/`.

### Figures (v1.1)

- **Reproduced figures (17, badge “文献原图 · CC BY 4.0”)**: all from CC BY 4.0 open-access articles; the licence was checked per article in PMC OA metadata, the article XML and Europe PMC, with no figure-level third-party restriction. Content unchanged; only converted to WebP and downsized. Each carries a Chinese reading guide, the quoted original legend, and an attribution line (Reproduced from …, CC BY 4.0, no changes) with DOI and PMC links. Per-figure attributions: `FIGURES-LICENSES.md`.
- **Schematics (12, badge “AI 示意图 · 非实验数据”)**: AI-generated explanatory drawings, not experimental data.
- **Gaps**: no openly licensed figure was found for the exomere AF4 profile (Zhang 2018 [30]) or a urine DTT before/after comparison (Fernández-Llama 2010 [38]); the page links to the original papers instead.

### How to cite

Cite this guide together with the primary studies you rely on. GitHub reads `CITATION.cff` (“Cite this repository”).

> Ding H. Extracellular Vesicle Isolation Methods: An Interactive Chinese Guide (细胞外囊泡提取方法与优化指南). Version 1.1.0. 2026-11-13. https://github.com/TUANZIDING/ev-isolation-guide

### Disclaimer

This is a methods reference and literature review, not a protocol or conclusion for any specific project. Parameters are values reported in published studies or ISEV guidance; follow the manuals of your own instruments, rotors and commercial products, and pilot-test on your own samples before formal experiments.

### Licence

- **Text and data**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (`docs/`, `protocols/`, `checklists/`, `evidence/`, `references/`, `assets/data/`, this README, and the prose in the web page). Legal code in `LICENSE-CC-BY-4.0.txt`.
- **Code**: MIT (`index.html` markup, `assets/*.css`, `assets/*.js`, `tools/`). See `LICENSE`.
- **Third-party figures are not covered by this repository's licences**: the 17 reproduced figures in `figures/fig-*.webp` remain the work of their original authors under their original CC BY 4.0 licences; attribute them as listed in `FIGURES-LICENSES.md` when reusing.
- The mascot illustrations and the `figures/schem-*.webp` schematics are AI-generated; they are explanatory only, not depictions of real equipment or data.
- Reference records are bibliographic metadata only; the cited articles are not redistributed.
