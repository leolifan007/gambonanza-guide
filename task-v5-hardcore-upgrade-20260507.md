# Task: 全站内容硬核升级 v5 — 2026-05-07

## 目标
将 Gambonanza Guide 的 8 个内容页从"说明书风格"升级为"专业攻略编辑风格"。每个 Gambit/Boss/策略都必须包含 Meta Rating、Synergy Table、Early vs Late Game、Pro Tip。

## 完成内容

### CSS 新增组件（26个新类）
- `.meta-badge` S/A/B/C 四级彩色评级徽章（金/橙/青/玫红）
- `.synergy-table` 暗系数据表（金表头，hover 高亮）
- `.phase-tag` 阶段标签（early/mid/late 三种配色）
- `.pro-tip` 黑色提示框 + 金色 PRO TIP 标签
- `.boss-header` + 8 种 boss 色彩变体（rook/bishop/knight/queen/king/pawn/castle/grandmaster）
- `.split-col` 双栏布局（响应式：768px 以下堆叠）
- 全部追加 768px 断点响应式规则

### 8 页内容重写

| 页面 | 内容升级 |
|------|----------|
| **bosses.md** | 通用 Boss 技巧置顶（4 条规则，双栏）。8 个 Boss 各有彩色标头、Meta Rating、Synergy Table、阶段指示、Pro Tip（10h+ 独家技巧）。底部社区难度排名表 |
| **gambits.md** | S/A/B/C 四级评级。Teleport/Ultimate Counter/Heal Board 等 6 个深度解析（含 Synergy Table + Pro Tip）。B 级用双栏卡片展示。完整 Tier List 速查表 |
| **strategy.md** | 三大开局流派评级（Knight Aggro S / Pawn Wall A / Economy Rush B）。4 个 Gambit 组合（双栏）。Deck 容量数学。分阶段决策指南。Tilt 管理 |
| **economy.md** | 投资表 S/A/B 评级。Safe Haven 复合增长数学。3 阶段经济策略。Mini-game 期望值速查。Shop 优先级指南。0 库存恢复路径 |
| **achievements.md** | S/A/B/C 四级成就。King Killer 专属 Synergy Table。50 小时全成就路径。每个 S/A 级成就独立 Pro Tip |
| **cards.md** | S/A/B/C 卡片评级。Royal Gambit + Checkmate Engine 深度 Synergy Table。陷阱卡警告 |
| **faq.md** | 实战 FAQ。去说明书化 |
| **beginner.md** | 上轮已完成（三板斧：Verdict/Synergies/Broken Strategy/Avoid This） |

### 技术修复
- **hugo.toml** 添加 `markup.goldmark.renderer.unsafe = true` — 解决 HTML 标签不渲染问题（boss headers/pro-tip/meta-badge 全线可见）
- **CSS** 从 v4 升级至 v5，追加 100+ 行新组件样式

### 部署记录
- Main: 8 files changed, +1421 -889
- hugo.toml fix: +4 lines
- Gh-pages v5.1: 7 files changed, +633 -327, commit b76f43d
- 全部路径已 relativize

### 部署 URL
https://leolifan007.github.io/gambonanza-guide/
重点验证页：
- /bosses/ (8 个彩色 boss 标头)
- /gambits/ (S/A/B/C 评级表)
- /economy/ (Pro Tip + Synergy Table)
- /achievements/ (S-Tier Pro Tips)
