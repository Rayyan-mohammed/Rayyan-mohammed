"""Render a GitHub activity panel from the GitHub GraphQL API, with no third-party stats service.

    GITHUB_TOKEN=... python scripts/activity.py <login> <out.svg>

Runs in .github/workflows/profile-assets.yml and is published to the `output`
branch. If the API call fails, the script exits non-zero and the previously
published SVG stays in place, so the README never shows a broken image.

Raw commit counts are deliberately left out. Automated commits (deploy bots,
URL rotations) inflate them, and they say little about the work itself.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_assets import (CYAN, DIM, EMERALD, EMERALD_SOFT, LINE, MUTED, PAD, PANEL, TEXT, W,  # noqa: E402
                          defs, frame, svg, t)

# The seven flagship repositories (canonical upstreams for team projects).
FLAGSHIPS = [
    ("Angshuman1211", "Argus-Spot_Resilient_ML_Training_Orchestrator"),
    ("Angshuman1211", "Obscuron"),
    ("Rayyan-mohammed", "aarogya-lens"),
    ("Angshuman1211", "Doppel"),
    ("Angshuman1211", "CALIBER"),
    ("Angshuman1211", "DermaAegis-SmartHorizon"),
    ("Rayyan-mohammed", "Pharma-Flow-Pro"),
]

LANG = "languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } }"
QUERY = (
    "query($login: String!) {"
    " user(login: $login) {"
    " contributionsCollection { totalPullRequestContributions totalRepositoriesWithContributedCommits }"
    " repositories(ownerAffiliations: OWNER, privacy: PUBLIC) { totalCount } }"
    + "".join(f' r{i}: repository(owner: "{o}", name: "{n}") {{ {LANG} }}' for i, (o, n) in enumerate(FLAGSHIPS))
    + " }"
)

# Markup and notebooks dominate byte counts without reflecting engineering work.
EXCLUDE = {"HTML", "CSS", "SCSS", "Jupyter Notebook", "TeX", "Makefile", "Batchfile", "Procfile", "Dockerfile"}
BAR_COLORS = [EMERALD, CYAN, "#5EEAD4", "#7DD3FC", "#94A3B8", "#475569"]


def fetch(login: str, token: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-activity-panel"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    return payload["data"]


def render(data: dict) -> str:
    user = data["user"]
    cc = user["contributionsCollection"]
    langs: dict[str, int] = {}
    for i in range(len(FLAGSHIPS)):
        repo = data.get(f"r{i}")
        if not repo:  # renamed or made private: skip rather than fail
            continue
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            if name not in EXCLUDE:
                langs[name] = langs.get(name, 0) + e["size"]
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:5]
    other = total - sum(v for _, v in top)
    if other > 0:
        top.append(("Other", other))

    h = 246
    b = [defs(), frame(h)]
    b.append(t(PAD, 50, "GITHUB ACTIVITY  ·  LAST 12 MONTHS", 14, EMERALD_SOFT, mono=True, weight=600, spacing=1.5))
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    b.append(t(W - PAD, 50, f"generated {stamp} · GitHub GraphQL API", 13, DIM, mono=True, anchor="end"))

    stats = [
        (cc["totalRepositoriesWithContributedCommits"], "repositories contributed to"),
        (cc["totalPullRequestContributions"], "pull requests opened"),
        (user["repositories"]["totalCount"], "public repositories"),
    ]
    mw = (W - 2 * PAD) / len(stats)
    for i, (v, label) in enumerate(stats):
        x = PAD + i * mw
        if i:
            b.append(f'<line x1="{x - 18:.0f}" y1="78" x2="{x - 18:.0f}" y2="136" stroke="{LINE}"/>')
        b.append(t(x, 112, f"{v:,}", 34, EMERALD_SOFT if i == 0 else TEXT, weight=650))
        b.append(t(x, 136, label, 14, MUTED, mono=True))

    by = 176
    b.append(t(PAD, by - 10, "LANGUAGES ACROSS THE SEVEN FLAGSHIP REPOSITORIES · BY CODE SIZE · MARKUP EXCLUDED",
               12, DIM, mono=True, spacing=0.4))
    bw = W - 2 * PAD
    b.append(f'<rect x="{PAD}" y="{by}" width="{bw}" height="10" rx="5" fill="{PANEL}"/>')
    x = PAD
    lx = PAD
    for i, (name, size) in enumerate(top):
        w = bw * size / total
        color = BAR_COLORS[i % len(BAR_COLORS)]
        b.append(f'<rect x="{x:.1f}" y="{by}" width="{max(w - 2, 1):.1f}" height="10" rx="3" fill="{color}"/>')
        x += w
        label = f"{name} {100 * size / total:.0f}%"
        b.append(f'<circle cx="{lx + 5}" cy="{by + 40}" r="5" fill="{color}"/>')
        b.append(t(lx + 16, by + 45, label, 14, MUTED, mono=True))
        lx += len(label) * 14 * 0.61 + 44
    desc = ("GitHub activity over the last 12 months: " + "; ".join(f"{v} {l}" for v, l in stats)
            + ". Languages across the seven flagship repositories: " + ", ".join(f"{n} {100 * s / total:.0f}%" for n, s in top) + ".")
    return svg(W, h, "GitHub activity", desc, "".join(b))


def main():
    login, out = sys.argv[1], Path(sys.argv[2])
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(fetch(login, token)), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
