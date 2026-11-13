# 分样本优化要点

> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 [`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>
>
> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

| 样本 | 主要干扰物 | 推荐路线 | 关键优化 |
|---|---|---|---|
| 细胞上清 | 血清来源 EV 与蛋白、死亡细胞来源颗粒 [1,32] | TFF/超滤 + SEC 或 dUC（± SEC/密度梯度）[2,3,4] | 去 EV 血清（验证残留）或无血清窗口；报告活率；设未条件化培养基对照 [1,33] |
| 血浆 | 血小板、脂蛋白、溶血产物、可溶/聚集蛋白 [1,34] | SEC（需去脂蛋白时联合密度分离）；避免单用沉淀法 [17,19] | 空腹采血（降低乳糜微粒）；粗针头减少血小板活化与溶血；尽快处理 [1]；ISTH 方案：采血后 <2 h 内、室温 2,500×g 15 min 离心两次（不用刹车）制备无血小板血浆 [35]；量化残余血小板 [36]；填写 MIBlood-EV [1,34] |
| 血清 | 凝血过程中血小板释放的 EV（可占血清 EV 的 50% 以上）[37] | 同血浆；EV 循环研究优先用血浆 [37] | 报告促凝剂与凝血时间 [34]；血清与血浆数据不可直接混用 [37] |
| 尿液 | Tamm–Horsfall 蛋白（尿调蛋白）聚合网罗 EV 并共分离；尿蛋白 [1] | 超滤浓缩 + SEC；或还原剂处理后 dUC [1,38,39] | DTT 等还原剂可解聚 THP 网络、释放 EV [38]，但也有报告得率改善有限 [39]，处理方式需写入方法；归一化尚无共识，可用计时尿排泄率或按渗透压/肌酐近似 [1,39] |
| 脑脊液 / 唾液等 | 总量低；黏液（唾液） | 超滤浓缩 + SEC；或免疫捕获【实验室惯例】 | 全程使用低吸附耗材【实验室惯例】；唾液先离心去黏液层并记录收集方式【实验室惯例】 |
| 组织 / 类器官 | 细胞与细胞碎片伪影 [1] | 依样本选择 | 重点追踪应在 EV 中被耗竭的细胞组分 [1] |

## 本文引用的参考文献

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:[10.1002/jev2.12404](https://doi.org/10.1002/jev2.12404). PMID:[38326288](https://pubmed.ncbi.nlm.nih.gov/38326288/); [PMC10850029](https://pmc.ncbi.nlm.nih.gov/articles/PMC10850029/).

[2] Van Deun J, Mestdagh P, Sormunen R, Cocquyt V, Vermaelen K, Vandesompele J, et al. The impact of disparate isolation methods for extracellular vesicles on downstream RNA profiling. J Extracell Vesicles. 2014;3:24858. doi:[10.3402/jev.v3.24858](https://doi.org/10.3402/jev.v3.24858). PMID:[25317274](https://pubmed.ncbi.nlm.nih.gov/25317274/); [PMC4169610](https://pmc.ncbi.nlm.nih.gov/articles/PMC4169610/).

[3] Nordin JZ, Lee Y, Vader P, Mäger I, Johansson HJ, Heusermann W, et al. Ultrafiltration with size-exclusion liquid chromatography for high yield isolation of extracellular vesicles preserving intact biophysical and functional properties. Nanomedicine. 2015;11:879-883. doi:[10.1016/j.nano.2015.01.003](https://doi.org/10.1016/j.nano.2015.01.003). PMID:[25659648](https://pubmed.ncbi.nlm.nih.gov/25659648/).

[4] Busatto S, Vilanilam G, Ticer T, Lin WL, Dickson DW, Shapiro S, et al. Tangential Flow Filtration for Highly Efficient Concentration of Extracellular Vesicles from Large Volumes of Fluid. Cells. 2018;7:273. doi:[10.3390/cells7120273](https://doi.org/10.3390/cells7120273). PMID:[30558352](https://pubmed.ncbi.nlm.nih.gov/30558352/); [PMC6315734](https://pmc.ncbi.nlm.nih.gov/articles/PMC6315734/).

[17] Karimi N, Cvjetkovic A, Jang SC, Crescitelli R, Hosseinpour Feizi MA, Nieuwland R, et al. Detailed analysis of the plasma extracellular vesicle proteome after separation from lipoproteins. Cell Mol Life Sci. 2018;75:2873-2886. doi:[10.1007/s00018-018-2773-4](https://doi.org/10.1007/s00018-018-2773-4). PMID:[29441425](https://pubmed.ncbi.nlm.nih.gov/29441425/); [PMC6021463](https://pmc.ncbi.nlm.nih.gov/articles/PMC6021463/).

[19] Gámez-Valero A, Monguió-Tortajada M, Carreras-Planella L, Franquesa Ml, Beyer K, Borràs FE. Size-Exclusion Chromatography-based isolation minimally alters Extracellular Vesicles' characteristics compared to precipitating agents. Sci Rep. 2016;6:33641. doi:[10.1038/srep33641](https://doi.org/10.1038/srep33641). PMID:[27640641](https://pubmed.ncbi.nlm.nih.gov/27640641/); [PMC5027519](https://pmc.ncbi.nlm.nih.gov/articles/PMC5027519/).

[32] Shelke GV, Lässer C, Gho YS, Lötvall J. Importance of exosome depletion protocols to eliminate functional and RNA-containing extracellular vesicles from fetal bovine serum. J Extracell Vesicles. 2014;3:24783. doi:[10.3402/jev.v3.24783](https://doi.org/10.3402/jev.v3.24783). PMID:[25317276](https://pubmed.ncbi.nlm.nih.gov/25317276/); [PMC4185091](https://pmc.ncbi.nlm.nih.gov/articles/PMC4185091/).

[33] Lehrich BM, Liang Y, Khosravi P, Federoff HJ, Fiandaca MS. Fetal Bovine Serum-Derived Extracellular Vesicles Persist within Vesicle-Depleted Culture Media. Int J Mol Sci. 2018;19:3538. doi:[10.3390/ijms19113538](https://doi.org/10.3390/ijms19113538). PMID:[30423996](https://pubmed.ncbi.nlm.nih.gov/30423996/); [PMC6275013](https://pmc.ncbi.nlm.nih.gov/articles/PMC6275013/).

[34] Lucien F, Gustafson D, Lenassi M, Li B, Teske JJ, Boilard E, et al. MIBlood-EV: Minimal information to enhance the quality and reproducibility of blood extracellular vesicle research. J Extracell Vesicles. 2023;12:12385. doi:[10.1002/jev2.12385](https://doi.org/10.1002/jev2.12385). PMID:[38063210](https://pubmed.ncbi.nlm.nih.gov/38063210/); [PMC10704543](https://pmc.ncbi.nlm.nih.gov/articles/PMC10704543/).

[35] Lacroix R, Judicone C, Mooberry M, Boucekine M, Key NS, Dignat-George F. Standardization of pre-analytical variables in plasma microparticle determination: results of the International Society on Thrombosis and Haemostasis SSC Collaborative workshop. J Thromb Haemost. 2013;11:1190-1193. doi:[10.1111/jth.12207](https://doi.org/10.1111/jth.12207). PMID:[23551930](https://pubmed.ncbi.nlm.nih.gov/23551930/); [PMC4395506](https://pmc.ncbi.nlm.nih.gov/articles/PMC4395506/).

[36] Clayton A, Boilard E, Buzas EI, Cheng L, Falcón-Perez JM, Gardiner C, et al. Considerations towards a roadmap for collection, handling and storage of blood extracellular vesicles. J Extracell Vesicles. 2019;8:1647027. doi:[10.1080/20013078.2019.1647027](https://doi.org/10.1080/20013078.2019.1647027). PMID:[31489143](https://pubmed.ncbi.nlm.nih.gov/31489143/); [PMC6711123](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711123/).

[37] Witwer KW, Buzás EI, Bemis LT, Bora A, Lässer C, Lötvall J, et al. Standardization of sample collection, isolation and analysis methods in extracellular vesicle research. J Extracell Vesicles. 2013;2:20360. doi:[10.3402/jev.v2i0.20360](https://doi.org/10.3402/jev.v2i0.20360). PMID:[24009894](https://pubmed.ncbi.nlm.nih.gov/24009894/); [PMC3760646](https://pmc.ncbi.nlm.nih.gov/articles/PMC3760646/).

[38] Fernández-Llama P, Khositseth S, Gonzales PA, Star RA, Pisitkun T, Knepper MA. Tamm-Horsfall protein and urinary exosome isolation. Kidney Int. 2010;77:736-742. doi:[10.1038/ki.2009.550](https://doi.org/10.1038/ki.2009.550). PMID:[20130532](https://pubmed.ncbi.nlm.nih.gov/20130532/); [PMC3398710](https://pmc.ncbi.nlm.nih.gov/articles/PMC3398710/).

[39] Erdbrügger U, Blijdorp CJ, Bijnsdorp IV, Borràs FE, Burger D, Bussolati B, et al. Urinary extracellular vesicles: A position paper by the Urine Task Force of the International Society for Extracellular Vesicles. J Extracell Vesicles. 2021;10:e12093. doi:[10.1002/jev2.12093](https://doi.org/10.1002/jev2.12093). PMID:[34035881](https://pubmed.ncbi.nlm.nih.gov/34035881/); [PMC8138533](https://pmc.ncbi.nlm.nih.gov/articles/PMC8138533/).
