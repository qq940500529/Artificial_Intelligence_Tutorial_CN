"""
animate_geometric.py — Animated GIF: Geometric Sequence Growth, Decay & Partial Sums

Dependencies: Python 3.10+, matplotlib>=3.6, numpy>=1.23, Pillow>=9.0
Usage:        python code/animate_geometric.py
Output:       ../assets/geometric_anim.gif (relative to this script)
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# ── Font & style ──────────────────────────────────────────────────────────────
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── Output path (based on script location) ────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(ASSETS_DIR, "geometric_anim.gif")

# ── Sequence parameters ──────────────────────────────────────────────────────
# Left subplot
N_LEFT = 15
n_left = np.arange(1, N_LEFT + 1)
growth = 1.0 * 1.5 ** (n_left - 1)          # a_n = 1 * 1.5^(n-1)
decay = 50.0 * 0.7 ** (n_left - 1)           # b_n = 50 * 0.7^(n-1)
linear = 5.0 * n_left                         # c_n = 5n

# Right subplot
N_RIGHT = 30
n_right = np.arange(1, N_RIGHT + 1)
qs = [0.5, 0.8, 0.95]
a1 = 1.0
partial_sums = {}
s_inf = {}
for q in qs:
    terms = a1 * q ** (n_right - 1)
    partial_sums[q] = np.cumsum(terms)
    s_inf[q] = a1 / (1.0 - q)

colors_right = {0.5: "#2ca02c", 0.8: "#1f77b4", 0.95: "#ff7f0e"}

# ── Frame generation ─────────────────────────────────────────────────────────
TOTAL_FRAMES = 30
frames = []

for frame_idx in range(TOTAL_FRAMES):
    # How many points to reveal per subplot
    k_left = max(1, int(np.ceil((frame_idx + 1) / TOTAL_FRAMES * N_LEFT)))
    k_right = max(1, int(np.ceil((frame_idx + 1) / TOTAL_FRAMES * N_RIGHT)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=100,
                                   facecolor="white")

    # ── Left subplot: Growth vs Decay ─────────────────────────────────────
    # Full linear reference (gray dashed, always visible)
    ax1.plot(n_left, linear, "--", color="gray", linewidth=1.2,
             label="Linear $5n$", zorder=1)

    # Revealed growth
    ax1.plot(n_left[:k_left], growth[:k_left], "-o", color="#1f77b4",
             markersize=5, linewidth=1.5, label="$q=1.5$ (growth)", zorder=3)
    # Revealed decay
    ax1.plot(n_left[:k_left], decay[:k_left], "-o", color="#d62728",
             markersize=5, linewidth=1.5, label="$q=0.7$ (decay)", zorder=3)

    ax1.set_xlim(0.5, N_LEFT + 0.5)
    y_max_left = max(growth.max(), linear.max()) * 1.08
    ax1.set_ylim(-2, y_max_left)
    ax1.set_xlabel("$n$ (term index)", fontsize=11)
    ax1.set_ylabel("Value", fontsize=11)
    ax1.set_title("Geometric Sequences: Growth vs Decay", fontsize=12,
                  fontweight="bold")
    ax1.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax1.grid(True, alpha=0.3)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # ── Right subplot: Partial sums ───────────────────────────────────────
    for q in qs:
        color = colors_right[q]
        # Horizontal asymptote (always visible)
        ax2.axhline(y=s_inf[q], color=color, linestyle="--", linewidth=1,
                     alpha=0.5)
        # Revealed partial sums
        label = rf"$q={q} \to S_\infty={s_inf[q]:.0f}$"
        ax2.plot(n_right[:k_right], partial_sums[q][:k_right], "-o",
                 color=color, markersize=3.5, linewidth=1.4, label=label,
                 zorder=3)

    ax2.set_xlim(0.5, N_RIGHT + 0.5)
    ax2.set_ylim(-0.5, s_inf[0.95] * 1.15)
    ax2.set_xlabel("$n$", fontsize=11)
    ax2.set_ylabel("$S_n$", fontsize=11)
    ax2.set_title(r"Partial Sums: Convergence to $S_\infty$", fontsize=12,
                  fontweight="bold")
    ax2.legend(loc="lower right", fontsize=9, framealpha=0.9)
    ax2.grid(True, alpha=0.3)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    fig.tight_layout(pad=1.5)

    # Render frame to PIL Image
    buf = BytesIO()
    fig.savefig(buf, format="png", facecolor="white", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    frames.append(Image.open(buf).copy())
    buf.close()

# ── Save GIF ──────────────────────────────────────────────────────────────────
frames[0].save(
    OUTPUT_PATH,
    save_all=True,
    append_images=frames[1:],
    duration=200,
    loop=0,
)

print(f"GIF saved → {os.path.relpath(OUTPUT_PATH, SCRIPT_DIR)}  "
      f"({len(frames)} frames, 200 ms/frame)")
