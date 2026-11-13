# 方法 1：差速超速离心（dUC）· 最常用的参照方法

> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 [`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>
>
> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

按“分离原理”理解每种方法，才能判断它会共分离什么、损失或损伤什么 [1]。


**原理**：按沉降系数逐级离心——低速去细胞和碎片，中速去较大颗粒，高速沉淀较小 EV；沉降系数与颗粒大小和密度相关 [1]。

**典型参数**：最常引用的方案为 300×g 10 min → 2,000×g 10 min → 10,000×g 30 min → 100,000×g 70 min，沉淀重悬后再以 100,000×g 洗涤一次 [8,9]。文献中沉淀小 EV 的条件通常为约 100,000–200,000×g、45–150 min [1]。必须报告转子型号、转速（rpm）、时间、温度及加减速设置，以便计算校正 k 因子并换算到其他转子 [1]；转子类型、g 值和离心时间都会显著影响得率与纯度 [9,10]。

**优点**：不需额外试剂，是使用最广泛的方法（2015 年 ISEV 调查中 81% 受访者使用），因而文献可比性最好 [6]。

**局限**：高速、长时间离心会共分离沉降系数相近的非囊泡颗粒，并可能诱导 EV 聚集 [1,11]。回收率偏低：一项用纳米流式评估血浆的研究估算，单次 100,000×g 2 h 回收约 40%，两次超离约 16% [12]；重复超离会降低得率 [13]。（原稿“约 5%–40%”的下限无文献支持，已改写。）

**优化要点**：0.22 µm 过滤可去除较大颗粒，但也会把大 EV 截留在滤器上，并需注意挤压造成的人为颗粒，须在方法中声明 [1]。黏性体液中颗粒回收率与黏度成反比，应考虑先稀释再超离 [14]。沉淀轻柔重悬、避免反复吹打【实验室惯例】。

**定性评分**（领域定性共识，见“横向对比”说明）：纯度 3/5 · 得率 3/5 · 通量 2/5。

## 本文引用的参考文献

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:[10.1002/jev2.12404](https://doi.org/10.1002/jev2.12404). PMID:[38326288](https://pubmed.ncbi.nlm.nih.gov/38326288/); [PMC10850029](https://pmc.ncbi.nlm.nih.gov/articles/PMC10850029/).

[6] Gardiner C, Di Vizio D, Sahoo S, Théry C, Witwer KW, Wauben M, et al. Techniques used for the isolation and characterization of extracellular vesicles: results of a worldwide survey. J Extracell Vesicles. 2016;5:32945. doi:[10.3402/jev.v5.32945](https://doi.org/10.3402/jev.v5.32945). PMID:[27802845](https://pubmed.ncbi.nlm.nih.gov/27802845/); [PMC5090131](https://pmc.ncbi.nlm.nih.gov/articles/PMC5090131/).

[8] Théry C, Amigorena S, Raposo G, Clayton A. Isolation and characterization of exosomes from cell culture supernatants and biological fluids. Curr Protoc Cell Biol. 2006;30:Unit 3.22. doi:[10.1002/0471143030.cb0322s30](https://doi.org/10.1002/0471143030.cb0322s30). PMID:[18228490](https://pubmed.ncbi.nlm.nih.gov/18228490/).

[9] Livshits MA, Khomyakova E, Evtushenko EG, Lazarev VN, Kulemin NA, Semina SE, et al. Isolation of exosomes by differential centrifugation: Theoretical analysis of a commonly used protocol. Sci Rep. 2015;5:17319. doi:[10.1038/srep17319](https://doi.org/10.1038/srep17319). PMID:[26616523](https://pubmed.ncbi.nlm.nih.gov/26616523/); [PMC4663484](https://pmc.ncbi.nlm.nih.gov/articles/PMC4663484/).

[10] Cvjetkovic A, Lötvall J, Lässer C. The influence of rotor type and centrifugation time on the yield and purity of extracellular vesicles. J Extracell Vesicles. 2014;3:23111. doi:[10.3402/jev.v3.23111](https://doi.org/10.3402/jev.v3.23111). PMID:[24678386](https://pubmed.ncbi.nlm.nih.gov/24678386/); [PMC3967015](https://pmc.ncbi.nlm.nih.gov/articles/PMC3967015/).

[11] Linares R, Tan S, Gounou C, Arraud N, Brisson AR. High-speed centrifugation induces aggregation of extracellular vesicles. J Extracell Vesicles. 2015;4:29509. doi:[10.3402/jev.v4.29509](https://doi.org/10.3402/jev.v4.29509). PMID:[26700615](https://pubmed.ncbi.nlm.nih.gov/26700615/); [PMC4689953](https://pmc.ncbi.nlm.nih.gov/articles/PMC4689953/).

[12] Tian Y, Gong M, Hu Y, Liu H, Zhang W, Zhang M, et al. Quality and efficiency assessment of six extracellular vesicle isolation methods by nano-flow cytometry. J Extracell Vesicles. 2020;9:1697028. doi:[10.1080/20013078.2019.1697028](https://doi.org/10.1080/20013078.2019.1697028). PMID:[31839906](https://pubmed.ncbi.nlm.nih.gov/31839906/); [PMC6896440](https://pmc.ncbi.nlm.nih.gov/articles/PMC6896440/).

[13] Lobb RJ, Becker M, Wen SW, Wong CS, Wiegmans AP, Leimgruber A, et al. Optimized exosome isolation protocol for cell culture supernatant and human plasma. J Extracell Vesicles. 2015;4:27031. doi:[10.3402/jev.v4.27031](https://doi.org/10.3402/jev.v4.27031). PMID:[26194179](https://pubmed.ncbi.nlm.nih.gov/26194179/); [PMC4507751](https://pmc.ncbi.nlm.nih.gov/articles/PMC4507751/).

[14] Momen-Heravi F, Balaj L, Alian S, Trachtenberg AJ, Hochberg FH, Skog J, et al. Impact of biofluid viscosity on size and sedimentation efficiency of the isolated microvesicles. Front Physiol. 2012;3:162. doi:[10.3389/fphys.2012.00162](https://doi.org/10.3389/fphys.2012.00162). PMID:[22661955](https://pubmed.ncbi.nlm.nih.gov/22661955/); [PMC3362089](https://pmc.ncbi.nlm.nih.gov/articles/PMC3362089/).
