---
categories: ["Strategy & Guides"]
tags:
  - "Patch Updates"
  - "Game Mechanics"
title: "Gambonanza 1.5.1 to 1.5.3 Patch Notes Explained: Stalemate Resets the Graveyard"
description: "What every Gambonanza 1.5.1, 1.5.2b and 1.5.3 change actually means: Stalemate resets the Graveyard, Barter and Key of Life reset rules, Linux fixes, and renamed Enemy Modifiers."
game_version: ">=v1.5.0"
last_reviewed: "2026-09-24"
review_status: "current"
date: "2026-09-24"
hidden: false
---
{{< phase-tag "mid" >}}


{{< callout type="verdict" title="The Three Hotfixes That Matter" >}}
The 1.5.x hotfix line is small but it changes three real things. **Stalemate now resets the Graveyard** (1.5.1). **Barter's Gambit now resets on the shop after a Graveyard** (1.5.1). **Key of Life's Gambit now resets after a Stalemate** (1.5.1). The rest are presentation and platform fixes, but the "Enemy Modifiers" tab is now simply called "Enemies", which is worth knowing when you hunt for it.
{{< /callout >}}

{{< callout type="tip" title="Read the Resets Together" >}}
Three reset rules changed in a single hotfix. Read Barter, Key of Life, and the Graveyard as one system, not three isolated notes, because they interact inside the same run.
{{< /callout >}}


{{< diagram src="v151-153-timeline.svg" alt="Timeline of the 1.5.1 to 1.5.3 hotfixes" caption="The hotfix line runs from 1.5.1 on September 4 to 1.5.3 on September 17." >}}

## Why a Hotfix Line Deserves Its Own Guide

Major patches get the attention, but hotfixes are where the developer quietly rebalances the rules that bite you in a run. The 1.5.1 hotfix alone touches three Gambit and system reset rules. If you play Gambit-heavy builds that lean on repeatable triggers, these are not cosmetic notes. They change how many times per run you can expect a trigger to fire.

This guide covers every change in 1.5.1, 1.5.2b, and 1.5.3 in plain language, with a note on what each one means at the table.

## 1.5.1: The Rules Patch

### Stalemate Now Resets the Graveyard

This is the headline change of the hotfix line. A Stalemate event now resets the Graveyard. Before this, your Graveyard list of lost pieces persisted through a Stalemate. Now, when a Stalemate resolves, that list is cleared.

If you were relying on the Graveyard to recover an old loss after a long, slow stage, that safety net is gone. The reset means the Graveyard reflects only your recent losses, not your whole run. Our dedicated breakdown lives in the [Stalemate resets the Graveyard guide](/graveyard-stalemate-reset-guide/), and the fundamentals are in the [Graveyard system guide](/graveyard-system-guide/).

### Barter's Gambit Resets on the Shop After a Graveyard

Barter's Gambit lets you trade a BISHOP for another random piece a limited number of times, resetting when you enter the Shop. The 1.5.1 change adds a second reset condition: the trade now also resets after a Graveyard. That makes Barter more reliable across a run, because you are no longer gated on finding a Shop to refresh your uses. The full cycle is in the [Barter's Gambit guide](/barter-gambit-guide/).

### Key of Life's Gambit Resets After a Stalemate

Key of Life's Gambit now resets after a Stalemate. This mirrors the pattern of the other 1.5.1 changes: the developer is aligning reset rules so that system events (Shop, Graveyard, Stalemate) behave consistently across Gambits. If a Gambit felt "stuck" after a Stalemate before, this is the fix.

### Linux Letterboxing Fix

Some Linux devices showed black bars at the top and bottom of the screen due to a resolution and letterboxing issue. 1.5.1 fixes that. This matters for Steam Deck owners running the Linux build.

## 1.5.2b: The Cursor Fix

1.5.2b is a single-line patch: it fixes an issue where the cursor could be invisible on some Linux setups. There is nothing else to it. If you were fighting an invisible pointer, this is your fix.

## 1.5.3: Presentation and Navigation

1.5.3 is a quality-of-life pass across menus and controls:

- **Hover info layering:** pressing Pause or Info while hovering a piece or a Gambit now shows the description in front of the pause and info menu instead of behind it. This was a real annoyance on small screens.
- **Strains menu navigation:** fixed on Steam Deck and with a controller.
- **English typo:** corrected on the Screen Shake setting.
- **Gambit collection tab:** optimized so navigation is smoother when browsing all Gambits.
- **"Enemy Modifiers" renamed to "Enemies":** the tab is now just the word for enemies, updated across every localization (EN, FR, ES, PT-BR, PL, RU, TR, DE).

## Change Summary

| Version | Change | Type |
|---------|--------|------|
| 1.5.1 | Stalemate resets the Graveyard | Rule |
| 1.5.1 | Barter's Gambit resets on Shop after Graveyard | Rule |
| 1.5.1 | Key of Life's Gambit resets after Stalemate | Rule |
| 1.5.1 | Linux letterboxing resolution fix | Platform |
| 1.5.2b | Invisible cursor on some Linux setups fixed | Platform |
| 1.5.3 | Hover info shows above menus | UI |
| 1.5.3 | Strains menu controller navigation fixed | Input |
| 1.5.3 | Gambit collection tab navigation | UI |
| 1.5.3 | Enemy Modifiers renamed to Enemies | Localization |

## A Practical Example: Why the Reset Rules Matter

Say you are running a Barter-heavy economy build on PAWN. You burn all your trades early, then lose your Queen to a bad wave. Before 1.5.1, you waited for a Shop to refresh Barter, and a Stalemate did not clear your Graveyard, so your recovered pieces sat there indefinitely. After 1.5.1, the loop is tighter: a Graveyard visit refreshes Barter, and a Stalemate wipes the Graveyard. The net effect is that you plan resets deliberately instead of letting them pile up. Read the two systems together, not in isolation.

## What This Means for Your Builds

1. **Recovery builds:** a Stalemate is now a hard reset of your buyback list. Do not bank on old losses surviving one.
2. **Barter builds:** strictly better. Graveyard visits now refresh your trades.
3. **Key of Life users:** the reset after a Stalemate makes the Gambit more predictable across long runs.
4. **Handheld and Linux players:** the platform fixes remove two genuine friction points.

{{< section-divider >}}

## Where To Go Next

If you want to go deeper on the systems referenced here, read the [Barter's Gambit guide](/barter-gambit-guide/) and [Graveyard reset guide](/graveyard-stalemate-reset-guide/). They cover the mechanics this patch touches in full detail.

{{< pro-tip >}}Hotfix lines are where reset rules quietly change. A rule that reads like a footnote can move your whole economy build, so always scan the small patches.{{< /pro-tip >}}

## Community Resources

- [Official Gambonanza Steam News (hotfix announcements)](https://store.steampowered.com/news/app/3509230/)
- [Gambonanza Wiki - Stalemate](https://gambonanza.fandom.com/wiki/Stalemate)

---

*Guide updated for Gambonanza v1.5.x (hotfixes released September 2026). All changes verified against the official Steam news posts for 1.5.1, 1.5.2b, and 1.5.3.*
