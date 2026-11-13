# 细胞外囊泡提取方法与优化指南

方法学指南 · 依据 MISEV2023 及原始研究文献 · 最后核验：2026-11-13

> **声明**：本页为方法学参考与文献综述，不构成针对任何具体课题的实验方案或结论。文中参数为已发表研究或国际细胞外囊泡学会（ISEV）指南中的报告值或常见范围，具体数值以所用仪器、转子和商品化产品说明书为准，正式实验前应在本实验室样本上小试验证。用于正式研究时，提取方案与质控标准建议预先写入研究方案或预注册。凡标注“【实验室惯例】”或“【估算】”的内容，没有直接的文献测定值支持，仅供参考。

没有一种提取方法在所有样本和用途上都“最好”：各方法在回收率（得率）与特异性（纯度）之间位置不同，组合使用可提高特异性 [1]。因此，先定下游用途，再选方法，最后用表征数据证明你得到的是 EV [1]。

## 三条核心信息

**① 先定用途，再选方法。** MISEV2023 不强制要求或禁止任何技术或标志物，强调所选技术应“适合目的”（fit for purpose）并完整报告 [1]。组学研究对共分离物最敏感，提取方法会显著影响组学结果 [2]；功能和转化研究则更看重活性保持与可放大性 [3,4]。

**② 单一方法常常不够。** 由于 EV 与多种非囊泡颗粒（NVEP）在大小、密度上重叠，按不同物理/生化性质依次组合的分离策略越来越常用，可提高特异性 [1]；一项多样本比较研究未发现任何方法能得到 100% 纯的 EV [5]。2015 年 ISEV 全球调查中，59% 的受访者组合使用多种方法 [6]。

**③ 报告与表征同等重要。** 按 MISEV2023 报告来源、预处理、分离和储存的全部参数，并用多类互补证据（颗粒数量与大小、形貌、蛋白标志、纯度指标）表征 EV [1]。

## 方案推荐器（逻辑说明）

按“样本来源 × 下游用途 × 优先指标”给出起点方案，规则与依据见 `recommender-rulesv1.0.json`。推荐逻辑基于 MISEV2023 及各方法已发表的性能比较 [1,5,7]，只是起点，仍需用自己的样本小试验证。

## 七种主流方法详解

按“分离原理”理解每种方法，才能判断它会共分离什么、损失或损伤什么 [1]。

### 1. 差速超速离心（dUC）· 最常用的参照方法

**原理**：按沉降系数逐级离心——低速去细胞和碎片，中速去较大颗粒，高速沉淀较小 EV；沉降系数与颗粒大小和密度相关 [1]。

**典型参数**：最常引用的方案为 300×g 10 min → 2,000×g 10 min → 10,000×g 30 min → 100,000×g 70 min，沉淀重悬后再以 100,000×g 洗涤一次 [8,9]。文献中沉淀小 EV 的条件通常为约 100,000–200,000×g、45–150 min [1]。必须报告转子型号、转速（rpm）、时间、温度及加减速设置，以便计算校正 k 因子并换算到其他转子 [1]；转子类型、g 值和离心时间都会显著影响得率与纯度 [9,10]。

**优点**：不需额外试剂，是使用最广泛的方法（2015 年 ISEV 调查中 81% 受访者使用），因而文献可比性最好 [6]。

**局限**：高速、长时间离心会共分离沉降系数相近的非囊泡颗粒，并可能诱导 EV 聚集 [1,11]。回收率偏低：一项用纳米流式评估血浆的研究估算，单次 100,000×g 2 h 回收约 40%，两次超离约 16% [12]；重复超离会降低得率 [13]。（原稿“约 5%–40%”的下限无文献支持，已改写。）

**优化要点**：0.22 µm 过滤可去除较大颗粒，但也会把大 EV 截留在滤器上，并需注意挤压造成的人为颗粒，须在方法中声明 [1]。黏性体液中颗粒回收率与黏度成反比，应考虑先稀释再超离 [14]。沉淀轻柔重悬、避免反复吹打【实验室惯例】。

**定性评分**（领域定性共识，见“横向对比”说明）：纯度 3/5 · 得率 3/5 · 通量 2/5。

### 2. 密度梯度离心（DGUC）· 纯度上限高

**原理**：在碘克沙醇（OptiPrep）或蔗糖梯度中按浮力密度分离 [1]。EV 的浮力密度范围常引用为约 1.08–1.19 g/mL [7,9]；在碘克沙醇梯度中实测的 EV 富集段例如约 1.094 g/mL [2] 或 1.10–1.15 g/mL [5]（不同梯度介质与样本有差异）。DGUC 能把 EV 与可溶性蛋白及非囊泡组分分开 [2,15]，并与较低密度的脂蛋白（VLDL、LDL、乳糜微粒）分开；但 **HDL 的密度（1.063–1.21 g/mL）与 EV 重叠，单靠密度梯度无法去除** [1,16]。

**典型参数**：常在 dUC 粗提后上样。例如碘克沙醇梯度 100,000×g、4 °C 离心 18 h [2]；分段收集后用吸光度标准曲线或折光率确定各段密度 [1,2]。

**优点**：比单纯超离和沉淀法纯度更高，适合组学与标志物研究 [2,15]。与蔗糖不同，碘克沙醇在各密度下都可配成等渗溶液，更好地保持囊泡大小 [2]。

**局限**：耗时长、操作门槛高；下游分析前通常必须去除梯度介质（稀释后再超离或用 SEC），且梯度加洗涤后的回收率相对较低 [1]。

**优化要点**：优先选碘克沙醇 [2]；收集后换液去除介质 [1]；血液样本若需同时去除 HDL，与 SEC 组合 [1,17]。

**定性评分**：纯度 5/5 · 得率 2/5 · 通量 1/5。

### 3. 尺寸排阻色谱（SEC）· 温和，保功能

**原理**：大颗粒不进入填料孔隙，先流出（早期级分）；比孔径小的颗粒和游离蛋白滞留更久、在后期级分流出 [1]。

**典型参数**：柱可自装或购买商品化柱，商品柱装填条件受控，可能重复性更好 [1]。必须逐段表征以确定 EV 和杂质所在级分 [1]。例如 Sepharose CL-2B 柱处理血小板来源样本时，EV 主要在第 9–12 级分 [18]。应报告填料与孔径、柱尺寸、上样量、空体积、收集级分数与体积，柱重复使用时报告再生方法和使用次数 [1]。

**优点**：在血小板来源样本中，EV 富集级分仅含 <5% 的 HDL 和 <1% 的蛋白 [18]；在血浆中，SEC 去除了大部分可溶性蛋白，而 PEG 不能 [19]。与超离相比，超滤联合 SEC 得到的 EV 得率更高、生物物理性质保存更好 [3]；在一项心肌祖细胞 EV 研究中，SEC-EV 的体外功能读出高于超离 EV [20]。

**局限**：SEC 只按大小分离，与 EV 大小相近的较大脂蛋白颗粒会共洗脱（MISEV2023 指出除 HDL 外的脂蛋白与 EV 大小重叠）[1]；血浆 SEC 的 EV 级分含脂蛋白颗粒 [17]、ApoB⁺ 脂蛋白 [21]，LDL 可模拟 EV 并与之共纯化 [22]。SEC 会稀释样本，常需在前或后浓缩 [1]。

**优化要点**：大体积样本先超滤/TFF 浓缩再上柱 [3,23]；逐段检测、不要盲目合并级分 [1]；需要去除脂蛋白时联合密度分离 [17]。

**定性评分**：纯度 4/5 · 得率 4/5 · 通量 3/5。

### 4. 超滤与切向流过滤（UF / TFF）· 浓缩利器

**原理**：按膜截留分离与浓缩。死端过滤中较大颗粒易堵塞膜孔；TFF 中液流平行于膜面，避免滤饼形成，可连续处理大体积 [1,4]。

**典型参数**：文献中所用截留值差异较大，例如离心超滤 100 kDa [13]、10 kDa 离心超滤后接 SEC [23]、TFF 中空纤维 500 kDa（前接 0.65 µm 预过滤）[4]。应报告膜类型、截留值等参数 [1]；跨膜压、流速与换液（diafiltration）的具体设置以设备说明为准【实验室惯例】。

**优点**：与超离相比，TFF 浓缩细胞培养基的 EV 得率更高、单分子和聚集体更少、批间一致性更好，处理时间约 1 h，且可放大 [4]；在间充质干细胞 3D 培养中，TFF 使外泌体得率比超离高 7 倍 [24]。

**局限**：浓缩不等于纯化——产物所含非囊泡颗粒和蛋白的量取决于方法和截留值 [1]；不同滤膜对 EV 的吸附（“粘附”）程度不同，影响回收 [1]；浓缩器件的选择可显著影响得率 [13]。

**优化要点**：把 UF/TFF 定位为“浓缩步”，随后接 SEC 或密度梯度纯化 [1,3,23]；预过滤防堵 [4]；回收时少量缓冲液润洗膜面【实验室惯例】。

**定性评分**：纯度 2/5 · 得率 4/5 · 通量 5/5。

### 5. 聚合物沉淀（PEG 等试剂盒）· 方便但特异性最低

**原理**：聚合物“挤出”水分子、降低生物分子溶剂可及性，使包括 EV 在内的颗粒能被低速离心沉淀；许多所谓“外泌体提取试剂盒”即基于此原理，并不真正“分离” EV [1]。

**典型参数**：例如 ExtraPEG 方案：加入 PEG 后 4 °C 孵育过夜（≥12 h），台式离心机 3,214×g 离心 1 h，再加一步小体积超离纯化 [25]。商品试剂盒按说明书操作。

**优点**：不依赖超离机、操作简便、成本低，可处理大体积 [25]。

**局限**：沉淀法可能达不到明显的颗粒分离效果 [1]；血浆中 PEG 未能去除大量可溶性蛋白，且影响 EV 标志物检测 [19]；在纯度和组学结果上不如密度梯度 [2]。试剂盒得到的“颗粒数”可比超离高 2–4 个数量级，但纯度低得多——高颗粒数不等于高 EV 得率 [12]。

**优化要点**：仅建议用于探索性筛查，或后续仍有纯化步骤时使用 [1]；用于组学/功能结论前加一步 SEC 等纯化，并如实报告【实验室惯例，依据上述局限】。

**定性评分**：纯度 1/5 · 颗粒回收 5/5（非 EV 特异）· 通量 4/5。

### 6. 免疫亲和捕获 · 亚群富集专用

**原理**：用抗体（如抗 CD63、CD81、CD9 或目标抗原）捕获暴露该决定簇的 EV 亚群 [1,26]。

**典型参数**：可先按沉降速度分离再进行免疫分离 [26]。应报告亲和探针、基质、孵育时间、洗涤和洗脱条件，并定量下拉与流穿中的物质以评估效率与选择性 [1]。

**优点**：对目标标志阳性 EV 的富集能力强；在一项结肠癌细胞系比较中，EpCAM 免疫捕获的外泌体标志蛋白富集高于超离和密度梯度 [27]。

**局限**：只得到暴露该决定簇的颗粒（包括同样暴露它的非囊泡颗粒），结果不能代表全部 EV；例如尿液中用 CD9 或 CD63 捕获会遗漏近端肾单位来源的 EV [1]。抗体难以与 EV 分离，经典低 pH 洗脱很可能影响 EV 结构，蛋白酶处理也可能消化 EV 表面蛋白 [1]。

**优化要点**：明确报告捕获抗原并声明“亚群”属性 [1]；若下游是检测读出，可在珠上直接检测【实验室惯例】；用于功能实验需谨慎，因为 EV 表面被结合分子修饰 [1]。

**定性评分**：特异性（针对目标亚群）4/5 · 得率 1/5 · 通量 2/5。

### 7. 微流控与非对称流场流分离（AF4 等）· 分析级

**原理**：微流控平台整合多种基于大小、电荷或亲和的分离与检测方式 [28,29]。AF4 在无固定相的薄通道中按流体力学尺寸分离颗粒 [1]。

**典型参数**：依平台而定。AF4 曾分出大外泌体（90–120 nm）、小外泌体（60–80 nm）和无膜纳米颗粒“exomere”（约 35 nm）[30]。**更正**：supermere 并非用 AF4 分出，而是将 exomere 沉淀后的上清再以 367,000×g 超离获得 [31]。

**优点**：流场类方法无固定相、颗粒回收高，属最温和的分离方法之一；AF4 能精确分开大小差异小的颗粒群 [1]。

**局限**：AF4 标准配置并不对 EV 特异，也不是制备型技术 [1]；某些微流控装置得率高，但当输入样本中非 EV 颗粒多时可能共分离杂质 [5]。设备与方法学标准化程度较低【作者判断】。

**优化要点**：定位为分析与亚群研究工具，不作为常规制备主力 [1]；报告芯片/通道与运行参数以便复现 [1]。

**定性评分**：纯度 3/5（按尺寸分辨率高但非 EV 特异）· 回收 3/5（回收高但处理量小）· 通量/制备量 1/5。

## 推荐的组合思路

### 为什么常用“两步法”

每一步通常只按一种性质分离（沉降、密度、尺寸、电荷/抗原），而杂质往往在某一维度上与 EV 重叠；按不同性质依次组合可提高特异性 [1]。

- **浓缩步解决体积问题**：TFF / 超滤 / 离心 [1]。
- **纯化步解决杂质问题**：SEC 去可溶蛋白和 HDL [18]；密度梯度去除与 EV 大小重叠但密度不同的脂蛋白（VLDL、LDL、乳糜微粒）[1,17]；免疫捕获选择亚群 [26]。
- **功能实验（细胞/动物给药）**：超滤/TFF 浓缩 + SEC 是有文献支持的、兼顾得率与生物物理性质的组合 [3,4,23]。
- **组学与标志物**：dUC + 密度梯度 [2,15]，或 SEC 与密度分离联用（血液样本）[17]，纯度优先、得率让步。

## 横向对比速查

> 评分为基于所引比较研究和 MISEV2023 方法学描述的**定性共识**（同一样本类型内比较），不是测量值；实际表现随样本与操作波动很大——把它当选型地图，不要当绝对指标 [1,5,7,12]。“耗时”一栏为根据所引方案离心/运行时间加上操作时间的【估算】。

| 方法 | 纯度 | 得率 | 耗时【估算】 | 最适合 | 主要依据 |
|---|---|---|---|---|---|
| 差速超速离心 dUC | 中 | 中（血浆研究：单次约 40%，两次约 16%） | 约 4–5 h（离心合计约 3 h 10 min） | 常规制备、文献对照 | [6,8,9,12] |
| 密度梯度 DGUC | 最高 | 低 | 约 1 天（梯度离心 18 h） | 组学、标志物 | [1,2,15] |
| SEC | 较高（脂蛋白除外） | 中高 | 柱上运行通常 <1 h，另加浓缩 | 功能实验、体液纯化 | [3,17,18] |
| TFF / 超滤 | 低（需搭配） | 高 | TFF 约 1 h（200 mL 级） | 大体积浓缩、放大制备 | [1,4,24] |
| 聚合物沉淀 | 最低 | 颗粒数最高（非 EV 特异） | 过夜（≥12 h）+ 约 1 h | 初步筛查 | [12,19,25] |
| 免疫亲和 | 目标亚群特异性高 | 低 | 数小时（依方案） | 特定亚群富集 | [1,26,27] |
| 微流控 / AF4 | 高尺寸分辨率，非 EV 特异 | 回收高但处理量小 | 依平台 | 微量样本分析、分级研究 | [1,5,30] |

## 标准工作流程（以细胞培养上清为例）

样本质量在收集时就决定了上限：MISEV2023 建议尽早去除细胞，因为细胞破碎会形成类似 EV 的颗粒 [1]。

1. **收集与前处理**：胎牛血清（FBS）含大量 EV，可改变受体细胞表型；18 h 超离（120,000×g）可去除约 95% 含 RNA 的 FBS EV，1.5 h 不够 [32]；也有研究用 100,000×g 18 h [2]。但无论自制还是商品化“去 EV 血清”都会残留 EV，需验证 [1,33]；超离去除效果可能取决于稀释程度 [1]。也可用无血清/限定培养基窗口，但去 EV 血清和无血清培养都可能改变细胞生理和 EV 产生 [1]。应报告细胞身份、接种和收获密度、收获时活率及传代数 [1]。少数死亡细胞产生的 EV 就可能超过健康细胞产生的 EV，因此活率直接影响 EV 亚型构成和数量 [1]；具体活率阈值（如 >90%）无统一标准，属【实验室惯例】。收集窗口 24–48 h 为常见做法【实验室惯例】。
2. **梯度预澄清**：300×g 去细胞 → 2,000×g 去碎片 → 10,000×g 去较大颗粒 [8,9]；全程 4 °C【实验室惯例】。若当天处理不了，应先去除细胞再冻存上清，并报告冻存温度、时长和冻融次数 [1]。
3. **浓缩**：按体积选择——小体积用超滤管或直接 dUC，大体积（如数百毫升以上）用 TFF [4,13]；具体体积分界（如 <30 mL / ≥100 mL）为【实验室惯例】。
4. **纯化与换液**：SEC / 密度梯度 / 免疫捕获按用途选一 [1]；最终换液到实验所需缓冲液，必要时再浓缩。
5. **表征与储存**：测颗粒浓度与粒径、总蛋白，并分别报告绝对颗粒数和蛋白量 [1]；做蛋白标志检测 [1]。分装储存并报告全部储存参数 [1]（储存缓冲液选择见质控清单）。

## 示例：原代细胞上清的提取优化（通用示例）

- **先固定生物学变量**：供体、细胞纯度、分化/激活状态等都应作为产 EV 细胞的特征报告 [1]；不同组别应使用同一流程、同一批耗材平行提取【实验室惯例】。
- **培养窗口**：在细胞状态良好时换成去 EV 或无血清培养基并收集 24–48 h 上清【实验室惯例】；过度汇合或饥饿过久可能增加死亡细胞，而少量死亡细胞的 EV 即可占据主导 [1]。
- **推荐组合**：上清量大时 TFF 浓缩 → SEC 纯化 [3,4]；原代细胞上清量小时可用 dUC 或超滤粗提 → SEC【实验室惯例，依据上述方法特性】。体外功能实验要避免沉淀法共沉淀物带来的假象 [1,19]，必须设置“未经细胞条件化的培养基走同一流程”的空白对照 [1]。
- **剂量单位统一**：以蛋白浓度替代 EV 浓度需谨慎且一般不推荐 [1]；功能实验同时报告颗粒数和蛋白量，批间先做颗粒数与标志物一致性检查再进入动物实验【实验室惯例】。

## 分样本优化要点

| 样本 | 主要干扰物 | 推荐路线 | 关键优化 |
|---|---|---|---|
| 细胞上清 | 血清来源 EV 与蛋白、死亡细胞来源颗粒 [1,32] | TFF/超滤 + SEC 或 dUC（± SEC/密度梯度）[2,3,4] | 去 EV 血清（验证残留）或无血清窗口；报告活率；设未条件化培养基对照 [1,33] |
| 血浆 | 血小板、脂蛋白、溶血产物、可溶/聚集蛋白 [1,34] | SEC（需去脂蛋白时联合密度分离）；避免单用沉淀法 [17,19] | 空腹采血（降低乳糜微粒）；粗针头减少血小板活化与溶血；尽快处理 [1]；ISTH 方案：采血后 <2 h 内、室温 2,500×g 15 min 离心两次（不用刹车）制备无血小板血浆 [35]；量化残余血小板 [36]；填写 MIBlood-EV [1,34] |
| 血清 | 凝血过程中血小板释放的 EV（可占血清 EV 的 50% 以上）[37] | 同血浆；EV 循环研究优先用血浆 [37] | 报告促凝剂与凝血时间 [34]；血清与血浆数据不可直接混用 [37] |
| 尿液 | Tamm–Horsfall 蛋白（尿调蛋白）聚合网罗 EV 并共分离；尿蛋白 [1] | 超滤浓缩 + SEC；或还原剂处理后 dUC [1,38,39] | DTT 等还原剂可解聚 THP 网络、释放 EV [38]，但也有报告得率改善有限 [39]，处理方式需写入方法；归一化尚无共识，可用计时尿排泄率或按渗透压/肌酐近似 [1,39] |
| 脑脊液 / 唾液等 | 总量低；黏液（唾液） | 超滤浓缩 + SEC；或免疫捕获【实验室惯例】 | 全程使用低吸附耗材【实验室惯例】；唾液先离心去黏液层并记录收集方式【实验室惯例】 |
| 组织 / 类器官 | 细胞与细胞碎片伪影 [1] | 依样本选择 | 重点追踪应在 EV 中被耗竭的细胞组分 [1] |

## 质控清单（依据 MISEV2023）

提取做完不等于拿到 EV。MISEV2023 并不规定某一种必须使用的技术或标志物 [1]，但要求用互补证据支持“EV”的结论；缺项时如实说明，不要用单一颗粒计数结果宣称“提取成功”。

**表征**

- **颗粒数量与大小**：用 NTA、TRPS、纳米流式等方法报告粒径分布与颗粒浓度，并报告仪器设置和检测下限 [1]。
- **形貌**：TEM、冷冻电镜等成像；干燥条件下 EV 可能形成“杯状”伪影，水合条件下（如冷冻电镜）不出现 [1]。TEM 图像受操作者选图影响：操作者挑选的图像质量往往高于在预定位置随机取得的图像，后者更能反映样本差异 [40]。
- **蛋白标志（更正）**：MISEV2023 要求至少分析第 1、2、3 类蛋白各一种：第 1 类为跨膜或 GPI 锚定蛋白（如 CD9、CD63、CD81），第 2 类为胞质蛋白（如 TSG101、ALIX、syntenin），第 3 类为非 EV 共分离结构的主要成分，作为纯度对照（如脂蛋白 ApoA1/ApoB、白蛋白、尿中的 THP）[1]。**原稿“至少 3 个阳性标志”来自 MISEV2014，MISEV2018 已更新** [41]。
- **细胞内区室蛋白**：calnexin、GM130 等属第 4 类，在 MISEV2023 中为**可选**项，因为它们可能存在于某些 EV 亚型中 [1]；MISEV2018 则要求在宣称研究小 EV 时检测第 4 类 [41]。更宜报告“相对细胞裂解物的耗竭程度”，而不是简单的有/无 [41]。

**纯度与报告指标**

- **颗粒/蛋白比**：颗粒数 ÷ 蛋白量是常用的纯度估计 [42]；原作者提出 >3×10¹⁰ 颗粒/µg 为高纯度，2×10⁹–2×10¹⁰ 为低纯度，<1.5×10⁹ 为不纯（基于其实验室数据）[42]。该比值依赖仪器检测下限，若报告比值，应同时分别报告颗粒和蛋白的绝对浓度 [1]，也不能替代标志蛋白证据。
- **回收与特异性**：报告样本投入量与各步骤参数；免疫捕获等方法应定量下拉与流穿以评估效率 [1]。
- **方法报告**：离心报告转子、rpm、时间、温度、加减速 [1]；SEC 报告填料、柱尺寸、上样量、空体积和收集级分 [1]；过滤/TFF 报告膜类型与截留值 [1]。“100,000×g 离心”这种写法无法复现。可将方法上传 EV-TRACK 知识库以提高透明度 [43]。
- **储存（更正）**：MISEV2023 指出冻融影响的证据不一致，建议避免反复冻融或评估其影响，并报告全部储存参数 [1]。−80 °C 储存会随时间降低 EV 浓度和纯度 [44]；单纯 PBS 中储存或稀释 EV 回收率可大幅下降，含白蛋白和海藻糖的 PBS（PBS-HAT）稳定性更好 [45]。原稿“PBS 分装、冻融 ≤1 次”的硬性规定无统一依据，已改为上述表述。
- **用词规范**：除非能证明内体来源，不宜称“外泌体（exosome）”，而应使用“EV”或操作性术语 [1]；“小 EV”常被描述为 <200 nm，但并无严格的大小界限共识，测得的直径也取决于表征方法 [1]。

## 常见坑与排查

**得率异常**

- **颗粒计数虚高**：血浆中大小在 EV 范围内的颗粒多数缺乏 EV 标志，主要是脂蛋白（以 LDL 为主）[22]；试剂盒颗粒数高但纯度低 [12]。应加做标志蛋白和纯度指标，必要时用 SEC 或密度梯度复核 [17]。
- **得率突然变低**：检查细胞活率与培养条件 [1]、血清批次 [33]、超滤膜吸附 [1]、转子与 k 因子换算 [1,10]。
- **批间波动大**：固定收集窗口、操作者和耗材批次，把每步参数写进批记录【实验室惯例】。

**功能实验假象**

- **“EV 效应”其实来自共分离物**：设置非 EV 级分、EV 去除级分或酶处理级分等对照，判断功能是否 EV 特异 [1]；设未条件化培养基走全流程的对照 [1]。
- **剂量不可比**：以蛋白量作为 EV 剂量需谨慎 [1]；同时报告颗粒数和蛋白量。
- **储存影响活性**：储存条件可改变 EV 浓度、大小和功能相关特性 [44,45]；功能实验优先用新鲜或储存条件已验证的制备。

**一条底线**：提取方法会显著影响 EV 的纯度与组学结果 [2,5]，因此换了方法后，旧方法的剂量—效应关系不能直接平移；新方法上线前用同一批样本做平行比较【实验室惯例】。

## 参考文献

（编号与 `referencesv1.0.json` 一致；全部条目已经 PubMed E-utilities 与 Crossref API 核验。）

[1] Welsh JA, Goberdhan DCI, O'Driscoll L, Buzas EI, Blenkiron C, Bussolati B, et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13:e12404. doi:10.1002/jev2.12404. PMID:38326288; PMC10850029.

[2] Van Deun J, Mestdagh P, Sormunen R, Cocquyt V, Vermaelen K, Vandesompele J, et al. The impact of disparate isolation methods for extracellular vesicles on downstream RNA profiling. J Extracell Vesicles. 2014;3:24858. doi:10.3402/jev.v3.24858. PMID:25317274; PMC4169610.

[3] Nordin JZ, Lee Y, Vader P, Mäger I, Johansson HJ, Heusermann W, et al. Ultrafiltration with size-exclusion liquid chromatography for high yield isolation of extracellular vesicles preserving intact biophysical and functional properties. Nanomedicine. 2015;11:879-883. doi:10.1016/j.nano.2015.01.003. PMID:25659648.

[4] Busatto S, Vilanilam G, Ticer T, Lin WL, Dickson DW, Shapiro S, et al. Tangential Flow Filtration for Highly Efficient Concentration of Extracellular Vesicles from Large Volumes of Fluid. Cells. 2018;7:273. doi:10.3390/cells7120273. PMID:30558352; PMC6315734.

[5] Dong L, Zieren RC, Horie K, Kim CJ, Mallick E, Jing Y, et al. Comprehensive evaluation of methods for small extracellular vesicles separation from human plasma, urine and cell culture medium. J Extracell Vesicles. 2020;10:e12044. doi:10.1002/jev2.12044. PMID:33489012; PMC7810129.

[6] Gardiner C, Di Vizio D, Sahoo S, Théry C, Witwer KW, Wauben M, et al. Techniques used for the isolation and characterization of extracellular vesicles: results of a worldwide survey. J Extracell Vesicles. 2016;5:32945. doi:10.3402/jev.v5.32945. PMID:27802845; PMC5090131.

[7] Brennan K, Martin K, FitzGerald SP, O'Sullivan J, Wu Y, Blanco A, et al. A comparison of methods for the isolation and separation of extracellular vesicles from protein and lipid particles in human serum. Sci Rep. 2020;10:1039. doi:10.1038/s41598-020-57497-7. PMID:31974468; PMC6978318.

[8] Théry C, Amigorena S, Raposo G, Clayton A. Isolation and characterization of exosomes from cell culture supernatants and biological fluids. Curr Protoc Cell Biol. 2006;30:Unit 3.22. doi:10.1002/0471143030.cb0322s30. PMID:18228490.

[9] Livshits MA, Khomyakova E, Evtushenko EG, Lazarev VN, Kulemin NA, Semina SE, et al. Isolation of exosomes by differential centrifugation: Theoretical analysis of a commonly used protocol. Sci Rep. 2015;5:17319. doi:10.1038/srep17319. PMID:26616523; PMC4663484.

[10] Cvjetkovic A, Lötvall J, Lässer C. The influence of rotor type and centrifugation time on the yield and purity of extracellular vesicles. J Extracell Vesicles. 2014;3:23111. doi:10.3402/jev.v3.23111. PMID:24678386; PMC3967015.

[11] Linares R, Tan S, Gounou C, Arraud N, Brisson AR. High-speed centrifugation induces aggregation of extracellular vesicles. J Extracell Vesicles. 2015;4:29509. doi:10.3402/jev.v4.29509. PMID:26700615; PMC4689953.

[12] Tian Y, Gong M, Hu Y, Liu H, Zhang W, Zhang M, et al. Quality and efficiency assessment of six extracellular vesicle isolation methods by nano-flow cytometry. J Extracell Vesicles. 2020;9:1697028. doi:10.1080/20013078.2019.1697028. PMID:31839906; PMC6896440.

[13] Lobb RJ, Becker M, Wen SW, Wong CS, Wiegmans AP, Leimgruber A, et al. Optimized exosome isolation protocol for cell culture supernatant and human plasma. J Extracell Vesicles. 2015;4:27031. doi:10.3402/jev.v4.27031. PMID:26194179; PMC4507751.

[14] Momen-Heravi F, Balaj L, Alian S, Trachtenberg AJ, Hochberg FH, Skog J, et al. Impact of biofluid viscosity on size and sedimentation efficiency of the isolated microvesicles. Front Physiol. 2012;3:162. doi:10.3389/fphys.2012.00162. PMID:22661955; PMC3362089.

[15] Jeppesen DK, Fenix AM, Franklin JL, Higginbotham JN, Zhang Q, Zimmerman LJ, et al. Reassessment of Exosome Composition. Cell. 2019;177:428-445.e18. doi:10.1016/j.cell.2019.02.029. PMID:30951670; PMC6664447.

[16] Yuana Y, Levels J, Grootemaat A, Sturk A, Nieuwland R. Co-isolation of extracellular vesicles and high-density lipoproteins using density gradient ultracentrifugation. J Extracell Vesicles. 2014;3:23262. doi:10.3402/jev.v3.23262. PMID:25018865; PMC4090368.

[17] Karimi N, Cvjetkovic A, Jang SC, Crescitelli R, Hosseinpour Feizi MA, Nieuwland R, et al. Detailed analysis of the plasma extracellular vesicle proteome after separation from lipoproteins. Cell Mol Life Sci. 2018;75:2873-2886. doi:10.1007/s00018-018-2773-4. PMID:29441425; PMC6021463.

[18] Böing AN, van der Pol E, Grootemaat AE, Coumans FA, Sturk A, Nieuwland R. Single-step isolation of extracellular vesicles by size-exclusion chromatography. J Extracell Vesicles. 2014;3:23430. doi:10.3402/jev.v3.23430. PMID:25279113; PMC4159761.

[19] Gámez-Valero A, Monguió-Tortajada M, Carreras-Planella L, Franquesa Ml, Beyer K, Borràs FE. Size-Exclusion Chromatography-based isolation minimally alters Extracellular Vesicles' characteristics compared to precipitating agents. Sci Rep. 2016;6:33641. doi:10.1038/srep33641. PMID:27640641; PMC5027519.

[20] Mol EA, Goumans MJ, Doevendans PA, Sluijter JPG, Vader P. Higher functionality of extracellular vesicles isolated using size-exclusion chromatography compared to ultracentrifugation. Nanomedicine. 2017;13:2061-2065. doi:10.1016/j.nano.2017.03.011. PMID:28365418.

[21] Takov K, Yellon DM, Davidson SM. Comparison of small extracellular vesicles isolated from plasma by ultracentrifugation or size-exclusion chromatography: yield, purity and functional potential. J Extracell Vesicles. 2019;8:1560809. doi:10.1080/20013078.2018.1560809. PMID:30651940; PMC6327926.

[22] Sódar BW, Kittel Á, Pálóczi K, Vukman KV, Osteikoetxea X, Szabó-Taylor K, et al. Low-density lipoprotein mimics blood plasma-derived exosomes and microvesicles during isolation and detection. Sci Rep. 2016;6:24316. doi:10.1038/srep24316. PMID:27087061; PMC4834552.

[23] Benedikter BJ, Bouwman FG, Vajen T, Heinzmann ACA, Grauls G, Mariman EC, et al. Ultrafiltration combined with size exclusion chromatography efficiently isolates extracellular vesicles from cell culture media for compositional and functional studies. Sci Rep. 2017;7:15297. doi:10.1038/s41598-017-15717-7. PMID:29127410; PMC5681555.

[24] Haraszti RA, Miller R, Stoppato M, Sere YY, Coles A, Didiot MC, et al. Exosomes Produced from 3D Cultures of MSCs by Tangential Flow Filtration Show Higher Yield and Improved Activity. Mol Ther. 2018;26:2838-2847. doi:10.1016/j.ymthe.2018.09.015. PMID:30341012; PMC6277553.

[25] Rider MA, Hurwitz SN, Meckes DG Jr. ExtraPEG: A Polyethylene Glycol-Based Method for Enrichment of Extracellular Vesicles. Sci Rep. 2016;6:23978. doi:10.1038/srep23978. PMID:27068479; PMC4828635.

[26] Kowal J, Arras G, Colombo M, Jouve M, Morath JP, Primdal-Bengtson B, et al. Proteomic comparison defines novel markers to characterize heterogeneous populations of extracellular vesicle subtypes. Proc Natl Acad Sci U S A. 2016;113:E968-E977. doi:10.1073/pnas.1521230113. PMID:26858453; PMC4776515.

[27] Tauro BJ, Greening DW, Mathias RA, Ji H, Mathivanan S, Scott AM, et al. Comparison of ultracentrifugation, density gradient separation, and immunoaffinity capture methods for isolating human colon cancer cell line LIM1863-derived exosomes. Methods. 2012;56:293-304. doi:10.1016/j.ymeth.2012.01.002. PMID:22285593.

[28] Contreras-Naranjo JC, Wu HJ, Ugaz VM. Microfluidics for exosome isolation and analysis: enabling liquid biopsy for personalized medicine. Lab Chip. 2017;17:3558-3577. doi:10.1039/c7lc00592j. PMID:28832692; PMC5656537.

[29] Liangsupree T, Multia E, Riekkola ML. Modern isolation and separation techniques for extracellular vesicles. J Chromatogr A. 2021;1636:461773. doi:10.1016/j.chroma.2020.461773. PMID:33316564.

[30] Zhang H, Freitas D, Kim HS, Fabijanic K, Li Z, Chen H, et al. Identification of distinct nanoparticles and subsets of extracellular vesicles by asymmetric flow field-flow fractionation. Nat Cell Biol. 2018;20:332-343. doi:10.1038/s41556-018-0040-4. PMID:29459780; PMC5931706.

[31] Zhang Q, Jeppesen DK, Higginbotham JN, Graves-Deal R, Trinh VQ, Ramirez MA, et al. Supermeres are functional extracellular nanoparticles replete with disease biomarkers and therapeutic targets. Nat Cell Biol. 2021;23:1240-1254. doi:10.1038/s41556-021-00805-8. PMID:34887515; PMC8656144.

[32] Shelke GV, Lässer C, Gho YS, Lötvall J. Importance of exosome depletion protocols to eliminate functional and RNA-containing extracellular vesicles from fetal bovine serum. J Extracell Vesicles. 2014;3:24783. doi:10.3402/jev.v3.24783. PMID:25317276; PMC4185091.

[33] Lehrich BM, Liang Y, Khosravi P, Federoff HJ, Fiandaca MS. Fetal Bovine Serum-Derived Extracellular Vesicles Persist within Vesicle-Depleted Culture Media. Int J Mol Sci. 2018;19:3538. doi:10.3390/ijms19113538. PMID:30423996; PMC6275013.

[34] Lucien F, Gustafson D, Lenassi M, Li B, Teske JJ, Boilard E, et al. MIBlood-EV: Minimal information to enhance the quality and reproducibility of blood extracellular vesicle research. J Extracell Vesicles. 2023;12:12385. doi:10.1002/jev2.12385. PMID:38063210; PMC10704543.

[35] Lacroix R, Judicone C, Mooberry M, Boucekine M, Key NS, Dignat-George F. Standardization of pre-analytical variables in plasma microparticle determination: results of the International Society on Thrombosis and Haemostasis SSC Collaborative workshop. J Thromb Haemost. 2013;11:1190-1193. doi:10.1111/jth.12207. PMID:23551930; PMC4395506.

[36] Clayton A, Boilard E, Buzas EI, Cheng L, Falcón-Perez JM, Gardiner C, et al. Considerations towards a roadmap for collection, handling and storage of blood extracellular vesicles. J Extracell Vesicles. 2019;8:1647027. doi:10.1080/20013078.2019.1647027. PMID:31489143; PMC6711123.

[37] Witwer KW, Buzás EI, Bemis LT, Bora A, Lässer C, Lötvall J, et al. Standardization of sample collection, isolation and analysis methods in extracellular vesicle research. J Extracell Vesicles. 2013;2:20360. doi:10.3402/jev.v2i0.20360. PMID:24009894; PMC3760646.

[38] Fernández-Llama P, Khositseth S, Gonzales PA, Star RA, Pisitkun T, Knepper MA. Tamm-Horsfall protein and urinary exosome isolation. Kidney Int. 2010;77:736-742. doi:10.1038/ki.2009.550. PMID:20130532; PMC3398710.

[39] Erdbrügger U, Blijdorp CJ, Bijnsdorp IV, Borràs FE, Burger D, Bussolati B, et al. Urinary extracellular vesicles: A position paper by the Urine Task Force of the International Society for Extracellular Vesicles. J Extracell Vesicles. 2021;10:e12093. doi:10.1002/jev2.12093. PMID:34035881; PMC8138533.

[40] Rikkert LG, Nieuwland R, Terstappen LWMM, Coumans FAW. Quality of extracellular vesicle images by transmission electron microscopy is operator and protocol dependent. J Extracell Vesicles. 2019;8:1555419. doi:10.1080/20013078.2018.1555419. PMID:30651939; PMC6327933.

[41] Théry C, Witwer KW, Aikawa E, Alcaraz MJ, Anderson JD, Andriantsitohaina R, et al. Minimal information for studies of extracellular vesicles 2018 (MISEV2018): a position statement of the International Society for Extracellular Vesicles and update of the MISEV2014 guidelines. J Extracell Vesicles. 2018;7:1535750. doi:10.1080/20013078.2018.1535750. PMID:30637094; PMC6322352.

[42] Webber J, Clayton A. How pure are your vesicles?. J Extracell Vesicles. 2013;2:19861. doi:10.3402/jev.v2i0.19861. PMID:24009896; PMC3760653.

[43] EV-TRACK Consortium; Van Deun J, Mestdagh P, Agostinis P, Akay Ö, Anand S, et al. EV-TRACK: transparent reporting and centralizing knowledge in extracellular vesicle research. Nat Methods. 2017;14:228-232. doi:10.1038/nmeth.4185. PMID:28245209.

[44] Gelibter S, Marostica G, Mandelli A, Siciliani S, Podini P, Finardi A, et al. The impact of storage on extracellular vesicles: A systematic study. J Extracell Vesicles. 2022;11:e12162. doi:10.1002/jev2.12162. PMID:35102719; PMC8804350.

[45] Görgens A, Corso G, Hagey DW, Jawad Wiklander R, Gustafsson MO, Felldin U, et al. Identification of storage conditions stabilizing extracellular vesicles preparations. J Extracell Vesicles. 2022;11:e12238. doi:10.1002/jev2.12238. PMID:35716060; PMC9206228.
