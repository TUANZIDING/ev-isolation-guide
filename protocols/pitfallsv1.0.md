# 常见坑与排查

> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 [`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>
>
> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

**得率异常**

- **颗粒计数虚高**：血浆中大小在 EV 范围内的颗粒多数缺乏 EV 标志，主要是脂蛋白（以 LDL 为主）[22]；试剂盒颗粒数高但纯度低 [12]。应加做标志蛋白和纯度指标，必要时用 SEC 或密度梯度复核 [17]。
- **得率突然变低**：检查细胞活率与培养条件 [1]、血清批次 [33]、超滤膜吸附 [1]、转子与 k 因子换算 [1,10]。
- **批间波动大**：固定收集窗口、操作者和耗材批次，把每步参数写进批记录【实验室惯例】。

**功能实验假象**

- **“EV 效应”其实来自共分离物**：设置非 EV 级分、EV 去除级分或酶处理级分等对照，判断功能是否 EV 特异 [1]；设未条件化培养基走全流程的对照 [1]。
- **剂量不可比**：以蛋白量作为 EV 剂量需谨慎 [1]；同时报告颗粒数和蛋白量。
- **储存影响活性**：储存条件可改变 EV 浓度、大小和功能相关特性 [44,45]；功能实验优先用新鲜或储存条件已验证的制备。

**一条底线**：提取方法会显著影响 EV 的纯度与组学结果 [2,5]，因此换了方法后，旧方法的剂量—效应关系不能直接平移；新方法上线前用同一批样本做平行比较【实验室惯例】。

## 本文引用的参考文献

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:[10.1002/jev2.12404](https://doi.org/10.1002/jev2.12404). PMID:[38326288](https://pubmed.ncbi.nlm.nih.gov/38326288/); [PMC10850029](https://pmc.ncbi.nlm.nih.gov/articles/PMC10850029/).

[2] Van Deun J, Mestdagh P, Sormunen R, Cocquyt V, Vermaelen K, Vandesompele J, et al. The impact of disparate isolation methods for extracellular vesicles on downstream RNA profiling. J Extracell Vesicles. 2014;3:24858. doi:[10.3402/jev.v3.24858](https://doi.org/10.3402/jev.v3.24858). PMID:[25317274](https://pubmed.ncbi.nlm.nih.gov/25317274/); [PMC4169610](https://pmc.ncbi.nlm.nih.gov/articles/PMC4169610/).

[5] Dong L, Zieren RC, Horie K, Kim CJ, Mallick E, Jing Y, et al. Comprehensive evaluation of methods for small extracellular vesicles separation from human plasma, urine and cell culture medium. J Extracell Vesicles. 2020;10:e12044. doi:[10.1002/jev2.12044](https://doi.org/10.1002/jev2.12044). PMID:[33489012](https://pubmed.ncbi.nlm.nih.gov/33489012/); [PMC7810129](https://pmc.ncbi.nlm.nih.gov/articles/PMC7810129/).

[10] Cvjetkovic A, Lötvall J, Lässer C. The influence of rotor type and centrifugation time on the yield and purity of extracellular vesicles. J Extracell Vesicles. 2014;3:23111. doi:[10.3402/jev.v3.23111](https://doi.org/10.3402/jev.v3.23111). PMID:[24678386](https://pubmed.ncbi.nlm.nih.gov/24678386/); [PMC3967015](https://pmc.ncbi.nlm.nih.gov/articles/PMC3967015/).

[12] Tian Y, Gong M, Hu Y, Liu H, Zhang W, Zhang M, et al. Quality and efficiency assessment of six extracellular vesicle isolation methods by nano-flow cytometry. J Extracell Vesicles. 2020;9:1697028. doi:[10.1080/20013078.2019.1697028](https://doi.org/10.1080/20013078.2019.1697028). PMID:[31839906](https://pubmed.ncbi.nlm.nih.gov/31839906/); [PMC6896440](https://pmc.ncbi.nlm.nih.gov/articles/PMC6896440/).

[17] Karimi N, Cvjetkovic A, Jang SC, Crescitelli R, Hosseinpour Feizi MA, Nieuwland R, et al. Detailed analysis of the plasma extracellular vesicle proteome after separation from lipoproteins. Cell Mol Life Sci. 2018;75:2873-2886. doi:[10.1007/s00018-018-2773-4](https://doi.org/10.1007/s00018-018-2773-4). PMID:[29441425](https://pubmed.ncbi.nlm.nih.gov/29441425/); [PMC6021463](https://pmc.ncbi.nlm.nih.gov/articles/PMC6021463/).

[22] Sódar BW, Kittel Á, Pálóczi K, Vukman KV, Osteikoetxea X, Szabó-Taylor K, et al. Low-density lipoprotein mimics blood plasma-derived exosomes and microvesicles during isolation and detection. Sci Rep. 2016;6:24316. doi:[10.1038/srep24316](https://doi.org/10.1038/srep24316). PMID:[27087061](https://pubmed.ncbi.nlm.nih.gov/27087061/); [PMC4834552](https://pmc.ncbi.nlm.nih.gov/articles/PMC4834552/).

[33] Lehrich BM, Liang Y, Khosravi P, Federoff HJ, Fiandaca MS. Fetal Bovine Serum-Derived Extracellular Vesicles Persist within Vesicle-Depleted Culture Media. Int J Mol Sci. 2018;19:3538. doi:[10.3390/ijms19113538](https://doi.org/10.3390/ijms19113538). PMID:[30423996](https://pubmed.ncbi.nlm.nih.gov/30423996/); [PMC6275013](https://pmc.ncbi.nlm.nih.gov/articles/PMC6275013/).

[44] Gelibter S, Marostica G, Mandelli A, Siciliani S, Podini P, Finardi A, et al. The impact of storage on extracellular vesicles: A systematic study. J Extracell Vesicles. 2022;11:e12162. doi:[10.1002/jev2.12162](https://doi.org/10.1002/jev2.12162). PMID:[35102719](https://pubmed.ncbi.nlm.nih.gov/35102719/); [PMC8804350](https://pmc.ncbi.nlm.nih.gov/articles/PMC8804350/).

[45] Görgens A, Corso G, Hagey DW, Jawad Wiklander R, Gustafsson MO, Felldin U, et al. Identification of storage conditions stabilizing extracellular vesicles preparations. J Extracell Vesicles. 2022;11:e12238. doi:[10.1002/jev2.12238](https://doi.org/10.1002/jev2.12238). PMID:[35716060](https://pubmed.ncbi.nlm.nih.gov/35716060/); [PMC9206228](https://pmc.ncbi.nlm.nih.gov/articles/PMC9206228/).
