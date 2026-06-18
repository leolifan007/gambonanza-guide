# -*- coding: utf-8 -*-
"""Generate SVG diagrams for all 8 articles"""
import os, textwrap, shutil

DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\static\images\diagrams"
os.makedirs(DIR, exist_ok=True)

def write_svg(name, svg):
    path = os.path.join(DIR, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg.strip())
    print(f"  {name} ({os.path.getsize(path)} bytes)")

# ===== Design tokens matching site VI =====
D = "#1A0F1A"       # dark bg
D2 = "#2D1A2D"      # dark-2
G = "#D4A84A"       # gold
T = "#4A9B9B"       # teal
R = "#A85D6A"       # rose
O = "#D4764A"       # orange
C = "#F5E6D3"       # cream
Cd = "#E8D5C0"      # cream-dark
Gr = "#5CB85C"      # green
FONT = "Inter,sans-serif"
FONT_M = "'VT323',monospace"
BASE = f'xmlns="http://www.w3.org/2000/svg" font-family="{FONT}"'

print("Generating SVGs...")

# ===== 1. BOSS PROGRESSION =====
write_svg("boss-progression.svg", f"""<svg {BASE} width="700" height="440" viewBox="0 0 700 440">
<rect width="700" height="440" fill="{D}" rx="12"/>
<text x="350" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Boss Progression Chart</text>

<!-- Stage labels -->
<text x="60" y="75" fill="{Cd}" font-size="12">Stage 2</text>
<text x="60" y="140" fill="{Cd}" font-size="12">Stage 4</text>
<text x="60" y="210" fill="{Cd}" font-size="12">Stage 6</text>
<text x="60" y="280" fill="{Cd}" font-size="12">Stage 8</text>
<text x="60" y="365" fill="{G}" font-family="{FONT_M}" font-size="14">Stage 10</text>

<!-- Boss boxes -->
<rect x="130" y="58" width="150" height="30" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="205" y="78" fill="{C}" font-size="13" text-anchor="middle">Stage 2 Boss (Easy)</text>

<rect x="130" y="125" width="150" height="30" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="205" y="145" fill="{C}" font-size="13" text-anchor="middle">Stage 4 Boss (Moderate)</text>

<rect x="130" y="195" width="150" height="30" rx="6" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<text x="205" y="215" fill="{C}" font-size="13" text-anchor="middle">Stage 6 Boss (Hard)</text>

<rect x="130" y="265" width="150" height="30" rx="6" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<text x="205" y="285" fill="{C}" font-size="13" text-anchor="middle">Stage 8 Boss (V.Hard)</text>

<rect x="130" y="340" width="150" height="60" rx="8" fill="{D2}" stroke="{G}" stroke-width="2"/>
<text x="205" y="365" fill="{G}" font-family="{FONT_M}" font-size="15" text-anchor="middle">GRANDMASTER</text>
<text x="205" y="385" fill="{Cd}" font-size="12" text-anchor="middle">Stage 10 Final Boss</text>

<!-- Connector lines -->
<line x1="280" y1="73" x2="330" y2="73" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="330" y1="73" x2="330" y2="140" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="280" y1="140" x2="330" y2="140" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="280" y1="210" x2="330" y2="210" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="330" y1="210" x2="330" y2="280" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="280" y1="280" x2="330" y2="280" stroke="{Cd}" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="280" y1="370" x2="330" y2="370" stroke="{G}" stroke-width="1.5" stroke-dasharray="3,3"/>

<!-- Check recommendations -->
<text x="350" y="80" fill="{Gr}" font-size="12">Any build works</text>
<text x="350" y="147" fill="{Gr}" font-size="12">Have 1 defensive gambit</text>
<text x="350" y="217" fill="{O}" font-size="12">Teleport + Backstab recommended</text>
<text x="350" y="287" fill="{O}" font-size="12">Save Ultimate Counter for Phase 3</text>
<text x="350" y="365" fill="{G}" font-size="13" font-weight="bold">Ultimate Counter + Teleport - MUST HAVE</text>
<text x="350" y="385" fill="{Cd}" font-size="12">20+ stock, multi-phase fight</text>

<!-- King difficulty note -->
<rect x="350" y="400" width="320" height="28" rx="4" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="510" y="418" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">King: Stage 6 True Final Boss after Grandmaster</text>
</svg>""")

# ===== 2. GRANDMASTER PHASES =====
write_svg("grandmaster-phases.svg", f"""<svg {BASE} width="700" height="350" viewBox="0 0 700 350">
<rect width="700" height="350" fill="{D}" rx="12"/>
<text x="350" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Grandmaster Boss Fight - Phase Breakdown</text>

<!-- Phase 1 -->
<rect x="30" y="70" width="190" height="220" rx="10" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="30" y="70" width="190" height="36" rx="10" fill="{T}" opacity="0.2"/>
<text x="125" y="93" fill="{T}" font-family="{FONT_M}" font-size="16" text-anchor="middle">Phase 1</text>
<text x="125" y="115" fill="{C}" font-size="13" text-anchor="middle">Grandmaster Standard</text>
<text x="125" y="140" fill="{Cd}" font-size="11" text-anchor="middle">Normal AI with</text>
<text x="125" y="156" fill="{Cd}" font-size="11" text-anchor="middle">enhanced stats</text>
<text x="125" y="176" fill="{Cd}" font-size="11" text-anchor="middle">Standard piece</text>
<text x="125" y="192" fill="{Cd}" font-size="11" text-anchor="middle">placement</text>
<line x1="50" y1="210" x2="200" y2="210" stroke="{T}" stroke-width="0.5" opacity="0.3"/>
<text x="125" y="232" fill="{Gr}" font-size="12" text-anchor="middle">Goal:</text>
<text x="125" y="250" fill="{C}" font-size="11" text-anchor="middle">Establish position</text>
<text x="125" y="266" fill="{C}" font-size="11" text-anchor="middle">Dont lose pieces</text>

<!-- Arrow -->
<text x="235" y="180" fill="{Cd}" font-size="20">-></text>

<!-- Phase 2 -->
<rect x="255" y="70" width="190" height="220" rx="10" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<rect x="255" y="70" width="190" height="36" rx="10" fill="{R}" opacity="0.2"/>
<text x="350" y="93" fill="{R}" font-family="{FONT_M}" font-size="16" text-anchor="middle">Phase 2</text>
<text x="350" y="115" fill="{C}" font-size="13" text-anchor="middle">Grandmaster Aggressive</text>
<text x="350" y="140" fill="{Cd}" font-size="11" text-anchor="middle">AI targets key pieces</text>
<text x="350" y="156" fill="{Cd}" font-size="11" text-anchor="middle">Increased capture</text>
<text x="350" y="176" fill="{Cd}" font-size="11" text-anchor="middle">frequency</text>
<line x1="275" y1="210" x2="425" y2="210" stroke="{R}" stroke-width="0.5" opacity="0.3"/>
<text x="350" y="232" fill="{O}" font-size="12" text-anchor="middle">Goal:</text>
<text x="350" y="250" fill="{C}" font-size="11" text-anchor="middle">SURVIVE</text>
<text x="350" y="266" fill="{Cd}" font-size="11" text-anchor="middle">Dont try to win here</text>

<!-- Arrow -->
<text x="460" y="180" fill="{Cd}" font-size="20">-></text>

<!-- Phase 3 -->
<rect x="480" y="70" width="190" height="220" rx="10" fill="{D2}" stroke="{G}" stroke-width="2"/>
<rect x="480" y="70" width="190" height="36" rx="10" fill="{G}" opacity="0.2"/>
<text x="575" y="93" fill="{G}" font-family="{FONT_M}" font-size="16" text-anchor="middle">Phase 3</text>
<text x="575" y="115" fill="{C}" font-size="13" text-anchor="middle">Grandmaster Desperation</text>
<text x="575" y="140" fill="{Cd}" font-size="11" text-anchor="middle">Multiple threats/turn</text>
<text x="575" y="156" fill="{Cd}" font-size="11" text-anchor="middle">Sacrifices for position</text>
<text x="575" y="176" fill="{Cd}" font-size="11" text-anchor="middle">Most runs end here!</text>
<line x1="500" y1="210" x2="650" y2="210" stroke="{G}" stroke-width="0.5" opacity="0.3"/>
<text x="575" y="232" fill="{Gr}" font-size="12" text-anchor="middle">WIN CONDITION</text>
<text x="575" y="252" fill="{G}" font-size="12" font-weight="bold" text-anchor="middle">Use Ultimate Counter</text>
<text x="575" y="270" fill="{C}" font-size="11" text-anchor="middle">Go all-in here</text>

<!-- Bottom tip -->
<rect x="100" y="305" width="500" height="32" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="325" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">PRO TIP: Save The Ultimate Counter specifically for Phase 3</text>
</svg>""")

# ===== 3. SPECTRAL CONVERSION FLOW =====
write_svg("spectral-conversion.svg", f"""<svg {BASE} width="700" height="320" viewBox="0 0 700 320">
<rect width="700" height="320" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Spectral Piece - Gold Tile Conversion Flow</text>

<!-- Step 1 -->
<rect x="30" y="70" width="180" height="180" rx="10" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<rect x="30" y="70" width="180" height="30" rx="10" fill="{T}" opacity="0.2"/>
<text x="120" y="90" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 1</text>
<text x="120" y="120" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">Get Spectral Piece</text>
<text x="120" y="148" fill="{Cd}" font-size="12" text-anchor="middle">From Piece Wheel</text>
<text x="120" y="166" fill="{Cd}" font-size="12" text-anchor="middle">Shop events</text>
<text x="120" y="184" fill="{Cd}" font-size="12" text-anchor="middle">Gambit rewards</text>
<text x="120" y="210" fill="{Cd}" font-size="11" text-anchor="middle">Has expiration timer</text>
<text x="120" y="228" fill="{O}" font-size="11" text-anchor="middle">Must act before timer!</text>

<!-- Arrow -->
<text x="225" y="160" fill="{G}" font-size="28">-></text>

<!-- Step 2 -->
<rect x="260" y="70" width="180" height="180" rx="10" fill="{D2}" stroke="{G}" stroke-width="2"/>
<rect x="260" y="70" width="180" height="30" rx="10" fill="{G}" opacity="0.2"/>
<text x="350" y="90" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 2</text>
<text x="350" y="120" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">Move to Gold Tile</text>
<circle cx="350" cy="152" r="18" fill="none" stroke="{G}" stroke-width="2"/>
<text x="350" y="157" fill="{G}" font-size="12" text-anchor="middle">$</text>
<text x="350" y="185" fill="{Cd}" font-size="12" text-anchor="middle">Gold tile converts</text>
<text x="350" y="203" fill="{Cd}" font-size="12" text-anchor="middle">spectral -> permanent</text>
<text x="350" y="225" fill="{Gr}" font-size="12" text-anchor="middle">Tile also generates $$</text>

<!-- Arrow -->
<text x="455" y="160" fill="{G}" font-size="28">-></text>

<!-- Step 3 -->
<rect x="490" y="70" width="180" height="180" rx="10" fill="{D2}" stroke="{Gr}" stroke-width="1.5"/>
<rect x="490" y="70" width="180" height="30" rx="10" fill="{Gr}" opacity="0.2"/>
<text x="580" y="90" fill="{Gr}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 3</text>
<text x="580" y="120" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">Permanent!</text>
<text x="580" y="148" fill="{Cd}" font-size="12" text-anchor="middle">Piece is now permanent</text>
<text x="580" y="166" fill="{Cd}" font-size="12" text-anchor="middle">Retains all buffs</text>
<text x="580" y="184" fill="{Cd}" font-size="12" text-anchor="middle">No expiration</text>
<text x="580" y="210" fill="{G}" font-size="12" text-anchor="middle">VALUE DOUBLED:</text>
<text x="580" y="228" fill="{Gr}" font-size="12" text-anchor="middle">Income + Permanent piece</text>

<!-- Bottom tip -->
<rect x="100" y="270" width="500" height="36" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="350" y="293" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Community verified on Reddit & YouTube - Best value mechanic in v1.1.0</text>
</svg>""")

# ===== 4. ECONOMIC LOOP =====
write_svg("economic-loop.svg", f"""<svg {BASE} width="600" height="420" viewBox="0 0 600 420">
<rect width="600" height="420" fill="{D}" rx="12"/>
<text x="300" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Economic Gambit Loop</text>

<!-- Cycle arrow circle -->
<circle cx="300" cy="220" r="130" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="8,4"/>

<!-- Step 1: top -->
<rect x="200" y="60" width="200" height="50" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="300" y="83" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 1</text>
<text x="300" y="100" fill="{C}" font-size="13" text-anchor="middle">Take Economic Gambit</text>

<!-- Step 2: right -->
<rect x="370" y="195" width="200" height="50" rx="8" fill="{D2}" stroke="{Gr}" stroke-width="1.5"/>
<text x="470" y="218" fill="{Gr}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 2</text>
<text x="470" y="235" fill="{C}" font-size="13" text-anchor="middle">Pawn capture -> Coin</text>

<!-- Step 3: bottom -->
<rect x="200" y="320" width="200" height="50" rx="8" fill="{D2}" stroke="{G}" stroke-width="1.5"/>
<text x="300" y="343" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Step 3</text>
<text x="300" y="360" fill="{C}" font-size="13" text-anchor="middle">Coin -> Buy more Gambits</text>

<!-- Step 4: left -->
<rect x="30" y="195" width="200" height="50" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<text x="130" y="218" fill="{O}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Bonus</text>
<text x="130" y="235" fill="{C}" font-size="13" text-anchor="middle">Gold Tile + Gambit = $$ both</text>

<!-- Arrow annotations -->
<text x="300" y="135" fill="{Cd}" font-size="11" text-anchor="middle">|</text>
<text x="300" y="155" fill="{Cd}" font-size="11" text-anchor="middle">v</text>
<text x="470" y="180" fill="{Cd}" font-size="11" text-anchor="middle"><-</text>
<text x="305" y="295" fill="{Cd}" font-size="11" text-anchor="middle">|</text>
<text x="305" y="310" fill="{Cd}" font-size="11" text-anchor="middle">v</text>
<text x="175" y="290" fill="{Cd}" font-size="11" text-anchor="middle"><-</text>
<text x="175" y="180" fill="{G}" font-size="11" text-anchor="middle"><-</text>

<!-- Stats box -->
<rect x="170" y="145" width="260" height="38" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="300" y="165" fill="{G}" font-size="12" font-weight="bold" text-anchor="middle">70%+ win rate - S-tier strategy every run</text>
<text x="300" y="180" fill="{Cd}" font-size="11" text-anchor="middle">5+ stock per turn once loop is established</text>
</svg>""")

# ===== 5. CRUMBLE BOARD DECAY =====
write_svg("crumble-stages.svg", f"""<svg {BASE} width="700" height="400" viewBox="0 0 700 400">
<rect width="700" height="400" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Crumble Mode - Board Decay Stages</text>

def draw_board(cx, cy, size, label, color):
    s = size * 12
    offset = s // 2
    x, y = cx - offset, cy - offset
    # Board background
    rect = f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="4" fill="{D2}" stroke="{color}" stroke-width="1.5"/>'
    # Grid squares
    grid = ""
    for i in range(size):
        for j in range(size):
            gx = x + j * (s / size)
            gy = y + i * (s / size)
            fill = "#3A2030" if (i + j) % 2 == 0 else D2
            grid += f'<rect x="{gx}" y="{gy}" width="{s/size}" height="{s/size}" fill="{fill}" stroke="none"/>'
            # Center marker for stages
            if size == 4:
                grid += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{G}" opacity="0.5"/>'
    return rect + grid

# Stage 1 - 8x8
rect1 = f'<rect x="30" y="55" width="100" height="100" rx="4" fill="{D2}" stroke="{T}" stroke-width="1.5"/>'
text1 = f'<text x="80" y="175" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 1</text><text x="80" y="192" fill="{Cd}" font-size="11" text-anchor="middle">Full 8x8</text>'
# Grid
for i in range(8):
    for j in range(8):
        gx, gy = 30 + j*12.5, 55 + i*12.5
        fill = "#3A2030" if (i+j)%2 == 0 else D2
        rect1 += f'<rect x="{gx}" y="{gy}" width="12.5" height="12.5" fill="{fill}" stroke="#3A2030" stroke-width="0.5"/>'

write_svg("crumble-stages.svg", f"""<svg {BASE} width="700" height="400" viewBox="0 0 700 400">
<rect width="700" height="400" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Crumble Mode - Board Decay 5 Stages</text>

<!-- Stage 1 -->
<rect x="30" y="55" width="100" height="100" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="80" y="175" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 1</text>
<text x="80" y="192" fill="{Cd}" font-size="11" text-anchor="middle">8x8 - Full</text>

<!-- Stage 2 -->
<rect x="155" y="68" width="80" height="80" rx="6" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="195" y="168" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 2</text>
<text x="195" y="185" fill="{Cd}" font-size="11" text-anchor="middle">7x7 - 1st collapse</text>

<!-- Stage 3 -->
<rect x="260" y="80" width="60" height="60" rx="6" fill="{D2}" stroke="{R}" stroke-width="1.5"/>
<text x="290" y="160" fill="{R}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 3</text>
<text x="290" y="177" fill="{Cd}" font-size="11" text-anchor="middle">6x6 - Knights suffer</text>

<!-- Stage 4 -->
<rect x="345" y="90" width="45" height="45" rx="6" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<text x="367" y="153" fill="{O}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 4</text>
<text x="367" y="170" fill="{Cd}" font-size="11" text-anchor="middle">5x5 - Critical phase</text>

<!-- Stage 5 -->
<rect x="415" y="98" width="33" height="33" rx="6" fill="{D2}" stroke="{G}" stroke-width="2"/>
<text x="432" y="148" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Stage 5</text>
<text x="432" y="165" fill="{Cd}" font-size="11" text-anchor="middle">4x4 - Endgame</text>

<!-- Collapse arrows -->
<text x="140" y="110" fill="{Cd}" font-size="18">-></text>
<text x="243" y="110" fill="{Cd}" font-size="18">-></text>
<text x="328" y="115" fill="{Cd}" font-size="18">-></text>
<text x="398" y="118" fill="{Cd}" font-size="18">-></text>

<!-- Strategy tips -->
<rect x="30" y="210" width="640" height="175" rx="8" fill="{D2}" stroke="{G}" stroke-width="1"/>
<text x="350" y="235" fill="{G}" font-family="{FONT_M}" font-size="15" text-anchor="middle">Strategy by Stage</text>

<text x="50" y="260" fill="{T}" font-family="{FONT_M}" font-size="13">Stage 1-2</text>
<text x="140" y="260" fill="{Cd}" font-size="12">Economic gambits early. Compact center. Avoid edges.</text>

<text x="50" y="285" fill="{R}" font-family="{FONT_M}" font-size="13">Stage 3</text>
<text x="140" y="285" fill="{Cd}" font-size="12">Trade Knights for Rooks. Activate Reserve gambits.</text>

<text x="50" y="310" fill="{O}" font-family="{FONT_M}" font-size="13">Stage 4</text>
<text x="140" y="310" fill="{Cd}" font-size="12">Every piece must pull weight. Backstab + Trap tiles shine.</text>

<text x="50" y="335" fill="{G}" font-family="{FONT_M}" font-size="13">Stage 5</text>
<text x="140" y="335" fill="{Cd}" font-size="12">Every move threatens capture. Teleport dominates.</text>

<text x="50" y="360" fill="{R}" font-size="12">3/3 Counter:</text>
<text x="140" y="360" fill="{Cd}" font-size="11">3 moves without capture = board collapses one stage. Capture resets counter.</text>
</svg>""")

# ===== 6. DIFFICULTY LADDER =====
write_svg("difficulty-ladder.svg", f"""<svg {BASE} width="600" height="420" viewBox="0 0 600 420">
<rect width="600" height="420" fill="{D}" rx="12"/>
<text x="300" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Difficulty Progression Ladder</text>

levels = [
    ("Easy", 30, T, "3-5 runs", "Tutorial AI, gambits persistent"),
    ("Normal", 100, T, "10-15 runs", "Reactive AI, limited gambit expiration"),
    ("Queen", 170, R, "25-40 runs", "Aggressive AI, gambits expire 5 rounds"),
    ("King", 240, O, "25+ runs", "Clinical AI, multi-phase bosses"),
    ("Grandmaster", 310, G, "50+ runs est.", "True Final Boss at Stage 6"),
]

for name, y, color, clears, desc in levels:
    rect = f'<rect x="40" y="{y}" width="200" height="36" rx="8" fill="{D2}" stroke="{color}" stroke-width="1.5"/>'
    text_name = f'<text x="140" y="{y+23}" fill="{color}" font-family="{FONT_M}" font-size="15" text-anchor="middle">{name}</text>'
    text_clear = f'<text x="270" y="{y+15}" fill="{Cd}" font-size="12">First clear: {clears}</text>'
    text_desc = f'<text x="270" y="{y+30}" fill="{Cd}" font-size="10">{desc}</text>'
    # ladder rung
    rung = ""
    if len(levels) > 1 and name != "Easy":
        rung = f'<line x1="140" y1="{y}" x2="140" y2="{y-15}" stroke="{color}" stroke-width="1.5"/>'
    print(rect + text_name + text_clear + text_desc + rung)

# Use raw for simplicity
stages = [
    (30, "Easy", T, "3-5 runs", "Tutorial AI, gambits persistent"),
    (100, "Normal", T, "10-15 runs", "Reactive AI, limited gambit expiration"),
    (170, "Queen", R, "25-40 runs", "Aggressive AI, gambits expire 5 rounds"),
    (240, "King", O, "25+ runs", "Clinical AI, multi-phase bosses"),
    (310, "Grandmaster", G, "50+ runs est.", "True Final Boss at Stage 6"),
]
content = ""
for i, (y, name, color, clears, desc) in enumerate(stages):
    content += f'<rect x="30" y="{y}" width="220" height="44" rx="8" fill="{D2}" stroke="{color}" stroke-width="1.5"/>'
    content += f'<text x="140" y="{y+27}" fill="{color}" font-family="{FONT_M}" font-size="16" text-anchor="middle">{name}</text>'
    content += f'<text x="280" y="{y+18}" fill="{Cd}" font-size="12">First clear: {clears}</text>'
    content += f'<text x="280" y="{y+35}" fill="{Cd}" font-size="11">{desc}</text>'
    if i > 0:
        content += f'<line x1="140" y1="{y}" x2="140" y2="{y-24}" stroke="{color}" stroke-width="1.5" stroke-dasharray="4,3"/>'

write_svg("difficulty-ladder.svg", f"""<svg {BASE} width="600" height="420" viewBox="0 0 600 420">
<rect width="600" height="420" fill="{D}" rx="12"/>
<text x="300" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Difficulty Progression Ladder</text>
{content}
<rect x="30" y="370" width="540" height="36" rx="6" fill="#3A2030" stroke="{G}" stroke-width="1"/>
<text x="300" y="393" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Rule: 50%+ win rate at current difficulty before advancing</text>
</svg>""")

# ===== 7. BUILD ARCHETYPE COMPARISON =====
write_svg("build-comparison.svg", f"""<svg {BASE} width="700" height="340" viewBox="0 0 700 340">
<rect width="700" height="340" fill="{D}" rx="12"/>
<text x="350" y="38" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Build Archetype Comparison</text>

# Header
headers = ["Build", "Win Rate", "Difficulty", "Best Board"]
cols = [0, 140, 280, 420, 560]
for i, h in enumerate(headers):
    x = cols[len(headers)-1] if i == len(headers)-1 else cols[i]
    text = f'<text x="{x + (120 if i==0 else 80) if i < len(headers)-1 else x+80}" y="65" fill="{G}" font-family="{FONT_M}" font-size="13" text-anchor="middle">{h}</text>'

rows = [
    ("Pawn Economy", "70%+", "Low", "Any", G),
    ("Queen Supremacy", "58-65%", "High", "7x7", T),
    ("Knight Aggro", "50-57%", "Medium", "5x5", R),
    ("Rook Control", "48-55%", "High", "6x6-7x7", O),
    ("Gambit Chain", "35-60%", "V.High", "7x7", "#7A3D4A"),
]

for i, (name, wr, diff, board, color) in enumerate(rows):
    y = 88 + i * 48
    # Row bg
    bg = f'<rect x="20" y="{y}" width="660" height="42" rx="6" fill="{D2}" stroke="{color}" stroke-width="1" opacity="0.8"/>'
    # Name
    nm = f'<text x="80" y="{y+26}" fill="{color}" font-family="{FONT_M}" font-size="13" text-anchor="middle">{name}</text>'
    # Win rate
    wr_elem = f'<text x="210" y="{y+26}" fill="{C}" font-size="13" font-weight="bold" text-anchor="middle">{wr}</text>'
    # Difficulty bar
    diff_width = {"Low": 60, "Medium": 100, "High": 140, "V.High": 170}[diff]
    diff_color = {"Low": Gr, "Medium": G, "High": O, "V.High": R}[diff]
    db = f'<rect x="300" y="{y+14}" width="{diff_width}" height="14" rx="3" fill="{diff_color}" opacity="0.6"/>'
    dt = f'<text x="370" y="{y+26}" fill="{C}" font-size="11" text-anchor="middle">{diff}</text>'
    # Board
    bd = f'<text x="520" y="{y+26}" fill="{Cd}" font-size="12" text-anchor="middle">{board}</text>'
    # Best for
    bf = f'<text x="600" y="{y+26}" fill="{color}" font-family="{FONT_M}" font-size="11" text-anchor="middle">Best</text>'

write_svg("build-comparison.svg", f"""<svg {BASE} width="700" height="370" viewBox="0 0 700 370">
<rect width="700" height="370" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Build Archetype Comparison</text>

<text x="80" y="68" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Build</text>
<text x="210" y="68" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Win Rate</text>
<text x="370" y="68" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Difficulty</text>
<text x="520" y="68" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Best Board</text>
<text x="620" y="68" fill="{G}" font-family="{FONT_M}" font-size="12" text-anchor="middle">Verdict</text>

<line x1="20" y1="78" x2="680" y2="78" stroke="{Cd}" stroke-width="0.5" opacity="0.3"/>

<rect x="20" y="88" width="660" height="42" rx="6" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="80" y="115" fill="{Gr}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Pawn Economy</text>
<text x="210" y="115" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">70%+</text>
<rect x="300" y="104" width="60" height="14" rx="3" fill="{Gr}" opacity="0.6"/>
<text x="370" y="115" fill="{C}" font-size="11" text-anchor="middle">Low</text>
<text x="520" y="115" fill="{Cd}" font-size="12" text-anchor="middle">Any</text>
<text x="620" y="115" fill="{Gr}" font-family="{FONT_M}" font-size="12" text-anchor="middle">S-Tier</text>

<rect x="20" y="136" width="660" height="42" rx="6" fill="{D2}" stroke="{T}" stroke-width="1"/>
<text x="80" y="163" fill="{T}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Queen Supremacy</text>
<text x="210" y="163" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">58-65%</text>
<rect x="300" y="152" width="140" height="14" rx="3" fill="{O}" opacity="0.6"/>
<text x="370" y="163" fill="{C}" font-size="11" text-anchor="middle">High</text>
<text x="520" y="163" fill="{Cd}" font-size="12" text-anchor="middle">7x7</text>
<text x="620" y="163" fill="{T}" font-family="{FONT_M}" font-size="12" text-anchor="middle">A-Tier</text>

<rect x="20" y="184" width="660" height="42" rx="6" fill="{D2}" stroke="{R}" stroke-width="1"/>
<text x="80" y="211" fill="{R}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Knight Aggro</text>
<text x="210" y="211" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">50-57%</text>
<rect x="300" y="200" width="100" height="14" rx="3" fill="{G}" opacity="0.6"/>
<text x="370" y="211" fill="{C}" font-size="11" text-anchor="middle">Medium</text>
<text x="520" y="211" fill="{Cd}" font-size="12" text-anchor="middle">5x5</text>
<text x="620" y="211" fill="{R}" font-family="{FONT_M}" font-size="12" text-anchor="middle">B-Tier</text>

<rect x="20" y="232" width="660" height="42" rx="6" fill="{D2}" stroke="{O}" stroke-width="1"/>
<text x="80" y="259" fill="{O}" font-family="{FONT_M}" font-size="13" text-anchor="middle">Rook Control</text>
<text x="210" y="259" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">48-55%</text>
<rect x="300" y="248" width="140" height="14" rx="3" fill="{O}" opacity="0.6"/>
<text x="370" y="259" fill="{C}" font-size="11" text-anchor="middle">High</text>
<text x="520" y="259" fill="{Cd}" font-size="12" text-anchor="middle">6x6-7x7</text>
<text x="620" y="259" fill="{O}" font-family="{FONT_M}" font-size="12" text-anchor="middle">B-Tier</text>

<rect x="20" y="280" width="660" height="42" rx="6" fill="{D2}" stroke="#7A3D4A" stroke-width="1"/>
<text x="80" y="307" fill="#7A3D4A" font-family="{FONT_M}" font-size="13" text-anchor="middle">Gambit Chain</text>
<text x="210" y="307" fill="{C}" font-size="14" font-weight="bold" text-anchor="middle">35-60%</text>
<rect x="300" y="296" width="170" height="14" rx="3" fill="{R}" opacity="0.6"/>
<text x="385" y="307" fill="{C}" font-size="11" text-anchor="middle">Very High</text>
<text x="520" y="307" fill="{Cd}" font-size="12" text-anchor="middle">7x7</text>
<text x="620" y="307" fill="#7A3D4A" font-family="{FONT_M}" font-size="12" text-anchor="middle">Situat.</text>
</svg>""")

# ===== 8. HIDDEN GAMBIT UNLOCK PATH =====
write_svg("hidden-gambit-path.svg", f"""<svg {BASE} width="700" height="380" viewBox="0 0 700 380">
<rect width="700" height="380" fill="{D}" rx="12"/>
<text x="350" y="35" fill="{G}" font-family="{FONT_M}" font-size="22" text-anchor="middle">Hidden Gambit Unlock Path</text>

<rect x="30" y="60" width="640" height="56" rx="8" fill="#3A2030" stroke="{T}" stroke-width="1"/>
<text x="50" y="82" fill="{T}" font-family="{FONT_M}" font-size="13">6 Hidden Gambits exist</text>
<text x="50" y="102" fill="{Cd}" font-size="12">5 have vague descriptions in collection menu. 1 has NO description at all (most mysterious).</text>

<rect x="30" y="130" width="150" height="80" rx="8" fill="{D2}" stroke="{T}" stroke-width="1.5"/>
<text x="105" y="156" fill="{T}" font-family="{FONT_M}" font-size="14" text-anchor="middle">HG #1-5</text>
<text x="105" y="178" fill="{Cd}" font-size="11" text-anchor="middle">Vague unlock hints</text>
<text x="105" y="195" fill="{Cd}" font-size="11" text-anchor="middle">Try diverse builds</text>

<text x="190" y="170" fill="{Cd}" font-size="18">-></text>

<rect x="215" y="130" width="200" height="80" rx="8" fill="{D2}" stroke="{O}" stroke-width="1.5"/>
<text x="315" y="156" fill="{O}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Theory: Triggers</text>
<text x="315" y="178" fill="{Cd}" font-size="11" text-anchor="middle">Single piece type runs</text>
<text x="315" y="195" fill="{Cd}" font-size="11" text-anchor="middle">Crumble Mode completions</text>

<text x="425" y="170" fill="{Cd}" font-size="18">-></text>

<rect x="450" y="130" width="220" height="80" rx="8" fill="{D2}" stroke="{G}" stroke-width="2"/>
<text x="560" y="156" fill="{G}" font-family="{FONT_M}" font-size="14" text-anchor="middle">Unlock!</text>
<text x="560" y="178" fill="{Cd}" font-size="11" text-anchor="middle">New gambits added</text>
<text x="560" y="195" fill="{Cd}" font-size="11" text-anchor="middle">to collection</text>

<!-- Secret 6th -->
<rect x="30" y="230" width="640" height="56" rx="8" fill="#3A2030" stroke="{G}" stroke-width="1.5"/>
<text x="50" y="252" fill="{G}" font-family="{FONT_M}" font-size="13">HG #6 - The Mystery Gambit</text>
<text x="50" y="272" fill="{Cd}" font-size="12">No unlock description at all. Community theory: Related to King difficulty True Final Boss at Stage 6.</text>

<rect x="30" y="300" width="640" height="65" rx="8" fill="{D2}" stroke="{Gr}" stroke-width="1"/>
<text x="50" y="322" fill="{Gr}" font-family="{FONT_M}" font-size="13">v1.1.0 added 2 new gambits:</text>
<text x="50" y="344" fill="{C}" font-size="13">Empress - New S-tier contender being explored</text>
<text x="50" y="360" fill="{C}" font-size="13">Horse Dealer - Knight-related interactions</text>
</svg>""")

print("\nDone! All SVGs created.")
