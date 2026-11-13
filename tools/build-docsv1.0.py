#!/usr/bin/env python3
"""Generate repo Markdown (protocols, QC checklist) from content-zhv1.0.md. Text is copied verbatim.
Usage: python3 build-docsv1.0.py <repo-root>"""
import sys, re, os
R = sys.argv[1]
MD = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'content-zhv1.0.md'), encoding='utf-8').read()
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

HEAD = ('> 摘自 [`docs/content-zhv1.0.md`](../docs/content-zhv1.0.md)（v1.0.0，最后核验 2026-11-13），文字逐字保留，[n] 编号与 '
        '[`references/referencesv1.0.json`](../references/referencesv1.0.json) 一致。在线互动版：<https://tuanziding.github.io/ev-isolation-guide/>\n>\n')

def write(path, title, body):
    refs = cited(body)
    out = f'# {title}\n\n{HEAD}{DISCL}\n\n{body.strip()}\n\n## 本文引用的参考文献\n\n' + '\n\n'.join(linkify(n) for n in refs) + '\n'
    full = os.path.join(R, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(out)
    return path, len(refs)

made = []
# methods
mb = '\n'.join(secs['七种主流方法详解'])
intro = mb.split('### ')[0].strip()
names = ['duc-differential-ultracentrifugation', 'dguc-density-gradient', 'sec-size-exclusion-chromatography',
         'uf-tff-ultrafiltration', 'polymer-precipitation', 'immunoaffinity-capture', 'microfluidics-af4']
for i, ch in enumerate(mb.split('### ')[1:]):
    head, body = ch.split('\n', 1)
    title = re.sub(r'^\d+\. ', '', head.strip())
    made.append(write(f'protocols/{i+1}-{names[i]}v1.0.md', f'方法 {i+1}：{title}', intro + '\n\n' + re.sub(r'\*\*定性评分\*\*(?!（)', '**定性评分**（定性共识，非测量值）', body)))
made.append(write('protocols/combinationsv1.0.md', '推荐的组合思路', '\n'.join(secs['推荐的组合思路']).replace('### ', '## ')))
cmp_ = '\n'.join(secs['横向对比速查'])
made.append(write('protocols/comparisonv1.0.md', '横向对比速查', cmp_))
made.append(write('protocols/standard-workflowv1.0.md', '标准工作流程（以细胞培养上清为例）', '\n'.join(secs['标准工作流程（以细胞培养上清为例）'])))
made.append(write('protocols/primary-cell-examplev1.0.md', '示例：原代细胞上清的提取优化（通用示例）', '\n'.join(secs['示例：原代细胞上清的提取优化（通用示例）'])))
made.append(write('protocols/per-samplev1.0.md', '分样本优化要点', '\n'.join(secs['分样本优化要点'])))
made.append(write('protocols/pitfallsv1.0.md', '常见坑与排查', '\n'.join(secs['常见坑与排查'])))
# QC checklist with checkboxes
qc = []
for l in secs['质控清单（依据 MISEV2023）']:
    if l.startswith('- '): qc.append('- [ ] ' + l[2:])
    elif re.match(r'^\*\*[^*]+\*\*$', l.strip()): qc.append('### ' + l.strip().strip('*'))
    else: qc.append(l)
made.append(write('checklists/qc-checklistv1.0.md', '质控清单（依据 MISEV2023）', '\n'.join(qc)))
for p, n in made: print(p, n, 'refs')
