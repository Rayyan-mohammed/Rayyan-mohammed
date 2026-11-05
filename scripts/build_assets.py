"""Generate every static SVG used by the profile README.

One design system, one source of truth: edit the data below and re-run

    python scripts/build_assets.py

Every number shown in a card or diagram must be traceable to a committed
result file in the project's own repository (see the comments next to each).
The script fails if any text is estimated to overflow its container.
"""

from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

# ---------------------------------------------------------------- tokens
BG = "#0B0E12"        # near-black canvas
PANEL = "#10151B"     # graphite panel
PANEL_2 = "#141A21"   # raised graphite
LINE = "#232B35"      # hairlines
TEXT = "#E6EDF3"
MUTED = "#8E9AA8"
DIM = "#5C6774"
EMERALD = "#10B981"
EMERALD_SOFT = "#34D399"
CYAN = "#22D3EE"

SANS = "ui-sans-serif, -apple-system, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"

W = 1200
PAD = 36

overflow_errors: list[str] = []


def text_width(s: str, size: float, mono: bool = False, bold: bool = False) -> float:
    """Conservative width estimate for system fonts (no font files are embedded)."""
    factor = 0.61 if mono else (0.56 if bold else 0.53)
    return len(s) * size * factor


def check(s: str, size: float, max_w: float, where: str, mono=False, bold=False):
    w = text_width(s, size, mono, bold)
    if w > max_w:
        overflow_errors.append(f"{where}: '{s}' ~{w:.0f}px > {max_w:.0f}px")


def t(x, y, s, size=14, fill=TEXT, mono=False, weight=400, anchor="start", spacing=0, opacity=1):
    fam = MONO if mono else SANS
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    op = f' opacity="{opacity}"' if opacity != 1 else ""
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}{op}>{escape(s)}</text>')


def svg(width, height, title, desc, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">'
        f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
        f'{body}</svg>\n'
    )


def defs():
    return (
        '<defs>'
        f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker>'
        f'<marker id="arrowE" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{EMERALD}"/></marker>'
        f'<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
        f'<circle cx="1" cy="1" r="1" fill="{LINE}"/></pattern>'
        f'<radialGradient id="glow" cx="85%" cy="0%" r="70%">'
        f'<stop offset="0%" stop-color="{EMERALD}" stop-opacity="0.16"/>'
        f'<stop offset="100%" stop-color="{EMERALD}" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="rule" x1="0" x2="1" y1="0" y2="0">'
        f'<stop offset="0%" stop-color="{EMERALD}"/><stop offset="35%" stop-color="{CYAN}" stop-opacity="0.6"/>'
        f'<stop offset="100%" stop-color="{LINE}" stop-opacity="0"/></linearGradient>'
        '</defs>'
    )


def frame(height, glow=False):
    g = f'<rect width="{W}" height="{height}" rx="16" fill="url(#glow)"/>' if glow else ""
    return (f'<rect width="{W}" height="{height}" rx="16" fill="{BG}"/>'
            f'<rect width="{W}" height="{height}" rx="16" fill="url(#dots)" opacity="0.55"/>{g}'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{height-1}" rx="15.5" fill="none" stroke="{LINE}"/>')


def chip(x_right, y, label, color=EMERALD):
    w = text_width(label, 13, mono=True) + 30
    x = x_right - w
    return (f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="30" rx="15" fill="{PANEL_2}" stroke="{color}" stroke-opacity="0.55"/>'
            f'<circle cx="{x+15:.0f}" cy="{y+15}" r="3.5" fill="{color}"/>'
            + t(x + 25, y + 20, label, 13, MUTED, mono=True)), w


# ---------------------------------------------------------------- hero
def hero():
    h = 380
    b = [defs(), frame(h, glow=True)]
    b.append(t(PAD + 8, 72, "INTELLIGENCE, ENGINEERED.", 15, EMERALD_SOFT, mono=True, weight=600, spacing=4))
    b.append(t(PAD + 4, 150, "MD RAYYAN", 68, TEXT, weight=700, spacing=3))
    b.append(t(PAD + 8, 198, "AI/ML Engineer  ·  Applied Research  ·  ML Systems", 25, MUTED))
    b.append(t(PAD + 8, 240, "Models, the evidence that they work, and the infrastructure that keeps them running.",
               18, TEXT, opacity=0.86))
    check("Models, the evidence that they work, and the infrastructure that keeps them running.", 18, 820, "hero")

    # right: reliability-diagram motif (calibration as a design principle)
    fx, fy, fw, fh = 880, 52, 270, 190
    b.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="12" fill="{PANEL}" stroke="{LINE}"/>')
    ox, oy, s = fx + 34, fy + fh - 34, 128
    b.append(f'<path d="M{ox},{oy-s} L{ox},{oy} L{ox+s*1.55:.0f},{oy}" fill="none" stroke="{DIM}" stroke-width="1"/>')
    b.append(f'<path d="M{ox},{oy} L{ox+s*1.55:.0f},{oy-s}" stroke="{DIM}" stroke-dasharray="4 5" stroke-width="1"/>')
    pts = [(0, 0), (0.12, 0.09), (0.25, 0.21), (0.38, 0.36), (0.5, 0.47), (0.62, 0.61), (0.75, 0.72), (0.88, 0.86), (1, 0.97)]
    path = " ".join(f"{ox + p*s*1.55:.1f},{oy - q*s:.1f}" for p, q in pts)
    b.append(f'<polyline points="{path}" fill="none" stroke="{EMERALD}" stroke-width="2.2" stroke-linejoin="round"/>')
    for p, q in pts[1:-1]:
        b.append(f'<circle cx="{ox + p*s*1.55:.1f}" cy="{oy - q*s:.1f}" r="3" fill="{BG}" stroke="{CYAN}" stroke-width="1.5"/>')
    b.append(t(fx + 18, fy + 28, "fig. 0", 13, DIM, mono=True))
    b.append(t(fx + fw - 18, fy + 28, "claims ≈ evidence", 13, MUTED, mono=True, anchor="end"))

    # bottom: lifecycle rail
    stages = ["PROBLEM", "DATA", "MODEL", "EVALUATION", "ARCHITECTURE", "DEPLOYMENT", "MONITORING", "ITERATE"]
    y = 316
    x0, x1 = PAD + 8, W - PAD - 8
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="url(#rule)" stroke-width="1.5"/>')
    step = (x1 - x0) / (len(stages) - 1)
    for i, s_ in enumerate(stages):
        cx = x0 + i * step
        key = s_ in ("EVALUATION", "MONITORING")
        b.append(f'<circle cx="{cx:.0f}" cy="{y}" r="{5 if key else 4}" fill="{BG}" '
                 f'stroke="{EMERALD if key else MUTED}" stroke-width="{2 if key else 1.4}"/>')
        anchor = "start" if i == 0 else ("end" if i == len(stages) - 1 else "middle")
        b.append(t(cx, y + 32, s_, 13, EMERALD_SOFT if key else MUTED, mono=True, anchor=anchor, spacing=0.8))
    b.append(t(x1, y - 18, "the full loop, not just the notebook", 13, DIM, mono=True, anchor="end"))
    return svg(W, h, "MD Rayyan, AI/ML Engineer, Applied Research, ML Systems",
               "Banner reading 'Intelligence, engineered.' with the ML lifecycle from problem to iteration, "
               "evaluation and monitoring highlighted, and a reliability-diagram motif.", "".join(b))


def divider():
    h = 18
    body = (defs() + f'<line x1="0" y1="9" x2="{W}" y2="9" stroke="url(#rule)" stroke-width="1"/>'
            f'<rect x="0" y="6" width="44" height="6" rx="3" fill="{EMERALD}"/>')
    return svg(W, h, "Section divider", "A thin emerald-to-graphite rule.", body)


# ---------------------------------------------------------------- project cover plates
def cover(p, featured):
    h = 272 if featured else 208
    b = [defs(), frame(h, glow=featured)]
    b.append(t(PAD, 54, p["index"], 15, EMERALD_SOFT, mono=True, weight=700, spacing=1))
    b.append(t(PAD + 38, 54, p["kind"], 14, MUTED, mono=True, spacing=0.6))
    c, cw = chip(W - PAD, 34, p["role"])
    b.append(c)
    check(p["kind"], 14, W - 2 * PAD - cw - 70, p["name"] + " kind", mono=True)
    title_size = 42 if featured else 32
    ty = 108 if featured else 96
    b.append(t(PAD - 2, ty, p["name"], title_size, TEXT, weight=700, spacing=0.5))
    tag_size = 19 if featured else 17
    b.append(t(PAD, ty + (34 if featured else 28), p["tagline"], tag_size, MUTED))
    check(p["tagline"], tag_size, W - 2 * PAD, p["name"] + " tagline")

    metrics = p["metrics"]
    my = 192 if featured else 162
    mw = (W - 2 * PAD) / len(metrics)
    for i, (val, lab) in enumerate(metrics):
        mx = PAD + i * mw
        if i:
            b.append(f'<line x1="{mx - 18:.0f}" y1="{my - 30}" x2="{mx - 18:.0f}" y2="{my + 24}" stroke="{LINE}"/>')
        vs = 32 if featured else 25
        b.append(t(mx, my, val, vs, EMERALD_SOFT if i == 0 else TEXT, weight=650))
        b.append(t(mx, my + (28 if featured else 24), lab, 14, MUTED, mono=True))
        check(val, vs, mw - 30, p["name"] + " metric", bold=True)
        check(lab, 14, mw - 30, p["name"] + " metric label", mono=True)
    return svg(W, h, f'{p["name"]}: {p["tagline"]}',
               f'{p["name"]} project card. Role: {p["role"].lower()}. Key results: '
               + "; ".join(f"{v} {l}" for v, l in metrics) + ".", "".join(b))


# ---------------------------------------------------------------- architecture diagrams
def architecture(a):
    cols = a["columns"]
    n = len(cols)
    gap = 28
    colw = (W - 2 * PAD - gap * (n - 1)) / n
    box_h = 68
    vgap = 14
    max_boxes = max(len(c["boxes"]) for c in cols)
    top = 104
    stack_h = max_boxes * box_h + (max_boxes - 1) * vgap
    band_y = top + 34 + stack_h + 36
    h = band_y + (74 if a.get("band") else 0) + 26
    b = [defs(), frame(h)]
    b.append(t(PAD, 50, a["label"], 14, EMERALD_SOFT, mono=True, weight=600, spacing=1.5))
    b.append(t(PAD, 78, a["title"], 21, TEXT, weight=600))
    check(a["title"], 21, W - 2 * PAD, a["label"] + " title", bold=True)
    if a.get("note"):
        b.append(t(W - PAD, 50, a["note"], 13, DIM, mono=True, anchor="end"))

    centers = []
    for i, c in enumerate(cols):
        x = PAD + i * (colw + gap)
        b.append(t(x, top + 14, f'{i + 1:02d}  {c["head"]}', 13, MUTED, mono=True, spacing=0.8))
        boxes = c["boxes"]
        bh_total = len(boxes) * box_h + (len(boxes) - 1) * vgap
        y0 = top + 34 + (stack_h - bh_total) / 2
        for j, bx in enumerate(boxes):
            y = y0 + j * (box_h + vgap)
            hl = bx.get("hl", False)
            b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{colw:.1f}" height="{box_h}" rx="10" '
                     f'fill="{PANEL_2 if hl else PANEL}" stroke="{EMERALD if hl else LINE}" '
                     f'stroke-opacity="{0.8 if hl else 1}"/>')
            if hl:
                b.append(f'<rect x="{x:.1f}" y="{y + 14:.1f}" width="3" height="{box_h - 28}" rx="1.5" fill="{EMERALD}"/>')
            b.append(t(x + 13, y + 28, bx["t"], 16, TEXT, weight=600))
            b.append(t(x + 13, y + 51, bx.get("s", ""), 13, MUTED, mono=True))
            check(bx["t"], 16, colw - 20, a["label"] + " box", bold=True)
            check(bx.get("s", ""), 13, colw - 20, a["label"] + " box sub", mono=True)
        centers.append((x, x + colw, top + 34 + stack_h / 2))
    for (x0, x1, cy), (nx0, _, _) in zip(centers, centers[1:]):
        b.append(f'<line x1="{x1 + 4:.1f}" y1="{cy:.1f}" x2="{nx0 - 4:.1f}" y2="{cy:.1f}" '
                 f'stroke="{DIM}" stroke-width="1.4" marker-end="url(#arrow)"/>')
    if a.get("loop"):  # feedback arc under the stacks, from last column back to a target column
        src = centers[-1]
        dst = centers[a["loop"]["to"]]
        ly = top + 34 + stack_h + 20
        sx, dx = (src[0] + src[1]) / 2, (dst[0] + dst[1]) / 2
        b.append(f'<path d="M{sx:.0f},{top + 34 + stack_h + 2} L{sx:.0f},{ly} L{dx:.0f},{ly} L{dx:.0f},{top + 34 + stack_h + 4}" '
                 f'fill="none" stroke="{EMERALD}" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#arrowE)"/>')
        b.append(t((sx + dx) / 2, ly - 7, a["loop"]["label"], 13, EMERALD_SOFT, mono=True, anchor="middle"))
    if a.get("band"):
        head, body_ = a["band"]
        b.append(f'<rect x="{PAD}" y="{band_y}" width="{W - 2 * PAD}" height="56" rx="10" fill="{PANEL}" '
                 f'stroke="{LINE}" stroke-dasharray="4 4"/>')
        b.append(t(PAD + 16, band_y + 34, head, 13, CYAN, mono=True, weight=600, spacing=0.8))
        hw = text_width(head, 13, mono=True) + 34
        b.append(t(PAD + hw, band_y + 34, body_, 15, MUTED))
        check(body_, 15, W - 2 * PAD - hw - 16, a["label"] + " band")
    desc = (f'{a["title"]}. Stages: ' + "; ".join(
        f'{c["head"].lower()}: ' + ", ".join(bx["t"] for bx in c["boxes"]) for c in cols) + ".")
    if a.get("band"):
        desc += f' {a["band"][0].title()}: {a["band"][1]}'
    return svg(W, h, f'{a["label"]} architecture', desc, "".join(b))


# ---------------------------------------------------------------- content (verified facts only)
PROJECTS = {
    # Argus: docs/objective1_result.md (~75 s), docs/wide_model_result.md §7b (152 reclaims),
    # docs/trace_benchmark_result.md (1.14x vs 1.34x at 300 s checkpoints)
    "argus": dict(index="01", name="Argus", kind="ML INFRASTRUCTURE  ·  KUBERNETES  ·  AWS EKS",
                  role="CO-AUTHOR  ·  ML LAYER",
                  tagline="Keeps PyTorch training alive across EC2 Spot reclaims: predict, checkpoint, migrate, resume.",
                  metrics=[("~75 s", "resume after a real Spot drain on EKS"),
                           ("152", "real reclaims labelled by a sensor fleet"),
                           ("1.14× vs 1.34×", "slowdown vs Young-Daly, 300 s ckpt")]),
    # Obscuron: README results 1-2, results/ held-out-family eval
    "obscuron": dict(index="02", name="Obscuron", kind="APPLIED RESEARCH  ·  PROTEIN LANGUAGE MODELS",
                     role="CO-AUTHOR  ·  IMPLEMENTATION",
                     tagline="Calibrated novelty scores for uncharacterised microbial proteins, validated retrospectively.",
                     metrics=[("0.962", "held-out-family AUROC, 903 families"),
                              ("1.34M", "proteins scanned across 502 genomes"),
                              ("4,138", "dark-then-characterised positives")]),
    # BharatHealth: aarogya-lens README results 1-3
    "bharathealth": dict(index="03", name="BharatHealth Analyst", kind="AGENTIC AI  ·  HEALTH ANALYTICS",
                         role="SOLE AUTHOR",
                         tagline="A tool-using LLM analyst over India's district health survey, with its own benchmark.",
                         metrics=[("200", "benchmark Qs, computed ground truth"),
                                  ("71.1%  /  5.0%", "exact-answer accuracy / hallucination"),
                                  ("706 × 448", "districts × columns, DVC-reproducible")]),
    # Doppel: docs/final_evaluation_result.md
    "doppel": dict(index="04", name="Doppel", kind="PRIVACY EVALUATION  ·  SYNTHETIC EHR",
                   role="TEAM OF 4  ·  EVALUATION TRACK",
                   tagline="One protocol for fidelity, utility and privacy of synthetic health-record generators.",
                   metrics=[("36%", "training patients exposed at 1% FPR (diffusion)"),
                            ("180", "runs: 9 generator arms × 20 seeds")]),
    # CALIBER: README 'What exists today' (CT coverage 0.693 at 30 views; 0.902-0.923 restored; 836 tests)
    "caliber": dict(index="05", name="CALIBER", kind="CONFORMAL PREDICTION  ·  MEDICAL IMAGING",
                    role="TEAM  ·  THEORY TRACK",
                    tagline="Reliability certificates for generative image reconstruction when the scanner changes.",
                    metrics=[("0.69 → 0.90+", "CT coverage: naive vs group-conditional"),
                             ("2", "modalities: accelerated MRI and CT")]),
    # DermaAegis: models/eval_metadata_stratified_on_grouped.json (tta_test_accuracy 0.8575)
    "dermaaegis": dict(index="06", name="DermaAegis", kind="COMPUTER VISION  ·  EXPLAINABILITY",
                       role="TEAM  ·  CONTAINERISATION",
                       tagline="Dermoscopic lesion classification with Grad-CAM and uncertainty. A research prototype.",
                       metrics=[("85.75%", "test accuracy, TTA ×4, grouped split"),
                                ("7", "HAM10000 lesion classes")]),
    # PharmaFlow: database/medical_management.sql (31 tables), app/init.php, public/login.php
    "pharmaflow": dict(index="07", name="PharmaFlow Pro", kind="SOFTWARE SYSTEMS  ·  SECURITY  ·  AWS",
                       role="SOLE AUTHOR",
                       tagline="Pharmacy ERP with role-based access, audit logging and inventory controls.",
                       metrics=[("31", "tables in the relational schema"),
                                ("3 roles", "+ per-action permission matrix")]),
}

ARCH = {
    "argus": dict(label="ARGUS", title="Two interruption paths, one recovery flow",
                  note="operator signals · pod owns the flush",
                  columns=[
                      dict(head="SIGNAL", boxes=[dict(t="Spot price feed", s="Lambda → S3, 5-min"),
                                                 dict(t="Capacity signal", s="placement score + age")]),
                      dict(head="PREDICT", boxes=[dict(t="Risk service", s="FastAPI /reclaim_risk", hl=True),
                                                  dict(t="Risk models", s="XGBoost · logistic", hl=True)]),
                      dict(head="DECIDE", boxes=[dict(t="kopf operator", s="SpotResilientJob CRD"),
                                                 dict(t="Risk > threshold", s="10% alarm budget")]),
                      dict(head="CHECKPOINT", boxes=[dict(t="Flush handshake", s="trigger → ack, S3"),
                                                     dict(t="S3 checkpoint", s="atomic upload")]),
                      dict(head="RECOVER", boxes=[dict(t="Cordon + recreate", s="healthy node"),
                                                  dict(t="Resume epoch N", s="~75 s on real EKS")]),
                  ],
                  loop=dict(to=2, label="15-min cooldown before the next migration"),
                  band=("REACTIVE PATH", "AWS Node Termination Handler → drain → SIGTERM handler checkpoints → same recovery. "
                                         "Prometheus + Grafana observe both.")),
    "obscuron": dict(label="OBSCURON", title="Retrospective validation: freeze the past, grade against the future",
                     note="metrics frozen before any scorer ran",
                     columns=[
                         dict(head="SNAPSHOTS", boxes=[dict(t="GTDB R207 · Pfam 35", s="T0, frozen reference"),
                                                       dict(t="Pfam 37 proxy", s="T1, later knowledge")]),
                         dict(head="LABEL", boxes=[dict(t="Snapshot diffing", s="1.34M proteins", hl=True),
                                                   dict(t="4,138 positives", s="dark T0 → known T1", hl=True)]),
                         dict(head="EMBED", boxes=[dict(t="ESM-2 650M", s="leakage-clean arm", hl=True),
                                                   dict(t="Genos-m 4.7B", s="leakage-controlled"),
                                                   dict(t="ProstT5", s="structure-aware")]),
                         dict(head="SCORE", boxes=[dict(t="L1 kNN + GPD", s="EVT p-value", hl=True),
                                                   dict(t="L3 neg. selection", s="self / non-self"),
                                                   dict(t="L2 · L4 · L5", s="struct · conv · coding")]),
                         dict(head="EVALUATE", boxes=[dict(t="Held-out family", s="AUROC 0.962"),
                                                      dict(t="Calibration", s="false-flag rate ≈ α")]),
                     ],
                     band=("LEAKAGE CONTROL", "Pretraining cut-offs checked against the T0→T1 window. "
                                              "Raw data streamed, never warehoused.")),
    "bharathealth": dict(label="BHARATHEALTH ANALYST", title="Question → planned tool calls → grounded answer → measured",
                         note="sole author · end to end",
                         columns=[
                             dict(head="DATA", boxes=[dict(t="NFHS-5 + NFHS-4", s="706 × 448 columns"),
                                                      dict(t="DVC pipeline", s="byte-identical repro")]),
                             dict(head="INDEX", boxes=[dict(t="Parquet + schema", s="imputed cells flagged"),
                                                       dict(t="ChromaDB", s="MiniLM embeddings")]),
                             dict(head="AGENT", boxes=[dict(t="LangGraph ReAct", s="plans tool chains", hl=True),
                                                       dict(t="7 tools", s="search·pandas·SQL·chart", hl=True),
                                                       dict(t="Sandboxed exec", s="whitelisted pandas")]),
                             dict(head="SERVE", boxes=[dict(t="FastAPI", s="11 endpoints, limits"),
                                                       dict(t="Static web app", s="Ask·Explore·Correlate")]),
                             dict(head="EVALUATE", boxes=[dict(t="200-Q benchmark", s="computed ground truth", hl=True),
                                                          dict(t="EA 71.1% · HR 5%", s="5 metrics, resumable")]),
                         ],
                         band=("OPS", "Watchdog keeps the API and Cloudflare tunnel alive. "
                                      "Explore runs offline from data baked into the page.")),
    "doppel": dict(label="DOPPEL", title="Generators are graded on one dataset, one protocol, one environment",
                   note="my track: 03 + 04",
                   columns=[
                       dict(head="DATA", boxes=[dict(t="MIMIC-III Demo", s="129 admissions"),
                                                dict(t="Patient split", s="94 train · 35 holdout")]),
                       dict(head="GENERATE", boxes=[dict(t="Shared codec", s="110-col frame"),
                                                    dict(t="4 families", s="copula·GAN·VAE·diff")]),
                       dict(head="EVALUATE", boxes=[dict(t="Fidelity", s="JSD · corr · KS", hl=True),
                                                    dict(t="Utility", s="train syn, test real", hl=True),
                                                    dict(t="Privacy", s="shadow-model MIA", hl=True)]),
                       dict(head="CALIBRATE", boxes=[dict(t="Attack controls", s="ceiling · floor", hl=True),
                                                     dict(t="Worst-of-3", s="privacy score", hl=True)]),
                       dict(head="DECIDE", boxes=[dict(t="Pareto frontier", s="bootstrap sensitivity"),
                                                  dict(t="React dashboard", s="score your own file")]),
                   ],
                   band=("SCALE", "180 runs: 9 arms × 20 seeds. Docker images and Kubernetes Jobs exist; "
                                  "stages are launched manually.")),
    "caliber": dict(label="CALIBER", title="Solver-agnostic audit layer over pretrained reconstruction priors",
                    note="my track: 05",
                    columns=[
                        dict(head="OPERATORS", boxes=[dict(t="Operator registry", s="MRI masks · CT views"),
                                                      dict(t="Range / null space", s="exact adjoints")]),
                        dict(head="RECONSTRUCT", boxes=[dict(t="Posterior samplers", s="DPS·DDNM·FlowDPS"),
                                                        dict(t="Pretrained priors", s="one interface")]),
                        dict(head="SCORE", boxes=[dict(t="Operator-aware", s="per-region score"),
                                                  dict(t="Score bank", s="MRI + CT, cached")]),
                        dict(head="CALIBRATE", boxes=[dict(t="Naive transfer", s="breaks under shift"),
                                                      dict(t="Group-conditional", s="restores nominal")]),
                        dict(head="BOUND", boxes=[dict(t="Coverage-gap bound", s="Kolmogorov → d_op", hl=True),
                                                  dict(t="Numerical checks", s="synthetic operators", hl=True)]),
                    ],
                    band=("SCOPE", "Exact guarantee only for discrete known operators; "
                                   "continuous shift gets a stated gap bound, not coverage.")),
    "dermaaegis": dict(label="DERMAAEGIS", title="Image in, prediction plus evidence out",
                       note="research prototype · not a diagnostic device",
                       columns=[
                           dict(head="INPUT", boxes=[dict(t="Dermoscopic image", s="HAM10000, 7 classes")]),
                           dict(head="PREPROCESS", boxes=[dict(t="Resize 300×300", s="augment, grouped split")]),
                           dict(head="INFER", boxes=[dict(t="EfficientNetB3", s="ImageNet transfer"),
                                                     dict(t="TTA ×4 · MC dropout", s="uncertainty")]),
                           dict(head="EXPLAIN", boxes=[dict(t="Grad-CAM overlay", s="input-gradient map"),
                                                       dict(t="Fitzpatrick check", s="skin-tone bias")]),
                           dict(head="SERVE", boxes=[dict(t="FastAPI", s="inference API"),
                                                     dict(t="Docker Compose", s="API + UI", hl=True)]),
                       ],
                       band=("LIMITS", "85.75% test accuracy (TTA). Weak recall on rare classes (akiec 0.36). "
                                       "Not clinically validated.")),
    "pharmaflow": dict(label="PHARMAFLOW PRO", title="Roles → authentication → business workflows → database → audit controls",
                       note="sole author",
                       columns=[
                           dict(head="ROLES", boxes=[dict(t="Administrator", s="users · settings"),
                                                     dict(t="Pharmacist", s="sell · approve returns"),
                                                     dict(t="Staff", s="day-to-day sales")]),
                           dict(head="AUTH", boxes=[dict(t="Login throttling", s="15-min lockout", hl=True),
                                                    dict(t="Permission matrix", s="per-action grants", hl=True)]),
                           dict(head="WORKFLOWS", boxes=[dict(t="Sales + returns", s="invoices, held carts"),
                                                         dict(t="Purchases", s="suppliers, payables"),
                                                         dict(t="Prescriptions", s="status logs")]),
                           dict(head="DATA", boxes=[dict(t="MySQL · 31 tables", s="PDO prepared stmts"),
                                                    dict(t="Batches + expiry", s="stock transfers")]),
                           dict(head="CONTROL", boxes=[dict(t="Activity log", s="audit trail", hl=True),
                                                       dict(t="Reorder rules", s="stock ≤ reorder level"),
                                                       dict(t="Backups", s="run metadata")]),
                       ],
                       band=("SECURITY", "CSRF tokens checked with hash_equals; session regenerated on login. "
                                         "Deployed on Elastic Beanstalk + RDS.")),
}

FEATURED = {"argus", "obscuron", "bharathealth"}


def main():
    OUT.mkdir(exist_ok=True)
    files = {"hero.svg": hero(), "divider.svg": divider()}
    for key, p in PROJECTS.items():
        files[f"card-{key}.svg"] = cover(p, key in FEATURED)
        files[f"arch-{key}.svg"] = architecture(ARCH[key])
    if overflow_errors:
        print("Text overflow detected:\n  " + "\n  ".join(overflow_errors), file=sys.stderr)
        sys.exit(1)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"{name:28s} {len(content.encode()):>7,d} bytes")


if __name__ == "__main__":
    main()
