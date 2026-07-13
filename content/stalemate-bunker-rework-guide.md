---
category: "Strategy & Guides"
title: "Stalemate & Bunker's Gambit Rework - How v1.3.0 Changed Two Core Systems"
description: "Gambonanza v1.3.0 revamped Stalemate to reset after boss fights and reworked Bunker's Gambit to be global. What these changes mean for your playstyle. Updated for v1.3.0."
game_version: ">=v1.3.0"
last_reviewed: "2026-07-13"
review_status: "current"
date: "2026-07-13"
hidden: true
publishDate: "2026-07-19"
---

{{< callout type="verdict" title="Two Core Systems Changed" >}}
v1.3.0 made two significant system-level changes that don't get enough attention: Stalemate now resets after every boss fight, and Bunker's Gambit works globally (not just Crumble Mode). These changes affect **every run**, regardless of build.
{{< /callout >}}

## Stalemate Revamp

{{< diagram src="stalemate-reset-flow.svg" alt="Before and after comparison of Stalemate counter behavior" caption="Left: Before v1.3, counter carries over stages. Right: After v1.3, boss win = full reset." >}}

### What Changed

**Old behavior:** The Stalemate counter accumulated across all stages. Even after winning a boss fight, the count carried over.

**New behavior:** The Stalemate counter resets to 0 after each boss victory.

### What This Means

Before v1.3.0, if you played conservatively and built up a 5+ move Stalemate count by the boss, you'd start the next stage already at risk. This forced you into aggressive play after every boss, even when you wanted to rebuild.

Now you get a **clean slate**. This has three practical effects:

1. **More rebuild time** -- After a tough boss fight, you can take 1-2 safe turns to rebuild without Stalemate pressure
2. **Different risk calculus** -- You can play defensive in Stage 1, aggressive in Stage 2, and never worry about carry-over
3. **BOSS fights are natural resets** -- Push hard at the end of each stage, knowing the counter resets

{{< callout type="tip" >}}
Use the post-boss period to **rebuild your Stock**. The boss fight probably depleted your reserves. The Stalemate reset gives you breathing room. See our [Post-Boss Economy Guide](/post-boss-economy-restart/) for the exact rebuild sequence.
{{< /callout >}}

### Strategy Changes

| Scenario | Before v1.3 | After v1.3 |
|----------|-------------|------------|
| After Stage 1 boss | Counter at 3-4 from boss fight, carry over | Counter resets to 0 |
| Farming in Stage 2 | Rushed, limited turns | Can farm 2-3 extra turns safely |
| Post-boss rebuild | Must capture immediately | Can position first, capture second |
| True Final Boss | High counter from previous stages | Clean slate, only Stage 5 matters |

## Bunker's Gambit Rework

{{< diagram src="bunker-comparison.svg" alt="Bunker's Gambit old vs new value comparison" caption="Left: Old Bunker's ($0 in stages 1-3, $3 only in Crumble). Right: New Bunker's ($1 every PROTECT, all stages)." >}}

### What Changed

**Old:** PROTECTING a piece during Crumble Mode gives +$3.
**New:** PROTECTING a piece gives +$1 (in any mode).

### Why This Is a Buff

On paper, $3 to $1 looks like a nerf. In practice:

- **Stages 1-3**: Old Bunker's did NOTHING (Crumble Mode isn't active). New Bunker's pays $1 each trigger. That's infinite improvement over $0.
- **Stage 4+ (Crumble)**: Old Bunker's paid $3 per PROTECT, but only 1-2 PROTECTs per Crumble trigger = $3-6. New Bunker's pays $1 per PROTECT, with 4-5 PROTECTs per turn = $4-5. Approximately equal.
- **Total per run**: Significantly more because Bunker's now activates 50+ times across all stages instead of 10-15 times during Crumble.

### How to Use It

Bunker's is now an **early pick** Gambit. Since it works from turn 1, grab it whenever it appears:

1. **Stage 1**: PROTECT your starting PAWN. Get +$1 immediately.
2. **Stage 2**: Start building PROTECT chains. Each PROTECT action stacks +$1.
3. **Stage 3+**: PROTECT high-value pieces. Every PROTECT = income.

Combine with:
- **Protect-intensive builds** -- Shield builds, Tower builds. Every PROTECT action becomes a $1 machine.
- **Boss Tooth's Gambit** -- triggers more reliably post-boss since v1.2 fix
- **[Crumble Mode Guide](/crumble-mode-guide/)** -- still the best reference for Crumble fundamentals

## Summary

| Change | Old | New | Verdict |
|--------|-----|-----|---------|
| Stalemate reset | Never | After boss wins | Big QoL improvement |
| Bunker's Gamit | Crumble only, $3 | Global, $1 | Net buff (more total $) |
| Both combined | Tight, aggressive meta | More breathing room | Healthy change |

## Community Resources

- [Official v1.3.0 Patch Notes (Steam)](https://store.steampowered.com/news/app/3509230/view/689761349249532405)
- [Bunker's Gambit Wiki](https://gambonanza.fandom.com/wiki/Bunker%27s_Gambit)

---

*Guide updated for Gambonanza v1.3.0. Both Stalemate revamp and Bunker's rework are v1.3.0 changes (June 25, 2026).*
