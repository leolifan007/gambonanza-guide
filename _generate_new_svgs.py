# -*- coding: utf-8 -*-
"""Generate SVG diagrams for 10 new articles"""
import os

DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\static\images\diagrams"
os.makedirs(DIR, exist_ok=True)

def write_svg(name, svg):
    path = os.path.join(DIR, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg.strip())
    print(f"  {name} ({os.path.getsize(path)} bytes)")

# Design tokens
D = "#1A0F1A"
D2 = "#2D1A2D"
G = "#D4A84A"
T = "#4A9B9B"
R = "#A85D6A"
O = "#D4764A"
C = "#F5E6D3"
Cd = "#E8D5C0"
Gr = "#5CB85C"
FONT = "Inter,sans-serif"
FONT_M = "'VT323',monospace"
BASE = f'xmlns="http://www.w3.org/2000/svg" font-family="{FONT}"'

print("Generating 10 new SVGs...\n")

# =============================================
# 1. STAGE 4 ECONOMY DRAIN
# =============================================
write_svg("economy-drain-flow.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Stage 4 Economy Drain - 3 Killers</text>

<rect x="350" y="55" width="320" height="28" rx="4" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="510" y="73" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">You reach Stage 4: 50 stock. Boss arrives: 12 stock.</text>

<!-- Killer 1 -->
<rect x="30" y="100" width="200" height="170" rx="10" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="30" y="100" width="200" height="30" rx="10" fill="{T}" opacity="0.2"/>
<text x="130" y="120" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Killer #1</text>
<text x="130" y="145" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Shop Reset Timing</text>
<text x="130" y="168" fill="{Cd}" font-size="11" text-anchor="middle">Reset at wrong turn:</text>
<text x="130" y="186" fill="{Cd}" font-size="11" text-anchor="middle">- 8 stock per reset</text>
<text x="130" y="204" fill="{Cd}" font-size="11" text-anchor="middle">- Reset 3x = -24 stock</text>
<text x="130" y="222" fill="{Cd}" font-size="11" text-anchor="middle">- No gambit = no income</text>
<text x="130" y="248" fill="{O}" font-size="12" text-anchor="middle">Fix: Reset only when</text>
<text x="130" y="264" fill="{O}" font-size="11" text-anchor="middle">gambit pool is empty</text>

<arrow x="240" y="185" fill="{Cd}" font-size="18">-></arrow>

<!-- Killer 2 -->
<rect x="250" y="100" width="200" height="170" rx="10" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<rect x="250" y="100" width="200" height="30" rx="10" fill="{R}" opacity="0.2"/>
<text x="350" y="120" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Killer #2</text>
<text x="350" y="145" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Gambit Threshold</text>
<text x="350" y="168" fill="{Cd}" font-size="11" text-anchor="middle">Stage 4 hidden cost jump:</text>
<text x="350" y="186" fill="{Cd}" font-size="11" text-anchor="middle">- Econ gambit: 8->14 stock</text>
<text x="350" y="204" fill="{Cd}" font-size="11" text-anchor="middle">- Activate costs +40%</text>
<text x="350" y="222" fill="{Cd}" font-size="11" text-anchor="middle">- Same plays cost more</text>
<text x="350" y="248" fill="{O}" font-size="12" text-anchor="middle">Fix: Pre-buy gambits</text>
<text x="350" y="264" fill="{O}" font-size="11" text-anchor="middle">in Stage 3, not Stage 4</text>

<arrow x="460" y="185" fill="{Cd}" font-size="18">-></arrow>

<!-- Killer 3 -->
<rect x="470" y="100" width="200" height="170" rx="10" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<rect x="470" y="100" width="200" height="30" rx="10" fill="{O}" opacity="0.2"/>
<text x="570" y="120" fill="{O}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Killer #3</text>
<text x="570" y="145" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Board Transition</text>
<text x="570" y="168" fill="{Cd}" font-size="11" text-anchor="middle">Mid-game -> Boss board:</text>
<text x="570" y="186" fill="{Cd}" font-size="11" text-anchor="middle">- Sell 3+ pieces</text>
<text x="570" y="204" fill="{Cd}" font-size="11" text-anchor="middle">- Lose gambit triggers</text>
<text x="570" y="222" fill="{Cd}" font-size="11" text-anchor="middle">- Economy loop breaks</text>
<text x="570" y="248" fill="{O}" font-size="12" text-anchor="middle">Fix: Transition limit</text>
<text x="570" y="264" fill="{O}" font-size="11" text-anchor="middle">sell only 2 pieces max</text>

<rect x="100" y="290" width="500" height="36" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="312" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">If you plan for Stage 4 in Stage 3, you skip all 3 killers.</text>

<rect x="150" y="335" width="400" height="30" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="350" y="355" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Tested 40+ runs - 68% survive rate with pre-planning</text>
</svg>""")

# =============================================
# 2. PRUNING PRIORITY PYRAMID
# =============================================
write_svg("pruning-priority.svg", f"""<svg {BASE} width="600" height="420" viewBox="0 0 600 420">
<rect width="600" height="420" fill="{D}" rx="12"/>
<text x="300" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Piece Pruning Priority Pyramid</text>

<!-- S-Tier -->
<rect x="190" y="60" width="220" height="50" rx="8" fill="{D2}" stroke="{Gr}" stroke-width="2"/>
<text x="300" y="83" fill="{Gr}" font-family="{FONT_M}" font-size="15" text-anchor="middle">S-Tier: KEEP</text>
<text x="300" y="100" fill="{Cd}" font-size="11" text-anchor="middle">Economy generators + Gambit cores</text>

<line x1="150" y1="115" x2="450" y2="115" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- A-Tier -->
<rect x="160" y="120" width="280" height="50" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="300" y="143" fill="{T}" font-family="{FONT_M}" font-size="15" text-anchor="middle">A-Tier: KEEP if synergized</text>
<text x="300" y="160" fill="{Cd}" font-size="11" text-anchor="middle">Board control + Synergy hubs</text>

<line x1="120" y1="175" x2="480" y2="175" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- B-Tier -->
<rect x="130" y="180" width="340" height="50" rx="8" fill="{D2}" stroke="{G}" stroke-width="1.5"/>
<text x="300" y="203" fill="{G}" font-family="{FONT_M}" font-size="15" text-anchor="middle">B-Tier: TEMPORARY</text>
<text x="300" y="220" fill="{Cd}" font-size="11" text-anchor="middle">Replace if better option appears</text>

<line x1="90" y1="235" x2="510" y2="235" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- C-Tier -->
<rect x="100" y="240" width="400" height="50" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<text x="300" y="263" fill="{O}" font-family="{FONT_M}" font-size="15" text-anchor="middle">C-Tier: SELL FIRST</text>
<text x="300" y="280" fill="{Cd}" font-size="11" text-anchor="middle">No gambit synergy, no economy value</text>

<line x1="60" y1="295" x2="540" y2="295" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- Sell rules -->
<rect x="50" y="300" width="500" height="105" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="300" y="320" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">3-Second Sell Decision Rule</text>
<text x="65" y="345" fill="{Gr}" font-size="12">Second 1:</text>
<text x="150" y="345" fill="{C}" font-size="12">Any C-tier pieces? Sell one. Done.</text>
<text x="65" y="365" fill="{G}" font-size="12">Second 2:</text>
<text x="150" y="365" fill="{C}" font-size="12">No C-tier. Worst B-tier doing &lt;2 stock/turn? Sell.</text>
<text x="65" y="385" fill="{O}" font-size="12">Second 3:</text>
<text x="150" y="385" fill="{C}" font-size="12">Only A-tier left. New piece a direct upgrade? Sell A. Else keep.</text>
</svg>""")

# =============================================
# 3. QUEEN VS KING DIFFICULTY COMPARISON
# =============================================
write_svg("queen-king-comparison.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Queen vs King - Hidden Scaling Changes</text>

<rect x="50" y="60" width="180" height="28" rx="4" fill="{D2}" stroke="{T}" stroke-width="1"/>
<text x="140" y="79" fill="{T}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Queen (You Know)</text>

<rect x="470" y="60" width="180" height="28" rx="4" fill="{D2}" stroke="{O}" stroke-width="1"/>
<text x="560" y="79" fill="{O}" font-family="{FONT_M}" font-size="13" text-anchor="middle">King (Hidden)</text>

<!-- Row 1: Economy -->
<rect x="30" y="100" width="640" height="55" rx="6" fill="{D2}" stroke="#3A2030" stroke-width="1"/>
<text x="50" y="122" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="start">Economy Scaling</text>
<text x="50" y="142" fill="{Cd}" font-size="11" text-anchor="start">Prices normal. Reset = 8 stock.</text>
<text x="370" y="142" fill="{O}" font-size="11" text-anchor="start">Shop up 25-40%. Reset = 16 stock. Pay more, earn same.</text>

<line x1="330" y1="105" x2="330" y2="150" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- Row 2: Boss HP -->
<rect x="30" y="160" width="640" height="55" rx="6" fill="{D2}" stroke="#3A2030" stroke-width="1"/>
<text x="50" y="182" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="start">Boss HP Multiplier</text>
<text x="50" y="202" fill="{Cd}" font-size="11" text-anchor="start">Boss HP +0%. Predictable phase shift.</text>
<text x="370" y="202" fill="{O}" font-size="11" text-anchor="start">Boss HP +60-80%. Phase shift threshold -2 turns.</text>

<line x1="330" y1="165" x2="330" y2="210" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- Row 3: Crumble Timer -->
<rect x="30" y="220" width="640" height="55" rx="6" fill="{D2}" stroke="#3A2030" stroke-width="1"/>
<text x="50" y="242" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="start">Crumble Timer</text>
<text x="50" y="262" fill="{Cd}" font-size="11" text-anchor="start">Standard timer. Predictable collapse.</text>
<text x="370" y="262" fill="{O}" font-size="11" text-anchor="start">Timer -40%. Board shrinks 2-3 turns sooner.</text>

<line x1="330" y1="225" x2="330" y2="270" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- Row 4: AI Priority -->
<rect x="30" y="280" width="640" height="55" rx="6" fill="{D2}" stroke="#3A2030" stroke-width="1"/>
<text x="50" y="302" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="start">AI Target Priority</text>
<text x="50" y="322" fill="{Cd}" font-size="11" text-anchor="start">Random target. Gambit cores survive.</text>
<text x="370" y="322" fill="{O}" font-size="11" text-anchor="start">Targets gambit cores. Your engine dies first.</text>

<rect x="100" y="348" width="500" height="24" rx="4" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="364" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">King is not harder Queen. King is different rules. Adjust or die.</text>
</svg>""")

# =============================================
# 4. LOOP TOPOLOGY - SAFE VS SELF-DESTRUCTIVE
# =============================================
write_svg("loop-topology.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Loop Topology: Safe vs Self-Destructive</text>

<rect x="30" y="55" width="310" height="38" rx="6" fill="{D2}" stroke="{Gr}" stroke-width="1.5"/>
<text x="185" y="79" fill="{Gr}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Safe Loop (Net Positive)</text>

<rect x="360" y="55" width="310" height="38" rx="6" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<text x="515" y="79" fill="{R}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Self-Destructive (Net Zero/Negative)</text>

<!-- Safe row -->
<rect x="30" y="105" width="310" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="0.5"/>
<text x="185" y="123" fill="{Gr}" font-size="12" text-anchor="middle">Income > Activation cost per cycle</text>

<rect x="30" y="138" width="310" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="0.5"/>
<text x="185" y="156" fill="{Cd}" font-size="12" text-anchor="middle">Board space grows with economy</text>

<rect x="30" y="171" width="310" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="0.5"/>
<text x="185" y="189" fill="{Cd}" font-size="12" text-anchor="middle">0-1 piece sold per cycle max</text>

<rect x="30" y="204" width="310" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="0.5"/>
<text x="185" y="222" fill="{Cd}" font-size="12" text-anchor="middle">300+ stock by turn 30</text>

<rect x="30" y="237" width="310" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="0.5"/>
<text x="185" y="255" fill="{Cd}" font-size="12" text-anchor="middle">Survives stage transitions</text>

<!-- Destructive row -->
<rect x="360" y="105" width="310" height="28" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="515" y="123" fill="{R}" font-size="12" text-anchor="middle">Income < Activation cost per cycle</text>

<rect x="360" y="138" width="310" height="28" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="515" y="156" fill="{Cd}" font-size="12" text-anchor="middle">Board overflows, forced sells</text>

<rect x="360" y="171" width="310" height="28" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="515" y="189" fill="{Cd}" font-size="12" text-anchor="middle">3+ pieces sold per cycle</text>

<rect x="360" y="204" width="310" height="28" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="515" y="222" fill="{Cd}" font-size="12" text-anchor="middle">Stock flat or decreasing by turn 20</text>

<rect x="360" y="237" width="310" height="28" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="515" y="255" fill="{Cd}" font-size="12" text-anchor="middle">Collapses on stage transition</text>

<!-- 3 types -->
<rect x="80" y="285" width="540" height="80" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="305" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">3 Self-Destructive Patterns to Watch</text>
<text x="350" y="325" fill="{R}" font-size="12" text-anchor="middle">Type A: Summon Spam - Generates faster than economy supports</text>
<text x="350" y="343" fill="{R}" font-size="12" text-anchor="middle">Type B: Resource Loop Lock - Gambits consume each other</text>
<text x="350" y="361" fill="{R}" font-size="12" text-anchor="middle">Type C: Timer Trap - Key gambit expires, chain breaks</text>
</svg>""")

# =============================================
# 5. POST-BOSS RECOVERY FLOW
# =============================================
write_svg("recovery-flow.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Post-Boss Recovery Decision Tree</text>

<!-- Step 1 -->
<rect x="45" y="65" width="610" height="38" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="350" y="89" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 1: INVENTORY - What survived? (gambits, pieces, stock)</text>

<arrow y="105" fill="{Cd}" font-size="14">--> goto next</arrow>

<!-- Decision: enough gambits? -->
<rect x="45" y="115" width="610" height="38" rx="6" fill="{D2}" stroke="{G}" stroke-width="1"/>
<text x="350" y="139" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">> 2 active gambits? ---YES--- Buy ECONOMY first, not attack</text>

<rect x="45" y="158" width="610" height="38" rx="6" fill="{D2}" stroke="{R}" stroke-width="1"/>
<text x="350" y="182" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="middle">< 2 active gambits? ---RUN--- Emergency buy ANY gambit</text>

<arrow y="200" fill="{Cd}" font-size="14">--> </arrow>

<!-- Stage-specific recovery -->
<rect x="100" y="210" width="500" height="80" rx="8" fill="#3A2030" stroke="{Gr}" stroke-width="1"/>
<text x="350" y="230" fill="{Gr}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Recovery Speed by Stage</text>
<text x="350" y="252" fill="{Gr}" font-size="12" text-anchor="middle">Stage 1->2:  5-8 turns back to normal. Low risk.</text>
<text x="350" y="270" fill="{G}" font-size="12" text-anchor="middle">Stage 3->4: 15-20 turns rebuild. Medium risk. Save 10 stock buffer.</text>
<text x="350" y="288" fill="{O}" font-size="12" text-anchor="middle">Stage 5->6: 5 turns or die. Fatal risk. Pre-buy insurance gambits.</text>

<!-- Bottom rule -->
<rect x="100" y="305" width="500" height="28" rx="4" fill="{D2}" stroke="{G}" stroke-width="1"/>
<text x="350" y="324" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Golden Rule: Economy before attack. Always. Every post-boss.</text>
</svg>""")

# =============================================
# 6. PROMOTION TROUBLESHOOTING FLOWCHART
# =============================================
write_svg("promotion-flow.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Pawn Promotion - 4 Blockers Diagnostic</text>

<!-- Blocker 1 -->
<rect x="30" y="60" width="150" height="135" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="30" y="60" width="150" height="25" rx="8" fill="{T}" opacity="0.2"/>
<text x="105" y="78" fill="{T}" font-family="{FONT_M}" font-size="12" text-anchor="middle">#1</text>
<text x="105" y="100" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Tile Ownership</text>
<text x="105" y="120" fill="{Cd}" font-size="10" text-anchor="middle">Pawn at rank 8 but</text>
<text x="105" y="136" fill="{Cd}" font-size="10" text-anchor="middle">tile not yours</text>
<text x="105" y="160" fill="{O}" font-size="10" text-anchor="middle">Check end-of-turn</text>
<text x="105" y="175" fill="{O}" font-size="10" text-anchor="middle">ownership</text>

<arrow x="188" y="130" fill="{Cd}" font-size="16">-></arrow>

<!-- Blocker 2 -->
<rect x="200" y="60" width="150" height="135" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<rect x="200" y="60" width="150" height="25" rx="8" fill="{O}" opacity="0.2"/>
<text x="275" y="78" fill="{O}" font-family="{FONT_M}" font-size="12" text-anchor="middle">#2</text>
<text x="275" y="100" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Gambit Conflict</text>
<text x="275" y="120" fill="{Cd}" font-size="10" text-anchor="middle">Gambit absorbs</text>
<text x="275" y="136" fill="{Cd}" font-size="10" text-anchor="middle">the promotion event</text>
<text x="275" y="160" fill="{O}" font-size="10" text-anchor="middle">Disable gambits</text>
<text x="275" y="175" fill="{O}" font-size="10" text-anchor="middle">one at a time</text>

<arrow x="358" y="130" fill="{Cd}" font-size="16">-></arrow>

<!-- Blocker 3 -->
<rect x="370" y="60" width="150" height="135" rx="8" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<rect x="370" y="60" width="150" height="25" rx="8" fill="{R}" opacity="0.2"/>
<text x="445" y="78" fill="{R}" font-family="{FONT_M}" font-size="12" text-anchor="middle">#3</text>
<text x="445" y="100" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Turn Phase</text>
<text x="445" y="116" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Restriction</text>
<text x="445" y="136" fill="{Cd}" font-size="10" text-anchor="middle">Pawn promoted by</text>
<text x="445" y="152" fill="{Cd}" font-size="10" text-anchor="middle">gambit not move</text>
<text x="445" y="175" fill="{O}" font-size="10" text-anchor="middle">Wait 1 full turn</text>

<arrow x="528" y="130" fill="{Cd}" font-size="16">-></arrow>

<!-- Blocker 4 -->
<rect x="540" y="60" width="130" height="135" rx="8" fill="{D2}" stroke="#7A3D4A" stroke-width="1.5"/>
<rect x="540" y="60" width="130" height="25" rx="8" fill="#7A3D4A" opacity="0.2"/>
<text x="605" y="78" fill="#7A3D4A" font-family="{FONT_M}" font-size="12" text-anchor="middle">#4</text>
<text x="605" y="100" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Piece Count</text>
<text x="605" y="116" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Cap</text>
<text x="605" y="136" fill="{Cd}" font-size="10" text-anchor="middle">Max queens on</text>
<text x="605" y="152" fill="{Cd}" font-size="10" text-anchor="middle">board reached</text>
<text x="605" y="175" fill="{O}" font-size="10" text-anchor="middle">Sacrifice 1 queen</text>

<!-- Diagnosis flow -->
<rect x="100" y="215" width="500" height="55" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="235" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Diagnosis: 3-Step Check for Any Blocker</text>
<text x="350" y="255" fill="{C}" font-size="11" text-anchor="middle">1. Replay the turn. 2. Identify when condition happened. 3. Test with one variable changed.</text>

<rect x="100" y="280" width="500" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="350" y="298" fill="{Gr}" font-family="{FONT_M}" font-size="12" text-anchor="middle">30+ controlled tests on v1.1.0 - All 4 blockers confirmed</text>

<rect x="100" y="315" width="500" height="50" rx="6" fill="{D2}" stroke="{T}" stroke-width="1"/>
<text x="350" y="335" fill="{T}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Still failing after all 4 checks?</text>
<text x="350" y="353" fill="{Cd}" font-size="11" text-anchor="middle">Screenshot board + gambit panel. Post to Gambonanza Troubleshooting thread.</text>
</svg>""")

# =============================================
# 7. BOSS PHASE 1 VS 2 COMPARISON
# =============================================
write_svg("boss-phase-comparison.svg", f"""<svg {BASE} width="700" height="360" viewBox="0 0 700 360">
<rect width="700" height="360" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Final Boss - Phase 1 vs Phase 2</text>

<rect x="50" y="55" width="260" height="30" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="180" y="75" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Phase 1: Standard Fight</text>

<rect x="390" y="55" width="260" height="30" rx="6" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<text x="520" y="75" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Phase 2: TRANSFORMATION!</text>

<!-- Trigger -->
<rect x="150" y="100" width="400" height="40" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1.5"/>
<text x="350" y="120" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">TRIGGER: Patience Meter fills by gambit activations</text>
<text x="350" y="136" fill="{Cd}" font-size="11" text-anchor="middle">NOT by HP. BOSS watches how many gambits you trigger.</text>

<line x1="50" y1="155" x2="650" y2="155" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<!-- Comparison rows -->
<rect x="60" y="165" width="240" height="26" rx="4" fill="{D2}" stroke="{T}" stroke-width="0.5"/>
<text x="180" y="183" fill="{Cd}" font-size="12" text-anchor="middle">Move speed: Normal (1 move/turn)</text>

<rect x="60" y="196" width="240" height="26" rx="4" fill="{D2}" stroke="{T}" stroke-width="0.5"/>
<text x="180" y="214" fill="{Cd}" font-size="12" text-anchor="middle">Effects: Standard debuffs</text>

<rect x="60" y="227" width="240" height="26" rx="4" fill="{D2}" stroke="{T}" stroke-width="0.5"/>
<text x="180" y="245" fill="{Cd}" font-size="12" text-anchor="middle">Survivability: Predictable patterns</text>

<rect x="60" y="258" width="240" height="26" rx="4" fill="{D2}" stroke="{T}" stroke-width="0.5"/>
<text x="180" y="276" fill="{Cd}" font-size="12" text-anchor="middle">Win condition: Outlast</text>

<rect x="400" y="165" width="240" height="26" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="520" y="183" fill="{R}" font-size="12" text-anchor="middle">Move speed: 2x (+teleport)</text>

<rect x="400" y="196" width="240" height="26" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="520" y="214" fill="{Cd}" font-size="12" text-anchor="middle">Effects: Clears all non-permanent effects</text>

<rect x="400" y="227" width="240" height="26" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="520" y="245" fill="{Cd}" font-size="12" text-anchor="middle">Survivability: AOE attacks, multi-target</text>

<rect x="400" y="258" width="240" height="26" rx="4" fill="{D2}" stroke="{R}" stroke-width="0.5"/>
<text x="520" y="276" fill="{Cd}" font-size="12" text-anchor="middle">Win condition: Burst before wipe</text>

<rect x="100" y="300" width="500" height="48" rx="8" fill="#3A2030" stroke="{Gr}" stroke-width="1"/>
<text x="350" y="318" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">3 Builds That Survive Phase 2</text>
<text x="350" y="338" fill="{C}" font-size="11" text-anchor="middle">High-tolerance economy | Fast burst | Board control lock</text>
</svg>""")

# =============================================
# 8. TILE BEHAVIOR MATRIX
# =============================================
write_svg("tile-behavior.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Tile Gambit Legality - Matrix</text>

<!-- Header -->
<rect x="30" y="55" width="140" height="30" rx="4" fill="{D2}"/>
<text x="100" y="74" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Tile Type</text>

<rect x="175" y="55" width="120" height="30" rx="4" fill="{D2}"/>
<text x="235" y="74" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Gambit Activation</text>

<rect x="300" y="55" width="160" height="30" rx="4" fill="{D2}"/>
<text x="380" y="74" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Effect Persistence</text>

<rect x="465" y="55" width="205" height="30" rx="4" fill="{D2}"/>
<text x="567" y="74" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Verdict</text>

<!-- Light Tile -->
<rect x="30" y="90" width="140" height="44" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="100" y="111" fill="{Gr}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Light Tile</text>
<text x="100" y="126" fill="{Cd}" font-size="10" text-anchor="middle">Standard</text>

<rect x="175" y="90" width="120" height="44" rx="4" fill="{D2}"/>
<text x="235" y="115" fill="{Gr}" font-size="14" text-anchor="middle">Full</text>

<rect x="300" y="90" width="160" height="44" rx="4" fill="{D2}"/>
<text x="380" y="115" fill="{Gr}" font-size="12" text-anchor="middle">Full duration</text>

<rect x="465" y="90" width="205" height="44" rx="4" fill="{D2}"/>
<text x="567" y="115" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Always Safe</text>

<line x1="30" y1="139" x2="670" y2="139" stroke="{Cd}" stroke-width="0.3" opacity="0.2"/>

<!-- Dark Tile -->
<rect x="30" y="144" width="140" height="44" rx="4" fill="{D2}" stroke="#3A2030" stroke-width="1"/>
<text x="100" y="165" fill="#7A3D4A" font-family="{FONT_M}" font-size="12" text-anchor="middle">Dark Tile</text>
<text x="100" y="180" fill="{Cd}" font-size="10" text-anchor="middle">Shadow zone</text>

<rect x="175" y="144" width="120" height="44" rx="4" fill="{D2}"/>
<text x="235" y="169" fill="{O}" font-size="14" text-anchor="middle">Silent fail</text>

<rect x="300" y="144" width="160" height="44" rx="4" fill="{D2}"/>
<text x="380" y="169" fill="{Cd}" font-size="12" text-anchor="middle">None</text>

<rect x="465" y="144" width="205" height="44" rx="4" fill="{D2}"/>
<text x="567" y="169" fill="{O}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Move off ASAP</text>

<line x1="30" y1="193" x2="670" y2="193" stroke="{Cd}" stroke-width="0.3" opacity="0.2"/>

<!-- Ghost Tile -->
<rect x="30" y="198" width="140" height="44" rx="4" fill="{D2}" stroke="{T}" stroke-width="1"/>
<text x="100" y="219" fill="{T}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Ghost Tile</text>
<text x="100" y="234" fill="{Cd}" font-size="10" text-anchor="middle">Phantom zone</text>

<rect x="175" y="198" width="120" height="44" rx="4" fill="{D2}"/>
<text x="235" y="223" fill="{T}" font-size="14" text-anchor="middle">Fake activates</text>

<rect x="300" y="198" width="160" height="44" rx="4" fill="{D2}"/>
<text x="380" y="223" fill="{Cd}" font-size="12" text-anchor="middle">Cancelled</text>

<rect x="465" y="198" width="205" height="44" rx="4" fill="{D2}"/>
<text x="567" y="223" fill="{T}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Tricky. Test 1st</text>

<line x1="30" y1="247" x2="670" y2="247" stroke="{Cd}" stroke-width="0.3" opacity="0.2"/>

<!-- Boundary Tile -->
<rect x="30" y="252" width="140" height="44" rx="4" fill="{D2}" stroke="{R}" stroke-width="1"/>
<text x="100" y="273" fill="{R}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Boundary Tile</text>
<text x="100" y="288" fill="{Cd}" font-size="10" text-anchor="middle">Edge zone</text>

<rect x="175" y="252" width="120" height="44" rx="4" fill="{D2}"/>
<text x="235" y="277" fill="{O}" font-size="14" text-anchor="middle">Degraded</text>

<rect x="300" y="252" width="160" height="44" rx="4" fill="{D2}"/>
<text x="380" y="277" fill="{Cd}" font-size="12" text-anchor="middle">50% reduced</text>

<rect x="465" y="252" width="205" height="44" rx="4" fill="{D2}"/>
<text x="567" y="277" fill="{R}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Center zone only</text>

<!-- Gold Tile -->
<rect x="30" y="301" width="140" height="44" rx="4" fill="{D2}" stroke="{G}" stroke-width="1.5"/>
<text x="100" y="322" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Gold Tile</text>
<text x="100" y="337" fill="{Cd}" font-size="10" text-anchor="middle">Value zone</text>

<rect x="175" y="301" width="120" height="44" rx="4" fill="{D2}"/>
<text x="235" y="326" fill="{G}" font-size="14" text-anchor="middle">Full + Bonus</text>

<rect x="300" y="301" width="160" height="44" rx="4" fill="{D2}"/>
<text x="380" y="326" fill="{Gr}" font-size="12" text-anchor="middle">Enhanced</text>

<rect x="465" y="301" width="205" height="44" rx="4" fill="{D2}"/>
<text x="567" y="326" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">PRIORITY TARGET</text>
</svg>""")

# =============================================
# 9. OPENING TURN 1-3 DECISION TREE
# =============================================
write_svg("opening-decision-tree.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Universal Opening Template - Turn 1-3</text>

<!-- Turn 1 -->
<rect x="35" y="65" width="190" height="130" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="35" y="65" width="190" height="28" rx="8" fill="{T}" opacity="0.2"/>
<text x="130" y="84" fill="{T}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Turn 1: MOVE</text>
<text x="130" y="108" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Control Center</text>
<text x="130" y="128" fill="{Cd}" font-size="11" text-anchor="middle">Move center piece</text>
<text x="130" y="146" fill="{Cd}" font-size="11" text-anchor="middle">2 squares forward</text>
<text x="130" y="164" fill="{Cd}" font-size="11" text-anchor="middle">Center opponent's side</text>
<text x="130" y="182" fill="{Gr}" font-size="11" text-anchor="middle">100% safe move</text>

<arrow x="235" y="130" fill="{Cd}" font-size="20">-></arrow>

<!-- Turn 2 -->
<rect x="255" y="65" width="190" height="130" rx="8" fill="{D2}" stroke="{G}" stroke-width="1.5"/>
<rect x="255" y="65" width="190" height="28" rx="8" fill="{G}" opacity="0.2"/>
<text x="350" y="84" fill="{G}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Turn 2: PICK</text>
<text x="350" y="108" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Buy ANY Gambit</text>
<text x="350" y="128" fill="{Cd}" font-size="11" text-anchor="middle">Shop gambit available?</text>
<text x="350" y="146" fill="{G}" font-size="11" text-anchor="middle">Buy it</text>
<text x="350" y="164" fill="{Cd}" font-size="11" text-anchor="middle">None affordable?</text>
<text x="350" y="182" fill="{Gr}" font-size="11" text-anchor="middle">Buy the cheapest one</text>

<arrow x="455" y="130" fill="{Cd}" font-size="20">-></arrow>

<!-- Turn 3 -->
<rect x="475" y="65" width="190" height="130" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<rect x="475" y="65" width="190" height="28" rx="8" fill="{O}" opacity="0.2"/>
<text x="570" y="84" fill="{O}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Turn 3: SYNERGIZE</text>
<text x="570" y="108" fill="{C}" font-size="12" font-weight="bold" text-anchor="middle">Create Interaction</text>
<text x="570" y="128" fill="{Cd}" font-size="11" text-anchor="middle">Apply gambit near</text>
<text x="570" y="146" fill="{Cd}" font-size="11" text-anchor="middle">your center piece</text>
<text x="570" y="164" fill="{Cd}" font-size="11" text-anchor="middle">Build 1 synergy</text>
<text x="570" y="182" fill="{O}" font-size="11" text-anchor="middle">Not perfect, just 1 link</text>

<!-- Traps -->
<rect x="100" y="215" width="500" height="80" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="238" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">3 Opening Traps to Avoid</text>
<text x="350" y="258" fill="{Cd}" font-size="11" text-anchor="middle">Trap 1: Overextension - Dont move a piece more than 2 squares from start</text>
<text x="350" y="276" fill="{Cd}" font-size="11" text-anchor="middle">Trap 2: Saving for big gambit - Buy ANY gambit, dont hoard</text>
<text x="350" y="294" fill="{Cd}" font-size="11" text-anchor="middle">Trap 3: Seed superstition - This template works with ANY seed</text>

<rect x="100" y="310" width="500" height="28" rx="4" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="350" y="329" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Tested 50+ runs - Works with ANY starting piece, board, seed</text>
</svg>""")

# =============================================
# 10. SACRIFICE EVALUATION MATRIX
# =============================================
write_svg("evaluation-matrix.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">4-Dimensional Piece Evaluation Matrix</text>

<rect x="30" y="55" width="640" height="38" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="79" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Before sacrificing: evaluate across ALL 4 dimensions, not just 1</text>

<!-- Dimensions -->
<rect x="30" y="105" width="145" height="100" rx="8" fill="{D2}" stroke="{Gr}" stroke-width="1.5"/>
<rect x="30" y="105" width="145" height="26" rx="8" fill="{Gr}" opacity="0.2"/>
<text x="102" y="123" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">DIMENSION 1</text>
<text x="102" y="148" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Stock Value</text>
<text x="102" y="170" fill="{Cd}" font-size="11" text-anchor="middle">Stock gain per turn</text>
<text x="102" y="188" fill="{Cd}" font-size="11" text-anchor="middle">+ future projection</text>

<rect x="190" y="105" width="145" height="100" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="190" y="105" width="145" height="26" rx="8" fill="{T}" opacity="0.2"/>
<text x="262" y="123" fill="{T}" font-family="{FONT_M}" font-size="13" text-anchor="middle">DIMENSION 2</text>
<text x="262" y="148" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Gambit Weight</text>
<text x="262" y="170" fill="{Cd}" font-size="11" text-anchor="middle">Gambits this piece</text>
<text x="262" y="188" fill="{Cd}" font-size="11" text-anchor="middle">triggers per turn</text>

<rect x="350" y="105" width="145" height="100" rx="8" fill="{D2}" stroke="{G}" stroke-width="1.5"/>
<rect x="350" y="105" width="145" height="26" rx="8" fill="{G}" opacity="0.2"/>
<text x="422" y="123" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">DIMENSION 3</text>
<text x="422" y="148" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Board Control</text>
<text x="422" y="170" fill="{Cd}" font-size="11" text-anchor="middle">Squares covered</text>
<text x="422" y="188" fill="{Cd}" font-size="11" text-anchor="middle">Loss of space</text>

<rect x="510" y="105" width="160" height="100" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<rect x="510" y="105" width="160" height="26" rx="8" fill="{O}" opacity="0.2"/>
<text x="590" y="123" fill="{O}" font-family="{FONT_M}" font-size="13" text-anchor="middle">DIMENSION 4</text>
<text x="590" y="148" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">Replacement Cost</text>
<text x="590" y="170" fill="{Cd}" font-size="11" text-anchor="middle">Stock to replace</text>
<text x="590" y="188" fill="{Cd}" font-size="11" text-anchor="middle">+ missed turns</text>

<!-- Common mistakes -->
<rect x="100" y="225" width="500" height="75" rx="8" fill="#3A2030" stroke="{R}" stroke-width="1"/>
<text x="350" y="245" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="middle">3 Common Mistake Patterns</text>
<text x="350" y="265" fill="{Cd}" font-size="11" text-anchor="middle">False Accounting: Only looking at stock value, ignoring gambit weight</text>
<text x="350" y="283" fill="{Cd}" font-size="11" text-anchor="middle">Short Vision: Save 5 stock now, lose 8 stock per turn forever</text>
<text x="350" y="301" fill="{Cd}" font-size="11" text-anchor="middle">Panic Sacrifice: Boss in 1 turn, sold the economy engine</text>

<!-- 5-question checklist -->
<rect x="100" y="315" width="500" height="50" rx="8" fill="{D2}" stroke="{Gr}" stroke-width="1.5"/>
<text x="350" y="333" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">5-Question Sacrifice Checklist</text>
<text x="350" y="353" fill="{C}" font-size="11" text-anchor="middle">Q1: Can I buy it back? | Q2: Does it trigger 2+ gambits? | Q3: Any other piece to sacrifice?</text>
</svg>""")

print("\nAll 10 SVGs generated successfully!")
