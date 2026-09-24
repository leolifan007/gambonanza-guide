#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrich the 10 v1.5.x articles: add pro-tip, section-divider, second callout,
phase-tag, and internal links so each hits SOP visual-component density.
Idempotent-safe: checks markers before inserting.
"""
import os

CONTENT = "content"

# per-article enrichment data
DATA = {
"v150-patch-breakdown.md": dict(
    tip_title="What to Verify First",
    tip_body="Update your client, then open Settings and confirm the Extra toggles are present. If they are missing, you are not on 1.5.x yet. The enemy power warning only appears on the current build.",
    protip="The enemy power warning is a reaction cue, not a pause button. Decide your response before it appears, and you will save more pieces than any defensive Gambit.",
    links=[("/steam-deck-settings-guide/", "Steam Deck settings guide"), ("/enemy-powers-warning-guide/", "enemy powers guide")],
    phase="mid"),
"v151-153-hotfix-breakdown.md": dict(
    tip_title="Read the Resets Together",
    tip_body="Three reset rules changed in a single hotfix. Read Barter, Key of Life, and the Graveyard as one system, not three isolated notes, because they interact inside the same run.",
    protip="Hotfix lines are where reset rules quietly change. A rule that reads like a footnote can move your whole economy build, so always scan the small patches.",
    links=[("/barter-gambit-guide/", "Barter's Gambit guide"), ("/graveyard-stalemate-reset-guide/", "Graveyard reset guide")],
    phase="mid"),
"steam-deck-settings-guide.md": dict(
    tip_title="Two Minutes Saves Runs",
    tip_body="Do not start a serious climb on default settings. Confirm full-screen display, turn on skip animations, and test the Strains menu before your first real game on the Deck.",
    protip="Trackpad hovering is the fastest way to read a Gambit tooltip on the Deck. It is more precise than the stick and the 1.5.3 fix made the text land in front of the menu.",
    links=[("/ui-text-readability-guide/", "UI readability guide"), ("/controller-gamepad-guide/", "controller guide")],
    phase="mid"),
"barter-gambit-guide.md": dict(
    tip_title="Never Trade a Load-Bearing Bishop",
    tip_body="Barter's reward is random, so the only thing you control is what you spend. If the Bishop anchors a diagonal your defense depends on, keep it and skip the trade.",
    protip="Treat a Barter use as a price tag on a random piece. If you would not pay that specific Bishop for an unknown reward, do not let the Gambit decide for you.",
    links=[("/graveyard-stalemate-reset-guide/", "Graveyard reset guide"), ("/strain-system-guide/", "Strain system guide")],
    phase="early"),
"enemy-powers-warning-guide.md": dict(
    tip_title="Learn Powers Between Runs",
    tip_body="The warning window is too short to learn anything new. Use Enhanced AI Mode or a PAWN game to study what each power does, so the warning becomes recognition rather than analysis.",
    protip="Pair the warning with a mental priority list of your protected pieces. When it fires, you check the list, not the whole board, and your response is instant.",
    links=[("/ui-text-readability-guide/", "UI readability guide"), ("/enhanced-ai-mode-guide/", "Enhanced AI Mode guide")],
    phase="mid"),
"controller-gamepad-guide.md": dict(
    tip_title="Read Modifiers Before You Climb",
    tip_body="A smooth Strains menu is only useful if you open it. Read your modifiers once per run and adjust your build before the first turn, because the menu lists exactly what higher tiers change.",
    protip="Browse the Gambit collection between runs, not during them. The optimized tab is a study tool, and recognition beats reading mid-combat.",
    links=[("/strain-system-guide/", "Strain system guide"), ("/steam-deck-settings-guide/", "Steam Deck settings guide")],
    phase="early"),
"strain-system-guide.md": dict(
    tip_title="The Graveyard Is Tier-Locked",
    tip_body="From KNIGHT upward the Graveyard is removed by the Strain system, so plan every run as if losses are permanent once you leave PAWN. The safety net does not follow you up the ladder.",
    protip="Open the Strains menu before every climb. It takes under a minute and prevents the most common mistake in the game: not knowing which rules the tier just changed.",
    links=[("/graveyard-system-guide/", "Graveyard system guide"), ("/difficulty-guide/", "difficulty guide")],
    phase="mid"),
"graveyard-stalemate-reset-guide.md": dict(
    tip_title="Treat the Reset as a Deadline",
    tip_body="As of 1.5.1 a Stalemate clears the Graveyard, so the window to buy back a key piece runs from the loss to the next Stalemate. Buy what matters before that window closes.",
    protip="Since the list can reset, spend on your single most important lost piece first. Scattered recovery was already punished by the escalating cost; now it is also time-limited.",
    links=[("/graveyard-system-guide/", "Graveyard system guide"), ("/stalemate-bunker-rework-guide/", "Stalemate rework guide")],
    phase="mid"),
"post-15-new-player-guide.md": dict(
    tip_title="Learn the Warning Before the Climb",
    tip_body="Play a couple of low-stakes games purely to watch enemy powers fire. The 1.5 warning is short, and it only helps once you recognize what is about to trigger.",
    protip="Start on PAWN and stay there until it feels easy. The Graveyard is the only safety net in the game, and it disappears the moment you climb past the learning tier.",
    links=[("/graveyard-system-guide/", "Graveyard system guide"), ("/v150-patch-breakdown/", "v1.5.0 patch breakdown")],
    phase="early"),
"ui-text-readability-guide.md": dict(
    tip_title="The Revamp Is the Baseline",
    tip_body="Use the clearer text to identify the board state first, then check the Gambits that apply. Readability is a workflow: scan the board, then the sidebar, in that order.",
    protip="Turn animations off and algebraic notation on. Together they remove visual noise and give every square a name, which is the fastest way to read a dense board.",
    links=[("/steam-deck-settings-guide/", "Steam Deck settings guide"), ("/enemy-powers-warning-guide/", "enemy powers guide")],
    phase="mid"),
}

for name, d in DATA.items():
    path = os.path.join(CONTENT, name)
    t = open(path, encoding="utf-8").read()

    # 1. second callout (tip) right after the first diagram line, if not already present
    if "section-divider" not in t:
        block = "{{< section-divider >}}\n\n"
    else:
        block = ""

    # 2. insert a "Go Deeper" section with internal links + pro-tip before Community Resources
    link_md = " and ".join("[%s](%s)" % (txt, url) for url, txt in d["links"])
    deeper = (
        "%s## Where To Go Next\n\n"
        "If you want to go deeper on the systems referenced here, read the %s. "
        "They cover the mechanics this patch touches in full detail.\n\n"
        "{{< pro-tip \"%s\" >}}\n\n"
        "## Community Resources\n" % (block, link_md, d["protip"])
    )
    if "## Where To Go Next" not in t:
        t = t.replace("## Community Resources\n", deeper, 1)

    # 3. add a tip callout after the first verdict callout block for extra density
    if d["tip_title"] not in t:
        callout = (
            "{{< callout type=\"tip\" title=\"%s\" >}}\n%s\n{{< /callout >}}\n\n"
            % (d["tip_title"], d["tip_body"])
        )
        # insert before the first "## " heading after the verdict callout
        marker = "{{< /callout >}}\n"
        idx = t.find(marker)
        if idx != -1:
            insert_at = idx + len(marker)
            t = t[:insert_at] + "\n" + callout + t[insert_at:]

    # 4. phase-tag near top (after front matter)
    if "phase-tag" not in t:
        parts = t.split("---", 2)
        parts[2] = "\n" + "{{< phase-tag \"%s\" >}}\n" % d["phase"] + parts[2]
        t = "---".join(parts)

    open(path, "w", encoding="utf-8", newline="\n").write(t)
    print("enriched", name)
print("done")
