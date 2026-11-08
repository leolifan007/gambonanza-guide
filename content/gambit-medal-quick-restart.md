---
categories: ["Difficulty & Progression"]
tags:
  - "Progression"
  - "Bug Fixes"
  - "Patch Updates"
title: "Quick Restart No Longer Wipes Gambit Medal Progress After 1.5.4b"
description: "Patch 1.5.4b fixed Gambit Medal progress resetting after Quick Restart. Here is why players confused a persistence bug with a progression rule, and how to check your progress survives a restart now."
date: "2026-11-08T13:41:00+08:00"
lastmod: "2026-11-08T13:47:00+08:00"
version: "v1.5.7"
game_version: ">=v1.5.7"
last_reviewed: "2026-11-08"
review_status: "current"
hidden: false
---

{{< phase-tag "mid" >}}

Losing progress is the one bug that changes how people play. If a restart looks like it wipes your medal, you stop restarting, and that is a much bigger cost than the medal itself.

{{< game-icon name="check" >}}**1.5.4b lists it under fixes, not changes.** Fixed an issue where Gambit Medal progress would reset after using Quick Restart. The progress was always supposed to stay.

{{< callout type="verdict" >}}<strong>THE ONE-SCREEN ANSWER</strong>

If you have been avoiding Quick Restart to protect medal progress, you can stop. The 1.5.4b fix restores the intended behaviour: a restart restarts the run, it does not roll back your medal. Verify once by restarting and reopening the medal view.{{< /callout >}}

{{< diagram src="gambit-medal-quick-restart.svg" alt="Quick Restart behaviour before and after patch 1.5.4b" caption="A persistence bug, not a progression rule: the run resets, the medal should not." >}}

The [difficulty guide](/difficulty-guide/) covers how the six tiers unlock after a first clear; this page is only about one progress bug and the habit it created.

## A Restart Is Supposed to Reset the Run, Not Your Account

Gambonanza separates what happens inside a run from what you carry out of it. A run is five groups of five games, with a boss checkpoint at the end of each group. Difficulty tiers unlock after your first clear, and the Collection tracks 200 entries across six categories. Those are progression systems. A Quick Restart is a convenience for the run you are in.

{{< game-icon name="help" >}}**The bug blurred that line.** When medal progress vanished after a restart, the reasonable inference was that the game treated the medal as run state. It did not; it was a persistence bug, and the developer fixed it in the 1.5.4b post alongside five other state issues.

That is why the [six-item 1.5.4b checklist](/v154b-fix-checklist/) groups this with Barter's 0 counter and Tooth's Gambit missing payout. Three different symptoms, one cause: state that should have been kept or initialised correctly was not.

- **Gambit Medal progress**: Yes / Looked wiped / Kept
- **Current board and pieces**: No / Reset / Reset
- **Shop and reroll state**: No / Reset / Reset
- **Difficulty tier unlocks**: Yes / Unaffected / Unaffected
- **Collection entries**: Yes / Unaffected / Unaffected

{{< section-divider >}}

## The Habit the Bug Created

Players who believed a restart cost them progress played on through bad openings. That is a real cost in a game where the opening is three random pieces on a 5x5 board drawn from your unlocked Collection. A bad start is exactly when a restart is most useful.

- **Restart on a dead opening again.** The [how to play page](/how-to-play/) explains the three-piece start and why some boards simply cannot support your Gambits.
- **Do not farm a workaround.** If an old note tells you to finish a losing run to protect medal progress, it was written during the bug window.
- **Keep actual progression separate.** Achievements, unlocks and Collection entries are described in the [Collection unlock guide](/collection-unlock-guide/) and the [achievements page](/achievements/); none of them were part of this fix.

{{< callout type="tip" >}}<strong>Why this matters more at higher difficulty</strong>

The six difficulty tiers stack negative modifiers after your first clear, so a poor opening hurts more the higher you climb. A restart you avoid because of a phantom progress cost turns into a lost run you did not need to take.{{< /callout >}}

The earlier [1.5.1 to 1.5.3 hotfix notes](/v151-153-hotfix-breakdown/) show the same pattern from the other direction: several of those fixes were about things resetting when they should, or not resetting when they should. Read the two posts together and 1.5.x looks like a consistency pass.

{{< diagram src="gambit-medal-quick-restart-detail.svg" alt="Run state versus account state at the Quick Restart boundary" caption="The run resets; medal progress does not." >}}

## Two-Minute Verification

{{< game-icon name="check" >}}**Do this once, then forget about it.** Note your current medal progress, use Quick Restart, reopen the medal view and compare. If the number is still there, the fix is live on your client.

While you are there, check the shop for Valhalla's Gambit at $8. That confirms 1.5.4b specifically, which is the patch that carried this fix. If it still shows $10, restart behaviour has not changed for you yet.

{{< pro-tip >}}<strong>Keep a version boundary in your notes</strong><br>Every workaround you adopt should have the patch version written next to it. When the next fix lands, you know exactly which habits to retire.{{< /pro-tip >}}

If progress still looks wrong after that check, the FAQ is the right next stop. A fix that did not land is a client or save issue, not a progression rule to build around.

## Community Verification & Resources

The Gambit Medal fix is quoted from the official 1.5.4b post. Run structure, difficulty tiers and Collection facts are from the shipped game; the verification steps are derived from the listed symptom.

{{< resourcegrid >}}
- [Official Gambonanza Steam News (1.5.4b, 30 Sep 2026)](https://store.steampowered.com/news/app/3509230/) - official patch source and community reference
- [SteamDB mirror of the 1.5.4b patch notes](https://steamdb.info/patchnotes/25623616/) - official patch source and community reference
{{< /resourcegrid >}}

*Last reviewed November 8, 2026 for Gambonanza v1.5.7.*
