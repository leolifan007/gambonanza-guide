---
categories: ["Boss Battles"]
tags:
  - "Bosses"
  - "Tiles"
  - "Bug Fixes"
title: "Cursed Tiles Now Show When They Expire: Reading Tal the Cursed's Board After 1.5.4b"
description: "Patch 1.5.4b fixed Tile Expiration not visually updating cursed tiles, and 1.5.6 fixed an error when a cursed tile's piece vanishes before the curse triggers. Here is how to read a cursed board now."
date: "2026-11-08T13:45:00+08:00"
lastmod: "2026-11-08T13:51:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

A curse that looks permanent gets played around forever. That was the actual problem behind two 1.5.x fixes, and it changed boss decisions without changing a single boss rule.

{{< game-icon name="warning" >}}**1.5.4b: Tile Expiration did not visually update cursed tiles when they expired.** 1.5.6 added a second fix: no error when a cursed tile's piece disappears before the curse triggers.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

The countdown was real, the display was not keeping up. After 1.5.4b an expired cursed square clears visually, so you can plan around when it ends instead of treating the whole board as permanently cursed. Watch one expiry in your own run before trusting an old guide that says curses never lift.{{< /callout >}}

{{< diagram src="cursed-tile-expiration-154b.svg" alt="Cursed tile expiration read before and after patch 1.5.4b" caption="Two fixes, one outcome: what you see on the board now matches what the rules are doing." >}}

The [full boss roster](/bosses/) lists all 8 modifiers; this page is about the board read during a curse fight, not a boss-by-boss walkthrough.

## What the Two Fixes Actually Say

The 1.5.4b post: fixed an issue where Tile Expiration didn't visually update cursed tiles when they expired. The 1.5.6 post: no error when a cursed tile's piece disappears before the curse triggers. Neither line changes what a cursed tile does. Both change whether the board tells you the truth about it.

{{< game-icon name="grid" >}}**In the shipped game, Tal the Cursed places five cursed squares and stepping on one demotes the piece to a pawn.** That is the rule. The bug was that an expired curse kept looking like a live one, so players routed around a threat that was no longer there.

Boss order is not fixed and there are five boss checkpoints across a run, which is why the [boss preview guide](/reading-boss-preview-shop/) matters here: the shop tells you which modifier is coming before you spend. A correct read of the cursed board is only useful if you prepared for it.

- **Curse expires**: Square still looked cursed / Square clears visually
- **Piece disappears before trigger**: Could throw an error / No error
- **Planning a route**: Avoid the square indefinitely / Time your move after expiry
- **Boss rule itself**: Unchanged / Unchanged

{{< section-divider >}}

## The Route Decision, Not the Boss Page

This is a decision page rather than a boss page for a reason. Single-boss guides for this game are already well covered by community wikis, and repeating a boss biography here adds nothing. What a player actually needs at the board is a sequence: read the squares, identify which are live, and move when the safe route opens.

- **Read all five.** Tal the Cursed places five cursed squares, not one. A route that avoids one and crosses another is not a route.
- **Watch one expiry.** Once you have seen a curse clear on your own client, you know the display is keeping up and you can plan around the timing.
- **Do not spend a tile token on an expired square.** A [tile token](/which-token-piece-gambit-tile/) lets you choose the square, so spend it where the board is still a problem.
- **Remember the demotion.** A cursed square turns the piece into a pawn. The [promotion notes](/pawn-promotion-sustainability-guide/) cover what it costs to climb back.

{{< callout type="danger" >}}<strong>A stale visual is not a secret mechanic</strong>

If an older guide insists cursed squares never lift, it was written while the display bug was live. Do not build a strategy around a UI defect the developer already fixed.{{< /callout >}}

For the general boss prep checklist, the [boss strategy guide](/boss-strategy-guide/) covers what to carry into the five checkpoints, and the [crumble mechanic guide](/crumble-mechanic-guide/) is the other board-state read that punishes a rushed route.

{{< diagram src="cursed-tile-expiration-154b-detail.svg" alt="Two route options around a cursed square" caption="Time the safe route; do not spend a tile on an expired curse." >}}

## Where the Other 1.5.6 Board Fixes Fit

1.5.6 also made enemies clear their old tile reliably. Put next to the cursed tile fixes, the theme is the same: what is on the board should match what the rules say is on the board. If a fight in October felt like it had leftover hazards, that was likely a stale tile rather than a hidden mechanic.

{{< game-icon name="check" >}}**Version order matters.** 1.5.4b (30 September) fixed the expiry visual. 1.5.6 (30 October) fixed the vanishing-piece error and enemy tile clearing. 1.5.7 (2 November) touched two Gambit triggers. The 1.5.4b checklist is the quick way to confirm which batch your client has.

{{< pro-tip >}}<strong>Before every boss game</strong><br>Read the preview, name the resource being attacked, then read the actual squares. Two seconds of looking beats any amount of memorised boss trivia.{{< /pro-tip >}}

If you are still building a mental model of tiles, the tile control guide is the reference for what each square does.

## Community Verification & Resources

The cursed tile expiry fix is from the official 1.5.4b post and the vanishing-piece and enemy tile fixes are from 1.5.6. The five cursed squares and demotion rule are shipped game facts; no single-boss walkthrough is duplicated here.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.4b, 30 Sep 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [Official Gambonanza Steam News (1.5.6, 30 Oct 2026)](https://steamdb.info/patchnotes/26319297/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
