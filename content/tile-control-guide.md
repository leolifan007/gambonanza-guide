---
title: "Tile Control Guide"
description: "Which tiles matter, center vs edge, Gambit tile map, and a 5-rule checklist. Own the board, win the game."
see_also:
  - title: 'Crumble Mechanic Guide'
    url: '/crumble-mechanic-guide/'
  - title: 'Decision Framework'
    url: '/decision-framework-guide/'
  - title: 'Queen Supremacy Guide'
    url: '/queen-supremacy-guide/'
lastUpdated: '2026-05-17'
version: 'v1.1.0'
---

## Tile Control — TL;DR

<div class="callout callout-verdict">
<strong>Center = wins. Edges = Crumble bait.</strong><br>
Gambonanza is territory control, not chess. Control the center tiles and the game plays itself.
</div>

<div class="meta-rating">
  <span class="meta-badge meta-a">A</span>
  <span class="meta-label">Once you see the board as territory, everything else makes sense.</span>
</div>

<hr class="section-divider">

## Tile Value Maps

### 5×5 Board

```
D  C  B  C  D        D = Danger (collapses 1st)
C  A  A  A  C        C = Corridor (connects to center)
B  A  S  A  B        A = Anchor (stable, mid-ring)
C  A  A  A  C        S = Supreme (center, never collapses)
D  C  B  C  D
```

### 6×6 Board

```
D  C  C  C  C  D
C  B  B  B  B  C
C  B  A  A  B  C
C  B  A  A  B  C
C  B  B  B  B  C
D  C  C  C  C  D
```

| Tier | Value | Crumble Safety | Best Piece |
|------|-------|---------------|------------|
| S (center) | ★★★ | Never | Queen / Knight |
| A (mid-ring) | ★★☆ | Last | Rook / Bishop |
| B (bridge) | ★☆☆ | Mid | Any |
| C (corridor) | ☆☆☆ | Early | Avoid |
| D (edge) | ☆☆☆ | 1st to collapse | Avoid |

<hr class="section-divider">

## Gambit Tiles — Quick Reference

| Tile | Effect | Priority |
|------|--------|----------|
| ♛ Free Gambit | Free Gambit use (3-turn cooldown) | ★★★ (always take) |
| ★ Stock Boost | +2-5 stock | ★★☆ (only if safe) |
| ♝ Heal Square | Restore 1 collapsed adjacent tile | ★★☆ (vs Crumble) |
| ⚡ Power Square | Next move +1 range | ★☆☆ (nice to have) |
| ⚠ Trap Tile | Damages your piece | ☆☆☆ (avoid) |

> **Rule:** Free Gambit tiles are the most valuable on the board. Plan routes to revisit them after cooldown.

<hr class="section-divider">

## 2 Strategies — Pick One

### ⚔ Center Lock (Recommended)

```
Turn 1: Knight → center
Turn 2: Bishop/Rook → reinforce center
Turn 3: Fortress Gambit on center piece
→ Hold center, win from there
```

| ✅ Pros | ❌ Cons |
|---------|----------|
| Safe from Crumble | Vulnerable to early aggression |
| Max mobility | Can be flanked |

---

### ⚡ Edge Gambit (Advanced)

```
Deploy to edge Gambit tiles → farm stock
→ Earthquake/Board Shrink to collapse center
→ Sweep in when board shrinks
```

| ✅ Pros | ❌ Cons |
|---------|----------|
| Economy advantage | Very risky |
| Turns Crumble into weapon | Needs specific Gambits |

> **Best vs Jester:** Jester accelerates Crumble anyway — Edge Gambit works perfectly.

<hr class="section-divider">

## Tile Control by Piece

| Piece | Best Tile | Control Style |
|-------|------------|----------------|
| ♕ Queen | S (center) | Dominates all 8 directions |
| ♖ Rook | A (mid-ring, file) | Locks down entire files |
| ♗ Bishop | A (mid-ring, diagonal) | Controls diagonals |
| ♘ Knight | S/A (center area) | Forks from center |
| ♙ Pawn | C/D (corridor/edge) | Only useful for promotion |

<hr class="section-divider">

## 5-Rule Checklist (Use Every Turn)

```
□ Am I moving toward higher-value tiles?  (S > A > B > C > D)
□ Will this tile still exist in 3 turns?  (check Crumble timeline)
□ Am I activating a Gambit tile?         (prioritize Free Gambit)
□ Does this expand or abandon territory?   (never give up S/A tiles)
□ Can opponent take this tile next turn?    (have a counter ready)
```

<hr class="section-divider">

## Tile × Crumble Timing

| Turn | 5×5 Safe Zone | 6×6 Safe Zone |
|------|-----------------|-----------------|
| 1-3 | Full board | Full board |
| 4-5 | 3×3 center + corridors | Full (minus corners) |
| 6-7 | 3×3 center | 4×4 center + bridges |
| 8-9 | Center 4 tiles | 4×4 center |
| 10+ | Center 4 (stable) | 3×3 center (stable) |

> **Rule:** Always stay within or adjacent to the safe zone. Pieces outside = Crumble casualties.

---

*Last updated: May 17, 2026 | Version: v1.1.0*
