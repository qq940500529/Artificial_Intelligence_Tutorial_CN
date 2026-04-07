# 文件：code/plot_amgm_geometry.py
# 用途：绘制 AM-GM 不等式的经典几何证明图（半圆法）
#       直径 a+b 的半圆中，半径 = (a+b)/2（算术平均），
#       从分界点向半圆作垂线，垂线长度 = sqrt(ab)（几何平均）。
# 依赖：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── 字体与样式设置 ──
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ── 输出路径（基于脚本自身位置） ──
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'amgm_geometry.png')

# ── 参数设置 ──
a_val = 3.0   # 线段 a 的长度
b_val = 7.0   # 线段 b 的长度
diameter = a_val + b_val            # 直径 = a + b
radius = diameter / 2.0             # 半径 = (a+b)/2 = 算术平均
gm = np.sqrt(a_val * b_val)        # 几何平均 = sqrt(ab)

# 关键点坐标（以直径左端为原点）
A = np.array([0.0, 0.0])                    # 左端点 A
B = np.array([diameter, 0.0])               # 右端点 B
M = np.array([radius, 0.0])                 # 圆心（中点 M）
P = np.array([a_val, 0.0])                  # 分界点（AP = a, PB = b）
H = np.array([a_val, gm])                   # 垂线与半圆的交点

# ── 创建画布 ──
fig, ax = plt.subplots(1, 1, figsize=(10, 6), facecolor='white')

# ── 绘制半圆 ──
theta = np.linspace(0, np.pi, 300)
semicircle_x = M[0] + radius * np.cos(theta)
semicircle_y = M[1] + radius * np.sin(theta)
ax.plot(semicircle_x, semicircle_y, color='#1565C0', linewidth=2.5, zorder=3)

# ── 绘制直径 ──
ax.plot([A[0], B[0]], [A[1], B[1]], color='#333333', linewidth=2, zorder=3)

# ── 标注线段 a 和 b（直径上） ──
# 线段 a 的标注（A 到 P）
ax.annotate('', xy=(a_val - 0.05, -0.45), xytext=(0.05, -0.45),
            arrowprops=dict(arrowstyle='<->', color='#E65100', lw=1.8))
ax.text(a_val / 2, -0.75, r'$a$', ha='center', va='top',
        fontsize=16, fontweight='bold', color='#E65100')

# 线段 b 的标注（P 到 B）
ax.annotate('', xy=(diameter - 0.05, -0.45), xytext=(a_val + 0.05, -0.45),
            arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=1.8))
ax.text(a_val + b_val / 2, -0.75, r'$b$', ha='center', va='top',
        fontsize=16, fontweight='bold', color='#2E7D32')

# ── 绘制半径 MH（算术平均） ──
ax.plot([M[0], H[0]], [M[1], H[1]], color='#D32F2F', linewidth=2.5,
        linestyle='-', zorder=4, label=r'Radius $= \frac{a+b}{2}$ (AM)')

# ── 绘制垂线 PH（几何平均） ──
ax.plot([P[0], H[0]], [P[1], H[1]], color='#1565C0', linewidth=2.5,
        linestyle='--', zorder=4, label=r'Height $= \sqrt{ab}$ (GM)')

# ── 绘制直角标记 ──
sq_size = 0.3
sq = plt.Polygon([[P[0], P[1]], [P[0] + sq_size, P[1]],
                   [P[0] + sq_size, P[1] + sq_size], [P[0], P[1] + sq_size]],
                  fill=False, edgecolor='#666666', linewidth=1.2, zorder=5)
ax.add_patch(sq)

# ── 绘制关键点 ──
points = [
    (A, 'A', 'right', (0.25, -0.35)),
    (B, 'B', 'left', (-0.25, -0.35)),
    (M, 'M', 'center', (0, -0.35)),
    (P, 'P', 'center', (0.35, -0.35)),
    (H, 'H', 'left', (0.25, 0.15)),
]

for pt, label, ha, offset in points:
    ax.plot(pt[0], pt[1], 'o', color='#333333', markersize=6, zorder=6)
    ax.text(pt[0] + offset[0], pt[1] + offset[1], f'${label}$',
            ha=ha, va='center', fontsize=14, fontweight='bold', color='#333333')

# ── 标注数值 ──
# 半径长度标注
mid_MH = (M + H) / 2
ax.text(mid_MH[0] - 0.6, mid_MH[1] + 0.15, r'$\frac{a+b}{2}$',
        ha='center', va='bottom', fontsize=14, color='#D32F2F',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                  edgecolor='#D32F2F', alpha=0.85))

# 垂线长度标注
mid_PH = (P + H) / 2
ax.text(mid_PH[0] + 0.55, mid_PH[1], r'$\sqrt{ab}$',
        ha='left', va='center', fontsize=14, color='#1565C0',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                  edgecolor='#1565C0', alpha=0.85))

# ── 不等式结论 ──
ax.text(diameter / 2, radius + 1.0,
        r'AM $\geq$ GM :   $\frac{a+b}{2} \geq \sqrt{ab}$',
        ha='center', va='bottom', fontsize=15,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4',
                  edgecolor='#F9A825', alpha=0.95))

# ── 图例 ──
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

# ── 坐标轴设置 ──
ax.set_xlim(-1.0, diameter + 1.0)
ax.set_ylim(-1.5, radius + 2.0)
ax.set_aspect('equal')
ax.axis('off')

# ── 保存 ──
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f"Plot saved to: {output_path}")
