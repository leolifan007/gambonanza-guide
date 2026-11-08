---
categories: ["Economy"]
tags:
  - "Patch Updates"
  - "Economy"
  - "Probability"
title: "Golden Idol's Proc Rate Went From 1/3 to 1/2 in 1.5.7: What That Does to Your Build Math"
description: "Patch 1.5.7 changed Golden Idol's Gambit proc chance from 1/3 to 1/2. A plain-English expected value table, what the change does not mean, and how to confirm your client is actually on 1.5.7."
date: "2026-11-08T13:33:00+08:00"
lastmod: "2026-11-08T13:39:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

One number changed on 2 November 2026: Golden Idol's Gambit now procs on 1/2 instead of 1/3. That is the whole patch line, and it is also the kind of line players consistently over-read into a damage buff.

{{< game-icon name="bolt" >}}**It is a 1.5x increase in trigger frequency, not a 1.5x increase in anything else.** Over six chances, the old rate expected 2 procs and the new rate expects 3. Nothing in the note changes what a proc does.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

If a build leans on Golden Idol's Gambit firing, it now fires half again as often. If the build only carries it as a filler, nothing about your decisions changed. Re-check any plan that assumed the old 1/3 rate, then leave the rest of your build alone.{{< /callout >}}

{{< diagram src="v157-proc-odds-change.svg" alt="Expected proc counts at 1/3 versus 1/2 across six to thirty chances" caption="Same trigger, new rate: the gap is one extra proc per six chances, and it compounds with volume." >}}

For the wider money picture behind a probability change like this, the [economy guide](/economy/) is the baseline; this page stays on the single number in the 1.5.7 note.

## The Arithmetic, Without Any Invented Run Data

The official 1.5.7 post says: change Golden Idol's Gambit proc chance from 1/3 to 1/2. That gives us a rate and nothing else, so the honest analysis is arithmetic on the rate. Multiply the number of chances by the rate and you get the expected count. There is no hidden variance number, no sim and no 25-run sample behind the table below.

- **6**: 2 / 3 / +1
- **12**: 4 / 6 / +2
- **18**: 6 / 9 / +3
- **30**: 10 / 15 / +5

{{< game-icon name="grid" >}}**The gap scales with volume.** A build that creates few chances barely notices the change. A build that creates many chances gets the full benefit, which is why this patch is really a buff to builds that already feed the trigger, not to the Gambit in isolation.

That distinction matters if you are choosing between a probabilistic Gambit and one that fires on a fixed condition. The [deterministic Gambits guide](/deterministic-gambits-guide/) covers the other side of that trade, and the [Gambits overview](/gambits/) lists the slot limit you are working within.

{{< section-divider >}}

## Three Over-Reads That Will Cost You a Run

- **'It procs 50% more, so I can drop a supporting Gambit.'** The rate changed, the trigger condition did not. If your board was not producing chances before, it still is not.
- **'The effect got stronger.'** The note changes a proc chance. It says nothing about the effect resolving differently, so do not rewrite a [tier list](/gambonanza-tier-list/) on that assumption.
- **'This applies to my old notes.'** Any plan written against 1/3 understates how often the effect now fires. Re-read the plan, not the whole game.

{{< callout type="danger" >}}<strong>Expected value is not a promise</strong>

Three expected procs in six chances does not mean three procs will happen in your next six chances. It means that over many chances, the average moves from a third to a half. Short runs will still be streaky, and a build that collapses when the proc misses is still fragile at 1/2.{{< /callout >}}

This is also why the change belongs in an economy conversation rather than a pure power ranking. You are spending money and one of five Gambit slots on a chance. The [token decision guide](/which-token-piece-gambit-tile/) gives the run-state test for whether that slot should go to a Gambit at all, and the [shop economy page](/economy/) covers what the same money buys elsewhere.

{{< diagram src="v157-proc-odds-change-detail.svg" alt="Expected procs over six chances at 1/3 versus 1/2" caption="Over the same six chances, the new rate expects one extra proc." >}}

## Confirm You Are Actually on 1.5.7

The patch is small and easy to miss. The 1.5.7 post contains exactly two lines: the Dainsleif's Gambit trigger fix and this proc chance change. If your client is still on 1.5.6, you are still playing at 1/3 and every conclusion above is wrong for you.

{{< game-icon name="check" >}}**Use the shop, not the launcher.** If Valhalla's Gambit shows $8, you are at least on 1.5.4b. To separate 1.5.6 from 1.5.7, check the news panel in the client for the 2 November entry, or compare against the [1.5.0 to 1.5.3 notes](/v151-153-hotfix-breakdown/) to see how the developer labels these small posts.

{{< pro-tip >}}<strong>One habit that survives every rate change</strong><br>Write down why you bought a Gambit, not just that you bought it. When a proc rate moves, you can tell in seconds whether the reason still holds instead of rebuilding from scratch.{{< /pro-tip >}}

If you are new to the game and the terminology here is dense, the how to play page defines the pieces, Gambits and shop loop before you start doing build math.

## Community Verification & Resources

The 1/3 to 1/2 rate is quoted from the official 1.5.7 post. All counts in the table are direct arithmetic on those two rates; no run measurements are claimed.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.7, 2 Nov 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.7 patch notes](https://steamdb.info/patchnotes/26379999/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
