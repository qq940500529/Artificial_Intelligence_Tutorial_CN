# 文件：code/plot_dot_product.py
# 用途：绘制数量积的投影几何意义图
# 环境要求：Python 3.10+, matplotlib>=3.7, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Output path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'dot_product_projection.png')

# Define vectors
a = np.array([3.0, 3.5])
b = np.array([5.0, 1.0])

# Compute projection of a onto b
b_unit = b / np.linalg.norm(b)
proj_length = np.dot(a, b_unit)  # |a|cos(theta)
proj_point = proj_length * b_unit

# Compute angle
cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
theta = np.arccos(np.clip(cos_theta, -1, 1))

fig, ax = plt.subplots(figsize=(9, 6))

# Draw vectors as arrows
arrow_props = dict(head_width=0.15, head_length=0.12, linewidth=2.2)
ax.annotate('', xy=a, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#2166AC', lw=2.5,
                            mutation_scale=18))
ax.annotate('', xy=b, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#B2182B', lw=2.5,
                            mutation_scale=18))

# Draw projection line (from a to projection point) — dashed perpendicular
ax.plot([a[0], proj_point[0]], [a[1], proj_point[1]],
        'k--', linewidth=1.5, alpha=0.7, zorder=3)

# Draw projection segment on b direction
ax.plot([0, proj_point[0]], [0, proj_point[1]],
        color='#4DAF4A', linewidth=3, solid_capstyle='round', zorder=2)
ax.plot(proj_point[0], proj_point[1], 'o', color='#4DAF4A',
        markersize=8, zorder=4)

# Right angle marker at projection point
perp_size = 0.25
perp_dir = (a - proj_point) / np.linalg.norm(a - proj_point)
along_dir = -b_unit
corner1 = proj_point + perp_size * perp_dir
corner2 = proj_point + perp_size * along_dir
corner3 = proj_point + perp_size * (perp_dir + along_dir)
ax.plot([corner1[0], corner3[0]], [corner1[1], corner3[1]],
        'k-', linewidth=1.0)
ax.plot([corner2[0], corner3[0]], [corner2[1], corner3[1]],
        'k-', linewidth=1.0)

# Draw angle arc
angle_radius = 0.8
angles = np.linspace(0, theta, 40)
arc_x = angle_radius * np.cos(angles)
arc_y = angle_radius * np.sin(angles)
# Rotate arc to align with b direction
b_angle = np.arctan2(b[1], b[0])
rot = np.array([[np.cos(b_angle), -np.sin(b_angle)],
                [np.sin(b_angle),  np.cos(b_angle)]])
arc_pts = rot @ np.vstack([arc_x, arc_y])
ax.plot(arc_pts[0], arc_pts[1], 'k-', linewidth=1.5)

# Theta label
mid_angle = b_angle + theta / 2
ax.text(1.1 * np.cos(mid_angle), 1.1 * np.sin(mid_angle),
        r'$\theta$', fontsize=16, ha='center', va='center')

# Vector labels
ax.text(a[0] + 0.15, a[1] + 0.15, r'$\vec{a}$',
        fontsize=18, color='#2166AC', fontweight='bold')
ax.text(b[0] + 0.15, b[1] - 0.25, r'$\vec{b}$',
        fontsize=18, color='#B2182B', fontweight='bold')

# Projection length label
mid_proj = proj_point / 2
offset = np.array([-0.15, -0.35])
ax.text(mid_proj[0] + offset[0], mid_proj[1] + offset[1],
        r'$|\vec{a}|\cos\theta$',
        fontsize=14, color='#4DAF4A', fontweight='bold',
        ha='center', va='top')

# Formula annotation
ax.text(0.98, 0.95,
        r'$\vec{a} \cdot \vec{b} = |\vec{a}|\,|\vec{b}|\,\cos\theta$',
        transform=ax.transAxes, fontsize=16,
        ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.9))

# Origin label
ax.plot(0, 0, 'ko', markersize=5, zorder=5)
ax.text(-0.2, -0.2, 'O', fontsize=14, ha='center', va='center')

# Styling
ax.set_xlim(-0.8, 6.0)
ax.set_ylim(-0.8, 4.5)
ax.set_aspect('equal')
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$y$', fontsize=14)
ax.set_title('Dot Product: Projection of $\\vec{a}$ onto $\\vec{b}$',
             fontsize=15, pad=12)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Plot saved to {output_path}")
