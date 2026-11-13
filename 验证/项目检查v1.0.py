#!/usr/bin/env python3
"""项目检查 v1.0：离线检查本仓库的链接、引用、图片许可、禁用措辞与许可一致性。
Project check v1.0 (offline): local links/images/anchors, citations, figure licences,
banned phrases, licence consistency, duplicated data files and file naming.
Usage: python3 验证/项目检查v1.0.py   (exit 1 on any error)"""
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
errors, notes = [], []


def err(msg):
    errors.append(msg)


def rel(p):
    return p.relative_to(ROOT).as_posix()


def files(*suffixes):
    for p in sorted(ROOT.rglob("*")):
        if ".git" in p.parts or not p.is_file():
            continue
        if not suffixes or p.suffix in suffixes:
            yield p


# 1. required files ----------------------------------------------------------
REQUIRED = [
    "README.md", "LICENSE", "CITATION.cff", "index.html",
    "LICENSES/CC-BY-NC-4.0.txt", "LICENSES/PolyForm-Noncommercial-1.0.0.md", "LICENSES/CC-BY-4.0.txt",
    "文档/英文说明v1.0.md", "文档/指南正文v1.2.md", "文档/质控清单v1.2.md", "文档/图片说明v1.0.md",
    "文档/主图/封面v1.0.jpg", "示例/推荐规则v1.0.json", "示例/推荐示例v1.0.py", "示例/推荐示例v1.0.md",
    "验证/参考文献v1.1.json", "验证/参考文献v1.1.bib", "验证/陈述核验v1.0.json", "验证/审核报告v1.0.md",
    "图片/文献原图/文献原图说明v1.0.json", "图片/示意图/示意图标注v1.1.json",
    "assets/data/referencesv1.1.json", "assets/data/recommender-rulesv1.0.json",
]
for name in REQUIRED:
    if not (ROOT / name).exists():
        err(f"missing required file {name}")
if len(list((ROOT / "文档/方法").glob("*.md"))) < 13:
    err("文档/方法/ should hold 7 method SOPs + 6 topic files")
if len(list((ROOT / "文档/截图").glob("*.jpg"))) < 4:
    err("文档/截图/ should hold real desktop + mobile screenshots")

# 2. file naming: hyphens + version numbers, no underscores -----------------
EXEMPT = {"README.md", "LICENSE", "CITATION.cff", ".nojekyll", ".gitignore", "index.html"}
for p in files():
    if p.name in EXEMPT or "LICENSES" in p.parts:
        continue
    if "_" in p.name:
        err(f"underscore in file name: {rel(p)}")
    if not re.search(r"v\d+\.\d+", p.name):
        err(f"file name lacks a version number: {rel(p)}")

# 3. local links, images and anchors in Markdown and HTML -------------------
MDLINK = re.compile(r'(?:\]\(([^)\s]+)\)|(?:href|src)="([^"]+)")')


class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("href", "src"):
            if a.get(k):
                self.refs.append(a[k])


def md_anchors(text):
    return set(re.findall(r'<a id="([^"]+)"', text))


def check_target(src, target, html_ids=None):
    if re.match(r"^(https?:|mailto:|data:|javascript:)", target):
        return
    path, _, frag = target.partition("#")
    if not path:
        if html_ids is not None and frag and frag not in html_ids:
            err(f"{rel(src)}: missing anchor #{frag}")
        if src.suffix == ".md" and frag and frag not in md_anchors(src.read_text(encoding="utf-8")):
            err(f"{rel(src)}: missing anchor #{frag}")
        return
    dest = (src.parent / unquote(path)).resolve()
    if not dest.exists():
        err(f"{rel(src)}: missing {target}")
    elif frag and dest.suffix == ".md" and frag not in md_anchors(dest.read_text(encoding="utf-8")):
        err(f"{rel(src)}: missing anchor #{frag} in {path}")


for md in files(".md"):
    if "LICENSES" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in MDLINK.finditer(text):
        check_target(md, m.group(1) or m.group(2))

page = (ROOT / "index.html").read_text(encoding="utf-8")
col = Collect()
col.feed(page)
for t in col.refs:
    check_target(ROOT / "index.html", t, col.ids)

# 4. citations and references ------------------------------------------------
refs = json.loads((ROOT / "验证/参考文献v1.1.json").read_text(encoding="utf-8"))
nref = len(refs)
if nref != 49:
    err(f"expected 49 references, found {nref}")
if [r["number"] for r in refs] != list(range(1, nref + 1)):
    err("reference numbers are not 1..N in order")
for r in refs:
    if not r.get("doi") or not r.get("pmid"):
        err(f"reference [{r['number']}] lacks DOI or PMID")
body = (ROOT / "文档/指南正文v1.2.md").read_text(encoding="utf-8")
cited = {int(x) for g in re.findall(r"\[(\d+(?:,\d+)*)\]", body) for x in g.split(",")}
bad = sorted(n for n in cited if not 1 <= n <= nref)
if bad:
    err(f"指南正文 cites unknown references {bad}")
uncited = sorted(set(range(1, nref + 1)) - cited)
if uncited:
    notes.append(f"references never cited in 指南正文: {uncited}")
page_cites = {int(n) for n in re.findall(r'href="#ref-(\d+)"', page)}
page_ids = {int(n) for n in re.findall(r'id="ref-(\d+)"', page)}
if page_ids != set(range(1, nref + 1)):
    err(f"index.html reference list has {len(page_ids)} entries, expected {nref}")
if page_cites - page_ids:
    err(f"index.html citations without a reference entry: {sorted(page_cites - page_ids)}")
if len(page_cites) != nref:
    err(f"index.html cites {len(page_cites)} distinct references, expected {nref}")
for md in (ROOT / "文档/方法").glob("*.md"):
    for g in re.findall(r"^\[(\d+)\] ", md.read_text(encoding="utf-8"), flags=re.M):
        if not 1 <= int(g) <= nref:
            err(f"{rel(md)}: reference [{g}] out of range")

# 5. figure licences ---------------------------------------------------------
meta = json.loads((ROOT / "图片/文献原图/文献原图说明v1.0.json").read_text(encoding="utf-8"))["figures"]
table = (ROOT / "文档/图片说明v1.0.md").read_text(encoding="utf-8")
if len(meta) != 17:
    err(f"expected 17 literature figures, metadata lists {len(meta)}")
for f in meta:
    fn = f["filename"]
    for name in (fn, fn.replace(".webp", "-sm.webp")):
        if not (ROOT / "图片/文献原图" / name).exists():
            err(f"literature figure file missing: {name}")
    if "creativecommons.org/licenses/by/4.0" not in f.get("license_url", ""):
        err(f"{fn}: licence is not CC BY 4.0")
    if not f.get("doi"):
        err(f"{fn}: no DOI")
    if fn not in table:
        err(f"{fn}: not in 文档/图片说明v1.0.md attribution table")
    if fn not in page:
        err(f"{fn}: not shown on index.html")
real_files = {p.name for p in (ROOT / "图片/文献原图").glob("fig-*.webp") if not p.name.endswith("-sm.webp")}
if real_files != {f["filename"] for f in meta}:
    err(f"图片/文献原图 files and metadata differ: {sorted(real_files ^ {f['filename'] for f in meta})}")
schem = json.loads((ROOT / "图片/示意图/示意图标注v1.1.json").read_text(encoding="utf-8"))["items"]
if len(schem) != 12:
    err(f"expected 12 schematics, metadata lists {len(schem)}")
for s in schem:
    if not (ROOT / "图片/示意图" / s["file"]).exists():
        err(f"schematic missing: {s['file']}")
if page.count("AI 示意图 · 非实验数据") < 12:
    err("index.html: schematics must carry the 'AI 示意图 · 非实验数据' badge")
if page.count("文献原图 · CC BY 4.0") < 17:
    err("index.html: literature figures must carry the 'CC BY 4.0' badge")

# 6. banned phrases (old draft wording); a quoted correction of the old draft is allowed
BANNED = ["至少 3 个", "应缺失", "Pax7", "升升级", "学位课题", "黄金组合"]
for p in [ROOT / "index.html", ROOT / "文档/指南正文v1.2.md", *sorted((ROOT / "文档/方法").glob("*.md")), ROOT / "文档/质控清单v1.2.md"]:
    text = p.read_text(encoding="utf-8")
    for b in BANNED:
        for m in re.finditer(re.escape(b), text):
            if text[max(0, m.start() - 3):m.start()].endswith("原稿“"):
                continue
            err(f"{rel(p)}: banned phrase '{b}'")

# 7. licence consistency ----------------------------------------------------
cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "license: CC-BY-NC-4.0" not in cff or "version: 1.2.0" not in cff:
    err("CITATION.cff must say license: CC-BY-NC-4.0 and version: 1.2.0")
lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
for need in ["CC BY-NC 4.0", "PolyForm Noncommercial", "https://tuanziding.github.io/#contact", "Attribution-NonCommercial 4.0 International"]:
    if need not in lic:
        err(f"LICENSE lacks '{need}'")
foot = " ".join(re.findall(r'<p class="lic">(.*?)</p>', page, flags=re.S))
for need in ["CC BY-NC 4.0", "PolyForm Noncommercial 1.0.0", "商业用途需事先联系作者获得授权合作", "https://tuanziding.github.io/#contact"]:
    if need not in foot:
        err(f"index.html footer lacks '{need}'")
OLD = [r"\bMIT\b", r"文字内容采用[^。]*CC BY 4\.0", r"按 CC BY 4\.0 发布", r"license: CC-BY-4\.0", r"CC BY 4\.0 / MIT"]
for p in files(".md", ".html", ".cff", ".json", ".py", ".yml"):
    if "LICENSES" in p.parts or p.name == "项目检查v1.0.py":
        continue
    text = p.read_text(encoding="utf-8")
    for pat in OLD:
        if re.search(pat, text):
            err(f"{rel(p)}: leftover old licence wording /{pat}/")
for p in [ROOT / "README.md", ROOT / "文档/英文说明v1.0.md"]:
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8")
    for need in ["CC BY-NC 4.0", "PolyForm Noncommercial", "https://tuanziding.github.io/#contact"]:
        if need not in t:
            err(f"{rel(p)} lacks '{need}'")
# no personal e-mail address or phone number published
for p in files(".md", ".html", ".cff", ".json"):
    t = p.read_text(encoding="utf-8")
    if re.search(r"[\w.+-]+@(?:gmail|163|qq|outlook|hotmail)\.com", t) or re.search(r"\b1[3-9]\d{9}\b", t):
        err(f"{rel(p)}: looks like a personal e-mail or phone number")

# 8. duplicated data files must stay identical ------------------------------
def digest(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


for a, b in [("assets/data/referencesv1.1.json", "验证/参考文献v1.1.json"),
             ("assets/data/recommender-rulesv1.0.json", "示例/推荐规则v1.0.json")]:
    if digest(a) != digest(b):
        err(f"{a} and {b} differ")
rules = json.loads((ROOT / "示例/推荐规则v1.0.json").read_text(encoding="utf-8"))["rules"]
if len(rules) != 80:
    err(f"expected 80 recommender rules, found {len(rules)}")
for r in rules:
    for n in r.get("route_ref_numbers", []) + r.get("note_ref_numbers", []):
        if not 1 <= n <= nref:
            err(f"rule {r['sample']}/{r['use']}/{r['priority']} cites [{n}]")
json.loads((ROOT / "验证/陈述核验v1.0.json").read_text(encoding="utf-8"))

for n in notes:
    print("note:", n)
if errors:
    print("\n".join(errors))
    print(f"项目检查未通过 / project check failed: {len(errors)} error(s)")
    sys.exit(1)
print(f"项目检查通过 / project check passed: {nref} references, {len(meta)} literature figures, {len(schem)} schematics, {len(rules)} rules")
