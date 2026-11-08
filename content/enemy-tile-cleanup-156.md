---
categories: ["Boss Battles"]
tags:
  - "Bosses"
  - "Tiles"
  - "Patch Updates"
title: "Enemies Clear Their Old Tiles Reliably in 1.5.6: What No Longer Lingers Between Fights"
description: "One line in the 1.5.6 post says enemies clear their old tile reliably. A practical read on why stale tile visuals changed fight decisions, plus the other three fixes in the same patch."
date: "2026-11-08T13:47:00+08:00"
lastmod: "2026-11-08T13:53:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

A leftover tile you cannot interact with is worse than no tile at all, because you plan around it. The 1.5.6 post spends four words on this: enemies clear their old tile reliably.

{{< game-icon name="shield" >}}**It is a cleanup fix.** The rule did not change, the visual did. Old enemy tiles now clear when they should, so the board in front of you is the board you are actually playing on.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

If an enemy tile looked like it survived into the next exchange, stop routing around it. On 1.5.6 or later, check the square at the start of the fight and trust what you see. The rest of the patch is two crash fixes and a Strain pool change.{{< /callout >}}

{{< diagram src="enemy-tile-cleanup-156.svg" alt="The four fixes in Gambonanza patch 1.5.6 grouped by what they affect" caption="Two board-state fixes, one menu crash fix, one Strain pool change. No rule rewrites." >}}

The [tile control guide](/tile-control-guide/) is the reference for what each square does; this page is only the 1.5.6 cleanup and how it changes a fight read.

## Why a Stale Square Costs a Turn

Tiles in this game are not decoration. A Trap Tile stops an enemy that steps on it from moving next turn, a Protective Tile protects a piece for the turn it moves in, a Blessed Tile returns a captured piece to Stock, and a Gold Tile gives a piece a money value. When a tile you think is there has actually been cleared, every one of those reads flips.

{{< game-icon name="grid" >}}**The 1.5.6 fix makes the clearing reliable.** That means the board at the start of an exchange reflects the current state, and the decisions you make from it are based on something real. This is the same class of fix as the [cursed tile expiry visual](/cursed-tile-expiration-154b/) from 1.5.4b.

Enemy powers are a separate system. Patch 1.5.0 added clearer feedback before an enemy power triggers, and the [enemy power warning guide](/enemy-powers-warning-guide/) covers how to react to it. Tile cleanup is quieter: there is no warning, just a square that should no longer be there.

{{< callout type="info" >}}<strong>Quick reference, no table needed</strong>

On An old enemy tile still drawn: Check the square, it should be clear. 
On A tile looks absent: Trust the board. 
On A boss modifier changes the board: Re-read once per exchange. 
On Cursed square piece disappears: Fixed in the same patch. 
{{< /callout >}}

{{< section-divider >}}

## The Other Three Lines in 1.5.6

- **Magic Tiles Strain** now adds phantom tiles to the pool of tiles available at start. That is a run-creation change, covered in the [Strain pool page](/magic-tiles-strain-phantom/).
- **No breakage when spamming Esc after Pause > Main Menu.** A menu stability fix reported on Discord, with no effect on board rules.
- **No error when a cursed tile's piece disappears before the curse triggers.** A boss-board edge case, covered in the [cursed tile read](/cursed-tile-expiration-154b/).
- **No new content.** The post adds no Gambit, no boss and no difficulty tier. 1.5.x has been a consistency pass since 1.5.4b.

{{< callout type="tip" >}}<strong>One patch, one habit</strong>

When a patch says something is cleared reliably, the useful response is not a new strategy. It is to look at the board once at the start of each exchange instead of carrying the previous exchange's picture in your head.{{< /callout >}}

Boss order is random and only five boss checkpoints appear in a run, so the [boss preview guide](/reading-boss-preview-shop/) and the [full roster](/bosses/) remain the right preparation tools. Tile cleanup changes the read mid-fight, not the preparation before it.

{{< diagram src="enemy-tile-cleanup-156-detail.svg" alt="A stale square before the fix versus a cleared board after" caption="Once the old tile clears, the board read is honest again." >}}

## A Short Verification Pass

You can confirm all four lines without a full run. Use Quick Restart from Pause to Main Menu several times and confirm nothing breaks, start a run with Magic Tiles and inspect the opening squares, then watch a boss exchange where an enemy leaves a tile.

{{< game-icon name="check" >}}**If a stale square still appears**, check your client first. 1.5.6 is dated 30 October 2026 and 1.5.7 followed on 2 November; a client on 1.5.5 will not have either board fix.

{{< pro-tip >}}<strong>Do not over-correct</strong><br>A cleanup fix means old advice about routing around leftover hazards is obsolete. It does not mean tiles are weaker now. The crumble mechanic guide is a better place to think about squares disappearing for real.{{< /pro-tip >}}

For general patch questions and version checks, the FAQ and the 1.5.4b fix checklist cover the surrounding release sequence.

## Community Verification & Resources

All four 1.5.6 lines are quoted from the official post. Tile behaviours, the 1.5.0 enemy power feedback and boss checkpoint structure are shipped game facts; the verification steps are derived from the listed fixes.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.6, 30 Oct 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.6 patch notes](https://steamdb.info/patchnotes/26319297/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
