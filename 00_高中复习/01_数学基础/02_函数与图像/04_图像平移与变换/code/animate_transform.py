# 文件：animate_transform.py
# 用途：生成函数图像变换动画 GIF，展示平移、缩放、翻转四个阶段
# 环境要求：Python 3.10+, numpy, matplotlib, Pillow

import os
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ── 配置 ──
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ── 输出路径 ──
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'transform_anim.gif')

# ── 动画参数 ──
TOTAL_FRAMES = 60
FRAMES_PER_PHASE = 15
FPS_DELAY = 150  # ms per frame
X_RANGE = (-5, 8)
Y_RANGE = (-2, 20)
FIG_SIZE = (8, 6)
DPI = 100

x = np.linspace(X_RANGE[0], X_RANGE[1], 500)


def render_frame(frame_idx: int) -> Image.Image:
    """Render a single animation frame and return it as a PIL Image."""
    fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI, facecolor='white')
    ax.set_xlim(X_RANGE)
    ax.set_ylim(Y_RANGE)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$y$', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Reference curve: y = x^2 (gray dashed)
    y_ref = x ** 2
    ax.plot(x, y_ref, color='gray', linestyle='--', linewidth=1.5,
            alpha=0.5, label='$y = x^2$')

    phase = frame_idx // FRAMES_PER_PHASE
    local = frame_idx % FRAMES_PER_PHASE
    t = local / (FRAMES_PER_PHASE - 1)  # progress 0 → 1

    if phase == 0:
        # Phase 1: Horizontal shift  y = (x - h)^2, h: 0 → 3
        h = 3.0 * t
        y_curve = (x - h) ** 2
        ax.plot(x, y_curve, color='red', linewidth=2.5,
                label=f'$y = (x - {h:.1f})^2$')
        ax.plot(h, 0, 'o', color='red', markersize=8, zorder=5)
        ax.set_title(f'Horizontal Shift: $y=(x-h)^2$,  $h={h:.1f}$',
                     fontsize=13, pad=10)

    elif phase == 1:
        # Phase 2: Vertical shift  y = (x-3)^2 + k, k: 0 → 2
        k = 2.0 * t
        y_curve = (x - 3) ** 2 + k
        ax.plot(x, y_curve, color='royalblue', linewidth=2.5,
                label=f'$y = (x-3)^2 + {k:.1f}$')
        ax.plot(3, k, 'o', color='royalblue', markersize=8, zorder=5)
        ax.set_title(f'Vertical Shift: $y=(x-3)^2+k$,  $k={k:.1f}$',
                     fontsize=13, pad=10)

    elif phase == 2:
        # Phase 3: Horizontal scale  y = (a*x)^2, a: 1 → 2
        a = 1.0 + 1.0 * t
        y_curve = (a * x) ** 2
        ax.plot(x, y_curve, color='green', linewidth=2.5,
                label=f'$y = ({a:.1f}x)^2$')
        ax.plot(0, 0, 'o', color='green', markersize=8, zorder=5)
        ax.set_title(f'Horizontal Scale: $y=(ax)^2$,  $a={a:.1f}$',
                     fontsize=13, pad=10)

    else:
        # Phase 4: Reflection  f(x) = (x-1)^2 + 1  →  f(-x) = (x+1)^2 + 1
        y_orig = (x - 1) ** 2 + 1
        y_refl = (x + 1) ** 2 + 1

        ax.plot(x, y_orig, color='red', linewidth=2, alpha=0.7,
                label='$f(x) = (x-1)^2+1$')

        # Blue reflected curve fades in
        alpha_refl = t
        ax.plot(x, y_refl, color='royalblue', linewidth=2.5,
                alpha=max(alpha_refl, 0.05),
                label='$f(-x) = (x+1)^2+1$')

        # Mark vertices
        ax.plot(1, 1, 'o', color='red', markersize=7, zorder=5)
        ax.plot(-1, 1, 'o', color='royalblue', markersize=7,
                alpha=max(alpha_refl, 0.05), zorder=5)

        # Dashed line connecting symmetric vertices once visible
        if alpha_refl > 0.3:
            ax.plot([1, -1], [1, 1], 'k:', linewidth=1, alpha=0.4)
            ax.axvline(x=0, color='gray', linestyle=':', linewidth=1,
                       alpha=0.3)

        ax.set_title(r'Reflection: $f(x) \to f(-x)$',
                     fontsize=13, pad=10)

    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    fig.tight_layout()

    # Convert figure to PIL Image via in-memory buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png', facecolor='white', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).copy()


def main():
    print(f'Generating {TOTAL_FRAMES} frames...')
    frames = []
    for i in range(TOTAL_FRAMES):
        frames.append(render_frame(i))
        if (i + 1) % 15 == 0:
            print(f'  Phase {i // 15 + 1}/4 complete ({i + 1} frames)')

    print(f'Saving GIF to {output_path}')
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_DELAY,
        loop=0,
    )
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f'Done! File size: {file_size_kb:.0f} KB')


if __name__ == '__main__':
    main()
