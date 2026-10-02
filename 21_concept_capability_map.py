import os
os.makedirs('out', exist_ok=True)
#!/usr/bin/env python3
"""Conceptual architecture v2 — spine layout, one colour family, AI as a distinct shape, hub + truth rail."""
import os
FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', SFMono-Regular, Consolas, monospace"
INK, SLATE, MUTED, LINE, PAPER = "#0f172a", "#334155", "#64748b", "#cbd5e1", "#f8fafc"
AI, AI_BG, AI_INK = "#2563eb", "#eff6ff", "#1e40af"
NEXT, NEXT_BG = "#7c3aed", "#f5f3ff"
GATE, GATE_BG, GATE_INK = "#059669", "#ecfdf5", "#065f46"
AMBER, AMBER_INK = "#d97706", "#92400e"
W, H = 1900, 1385
out = []
def w(s): out.append(s)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def text(x, y, s, size=11, anchor="start", weight="normal", fill=INK, font=FONT, style="", ls=""):
    ex = (f" font-style='{style}'" if style else "") + (f" letter-spacing='{ls}'" if ls else "")
    w(f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' text-anchor='{anchor}' font-weight='{weight}' fill='{fill}'{ex} dominant-baseline='middle' font-family=\"{font}\">{esc(s)}</text>")
def rect(x, y, wd, h, fill, stroke, rx=10, sw=1.5, dash="", extra=""):
    d = f" stroke-dasharray='{dash}'" if dash else ""
    w(f"<rect x='{x:.1f}' y='{y:.1f}' width='{wd:.1f}' height='{h:.1f}' rx='{rx}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'{d}{extra}/>")
def arrow(pts, color=SLATE, width=1.6, dashed=False):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    m = {SLATE: "a", AMBER: "am", AI: "ab"}[color]
    d = " stroke-dasharray='5 4'" if dashed else ""
    w(f"<polyline points='{p}' fill='none' stroke='{color}' stroke-width='{width}'{d} marker-end='url(#{m})'/>")
def diamond(x, y, s=8):
    w(f"<polygon points='{x},{y-s} {x+s},{y} {x},{y+s} {x-s},{y}' fill='{GATE_BG}' stroke='{GATE}' stroke-width='2'/>")
def hexagon(cx, cy, r, fill, stroke, sw=2):
    pts = " ".join(f"{cx + r * __import__('math').cos(__import__('math').radians(60*i-30)):.1f},{cy + r * __import__('math').sin(__import__('math').radians(60*i-30)):.1f}" for i in range(6))
    w(f"<polygon points='{pts}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'/>")

w(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-labelledby='t'>")
w("<title id='t'>AI API Testing Platform — conceptual architecture</title>")
w("<defs>")
for mid, col in [("a", SLATE), ("am", AMBER), ("ab", AI)]:
    w(f"<marker id='{mid}' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='6' markerHeight='6' orient='auto'><path d='M0,0 L10,5 L0,10 z' fill='{col}'/></marker>")
w("<filter id='sh' x='-5%' y='-5%' width='110%' height='125%'><feDropShadow dx='0' dy='2' stdDeviation='2.5' flood-color='#0f172a' flood-opacity='0.08'/></filter></defs>")
w(f"<rect width='{W}' height='{H}' fill='#ffffff'/>")

# ------------------------------------------------------------- title + tech strip
text(40, 40, "AI API Testing Platform", size=28, weight="700")
text(40, 72, "From an API contract to a verified fix. Engines prove, agents propose, people decide — around one canonical test case.", size=13.5, fill=MUTED)
tech = ["Python · FastAPI", "LangGraph", "Gemini on Vertex AI", "PostgreSQL · pgvector", "Pub/Sub", "GKE", "Karate", "Prism", "Git", "Jira · Zephyr", "Secret Manager", "Cloud Storage · DLP"]
tx = 40
for t in tech:
    tw = len(t) * 6.3 + 22
    rect(tx, 92, tw, 24, PAPER, LINE, rx=12, sw=1)
    text(tx + tw / 2, 104, t, size=10, anchor="middle", weight="600", fill=SLATE)
    tx += tw + 8
text(tx + 8, 104, "built on", size=10, fill=MUTED, style="italic")
# key (top right)
kx = W - 40
rect(kx - 110, 30, 110, 22, "#ffffff", SLATE, rx=5, sw=1.5); text(kx - 55, 41, "engine · release 1", size=9.5, anchor="middle", weight="600", fill=SLATE)
rect(kx - 230, 30, 110, 22, AI_BG, AI, rx=11, sw=1.5, dash="4 3"); text(kx - 175, 41, "AI agent · R2 / R3", size=9.5, anchor="middle", weight="700", fill=AI_INK)
rect(kx - 350, 30, 110, 22, NEXT_BG, NEXT, rx=11, sw=1.2, dash="2 3"); text(kx - 295, 41, "AI next · roadmap", size=9.5, anchor="middle", weight="700", fill=NEXT)
diamond(kx - 420, 41, 7); text(kx - 408, 41, "human gate", size=9.5, fill=GATE_INK, weight="600")
text(kx, 70, "five agents draft, never decide · every draft is checked by an engine and approved by a person", size=10, anchor="end", fill=MUTED)

# ------------------------------------------------------------- inputs (plain labels, no boxes)
IY = 148
text(40, IY, "WHAT COMES IN", size=10, weight="700", fill=MUTED, ls="0.14em")
CX0, CW_ = 330, 1530
ins = [("API contracts", "OpenAPI 3 · Swagger 2 · (R3) GraphQL"), ("Environments & logins", "dev / qa / staging · never prod"), ("Business content", "Jira stories · acceptance criteria"),
       ("Existing assets", "Karate suites · CSV data · QA catalog"), ("Runtime signals", "CI deploys · Jira webhooks · schedules"), ("Policy", "roles · PHI rules · thresholds")]
iw = CW_ / 6
for i, (a, b) in enumerate(ins):
    x = CX0 + i * iw
    text(x, IY - 6, a, size=12, weight="700"); text(x, IY + 10, b, size=9.5, fill=MUTED)
    w(f"<line x1='{x}' y1='{IY+22}' x2='{x}' y2='{IY+40}' stroke='{SLATE}' stroke-width='1.2' stroke-dasharray='2 3'/>")
w(f"<line x1='{CX0}' y1='{IY+40}' x2='{CX0+CW_-10}' y2='{IY+40}' stroke='{SLATE}' stroke-width='1.2' stroke-dasharray='2 3'/>")

# ------------------------------------------------------------- layers
LY0 = IY + 58
LH, OUT_H, LG = 140, 22, 14
STRIDE = LH + OUT_H + LG
SPX = 92            # spine x
RAIL = 312          # truth rail x
layers = [
    ("Discover &", "understand", [
        ("Discover & catalog the API", "eng", ["parse & normalize contracts", "classify safe · idempotent · mutating", "stable endpoint ids · diff & renames", "inventory + field catalog (PHI flags)"], "AI next: infer resource lifecycles"),
        ("The API knowledge model", "hub", ["endpoints · fields · constraints · scopes", "dependency graph: explicit + inferred", "coverage universe — all a test must cover", "versioned with the spec; read by every layer"], None),
        ("Extract business rules", "ai", ["rules from stories & acceptance criteria", "each with its source sentence + confidence", "mapped to endpoints and fields", "nothing used until a QE confirms"], None),
        ("Check readiness", "eng", ["secrets → vault; only an address is kept", "live check: reach · log in · one safe call", "real response vs the contract", "green · yellow (ack) · red (stop)"], None),
     ], ["API inventory", "field catalog", "dependency graph", "rules repository", "coverage universe", "readiness report"], [(2, "rules review"), (3, "readiness")]),
    ("Generate", "tests", [
        ("Write cases from the facts — six generators", "eng", ["structural · response-code · schema", "boundary · dependency chain · security", "smallest valid body + ONE mutation", "same spec in → same cases out"], None),
        ("Write cases for the gaps", "ai", ["business-rule & semantic scenarios only", "sees one endpoint slice + confirmed rules", "returns test-case JSON, never 'high' confidence", "≤ 3 rounds: generate → check → measure"], None),
        ("Measure coverage", "eng", ["seven dimensions × every endpoint", "thresholds per dimension", "gap list drives the agent and the guard", "snapshot per suite → trend"], "AI next: explain gaps in plain words"),
        ("Prove every case against the contract", "eng", ["rejects anything the spec does not document", "dedup · priority P1/P2/P3 · per-endpoint cap", "confidence: high (fact) · medium · low", "ONE canonical JSON per case"], None),
     ], ["canonical test cases (JSON)", "coverage matrix + gaps", "positive · negative · boundary · security · business-flow · (R3) Kafka"], []),
    ("Govern &", "approve", [
        ("Review in a queue", "eng", ["filter by endpoint · dimension · confidence", "approve · edit · reject (reason) · add manual", "bulk-approve high confidence only", "optimistic locking — no silent overwrites"], None),
        ("Guard the approval", "eng", ["every P1 decided first", "every dimension at threshold, or a lead accepts the gap", "approved suite freezes; change = next version", "optional publish to Zephyr (P1/P2)"], None),
        ("Audit and learn from every decision", "eng", ["audit event per decision, bulk or single", "decisions become the agents' examples", "roles: QE · QE lead · admin", "teams never see each other (row-level security)"], "AI next: suggest the likely decision"),
     ], ["approved, frozen suite", "audit trail", "agent feedback set", "Zephyr test cases (R2)"], [(1, "suite approval")]),
    ("Build data", "& scripts", [
        ("Build test data", "eng", ["bodies from the spec's examples & limits", "runtime values: ids · dates · unique suffixes", "QA catalog: match by filter, reserve per run", "masking wherever a sensitive field appears"], "AI next: realistic semantic values"),
        ("Map a QE's CSV to fields", "ai", ["reads headers + 5 masked rows", "proposes column → field with confidence", "QE confirms the mapping", "rows become data-driven scenarios"], None),
        ("Generate Karate from templates", "eng", ["six hand-written templates, filled from JSON", "one .feature per endpoint, one Scenario per case", "tags @TC-id @p1 @type", "locked scripts never overwritten"], "AI next: learn the style of your existing suites"),
        ("Write what no template fits · validate", "ai", ["agent writes only the complex scenarios", "parse · static rules · contract check", "mock run against the spec (Prism) · ≤ 2 repairs", "one Git commit per suite — runs pin it"], None),
     ], ["data sets per environment", "Karate project in Git", "helpers & config", "validation status per script"], [(1, "data review")]),
    ("Run &", "collect evidence", [
        ("Pre-flight the environment", "eng", ["freeze windows · concurrency · queue position", "tokens per profile · one safe call · data reserved", "build version captured", "red → stop, one notification"], None),
        ("Run Karate in a Kubernetes Job", "eng", ["one Job per run · N pods = N shards", "clone at the pinned commit · secrets mounted", "retry network/5xx once → flaky; assertions never", "masks every request/response before writing"], None),
        ("Collect results & evidence", "eng", ["one result per case: pass · fail · flaky · blocked", "failure fingerprint — same bug, same hash", "evidence per call, signed links, 90 days", "cleanup ledger: delete what tests created"], None),
     ], ["immutable run record", "results per case", "masked evidence", "flaky & blocked insight"], []),
    ("Close the loop", "& improve", [
        ("Triage failures", "ai", ["signals first: env · data · flaky · drift", "agent classifies the rest: category + reason", "clusters by root cause", "drafts the defect — never files it"], None),
        ("File once, rerun on fix", "eng", ["QE confirms → Jira issue, dedup by fingerprint", "repeat = comment · regression = linked issue", "'ready for QA' webhook → scoped rerun", "result commented back on the ticket"], None),
        ("Report & analyse", "eng", ["run · workflow · portfolio · release readiness", "every number computed", "flaky rate · AI acceptance · cost per API", "executive summary & PDF"], "AI now (R3): narrative summary"),
        ("Keep getting better", "eng", ["gate decisions tune prompts & examples", "golden-set harness gates every AI change", "kill switch: > 30 % rejection → rules only", "spec change → regenerate impacted cases only"], None),
     ], ["triage decisions", "Jira defects verified by rerun", "dashboards & KPIs", "a better suite every cycle"], [(0, "defect review")]),
]
# spine
w(f"<line x1='{SPX}' y1='{LY0-10}' x2='{SPX}' y2='{LY0 + 6*STRIDE - LG + 10}' stroke='{SLATE}' stroke-width='3'/>")
# truth rail
rail_top = LY0 + LH / 2
w(f"<line x1='{RAIL}' y1='{rail_top}' x2='{RAIL}' y2='{LY0 + 5*STRIDE + LH/2}' stroke='{AI}' stroke-width='2' stroke-dasharray='1 5' stroke-linecap='round'/>")
w(f"<text transform='translate({RAIL-16},{LY0 + 3*STRIDE}) rotate(-90)' font-size='9' font-weight='700' fill='{AI_INK}' text-anchor='middle' dominant-baseline='middle' letter-spacing='0.12em' font-family=\"{FONT}\">THE TRUTH RAIL — the model and the canonical case, read and written by every layer</text>")

for li, (t1, t2, blocks, outs, gates) in enumerate(layers):
    y = LY0 + li * STRIDE
    # spine node + layer name
    w(f"<circle cx='{SPX}' cy='{y+LH/2}' r='20' fill='#ffffff' stroke='{INK}' stroke-width='3'/>")
    text(SPX, y + LH / 2 + 1, str(li + 1), size=17, weight="700", anchor="middle")
    text(SPX + 36, y + LH / 2 - 11, t1, size=17, weight="700")
    text(SPX + 36, y + LH / 2 + 11, t2, size=17, weight="700", fill=SLATE)
    # rail tap
    w(f"<circle cx='{RAIL}' cy='{y+LH/2}' r='4' fill='{AI}'/>")
    nb = len(blocks); gap = 16; bw = (CW_ - (nb - 1) * gap) / nb
    for bi, (bt, kind, bullets, nxt) in enumerate(blocks):
        x = CX0 + bi * (bw + gap)
        if kind == "ai":
            rect(x, y, bw, LH, AI_BG, AI, rx=26, sw=1.8, dash="6 4", extra=" filter='url(#sh)'")
            rect(x + bw - 64, y + 10, 52, 18, AI, AI, rx=9); text(x + bw - 38, y + 19, "AI agent", size=9, weight="700", anchor="middle", fill="#ffffff")
            tcol = AI_INK
        elif kind == "hub":
            rect(x, y, bw, LH, "#ffffff", AI, rx=10, sw=2.2, extra=" filter='url(#sh)'")
            hexagon(x + bw - 26, y + 22, 14, AI, AI)
            tcol = AI_INK
        else:
            rect(x, y, bw, LH, "#ffffff", LINE, rx=10, sw=1.5, extra=" filter='url(#sh)'")
            tcol = INK
        text(x + 14, y + 20, bt, size=12.5, weight="700", fill=tcol)
        for k, b in enumerate(bullets):
            text(x + 16, y + 44 + k * 18, "–", size=11, fill=MUTED); text(x + 28, y + 44 + k * 18, b, size=10.3, fill=INK)
        if nxt:
            lab = nxt; pw = len(lab) * 5.6 + 16
            col = AI if lab.startswith("AI now") else NEXT; bg = AI_BG if col == AI else NEXT_BG
            rect(x + bw - pw - 8, y + LH - 24, pw, 17, bg, col, rx=8, sw=1, dash="2 3")
            text(x + bw - pw / 2 - 8, y + LH - 15.5, lab, size=8.8, weight="700", anchor="middle", fill=col)
        if bi < nb - 1:
            arrow([(x + bw + 2, y + LH / 2), (x + bw + gap - 2, y + LH / 2)], width=1.4)
    # gates
    ox = CX0
    for bi, lab in gates:
        pw = len(lab) * 6 + 40
        rect(ox, y + LH + 3, pw, 18, GATE_BG, GATE, rx=9, sw=1.2)
        diamond(ox + 12, y + LH + 12, 5); text(ox + 24, y + LH + 12, "gate: " + lab, size=9.5, weight="700", fill=GATE_INK)
        ox += pw + 8
    if gates: ox += 10
    text(ox, y + LH + 12, "produces", size=9, weight="700", fill=MUTED, ls="0.1em")
    ox += 60
    for o in outs:
        cw = len(o) * 5.9 + 18
        rect(ox, y + LH + 3, cw, 18, PAPER, LINE, rx=9, sw=1)
        text(ox + cw / 2, y + LH + 12, o, size=9.5, anchor="middle", fill=SLATE, weight="600")
        ox += cw + 6
    # layer handoff arrow (first card to next layer)
    if li < 5:
        w(f"<line x1='{SPX}' y1='{y+LH/2+20}' x2='{SPX}' y2='{y+STRIDE+LH/2-20}' stroke='{SLATE}' stroke-width='3'/>")
        arrow([(CX0 + 40, y + LH + OUT_H), (CX0 + 40, y + STRIDE - 2)], width=1.4, dashed=True)
        arrow([(CX0 + CW_ - 40, y + LH + OUT_H), (CX0 + CW_ - 40, y + STRIDE - 2)], width=1.4, dashed=True)

# ------------------------------------------------------------- bottom: flow + loops
BY = LY0 + 6 * STRIDE + 6
text(40, BY + 12, "THE LOOP", size=10, weight="700", fill=MUTED, ls="0.14em")
flow = ["Onboard", "Understand", "Design", "Govern", "Build", "Run", "Close the loop"]
fx, fw = 330, 190
for i, f in enumerate(flow):
    x = fx + i * (fw + 8)
    rect(x, BY, fw, 36, "#ffffff", INK, rx=18, sw=1.6)
    text(x + fw / 2, BY + 18, f, size=12.5, weight="700", anchor="middle", fill=INK)
    if i < 6: arrow([(x + fw + 1, BY + 18), (x + fw + 7, BY + 18)], width=1.4)
def band_loop(i_from, i_to, dy, label):
    x1 = fx + i_from * (fw + 8) + fw / 2; x2 = fx + i_to * (fw + 8) + fw / 2
    w(f"<path d='M{x1},{BY+38} v{dy} H{x2} v-{dy-2}' fill='none' stroke='{AMBER}' stroke-width='1.8' stroke-dasharray='6 4' marker-end='url(#am)'/>")
    text((x1 + x2) / 2, BY + 38 + dy + 11, label, size=9.5, anchor="middle", weight="600", fill=AMBER_INK)
band_loop(6, 5, 12, "a fixed defect → scoped rerun, result back on the ticket")
band_loop(6, 1, 40, "a new spec version → regenerate impacted endpoints only · every gate decision becomes an agent example")
text(40, BY + 48, "six stages", size=10, fill=MUTED); text(40, BY + 64, "five human gates", size=10, fill=MUTED); text(40, BY + 80, "two loops", size=10, fill=MUTED); text(40, BY + 96, "one truth", size=10, fill=MUTED, weight="700")
w("</svg>")
pass
open("out/concept-capability-map.svg", "w").write("\n".join(out))
print("ok", BY + 110)
