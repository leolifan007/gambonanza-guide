#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write 10 v1.5.x articles as UTF-8 without BOM. ASCII-safe punctuation only."""
import os

OUT = "content"
DATE = "2026-09-24"

def fm(cats, tags, title, desc, ver=">=v1.5.0"):
    lines = ["---"]
    lines.append("categories: [%s]" % ", ".join('"%s"' % c for c in cats))
    lines.append("tags:")
    for t in tags:
        lines.append('  - "%s"' % t)
    lines.append('title: "%s"' % title)
    lines.append('description: "%s"' % desc)
    lines.append('game_version: "%s"' % ver)
    lines.append('last_reviewed: "%s"' % DATE)
    lines.append('review_status: "current"')
    lines.append('date: "%s"' % DATE)
    lines.append("hidden: false")
    lines.append("---")
    return "\n".join(lines) + "\n\n"

ARTICLES = {}

ARTICLES["v150-patch-breakdown.md"] = fm(
    ["Strategy & Guides"], ["Patch Updates", "Game Mechanics"],
    "Gambonanza 1.5.0 Patch Breakdown: UI Revamp, Steam Deck Verified & Enemy Power Feedback",
    "Complete breakdown of Gambonanza v1.5.0: the UI and text revamp, clearer enemy power trigger feedback, achievement fixes, and official Steam Deck Verified status. Updated for patch 1.5.x."
) + """{{< callout type="verdict" title="Patch Summary" >}}
v1.5.0 is a polish and accessibility update, not a balance shakeup. The three things that matter: a **UI and text revamp** that makes the board far easier to read (mainly for Steam Deck), **new feedback when an enemy power is about to trigger** so you can react in time, and **several achievement bug fixes**. The headline is that Gambonanza is now **officially Steam Deck Verified**. No Gambit numbers changed, so your builds carry over untouched.
{{< /callout >}}

{{< diagram src="v150-change-map.svg" alt="v1.5.0 change map across UI, enemy powers, achievements and Steam Deck" caption="v1.5.0 ships four strands of change: UI, enemy power feedback, achievement fixes, and Steam Deck verification." >}}

## What Landed in 1.5.0

This is every material change pulled straight from the official 1.5.0 Steam news post, plus the hotfixes that followed it (1.5.1, 1.5.2b, 1.5.3). If you only read one section, read the verdict above: nothing here changes your Gambit math, so your existing tier lists and build notes are still valid.

### UI Revamp for Readability

The single biggest change in 1.5.0 is a UI overhaul aimed at making text easier to read. The developer notes are explicit that this mainly affects Steam Deck, where the board and the information panels are compressed onto a small screen.

In practice this means piece labels, Gambit descriptions, and menu text are clearer than they were before. If you played earlier builds on a handheld and squinted at a crowded board, this patch is the fix. On desktop the change is subtler but still present, especially in the sidebar and the in-run HUD.

The two systems this helps most:

- **Reading the board at a glance.** Faster recognition of which piece is where means faster decisions.
- **Reading Gambit text mid-run.** Less time parsing a tooltip, more time playing.

### Clearer Feedback When an Enemy Power Triggers

The second headline change is better feedback when an enemy power is about to fire. Before 1.5.0, it was easy to lose a piece to an enemy ability you did not see coming because the visual cue was too subtle. 1.5.0 adds a clearer prompt that makes the incoming trigger more obvious.

The practical consequence is that you now get a warning window. Treat it as a reaction cue:

- When the prompt appears, re-check which of your pieces is exposed.
- Decide immediately whether to shield, move, or accept the loss.
- Do not spend the window reading a tooltip. The cue is short.

Our [enemy powers guide](/enemy-powers-warning-guide/) breaks down how to read these triggers and what to do in the warning window.

### Achievement Bug Fixes

Several Steam Achievements were failing to fire correctly, and 1.5.0 fixes a batch of them. If you met an achievement condition and did not get credit, the fix means it should now register when the condition is met again. The developer did not enumerate every achievement touched, so the honest guidance is: replay the condition once and confirm.

### Steam Deck Verified

Gambonanza is now officially Steam Deck Verified. That is a meaningful signal: the game has been checked against Valve's compatibility criteria for input, legibility, and stability on the handheld. If you were holding off on buying for the Deck, the barrier is gone.

{{< callout type="tip" >}}
Verified status does not mean the default settings are perfect for you. Text size is a personal preference and the Deck's screen is small. Spend two minutes in Settings before your first run. Our [Steam Deck settings guide](/steam-deck-settings-guide/) walks through the exact toggles worth changing.
{{< /callout >}}

## Change Summary

| Area | What Changed | Impact |
|------|--------------|--------|
| UI and text | Revamp for readability (mainly Steam Deck) | Faster board reading |
| Enemy powers | Clearer feedback before a power triggers | Reactive warning window |
| Achievements | Several bug fixes | Conditions fire correctly |
| Platform | Officially Steam Deck Verified | Confident handheld play |
| Balance | No Gambit number changes | Builds carry over |

## What This Means for Your Builds

1. **Nothing changed numerically.** If you were mid-climb on a build, keep going. No Gambit probabilities, prices, or effects moved in 1.5.0.
2. **Handheld players get a real upgrade.** The readability changes plus Verified status make the Deck a first-class way to play.
3. **Reactive play gets better.** The enemy power warning turns some unavoidable losses into avoidable ones.
4. **Achievement hunters catch up.** Re-run any condition that failed to register.

## Community Resources

- [Official Gambonanza Steam News (1.5.0 announcement)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Gambits](https://gambonanza.fandom.com/wiki/Gambits){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (released August to September 2026). All changes verified against the official Steam news posts for 1.5.0, 1.5.1, 1.5.2b, and 1.5.3.*
"""

ARTICLES["v151-153-hotfix-breakdown.md"] = fm(
    ["Strategy & Guides"], ["Patch Updates", "Game Mechanics"],
    "Gambonanza 1.5.1 to 1.5.3 Patch Notes Explained: Stalemate Resets the Graveyard",
    "What every Gambonanza 1.5.1, 1.5.2b and 1.5.3 change actually means: Stalemate resets the Graveyard, Barter and Key of Life reset rules, Linux fixes, and renamed Enemy Modifiers."
) + """{{< callout type="verdict" title="The Three Hotfixes That Matter" >}}
The 1.5.x hotfix line is small but it changes three real things. **Stalemate now resets the Graveyard** (1.5.1). **Barter's Gambit now resets on the shop after a Graveyard** (1.5.1). **Key of Life's Gambit now resets after a Stalemate** (1.5.1). The rest are presentation and platform fixes, but the "Enemy Modifiers" tab is now simply called "Enemies", which is worth knowing when you hunt for it.
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

## Community Resources

- [Official Gambonanza Steam News (hotfix announcements)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Stalemate](https://gambonanza.fandom.com/wiki/Stalemate){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (hotfixes released September 2026). All changes verified against the official Steam news posts for 1.5.1, 1.5.2b, and 1.5.3.*
"""

ARTICLES["steam-deck-settings-guide.md"] = fm(
    ["Strategy & Guides"], ["Tips", "Game Mechanics"],
    "Gambonanza on Steam Deck: Best Settings for Text, Cursor & Controller",
    "Gambonanza is now Steam Deck Verified. Here are the settings worth changing for text readability, letterboxing, cursor visibility, and controller navigation so handheld runs feel as good as desktop."
) + """{{< callout type="verdict" title="The Short Answer" >}}
Gambonanza is officially Steam Deck Verified as of v1.5.0, and the 1.5.x line fixed the two things that hurt handheld play most: text readability and an invisible-cursor bug on some Linux setups. Set aside two minutes before your first run. Turn on the readability improvements, confirm there is no letterboxing, and use the updated Strains menu navigation. That is the whole checklist.
{{< /callout >}}

{{< diagram src="steamdeck-settings-flow.svg" alt="Steam Deck setup flow across display, controls and in-game settings" caption="Work through display and controls first, then tune in-game Extras for readability." >}}

## Why the Deck Needs Its Own Setup Guide

Gambonanza is a busy game. A small chess board, a dense Gambit sidebar, and a compact HUD are all fighting for space. On desktop you have monitor real estate to spare. On the Steam Deck you have a seven-inch screen and a controller. That is exactly why the 1.5.0 UI revamp targeted the Deck, and why Verified status matters: Valve's criteria include legibility, default input, and stability on the handheld.

The good news is the game is light. This is not a shooter where you are chasing framerates. Your setup time is better spent on readability and controls than on performance.

## Text and Readability

The 1.5.0 patch revamped the UI to make text easier to read, with the developer noting it mainly affects Steam Deck. Combined with the Verified status, that means the default experience is now good rather than merely playable.

What to check:

- **Read the board at a glance.** After the revamp, labels should be legible without zooming. If they are not, your device may be running a stale build. Update.
- **Use the algebraic notation toggle** if you read chess coordinates. It adds column and row labels next to tiles, which makes positions unambiguous on a small screen.
- **Skip animations** to cut Gachapon and Piece Wheel transitions, which shortens the time between decisions. On a handheld, fewer animations means less waiting.

Our [UI and text readability guide](/ui-text-readability-guide/) goes deeper on what the revamp changed and how to use it.

## Display and Letterboxing

Some Linux devices, including Steam Deck configurations, showed black bars at the top and bottom of the screen before 1.5.1. That letterboxing issue is fixed. If you still see bars after updating, check the game's resolution settings and confirm the aspect ratio matches the Deck's display.

A clean, full-screen board matters more here than on any other platform, because every pixel of the board is information.

## Controls and Navigation

The 1.5.3 hotfix fixed navigation on Steam Deck and with a controller in the Strains menu. The Strains menu is where you review the difficulty modifiers attached to a run, so being able to move through it cleanly is not a minor detail.

Practical control notes:

- **Strains menu:** navigation now works as expected on Deck and controller. Review your modifiers before committing to a climb.
- **Gambit collection tab:** optimized in 1.5.3 for smoother navigation. Browsing all Gambits is now less of a chore.
- **Hover info:** 1.5.3 fixed the case where pressing Pause or Info while hovering a piece or Gambit showed the description behind the menu. It now appears in front, which matters when you tap a tooltip on a small screen.
- **Trackpad:** if you prefer trackpad-style pointing, the Deck's trackpads work well for hovering tooltips. Many players find them more precise than the stick for reading Gambit text.

Full control details are in the [controller and gamepad guide](/controller-gamepad-guide/).

## A Practical Deck Session

Here is a concrete sequence for a fresh install on the Deck:

1. Launch the game and confirm it is on the latest 1.5.x build.
2. Open Settings and check the display fills the screen with no letterboxing.
3. Turn on skip animations and, if you read chess notation, algebraic notation.
4. Start on PAWN so the Graveyard safety net is active while you learn the Deck's input.
5. Run one short game purely to test controls, not to win. Confirm the Strains menu and Gambit collection navigate cleanly.
6. Only then start a serious climb.

## Settings Checklist

| Setting | Recommended | Why |
|---------|-------------|-----|
| Game build | Latest 1.5.x | Text revamp and platform fixes |
| Display fit | Full screen, no bars | Letterboxing fixed in 1.5.1 |
| Skip animations | On | Shorter decision loops |
| Algebraic notation | On if you read it | Unambiguous positions |
| Strains navigation | Verify in menu | Fixed in 1.5.3 |
| Cursor visibility | Verify | Linux cursor fix in 1.5.2b |

## What This Means for Your Builds

1. **Nothing about your strategy changes on Deck.** The same Gambit math applies; only the presentation improves.
2. **Readability is now a platform strength, not a weakness.** The revamp plus Verified status put Deck play on par with desktop for information access.
3. **Controls are reliable.** With the Strains and collection fixes, you can manage modifiers and browse Gambits without friction.
4. **Update before judging.** If your Deck copy feels rough, it is probably an older build.

## Community Resources

- [Official Gambonanza Steam News (Steam Deck Verified)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza on Steam](https://store.steampowered.com/app/3509230/){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (released August to September 2026). Readability revamp, letterboxing fix, cursor fix, and navigation fixes verified against the official Steam news posts.*
"""

ARTICLES["barter-gambit-guide.md"] = fm(
    ["Gambits & Combos"], ["Gambits", "Economy"],
    "Barter's Gambit Guide: Shop Reset Cycles & Graveyard Interaction (v1.5.1)",
    "How Barter's Gambit works in Gambonanza: a limited number of BISHOP trades per run, reset on entering the Shop, and now also after a Graveyard as of 1.5.1. Full cycle and build notes."
) + """{{< callout type="verdict" title="The Short Answer" >}}
Barter's Gambit lets you sell a BISHOP and get another random piece in return, up to a limited number of times, resetting when you enter the Shop. The 1.5.1 hotfix adds a second reset: the trade also resets after a Graveyard. That makes Barter one of the more forgiving economy Gambits in the game, because two different systems now refresh your uses.
{{< /callout >}}

{{< diagram src="barter-cycle.svg" alt="Barter's Gambit reset cycle through reward, shop and graveyard" caption="Barter counts down as you trade, then resets on entering the Shop or after a Graveyard." >}}

## What Barter's Gambit Does

Barter's Gambit is a trade engine. Selling a BISHOP grants you another random piece. The Gambit has a limited number of uses per cycle, and that cycle resets when you enter the Shop. The design intent is straightforward: turn a piece you do not need into a roll at a piece you might.

Two properties make it interesting:

- **It converts a specific piece into randomness.** You are not choosing the reward. You are spending a Bishop for a lottery ticket.
- **It has a reset condition.** Because uses refresh on Shop entry, Barter rewards players who plan their shop visits around a trade sequence rather than dumping trades at random.

The developer has not published exact per-cycle use counts in the patch notes, so treat the "limited uses" as a real constraint and plan around it rather than assuming a fixed number.

## The 1.5.1 Change: Reset After a Graveyard

The 1.5.1 hotfix added a second reset trigger: Barter's trade now resets on the shop after a Graveyard. In plain language, visiting the Graveyard can now refresh your Barter uses, not just entering the Shop.

Why this matters:

- **More trades per run.** Two reset paths instead of one means Barter comes back online more often.
- **Better synergy with recovery play.** The Graveyard is a PAWN-difficulty recovery system. A Barter player who buys back pieces is already visiting it. Now that visit does double duty.
- **Less dead time.** Before the change, a Barter player who missed a Shop could be stuck. Now the reset has redundancy.

This is a strict improvement. There is no scenario where the added reset hurts you.

## How to Play Barter Well

The core decision is simple: **only trade a Bishop you are happy to lose.** Barter does not let you pick the reward, so you are trading certainty for variance. The question is always whether the Bishop in front of you is worth more than an unknown piece.

Guidelines:

- **Trade spare Bishops, not core ones.** If a Bishop is part of your win condition, do not feed it to Barter.
- **Trade when your piece count is low.** A random piece is best when it fills a gap. If your board is already full, you may not have room for the reward.
- **Plan resets deliberately.** Bank your trades and spend them across a Shop or Graveyard visit rather than dribbling them out.
- **Pair it with economy Gambits.** Barter is fundamentally a value-conversion tool. It works best alongside Gambits that reward piece count or piece variety.

## A Practical Example

Say you draw Barter's Gambit in Stage 1 while your board is thin: two Pawns and a Bishop you picked up but never integrated. Your build needs another body to hold the center. Trading the spare Bishop for a random piece is close to free value here, because the Bishop was not doing anything and an extra piece will.

Now say you draw Barter in Stage 4 with a Bishop that is anchoring a diagonal your whole defense depends on. Do not trade it. The expected value of a random piece does not beat a working defensive anchor.

The Gambit is not "always good" or "always bad". It is a conditional trade tool. Read your board before you use it.

## Best Pairings

| Pairing | Why It Works |
|---------|--------------|
| Graveyard recovery | Both lean on the same visits; 1.5.1 makes Barter refresh on a Graveyard |
| Piece-count payoffs | More bodies means more triggers for count-based Gambits |
| Wide-board builds | Room to place the random reward without crowding |
| Shop-routing builds | Players who already time Shops get a second reset lane |

{{< callout type="tip" >}}
Think of Barter as a conversion rate, not a freebie. Every trade spends a real Bishop. If you would not sell that Bishop for a random piece in the Shop, do not let Barter do it either.
{{< /callout >}}

## What This Means for Your Builds

1. **Barter is a conditional pick.** Strong when you have spare Bishops and board room; weak when every piece is load-bearing.
2. **The 1.5.1 reset is pure upside.** Plan for two reset paths and use both.
3. **It pairs naturally with the Graveyard on PAWN.** The two systems reinforce each other after 1.5.1.
4. **It is not a panic button.** Selling a core Bishop for a random reward is how Barter loses you runs.

## Community Resources

- [Official Gambonanza Steam News (1.5.1 announcement)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Gambits](https://gambonanza.fandom.com/wiki/Gambits){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.1 (released September 2026). The Barter reset after a Graveyard is confirmed in the official 1.5.1 Steam news post.*
"""

ARTICLES["enemy-powers-warning-guide.md"] = fm(
    ["Boss Battles"], ["Enemies & Waves", "Game Mechanics"],
    "Reading Enemy Powers in Gambonanza: The 1.5 Trigger Warnings Explained",
    "Gambonanza v1.5.0 added clearer feedback when an enemy power is about to trigger. Here is how to read the warning, what to do in the window, and how it turns avoidable losses into recoverable turns."
) + """{{< callout type="verdict" title="The Short Answer" >}}
v1.5.0 added better feedback when an enemy power is about to trigger, so the ability is more obvious before it fires. That converts some previously unavoidable losses into avoidable ones. When the warning appears, stop reading tooltips and immediately decide whether to shield, move, or accept the loss. The warning window is short, and it rewards players who already understand what the enemy power does.
{{< /callout >}}

{{< diagram src="enemy-power-warning.svg" alt="Enemy power feedback before and after v1.5" caption="Before 1.5 the trigger cue was easy to miss. After 1.5 a clearer prompt appears before the power fires." >}}

## Why Enemy Power Feedback Was a Problem

Enemy powers are the abilities that make Gambonanza's enemies more than vanilla chess pieces. Some eat pieces, some modify the board, some punish specific positions. The trouble was never that the powers existed. The trouble was that their activation was not obvious enough. You could lose a key piece to a power you did not see coming, and the game gave you little chance to respond.

v1.5.0 addresses that directly. The developer notes describe "better feedback when an enemy power is about to trigger, to make them more obvious." That phrasing matters: the power still triggers, but you now get a clearer cue beforehand.

## How to Read the Warning Window

The cue is a fair warning, not a pause button. The power will still fire. What changes is that you have a moment to react. Use it with discipline:

- **Identify the target.** The most common mistake is reacting to the warning without knowing which of your pieces is threatened. Look first.
- **Pick one response, not three.** Either shield the piece, move it out of range, or accept the loss on purpose. Do not split your attention across options in a two-second window.
- **Do not open a tooltip.** The warning window is not the time to read. If you do not already know what the power does, that is a gap to close between runs, not during one.
- **Accept losses deliberately.** Sometimes eating the loss is correct. A pawn lost to save a Queen is a good trade. The warning helps you make that call consciously instead of discovering it after the fact.

## A Practical Example

Picture a Stage 3 board where an enemy power is about to fire and your Bishop is the piece it threatens. Before 1.5.0, you might not have noticed until the Bishop was gone. After 1.5.0, the warning appears. You have two viable lines: shield the Bishop if your build depends on it, or move it and let a Pawn absorb the hit if you can spare one. The warning turns a passive loss into a decision.

If you are running a build where the Bishop anchors a diagonal, you shield. If the Bishop is expendable and you want to keep tempo, you move and accept the Pawn loss. Either way, the choice is yours now.

## Which Powers Deserve the Most Attention

The developer did not enumerate every power in the 1.5.0 notes, so the honest approach is to learn the categories that hurt most:

| Power Type | Threat | Best Response |
|-----------|--------|---------------|
| Piece capture | Direct loss of a piece | Shield or relocate the target |
| Board modification | Alters tiles you rely on | Reposition before it lands |
| Positional punish | Rewards the enemy for your setup | Break the pattern or hold |
| Economy drain | Costs you gold or stock | Accept if minor, else shield |

Learn which category each enemy falls into, and the warning window becomes a reflex rather than a scramble.

{{< callout type="tip" >}}
The best time to learn enemy powers is not during a run. Use Enhanced AI Mode or a low-stakes PAWN game to watch powers trigger and note what the warning looks like for each enemy. When it counts, you want recognition, not analysis.
{{< /callout >}}

## Pairing Warnings With Board Reading

The warning is only useful if you already read the board well. Two habits sharpen that:

- **Track threats every turn,** not just when a warning fires. If you know which piece is exposed, the warning confirms what you already suspect.
- **Keep a mental priority list** of which pieces are worth protecting. When the warning appears, you check the list, not the whole board.

Our [UI and text readability guide](/ui-text-readability-guide/) covers how the 1.5 revamp makes the board easier to scan in the first place, which directly supports this habit.

## What This Means for Your Builds

1. **Reactive play is rewarded.** Losses that were once unavoidable now have a response window.
2. **Knowledge compounds.** The warning is only as useful as your understanding of the power behind it.
3. **Protect your anchors.** Builds with a single load-bearing piece benefit most from the new cue.
4. **No numbers changed.** This is a feedback change, not a rebalance. Your counters still work.

## Community Resources

- [Official Gambonanza Steam News (1.5.0 announcement)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Board Formations](https://gambonanza.fandom.com/wiki/Board_Formations){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.0 (released August 2026). The enemy power feedback change is confirmed in the official 1.5.0 Steam news post.*
"""

ARTICLES["controller-gamepad-guide.md"] = fm(
    ["Beginner"], ["Tips", "Game Mechanics"],
    "Gambonanza Controller & Gamepad Guide: Strains, Gambit Collection & Deck Navigation",
    "Gambonanza v1.5.3 fixed Strains menu navigation on Steam Deck and controllers, and optimized the Gambit collection tab. Here is the full control map and how to browse menus without friction."
) + """{{< callout type="verdict" title="The Short Answer" >}}
Gambonanza has full controller support, and the 1.5.3 hotfix fixed the two menu flows that were roughest on a gamepad: the **Strains menu** and the **Gambit collection tab**. If you play on Steam Deck or with a controller, these fixes are the difference between a smooth run and a fight with the UI. The control scheme itself is simple once you know where everything lives.
{{< /callout >}}

{{< diagram src="controller-nav-map.svg" alt="Map of controller-navigated menus in Gambonanza" caption="The main menus you navigate with a controller: Settings, Strains, Gambit collection, and the in-run HUD." >}}

## Why Controller Support Matters Here

Gambonanza is a menu-heavy game. A run involves the board, the Gambit sidebar, the Shop, the Graveyard, the Strains menu, and the Gambit collection. Each is a distinct interface. When controller navigation works, the game feels native on a handheld. When it does not, you feel every menu.

The 1.5.3 hotfix targeted exactly this. It fixed navigation on Steam Deck and with a controller in the Strains menu, and optimized the Gambit collection tab for smoother navigation. Both are menus you visit often, so the fixes have an outsized impact on how the game feels.

## The Core Menus and What They Do

Understanding what each menu is for makes navigation intuitive, because you know what you are trying to reach.

- **Settings, including the Extra category.** This is where the quality-of-life toggles live: skip animations, algebraic notation, unlock all, and erase save data.
- **Strains menu.** This is where the difficulty modifiers attached to a run are listed. On higher difficulties, Strains are the reason the Graveyard disappears and prices rise. Review it before a climb. Navigation here was fixed in 1.5.3.
- **Gambit collection.** The full catalog of Gambits. Browsing it is how you learn what exists. Navigation was optimized in 1.5.3.
- **In-run HUD.** The board plus the Gambit sidebar. Hovering a piece or Gambit and pressing Pause or Info now shows the description in front of the menu (fixed in 1.5.3).

## Tips That Make Controller Play Better

Controller play rewards a few habits:

- **Use the hover-info flow deliberately.** On a small screen, tapping into a tooltip is the fastest way to read a Gambit. The 1.5.3 fix means the description now lands in front of the pause and info menu instead of behind it, so the read is clean.
- **Learn the Strains menu early.** Do not treat it as a settings screen you ignore. Your modifiers define the run's rules. Open it once per climb and read it.
- **Browse the collection between runs.** The optimized Gambit collection tab is best used as a study tool, not mid-combat. Learn names between games so you recognize them during one.
- **Confirm your mapping once.** If you use a non-Deck controller, confirm the D-pad and stick behavior in the Settings menu before a serious run. Controller navigation in the Settings menu was improved back in the 1.4 hotfix line, so it should feel responsive.

{{< callout type="tip" >}}
If you came to Gambonanza as a chess player, the algebraic notation toggle in the Extra settings is worth turning on. On a controller, reading positions by coordinate is often faster than pointing at them.
{{< /callout >}}

## A Practical Controller Session

Here is a clean way to run your first controller games:

1. Open Settings and confirm controls respond the way you expect.
2. Turn on skip animations to shorten the loop.
3. Open the Strains menu once so you know the run's modifiers.
4. Play a PAWN game to test board navigation and tooltip hovering.
5. Between runs, browse the Gambit collection to build recognition.
6. Only then start a climb on a higher difficulty.

## Menu and Fix Reference

| Menu or Action | Status After 1.5.3 | Notes |
|----------------|--------------------|-------|
| Strains menu navigation | Fixed | Works on Deck and controller |
| Gambit collection tab | Optimized | Smoother browse |
| Hover info on piece/Gambit | Fixed | Description shows in front of menus |
| Settings navigation | Improved since 1.4 | Responsive on controller |

## What This Means for Your Builds

1. **Controller play is now first-class.** The two rough menus are fixed, so nothing about the run flow fights you.
2. **Strains knowledge is the real skill.** Navigation being smooth does not help if you never open the menu. Read your modifiers.
3. **Collection browsing pays off.** A smooth Gambit tab is a learning tool. Use it between runs.
4. **No strategy changed.** This is an input and UI fix, not a balance change.

## Community Resources

- [Official Gambonanza Steam News (1.5.3 hotfix)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Gambits](https://gambonanza.fandom.com/wiki/Gambits){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.3 (released September 2026). Strains navigation, collection tab, and hover info fixes are confirmed in the official 1.5.3 Steam news post.*
"""

ARTICLES["strain-system-guide.md"] = fm(
    ["Difficulty & Progression"], ["Difficulty & Progression", "Game Mechanics"],
    "Gambonanza Strain System Guide: Every Difficulty Modifier & When the Graveyard Disappears",
    "How the Gambonanza Strain system works: PAWN is the learning tier with the Graveyard, and from KNIGHT upward Strains add modifiers and remove safety nets. A plain guide to every difficulty step."
) + """{{< callout type="verdict" title="The Short Answer" >}}
The Strain system is how Gambonanza layers difficulty. PAWN is the learning tier and the only one with the Graveyard safety net. Starting from KNIGHT, Strains add modifiers and remove that net. If a run suddenly feels harder, it is almost always a Strain, not your build. Read the Strains menu before every climb so you know what rules you are agreeing to.
{{< /callout >}}

{{< diagram src="strain-ladder.svg" alt="Gambonanza difficulty ladder from PAWN to KING with Strain modifiers" caption="From PAWN to KING, each step adds modifiers and removes safety nets." >}}

## What the Strain System Is

Gambonanza's difficulty is not a single slider. It is a ladder of tiers, and each tier above the first adds modifiers called Strains. A Strain is a rule change. It might raise prices, shrink your Stock, change who plays first, or remove a system entirely.

The design intent is clear from the developer's own notes: the base game should be a playground where breaking it is fun, but higher tiers are meant to punish mistakes. The Strain system is the mechanism that makes the punishment scale. On PAWN, you get room to experiment. On KING, you get a challenge the developer has openly said they have not beaten themselves.

## The Difficulty Ladder

The exact set of Strains at each tier is not fully enumerated by the developer in the patch notes, but the shape of the ladder is well established from the game's own progression and the 1.4 notes. Here is the ladder as the game presents it:

| Tier | Character | Key Difference |
|------|-----------|----------------|
| PAWN | Learning tier | Graveyard safety net is active |
| ROOK | First escalation | Higher prices, WAIT costs more, less Stock room |
| KNIGHT | Real difficulty | Enemy plays first, Queens leave the Shop, tiles single-use |
| BISHOP | Harder | Tightened economy and Stock pressure |
| QUEEN | Severe | Tiles limited to once per run |
| KING | Maximum | The big challenge tier |

The precise modifier list per tier is visible in the in-game Strains menu, which is why reading it matters more than memorizing a table from a guide.

## The Graveyard Is the PAWN Safety Net

The Graveyard is the system most tied to difficulty. It holds your last five lost pieces during a run, and on PAWN you can spend gold to buy them back, with each recovery raising the cost of the rest. It is a genuine second chance for learning a build.

The critical detail: **the Graveyard disappears from KNIGHT upward via the Strain system.** This is deliberate. At higher tiers, losing a piece is supposed to hurt, so the game removes the buyback option to keep the risk calculus honest.

The practical takeaway is that your recovery planning is tier-dependent:

- **On PAWN,** you can afford to be a little loose. The Graveyard catches your worst variance.
- **From KNIGHT up,** treat every loss as permanent. Play like the safety net does not exist, because it does not.

Our [Graveyard system guide](/graveyard-system-guide/) covers the buyback math, and the [Stalemate resets the Graveyard guide](/graveyard-stalemate-reset-guide/) covers the 1.5.1 reset rule.

## Why Reading the Strains Menu Matters

A common mistake is to start a climb and then feel confused when prices are higher or the enemy moves first. Those are Strains, and the game lists them. The menu was made easier to navigate on controller and Steam Deck in the 1.5.3 hotfix, which suggests the developer knows players need to consult it.

A quick pre-climb ritual:

- Open the Strains menu.
- Read each modifier aloud or in your head.
- Ask whether your current build tolerates them.
- Only then commit.

This takes less than a minute and prevents the most common "why is this run so hard" confusion.

## A Practical Example

You are comfortable on PAWN and decide to climb to KNIGHT. Before you start, you open the Strains menu. You see that the enemy plays first, Queens are removed from the Shop, and tiles can only be used once per run. Armed with that, you adjust before the first turn: you plan for a slower opening because the enemy moves first, you stop assuming you can buy a Queen later, and you commit to your tile choices because you cannot reuse them.

Those three adjustments are the entire difference between a KNIGHT climb that feels fair and one that feels brutal. The information was always available. The skill is reading it.

## What This Means for Your Builds

1. **Tier defines your safety net.** PAWN has the Graveyard; KNIGHT and up do not.
2. **Strains are the real difficulty.** Read them before committing to a climb.
3. **Builds must adapt to tier.** A build that relies on a Shop Queen will fail on KNIGHT.
4. **No P2W shortcuts.** Higher tiers are meant to punish mistakes, and the Strain system enforces that.

## Community Resources

- [Official Gambonanza Steam News](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - King Difficulty Guide](https://gambonanza.fandom.com/wiki/King_Difficulty_Guide){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (released August to September 2026). The Graveyard tier gating and difficulty escalation are described in the official v1.4.0 and v1.5.x Steam news posts.*
"""

ARTICLES["graveyard-stalemate-reset-guide.md"] = fm(
    ["Economy"], ["Economy", "Game Mechanics"],
    "Stalemate Resets the Graveyard in Gambonanza 1.5.1: What Changed and Why It Matters",
    "Gambonanza 1.5.1 made Stalemate reset the Graveyard. Here is what that means for PAWN-difficulty recovery play, when to buy back pieces, and how the reset changes your run planning."
) + """{{< callout type="verdict" title="The Short Answer" >}}
As of 1.5.1, a Stalemate resets the Graveyard. Before, your list of lost pieces survived a Stalemate; now it is cleared. If you play PAWN difficulty and lean on recovery, this means your buyback list reflects only recent losses, not your whole run. Plan recoveries around Stalemate events instead of assuming old losses stay available.
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

## Community Resources

- [Official Gambonanza Steam News (1.5.1 hotfix)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Stalemate](https://gambonanza.fandom.com/wiki/Stalemate){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.1 (released September 2026). The Stalemate reset of the Graveyard is confirmed in the official 1.5.1 Steam news post.*
"""

ARTICLES["post-15-new-player-guide.md"] = fm(
    ["Beginner"], ["Beginner", "Strategy & Guides"],
    "New to Gambonanza After 1.5? What Changed for Beginners",
    "New to Gambonanza after v1.5.0? Here is what matters for beginners: the readability revamp, clearer enemy power warnings, Steam Deck Verified status, and how to start without drowning in systems."
) + """{{< callout type="verdict" title="If You Are Starting Now" >}}
Start on PAWN. Turn on skip animations, and turn on algebraic notation if you read chess. The 1.5.0 patch made the game far easier to read, and it added clearer warnings before enemy powers trigger, so you will lose fewer pieces to abilities you never saw coming. Ignore the balance history for now. You do not need it to win your first runs.
{{< /callout >}}

{{< diagram src="post15-beginner-path.svg" alt="Beginner learning path after v1.5" caption="A simple four-step start: pick PAWN, tune settings, learn enemy powers, then climb." >}}

## Why 1.5 Is a Good Time to Start

Gambonanza has been patched steadily since launch, and v1.5.0 is the friendliest build for a newcomer yet. The two changes that matter most for beginners are not balance tweaks. They are readability and feedback.

The readability revamp makes the board and the interface legible, which lowers the barrier to simply understanding what is happening. The enemy power feedback means the game warns you before an ability fires, so your early losses are more likely to be your mistakes and less likely to be surprises. Both changes reduce the frustration that drives new players away.

Add the hotfix line on top and you also get small quality-of-life wins: the hover-info fix (descriptions show in front of menus now), smoother Gambit collection browsing, and controller navigation fixes.

## Start on PAWN and Use the Graveyard

PAWN difficulty is the learning tier, and it is the only tier with the Graveyard. The Graveyard holds your last five lost pieces and lets you spend gold to buy them back. That means a single bad turn does not erase your run. You get to see whether your build works at scale before the game starts punishing you for every mistake.

Two rules to remember:

- Use the Graveyard for key pieces, not every pawn.
- As of 1.5.1, a Stalemate resets the Graveyard, so buy back what matters before a Stalemate clears the list.

Our [Graveyard system guide](/graveyard-system-guide/) has the full math.

## Settings Worth Changing on Day One

The Extra settings category is where the beginner-friendly toggles live. Two of them directly help you learn:

- **Skip animations.** Cutting the Gachapon and Piece Wheel animations shortens the loop between decisions, so you spend more time playing.
- **Algebraic notation.** If you read chess coordinates, this labels columns and rows next to tiles and makes positions unambiguous.

A third toggle, **Unlock All**, is useful as a sandbox if you want to experiment with Gambits outside a real run. It is optional.

For a graphical walkthrough of these, see our [UI and text readability guide](/ui-text-readability-guide/).

## Learn Enemy Powers Early

The 1.5.0 change that adds clearer warnings before enemy powers trigger is a gift to new players, but only if you use it. The warning is short, and it helps most when you already know roughly what the power does.

A good beginner habit: play a few low-stakes games purely to watch enemy powers fire. Do not try to win. Just note what the warning looks like and which piece it threatened. Our [enemy powers guide](/enemy-powers-warning-guide/) explains how to react once the warning appears.

## Your First Ten Hours, in Order

Follow this and your early experience will be far smoother:

1. **Start on PAWN.** Keep the Graveyard available while you learn.
2. **Tune settings.** Skip animations on. Algebraic notation on if you read it.
3. **Learn enemy powers.** Play a couple of games just to observe warnings.
4. **Climb slowly.** Move to KNIGHT only when PAWN feels easy. Expect the Graveyard to vanish and the enemy to move first.
5. **Ignore the balance history.** The Gambit buffs and nerfs from earlier patches matter for optimization, not survival.

## What You Can Safely Ignore for Now

The 1.5.x line mostly changed presentation and rules, not Gambit numbers. The 1.5.0 patch changed no Gambit math. The hotfixes changed a few reset rules (Stalemate and the Graveyard, Barter, Key of Life) that you will not bump into during your first runs. Save those for later and focus on learning the board.

## FAQ for New Players

- **Is the game still changing a lot?** Yes. The developer patches frequently, so check the [1.5.0 patch breakdown](/v150-patch-breakdown/) when you are ready to go deeper.
- **Do I need chess experience?** No. The game is explicit that it is not a chess simulator. Chess helps, but it is not required.
- **Should I play on Steam Deck?** Yes if you want to. Gambonanza is Steam Deck Verified, and the 1.5 revamp made handheld play much more readable.
- **Will I lose runs?** Constantly. That is the genre. The Graveyard on PAWN is there to soften the worst of it.

## Community Resources

- [Official Gambonanza Steam News](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza Wiki - Gambits](https://gambonanza.fandom.com/wiki/Gambits){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (released August to September 2026). Beginner-relevant changes verified against the official 1.5.0 and 1.5.1 Steam news posts.*
"""

ARTICLES["ui-text-readability-guide.md"] = fm(
    ["Strategy & Guides"], ["Game Mechanics", "Tips"],
    "Gambonanza UI & Text Readability After 1.5: Read the Board Faster",
    "Gambonanza v1.5.0 revamped the UI to make text easier to read, mainly for Steam Deck. Here is what changed, which settings to combine with it, and why readability is an actual skill edge."
) + """{{< callout type="verdict" title="The Short Answer" >}}
The v1.5.0 UI revamp makes text easier to read, with the biggest impact on Steam Deck. Combined with the algebraic notation toggle and the 1.5.3 hover-info fix, the board and its tooltips are now legible on small screens. Readability is not cosmetic in a game this dense. Clearer text means faster decisions and fewer mistakes.
{{< /callout >}}

{{< diagram src="ui-readability-compare.svg" alt="UI readability before and after v1.5" caption="Before 1.5 text was harder to scan on handhelds. After 1.5 the revamp sharpens it." >}}

## Why Readability Is a Real Advantage

Gambonanza throws a lot at you at once. A small board, a Gambit sidebar, a Shop, and a HUD all compete for attention. Every time you have to squint or re-read a tooltip, you lose tempo. In a turn-based roguelike, tempo is everything: the player who reads the board faster makes more moves in the same amount of thinking time, and makes fewer misreads.

That is why the 1.5.0 UI revamp is more than a coat of paint. The developer explicitly notes it makes text easier to read, and that it mainly affects Steam Deck. On a handheld, where the screen is small and your eyes sit close to it, legible text is the difference between a smooth run and a frustrating one.

## What the Revamp Changed

The developer's notes describe a UI revamp focused on text readability. The practical effect is that labels, descriptions, and menu text are clearer than in earlier builds. On desktop the change is subtle; on Steam Deck it is significant.

The change also pairs with earlier platform fixes:

- **Letterboxing fix (1.5.1).** Black bars on some Linux devices were removed, so the board uses the full screen.
- **Cursor visibility fix (1.5.2b).** An invisible cursor on some Linux setups was fixed, so any pointer-based navigation works.
- **Hover info fix (1.5.3).** Pressing Pause or Info while hovering a piece or Gambit now shows the description in front of the menu instead of behind it.

Together, these remove the four biggest readability annoyances on handhelds: small text, wasted screen space, a missing cursor, and hidden tooltips.

## Settings to Combine With the Revamp

The revamp is the baseline. Three settings finish the job:

- **Algebraic notation.** Adds column and row labels next to tiles. If you read chess coordinates, this makes positions unambiguous and lets you refer to squares precisely.
- **Skip animations.** Cuts Gachapon and Piece Wheel transitions. Less animation means less visual noise and a shorter loop between decisions.
- **Enhanced AI Mode (optional).** On PAWN or practice runs, this changes enemy behavior to conventional chess. It is a separate axis from readability, but a calmer opponent is easier to read.

Our [Steam Deck settings guide](/steam-deck-settings-guide/) walks through these in a handheld context.

## A Practical Example

Imagine you are on Steam Deck, mid-run, and you need to check whether a Gambit in your sidebar triggers on capture or on promotion. Before 1.5, you would hover, squint at a small tooltip, and maybe misread it. After the revamp and the hover-info fix, the text is clear and the description appears in front of the menu, so the read is fast and correct.

That single interaction, repeated dozens of times per run, is where the revamp pays off. It is not one dramatic improvement. It is many small ones.

## Readability Habits That Help

- **Scan the board before the sidebar.** Use the clearer text to identify the board state first, then check Gambits that apply.
- **Use coordinates when precision matters.** With algebraic notation on, refer to squares by name in your head. It reduces ambiguity when planning multi-move sequences.
- **Keep animations off.** Visual noise is the enemy of fast reading.
- **Read Gambit text between runs.** The collection tab was optimized in 1.5.3. Use downtime to learn names and effects so in-run reads are recognition, not study.

## Change Reference

| Change | Version | Effect on Readability |
|--------|---------|----------------------|
| UI and text revamp | 1.5.0 | Clearer labels and descriptions |
| Letterboxing fix | 1.5.1 | Full-screen board, no wasted space |
| Cursor visibility fix | 1.5.2b | Pointer usable on Linux |
| Hover info fix | 1.5.3 | Tooltips show in front of menus |
| Collection tab optimization | 1.5.3 | Smoother Gambit browsing |

## What This Means for Your Builds

1. **Readability is a skill edge.** Faster reading means faster, more correct decisions.
2. **Steam Deck is now viable for serious play.** The revamp plus Verified status removes the information disadvantage.
3. **Combine the toggles.** Revamp plus algebraic notation plus skip animations is the full package.
4. **No strategy changed.** This is presentation, not balance. Your builds are unaffected.

## Community Resources

- [Official Gambonanza Steam News (1.5.0 announcement)](https://store.steampowered.com/news/app/3509230/){target="_blank" rel="noopener noreferrer"}
- [Gambonanza on Steam](https://store.steampowered.com/app/3509230/){target="_blank" rel="noopener noreferrer"}

---

*Guide updated for Gambonanza v1.5.x (released August to September 2026). The UI revamp and related UI fixes are confirmed in the official 1.5.0, 1.5.1, 1.5.2b, and 1.5.3 Steam news posts.*
"""

# write files
os.makedirs(OUT, exist_ok=True)
for name, content in ARTICLES.items():
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")

# validation: banned chars & BOM
BANNED = {"\u2014": "em-dash", "\u2013": "en-dash", "\u2018": "curly-lq", "\u2019": "curly-rq",
          "\u201c": "curly-ldq", "\u201d": "curly-rdq", "\u2026": "ellipsis"}
print("\n--- validation ---")
bad = 0
for name in ARTICLES:
    path = os.path.join(OUT, name)
    raw = open(path, "rb").read()
    if raw[:3] == b"\xef\xbb\xbf":
        print("BOM in", name); bad += 1
    txt = raw.decode("utf-8")
    for ch, label in BANNED.items():
        if ch in txt:
            print("BANNED", label, "in", name); bad += 1
    # word count (rough)
    wc = len(txt.split())
    print("%-45s ~%d words" % (name, wc))
print("issues:", bad)
