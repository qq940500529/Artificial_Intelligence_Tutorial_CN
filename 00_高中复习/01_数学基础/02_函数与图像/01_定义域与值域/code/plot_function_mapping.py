# 文件：code/plot_function_mapping.py
# 用途：绘制函数 f(x) = x² 的映射图（集合 A → 集合 B），
#       直观展示函数作为"映射"的含义。
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
output_path = os.path.join(output_dir, 'function_mapping.png')

# ── 创建画布 ──
fig, ax = plt.subplots(1, 1, figsize=(8, 5), facecolor='white')
ax.set_xlim(-1.5, 8.5)
ax.set_ylim(-0.5, 6.5)
ax.set_aspect('equal')
ax.axis('off')

# ── 椭圆参数 ──
ellipse_a_cx, ellipse_a_cy = 2.0, 3.0  # 集合 A 的中心
ellipse_b_cx, ellipse_b_cy = 6.5, 3.0  # 集合 B 的中心
ellipse_w, ellipse_h = 2.8, 5.2         # 椭圆宽度、高度

# 绘制椭圆（集合 A 和集合 B）
ellipse_a = mpatches.Ellipse(
    (ellipse_a_cx, ellipse_a_cy), ellipse_w, ellipse_h,
    fill=True, facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=2, alpha=0.8
)
ellipse_b = mpatches.Ellipse(
    (ellipse_b_cx, ellipse_b_cy), ellipse_w, ellipse_h,
    fill=True, facecolor='#FFF3E0', edgecolor='#E65100', linewidth=2, alpha=0.8
)
ax.add_patch(ellipse_a)
ax.add_patch(ellipse_b)

# ── 集合标签 ──
ax.text(ellipse_a_cx, ellipse_a_cy + ellipse_h / 2 + 0.3,
        'Set A (Domain)', ha='center', va='bottom',
        fontsize=13, fontweight='bold', color='#1565C0')
ax.text(ellipse_b_cx, ellipse_b_cy + ellipse_h / 2 + 0.3,
        'Set B (Range)', ha='center', va='bottom',
        fontsize=13, fontweight='bold', color='#E65100')

# ── 元素位置 ──
# 集合 A 中的元素及其纵向位置
a_elements = [
    ('1',  ellipse_a_cx, 4.5),
    ('2',  ellipse_a_cx, 3.7),
    ('-1', ellipse_a_cx, 2.9),
    ('-2', ellipse_a_cx, 2.1),
    ('3',  ellipse_a_cx, 1.3),
]

# 集合 B 中的元素及其纵向位置
b_elements = [
    ('1', ellipse_b_cx, 4.2),
    ('4', ellipse_b_cx, 3.0),
    ('9', ellipse_b_cx, 1.8),
]

# ── 绘制元素（小圆点 + 标签） ──
dot_radius = 0.12
for label, x, y in a_elements:
    circle = plt.Circle((x, y), dot_radius, color='#1565C0', zorder=5)
    ax.add_patch(circle)
    ax.text(x - 0.4, y, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color='#0D47A1')

for label, x, y in b_elements:
    circle = plt.Circle((x, y), dot_radius, color='#E65100', zorder=5)
    ax.add_patch(circle)
    ax.text(x + 0.4, y, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color='#BF360C')

# ── 映射箭头（f(x) = x²） ──
# 映射关系：1→1, -1→1, 2→4, -2→4, 3→9
mappings = [
    (0, 0),   # 1 → 1
    (2, 0),   # -1 → 1
    (1, 1),   # 2 → 4
    (3, 1),   # -2 → 4
    (4, 2),   # 3 → 9
]

arrow_color = '#616161'
for a_idx, b_idx in mappings:
    ax_start = a_elements[a_idx][1] + dot_radius + 0.05
    ay_start = a_elements[a_idx][2]
    ax_end = b_elements[b_idx][1] - dot_radius - 0.05
    ay_end = b_elements[b_idx][2]

    ax.annotate(
        '', xy=(ax_end, ay_end), xytext=(ax_start, ay_start),
        arrowprops=dict(
            arrowstyle='->', color=arrow_color, linewidth=1.5,
            connectionstyle='arc3,rad=0.12', alpha=0.7
        )
    )

# ── 函数标签 ──
ax.text(4.25, 5.8, r'$f(x) = x^2$', ha='center', va='center',
        fontsize=14, fontstyle='italic', color='#333333',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                  edgecolor='#9E9E9E', alpha=0.9))

# ── 保存 ──
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f"Plot saved to: {output_path}")
