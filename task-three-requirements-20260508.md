# 任务记录 — 2026-05-08 01:48

## 三项核心需求

### 1️⃣ Steam 链接跳转 ✅
所有 Steam 链接现在统一指向 `https://store.steampowered.com/app/3182810/Gambonanza/`
- 首页 Header: `btn-steam` 按钮 ✓
- 所有子页面 Sidebar: `Buy on Steam` 醒目按钮 ✓
- Footer: Steam Page + Buy on Steam 两个链接 ✓
- Baseof 模板：所有 Steam 链接使用 `{{ .Site.Params.steam_url }}` 统一管理 ✓

### 2️⃣ 广告位布局 ✅
所有子页面现在都包含广告位置（在 single.html 模板中统一添加）：
- **内容前广告位** `margin-bottom:24px`
- **内容后广告位** `margin-top:32px`
- 首页保持原有 2 个广告位不变
- 广告位使用统一的 `.ad-slot` / `.ad-placeholder` / `.ad-label` CSS 样式
- 占位符文本 `📊 Google AdSense — Responsive Ad Unit`（替换为真实 AdSense ID 即可上线）

### 3️⃣ 多国语言切换 ✅
根据搜索确认，Gambonanza 支持：English, 中文(简体), 日文, 其他

**选出的 TOP 3 语言（按用户量估算）：**
| 排名 | 语言 | 地区 | 原因 |
|------|------|------|------|
| 1 | English 🇺🇸 | US/UK | 最大 Steam 市场，独立游戏主力 |
| 2 | 中文 🇨🇳 | China | 多家中型网站报道，策略类热门 |
| 3 | 日本語 🇯🇵 | Japan | 官方支持，象棋文化受众 |

**实现方式：**
- 页面顶部：语言切换条（lang-bar），在 Hero 上方
- 当前语言金色边框标识（current-lang）
- 点击国旗 → Google Translate 自动翻译整页
- Sidebar 也有语言切换器
- `hreflang` SEO 标签（en/zh-CN/ja/x-default）写入 `<head>`

### 部署
- main 分支 commit: `f513a4d`
- gh-pages 推送成功
- 网址：https://leolifan007.github.io/gambonanza-guide/

## 遗留事项
- [ ] AdSense 占位符需替换为真实 AdSense client ID
- [ ] 语言切换使用 Google Translate 外链，属于轻量方案；如需深度本地化需创建独立语言版本
- [ ] Google Search Console 验证未配置
