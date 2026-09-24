---
categories: ["Economy"]
tags:
  - "Economy"
  - "Game Mechanics"
title: "Stalemate Resets the Graveyard in Gambonanza 1.5.1: What Changed and Why It Matters"
description: "Gambonanza 1.5.1 made Stalemate reset the Graveyard. Here is what that means for PAWN-difficulty recovery play, when to buy back pieces, and how the reset changes your run planning."
game_version: ">=v1.5.0"
last_reviewed: "2026-09-24"
review_status: "current"
date: "2026-09-24"
hidden: false
---
{{< phase-tag "mid" >}}


{{< callout type="verdict" title="The Short Answer" >}}
As of 1.5.1, a Stalemate resets the Graveyard. Before, your list of lost pieces survived a Stalemate; now it is cleared. If you play PAWN difficulty and lean on recovery, this means your buyback list reflects only recent losses, not your whole run. Plan recoveries around Stalemate events instead of assuming old losses stay available.
{{< /callout >}}

{{< callout type="tip" title="Treat the Reset as a Deadline" >}}
As of 1.5.1 a Stalemate clears the Graveyard, so the window to buy back a key piece runs from the loss to the next Stalemate. Buy what matters before that window closes.
{{< /callout >}}


{{< diagram src="graveyard-stalemate-reset.svg" alt="Graveyard behavior before and after the 1.5.1 Stalemate reset" caption="Before 1.5.1 the Graveyard persisted through a Stalemate. After 1.5.1 it resets." >}}

## The Graveyard, in One Paragraph

The Graveyard is a PAWN-difficulty system introduced in v1.4.0. It holds the last five chess pieces you lost during a run, and you can spend money to buy them back. Each recovered piece raises the cost of the remaining ones, so recovery is a declining-value purchase rather than a flat fee. From KNIGHT upward, the Strain system removes the Graveyard entirely, because higher tiers are meant to make losses stick.

If you want the full mechanics, our [Graveyard system guide](/graveyard-system-guide/) covers the buyback escalation and the priority order for which pieces are worth recovering.

## What 1.5.1 Changed

The 1.5.1 hotfix added a single, consequential line: Stalemate now resets the Graveyard.

Before the change, a Stalemate was a non-event for the Graveyard. Your lost pieces stayed listed, and you could recover a piece you lost many turns earlier if you had the gold. After the change, a Stalemate clears the list. The Graveyard now reflects only losses since the last Stalemate.

Why would the developer make this change? The likely reasoning is consistency. The 1.5.1 hotfix aligned several reset rules at once, including making Key of Life's Gambit and Barter's Gambit reset on Stalemate and Graveyard events. Treating the Graveyard as something that resets on a major board event fits that pattern: system events should reset system state instead of leaving stale entries lying around.

## What It Means for Recovery Play

The change tightens the recovery window. Three practical consequences:

- **Old losses expire.** If you lose a Queen early and a Stalemate happens before you can afford to buy it back, that Queen is gone from the list. Time your recoveries before a Stalemate if the piece matters.
- **Recover decisively.** The escalation cost already punished scattered buys. The Stalemate reset adds urgency: delaying a recovery risks losing the option entirely.
- **Budget earlier.** If you know a Stalemate is coming, front-load the recovery you actually need instead of waiting for a cheaper moment that may never arrive.

Our [Stalemate and Bunker rework guide](/stalemate-bunker-rework-guide/) covers the older v1.3.0 change where Stalemate began resetting after boss fights, which is useful context for why the system behaves as it does now.

## A Practical Example

You are on PAWN and you lose your Bishop in Stage 2. You plan to buy it back once your economy recovers. In Stage 3, a long, slow exchange ends in a Stalemate. Before 1.5.1, your Bishop would still be sitting in the Graveyard, waiting. After 1.5.1, the Stalemate clears the list, and the Bishop is no longer recoverable.

The lesson is simple: if a lost piece matters to your build, treat the window between the loss and the next Stalemate as your deadline. Buy it back while you still can, even if the price is slightly worse than you hoped.

## Recovery Timing Checklist

| Situation | Before 1.5.1 | After 1.5.1 |
|-----------|--------------|-------------|
| Loss followed by many turns | Piece stays listed | Piece stays until a Stalemate |
| Stalemate occurs | List survives | List resets |
| Delayed recovery | Always possible | Only until the next Stalemate |
| Best practice | Buy eventually | Buy before the next Stalemate |

## What This Means for Your Builds

1. **Recovery is time-limited now.** Treat a Stalemate as the end of your buyback window.
2. **Prioritize hard.** Since the list can reset, spend on the piece you need most, first.
3. **PAWN play gets slightly tenser.** The safety net is still there, but it now has a clock.
4. **Nothing changed above PAWN.** The Graveyard does not exist from KNIGHT upward, so this is a PAWN-only consideration.

{{< section-divider >}}

## Where To Go Next

If you want to go deeper on the systems referenced here, read the [Graveyard system guide](/graveyard-system-guide/) and [Stalemate rework guide](/stalemate-bunker-rework-guide/). They cover the mechanics this patch touches in full detail.

{{< pro-tip >}}Since the list can reset, spend on your single most important lost piece first. Scattered recovery was already punished by the escalating cost; now it is also time-limited.{{< /pro-tip >}}

## Community Resources

- [Official Gambonanza Steam News (1.5.1 hotfix)](https://store.steampowered.com/news/app/3509230/)
- [Gambonanza Wiki - Stalemate](https://gambonanza.fandom.com/wiki/Stalemate)

---

*Guide updated for Gambonanza v1.5.1 (released September 2026). The Stalemate reset of the Graveyard is confirmed in the official 1.5.1 Steam news post.*
