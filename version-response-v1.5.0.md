# 版本响应: v1.5.0 - v1.5.3 (2026-08-21 ~ 2026-09-17)

> 站点上一次版本响应停在 v1.4.0（2026-08-18）。Steam 现已发布 1.5.0、1.5.1、1.5.2b、1.5.3，
> 按 SOP 12 补齐内容。审计日期：2026-09-24。

## 变更摘要（来自官方 Steam News，appid 3509230）

### 1.5.0（8/21）
- UI revamp：文字更易读（主要影响 Steam Deck）。
- 敌人能力即将触发时新增更明显的反馈提示。
- 修复若干成就（Achievement）bug。
- 官方确认 Gambonanza **Steam Deck Verified**。
- 开发者参加 gamescom（Indie Arena Booth）。

### 1.5.1（9/4）
- Barter 交易类 Gambit 在 Graveyard 后现在会重置（商店重置）。
- Key of Life's Gambit 现在在 Stalemate 后重置。
- **Stalemate 现在会重置 Graveyard**。
- 修复部分 Linux 设备 Letterboxing（上下黑边）分辨率问题。

### 1.5.2b（9/11）
- 修复部分 Linux 设备光标不可见的问题。

### 1.5.3（9/17）
- 悬停 Piece/Gambit 时按 Pause 或 Info，说明文本现在显示在菜单前面（层级修复）。
- 修复 Steam Deck 与手柄在 Strains 菜单中的导航。
- 英文 Screen Shake 设置项拼写修正。
- 优化 Gambit 收藏（collection）标签页导航，更顺滑。
- "Enemy Modifiers" 标签更名为 "Enemies"（多语言同步）。

## 受影响文章清单

| 文章 | 受影响程度 | 处理 |
|------|-----------|------|
| content/_index.md（首页） | 高 | 版本号 v1.4.0 -> v1.5.0，描述 + update-banner 同步 |
| hugo.toml | 高 | [params] description 版本/日期同步 |
| 14-qol-settings-guide | 中 | 补充 1.5 UI revamp + 敌人能力反馈 + 版本标签 |
| graveyard-system-guide | 中 | 补充 1.5.1 "Stalemate 重置 Graveyard" + 版本标签 |
| v140-patch-breakdown | 低 | 加 version_note 指向上一个版本 |
| crumble-mode-guide | 低 | Stalemate 行为补充说明 |
| （未发现涉及 Enemy Modifiers / Barter / Strain 的旧文，均为新增） | - | - |

排重结论：全站现有 82 篇文章中，**无任何** 1.5.0+ 相关内容，无 Strain 系统、无 Barter's Gambit、无 Steam Deck/手柄专题、无敌人能力提示专题。

## 新文章清单（10 篇）

### Batch 1 - P0 核心（4 篇）
1. `v150-patch-breakdown` - "Gambonanza 1.5.0 Patch Breakdown: UI Revamp, Steam Deck Verified & Enemy Power Feedback"
2. `v151-153-hotfix-breakdown` - "Gambonanza 1.5.1 to 1.5.3 Patch Notes Explained: Stalemate Resets the Graveyard"
3. `steam-deck-settings-guide` - "Gambonanza on Steam Deck: Best Settings for Text, Cursor & Controller"
4. `barter-gambit-guide` - "Barter's Gambit Guide: Shop Reset Cycles & Graveyard Interaction"

### Batch 2 - P1 支撑（6 篇）
5. `enemy-powers-warning-guide` - "Reading Enemy Powers in Gambonanza: The New Trigger Warnings Explained"
6. `controller-gamepad-guide` - "Gambonanza Controller & Gamepad Guide: Strains, Gambit Collection & Deck Navigation"
7. `strain-system-guide` - "Gambonanza Strain System Guide: Every Difficulty Modifier & When the Graveyard Disappears"
8. `graveyard-stalemate-reset-guide` - "Stalemate Resets the Graveyard (v1.5.1): What Changed and Why It Matters"
9. `post-15-new-player-guide` - "New to Gambonanza After 1.5? What Changed for Beginners"
10. `ui-text-readability-guide` - "Gambonanza UI & Text Readability After 1.5: Read the Board Faster"

## 执行计划
- Phase 1: 撰写 10 篇新文章 + 配 SVG（本日）
- Phase 2: 同步首页/配置版本号 + 旧文版本标签
- Phase 3: Hugo 构建 + QA 自检 + 提交
