#!/usr/bin/env python3
"""网页检查 v1.2 / Headless check (figure/lightbox/filter checks): screenshots at 390 and 1440, overflow, broken images, JS errors, recommender combos,
citation resolution, reference count, banned old-draft phrases.
Usage: python3 工具/网页检查v1.2.py <url> <shot-prefix>"""
import sys, json
from playwright.sync_api import sync_playwright

url, prefix = sys.argv[1], sys.argv[2]
BANNED = ['至少 3 个', '应缺失', 'Pax7', '升升级', '学位课题', '黄金组合']
report = {'url': url}
with sync_playwright() as p:
    import os, urllib.parse
    kw = {}
    if url.startswith('https://') and os.environ.get('HTTPS_PROXY'):
        u = urllib.parse.urlparse(os.environ['HTTPS_PROXY'])
        kw['proxy'] = {'server': f'{u.scheme}://{u.hostname}:{u.port}', 'username': urllib.parse.unquote(u.username or ''), 'password': urllib.parse.unquote(u.password or '')}
    if os.environ.get('CHROME_PATH'): kw['executable_path'] = os.environ['CHROME_PATH']
    b = p.chromium.launch(**kw)
    for w, h in [(390, 844), (1440, 900)]:
        ctx = b.new_context(ignore_https_errors=True, viewport={'width': w, 'height': h}, device_scale_factor=2 if w == 390 else 1,
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
        r['broken_images'] = pg.evaluate("Array.from(document.images).filter(i => i.getAttribute('src')).filter(i => { i.loading='eager'; return !(i.complete && i.naturalWidth>0) }).map(i=>i.src)")
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
            r['figs'] = pg.evaluate('''() => {
              const real = Array.from(document.querySelectorAll('.rfig, .rmini'));
              const badReal = real.filter(f => !(f.querySelector('.fbadge.real') && f.querySelector('.attr a[href^="https://doi.org/"]') && f.querySelector('.attr a[href*="creativecommons.org/licenses/by/4.0"]') && /Reproduced from .+ CC BY 4\\.0, no changes/.test(f.querySelector('.attr').textContent))).map(f => f.id || f.querySelector('.ft').textContent);
              const sch = Array.from(document.querySelectorAll('.schem'));
              const badSch = sch.filter(f => !f.querySelector('.fbadge.ai') || !/AI 示意图 · 非实验数据/.test(f.querySelector('.fbadge.ai').textContent)).map(f => f.id);
              const imgs = Array.from(document.querySelectorAll('figure img'));
              const noDim = imgs.filter(i => !i.getAttribute('width') || !i.getAttribute('height') || i.getAttribute('loading') !== 'lazy' || !/[.]webp/.test(i.getAttribute('src'))).map(i => i.src);
              const pinsBad = sch.map(f => { const b = f.querySelector('.simg').getBoundingClientRect(); return Array.from(f.querySelectorAll('.pin')).filter(p => { const r = p.getBoundingClientRect(); return r.left < b.left - 1 || r.left > b.right + 1 || r.top < b.top - 1 || r.top > b.bottom + 1; }).length; }).reduce((a, c) => a + c, 0);
              return {real_cards: document.querySelectorAll('.rfig').length, real_minis: document.querySelectorAll('.rmini').length, schematics: sch.length, badReal, badSch, noDim, pinsOutside: pinsBad,
                      keyVisible: getComputedStyle(document.querySelector('.schem .key')).display, chipVisible: getComputedStyle(document.querySelector('#sc-overview .pin span')).display};
            }''')
            # filter
            filt = {}
            for f in ['尿液', '脑脊液', '唾液', 'all']:
                pg.click(f'.ftab[data-f="{f}"]')
                filt[f] = pg.evaluate("[document.querySelectorAll('.rfig:not([hidden])').length, document.querySelectorAll('.rgroup:not([hidden])').length]")
            r['filter'] = filt
            # lightbox
            pg.evaluate("document.getElementById('realfigs').scrollIntoView({behavior:'instant'})")
            pg.click('.rfig .fzoom >> nth=0'); pg.wait_for_timeout(700)
            r['lb_open'] = pg.evaluate("({open: document.getElementById('lb').open, src: document.getElementById('lbImg').getAttribute('src'), loaded: document.getElementById('lbImg').naturalWidth, title: document.getElementById('lbTitle').textContent.slice(0,30), attr: !!document.querySelector('#lbAttr .attr a[href^=\"https://doi.org/\"]'), focus: document.activeElement.id})")
            pg.screenshot(path=f'{prefix}-{w}-lightbox.png')
            pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
            r['lb_after_esc'] = pg.evaluate("({open: document.getElementById('lb').open, focusIsOpener: document.activeElement.matches('a[data-lb]')})")
            pg.click('.schem .fzoom >> nth=0', force=True); pg.wait_for_timeout(500)
            r['lb_schem'] = pg.evaluate("({open: document.getElementById('lb').open, badge: document.getElementById('lbBadge').textContent})")
            pg.click('#lbClose'); pg.wait_for_timeout(200)
            r['lb_after_close'] = pg.evaluate("document.getElementById('lb').open")
            r['refs'] = pg.evaluate("({n: document.querySelectorAll('.reflist li').length, doi: document.querySelectorAll('.reflist a[href^=\"https://doi.org/\"]').length, pmid: document.querySelectorAll('.reflist a[href^=\"https://pubmed\"]').length})")
            txt = pg.evaluate('document.documentElement.outerHTML')
            r['banned_found'] = [x for x in BANNED if x in txt.replace('原稿“' + x, '')]
            r['labels'] = {k: txt.count(k) for k in ['【实验室惯例', '【估算】', '定性共识']}
            pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{prefix}-{w}-top.png')
        pg.screenshot(path=f'{prefix}-{w}-full.png', full_page=True)
        if w == 390:
            for sec in ['rec', 'methods', 'compare', 'workflow', 'qc', 'refs']:
                pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})"); pg.wait_for_timeout(300)
                pg.screenshot(path=f'{prefix}-{w}-{sec}.png')
        else:
            pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
            r['figs'] = pg.evaluate("({keyVisible: getComputedStyle(document.querySelector('#sc-duc .key')).display, chipVisible: getComputedStyle(document.querySelector('#sc-duc .pin span')).display, qcChip: getComputedStyle(document.querySelector('#sc-nta .pin span')).display})")
            pg.click('.rmini .fzoom >> nth=0'); pg.wait_for_timeout(700)
            r['lb_open'] = pg.evaluate("({open: document.getElementById('lb').open, loaded: document.getElementById('lbImg').naturalWidth})")
            pg.screenshot(path=f'{prefix}-{w}-lightbox.png')
            pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
            r['lb_after_esc'] = pg.evaluate("document.getElementById('lb').open")
            for sec in ['rec', 'methods', 'compare', 'qc']:
                pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})"); pg.wait_for_timeout(300)
                pg.screenshot(path=f'{prefix}-{w}-{sec}.png')
        pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
        for sid in pg.evaluate("Array.from(document.querySelectorAll('.schem')).map(f=>f.id)"):
            el = pg.query_selector('#' + sid); el.scroll_into_view_if_needed(); pg.wait_for_timeout(250)
            el.screenshot(path=f'{prefix}-{w}-{sid}.png')
        for sec in ['realfigs', 'samples', 'm-2']:
            pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})"); pg.wait_for_timeout(400)
            pg.screenshot(path=f'{prefix}-{w}-{sec}.png')
        report[str(w)] = r
        ctx.close()
    b.close()
print(json.dumps(report, ensure_ascii=False, indent=1))
