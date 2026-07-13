---
category: "Gambits"
title: "ADJACENT Keyword Guide - All 11 Gambits Using Gambonanza's New Keyword (v1.2+)"
description: "Gambonanza v1.2.0 introduced the ADJACENT keyword for 11 Gambits. Complete guide to how adjacency works and which Gambits use it. Updated for v1.3.0."
game_version: ">=v1.2.0"
last_reviewed: "2026-07-13"
review_status: "current"
date: "2026-07-13"
---

{{< callout type="verdict" title="What ADJACENT Means" >}}
ADJACENT means a piece is on one of the four orthogonally adjacent tiles: up, down, left, or right. **Diagonals do NOT count.** This keyword was added in v1.2.0 to 11 Gambits that previously had vague or missing range descriptions. Now every ADJACENT Gambit has the same, clear rule.
{{< /callout >}}

{{< diagram src="adjacent-tile-visualization.svg" alt="ADJACENT vs diagonal tile visualization on a chess board" caption="Green X tiles = ADJACENT (triggers the Gambit). Red _ tiles = diagonal (does NOT trigger)." >}}

## The 11 ADJACENT Gambits (Ranked)

| Gambit | How ADJACENT Matters | Tier |
|--------|----------------------|------|
| **Catapult's Gambit** | ROOK: capture an ADJACENT enemy piece to launch it diagonally 2 tiles | S |
| **Princess's Gambit** | BISHOP: bless an ADJACENT friendly piece | A |
| **Excalibur's Gambit** | KNIGHT: ADJACENT pieces get +1 attack | A |
| **Scout's Gambit** | PAWN: ADJACENT pieces reveal hidden tiles | B |
| **Mercenary's Gambit** | ROOK: ADJACENT enemy pieces cost +$1 to summon | B |
| **Firewatch's Gambit** | BISHOP: ADJACENT tiles are immune to Crumble | B |
| **Fleur de Lys' Gambit** | QUEEN: ADJACENT pieces gain PROTECT | B |
| **Squire's Gambit** | KNIGHT: ADJACENT KNIGHTs gain "No Luck" effect | C |
| **Family's Gambit** | PAWN: ADJACENT PAWNs get +1 move range | C |
| **Super Hero Landing's Gambit** | BISHOP: ADJACENT tiles become landing pads | C |
| **Makibishi's Gambit** | Trap on ADJACENT tile after KNIGHT capture | C (was bugged, now fixed) |

### What Changed

Before v1.2.0, several of these Gambits had variations of "nearby" or "neighboring" or nothing at all. This caused confusion about whether diagonals counted. Now ADJACENT is standardized: **only 4 orthogonal directions.**

## How to Play ADJACENT Gambits

### Positioning Basics

ADJACENT Gambits reward **clustering** your pieces. Center placement maximizes ADJACENT coverage -- up to 4 pieces can be adjacent to one central piece at the same time. Edge placement is the worst strategy for ADJACENT Gambits since you lose 1-3 potential trigger directions immediately.

Key positioning rules:
- **Avoid edges** unless your Gambit specifically benefits from edge placement
- **Cluster at least 3 pieces** near your ADJACENT Gambit piece for consistent triggers
- **Sacrifice a low-value piece** to reposition your Gambit piece to the center if needed
- **Stack ADJACENT Gambits** on the same cluster for exponential returns (Catapult + Excalibur on the same center piece)

### Best Builds for ADJACENT Gambits

**Catapult + Scout center build:** Place Catapult ROOK in the center, Scout PAWNs on all 4 adjacent tiles. Catapult fires diagonally, Scouts reveal everything. This is the most reliable ADJACENT build for new players.

**Excalibur cluster:** Create a KNIGHT cluster with Excalibur in the middle. Every ADJACENT KNIGHT gets +1 attack. In a 3x3 grid, you can position 8 KNIGHTs around a single Excalibur piece. Stack with Show Jumping or Whip's Gambit for even more value per turn.

**Family PAWN wall:** Line up PAWNs in a row so every PAWN is adjacent to at least one other. Family's Gambit gives +1 move range to each adjacent PAWN. A 6-PAWN wall means every PAWN gets the buff. Combine with [Pawn Promotion Guide](/pawn-promotion-sustainability-guide/) for full value.

### Anti-Synergies to Avoid

Not every ADJACENT combo works. Watch out for:
- **Spread Gambits** that require distance -- they conflict with ADJACENT clustering
- **Firewatch's Gambit** on a Crumble board -- if all tiles are immune, you lose Crumble-based triggers
- **Super Hero Landing** overlaps with existing tile effects -- check your board before picking

## Community Resources

- [Official v1.2.0 Patch Notes (Steam)](https://store.steampowered.com/news/app/3509230/view/711150909845932295)
- [Gambonanza Keywords Wiki](https://gambonanza.fandom.com/wiki/Keywords)

---

*Guide updated for Gambonanza v1.3.0. ADJACENT keyword introduced in v1.2.0 (June 1, 2026).*

