#!/usr/bin/env python3
"""Build the EV isolation guide page from content-zhv1.0.md (single source of truth).
Usage: python3 build-sitev1.0.py <variant: github|aiai> <out-html-path> <asset-prefix>
Text is taken verbatim from the Markdown; only markup is added."""
import sys, re, json, html, os

import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = open(ROOT / 'docs/content-zhv1.0.md', encoding='utf-8').read()
REFS = json.load(open(ROOT / 'references/referencesv1.0.json', encoding='utf-8'))
RULES = json.load(open(ROOT / 'assets/data/recommender-rulesv1.0.json', encoding='utf-8'))
REFNUM = {r['ref_id']: r['number'] for r in REFS}
VERSION = '1.0.0'
GH = 'https://github.com/TUANZIDING/ev-isolation-guide'

variant, OUT, AP = sys.argv[1], sys.argv[2], sys.argv[3].rstrip('/')

def short(r):
    a = r['authors'][0] if r['authors'] else ''
    if a.startswith('EV-TRACK'): a = 'EV-TRACK Consortium'
    return f"{a} {r['year']} · {r['journal_abbrev']}"
SHORT = {r['number']: short(r) for r in REFS}

def esc(s): return html.escape(s, quote=False)

def cite(nums):
    parts = []
    for n in nums:
        n = int(n)
        parts.append(f'<a href="#ref-{n}" title="{html.escape(SHORT[n])}">{n}</a>')
    return '<span class="cite">[' + ','.join(parts) + ']</span>'

TAGCLS = {'估算': 'est', '作者判断': 'judge'}
def inl(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`recommender-rulesv1\.0\.json`', f'<a class="code" href="{AP}/data/recommender-rulesv1.0.json"><code>recommender-rulesv1.0.json</code></a>', s)
    s = re.sub(r'`referencesv1\.0\.json`', f'<a class="code" href="{AP}/data/referencesv1.0.json"><code>referencesv1.0.json</code></a>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[(\d+(?:,\d+)*)\]', lambda m: cite(m.group(1).split(',')), s)
    def tag(m):
        t = m.group(1); k = 'lab'
        for key, c in TAGCLS.items():
            if t.startswith(key): k = c
        return f'<span class="tag tag-{k}">【{t}】</span>'
    s = re.sub(r'【([^】]+)】', tag, s)
    return s

# ---------- parse markdown ----------
lines = MD.split('\n')
TITLE = lines[0][2:].strip()
META = lines[2].strip()
DISCL = lines[4][2:].strip()
INTRO = lines[6].strip()
secs, cur = {}, None
for ln in lines[7:]:
    if ln.startswith('## '):
        cur = ln[3:].strip(); secs[cur] = []
    elif cur is not None:
        secs[cur].append(ln)
def paras(block):
    return [p.strip() for p in '\n'.join(block).split('\n\n') if p.strip()]

# key messages
KEY = [p for p in paras(secs['三条核心信息'])]
# recommender intro
REC_INTRO = paras(secs['方案推荐器（逻辑说明）'])[0]
# methods
mblock = '\n'.join(secs['七种主流方法详解'])
m_intro = mblock.split('### ')[0].strip()
METHODS = []
COLORS = ['blue', 'purple', 'green', 'orange', 'yellow', 'red', 'teal']
SHORTN = ['dUC', 'DGUC', 'SEC', 'UF / TFF', '沉淀', '免疫亲和', '微流控 / AF4']
for i, chunk in enumerate(mblock.split('### ')[1:]):
    head, *rest = chunk.strip().split('\n', 1)
    name, tagline = re.split(r' ?· ', head, 1)
    fields = []
    rating = None
    for p in paras(rest[0].split('\n')):
        m = re.match(r'\*\*(.+?)\*\*(.*)', p, re.S)
        key, body = m.group(1), m.group(2)
        if key == '定性评分':
            rating = body
        else:
            fields.append((key, body.lstrip('：')))
    METHODS.append(dict(name=name, tagline=tagline, fields=fields, rating=rating, color=COLORS[i], short=SHORTN[i], idx=i + 1))

def parse_rating(body):
    # body like '（...）：纯度 3/5 · 得率 3/5 · 通量 2/5。'  or '：纯度 5/5 · ...'
    note = ''
    m = re.match(r'（(.+?)）：(.*)', body)
    if m: note, body = m.group(1), m.group(2)
    else: body = body.lstrip('：')
    body = body.rstrip('。')
    items = []
    for seg in body.split(' · '):
        mm = re.match(r'(.+?) ?(\d)/5(.*)', seg)
        items.append((mm.group(1), int(mm.group(2)), mm.group(3)))
    return note, items

# combos
cb = secs['推荐的组合思路']
cparas = paras(cb)
COMBO_H = cparas[0].lstrip('# ').strip()
COMBO_WHY = cparas[1]
COMBO_LIST = [l[2:].strip() for l in cb if l.startswith('- ')]
# comparison
cmp_ = secs['横向对比速查']
CMP_NOTE = [l[2:] for l in cmp_ if l.startswith('> ')][0]
def table(block):
    rows = [l for l in block if l.startswith('|')]
    hdr = [c.strip() for c in rows[0].strip('|').split('|')]
    body = [[c.strip() for c in r.strip('|').split('|')] for r in rows[2:]]
    return hdr, body
CMP_H, CMP_B = table(cmp_)
# workflow
wf = secs['标准工作流程（以细胞培养上清为例）']
WF_INTRO = paras(wf)[0]
WF_STEPS = []
for l in wf:
    m = re.match(r'\d+\. \*\*(.+?)\*\*：(.*)', l)
    if m: WF_STEPS.append((m.group(1), m.group(2)))
# example
ex = secs['示例：原代细胞上清的提取优化（通用示例）']
EX = [l[2:] for l in ex if l.startswith('- ')]
# per sample
SP_H, SP_B = table(secs['分样本优化要点'])
# QC
qc = secs['质控清单（依据 MISEV2023）']
QC_INTRO = paras(qc)[0]
QC_GROUPS = []
for l in qc:
    if re.match(r'^\*\*[^*]+\*\*$', l.strip()):
        QC_GROUPS.append((l.strip().strip('*'), []))
    elif l.startswith('- '):
        m = re.match(r'- \*\*(.+?)\*\*：(.*)', l)
        QC_GROUPS[-1][1].append((m.group(1), m.group(2)))
# pitfalls
pf = secs['常见坑与排查']
PF_GROUPS, PF_BOTTOM = [], ''
for l in pf:
    s = l.strip()
    if re.match(r'^\*\*[^*]+\*\*$', s):
        PF_GROUPS.append((s.strip('*'), []))
    elif s.startswith('- '):
        m = re.match(r'- \*\*(.+?)\*\*：(.*)', s)
        PF_GROUPS[-1][1].append((m.group(1), m.group(2)))
    elif s.startswith('**一条底线**'):
        PF_BOTTOM = s
# references
rb = secs['参考文献']
REF_NOTE = paras(rb)[0]
REF_LINES = {}
for l in rb:
    m = re.match(r'\[(\d+)\] (.*)', l)
    if m: REF_LINES[int(m.group(1))] = m.group(2)
assert len(REF_LINES) == 45 and len(REFS) == 45

# ---------- render ----------
def svg(name, cls='ic'):
    P = {
        'flask': '<path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-2.5L14 9V3"/><path d="M7 15h10"/>',
        'route': '<circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H16a3.5 3.5 0 0 0 0-7H8a3.5 3.5 0 0 1 0-7h7.5"/>',
        'check': '<path d="M4 12.5l5 5L20 6.5"/>',
        'github': '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
        'print': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M6 14h12v7H6z"/>',
        'up': '<path d="M12 19V5M5 12l7-7 7 7"/>',
        'back': '<path d="M9 14L4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/>',
        'reset': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>',
        'home': '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
        'warn': '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17.5v.5"/>',
        'book': '<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5V4.5"/>',
    }
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg>'

def dots(n, color):
    return f'<span class="dots" style="--mc:var(--{color})" aria-hidden="true">' + ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(5)) + '</span>'

def method_card(m):
    note, items = parse_rating(m['rating'])
    rows = ''.join(f'<li><span class="rl">{esc(lbl)}{("<small>" + esc(q.strip()) + "</small>") if q.strip() else ""}</span>{dots(n, m["color"])}<b class="rn">{n}/5</b></li>' for lbl, n, q in items)
    note_html = f'<p class="rnote">{inl("（" + note + "）")}</p>' if note else ''
    flds = ''.join(f'<div class="fld"><dt>{esc(k)}</dt><dd>{inl(v)}</dd></div>' for k, v in m['fields'])
    return f'''<article class="mcard" id="m-{m['idx']}" style="--mc:var(--{m['color']});--mt:var(--{m['color']}-t)">
  <header class="mhead"><span class="mnum">{m['idx']}</span><div><h3>{esc(m['name'])}</h3><p class="mtag">{esc(m['tagline'])}</p></div></header>
  <div class="rating"><p class="rtitle">定性评分 <a class="badge" href="#compare">定性共识</a></p>{note_html}<ul>{rows}</ul></div>
  <dl class="fields">{flds}</dl>
</article>'''

def km_card(p, i):
    m = re.match(r'\*\*(.+?)\*\*\s*(.*)', p, re.S)
    head, body = m.group(1), m.group(2)
    c = ['red', 'blue', 'green'][i]
    return f'<article class="kcard" style="--mc:var(--{c});--mt:var(--{c}-t)"><h3>{esc(head)}</h3><p>{inl(body)}</p></article>'

def tbl(hdr, body, cls, first_strong=True):
    th = ''.join(f'<th scope="col">{inl(h)}</th>' for h in hdr)
    trs = ''
    for r in body:
        tds = ''
        for j, c in enumerate(r):
            if j == 0:
                tds += f'<th scope="row">{inl(c)}</th>'
            else:
                tds += f'<td data-label="{html.escape(hdr[j])}">{inl(c)}</td>'
        trs += f'<tr>{tds}</tr>'
    return f'<div class="tbl-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def ref_item(n, text):
    r = REFS[n - 1]; assert r['number'] == n
    t = esc(text)
    t = t.replace(f'doi:{esc(r["doi"])}', f'doi:<a href="https://doi.org/{html.escape(r["doi"])}" rel="noopener">{esc(r["doi"])}</a>')
    t = t.replace(f'PMID:{r["pmid"]}', f'PMID:<a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" rel="noopener">{r["pmid"]}</a>')
    if r.get('pmcid'):
        t = t.replace(r['pmcid'], f'<a href="https://pmc.ncbi.nlm.nih.gov/articles/{r["pmcid"]}/" rel="noopener">{r["pmcid"]}</a>')
    basis = '已读全文' if r.get('fulltext_read') else '仅核对摘要'
    return f'<li id="ref-{n}"><span class="rnum">[{n}]</span><span class="rtext">{t} <span class="rbasis">{basis}</span></span></li>'

# recommender data (inline, so the page works offline / from file)
gl = [dict(rule=g['rule'], refs=[REFNUM[x] for x in g['refs']]) for g in RULES['global_rules']]
recdata = dict(labels=RULES['labels'], global_rules=gl,
               rules=[dict(s=r['sample'], u=r['use'], p=r['priority'], route=r['route'], rr=r['route_ref_numbers'], note=r['note'], nr=r['note_ref_numbers']) for r in RULES['rules']],
               short={str(k): v for k, v in SHORT.items()})

def radio_group(key, title):
    opts = RULES['labels'][key]
    btns = ''.join(f'<label class="opt"><input type="radio" name="{key}" value="{k}"{" checked" if i == 0 else ""}><span>{esc(v)}</span></label>' for i, (k, v) in enumerate(opts.items()))
    return f'<fieldset class="og"><legend>{title}</legend><div class="opts">{btns}</div></fieldset>'

def mkind(c):
    for k, v in [('密度', 'purple'), ('SEC', 'green'), ('TFF', 'orange'), ('超滤', 'orange'), ('沉淀', 'yellow'), ('免疫', 'red'), ('珠上', 'red'), ('靶向', 'red'), ('AF4', 'teal'), ('超离', 'blue')]:
        if k in c: return v
    return 'ink'

# server-rendered default result (culture/omics/purity) for no-JS
def rec_html(s, u, p):
    r = next(x for x in RULES['rules'] if (x['sample'], x['use'], x['priority']) == (s, u, p))
    chips = '<span class="arr" aria-hidden="true">→</span>'.join(f'<span class="chip" data-m="{mkind(c)}">{esc(c.strip())}</span>' for c in r['route'].split('→'))
    return chips, r

NAV = [('key', '核心信息'), ('rec', '方案推荐器'), ('methods', '七种方法'), ('combo', '组合思路'), ('compare', '横向对比'), ('workflow', '标准流程'), ('example', '原代细胞示例'), ('samples', '分样本'), ('qc', '质控清单'), ('pitfalls', '常见坑'), ('refs', '参考文献')]

aiai = variant == 'aiai'
home_link = f'<a class="pill" href="../index.html#lessons" aria-label="返回课件馆">{svg("home")}<span>课件馆</span></a>' if aiai else ''
sister = ('<a href="exosome-explorerv1.0.html">外泌体与细胞外囊泡漫游</a>' if aiai
          else '<a href="https://aiai-academy.com/lessons/exosome-explorerv1.0.html">外泌体与细胞外囊泡漫游</a>')
canon = 'https://aiai-academy.com/lessons/ev-isolation-guidev1.0.html' if aiai else 'https://tuanziding.github.io/ev-isolation-guide/'
ogimg = ('https://aiai-academy.com/assets/ev-guide/ev-herov1.0.webp' if aiai else 'https://tuanziding.github.io/ev-isolation-guide/assets/images/ev-herov1.0.webp')
IMG = f'{AP}/images' if not aiai else AP

methods_html = '\n'.join(method_card(m) for m in METHODS)
mjump = ''.join(f'<a href="#m-{m["idx"]}" style="--mc:var(--{m["color"]})"><i></i>{esc(m["short"])}</a>' for m in METHODS)

combo_cards = ''
for i, c in enumerate(COMBO_LIST):
    m = re.match(r'\*\*(.+?)\*\*：(.*)', c)
    combo_cards += f'<li class="ccard c{i}"><h3>{esc(m.group(1))}</h3><p>{inl(m.group(2))}</p></li>'

steps_html = ''.join(f'<li class="step" id="step-{i+1}"><div class="sbody"><h3><span class="snum">{i+1}</span>{esc(t)}</h3><p>{inl(b)}</p></div></li>' for i, (t, b) in enumerate(WF_STEPS))
step_tabs = ''.join(f'<button type="button" class="stab" data-step="{i+1}" aria-controls="step-{i+1}"><span class="snum">{i+1}</span><span>{esc(t)}</span></button>' for i, (t, b) in enumerate(WF_STEPS))

ex_html = ''
for e in EX:
    m = re.match(r'\*\*(.+?)\*\*：(.*)', e)
    ex_html += f'<li><h3>{esc(m.group(1))}</h3><p>{inl(m.group(2))}</p></li>'

qc_html = ''
qn = 0
for g, items in QC_GROUPS:
    lis = ''
    for t, b in items:
        qn += 1
        lis += f'<li><label class="qitem"><input type="checkbox" data-qc="qc{qn}"><span class="box">{svg("check")}</span><span class="qtext"><strong>{esc(t)}</strong>：{inl(b)}</span></label></li>'
    qc_html += f'<div class="qgroup"><h3>{esc(g)}</h3><ul>{lis}</ul></div>'

pf_html = ''
for g, items in PF_GROUPS:
    lis = ''.join(f'<li><h4>{esc(t)}</h4><p>{inl(b)}</p></li>' for t, b in items)
    pf_html += f'<div class="pgroup"><h3>{esc(g)}</h3><ul>{lis}</ul></div>'

refs_html = ''.join(ref_item(n, REF_LINES[n]) for n in range(1, 46))
chips0, r0 = rec_html('culture', 'omics', 'purity')

# disclaimer label handling
disc = DISCL
dm = re.match(r'\*\*声明\*\*：(.*)', disc)
disc_body = dm.group(1)

robots = ''
PAGE = f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(TITLE)}｜方案推荐器 · 质控清单 · 45 篇核验文献</title>
<meta name="description" content="细胞外囊泡（EV）提取方法学指南：七种主流方法的原理、参数、优缺点与优化要点，按样本 × 用途 × 优先指标的方案推荐器，MISEV2023 质控清单，45 篇经 PubMed 与 Crossref 核验的参考文献。">
<meta name="theme-color" content="#fff7ec">
<meta name="author" content="Haixiang Ding">{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(TITLE)}">
<meta property="og:description" content="先定用途，再选方法，最后用表征数据证明你得到的是 EV。互动推荐器 + 质控清单 + 45 篇核验文献。">
<meta property="og:image" content="{ogimg}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='29' fill='%23fef1d7' stroke='%23ddac67' stroke-width='5'/%3E%3Ctext x='32' y='43' font-size='30' text-anchor='middle' fill='%23ca6736' font-family='sans-serif' font-weight='700'%3E%E5%9B%A2%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{AP}/ev-guidev1.0.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">跳到正文</a>
<header class="topbar">
  <div class="wrap tb-in">
    <a class="brand" href="#top" aria-label="回到页首"><span class="logo" aria-hidden="true">团</span><span class="bt"><b>EV 提取方法指南</b><small>v{VERSION} · 最后核验 2026-11-13</small></span></a>
    <div class="tb-act">{home_link}<a class="pill" href="{GH}" rel="noopener" aria-label="GitHub 仓库">{svg("github")}<span>GitHub</span></a></div>
  </div>
</header>
<nav class="secnav" aria-label="章节导航"><div class="wrap"><ul>{''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in NAV)}</ul></div></nav>

<main id="main">
<section class="hero" id="top">
  <div class="wrap">
    <div class="hero-card">
      <img class="hero-img" src="{IMG}/ev-herov1.0.webp" width="1376" height="768" alt="插图（AI 生成）：戴护目镜的团子举着试管，机器人在操作离心机，桌上有色谱柱、密度梯度管、滤器和显微镜">
      <div class="hero-txt">
        <h1>{esc(TITLE)}</h1>
        <p class="meta">{esc(META).replace("2026-11-13", "<span class=\"nw\">2026-11-13</span>")}</p>
        <p class="lead">{inl(INTRO)}</p>
        <div class="cta"><a class="btn btn-main" href="#rec">{svg("route")}打开方案推荐器</a><a class="btn btn-soft" href="#qc">{svg("check")}看质控清单</a></div>
      </div>
    </div>
    <aside class="disclaimer" aria-label="声明"><p><strong>声明</strong>：{inl(disc_body)}</p></aside>
  </div>
</section>

<section class="sec" id="key" aria-labelledby="h-key">
  <div class="wrap">
    <h2 id="h-key">三条核心信息</h2>
    <div class="kgrid">{''.join(km_card(p, i) for i, p in enumerate(KEY))}</div>
  </div>
</section>

<section class="sec sec-rec" id="rec" aria-labelledby="h-rec">
  <div class="wrap">
    <h2 id="h-rec">方案推荐器</h2>
    <p class="sintro">{inl(REC_INTRO)}</p>
    <div class="rec">
      <form class="rec-form" id="recForm" aria-label="选择样本、用途和优先指标">
        {radio_group('sample', '样本来源')}
        {radio_group('use', '下游用途')}
        {radio_group('priority', '优先指标')}
      </form>
      <div class="rec-out" id="recOut" aria-live="polite">
        <p class="ro-sel" id="roSel">细胞培养上清 · 组学分析 · 纯度优先</p>
        <h3 class="ro-h">起点方案</h3>
        <div class="route" id="roRoute">{chips0}</div>
        <p class="ro-refs" id="roRefs">依据 {cite(r0['route_ref_numbers'])}</p>
        <div class="ro-note"><h4>注意</h4><p id="roNote">{inl(r0['note'])} {cite(r0['note_ref_numbers'])}</p></div>
        <div class="ro-global"><h4>每个方案都要记住</h4><ul id="roGlobal"></ul></div>
        <p class="ro-foot">{esc(RULES['description'])}</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="methods" aria-labelledby="h-methods">
  <div class="wrap">
    <h2 id="h-methods">七种主流方法详解</h2>
    <p class="sintro">{inl(m_intro)}</p>
    <nav class="mjump" aria-label="跳到方法">{mjump}</nav>
    <div class="mgrid">{methods_html}</div>
  </div>
</section>

<section class="sec" id="combo" aria-labelledby="h-combo">
  <div class="wrap">
    <h2 id="h-combo">推荐的组合思路</h2>
    <div class="combo">
      <div class="combo-why"><h3>{esc(COMBO_H)}</h3><p>{inl(COMBO_WHY)}</p></div>
      <ul class="cgrid">{combo_cards}</ul>
    </div>
  </div>
</section>

<section class="sec" id="compare" aria-labelledby="h-compare">
  <div class="wrap">
    <h2 id="h-compare">横向对比速查</h2>
    <p class="callout">{inl(CMP_NOTE)}</p>
    {tbl(CMP_H, CMP_B, 'tcmp')}
  </div>
</section>

<section class="sec" id="workflow" aria-labelledby="h-workflow">
  <div class="wrap">
    <h2 id="h-workflow">标准工作流程（以细胞培养上清为例）</h2>
    <p class="sintro">{inl(WF_INTRO)}</p>
    <div class="stepper" id="stepper">
      <div class="stabs" role="tablist" aria-label="流程步骤">{step_tabs}</div>
      <ol class="steps">{steps_html}</ol>
      <div class="snav"><button type="button" class="btn btn-soft" id="sPrev">上一步</button><span id="sCount" class="scount"></span><button type="button" class="btn btn-main" id="sNext">下一步</button></div>
    </div>
  </div>
</section>

<section class="sec" id="example" aria-labelledby="h-example">
  <div class="wrap">
    <h2 id="h-example">示例：原代细胞上清的提取优化（通用示例）</h2>
    <ul class="exgrid">{ex_html}</ul>
  </div>
</section>

<section class="sec" id="samples" aria-labelledby="h-samples">
  <div class="wrap">
    <h2 id="h-samples">分样本优化要点</h2>
    {tbl(SP_H, SP_B, 'tsamp')}
  </div>
</section>

<section class="sec" id="qc" aria-labelledby="h-qc">
  <div class="wrap">
    <h2 id="h-qc">质控清单（依据 MISEV2023）</h2>
    <div class="qc-top">
      <figure class="coach"><img src="{IMG}/ev-coachv1.0.webp" width="480" height="631" alt="插图（AI 生成）：戴护目镜、穿白大褂的团子拿着勾选清单" loading="lazy"></figure>
      <div class="coach-say"><p class="cs-name">团子教练提醒</p><p>{inl(QC_INTRO)}</p>
        <div class="qc-bar"><div class="qprog" role="progressbar" aria-valuemin="0" aria-valuemax="{qn}" aria-valuenow="0" aria-label="已勾选项"><i id="qBar"></i></div><span id="qCount">0 / {qn}</span><button type="button" class="btn btn-soft btn-sm" id="qReset">{svg("reset")}清空勾选</button></div>
        <p class="qhint">勾选状态只保存在这台设备的浏览器里。</p>
      </div>
    </div>
    <div class="qc">{qc_html}</div>
  </div>
</section>

<section class="sec" id="pitfalls" aria-labelledby="h-pitfalls">
  <div class="wrap">
    <h2 id="h-pitfalls">常见坑与排查</h2>
    <div class="pgrid">{pf_html}</div>
    <p class="bottomline">{inl(PF_BOTTOM)}</p>
  </div>
</section>

<section class="sec" id="refs" aria-labelledby="h-refs">
  <div class="wrap">
    <h2 id="h-refs">参考文献</h2>
    <p class="sintro">{inl(REF_NOTE)}</p>
    <ol class="reflist">{refs_html}</ol>
  </div>
</section>
</main>

<footer class="foot">
  <div class="wrap">
    <div class="fcard">
      <p><strong>声明</strong>：{inl(disc_body)}</p>
      <ul class="fmeta">
        <li>版本 v{VERSION}</li><li>最后核验 2026-11-13</li><li>作者 Haixiang Ding（丁海祥）</li>
        <li><a href="{GH}" rel="noopener">GitHub 仓库与证据审核文件</a></li>
        <li>姊妹篇：{sister}</li>
      </ul>
      <p class="lic">文字内容采用 <a href="https://creativecommons.org/licenses/by/4.0/deed.zh-hans" rel="noopener">CC BY 4.0</a> 许可，页面代码采用 MIT 许可。页面插图由 AI 生成，仅作装饰示意，不代表真实实验装置。</p>
      <div class="factions"><button type="button" class="btn btn-soft btn-sm" id="printBtn">{svg("print")}打印 / 存为 PDF</button><a class="btn btn-soft btn-sm" href="#top">{svg("up")}回到页首</a></div>
    </div>
  </div>
</footer>
<button type="button" class="backjump" id="backJump" hidden>{svg("back")}回到刚才的位置</button>
<script type="application/json" id="recData">{json.dumps(recdata, ensure_ascii=False).replace('</', '<\\/')}</script>
<script src="{AP}/ev-guidev1.0.js" defer></script>
</body>
</html>
'''
os.makedirs(os.path.dirname(OUT) or '.', exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(PAGE)
print('wrote', OUT, len(PAGE), 'bytes; qc items', qn, '; methods', len(METHODS))
