# 质控清单（依据 MISEV2023）

> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 [`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>
>
> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

提取做完不等于拿到 EV。MISEV2023 并不规定某一种必须使用的技术或标志物 [1]，但要求用互补证据支持“EV”的结论；缺项时如实说明，不要用单一颗粒计数结果宣称“提取成功”。

### 表征

- [ ] **颗粒数量与大小**：用 NTA、TRPS、纳米流式等方法报告粒径分布与颗粒浓度，并报告仪器设置和检测下限 [1]。
- [ ] **形貌**：TEM、冷冻电镜等成像；干燥条件下 EV 可能形成“杯状”伪影，水合条件下（如冷冻电镜）不出现 [1]。TEM 图像受操作者选图影响：操作者挑选的图像质量往往高于在预定位置随机取得的图像，后者更能反映样本差异 [40]。
- [ ] **蛋白标志（更正）**：MISEV2023 要求至少分析第 1、2、3 类蛋白各一种：第 1 类为跨膜或 GPI 锚定蛋白（如 CD9、CD63、CD81），第 2 类为胞质蛋白（如 TSG101、ALIX、syntenin），第 3 类为非 EV 共分离结构的主要成分，作为纯度对照（如脂蛋白 ApoA1/ApoB、白蛋白、尿中的 THP）[1]。**原稿“至少 3 个阳性标志”来自 MISEV2014，MISEV2018 已更新** [41]。
- [ ] **细胞内区室蛋白**：calnexin、GM130 等属第 4 类，在 MISEV2023 中为**可选**项，因为它们可能存在于某些 EV 亚型中 [1]；MISEV2018 则要求在宣称研究小 EV 时检测第 4 类 [41]。更宜报告“相对细胞裂解物的耗竭程度”，而不是简单的有/无 [41]。

### 纯度与报告指标

- [ ] **颗粒/蛋白比**：颗粒数 ÷ 蛋白量是常用的纯度估计 [42]；原作者提出 >3×10¹⁰ 颗粒/µg 为高纯度，2×10⁹–2×10¹⁰ 为低纯度，<1.5×10⁹ 为不纯（基于其实验室数据）[42]。该比值依赖仪器检测下限，若报告比值，应同时分别报告颗粒和蛋白的绝对浓度 [1]，也不能替代标志蛋白证据。
- [ ] **回收与特异性**：报告样本投入量与各步骤参数；免疫捕获等方法应定量下拉与流穿以评估效率 [1]。
- [ ] **方法报告**：离心报告转子、rpm、时间、温度、加减速 [1]；SEC 报告填料、柱尺寸、上样量、空体积和收集级分 [1]；过滤/TFF 报告膜类型与截留值 [1]。“100,000×g 离心”这种写法无法复现。可将方法上传 EV-TRACK 知识库以提高透明度 [43]。
- [ ] **储存（更正）**：MISEV2023 指出冻融影响的证据不一致，建议避免反复冻融或评估其影响，并报告全部储存参数 [1]。−80 °C 储存会随时间降低 EV 浓度和纯度 [44]；单纯 PBS 中储存或稀释 EV 回收率可大幅下降，含白蛋白和海藻糖的 PBS（PBS-HAT）稳定性更好 [45]。原稿“PBS 分装、冻融 ≤1 次”的硬性规定无统一依据，已改为上述表述。
- [ ] **用词规范**：除非能证明内体来源，不宜称“外泌体（exosome）”，而应使用“EV”或操作性术语 [1]；“小 EV”常被描述为 <200 nm，但并无严格的大小界限共识，测得的直径也取决于表征方法 [1]。

## 本文引用的参考文献

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:[10.1002/jev2.12404](https://doi.org/10.1002/jev2.12404). PMID:[38326288](https://pubmed.ncbi.nlm.nih.gov/38326288/); [PMC10850029](https://pmc.ncbi.nlm.nih.gov/articles/PMC10850029/).

[40] Rikkert LG, Nieuwland R, Terstappen LWMM, Coumans FAW. Quality of extracellular vesicle images by transmission electron microscopy is operator and protocol dependent. J Extracell Vesicles. 2019;8:1555419. doi:[10.1080/20013078.2018.1555419](https://doi.org/10.1080/20013078.2018.1555419). PMID:[30651939](https://pubmed.ncbi.nlm.nih.gov/30651939/); [PMC6327933](https://pmc.ncbi.nlm.nih.gov/articles/PMC6327933/).

[41] Théry C, Witwer KW, Aikawa E, Alcaraz MJ, Anderson JD, Andriantsitohaina R, et al. Minimal information for studies of extracellular vesicles 2018 (MISEV2018): a position statement of the International Society for Extracellular Vesicles and update of the MISEV2014 guidelines. J Extracell Vesicles. 2018;7:1535750. doi:[10.1080/20013078.2018.1535750](https://doi.org/10.1080/20013078.2018.1535750). PMID:[30637094](https://pubmed.ncbi.nlm.nih.gov/30637094/); [PMC6322352](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322352/).

[42] Webber J, Clayton A. How pure are your vesicles?. J Extracell Vesicles. 2013;2:19861. doi:[10.3402/jev.v2i0.19861](https://doi.org/10.3402/jev.v2i0.19861). PMID:[24009896](https://pubmed.ncbi.nlm.nih.gov/24009896/); [PMC3760653](https://pmc.ncbi.nlm.nih.gov/articles/PMC3760653/).

[43] EV-TRACK Consortium; Van Deun J, Mestdagh P, Agostinis P, Akay Ö, Anand S, et al. EV-TRACK: transparent reporting and centralizing knowledge in extracellular vesicle research. Nat Methods. 2017;14:228-232. doi:[10.1038/nmeth.4185](https://doi.org/10.1038/nmeth.4185). PMID:[28245209](https://pubmed.ncbi.nlm.nih.gov/28245209/).

[44] Gelibter S, Marostica G, Mandelli A, Siciliani S, Podini P, Finardi A, et al. The impact of storage on extracellular vesicles: A systematic study. J Extracell Vesicles. 2022;11:e12162. doi:[10.1002/jev2.12162](https://doi.org/10.1002/jev2.12162). PMID:[35102719](https://pubmed.ncbi.nlm.nih.gov/35102719/); [PMC8804350](https://pmc.ncbi.nlm.nih.gov/articles/PMC8804350/).

[45] Görgens A, Corso G, Hagey DW, Jawad Wiklander R, Gustafsson MO, Felldin U, et al. Identification of storage conditions stabilizing extracellular vesicles preparations. J Extracell Vesicles. 2022;11:e12238. doi:[10.1002/jev2.12238](https://doi.org/10.1002/jev2.12238). PMID:[35716060](https://pubmed.ncbi.nlm.nih.gov/35716060/); [PMC9206228](https://pmc.ncbi.nlm.nih.gov/articles/PMC9206228/).
