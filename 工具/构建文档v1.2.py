#!/usr/bin/env python3
"""构建文档 v1.2：由 文档/指南正文v1.2.md 生成 文档/方法/ 与 文档/质控清单v1.2.md，附相关图片；文字逐字保留。
Generate repo Markdown (methods, QC checklist) from 文档/指南正文v1.2.md, with figure references. Text is copied verbatim.
Usage: python3 工具/构建文档v1.2.py"""
import sys, re, os, json
from pathlib import Path
R = str(Path(__file__).resolve().parent.parent)
MD = open(os.path.join(R, '文档/指南正文v1.2.md'), encoding='utf-8').read()
REFS = json.load(open(os.path.join(R, '验证/参考文献v1.1.json'), encoding='utf-8'))
REFNUM = {r['ref_id']: r['number'] for r in REFS}
FIGR = {f['filename'].split('v1.0')[0]: f for f in json.load(open(os.path.join(R, '图片/文献原图/文献原图说明v1.0.json'), encoding='utf-8'))['figures']}
FIGS = {x['file'].replace('-v1.0.webp', ''): x for x in json.load(open(os.path.join(R, '图片/示意图/示意图标注v1.1.json'), encoding='utf-8'))['items']}
lines = MD.split('\n')
DISCL = lines[4]
secs, cur = {}, None
for ln in lines:
    if ln.startswith('## '):
        cur = ln[3:].strip(); secs[cur] = []
    elif cur:
        secs[cur].append(ln)
REF = {}
for l in secs['参考文献']:
    m = re.match(r'\[(\d+)\] (.*)', l)
    if m: REF[int(m.group(1))] = m.group(2)

def cited(text):
    ns = set()
    for g in re.findall(r'\[(\d+(?:,\d+)*)\]', text):
        ns.update(int(x) for x in g.split(','))
    return sorted(ns)

def linkify(n):
    t = REF[n]
    t = re.sub(r'doi:(\S+?)\.( |$)', lambda m: f'doi:[{m.group(1)}](https://doi.org/{m.group(1)}).{m.group(2)}', t)
    t = re.sub(r'PMID:(\d+)', r'PMID:[\1](https://pubmed.ncbi.nlm.nih.gov/\1/)', t)
    t = re.sub(r'(PMC\d+)', r'[\1](https://pmc.ncbi.nlm.nih.gov/articles/\1/)', t)
    return f'[{n}] {t}'

def HEAD(up):
    return (f'> 摘自 [`文档/指南正文v1.2.md`]({up}文档/指南正文v1.2.md)（v1.2.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 '
            f'[`验证/参考文献v1.1.json`]({up}验证/参考文献v1.1.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>\n>\n'
            f'> 许可：本文文字采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)；商业用途需事先联系作者获得授权合作（<https://tuanziding.github.io/#contact>）。\n>\n')

def figmd(keys, up):
    out = ['## 相关图片', '', f'点击缩略图查看原图。标“AI 示意图 · 非实验数据”的是帮助理解原理的 AI 生成示意图；标“文献原图 · CC BY 4.0”的转载自原论文，版权归原作者，按其原 CC BY 4.0 许可使用（见 [`文档/图片说明v1.0.md`]({up}文档/图片说明v1.0.md)），不属于本仓库的许可范围。', '']
    nums = []
    for k in keys:
        if k.startswith('schem-'):
            x = FIGS[k]; fn = x['file']
            out.append(f"**{x['title']}**（AI 示意图 · 非实验数据）\n\n[![AI 示意图：{x['title']}]({up}图片/示意图/{fn.replace('.webp', '-sm.webp')})]({up}图片/示意图/{fn})\n\n" + '；'.join(f"{i+1}. {l['text']}" for i, l in enumerate(x['labels'])) + f"\n\n{x['caption']}\n")
        else:
            f = FIGR[k]; n = f.get('ref_number_in_guide') or REFNUM[f['ref_id']]; nums.append(n); r = REFS[n - 1]
            a = ', '.join(r['authors'][:3]) + (', et al.' if len(r['authors']) > 3 else '')
            fig = f['figure_panel'].split(' (')[0]
            out.append(f"**{f['title_zh']}**（文献原图 · CC BY 4.0）\n\n[![文献原图：{f['title_zh']}]({up}图片/文献原图/{f['filename'].replace('.webp', '-sm.webp')})]({up}图片/文献原图/{f['filename']})\n\n"
                       f"怎么读：{f['caption_zh']}\n\n> Reproduced from {a}, {r['year']}, *{r['journal_abbrev']}* {fig}, [CC BY 4.0]({f['license_url']}), no changes. "
                       f"DOI: [{f['doi']}](https://doi.org/{f['doi']})" + (f" · [{f['pmcid']}](https://pmc.ncbi.nlm.nih.gov/articles/{f['pmcid']}/)" if f.get('pmcid') else '') + f" · 文献 [{n}]\n")
    return '\n'.join(out), nums

def write(path, title, body, figs=()):
    up = '../' * path.count('/')
    fm, fnums = figmd(figs, up) if figs else ('', [])
    refs = sorted(set(cited(body)) | set(fnums))
    out = f'# {title}\n\n{HEAD(up)}{DISCL}\n\n{body.strip()}\n\n' + (fm + '\n\n' if fm else '') + '## 本文引用的参考文献\n\n' + '\n\n'.join(linkify(n) for n in refs) + '\n'
    full = os.path.join(R, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(out)
    return path, len(refs)

made = []
# methods
mb = '\n'.join(secs['七种主流方法详解'])
intro = mb.split('### ')[0].strip()
names = ['1-差速超速离心', '2-密度梯度离心', '3-尺寸排阻色谱', '4-超滤与切向流过滤', '5-聚合物沉淀', '6-免疫亲和捕获', '7-微流控与流场流分离']
MF = {1: ['schem-duc', 'fig-tff-vs-uc-busatto2018', 'fig-nta-size-3samples-dong2020'], 2: ['schem-dguc', 'fig-dguc-fractions-plasma-dong2020', 'fig-idc-sec-plasma-karimi2018'],
      3: ['schem-sec', 'fig-sec-profile-plasma-karimi2018', 'fig-cryoem-sec-peg-prospr-gamezvalero2016'], 4: ['schem-tff', 'fig-tff-vs-uc-busatto2018'],
      5: ['schem-peg', 'fig-cryoem-sec-peg-prospr-gamezvalero2016'], 6: ['schem-immuno'], 7: ['schem-af4', 'fig-af4-mals-plasma-holcar2020']}
for i, ch in enumerate(mb.split('### ')[1:]):
    head, body = ch.split('\n', 1)
    title = re.sub(r'^\d+\. ', '', head.strip())
    extra = '\n\n> 缺口：exomere 的 AF4 洗脱曲线没有找到开放许可的原图，请看原文 Zhang 2018 [30]（[doi:10.1038/s41556-018-0040-4](https://doi.org/10.1038/s41556-018-0040-4)）。' if i == 6 else ''
    made.append(write(f'文档/方法/{names[i]}v1.2.md', f'方法 {i+1}：{title}', intro + '\n\n' + re.sub(r'\*\*定性评分\*\*(?!（)', '**定性评分**（定性共识，非测量值）', body) + extra, MF[i + 1]))
made.append(write('文档/方法/组合思路v1.2.md', '推荐的组合思路', '\n'.join(secs['推荐的组合思路']).replace('### ', '## '), ['fig-idc-sec-plasma-karimi2018']))
cmp_ = '\n'.join(secs['横向对比速查'])
made.append(write('文档/方法/横向对比v1.2.md', '横向对比速查', cmp_, ['fig-method-grid-misev2023', 'schem-overview']))
made.append(write('文档/方法/标准流程v1.2.md', '标准工作流程（以细胞培养上清为例）', '\n'.join(secs['标准工作流程（以细胞培养上清为例）']), ['schem-overview', 'fig-fbs-depletion-nta-lehrich2018']))
made.append(write('文档/方法/原代细胞示例v1.2.md', '示例：原代细胞上清的提取优化（通用示例）', '\n'.join(secs['示例：原代细胞上清的提取优化（通用示例）'])))
made.append(write('文档/方法/分样本要点v1.2.md', '分样本优化要点', '\n'.join(secs['分样本优化要点']) + '\n\n> 缺口：尿液样本 DTT 还原处理前后的对比没有找到开放许可的原图，请看原文 Fernández-Llama 2010 [38]（[doi:10.1038/ki.2009.550](https://doi.org/10.1038/ki.2009.550)）。',
    ['fig-wb-lipoprotein-serum-brennan2020', 'fig-ldl-ev-tem-sodar2016', 'fig-idc-sec-plasma-karimi2018', 'fig-urine-thp-cryotem-musante2020', 'fig-urine-cryoem-tem-erdbrugger2021', 'fig-csf-cryoem-emelyanov2020', 'fig-saliva-em-palanisamy2010']))
made.append(write('文档/方法/常见坑与排查v1.2.md', '常见坑与排查', '\n'.join(secs['常见坑与排查'])))
# QC checklist with checkboxes
qc = []
for l in secs['质控清单（依据 MISEV2023）']:
    if l.startswith('- '): qc.append('- [ ] ' + l[2:])
    elif re.match(r'^\*\*[^*]+\*\*$', l.strip()): qc.append('### ' + l.strip().strip('*'))
    else: qc.append(l)
made.append(write('文档/质控清单v1.2.md', '质控清单（依据 MISEV2023）', '\n'.join(qc), ['schem-nta', 'schem-nfcm', 'schem-tem', 'schem-wb', 'fig-nta-size-3samples-dong2020', 'fig-tem-3samples-dong2020', 'fig-wb-purity-3samples-dong2020']))
for p, n in made: print(p, n, 'refs')
