"""
animate_arithmetic.py — Generate an animated GIF illustrating arithmetic sequence properties.

Left subplot : Terms a_n = 3 + (n-1)*2 appearing one by one, with the
               underlying linear function y = 2x + 1 and a "d = 2" step
               annotation between the last pair of plotted points.
Right subplot: Partial sums S_n = n(n + 2) growing quadratically, with
               the continuous parabola y = x^2 + 2x shown for reference.

Dependencies: Python 3.10+, matplotlib, numpy, Pillow
Output      : ../assets/arithmetic_anim.gif (relative to this script)
Usage       : python animate_arithmetic.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# ── matplotlib global settings ──────────────────────────────────────────
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── sequence parameters ─────────────────────────────────────────────────
A1, D = 3, 2                          # first term and common difference
N_FRAMES = 20                          # total frames (n = 1 … 20)
INTERVAL_MS = 200                      # milliseconds per frame

ns = np.arange(1, N_FRAMES + 1)       # 1, 2, …, 20
a_n = A1 + (ns - 1) * D               # arithmetic sequence values
s_n = ns * (ns + 2)                    # partial sums  S_n = n(n+2)

# continuous curves for reference lines
x_cont = np.linspace(0.5, N_FRAMES + 0.5, 300)
y_line = D * x_cont + (A1 - D)        # y = 2x + 1
y_para = x_cont ** 2 + 2 * x_cont     # y = x^2 + 2x

# ── output path ─────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, os.pardir, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(ASSETS_DIR, "arithmetic_anim.gif")


def render_frame(frame_idx: int) -> Image.Image:
    """Return a PIL Image for frame *frame_idx* (0-based → shows n = 1 … frame_idx+1)."""
    k = frame_idx + 1                  # number of terms visible

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(12, 5), dpi=100,
                                      facecolor="white")

    # ── LEFT: arithmetic sequence as linear function ────────────────────
    ax_l.plot(x_cont, y_line, color="gray", ls="--", lw=1, label="$y = 2x + 1$")
    ax_l.scatter(ns[:k], a_n[:k], color="red", s=50, zorder=5,
                 label="$a_n$ terms")
    if k >= 2:
        ax_l.plot(ns[:k], a_n[:k], color="royalblue", lw=1.5, zorder=4)

        # "d = 2" step annotation between the last two visible points
        n_prev, n_last = ns[k - 2], ns[k - 1]
        a_prev, a_last = a_n[k - 2], a_n[k - 1]
        ax_l.annotate(
            "", xy=(n_prev, a_last), xytext=(n_prev, a_prev),
            arrowprops=dict(arrowstyle="->", color="green", lw=1.8),
        )
        ax_l.text(n_prev - 0.45, (a_prev + a_last) / 2, "$d=2$",
                  fontsize=9, color="green", ha="right", va="center",
                  fontweight="bold")

    ax_l.set_xlabel("$n$", fontsize=11)
    ax_l.set_ylabel("$a_n$", fontsize=11)
    ax_l.set_title("Arithmetic Sequence: $a_n = 3 + (n-1) \\times 2$",
                    fontsize=11, pad=8)
    ax_l.set_xlim(0, N_FRAMES + 1)
    ax_l.set_ylim(0, a_n[-1] + 3)
    ax_l.legend(loc="upper left", fontsize=9)
    ax_l.grid(True, alpha=0.3)
    ax_l.spines["top"].set_visible(False)
    ax_l.spines["right"].set_visible(False)

    # ── RIGHT: partial sum S_n (quadratic growth) ───────────────────────
    ax_r.plot(x_cont, y_para, color="gray", ls="--", lw=1,
              label="$y = x^2 + 2x$")
    ax_r.scatter(ns[:k], s_n[:k], color="forestgreen", s=50, zorder=5,
                 label="$S_n$ values")
    if k >= 2:
        ax_r.plot(ns[:k], s_n[:k], color="forestgreen", lw=1.5, alpha=0.6,
                  zorder=4)

    ax_r.set_xlabel("$n$", fontsize=11)
    ax_r.set_ylabel("$S_n$", fontsize=11)
    ax_r.set_title("Partial Sum $S_n$ (Quadratic Growth)", fontsize=11,
                    pad=8)
    ax_r.set_xlim(0, N_FRAMES + 1)
    ax_r.set_ylim(0, s_n[-1] + 20)
    ax_r.legend(loc="upper left", fontsize=9)
    ax_r.grid(True, alpha=0.3)
    ax_r.spines["top"].set_visible(False)
    ax_r.spines["right"].set_visible(False)

    fig.tight_layout()

    # convert figure → PIL Image (in-memory)
    buf = BytesIO()
    fig.savefig(buf, format="png", facecolor="white", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def main() -> None:
    frames = [render_frame(i) for i in range(N_FRAMES)]

    # duplicate the last frame a few times so the final state lingers
    frames += [frames[-1]] * 3

    frames[0].save(
        OUTPUT_PATH,
        save_all=True,
        append_images=frames[1:],
        duration=INTERVAL_MS,
        loop=0,
    )
    print(f"GIF saved to {os.path.abspath(OUTPUT_PATH)}")


if __name__ == "__main__":
    main()
