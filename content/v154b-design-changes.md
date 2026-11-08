---
categories: ["Gambits & Combos"]
tags:
  - "Patch Updates"
  - "Gambits"
  - "Balance Changes"
title: "1.5.4b Changed Two Rules, Not Twenty: The Rook-King Protection and the $2 Valhalla Cut"
description: "Patch 1.5.4b shipped six bug fixes but only two design changes: Mercenary's Gambit now protects both the ROOK and the KING, and Valhalla's Gambit dropped from $10 to $8. Here is what actually changed and what it does to your build."
date: "2026-11-08T13:31:00+08:00"
lastmod: "2026-11-08T13:37:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

If you skimmed the 1.5.4b notes and assumed the whole meta moved, it did not. Six lines in that post are bug fixes, two lines are design changes, and one is an art pass. Only two rules in the game actually behave differently today.

{{< game-icon name="warning" >}}**Mercenary's Gambit now protects both pieces.** The developer's before-and-after line is exact: before, moving a ROOK ADJACENT to a KING protected it; after, moving a ROOK ADJACENT to a KING protects them both.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

Two changes, two consequences. Mercenary's Gambit went from a one-piece shield to a two-piece shield, so an ADJACENT setup now pays off twice. Valhalla's Gambit costs $8 instead of $10, so it competes with a reroll instead of competing with a slot. Everything else in 1.5.4b is a fix, not a rebalance.{{< /callout >}}

{{< diagram src="v154b-design-changes.svg" alt="The two design changes in Gambonanza patch 1.5.4b" caption="1.5.4b in two rules: a protection Gambit now shields two pieces, and a $10 Gambit now costs $8." >}}

The [1.5.0 to 1.5.3 hotfix breakdown](/v151-153-hotfix-breakdown/) covers the earlier reset rules; this page is only about the two design lines in the 30 September 2026 post.

## The Rook-King Line, Read Literally

The patch note quotes the old wording and the new wording side by side. Before: moving a ROOK ADJACENT to a KING PROTECTS it. After: moving a ROOK ADJACENT to a KING PROTECTS them both. That is the entire mechanical change, and it is worth reading slowly because the rest of the paragraph is the developer explaining why.

{{< game-icon name="shield" >}}**The stated reason is that the Gambit was too situational.** You needed three things to line up at once: a ROOK, an ADJACENT position, and a KING. Even with Anarchist's Gambit in the mix, protecting a single piece was hard to make work. The fix keeps the identity and doubles the payoff.

If you already run ADJACENT effects, the [ADJACENT keyword guide](/adjacent-keyword-gambits-guide/) explains the positioning rule this Gambit depends on. The difference now is that a successful setup protects the piece doing the moving as well as the piece being protected, which changes the risk of committing a ROOK into a crowded board.

{{< callout type="danger" >}}<strong>Do not read this as a new trigger</strong>

The trigger is unchanged. If your ROOK is not ADJACENT to a KING, nothing happens, exactly as before. Players who misread the note as 'Mercenary's Gambit now always protects two pieces' will waste a [Gambit slot](/gambits/) waiting for an effect that never fires.{{< /callout >}}

{{< section-divider >}}

## Why a $2 Price Cut Is a Real Decision Change

Valhalla's Gambit dropped from $10 to $8. Two dollars sounds cosmetic until you put it next to the shop: there is a $2 reroll, one random piece, three random Gambits and three random tokens between games. Two dollars is exactly one reroll, so the patch moved this Gambit from 'a full commitment' to 'a buy plus another look'.

| Budget state | Before 1.5.4b ($10) | After 1.5.4b ($8) |
|---|---|---|
| You have $8 - $9 | Could not buy it at all | Buyable without selling |
| You have $10 - $11 | Buy, then no reroll | Buy, then one $2 reroll left |
| You are saving for the board upgrade | Usually skipped | Still a real trade-off |
| The boss preview demands a counter | Too expensive to improvise | Cheap enough to answer the preview |

The [shop and economy guide](/economy/) covers how much you should be carrying into a boss game; the [upgrade cost breakdown](/max-piece-on-board-upgrade/) is the other side of the same budget. A $2 discount does not make Valhalla's Gambit correct in every run, it just stops price from being the only reason you skip it.

- **Buy it** when you already have the ROOK or KING density to make the protection chain pay, because $8 leaves room for a reroll.
- **Skip it** when your five Gambit slots are the bottleneck, not your money. A cheaper Gambit still occupies a slot.
- **Wait** when the [boss preview](/reading-boss-preview-shop/) shows a modifier that attacks a different resource. Spend on the answer, not on the discount.

{{< diagram src="v154b-design-changes-detail.svg" alt="Which of the nine 1.5.4b lines are design changes versus fixes and art" caption="Only two of nine lines change a rule; the other seven are fixes or VFX." >}}

## What Players Keep Getting Wrong About This Patch

{{< game-icon name="help" >}}**The art pass is not a balance pass.** Eight Gambits got missing visual effects in 1.5.4b: Dainsleif's, King XI's, Resurrection Stone's, Anna's Family's, Zen's, Jockey's, Princess's and Warlock's. Seeing an effect now does not mean the Gambit was buffed.

The same confusion hits the fix list. Barter's Gambit showing a counter of 0 was a bug, not a nerf. Tooth's Gambit not paying out on a sale was a bug, not a rules change. Gambit Medal progress vanishing after Quick Restart was a bug. None of these belong in a tier list, and the current tier list should not be rewritten on the strength of a fix.

{{< pro-tip >}}<strong>The 30-second version check</strong><br>Open the shop and look at Valhalla's Gambit. $8 means you are on 1.5.4b or later. $10 means your client is behind and none of the two design changes above apply to you yet.{{< /pro-tip >}}

If the shop offers you a Gambit you have not seen before, the three-token decision guide is the faster read than any tier list, because it starts from the state of your board instead of a ranking made for someone else's run.

## Community Verification & Resources

Both design lines are quoted from the official 1.5.4b post. The ADJACENT and shop rules are checked against the shipped game; if a later patch changes either rule, this page is updated.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.4b, 30 Sep 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.4b patch notes](https://steamdb.info/patchnotes/25623616/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
