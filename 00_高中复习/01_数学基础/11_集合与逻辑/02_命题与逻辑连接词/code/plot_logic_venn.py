# 文件：code/plot_logic_venn.py
# 用途：用韦恩图（几何图形）直观展示逻辑连接词 AND（合取）、OR（析取）、NOT（否定）
# 环境要求：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch

# 字体与样式
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, '..', 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)


def draw_venn(ax, highlight='none', title='', label_left='p', label_right='q'):
    """绘制一个韦恩图并高亮指定区域。

    highlight: 'and' / 'or' / 'not_p' / 'none'
    """
    theta = np.linspace(0, 2 * np.pi, 200)
    r = 1.0
    cx_left, cx_right = -0.5, 0.5
    cy = 0.0

    # 全集矩形
    rect = FancyBboxPatch((-2.2, -1.6), 4.4, 3.2,
                          boxstyle="round,pad=0.05",
                          linewidth=1.5, edgecolor='#555555',
                          facecolor='#f8f8f8', zorder=0)
    ax.add_patch(rect)
    ax.text(1.9, 1.3, 'U', fontsize=13, fontweight='bold', color='#555555')

    # 计算圆的坐标
    x_left = cx_left + r * np.cos(theta)
    y_left = cy + r * np.sin(theta)
    x_right = cx_right + r * np.cos(theta)
    y_right = cy + r * np.sin(theta)

    # 生成填充用的网格
    x_grid = np.linspace(-2.2, 2.2, 500)
    y_grid = np.linspace(-1.6, 1.6, 500)
    X, Y = np.meshgrid(x_grid, y_grid)
    in_left = (X - cx_left) ** 2 + (Y - cy) ** 2 <= r ** 2
    in_right = (X - cx_right) ** 2 + (Y - cy) ** 2 <= r ** 2
    in_rect = (X >= -2.2) & (X <= 2.2) & (Y >= -1.6) & (Y <= 1.6)

    # 高亮区域
    if highlight == 'and':
        mask = in_left & in_right
        color = '#FF6B6B'
    elif highlight == 'or':
        mask = in_left | in_right
        color = '#4ECDC4'
    elif highlight == 'not_p':
        mask = ~in_left & in_rect
        color = '#FFD93D'
    else:
        mask = np.zeros_like(X, dtype=bool)
        color = '#CCCCCC'

    if mask.any():
        ax.contourf(X, Y, mask.astype(float), levels=[0.5, 1.5],
                    colors=[color], alpha=0.5, zorder=1)

    # 画圆边界
    ax.plot(x_left, y_left, color='#2C3E50', linewidth=2, zorder=3)
    ax.plot(x_right, y_right, color='#2C3E50', linewidth=2, zorder=3)

    # 标签
    ax.text(cx_left - 0.3, cy, label_left, fontsize=16, fontweight='bold',
            ha='center', va='center', color='#2C3E50', zorder=4)
    ax.text(cx_right + 0.3, cy, label_right, fontsize=16, fontweight='bold',
            ha='center', va='center', color='#2C3E50', zorder=4)

    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    draw_venn(axes[0], highlight='and',
              title=r'AND ($p \wedge q$): Intersection')
    draw_venn(axes[1], highlight='or',
              title=r'OR ($p \vee q$): Union')
    draw_venn(axes[2], highlight='not_p',
              title=r'NOT ($\neg p$): Complement')

    fig.suptitle('Logic Connectives as Set Operations',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()

    save_path = os.path.join(ASSETS_DIR, 'logic_venn.png')
    fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {save_path}')


if __name__ == '__main__':
    main()
