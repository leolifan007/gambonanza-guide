# Gambonanza Guide 鈥?Comprehensive Project State (2026-05-15)

> This document captures the complete current state of the Gambonanza Guide project.
> A new session can pick this up and continue work seamlessly.

---

## ✅ Project Identity

| Field | Value |
|-------|-------|
| **Site** | Gambonanza Guide (Steam App ID 3509230) |
| **Domain** | https://gambonanzaguide.com/ |
| **GitHub** | `leolifan007/gambonanza-guide` |
| **Tech Stack** | Hugo v0.161.1 + GitHub Pages (gh-pages orphan branch) |
| **Analytics** | GA4 G-KCX7SWRL8B |
| **AdSense** | pub-7551387157478980 (ads.txt deployed, placeholders hidden, not yet submitted) |
| **Search Console** | DNS verification passed |

---

## 馃搧 Project Structure

```
C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\
鈹溾攢鈹€ layouts/                    鈫?All HTML templates (NOT inside theme)
鈹?  鈹溾攢鈹€ _default/
鈹?  鈹?  鈹溾攢鈹€ baseof.html         鈫?Base template (Google Fonts JS, CSS version)
鈹?  鈹?  鈹斺攢鈹€ single.html         鈫?Article page template
鈹?  鈹溾攢鈹€ partials/
鈹?  鈹?  鈹溾攢鈹€ header.html         鈫?Nav header (Steam buy btn, no lang-bar)
鈹?  鈹?  鈹溾攢鈹€ footer.html         鈫?Footer
鈹?  鈹?  鈹溾攢鈹€ page-header.html    鈫?Sub-page hero section
鈹?  鈹?  鈹溾攢鈹€ ads.html            鈫?AdSense ad slots
鈹?  鈹?  鈹斺攢鈹€ cookie-banner.html  鈫?Cookie consent banner
鈹?  鈹斺攢鈹€ index.html              鈫?Homepage (hero, Latest Guides cards)
鈹溾攢鈹€ content/                    鈫?22 .md files (all in English)
鈹溾攢鈹€ themes/gambonanza-theme/
鈹?  鈹斺攢鈹€ static/css/style.css    鈫?SOURCE CSS (~1000+ lines, CSS vars, responsive)
鈹溾攢鈹€ static/
鈹?  鈹溾攢鈹€ CNAME                   鈫?gambonanzaguide.com
鈹?  鈹溾攢鈹€ ads.txt
鈹?  鈹溾攢鈹€ robots.txt
鈹?  鈹斺攢鈹€ images/                 鈫?Hero bg, SVG diagrams, etc.
鈹溾攢鈹€ _deploy.py                  鈫?Atomically deploys (no delete, no 404 gap)
鈹斺攢鈹€ hugo.toml                   鈫?baseURL = https://gambonanzaguide.com/
```

### IMPORTANT: Template Location
Templates are at the **project root** `layouts/`, NOT inside the theme. The theme only provides `style.css`. Do NOT look for templates inside `themes/gambonanza-theme/layouts/` 鈥?they don't exist there.

---

## 馃帹 Current Visual State (as of 2026-05-15)

### What's Live
| Component | Status |
|-----------|--------|
| Pixel font headings | 鉁?"Press Start 2P" via Google Fonts (scaled to ~33% of default, monospace) |
| Body text | 鉁?Inter font (unchanged) |
| Homepage cards | 鉁?Gradient (#1a0f1a) background, full-click `<a>` wrapper, NEW badge system |
| Sub-page hero | 鉁?Hero bg image (cropped top) + gradient overlay |
| Nav bar | 鉁?white-space: nowrap, Steam buy button |
| Cookie consent | 鉁?Implemented |
| AdSense slots | 鉁?Placeholders hidden, real ID ready |
| Google Translate | 鉂?REMOVED from header, REMOVED from sidebar |
| CTA/buy widget | 鉂?REMOVED from sub-pages |

### NEW Badge System (added 2026-05-15)
- `.new-badge`: absolute positioned, red gradient (#e63946 鈫?#c1121f), pixel font, drop shadow
- Applied to `.latest-article-card` which has `position: relative`
- Card ordering: newest first (Recommended Seeds May 15 鈫?King of Spades May 11 鈫?...)

---

## 馃搫 Content Inventory (22 files, all English)

### Homepage
- `_index.md` 鈥?Site landing page (4,962 bytes)

### Core Reference Pages
| File | Size | Last Updated |
|------|------|-------------|
| `gambits.md` | 19,647 B | May 11 |
| `bosses.md` | 19,645 B | May 11 |
| `cards.md` | 7,894 B | May 11 |
| `economy.md` | 8,512 B | May 11 |
| `strategy.md` | 10,311 B | May 11 |
| `achievements.md` | 7,299 B | May 11 |
| `beginner.md` | 13,567 B | May 11 |
| `faq.md` | 11,431 B | May 11 |
| `gambonanza-tier-list.md` | 17,969 B | May 11 |
| `contact.md` | 10,266 B | 鈥?|
| `privacy.md` | 19,314 B | 鈥?|

### Guide / Walkthrough Pages (staggered release batch)
| File | Size | Release Date | Status |
|------|------|-------------|--------|
| `boss-strategy-guide.md` | 5,781 B | May 12 13:22 | 鉁?Live |
| `complete-walkthrough.md` | 5,308 B | May 14 09:53 | 鉁?Live |
| `recommended-seeds.md` | 3,594 B | **May 15 11:42** | 鉁?Live + NEW badge |
| `endgame-killer-tips.md` | 5,293 B | May 16 15:31 | 馃搮 Not yet in Latest Guides |
| `rook-bishop-guide.md` | 5,685 B | May 18 09:17 | 馃搮 Not yet in Latest Guides |
| `4x4-fast-farm-guide.md` | 4,151 B | Batch 1 (May 11) | 鉁?Live |
| `decision-framework-guide.md` | 6,466 B | Batch 1 (May 11) | 鉁?Live |
| `deterministic-gambits-guide.md` | 6,998 B | Batch 1 (May 11) | 鉁?Live |
| `king-of-spades-guide.md` | 7,027 B | Batch 1 (May 11) | 鉁?Live |
| `pawn-promotion-sustainability-guide.md` | 6,279 B | Batch 1 (May 11) | 鉁?Live |

---

## 馃摝 Deployment

### Deploy Script (`_deploy.py`)
- Must run from `projects/gambonanza-guide/` directory
- Workflow: `hugo` 鈫?create gh-pages orphan branch 鈫?`git push origin gh-pages --force`
- **CRITICAL RULE**: Never delete gh-pages branch first (causes 404). Only force push.
- To deploy: `python _deploy.py`
- After deploy, commit main: `git add -A && git commit -m "message" && git push origin main --force`

### Git Branches
- **main**: Source code (layouts/, content/, themes/, static/, hugo.toml, _deploy.py)
- **gh-pages**: Orphan branch, only built public/ output
- **local orphan branches** created during deploy are temporary

### baseURL
Currently: `https://gambonanzaguide.com/` (the real domain, working)
If domain changes 鈫?must update `hugo.toml` before next build.

### Hugo Build Note
Sometimes Hugo cache prevents `public/css/style.css` from regenerating. 
**Fix**: Delete `public/` folder before `hugo` (or re-run `hugo --minify`).
Always verify `public/css/style.css` has changes before deploying.

---

## 馃敡 Known Issues & TODOs

### Urgent
- [ ] **Screenshots for content pages** 鈥?6 Steam screenshots downloaded but never embedded into .md files. Needs WebP conversion (quality 80, max 250KB each).
- [ ] **sitemap.xml submission** to Google Search Console (user chose to delay)
- [ ] **Gambonanza绔欏唴瀹归〉闈㈠畬鏁村害纭**: gambits/bosses/economy/cards/strategy all exist but need visual polish
- [x] **sitemap.xml 涓?public/sitemap.xml 鍚屾** (2026-05-18): 婧愮爜 sitemap.xml 琛ュ厖浜?绡囩己澶遍〉闈紙blitzking-boss-guide, combo-chain-guide, crumble-mechanic-guide, queen-supremacy-guide, tile-control-guide, endgame-killer-tips锛?

### Pending (staggered release)
- [x] Day 5 (May 16 15:31): Add **Endgame Killer Tips** to homepage Latest Guides 鉁?
- [x] Day 7 (May 18 09:17): Add **Rook & Bishop Guide** to homepage Latest Guides 鉁?

### Future
- [ ] AdSense鍒濆鎻愪氦锛堝煙鍚嶈喘鍏ュ悗锛?
- [ ] 鎺ㄥ箍绛栫暐鍒跺畾锛圧eddit/Steam绀惧尯/GameFAQs锛?
- [ ] Employee A: 閲嶆柊绛涢€夊墠5涓€夐锛堣仛鐒︾嫭绔?涓皬鍨嬫父鎴忥級
- [ ] Employee B: 璁捐閫氱敤Wiki鐩綍妯℃澘
- [ ] Outworld Station guide: `leolifan007/outworld-station-guide` (Actions deployment pending, domain not yet configured)

---

## 馃洜锔?Operating SOPs

### Content Rules
1. **All content must be in English** 鈥?global audience, no Chinese guide pages
2. **First-person voice** 鈥?write from "I tested / I found / In my runs" perspective. NEVER "data compiled from / community reports / sources say / this guide covers"
3. **New pages need clickable entry** 鈥?add to homepage Latest Guides, nav, or footer. No orphan pages.
4. **Staggered release** 鈥?1-2 days per article, random non-round times. New pages: wait 12-24h before adding homepage entry.
5. **SEO-safe tone** (post-GSC-audit):
   - 鉁?"From my own runs" / "I've tested"
   - 鉁?"Here's what works"
   - 鉂?"According to community reports" / "Data compiled from" / "Sources: Steam discussions"
   - 鉂?"Based on Prima Games review" (citing competitors)

### Design Rules
1. **Responsive**: mobile-first (320px min), key breakpoints at 480/768/1024
2. **Components required**: callout boxes, meta-badge/rating, pro-tip (gold border), phase-tag, synergy-table
3. **Images**: WebP format only, quality 80, max 250KB, loading="lazy" with w/h attributes
4. **Heading font**: "Press Start 2P" (pixel/monospace style), body font: Inter
5. **No Google Translate** 鈥?lang-bar and sidebar translator removed
6. **No CTA/buy widget** on sub-pages 鈥?only Steam buy button in header

### Deployment Rules
1. `baseURL` must match the live domain 鈥?never change to github.io
2. gh-pages deploy: only `git push --force`, never `git push :gh-pages` (delete)
3. After deploy, always verify site is serving 200 OK
4. Version stamping: every page should have version + Last Updated date (current: v1.1.0)
5. **銆愰噸瑕併€慡itemap 鍚屾瑙勫垯**: 姣忔鎵ц缃戠珯鑷姩鏇存柊宸ヤ綔鏃讹紙鍖呮嫭 Hugo 鏋勫缓閮ㄧ讲銆佸彂甯冩柊鏂囩珷銆佷慨鏀归〉闈級锛屽繀椤诲悓姝ユ洿鏂?`sitemap.xml`銆傛祦绋嬶細Hugo 鏋勫缓瀹屾垚鍚庯紝灏?`public/sitemap.xml` 鐨勫唴瀹瑰畬鏁磋鐩栧埌椤圭洰鏍圭洰褰曠殑 `sitemap.xml`锛岀劧鍚?git commit push銆傛椂闂存埑浠ュ綋澶╂洿鏂板紑鏀惧閾剧殑鏃堕棿涓哄噯銆?

### 404 Recovery (if it happens again)
Root cause: `git push origin :gh-pages` (delete) creates a gap. Fix:
1. Rebuild: `hugo`
2. Create orphan: `git checkout --orphan gh-pages && git rm -rf .`
3. Copy public/*, commit, `git push origin gh-pages --force` (no delete step)
4. Verify CNAME in gh-pages branch exists

---

## 馃挕 Lessons Learned (hard-won)

1. **gh-pages delete = 404**. Never delete gh-pages branch. Only force-push with replacement.
2. **Hugo CSS cache bug**. Source CSS changes may not trigger public/ regeneration. Delete public/ or re-run hugo.
3. **Templates are at project root**, not inside theme. Theme only provides CSS.
4. **PowerShell encoding**: Avoid `Set-Content` and `>` for Unicode. Use Python for file writes.
5. **Steam community interaction**: `web_fetch` blocked by sandbox. xbrowser works but CDP evaluate is unavailable. Steam cookie persists though.
6. **xbrowser refs**: `@ref` is temporary. DOM changes require new snapshot -i.
7. **Orphan branch management**: deploy-v2 had correct CSS changes but commit wasn't on main branch 鈫?lost. Always merge visual changes back to main.

---

## 馃搵 Git Tips

```
# Deploy
cd C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide
python _deploy.py

# Commit source to main
git add -A
git commit -m "message"
git push origin main --force

# Deploy = main + gh-pages both pushed
```

---

## 鈿狅笍 Critical Notes for New Session
1. **The _fix_all.py and other temp scripts have been cleaned up.** Don't assume they exist.
2. **All GSC red-flag text has been removed** from all 22 content files. Don't re-add phrases like "community reports", "data compiled", "Prima Games", "this guide covers", etc.
3. The public/ directory may contain stale CSS. If CSS changes don't show, delete public/ first.
4. The stale `.html` files mixed in the project root (4x4-fast-farm-guide/index.html etc.) are old artifacts from a pre-Hugo version. They sit alongside the project but are NOT part of the Hugo build.

