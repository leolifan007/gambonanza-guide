# Gambonanza Guide — Comprehensive Project State (2026-05-15)

> This document captures the complete current state of the Gambonanza Guide project.
> A new session can pick this up and continue work seamlessly.

---

## 🎯 Project Identity

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

## 📁 Project Structure

```
C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\
├── layouts/                    ← All HTML templates (NOT inside theme)
│   ├── _default/
│   │   ├── baseof.html         ← Base template (Google Fonts JS, CSS version)
│   │   └── single.html         ← Article page template
│   ├── partials/
│   │   ├── header.html         ← Nav header (Steam buy btn, no lang-bar)
│   │   ├── footer.html         ← Footer
│   │   ├── page-header.html    ← Sub-page hero section
│   │   ├── ads.html            ← AdSense ad slots
│   │   └── cookie-banner.html  ← Cookie consent banner
│   └── index.html              ← Homepage (hero, Latest Guides cards)
├── content/                    ← 22 .md files (all in English)
├── themes/gambonanza-theme/
│   └── static/css/style.css    ← SOURCE CSS (~1000+ lines, CSS vars, responsive)
├── static/
│   ├── CNAME                   ← gambonanzaguide.com
│   ├── ads.txt
│   ├── robots.txt
│   └── images/                 ← Hero bg, SVG diagrams, etc.
├── _deploy.py                  ← Atomically deploys (no delete, no 404 gap)
└── hugo.toml                   ← baseURL = https://gambonanzaguide.com/
```

### IMPORTANT: Template Location
Templates are at the **project root** `layouts/`, NOT inside the theme. The theme only provides `style.css`. Do NOT look for templates inside `themes/gambonanza-theme/layouts/` — they don't exist there.

---

## 🎨 Current Visual State (as of 2026-05-15)

### What's Live
| Component | Status |
|-----------|--------|
| Pixel font headings | ✅ "Press Start 2P" via Google Fonts (scaled to ~33% of default, monospace) |
| Body text | ✅ Inter font (unchanged) |
| Homepage cards | ✅ Gradient (#1a0f1a) background, full-click `<a>` wrapper, NEW badge system |
| Sub-page hero | ✅ Hero bg image (cropped top) + gradient overlay |
| Nav bar | ✅ white-space: nowrap, Steam buy button |
| Cookie consent | ✅ Implemented |
| AdSense slots | ✅ Placeholders hidden, real ID ready |
| Google Translate | ❌ REMOVED from header, REMOVED from sidebar |
| CTA/buy widget | ❌ REMOVED from sub-pages |

### NEW Badge System (added 2026-05-15)
- `.new-badge`: absolute positioned, red gradient (#e63946 → #c1121f), pixel font, drop shadow
- Applied to `.latest-article-card` which has `position: relative`
- Card ordering: newest first (Recommended Seeds May 15 → King of Spades May 11 → ...)

---

## 📄 Content Inventory (22 files, all English)

### Homepage
- `_index.md` — Site landing page (4,962 bytes)

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
| `contact.md` | 10,266 B | — |
| `privacy.md` | 19,314 B | — |

### Guide / Walkthrough Pages (staggered release batch)
| File | Size | Release Date | Status |
|------|------|-------------|--------|
| `boss-strategy-guide.md` | 5,781 B | May 12 13:22 | ✅ Live |
| `complete-walkthrough.md` | 5,308 B | May 14 09:53 | ✅ Live |
| `recommended-seeds.md` | 3,594 B | **May 15 11:42** | ✅ Live + NEW badge |
| `endgame-killer-tips.md` | 5,293 B | May 16 15:31 | 📅 Not yet in Latest Guides |
| `rook-bishop-guide.md` | 5,685 B | May 18 09:17 | 📅 Not yet in Latest Guides |
| `4x4-fast-farm-guide.md` | 4,151 B | Batch 1 (May 11) | ✅ Live |
| `decision-framework-guide.md` | 6,466 B | Batch 1 (May 11) | ✅ Live |
| `deterministic-gambits-guide.md` | 6,998 B | Batch 1 (May 11) | ✅ Live |
| `king-of-spades-guide.md` | 7,027 B | Batch 1 (May 11) | ✅ Live |
| `pawn-promotion-sustainability-guide.md` | 6,279 B | Batch 1 (May 11) | ✅ Live |

---

## 📦 Deployment

### Deploy Script (`_deploy.py`)
- Must run from `projects/gambonanza-guide/` directory
- Workflow: `hugo` → create gh-pages orphan branch → `git push origin gh-pages --force`
- **CRITICAL RULE**: Never delete gh-pages branch first (causes 404). Only force push.
- To deploy: `python _deploy.py`
- After deploy, commit main: `git add -A && git commit -m "message" && git push origin main --force`

### Git Branches
- **main**: Source code (layouts/, content/, themes/, static/, hugo.toml, _deploy.py)
- **gh-pages**: Orphan branch, only built public/ output
- **local orphan branches** created during deploy are temporary

### baseURL
Currently: `https://gambonanzaguide.com/` (the real domain, working)
If domain changes → must update `hugo.toml` before next build.

### Hugo Build Note
Sometimes Hugo cache prevents `public/css/style.css` from regenerating. 
**Fix**: Delete `public/` folder before `hugo` (or re-run `hugo --minify`).
Always verify `public/css/style.css` has changes before deploying.

---

## 🔧 Known Issues & TODOs

### Urgent
- [ ] **Screenshots for content pages** — 6 Steam screenshots downloaded but never embedded into .md files. Needs WebP conversion (quality 80, max 250KB each).
- [ ] **sitemap.xml submission** to Google Search Console (user chose to delay)
- [ ] **Gambonanza站内容页面完整度确认**: gambits/bosses/economy/cards/strategy all exist but need visual polish

### Pending (staggered release)
- [ ] Day 5 (May 16 15:31): Add **Endgame Killer Tips** to homepage Latest Guides
- [ ] Day 7 (May 18 09:17): Add **Rook & Bishop Guide** to homepage Latest Guides

### Future
- [ ] AdSense初审提交（域名购入后）
- [ ] 推广策略制定（Reddit/Steam社区/GameFAQs）
- [ ] Employee A: 重新筛选前5个选题（聚焦独立/中小型游戏）
- [ ] Employee B: 设计通用Wiki目录模板
- [ ] Outworld Station guide: `leolifan007/outworld-station-guide` (Actions deployment pending, domain not yet configured)

---

## 🛠️ Operating SOPs

### Content Rules
1. **All content must be in English** — global audience, no Chinese guide pages
2. **First-person voice** — write from "I tested / I found / In my runs" perspective. NEVER "data compiled from / community reports / sources say / this guide covers"
3. **New pages need clickable entry** — add to homepage Latest Guides, nav, or footer. No orphan pages.
4. **Staggered release** — 1-2 days per article, random non-round times. New pages: wait 12-24h before adding homepage entry.
5. **SEO-safe tone** (post-GSC-audit):
   - ✅ "From my own runs" / "I've tested"
   - ✅ "Here's what works"
   - ❌ "According to community reports" / "Data compiled from" / "Sources: Steam discussions"
   - ❌ "Based on Prima Games review" (citing competitors)

### Design Rules
1. **Responsive**: mobile-first (320px min), key breakpoints at 480/768/1024
2. **Components required**: callout boxes, meta-badge/rating, pro-tip (gold border), phase-tag, synergy-table
3. **Images**: WebP format only, quality 80, max 250KB, loading="lazy" with w/h attributes
4. **Heading font**: "Press Start 2P" (pixel/monospace style), body font: Inter
5. **No Google Translate** — lang-bar and sidebar translator removed
6. **No CTA/buy widget** on sub-pages — only Steam buy button in header

### Deployment Rules
1. `baseURL` must match the live domain — never change to github.io
2. gh-pages deploy: only `git push --force`, never `git push :gh-pages` (delete)
3. After deploy, always verify site is serving 200 OK
4. Version stamping: every page should have version + Last Updated date (current: v1.1.0)

### 404 Recovery (if it happens again)
Root cause: `git push origin :gh-pages` (delete) creates a gap. Fix:
1. Rebuild: `hugo`
2. Create orphan: `git checkout --orphan gh-pages && git rm -rf .`
3. Copy public/*, commit, `git push origin gh-pages --force` (no delete step)
4. Verify CNAME in gh-pages branch exists

---

## 💡 Lessons Learned (hard-won)

1. **gh-pages delete = 404**. Never delete gh-pages branch. Only force-push with replacement.
2. **Hugo CSS cache bug**. Source CSS changes may not trigger public/ regeneration. Delete public/ or re-run hugo.
3. **Templates are at project root**, not inside theme. Theme only provides CSS.
4. **PowerShell encoding**: Avoid `Set-Content` and `>` for Unicode. Use Python for file writes.
5. **Steam community interaction**: `web_fetch` blocked by sandbox. xbrowser works but CDP evaluate is unavailable. Steam cookie persists though.
6. **xbrowser refs**: `@ref` is temporary. DOM changes require new snapshot -i.
7. **Orphan branch management**: deploy-v2 had correct CSS changes but commit wasn't on main branch → lost. Always merge visual changes back to main.

---

## 📋 Git Tips

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

## ⚠️ Critical Notes for New Session
1. **The _fix_all.py and other temp scripts have been cleaned up.** Don't assume they exist.
2. **All GSC red-flag text has been removed** from all 22 content files. Don't re-add phrases like "community reports", "data compiled", "Prima Games", "this guide covers", etc.
3. The public/ directory may contain stale CSS. If CSS changes don't show, delete public/ first.
4. The stale `.html` files mixed in the project root (4x4-fast-farm-guide/index.html etc.) are old artifacts from a pre-Hugo version. They sit alongside the project but are NOT part of the Hugo build.
