---
categories: ["Beginner"]
tags:
  - "Beginner"
title: "How to Play Gambonanza - Complete Rules and Getting Started Guide"
description: "Learn how to play Gambonanza. The real win condition, the 5x5 opening board with 3 pieces, Stock and Landing, Crumble, the Stalemate Counter, Gambits, Tiles, boss checkpoints, and the full run structure. Verified against patch 1.5.x."
lastmod: "2026-09-25T15:00:00+08:00"
version: "v1.5.0"
---

## How to Play Gambonanza - The Rules That Actually Matter

{{< callout type="verdict" >}}<strong>The Short Version</strong>

  Gambonanza is a chess roguelike. You start a run with **3 pieces on a 5x5 board**, capture **every enemy piece** to win each game, and between games you spend money in a shop to add pieces, Gambits, and tiles. A full run is **5 stages of 5 games**, and the last game of each stage is a boss. The [Beginner Guide](/beginner/) goes deeper on strategy, and the [Bosses Guide](/bosses/) lists every boss mechanic.{{< /callout >}}

I have restarted more runs than I want to admit, and almost every early loss came from carrying chess assumptions into this game. This page is the ruleset I wish I had read first. It is written for the current build, and everything here is checkable in-game on the rules and shop screens.

## The Goal Is Capture, Not Checkmate

This is the single most important fact in Gambonanza, and the one chess players get wrong first.

<div class="synergy-table" style="overflow-x:auto">

| You Might Expect | Gambonanza Reality |
|------------------|--------------------|
| Trap the King and deliver checkmate | Capture **all** enemy pieces instead |
| The King is special | The enemy King is just another piece |
| Draws and stalemates are neutral | Stalemate ends the game on a counter, not a negotiation |
| Protect your King above all | Protect your **count of pieces**, you lose when you have none left |

</div>

You win a game by removing every enemy piece from the board. You lose when all of **your** pieces are gone. There is no check, no mate, no fifty-move draw rule. If you find yourself setting up a mating net while enemy pieces sit safe in a corner, you are losing.

{{< pro-tip >}}Count enemy pieces constantly. That number is the scoreboard. If it is not dropping, you are not winning no matter how good your position looks.{{< /pro-tip >}}

## The Board and How It Grows

A run begins on a **5x5 board**, you get **3 pieces** drawn from the pool you have unlocked in your Collection, and the board grows as you progress.

<div class="synergy-table" style="overflow-x:auto">

| Stage Element | What Happens |
|---------------|--------------|
| Starting board | 5x5 |
| Starting pieces | 3, drawn from your unlocked Collection pool |
| Board growth | Gain a row after clearing a boss checkpoint |
| Staging phase | Before the game begins you see the enemy layout and place your own pieces |

</div>

The staging phase is free planning time and most new players click through it. You can see how the enemy pieces are arranged before the first turn, which means you can walk your pieces straight into positions where they capture instead of wandering. On a 5x5 board there is nowhere to hide anyway, so use the information.

Because the board grows only after bosses, a large slice of your run is played on cramped geometry. Learn to fight in tight space and you will find later boards easy. The [Board Size Strategy Guide](/board-size-strategy/) covers how the geometry changes your options.

## Stock and Landing

Stock is your reserve of pieces waiting off the board.

<div class="synergy-table" style="overflow-x:auto">

| Term | Meaning |
|------|---------|
| Stock | Pieces held off the board, not currently in play |
| Landing | Deploying a Stock piece onto the board, costs one turn |
| Stock cap | You can hold up to 7 extra pieces in reserve |
| Landing upgrades | You can upgrade how many pieces you may land per turn |

</div>

Landing costs a full turn, so it is not free tempo. That matters because a turn spent deploying is a turn the enemy gets to act. On a small board, arriving one piece at a time is often correct; on a large board you will want the landing upgrades so you can flood the board faster.

{{< callout type="tip" >}}<strong>Stock Is Your Safety Net and Your Ammunition</strong>

  Pieces in Stock are pieces that cannot be captured, which makes Stock both a reserve of bodies and a way to protect pieces that would otherwise be exposed. Losing your board with an empty Stock is how runs end.{{< /callout >}}

{{< section-divider >}}

## Crumble - When the Board Starts Eating Itself

When one side is down to a single piece, the Crumble counter starts. After that, the board loses tiles each turn, and pieces standing on those tiles go with them.

<div class="synergy-table" style="overflow-x:auto">

| Crumble Stage | What Happens |
|---------------|--------------|
| Trigger | One side is reduced to a single piece |
| Ongoing effect | The board loses tiles each turn |
| Punishment | Anything on a lost tile is removed with it |
| Implication | Center tiles survive longer than edges |

</div>

Crumble is a timer, not a random disaster. It turns a stalemate into a countdown, and it punishes piece hoarding at the end of a game. If you ever find yourself at 1 piece against many, do not sit still: you have a limited number of turns before the floor disappears. The [Crumble Mechanic Guide](/crumble-mechanic-guide/) has the full breakdown of collapse order.

## The Stalemate Counter

If neither side is making progress, a Stalemate Counter accumulates. When it fills to 3 out of 3, the game ends.

<div class="synergy-table" style="overflow-x:auto">

| Counter State | Meaning |
|---------------|---------|
| 0 / 3 | Game is progressing normally |
| Filling to 3 / 3 | No progress is being made by either side |
| 3 / 3 | The game ends immediately |

</div>

The counter exists so you cannot farm a stalemate forever, and it interacts with Crumble to guarantee that every game terminates. Practically, it means shuffling pieces around without capturing is not a neutral act, it is burning a resource. When the counter starts moving, force captures.

{{< section-divider >}}

## Gambits - The Core of Your Build

Gambits are the rule-breaking powers that make this game a roguelike instead of chess. There are well over 200 of them, and **you can hold a maximum of 5 at once**, so every slot is a real decision.

<div class="synergy-table" style="overflow-x:auto">

| Gambit | Rarity | Cost | Effect |
|--------|--------|------|--------|
| Thunder's Gambit | Legendary | $9 | Capturing with a Pawn skips the enemy turn |
| Bug Catcher's Gambit | Common | $4 | Capturing with a Pawn pays +$2 |
| Race Flag's Gambit | Common | $4 | Promotion pays +$3 |
| Berserker's Gambit | Common | $6 | Your first capture of the game pays $1 |
| Squirrel's Gambit | Common | $6 | Every Pawn you gain pays $1 |
| Jump's Gambit | Rare | $8 | Pieces can hop over holes and empty squares |

</div>

Thunder's Gambit is the one I recommend to every new player. It is safe because it does not ask you to change how you play: you were going to capture with pawns anyway, and now doing so takes away the enemy's reply. The $9 price is real, so it is not a day-one purchase, but it is the cleanest power spike in the game for a beginner.

Do not build five random Gambits. Build three that pay you for actions you already take, and leave room to react to the boss you can see on the shop screen. The [Gambits Guide](/gambits/) rates them all, and the [Gambit Synergy Chains guide](/gambit-synergy-chains/) shows proven combinations.

{{< callout type="verdict" >}}<strong>Five Slots, Not Fifty</strong>

  Because you can only hold 5 Gambits, a tight, purposeful set beats a pile of expensive ones. Empty slots are not a failure state. Buying the wrong Gambit to "fill" a slot costs money and dilutes your build.{{< /callout >}}

## Tiles

Tiles are board modifications, and they are one of the most controllable systems in the game.

<div class="synergy-table" style="overflow-x:auto">

| Tile | Effect |
|------|--------|
| Gold Tile | The piece on it turns gold and carries money value |
| Protective Tile | Protects a piece for one turn, only on the turn it moves in |
| Trap Tile | An enemy that steps on it cannot move next turn |
| Phantom Tile | A piece moving in creates a temporary phantom copy |
| Blessed Tile | A captured blessed piece returns to Stock instead of dying |
| Crumbling Tile | The board breaks and tiles are lost |

</div>

The [Tile Control Guide](/tile-control-guide/) covers placement strategy. The short version: Protective and Trap tiles reward you for steering where fights happen, and Gold tiles are an income source, not just decoration.

## The Shop Between Games

After every game you get a shop visit.

<div class="synergy-table" style="overflow-x:auto">

| Shop Slot | Content |
|-----------|---------|
| Piece | One random piece you can add |
| Gambits | Three random Gambits |
| Tokens | Three random tokens |
| Reroll | $2 to refresh the offers |
| Boss preview | Bottom-left of the screen |

</div>

There are three token types, each with three price tiers. A **piece token** gives a random piece, a **gambit token** lets you pick a rarity and then choose from three options, and a **tile token** gives a random tile change that you place on a square of your choice.

The boss preview in the bottom-left is the most valuable free thing in the game. It shows the next boss mechanic before you spend a dollar, so you can buy the answer instead of guessing. I read it every single shop now, and my run consistency went up immediately.

You can also upgrade the "Max Piece on Board" cap, which raises how many of your pieces may stand on the board at once, and that upgrade gets more expensive each time. Buying it too early starves your Gambit budget. Buying it too late leaves pieces stranded in Stock. I buy it the moment I notice games ending with my Stock still full.

## Bosses

A run is **5 stages of 5 games**. The first four games of a stage are normal, and the fifth is a boss checkpoint, so a full run contains five boss fights.

<div class="synergy-table" style="overflow-x:auto">

| Boss | Mechanic You Have to Plan Around |
|------|----------------------------------|
| Hikarul the Banished | You cannot use Stock |
| Botezarro | Captures on squares matching its mask colour crumble that square |
| Jawby Fisher | Every time it is captured, it destroys a random Stock piece |
| Judit Polgeisha | You cannot see the enemy layout during staging |
| Kev Borclick | Applies STASIS to your pieces, stopping them from capturing |
| M3CH4GNU5 C4RL53N | Shuffles and hides your pieces during staging |
| Tal the Cursed | Places five cursed tiles that downgrade pieces to pawns |
| Mighty Kasparov | Appears as one of the five checkpoints |

</div>

Two things about bosses that took me time to internalise. First, **boss order is randomised**, so you cannot plan a fixed route. Second, each boss has a piece you can only capture last, so the fight has a defined closing move. Hikarul removing your Stock access is the one that ends new runs most often, so learn to play without Landing before you meet it. The [Bosses Guide](/bosses/) has the detail.

{{< section-divider >}}

## The Run Structure, Start to Finish

Here is the whole loop in order, so you know what you are committing to when you press start.

1. **Start the run.** A 5x5 board, 3 pieces from your unlocked pool.
2. **Staging phase.** See the enemy layout, place your pieces.
3. **Play the game.** Capture enemy pieces. Land pieces from Stock as needed. Watch the Stalemate Counter and, late in a game, the Crumble counter.
4. **Win or lose.** Capture all enemies to win. Lose all your pieces and the game is over.
5. **Shop.** Buy a piece, Gambits, or tokens. Check the boss preview. Reroll for $2 if you have a plan.
6. **Repeat for four normal games**, then the fifth is a boss.
7. **Clear the boss** to finish the stage, and gain a row on your board.
8. **Five stages in total.** Your run ends when you clear all five, or when a loss ends it.

Once you have completed a run, difficulty tiers unlock, and higher difficulty tiers add negative modifiers called Strains. The [Strain System Guide](/strain-system-guide/) explains what each tier changes, and the [Difficulty Guide](/difficulty-guide/) covers when to move up. Higher difficulty tiers also hide an extra boss beyond the five checkpoints.

## Your First Run - What to Actually Do

{{< callout type="tip" >}}<strong>First Run Checklist</strong>

  **Do** use the staging phase to line up your first capture. **Do** buy a cheap Common Gambit that pays on captures. **Do** read the boss preview. **Do not** go hunting for a mate that does not exist, just take every piece. **Do not** dump your money into capacity upgrades in the first two shops. **Do not** sit on a full Stalemate Counter waiting for a perfect move.{{< /callout >}}

If I were starting over, I would spend my first run doing nothing but counting enemy pieces, reading the boss preview, and testing how Landing feels. Winning a first run is nice but not the point. Understanding that capture is the goal and that money is a tool for buying capture power is the actual lesson.

## Where to Go Next

- [Beginner Guide](/beginner/) - the strategy layer on top of these rules
- [Gambits Guide](/gambits/) - every Gambit rated, plus which five to hold
- [Bosses Guide](/bosses/) - all boss mechanics and how to shop for them
- [Economy Guide](/economy/) - how to build money and where to spend it
- [Tips](/tips/) - the small habits that keep runs alive
- [Early Board Money Guide](/early-board-economy/) - how I farm Stock on the opening board
- [Board Size Strategy Guide](/board-size-strategy/) - how geometry changes your build
- [Tile Control Guide](/tile-control-guide/) - making tiles work for you

---

*Last reviewed: 2026-09-25 | Build: v1.5.0 | Based on my own runs and the in-game rules, shop, and Collection screens*
