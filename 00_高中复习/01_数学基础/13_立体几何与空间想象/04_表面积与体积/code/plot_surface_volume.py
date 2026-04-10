# plot_surface_volume.py
# 用途：绘制圆柱、圆锥、球和截锥的三维图形，标注表面积与体积公式
# 环境：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'surface_volume.png')

fig = plt.figure(figsize=(12, 10), facecolor='white')

theta = np.linspace(0, 2 * np.pi, 80)

# ---------- 1. Cylinder ----------
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
r, h = 1.0, 2.0
z_cyl = np.linspace(0, h, 40)
theta_grid, z_grid = np.meshgrid(theta, z_cyl)
x_cyl = r * np.cos(theta_grid)
y_cyl = r * np.sin(theta_grid)
ax1.plot_surface(x_cyl, y_cyl, z_grid, alpha=0.35, color='dodgerblue')
ax1.plot_wireframe(x_cyl, y_cyl, z_grid, rstride=8, cstride=4, color='steelblue',
                   linewidth=0.5, alpha=0.6)
# Top and bottom circles
for z_val in [0, h]:
    ax1.plot(r * np.cos(theta), r * np.sin(theta), np.full_like(theta, z_val),
             color='steelblue', linewidth=1.5)
# Dimension annotations
ax1.plot([0, r], [0, 0], [0, 0], 'r-', linewidth=2)
ax1.text(0.5, 0, -0.3, '$r$', fontsize=11, color='red', ha='center')
ax1.plot([r + 0.2, r + 0.2], [0, 0], [0, h], 'g-', linewidth=2)
ax1.text(r + 0.4, 0, h / 2, '$h$', fontsize=11, color='green', ha='center')
ax1.set_title('Cylinder\n$S=2\\pi rh+2\\pi r^2$\n$V=\\pi r^2 h$',
              fontsize=11, fontweight='bold', pad=5)
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_zlim(-0.5, 2.5)
ax1.set_axis_off()

# ---------- 2. Cone ----------
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
r_cone, h_cone = 1.0, 2.0
z_cone = np.linspace(0, h_cone, 40)
theta_grid_c, z_grid_c = np.meshgrid(theta, z_cone)
r_at_z = r_cone * (1 - z_grid_c / h_cone)
x_cone = r_at_z * np.cos(theta_grid_c)
y_cone = r_at_z * np.sin(theta_grid_c)
ax2.plot_surface(x_cone, y_cone, z_grid_c, alpha=0.35, color='coral')
ax2.plot_wireframe(x_cone, y_cone, z_grid_c, rstride=8, cstride=4, color='orangered',
                   linewidth=0.5, alpha=0.6)
# Bottom circle
ax2.plot(r_cone * np.cos(theta), r_cone * np.sin(theta), np.zeros_like(theta),
         color='orangered', linewidth=1.5)
# Apex
ax2.scatter([0], [0], [h_cone], color='red', s=60, zorder=5)
# Annotations
ax2.plot([0, r_cone], [0, 0], [0, 0], 'r-', linewidth=2)
ax2.text(0.5, 0, -0.3, '$r$', fontsize=11, color='red', ha='center')
ax2.plot([0, 0], [0, 0], [0, h_cone], 'g-', linewidth=2)
ax2.text(0.2, 0.2, h_cone / 2, '$h$', fontsize=11, color='green')
# Slant height
l = np.sqrt(r_cone**2 + h_cone**2)
ax2.plot([r_cone, 0], [0, 0], [0, h_cone], 'm--', linewidth=1.5)
ax2.text(0.6, 0, 1.2, '$l$', fontsize=11, color='purple')
ax2.set_title('Cone\n$S=\\pi r l+\\pi r^2$\n$V=\\frac{1}{3}\\pi r^2 h$',
              fontsize=11, fontweight='bold', pad=5)
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_zlim(-0.5, 2.5)
ax2.set_axis_off()

# ---------- 3. Sphere ----------
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
r_sph = 1.0
phi = np.linspace(0, np.pi, 40)
theta_sph = np.linspace(0, 2 * np.pi, 60)
phi_grid, theta_grid_s = np.meshgrid(phi, theta_sph)
x_sph = r_sph * np.sin(phi_grid) * np.cos(theta_grid_s)
y_sph = r_sph * np.sin(phi_grid) * np.sin(theta_grid_s)
z_sph = r_sph * np.cos(phi_grid)
ax3.plot_wireframe(x_sph, y_sph, z_sph, rstride=4, cstride=4, color='seagreen',
                   linewidth=0.5, alpha=0.5)
ax3.plot_surface(x_sph, y_sph, z_sph, alpha=0.2, color='mediumseagreen')
# Radius line
ax3.plot([0, r_sph], [0, 0], [0, 0], 'r-', linewidth=2.5)
ax3.text(0.5, 0, 0.15, '$r$', fontsize=12, color='red', fontweight='bold')
# Center
ax3.scatter([0], [0], [0], color='red', s=40, zorder=5)
# Equator
ax3.plot(r_sph * np.cos(theta), r_sph * np.sin(theta), np.zeros_like(theta),
         color='darkgreen', linewidth=1.5, linestyle='--')
ax3.set_title('Sphere\n$S=4\\pi r^2$\n$V=\\frac{4}{3}\\pi r^3$',
              fontsize=11, fontweight='bold', pad=5)
ax3.set_xlim(-1.5, 1.5)
ax3.set_ylim(-1.5, 1.5)
ax3.set_zlim(-1.5, 1.5)
ax3.set_axis_off()

# ---------- 4. Frustum (Truncated Cone) ----------
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
r1, r2, h_fr = 1.0, 0.5, 1.5
z_fr = np.linspace(0, h_fr, 40)
theta_grid_f, z_grid_f = np.meshgrid(theta, z_fr)
r_at_z_f = r1 + (r2 - r1) * z_grid_f / h_fr
x_fr = r_at_z_f * np.cos(theta_grid_f)
y_fr = r_at_z_f * np.sin(theta_grid_f)
ax4.plot_surface(x_fr, y_fr, z_grid_f, alpha=0.35, color='mediumpurple')
ax4.plot_wireframe(x_fr, y_fr, z_grid_f, rstride=8, cstride=4, color='rebeccapurple',
                   linewidth=0.5, alpha=0.6)
# Top and bottom circles
ax4.plot(r1 * np.cos(theta), r1 * np.sin(theta), np.zeros_like(theta),
         color='rebeccapurple', linewidth=1.5)
ax4.plot(r2 * np.cos(theta), r2 * np.sin(theta), np.full_like(theta, h_fr),
         color='rebeccapurple', linewidth=1.5)
# Annotations
ax4.plot([0, r1], [0, 0], [0, 0], 'r-', linewidth=2)
ax4.text(0.5, 0, -0.2, '$r_1$', fontsize=11, color='red', ha='center')
ax4.plot([0, r2], [0, 0], [h_fr, h_fr], 'orange', linewidth=2)
ax4.text(0.25, 0, h_fr + 0.15, '$r_2$', fontsize=11, color='orange', ha='center')
ax4.plot([r1 + 0.15, r1 + 0.15], [0, 0], [0, h_fr], 'g-', linewidth=2)
ax4.text(r1 + 0.3, 0, h_fr / 2, '$h$', fontsize=11, color='green')
ax4.set_title('Frustum\n$V=\\frac{1}{3}\\pi h(r_1^2+r_1 r_2+r_2^2)$',
              fontsize=11, fontweight='bold', pad=5)
ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_zlim(-0.5, 2.0)
ax4.set_axis_off()

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
