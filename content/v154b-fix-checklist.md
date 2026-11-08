---
categories: ["Shop & Economy"]
tags:
  - "Patch Updates"
  - "Bug Fixes"
  - "Shop"
title: "Six Gambit Bugs Fixed in 1.5.4b: A Check-Your-Client Checklist"
description: "The 1.5.4b post lists six fixes: Linux stretching, Tooth's Gambit payout, a Valhalla phantom piece, cursed tile expiration visuals, Barter's counter at 0, and Gambit Medal progress after Quick Restart. Here is how to tell each one is gone."
date: "2026-11-08T13:35:00+08:00"
lastmod: "2026-11-08T13:41:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

Some bugs cost you a run. Others quietly cost you a Gambit slot. The 1.5.4b fixes are mostly the second kind, which is exactly why players kept misreading them as balance changes for a month.

{{< game-icon name="check" >}}**Six fixes shipped on 30 September 2026.** Two were visual or platform issues, four were state bugs that made a Gambit or a progress counter behave as if it were broken, because it was.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

If a Gambit looked unusable, a sale paid nothing, a medal reset, or a cursed square never seemed to expire, check your client before you change your strategy. Those were all listed as fixes in 1.5.4b, not rules you needed to play around.{{< /callout >}}

{{< diagram src="v154b-fix-checklist.svg" alt="Six bug fixes in patch 1.5.4b grouped by symptom" caption="Four state bugs, one visual bug, one platform bug. Only two of them were ever visible on the board." >}}

The [1.5.1 to 1.5.3 hotfix breakdown](/v151-153-hotfix-breakdown/) handles the earlier reset rules; the six items below are strictly the 1.5.4b fix list.

## The Six Lines, Mapped to What You Actually Saw

{{< callout type="info" >}}<strong>Quick reference, no table needed</strong>

On Tooth's Gambit wouldn't give money when selling it: Sell one and watch the counter. 
On Barter's Gambit could appear with its counter set to 0 instead of 5: Check the counter when it is offered. 
On Valhalla's Gambit could leave a phantom piece after an enemy-fall win: Win by a fall, then start the next game. 
On Tile Expiration didn't visually update cursed tiles: Watch an expired cursed square clear. 
On Gambit Medal progress reset after Quick Restart: Restart once, reopen the medal view. 
On Linux stretching at certain resolutions: Set a second resolution and compare. 
{{< /callout >}}

The first four are the ones that changed decisions. A Gambit with a 0 counter is not a weak Gambit, it is a dead [slot](/gambits/) until the next shop. A sale that pays nothing breaks the sell-for-gold loop entirely. Both got fixed in the same post, so any advice written in September that works around them is now obsolete.

{{< game-icon name="money" >}}**The Barter confusion is worth separating.** Patch 1.5.1 made Barter's trade Gambit reset on the shop after a Graveyard. Patch 1.5.4b fixed the counter appearing at 0 instead of 5. Those are two different problems, and the [Barter guide](/barter-gambit-guide/) covers the first while this checklist covers the second.

{{< section-divider >}}

## Why a 0 Counter Was Worse Than It Looked

You can hold at most five Gambits. One of them arriving with a 0 counter means you are carrying four working Gambits into a fight while the shop is already behind you. The [Graveyard and stalemate reset page](/graveyard-stalemate-reset-guide/) explains the surrounding reset rules; the important point here is that this was an initialisation bug, not a hidden cost or a nerf.

- **Do not sell around it anymore.** If the counter reads 5 when offered, the fix is live.
- **Do not rewrite your reroll budget.** The $2 reroll was never the workaround for a broken counter.
- **Do update old notes.** Any checklist that says to skip Barter's Gambit on sight is describing a bug that no longer exists.

{{< callout type="tip" >}}<strong>The same applies to the Medal</strong>

Gambit Medal progress resetting after Quick Restart was a persistence bug. If you changed your restart habits to protect medal progress, you can drop that workaround. The [difficulty guide](/difficulty-guide/) covers how progress tiers unlock after a first clear, which is a separate system.{{< /callout >}}

{{< diagram src="v154b-fix-checklist-detail.svg" alt="Four ordered client checks to confirm the 1.5.4b fixes" caption="Four quick checks confirm whether your client actually has the fixes." >}}

## A Five-Minute Verification Pass

You do not need to replay a full run to check a patch this small. Work through the shop, one sale, one restart, and one expiring tile.

- Open a shop and look at any offered Gambit counter. It should read a real value, not 0.
- Sell a Gambit and watch the money display. It should move.
- Use Quick Restart once, then reopen the Gambit Medal view. Progress should still be there.
- Let a cursed tile expire in a boss game. The visual should clear with the expiry.
- Check Valhalla's Gambit shows $8. If it shows $10, you are on an older client and none of the above applies.

{{< pro-tip >}}<strong>Keep fixes out of your tier list</strong><br>When a patch says FIX, assume the intended behaviour was always the one you are now seeing. Rank [Gambits](/gambits/) on what they do at their best, not on the month they spent broken.{{< /pro-tip >}}

If a symptom persists after this pass, the [FAQ](/faq/) is the right next stop rather than another strategy rewrite, because a fix that did not land is a client or platform issue, not a build problem.

## Community Verification & Resources

All six lines are quoted from the official 1.5.4b post. Verification steps are derived from each listed symptom; no additional patch behaviour is assumed.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.4b, 30 Sep 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.4b patch notes](https://steamdb.info/patchnotes/25623616/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
