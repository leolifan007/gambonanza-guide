---
categories: ["Difficulty & Progression"]
tags:
  - "Strains"
  - "Patch Updates"
  - "Tiles"
title: "Magic Tiles Strain Now Puts Phantom Tiles in the Starting Pool (1.5.6)"
description: "Patch 1.5.6 changed the Magic Tiles Strain so phantom tiles are in the pool of tiles available at the start of a run. A version-change read on what that means for staging, without inventing pool rates."
date: "2026-11-08T13:43:00+08:00"
lastmod: "2026-11-08T13:49:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

The entire 1.5.6 line about Magic Tiles is one sentence: phantom tiles are now in the pool of tiles available at the start. If you were treating your opening board as a fixed set of possibilities, that sentence changes what you check in staging.

{{< game-icon name="grid" >}}**It is a pool change, not a new tile.** The tile and its behaviour already existed. What 1.5.6 changed is that the Strain can now offer it among the tiles available when a run begins.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

With Magic Tiles active, your starting board can include phantom tiles. Read the board in staging instead of assuming the old pool, and do not spend a tile token on a square you already have a phantom answer for. No drop rates or pool sizes were published, so none are claimed here.{{< /callout >}}

{{< diagram src="magic-tiles-strain-phantom.svg" alt="How the 1.5.6 Magic Tiles Strain change affects the starting tile pool" caption="Same Strain, wider starting pool: the change is at run creation, not in the tile rules." >}}

The [tile control guide](/tile-control-guide/) covers tile interactions across a run; this page stays on the one 1.5.6 pool change and the opening decisions it affects.

## Read the Note Literally

The 1.5.6 post says: Magic TIles Strain add phantom tiles in the pool of tiles available at start, credited to a Discord report. That is a bug-fix-shaped sentence about a pool that was missing an entry. It is not a balance change to the tile, and the developer gives no weighting, no count and no probability.

{{< game-icon name="warning" >}}**So the honest conclusion is narrow.** If you play with Magic Tiles, the set of tiles that can appear on your opening board is now one entry wider. Everything downstream of that is a decision you make in staging, not a number anyone has published.

The [difficulty and progression guide](/difficulty-guide/) explains where Strains sit relative to the six difficulty tiers. Strains and difficulty both add modifiers to a run, but a pool change like this one acts at run creation while difficulty tiers act on the rules of the whole run.

- **A pool is not a guarantee.** A tile being in the pool does not mean it appears in your opening. Do not build a plan that requires it.
- **Staging is where it matters.** You can see the enemy formation and adjust your own positions before the game starts; that is the moment to read which tiles are actually present.
- **The [custom boards reference](/custom-boards-guide/) and the [how to play page](/how-to-play/) are the right background** if the opening board setup is still unfamiliar.

{{< section-divider >}}

## The Decision It Actually Changes

Every shop offers three random tokens, and a tile token gives you a random tile modifier on a square you choose. The interesting part is that the modifier is random but the placement is not. If phantom tiles can already be on the board at run start, your first tile token decision has one more board state to account for.

{{< callout type="info" >}}<strong>Quick reference, no table needed</strong>

On Phantom tile already present in a useful square: You already have that answer. 
On Phantom tile present in a bad square: Placement is the part you control. 
On No phantom tile present: A wider pool is not a guarantee. 
On Boss preview names a board problem: The [preview](/reading-boss-preview-shop/) outranks a tile gamble. 
{{< /callout >}}

{{< callout type="danger" >}}<strong>Do not turn a pool fix into a strategy</strong>

There is no published rate for how often phantom tiles appear at start, and no claim here that they are good or bad in the opening. The [token decision guide](/which-token-piece-gambit-tile/) gives the run-state test; the pool change only adds one more thing to look at before you apply it.{{< /callout >}}

That restraint is deliberate. This site has a standing rule against inventing run data, and a one-line pool fix is exactly the kind of note that attracts confident-sounding percentages with nothing behind them.

{{< diagram src="magic-tiles-strain-phantom-detail.svg" alt="Schematic opening board showing where phantom tiles can appear" caption="Phantom tiles can sit in the start pool, so read every square." >}}

## The Rest of 1.5.6, For Context

The same post fixed three other things: no breakage when spamming Esc after Pause to Main Menu, enemies clearing their old tile reliably, and no error when a cursed tile's piece disappears before the curse triggers. Two of those are board-state fixes. If your read of a fight felt off in October, a leftover visual or a stale tile may have been why.

{{< game-icon name="check" >}}**Version check:** 1.5.6 is dated 30 October 2026. The 1.5.4b fix checklist covers the previous batch, and 1.5.7 followed on 2 November with two Gambit trigger changes. None of these posts change the five-Gambit cap or the run structure.

{{< pro-tip >}}<strong>One habit for every pool change</strong><br>Spend two seconds reading every square in staging before you spend anything in the shop. A wider pool only rewards players who actually look at what they got.{{< /pro-tip >}}

For the full tile vocabulary, the [tile control guide](/tile-control-guide/) remains the reference; this page is only the delta that 1.5.6 introduced.

## Community Verification & Resources

The Magic Tiles Strain pool change and the other three 1.5.6 lines are quoted from the official post. Run structure, staging, tokens and the boss preview are from the shipped game facts. No pool rates are claimed because none were published.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.6, 30 Oct 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.6 patch notes](https://steamdb.info/patchnotes/26319297/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
