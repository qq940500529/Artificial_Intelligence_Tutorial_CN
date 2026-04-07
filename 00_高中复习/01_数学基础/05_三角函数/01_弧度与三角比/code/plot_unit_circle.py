# 文件：code/plot_unit_circle.py
# 用途：绘制单位圆与三角函数定义图
# 环境要求：Python 3.10+, matplotlib, numpy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出路径
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# ========== 图1：单位圆定义 ==========
fig, ax = plt.subplots(1, 1, figsize=(7, 7))

# 画单位圆
theta_circle = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(theta_circle), np.sin(theta_circle), 'b-', linewidth=1.5)

# 坐标轴
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)

# 选定角度 theta = 40 度
theta = np.radians(40)
x = np.cos(theta)
y = np.sin(theta)

# 从原点到圆上的线
ax.plot([0, x], [0, y], 'r-', linewidth=2, label=r'$r = 1$')

# 投影虚线
ax.plot([x, x], [0, y], 'g--', linewidth=1.5, label=r'$\sin\theta = y$')
ax.plot([0, x], [0, 0], 'm-', linewidth=3, alpha=0.6, label=r'$\cos\theta = x$')

# 标注点
ax.plot(x, y, 'ro', markersize=8, zorder=5)
ax.annotate(r'$P(\cos\theta,\,\sin\theta)$', xy=(x, y), xytext=(x + 0.12, y + 0.08),
            fontsize=13, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

# 标注 cos θ 和 sin θ
ax.annotate(r'$\cos\theta$', xy=(x / 2, -0.08), fontsize=12, color='purple',
            ha='center')
ax.annotate(r'$\sin\theta$', xy=(x + 0.08, y / 2), fontsize=12, color='green',
            ha='left')

# 画角度弧
angle_arc = np.linspace(0, theta, 50)
arc_r = 0.2
ax.plot(arc_r * np.cos(angle_arc), arc_r * np.sin(angle_arc), 'k-', linewidth=1.2)
ax.annotate(r'$\theta$', xy=(0.25, 0.08), fontsize=14)

# 标注象限
ax.text(0.5, 0.6, 'I', fontsize=16, color='gray', ha='center', alpha=0.5)
ax.text(-0.5, 0.6, 'II', fontsize=16, color='gray', ha='center', alpha=0.5)
ax.text(-0.5, -0.6, 'III', fontsize=16, color='gray', ha='center', alpha=0.5)
ax.text(0.5, -0.6, 'IV', fontsize=16, color='gray', ha='center', alpha=0.5)

# 标注坐标轴
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$y$', fontsize=14)
ax.set_title('Unit Circle: Trigonometric Function Definition', fontsize=14, pad=15)

ax.set_xlim(-1.4, 1.6)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11, loc='lower left')

# 隐藏不必要的边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'unit_circle.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ========== 图2：直角三角形定义 ==========
fig, ax = plt.subplots(1, 1, figsize=(6, 5))

# 三角形的三个顶点
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([4, 3])

# 画三角形
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(triangle)

# 直角符号
sq_size = 0.3
sq = plt.Polygon([B, B + np.array([0, sq_size]), B + np.array([-sq_size, sq_size]), B + np.array([-sq_size, 0])],
                  fill=False, edgecolor='blue', linewidth=1)
ax.add_patch(sq)

# 标注角 θ
angle_arc = np.linspace(0, np.arctan(3 / 4), 50)
arc_r = 0.7
ax.plot(A[0] + arc_r * np.cos(angle_arc), A[1] + arc_r * np.sin(angle_arc), 'r-', linewidth=1.5)
ax.text(0.85, 0.22, r'$\theta$', fontsize=16, color='red')

# 标注边
ax.text(2, -0.35, 'Adjacent', fontsize=12, ha='center', color='purple')
ax.text(4.5, 1.5, 'Opposite', fontsize=12, ha='center', color='green', rotation=90)
ax.text(1.5, 1.85, 'Hypotenuse', fontsize=12, ha='center', color='blue',
        rotation=np.degrees(np.arctan(3 / 4)))

# 标注顶点
ax.text(-0.2, -0.2, r'$A$', fontsize=14, fontweight='bold')
ax.text(4.1, -0.2, r'$B$', fontsize=14, fontweight='bold')
ax.text(4.1, 3.1, r'$C$', fontsize=14, fontweight='bold')

# 公式标注
formula_text = (r'$\sin\theta = \frac{\mathrm{Opposite}}{\mathrm{Hypotenuse}}$' + '\n\n'
                + r'$\cos\theta = \frac{\mathrm{Adjacent}}{\mathrm{Hypotenuse}}$' + '\n\n'
                + r'$\tan\theta = \frac{\mathrm{Opposite}}{\mathrm{Adjacent}}$')
ax.text(-0.5, 3.5, formula_text, fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange', alpha=0.8))

ax.set_xlim(-1, 6)
ax.set_ylim(-0.8, 4.2)
ax.set_aspect('equal')
ax.set_title('Right Triangle: Trigonometric Ratios', fontsize=14, pad=10)
ax.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'right_triangle_trig.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("Generated: unit_circle.png, right_triangle_trig.png")
