# 任务记录 — 2026-05-08 01:24

## 任务
1. FAQ 和 Beginner 页面排版品质升级 → 达到 Gambits/Bosses/Economy 同级
2. 首页加 KV 背景大图，参考用户提供的两张图（带文字版做排版参考、不带文字版做底图）

## 完成的工作

### FAQ 重写（4166 → 10960 字节）
添加了以下组件：
- `callout-verdict` 核心提示框（开头 + 关键位置）
- `callout-danger` 警示框（"The Broke Player Profile"、"The Rarity Trap"）
- `callout-tip` 技巧框
- `meta-badge` meta-s/a/b 评级标签（多处使用）
- `meta-rating` 评级行
- `synergy-table` 表格 ×6（Board Sizes、Gambit Count、Balatro vs Gambonanza 对比、Hours to Beat 等）
- `pro-tip` ×3（4×4 刷钱、Gambit 密度、Boss Gambit 顺序）
- `split-col` 双栏布局 ×3（Boss 问题、Boss-specific Gambits、底部导航）
- `phase-tag` 阶段标签

### Beginner 重写（9115 → 13140 字节）
- `callout-verdict` ×3（开头金句、黄金法则、Boss 预警）
- `callout-synergy` 协同提示框（Promotion）
- `callout-tip` ×2（学习目标、Pawn Rush 原理）
- `callout-danger` ×2（Trap Picks、5 大死因）
- `meta-badge` ×7（A/S-tier、Beginner Gambit 表格内 S/A/B）
- `meta-rating` ×3（Knights、Final Advice）
- `synergy-table` ×4（Crash Course、Knight Strategy、Pawn Rush、Beginner Gambits）
- `pro-tip` ×3（象棋玩家反直觉、AI 进攻算法、Stock Hoarding 心理学）
- `split-col` ×2（Promotion DO/DON'T、Boss Prep DO/AVOID）
- `phase-tag` 阶段标签

### 首页 KV 背景
- 用户提供两张 1672×941 像素风格大图
- 参考带文字版 → 首页标题改为大字 **GAMBONANZA**（5rem VT323，gold 色，text-shadow 发光）
- 底图换成无文字版 → WebP 81KB，CSS background url 引用
- 新增 `.hero-kv` CSS 类（720 行 CSS +46 行）
  - `background: linear-gradient overlay + url(hero-bg.webp) center/cover`
  - `h1 font-size: 5rem` 桌面端 / 3rem 平板 / 2.2rem 手机
  - `text-shadow` 发光效果
  - 响应式三断点
- 首页 Hero 添加 `hero-kv` class

### 部署
- main 分支 commit（4b1f339）
- gh-pages 分支推送（f4c1686, 57 files, +780/-3396）
- 网址：https://leolifan007.github.io/gambonanza-guide/

## 关键教训
- **视觉品质一致性**：所有内容页必须统一使用 callout/meta-badge/synergy-table/pro-tip/split-col 组件体系
- **KV 策略**：首页 Hero 用像素风格大图做背景 + 大字标题 + 发光效果 = 视觉冲击力
- **GitHub Pages** 中国可能有域名解析问题，web_fetch 和 browser 不可用

## 待验证
- [ ] 用户刷新页面后确认 KV 背景正常显示
- [ ] FAQ/Beginner 排版是否达到预期效果
- [ ] 手机端 Hero 文字和背景图适配
