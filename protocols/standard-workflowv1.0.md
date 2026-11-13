# 标准工作流程（以细胞培养上清为例）

> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 [`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>
>
> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

样本质量在收集时就决定了上限：MISEV2023 建议尽早去除细胞，因为细胞破碎会形成类似 EV 的颗粒 [1]。

1. **收集与前处理**：胎牛血清（FBS）含大量 EV，可改变受体细胞表型；18 h 超离（120,000×g）可去除约 95% 含 RNA 的 FBS EV，1.5 h 不够 [32]；也有研究用 100,000×g 18 h [2]。但无论自制还是商品化“去 EV 血清”都会残留 EV，需验证 [1,33]；超离去除效果可能取决于稀释程度 [1]。也可用无血清/限定培养基窗口，但去 EV 血清和无血清培养都可能改变细胞生理和 EV 产生 [1]。应报告细胞身份、接种和收获密度、收获时活率及传代数 [1]。少数死亡细胞产生的 EV 就可能超过健康细胞产生的 EV，因此活率直接影响 EV 亚型构成和数量 [1]；具体活率阈值（如 >90%）无统一标准，属【实验室惯例】。收集窗口 24–48 h 为常见做法【实验室惯例】。
2. **梯度预澄清**：300×g 去细胞 → 2,000×g 去碎片 → 10,000×g 去较大颗粒 [8,9]；全程 4 °C【实验室惯例】。若当天处理不了，应先去除细胞再冻存上清，并报告冻存温度、时长和冻融次数 [1]。
3. **浓缩**：按体积选择——小体积用超滤管或直接 dUC，大体积（如数百毫升以上）用 TFF [4,13]；具体体积分界（如 <30 mL / ≥100 mL）为【实验室惯例】。
4. **纯化与换液**：SEC / 密度梯度 / 免疫捕获按用途选一 [1]；最终换液到实验所需缓冲液，必要时再浓缩。
5. **表征与储存**：测颗粒浓度与粒径、总蛋白，并分别报告绝对颗粒数和蛋白量 [1]；做蛋白标志检测 [1]。分装储存并报告全部储存参数 [1]（储存缓冲液选择见质控清单）。

## 本文引用的参考文献

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:[10.1002/jev2.12404](https://doi.org/10.1002/jev2.12404). PMID:[38326288](https://pubmed.ncbi.nlm.nih.gov/38326288/); [PMC10850029](https://pmc.ncbi.nlm.nih.gov/articles/PMC10850029/).

[2] Van Deun J, Mestdagh P, Sormunen R, Cocquyt V, Vermaelen K, Vandesompele J, et al. The impact of disparate isolation methods for extracellular vesicles on downstream RNA profiling. J Extracell Vesicles. 2014;3:24858. doi:[10.3402/jev.v3.24858](https://doi.org/10.3402/jev.v3.24858). PMID:[25317274](https://pubmed.ncbi.nlm.nih.gov/25317274/); [PMC4169610](https://pmc.ncbi.nlm.nih.gov/articles/PMC4169610/).

[4] Busatto S, Vilanilam G, Ticer T, Lin WL, Dickson DW, Shapiro S, et al. Tangential Flow Filtration for Highly Efficient Concentration of Extracellular Vesicles from Large Volumes of Fluid. Cells. 2018;7:273. doi:[10.3390/cells7120273](https://doi.org/10.3390/cells7120273). PMID:[30558352](https://pubmed.ncbi.nlm.nih.gov/30558352/); [PMC6315734](https://pmc.ncbi.nlm.nih.gov/articles/PMC6315734/).

[8] Théry C, Amigorena S, Raposo G, Clayton A. Isolation and characterization of exosomes from cell culture supernatants and biological fluids. Curr Protoc Cell Biol. 2006;30:Unit 3.22. doi:[10.1002/0471143030.cb0322s30](https://doi.org/10.1002/0471143030.cb0322s30). PMID:[18228490](https://pubmed.ncbi.nlm.nih.gov/18228490/).

[9] Livshits MA, Khomyakova E, Evtushenko EG, Lazarev VN, Kulemin NA, Semina SE, et al. Isolation of exosomes by differential centrifugation: Theoretical analysis of a commonly used protocol. Sci Rep. 2015;5:17319. doi:[10.1038/srep17319](https://doi.org/10.1038/srep17319). PMID:[26616523](https://pubmed.ncbi.nlm.nih.gov/26616523/); [PMC4663484](https://pmc.ncbi.nlm.nih.gov/articles/PMC4663484/).

[13] Lobb RJ, Becker M, Wen SW, Wong CS, Wiegmans AP, Leimgruber A, et al. Optimized exosome isolation protocol for cell culture supernatant and human plasma. J Extracell Vesicles. 2015;4:27031. doi:[10.3402/jev.v4.27031](https://doi.org/10.3402/jev.v4.27031). PMID:[26194179](https://pubmed.ncbi.nlm.nih.gov/26194179/); [PMC4507751](https://pmc.ncbi.nlm.nih.gov/articles/PMC4507751/).

[32] Shelke GV, Lässer C, Gho YS, Lötvall J. Importance of exosome depletion protocols to eliminate functional and RNA-containing extracellular vesicles from fetal bovine serum. J Extracell Vesicles. 2014;3:24783. doi:[10.3402/jev.v3.24783](https://doi.org/10.3402/jev.v3.24783). PMID:[25317276](https://pubmed.ncbi.nlm.nih.gov/25317276/); [PMC4185091](https://pmc.ncbi.nlm.nih.gov/articles/PMC4185091/).

[33] Lehrich BM, Liang Y, Khosravi P, Federoff HJ, Fiandaca MS. Fetal Bovine Serum-Derived Extracellular Vesicles Persist within Vesicle-Depleted Culture Media. Int J Mol Sci. 2018;19:3538. doi:[10.3390/ijms19113538](https://doi.org/10.3390/ijms19113538). PMID:[30423996](https://pubmed.ncbi.nlm.nih.gov/30423996/); [PMC6275013](https://pmc.ncbi.nlm.nih.gov/articles/PMC6275013/).
