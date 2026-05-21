---
title: "Tile Control Guide"
description: "Gambonanza tile control guide for patch v1.1.0. Tile value map visualization, center vs edge strategy, and a 5-rule checklist to own the board. Updated for patch v1.1.0."
see_also:
  - title: 'Crumble Mechanic Guide'
    url: '/crumble-mechanic-guide/'
  - title: 'Decision Framework'
    url: '/decision-framework-guide/'
  - title: 'Queen Supremacy Guide'
    url: '/queen-supremacy-guide/'
lastUpdated: 'v1.1.0-05-17'
version: 'v1.1.0'
---

## Tile Control ï¿?TL;DR

<div class="callout callout-verdict">
<strong>Center = wins. Edges = Crumble bait.</strong><br>
Gambonanza is territory control, not chess. Control the center tiles and the game plays itself.
</div>

<div class="meta-rating">
  <span class="meta-badge meta-a">A</span>
  <span class="meta-label">Once you see the board as territory, everything else makes sense.</span>
</div>

<hr class="section-divider">

## Tile Value Map (5Ã—5)

<img src="/images/guides/tile-value-5x5.svg" alt="5Ã—5 Tile Value Map: piece-based tier guide" class="schema-diagram" loading="lazy" style="width:100%;max-width:640px;height:auto">

| Tier | Value | Crumble Safety | Best Piece |
|------|-------|---------------|------------|
| **S** (center) | â˜…â˜…ï¿?| Never collapses | Queen / Knight |
| **A** (mid-ring) | â˜…â˜…ï¿?| Collapses last | Rook / Bishop |
| **B** (bridge) | â˜…â˜†ï¿?| Collapses mid-game | Any |
| **C** (corridor) | â˜†â˜†ï¿?| Collapses early | Avoid |
| **D** (edge) | â˜†â˜†ï¿?| 1st to collapse | Avoid |

<hr class="section-divider">

## Gambit Tiles ï¿?Quick Reference

| Tile | Effect | Priority |
|------|--------|----------|
| ï¿?Free Gambit | Free Gambit use (3-turn cooldown) | â˜…â˜…ï¿?(always take) |
| ï¿?Stock Boost | +2-5 stock | â˜…â˜…ï¿?(only if safe) |
| ï¿?Heal Square | Restore 1 collapsed adjacent tile | â˜…â˜…ï¿?(vs Crumble) |
| ï¿?Power Square | Next move +1 range | â˜…â˜†ï¿?(nice to have) |
| ï¿?Trap Tile | Damages your piece | â˜†â˜†ï¿?(avoid) |

> **Rule:** Free Gambit tiles are the most valuable on the board. Plan routes to revisit them after cooldown.

<hr class="section-divider">

## 2 Strategies ï¿?Pick One

### ï¿?Center Lock (Recommended)

<img src="/images/guides/center-lock-strategy.svg" alt="Center Lock Strategy: Knight center ï¿?Bishop/Rook reinforce ï¿?Fortress Gambit" style="width:100%;max-width:440px;border-radius:8px;" loading="lazy">

| ï¿?Pros | ï¿?Cons |
|---------|----------|
| Safe from Crumble | Vulnerable to early aggression |
| Max mobility | Can be flanked |

---

### ï¿?Edge Gambit (Advanced)

Deploy to edge Gambit tiles ï¿?farm stock ï¿?Earthquake/Board Shrink to collapse center ï¿?sweep in.

| ï¿?Pros | ï¿?Cons |
|---------|----------|
| Economy advantage | Very risky |
| Turns Crumble into weapon | Needs specific Gambits |

> **Best vs Jester:** Jester accelerates Crumble anyway ï¿?Edge Gambit works perfectly.

<hr class="section-divider">

## Tile Control by Piece

| Piece | Best Tile | Control Style |
|-------|------------|----------------|
| ï¿?Queen | S (center) | Dominates all 8 directions |
| ï¿?Rook | A (mid-ring, file) | Locks down entire files |
| ï¿?Bishop | A (mid-ring, diagonal) | Controls diagonals |
| ï¿?Knight | S/A (center area) | Forks from center |
| ï¿?Pawn | C/D (corridor/edge) | Only useful for promotion |

<hr class="section-divider">

## 5-Rule Checklist (Use Every Turn)

```
ï¿?Am I moving toward higher-value tiles?  (S > A > B > C > D)
ï¿?Will this tile still exist in 3 turns?  (check Crumble timeline)
ï¿?Am I activating a Gambit tile?         (prioritize Free Gambit)
ï¿?Does this expand or abandon territory?   (never give up S/A tiles)
ï¿?Can opponent take this tile next turn?    (have a counter ready)
```

<hr class="section-divider">

## Tile Ã— Crumble Timing

| Turn | 5Ã—5 Safe Zone | 6Ã—6 Safe Zone |
|------|-----------------|-----------------|
| 1-3 | Full board | Full board |
| 4-5 | 3Ã—3 center + corridors | Full (minus corners) |
| 6-7 | 3Ã—3 center | 4Ã—4 center + bridges |
| 8-9 | Center 4 tiles | 4Ã—4 center |
| 10+ | Center 4 (stable) | 3Ã—3 center (stable) |

> **Rule:** Always stay within or adjacent to the safe zone. Pieces outside = Crumble casualties.

---

*Last updated: May 17, v1.1.0 | Version: v1.1.0*
