#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SOP 11 QA: 9 gates for the 10 v1.5.x articles."""
import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CONTENT = "content"
PREVIEW = "_hugo_preview"
ARTICLES = [
    "v150-patch-breakdown", "v151-153-hotfix-breakdown", "steam-deck-settings-guide",
    "barter-gambit-guide", "enemy-powers-warning-guide", "controller-gamepad-guide",
    "strain-system-guide", "graveyard-stalemate-reset-guide", "post-15-new-player-guide",
    "ui-text-readability-guide",
]
BANNED = {"\u2014": "em-dash", "\u2013": "en-dash", "\u2018": "lq", "\u2019": "rq",
          "\u201c": "ldq", "\u201d": "rdq", "\u2026": "ellipsis"}

def render_check(name, slug):
    """Check rendered HTML in preview."""
    idx = os.path.join(PREVIEW, slug, "index.html")
    if not os.path.exists(idx):
        return None
    html = open(idx, encoding="utf-8").read()
    res = {}
    # shortcode count
    res["shortcodes"] = len(re.findall(r'class="callout|class="diagram|section-divider|table-wrap', html))
    res["tables"] = html.count("<table")
    res["lists"] = html.count("<ul") + html.count("<ol")
    res["internal_links"] = len(re.findall(r'href="/[a-z0-9\-]+/"', html))
    res["external_links"] = len(re.findall(r'href="https?://', html))
    res["raw_shortcode_leak"] = ("{{<" in html) or ("{{%" in html)
    res["svg_present"] = (".svg" in html) or ('<svg' in html)
    res["img_count"] = html.count("<img")
    return res

print("=" * 90)
print("SOP 11 QA: 10 v1.5.x articles")
print("=" * 90)

all_ok = True
for slug in ARTICLES:
    md_path = os.path.join(CONTENT, slug + ".md")
    raw = open(md_path, "rb").read()
    txt = raw.decode("utf-8")
    fm, body = txt.split("---", 2)[1], txt.split("---", 2)[2]

    issues = []
    # Gate 1: BOM
    if raw[:3] == b"\xef\xbb\xbf":
        issues.append("BOM")
    # Gate 2: banned unicode
    for ch, lab in BANNED.items():
        if ch in txt:
            issues.append("unicode:" + lab)
    # Gate 3: emoji in body (non-ASCII outside allowed)
    emoji = re.findall(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]', txt)
    if emoji:
        issues.append("emoji:%s" % "".join(sorted(set(emoji))))
    # Gate 4: shortcodes >= 8
    sc = len(re.findall(r'\{\{<', body))
    if sc < 8:
        issues.append("shortcodes=%d(<8)" % sc)
    # Gate 5: icons >= 2  (diagrams + callouts count as visual)
    icons = len(re.findall(r'src="[^"]+\.svg"', body)) + len(re.findall(r'\{\{< callout', body))
    if icons < 2:
        issues.append("visual=%d(<2)" % icons)
    # Gate 6: word count >= 600
    wc = len(re.sub(r'\{\{[^}]+\}\}', '', body).split())
    if wc < 600:
        issues.append("wc=%d(<600)" % wc)
    # Gate 7: data components >= 2 (tables + lists)
    data = len(re.findall(r'^\|', body, re.M)) and body.count("\n|") or 0
    tables = body.count("\n|---") + body.count("|---|")
    lists = len(re.findall(r'^\d+\.\s|^- ', body, re.M))
    data_comp = (1 if tables else 0) + (1 if lists >= 5 else 0)
    if data_comp < 2:
        issues.append("data=%d(<2) tbl=%d lst=%d" % (data_comp, tables, lists))
    # Gate 8: internal links >= 1
    ilinks = len(re.findall(r'\]\(/[a-z0-9\-]+/\)', body))
    if ilinks < 1:
        issues.append("ilinks=%d(<1)" % ilinks)
    # Gate 9: resourcegrid (Community Resources)
    if "Community Resources" not in body:
        issues.append("no Community Resources")

    status = "PASS" if not issues else "FAIL"
    if issues:
        all_ok = False
    print("\n%-45s [%s]  words~%d shortcodes=%d ilinks=%d" % (slug + ".md", status, wc, sc, ilinks))
    for i in issues:
        print("    ! " + i)

    # rendered check if available
    r = render_check(slug, slug)
    if r:
        leaks = "LEAK" if r["raw_shortcode_leak"] else "ok"
        print("    rendered: tables=%d lists=%d ilinks=%d ext=%d svg=%s leak=%s" % (
            r["tables"], r["lists"], r["internal_links"], r["external_links"], r["svg_present"], leaks))
    else:
        print("    rendered: (not in preview)")

print("\n" + "=" * 90)
print("ALL PASS" if all_ok else "SOME FAILED")
