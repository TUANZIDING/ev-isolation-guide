#!/usr/bin/env python3
"""Headless check: screenshots at 390 and 1440, overflow, broken images, JS errors, recommender combos,
citation resolution, reference count, banned old-draft phrases.
Usage: python3 check-pagev1.0.py <url> <shot-prefix>"""
import sys, json
from playwright.sync_api import sync_playwright

url, prefix = sys.argv[1], sys.argv[2]
BANNED = ['至少 3 个', '应缺失', 'Pax7', '升升级', '学位课题', '黄金组合']
report = {'url': url}
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h in [(390, 844), (1440, 900)]:
        ctx = b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2 if w == 390 else 1,
                            user_agent=('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' if w == 390 else None))
        pg = ctx.new_page()
        errs, bad = [], []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append('console:' + m.text) if m.type == 'error' else None)
        pg.on('response', lambda r: bad.append(f'{r.status} {r.url}') if r.status >= 400 else None)
        pg.goto(url, wait_until='networkidle')
        pg.wait_for_timeout(600)
        r = {}
        r['errors'] = errs; r['bad_responses'] = bad
        r['doc_width'] = pg.evaluate('document.documentElement.scrollWidth'); r['viewport'] = w
        r['overflowing'] = pg.evaluate('''() => { const W = document.documentElement.clientWidth; const out=[];
          document.querySelectorAll('body *').forEach(el => { const b = el.getBoundingClientRect();
            if (b.width && (b.right > W + 1 || b.left < -1)) { let p = el.parentElement, clipped=false;
              while (p && p!==document.body) { const s=getComputedStyle(p); if (/(auto|scroll|hidden)/.test(s.overflowX)) {clipped=true;break;} p=p.parentElement; }
              if (!clipped && getComputedStyle(el).position!=='fixed') out.push(el.tagName+'.'+el.className+' '+Math.round(b.left)+'..'+Math.round(b.right)); } });
          return out.slice(0,15); }''')
        pg.evaluate("document.documentElement.style.scrollBehavior='auto';document.querySelectorAll('img').forEach(i=>i.loading='eager'); document.getElementById('qc').scrollIntoView({behavior:'instant'})"); pg.wait_for_timeout(1000); pg.evaluate("window.scrollTo(0,0)")
        r['broken_images'] = pg.evaluate("Array.from(document.images).filter(i => { i.loading='eager'; return !(i.complete && i.naturalWidth>0) }).map(i=>i.src)")
        if w == 390:
            # recommender combos
            combos = [('culture', 'func', 'gentle'), ('plasma', 'omics', 'purity'), ('urine', 'biomarker', 'yield'), ('tissue', 'routine', 'scale'), ('otherfluid', 'func', 'purity')]
            rec = []
            for s, u, pr in combos:
                for k, v in [('sample', s), ('use', u), ('priority', pr)]:
                    pg.click(f'input[name={k}][value={v}]', force=True)
                rec.append(pg.evaluate("({sel:document.querySelector('#roSel').textContent, route:document.querySelector('#roRoute').innerText.replace(/\\n/g,' '), note:document.querySelector('#roNote').innerText.slice(0,60), global:document.querySelectorAll('#roGlobal li').length})"))
            r['recommender'] = rec
            # stepper
            pg.click('#sNext'); pg.click('#sNext')
            r['stepper'] = pg.evaluate("[document.querySelector('#sCount').textContent, document.querySelectorAll('.step.on').length, document.querySelector('.step.on h3').innerText]")
            # QC persist
            pg.click('.qitem >> nth=0'); pg.click('.qitem >> nth=2')
            pg.reload(wait_until='networkidle')
            r['qc_after_reload'] = pg.evaluate("document.querySelector('#qCount').textContent")
            pg.click('#qReset')
            r['qc_after_reset'] = pg.evaluate("document.querySelector('#qCount').textContent")
            # citations
            r['cites'] = pg.evaluate('''() => { const as = Array.from(document.querySelectorAll('.cite a')); const miss = as.filter(a => !document.getElementById(a.getAttribute('href').slice(1)));
              const used = new Set(as.map(a=>a.getAttribute('href'))); return {n: as.length, missing: miss.length, distinct: used.size}; }''')
            r['refs'] = pg.evaluate("({n: document.querySelectorAll('.reflist li').length, doi: document.querySelectorAll('.reflist a[href^=\"https://doi.org/\"]').length, pmid: document.querySelectorAll('.reflist a[href^=\"https://pubmed\"]').length})")
            txt = pg.evaluate('document.documentElement.outerHTML')
            r['banned_found'] = [x for x in BANNED if x in txt]
            r['labels'] = {k: txt.count(k) for k in ['【实验室惯例', '【估算】', '定性共识']}
            pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{prefix}-{w}-top.png')
        pg.screenshot(path=f'{prefix}-{w}-full.png', full_page=True)
        if w == 390:
            for sec in ['rec', 'methods', 'compare', 'workflow', 'qc', 'refs']:
                pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})"); pg.wait_for_timeout(300)
                pg.screenshot(path=f'{prefix}-{w}-{sec}.png')
        else:
            for sec in ['rec', 'methods', 'compare', 'qc']:
                pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})"); pg.wait_for_timeout(300)
                pg.screenshot(path=f'{prefix}-{w}-{sec}.png')
        report[str(w)] = r
        ctx.close()
    b.close()
print(json.dumps(report, ensure_ascii=False, indent=1))
