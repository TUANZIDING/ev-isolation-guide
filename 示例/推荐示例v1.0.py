#!/usr/bin/env python3
"""推荐示例 v1.0：按“样本 × 用途 × 优先指标”从 推荐规则v1.0.json 查起点方案（与网页推荐器同一份规则）。
Recommender example v1.0: look up a starting route by sample × use × priority from 推荐规则v1.0.json.
Usage: python3 示例/推荐示例v1.0.py [sample] [use] [priority]
   e.g. python3 示例/推荐示例v1.0.py plasma omics purity
Run without arguments to list the allowed keys. 不联网 / offline. 起点方案，非规定；需本实验室小试验证。"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES = json.loads((HERE / "推荐规则v1.0.json").read_text(encoding="utf-8"))
REFS = {r["number"]: r for r in json.loads((HERE.parent / "验证" / "参考文献v1.1.json").read_text(encoding="utf-8"))}
L = RULES["labels"]


def cite(nums):
    return "; ".join(f"[{n}] {REFS[n]['authors'][0]} {REFS[n]['year']}, doi:{REFS[n]['doi']}" for n in nums)


def recommend(sample, use, priority):
    for r in RULES["rules"]:
        if (r["sample"], r["use"], r["priority"]) == (sample, use, priority):
            return r
    raise KeyError((sample, use, priority))


def main(argv):
    if len(argv) != 4:
        for k in ("sample", "use", "priority"):
            print(k + ":", ", ".join(f"{a}={b}" for a, b in L[k].items()))
        print(__doc__.split("Usage:")[1].split("Run")[0].strip())
        return 0
    s, u, p = argv[1:]
    r = recommend(s, u, p)
    print(f"选择 / Selection: {L['sample'][s]} · {L['use'][u]} · {L['priority'][p]}")
    print(f"起点路线 / Route: {r['route']}")
    print(f"  依据 / Evidence: {cite(r['route_ref_numbers'])}" if r["route_ref_numbers"] else "  依据：【实验室惯例】")
    print(f"关键注意 / Note: {r['note']}")
    if r.get("note_ref_numbers"):
        print(f"  依据 / Evidence: {cite(r['note_ref_numbers'])}")
    print("通用规则 / Global rules:")
    for g in RULES["global_rules"]:
        print(f"  - {g['rule']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
