# plot_spatial_relations.py
# 用途：绘制空间中点线面位置关系的四种典型情形
# 环境：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出路径基于脚本位置
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'spatial_relations.png')

fig = plt.figure(figsize=(12, 10), facecolor='white')

# ---------- 1. Intersecting Lines ----------
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
t = np.linspace(-2, 2, 50)
# Line 1: along x-axis through origin
ax1.plot(t, np.zeros_like(t), np.zeros_like(t), 'b-', linewidth=2.5, label='$l_1$')
# Line 2: along y=x direction in xy-plane through origin
ax1.plot(t, t, np.zeros_like(t), 'r-', linewidth=2.5, label='$l_2$')
# Mark intersection point
ax1.scatter([0], [0], [0], color='gold', s=100, zorder=5, edgecolors='black', linewidths=1)
ax1.text(0.3, 0.3, 0.4, 'Intersection\nPoint', fontsize=8, ha='center')
# Draw angle arc
theta = np.linspace(0, np.pi / 4, 30)
r_arc = 1.0
ax1.plot(r_arc * np.cos(theta), r_arc * np.sin(theta), np.zeros_like(theta),
         'g-', linewidth=2)
ax1.text(1.1, 0.4, 0.15, r'$\theta$', fontsize=12, color='green')
ax1.set_title('Intersecting Lines', fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('$x$', fontsize=10)
ax1.set_ylabel('$y$', fontsize=10)
ax1.set_zlabel('$z$', fontsize=10)
ax1.legend(loc='upper left', fontsize=9)

# ---------- 2. Parallel Lines ----------
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot(t, np.zeros_like(t), np.zeros_like(t), 'b-', linewidth=2.5, label='$l_1$')
ax2.plot(t, np.ones_like(t) * 2, np.zeros_like(t), 'r-', linewidth=2.5, label='$l_2$')
# Direction arrows
for line_y, color in [(0, 'blue'), (2, 'red')]:
    ax2.quiver(0.5, line_y, 0, 1, 0, 0, color=color, arrow_length_ratio=0.3,
               linewidth=2)
# Dashed lines showing equal distance
for x_pos in [-1, 0, 1]:
    ax2.plot([x_pos, x_pos], [0, 2], [0, 0], 'g--', linewidth=1, alpha=0.5)
ax2.text(0, 1, 0.5, 'Equal\ndistance', fontsize=8, ha='center', color='green')
ax2.set_title('Parallel Lines', fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel('$x$', fontsize=10)
ax2.set_ylabel('$y$', fontsize=10)
ax2.set_zlabel('$z$', fontsize=10)
ax2.legend(loc='upper left', fontsize=9)

# ---------- 3. Skew Lines ----------
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
# Line 1: in xy-plane, along x-axis
ax3.plot(t, np.zeros_like(t), np.zeros_like(t), 'b-', linewidth=2.5, label='$l_1$ (xy-plane)')
# Line 2: shifted in z, along y-axis
ax3.plot(np.ones_like(t) * 0, t, np.ones_like(t) * 1.5, 'r-', linewidth=2.5,
         label='$l_2$ (z = 1.5)')
# Show z-gap with a dashed line
ax3.plot([0, 0], [0, 0], [0, 1.5], 'k--', linewidth=1, alpha=0.6)
ax3.text(0.2, 0.2, 0.75, 'Gap', fontsize=9, color='black')
ax3.set_title('Skew Lines', fontsize=12, fontweight='bold', pad=10)
ax3.set_xlabel('$x$', fontsize=10)
ax3.set_ylabel('$y$', fontsize=10)
ax3.set_zlabel('$z$', fontsize=10)
ax3.legend(loc='upper left', fontsize=9)

# ---------- 4. Line Perpendicular to Plane ----------
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
# Draw a semi-transparent plane (z=0)
plane = Poly3DCollection([[(-2, -2, 0), (2, -2, 0), (2, 2, 0), (-2, 2, 0)]],
                         alpha=0.25, facecolor='skyblue', edgecolor='steelblue',
                         linewidths=1.5)
ax4.add_collection3d(plane)
# Perpendicular line along z-axis
z_line = np.linspace(0, 2.5, 50)
ax4.plot(np.zeros_like(z_line), np.zeros_like(z_line), z_line, 'r-', linewidth=2.5,
         label='$l \\perp \\alpha$')
# Right-angle mark
sq_size = 0.3
ax4.plot([0, sq_size], [0, 0], [0, 0], 'k-', linewidth=1.5)
ax4.plot([sq_size, sq_size], [0, 0], [0, sq_size], 'k-', linewidth=1.5)
ax4.plot([0, 0], [0, 0], [0, 0], 'k-', linewidth=1.5)
# Foot point
ax4.scatter([0], [0], [0], color='gold', s=100, zorder=5, edgecolors='black', linewidths=1)
ax4.text(0.4, 0.4, 1.5, r'$l$', fontsize=12, color='red', fontweight='bold')
ax4.text(1.5, 1.5, -0.3, r'$\alpha$', fontsize=14, color='steelblue', fontweight='bold')
ax4.set_title('Line $\\perp$ Plane', fontsize=12, fontweight='bold', pad=10)
ax4.set_xlabel('$x$', fontsize=10)
ax4.set_ylabel('$y$', fontsize=10)
ax4.set_zlabel('$z$', fontsize=10)
ax4.legend(loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
