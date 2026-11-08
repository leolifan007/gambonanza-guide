---
categories: ["Economy"]
tags:
  - "Economy"
  - "Bug Fixes"
  - "Gambits"
title: "Tooth's Gambit Finally Pays When You Sell It: Rebuilding the Sell-for-Gold Loop"
description: "Patch 1.5.4b fixed Tooth's Gambit not giving money when sold. Here is what a sell actually decides in Gambonanza, why the bug broke the loop, and how to rebuild the habit without inventing payout numbers."
date: "2026-11-08T13:39:00+08:00"
lastmod: "2026-11-08T13:45:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

If you sold Tooth's Gambit in September and the balance did not move, you did not misclick. The 1.5.4b notes list it plainly: fixed an issue where Tooth's Gambit wouldn't give money when selling it.

{{< game-icon name="money" >}}**Selling a Gambit is two decisions at once.** It frees one of your five slots and it should return money. Before 1.5.4b, one specific Gambit gave you the slot and kept the money.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

The payout works again, so the sell decision is a real trade again: a free slot plus money now, versus whatever that Gambit would have produced later. If you stopped selling because the money never arrived, restart the habit and check the balance once to confirm the fix.{{< /callout >}}

{{< diagram src="tooth-sell-payout-154b.svg" alt="The sell decision loop before and after the 1.5.4b Tooth's Gambit payout fix" caption="A broken payout removed half the reason to sell. The fix restores the loop, not a new rule." >}}

The [economy guide](/economy/) covers where money comes from; this page is about the one decision that turns a Gambit back into cash.

## What Selling Actually Costs You

Money in this game comes from winning games, from captures and from Gambits. You can hold at most five Gambits, and the shop between games offers three random ones. That cap is what makes selling interesting: keeping a Gambit you never trigger is not free, it is one fifth of your build sitting idle.

{{< game-icon name="bolt" >}}**A sale converts an idle slot back into a decision.** The cash can go into a piece, a Gambit, a token, a $2 reroll or the Max Piece on Board upgrade. The [shop economy page](/economy/) lays out those uses; the [upgrade breakdown](/max-piece-on-board-upgrade/) is the one that competes most directly with a mid-run sale.

When the payout did not arrive, the trade collapsed into a pure loss: you gave up the Gambit and got nothing portable back. Players reasonably concluded that selling was bugged in general and stopped doing it. That conclusion was too broad. The note names one Gambit.

| Decision | What you give up | What you should get back |
|---|---|---|
| Keep the Gambit | One of five slots | Its future triggers |
| Sell before 1.5.4b (Tooth's Gambit) | One slot | Slot only, payout missing |
| Sell on 1.5.4b or later | One slot | Slot plus money |
| Reroll the shop instead | $2 | A fresh set of offers |

{{< section-divider >}}

## Rebuilding the Habit Without Fake Numbers

The official note does not give a sell price for Tooth's Gambit, and this page will not invent one. What it does give is a behavioural rule: the sale should now move your balance. Build your loop around that observable fact rather than a spreadsheet of made-up returns.

- **Sell when the Gambit has no trigger on your current board.** An idle slot is the clearest case, and the [Gambits overview](/gambits/) explains how slots interact with new offers.
- **Sell when the shop in front of you has the actual answer.** A concrete upgrade beats a hoped-for proc later; the [token decision guide](/which-token-piece-gambit-tile/) gives the five-second test.
- **Do not sell to fund a reroll reflexively.** A $2 reroll is cheap, but it is still a gamble against three random offers.
- **Recheck the balance once.** If the money does not move, you are not on 1.5.4b or later and the fix is not live for you.

{{< callout type="danger" >}}<strong>One fix does not rewrite the economy</strong>

The 1.5.4b post fixes a payout. It does not change how much money winning a game gives, it does not change the $2 reroll, and it does not add a sell multiplier. Any guide that turns this line into a new gold-farming strategy is reading more into the note than the developer wrote.{{< /callout >}}

For the wider recovery patterns that follow a bad shop, the [gambit chain recovery guide](/gambit-chain-recovery-guide/) and the [pawn economy loop](/pawn-economy-loop/) are the natural next reads; both assume a working payout, which is now true again.

{{< diagram src="tooth-sell-payout-154b-detail.svg" alt="The two payoffs from selling a Gambit before and after the fix" caption="A slot always freed; after 1.5.4b the money does too." >}}

## Where This Sits in the 1.5.x Run of Fixes

1.5.1 made Barter's trade reset after a Graveyard and made stalemate reset the Graveyard. 1.5.4b fixed the Barter counter initialising at 0, the Medal progress reset, the phantom piece after a fall win, cursed tile expiry visuals and this payout. Put together, that is a month of patches aimed at state and money behaving consistently, not at rebalancing power.

{{< pro-tip >}}<strong>The 1.5.4b checklist</strong><br>If you are unsure whether a symptom was a rule or a bug, run the six-item fix checklist first. It is faster than rebuilding a strategy around behaviour the developer already removed.{{< /pro-tip >}}

And if the whole economy feels opaque, the FAQ collects the short answers on money, rerolls and selling in one place.

## Community Verification & Resources

The Tooth's Gambit payout fix is quoted from the official 1.5.4b post. The five-Gambit cap, shop composition and $2 reroll are from the shipped game facts. No sell value is stated because the official note gives none.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.4b, 30 Sep 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.4b patch notes](https://steamdb.info/patchnotes/25623616/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
