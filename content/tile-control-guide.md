---category: "Pieces & Cards"

title: "Tile Control Guide"
description: "Gambonanza tile control guide for patch v1.1.0. Tile value map visualization, center vs edge strategy, and a 5-rule checklist to own the board. Updated for patch v1.1.0."
lastUpdated: 'v1.1.0-05-17'
version: 'v1.1.0'
---

## Tile Control  TL;DR Check [Crumble Mechanic Guide](/crumble-mechanic-guide/) for the full breakdown. The [Decision Framework](/decision-framework-guide/) breaks this down in detail.

{{< callout type="verdict" >}}<strong>Center = wins. Edges = Crumble bait.</strong>

Gambonanza is territory control, not chess. Control the center tiles and the game plays itself.{{< /callout >}}

{{< meta-rating grade="A" label="Once you see the board as territory, everything else makes sense." >}}

{{< section-divider >}}

## Tile Value Map (5x5)

<img src="/images/guides/tile-value-5x5.svg" alt="5x5 Tile Value Map: piece-based tier guide" class="schema-diagram" loading="lazy" style="width:100%;max-width:640px;height:auto">

<div class="synergy-table" style="overflow-x:auto">

| Tier | Value | Crumble Safety | Best Piece |
|------|-------|---------------|------------|
| **S** (center) | | Never collapses | Queen / Knight |
| **A** (mid-ring) | | Collapses last | Rook / Bishop |
| **B** (bridge) | | Collapses mid-game | Any |
| **C** (corridor) | | Collapses early | Avoid |
| **D** (edge) | | 1st to collapse | Avoid |

</div>

{{< section-divider >}}

## Gambit Tiles  Quick Reference

<div class="synergy-table" style="overflow-x:auto">

| Tile | Effect | Priority |
|------|--------|----------|
|  Free Gambit | Free Gambit use (3-turn cooldown) | ?(always take) |
|  Stock Boost | +2-5 stock | ?(only if safe) |
|  Heal Square | Restore 1 collapsed adjacent tile | ?(vs Crumble) |
|  Power Square | Next move +1 range | ?(nice to have) |
|  Trap Tile | Damages your piece | ?(avoid) |

</div>

> **Rule:** Free Gambit tiles are the most valuable on the board. Plan routes to revisit them after cooldown.

{{< section-divider >}}

## 2 Strategies  Pick One

###  Center Lock (Recommended)

<img src="/images/guides/center-lock-strategy.svg" alt="Center Lock Strategy: Knight center "?Bishop/Rook reinforce "?Fortress Gambit" style="width:100%;max-width:440px;border-radius:8px;" loading="lazy">

<div class="synergy-table" style="overflow-x:auto">

| Pros | ?Cons |
|---------|----------|
| Safe from Crumble | Vulnerable to early aggression |
| Max mobility | Can be flanked |

</div>

---

###  Edge Gambit (Advanced)

Deploy to edge Gambit tiles "?farm stock "?Earthquake/Board Shrink to collapse center "?sweep in.

<div class="synergy-table" style="overflow-x:auto">

| Pros | ?Cons |
|---------|----------|
| Economy advantage | Very risky |
| Turns Crumble into weapon | Needs specific Gambits |

</div>

> **Best vs Jester:** Jester accelerates Crumble anyway "?Edge Gambit works perfectly.

{{< section-divider >}}

## Tile Control by Piece

<div class="synergy-table" style="overflow-x:auto">

| Piece | Best Tile | Control Style |
|-------|------------|----------------|
| Queen | S (center) | Dominates all 8 directions |
| Rook | A (mid-ring, file) | Locks down entire files |
| Bishop | A (mid-ring, diagonal) | Controls diagonals |
| Knight | S/A (center area) | Forks from center |
| Pawn | C/D (corridor/edge) | Only useful for promotion |

</div>

{{< section-divider >}}

## 5-Rule Checklist (Use Every Turn)

```
Am I moving toward higher-value tiles?  (S > A > B > C > D)
Will this tile still exist in 3 turns?  (check Crumble timeline)
Am I activating a Gambit tile?         (prioritize Free Gambit)
Does this expand or abandon territory?   (never give up S/A tiles)
Can opponent take this tile next turn?    (have a counter ready)
```

{{< section-divider >}}

## Tile x Crumble Timing

<div class="synergy-table" style="overflow-x:auto">

| Turn | 5x5 Safe Zone | 6x6 Safe Zone |
|------|-----------------|-----------------|
| 1-3 | Full board | Full board |
| 4-5 | 3x3 center + corridors | Full (minus corners) |
| 6-7 | 3x3 center | 4x4 center + bridges |
| 8-9 | Center 4 tiles | 4x4 center |
| 10+ | Center 4 (stable) | 3x3 center (stable) |

</div>

> **Rule:** Always stay within or adjacent to the safe zone. Pieces outside = Crumble casualties.

---

*Last updated: May 17, v1.1.0 | Version: v1.1.0*


