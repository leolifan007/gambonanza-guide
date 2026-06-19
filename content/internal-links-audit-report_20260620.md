# 正文内链合规审计报告

**日期**: 2026-06-20
**SOP 规范**: SOP 11 - 正文内链规范（强制）
**受检文章**: 63 篇（排除 contact.md / privacy.md / _index.md）

---

## 一、审计标准

| 等级 | 正文内链数 | 符合 SOP 11？ |
|------|-----------|-------------|
| 合格 | 2-4 个 | 是 |
| 不足 | 0-1 个 | 否（需补充） |
| 超标 | 5+ 个 | 可能需精简 |
| 违规 | 有底部 Related 模块 | 否（需迁移到正文） |
| 违规 | 有 see_also 但未嵌入正文 | 否（需迁移到正文） |

---

## 二、全站审计结果

### 2.1 违规：有 "Related guides" 底部模块（7 篇）

这些文章的底部显式列出了相关推荐模块，违反 SOP 11 "禁止单独列出"规则。

| # | 文件 | 分类 |
|---|------|------|
| 1 | **3-simple-habits-win-rate.md** | Strategy & Guides |
| 2 | **5-emergency-strategies-salvage.md** | Strategy & Guides |
| 3 | **master-the-knight-guide.md** | Pieces & Cards |
| 4 | **pick-right-build-archetype.md** | Strategy & Guides |
| 5 | **sacrifice-postmortem.md** | Strategy & Guides |
| 6 | **stop-making-5-mistakes.md** | Strategy & Guides |
| 7 | **universal-first-3-turns.md** | Strategy & Guides |

**操作**: 将底部 3-4 个相关链接逐个嵌入正文自然段落中，删除 "Related guides:" 标题行。

---

### 2.2 有 see_also 但未嵌入正文（40 篇）

这些文章通过 frontmatter 配置了 `see_also` 链接，但链接渲染在 sidebar（不在正文段落中），违反 SOP 11。

| 文件 | 分类 |
|------|------|
| 4x4-fast-farm-guide.md | Strategy & Guides |
| achievements.md | Strategy & Guides |
| beginner.md | Beginner |
| best-seeds.md | Strategy & Guides |
| blitzking-boss-guide.md | Boss Battles |
| board-clutter-priority.md | Strategy & Guides |
| boss-strategy-guide.md | Boss Battles |
| bosses.md | Boss Battles |
| cards.md | Pieces & Cards |
| combo-chain-guide.md | Strategy & Guides |
| complete-walkthrough.md | Strategy & Guides |
| crumble-mechanic-guide.md | Strategy & Guides |
| dark-tile-gambit-blocks.md | Strategy & Guides |
| decision-framework-guide.md | Strategy & Guides |
| deterministic-gambits-guide.md | Strategy & Guides |
| economy-recovery-guide.md | Economy |
| economy.md | Economy |
| endgame-killer-tips.md | Strategy & Guides |
| faq.md | Strategy & Guides |
| final-boss-hidden-phase.md | Boss Guides |
| gambit-chain-recovery-guide.md | Gambits |
| gambits.md | Gambits |
| gambonanza-tier-list.md | Strategy & Guides |
| how-to-play.md | Strategy & Guides |
| king-difficulty-hidden-changes.md | Difficulty & Progression |
| king-of-spades-guide.md | Boss Guides |
| pawn-promotion-sustainability-guide.md | Pieces & Cards |
| pawn-promotion-troubleshooting.md | Pieces & Cards |
| piece-sacrifice-guide.md | Pieces & Cards |
| post-boss-economy-restart.md | Economy & Shop |
| queen-supremacy-guide.md | Pieces & Cards |
| recommended-seeds.md | Strategy & Guides |
| rook-bishop-guide.md | Pieces & Cards |
| sacrifice-postmortem.md | Strategy & Guides |
| self-destructive-loop-guide.md | Gambits & Combos |
| stage-4-economy-wall.md | Economy & Shop |
| strategy.md | Strategy & Guides |
| tile-control-guide.md | Pieces & Cards |
| tips.md | Strategy & Guides |
| universal-first-3-turns.md | Strategy & Guides |

---

### 2.3 完全无正文内链（重点）

以下文章既无正文内链，也无 see_also / Related，完全孤立：

| 文件 | 分类 |
|------|------|
| 10-common-mistakes.md | Beginner |
| afks-gambit-guide.md | Gambits |
| board-size-strategy.md | Strategy & Guides |
| comeback-zero-stock.md | Economy |
| enigmas-gambit-guide.md | Gambits |
| gambit-synergy-chains.md | Gambits |
| jester-boss-guide.md | Boss Battles |
| knight-rush-opener.md | Pieces & Cards |
| pawn-economy-loop.md | Economy |
| rook-gambit-build-guide.md | Pieces & Cards |

---

## 三、按优先级排序的执行计划

### Phase 1：修复 7 篇违规底部模块（高优先级）

这些违反了 SOP "禁止单独列出"红线。

**操作目标**: 将底部 Related 链接拆入正文，删除底部模块。

示例（3-simple-habits-win-rate.md 修复方案）:

> 原文底部：
> ```
> **Related guides:**
> - [Economy & Stock Guide](/economy/) -- Deep dive on stock management
> - [All Gambits Guide](/gambits/) -- Complete Gambit reference
> - [Gambit Chain Recovery Guide](/gambit-chain-recovery/) -- Fix broken chains
> - [Tips & Tricks](/tips/) -- 25 more pro tips
> ```
>
> 改为在正文 Habit 1 处嵌入：
> "The 50-Stock Rule directly connects to our **[Economy & Stock Guide](/economy/)** where we break down stock growth strategies beyond boss prep."
>
> 在正文 Habit 3 处嵌入：
> "If you want to maximize your held Gambit bursts, our **[All Gambits Guide](/gambits/)** rates every Gambit so you know which ones are worth stacking."

### Phase 2：迁移 see_also 到正文（40 篇，中高优先级）

并非所有 40 篇都要等量处理。按流量优先：

**Tier 1 (高流量文章, 先处理)**:
- beginner.md
- boss-guide.md  
- gambits.md
- economy.md
- complete-walkthrough.md

策略：从 frontmatter 的 see_also 列表选 2-3 个链接，找到正文中最自然的锚点段落插入。

### Phase 3：从零建设孤立文章（10 篇，中优先级）

这些文章完全无内链。需从零设计 "2-4 个" 链接点和 "玩家下一步" 逻辑。

---

## 四、玩家旅程 + 内联映射方案

要让内链符合 "下一步遇到最可能的问题"逻辑，玩法旅程映射如下：

```
新手期 → 基础经济 → Gambit 构建 → Boss 战 → 经济恢复 → 进阶战术 → 高难度
```

**每类文章的"下一步"锚定**:

| 当前文章类型 | 玩家读完后的状态 | "下一步"应链接到 |
|-------------|----------------|----------------|
| Beginner (入门) | 刚知道怎么玩 | economy（经济）, how-to-play（机制）, complete-walkthrough（全局路线） |
| Economy (经济) | 会管经济了 | gambits（怎么花钱）, boss-guide（用钱打boss）, pawn-economy-loop（进阶印钱） |
| Gambits (Gambit列表) | 知道有什么Gambit | combo-chain-guide（怎么连招）, gambit-synergy-chains（协同）, pick-right-build（选Build） |
| Boss (Boss大全) | 知道Boss机制 | boss-strategy-guide（怎么打）, post-boss-economy（战后经济）, endgame-killer-tips（收关） |
| Pieces & Cards (棋子) | 了解棋子用法 | tile-control-guide（控场）, piece-sacrifice（取舍）, board-size-strategy（棋盘策略） |
| Strategy & Guides (策略) | 各种策略 | 根据具体主题交叉链接到 economy / gambits / pieces / bosses |

---

## 五、总工作量估算

| Phase | 篇数 | 预估每篇耗时 | 总时间 |
|-------|------|------------|--------|
| 1 - 修复底部模块 | 7 | 15 min | 1.75 h |
| 2 - Tier 1 see_also 迁移 | 5 | 10 min | 0.8 h |
| 3 - 孤立文章建设 | 10 | 15 min | 2.5 h |
| 4 - 其余 see_also 迁移 | 35 | 5 min | 3.0 h |
| **合计** | **57** | | **约 8 小时** |

**建议**: 先做 Phase 1 + Phase 2 Tier 1（共 12 篇），验证效果后再铺开。
