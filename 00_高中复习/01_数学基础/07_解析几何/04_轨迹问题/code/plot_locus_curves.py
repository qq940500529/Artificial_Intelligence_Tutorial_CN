"""
plot_locus_curves.py
用途：绘制四种经典轨迹曲线（椭圆、双曲线、抛物线、阿波罗尼斯圆）
环境：Python 3.10+, matplotlib, numpy
"""

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'locus_curves.png')

fig, axes = plt.subplots(2, 2, figsize=(11, 10))

theta = np.linspace(0, 2 * np.pi, 500)

# ============================================================
# Top-left: Ellipse with foci and distance sum
# ============================================================
ax = axes[0, 0]
a, b = 3, np.sqrt(5)
c = 2  # c^2 = a^2 - b^2

x_ell = a * np.cos(theta)
y_ell = b * np.sin(theta)
ax.plot(x_ell, y_ell, 'b-', linewidth=2)

# Foci
ax.plot(-c, 0, 'ko', markersize=7, zorder=5)
ax.plot(c, 0, 'ko', markersize=7, zorder=5)
ax.text(-c, -0.45, '$F_1$', fontsize=12, ha='center', fontweight='bold')
ax.text(c, -0.45, '$F_2$', fontsize=12, ha='center', fontweight='bold')

# Point P on ellipse
t_p = np.pi / 3.5
px = a * np.cos(t_p)
py = b * np.sin(t_p)
ax.plot(px, py, 'ro', markersize=8, zorder=5)
ax.text(px + 0.15, py + 0.25, '$P$', fontsize=12, color='red',
        fontweight='bold')

# Distance lines
ax.plot([-c, px], [0, py], 'r--', linewidth=1.5, alpha=0.7)
ax.plot([c, px], [0, py], 'r--', linewidth=1.5, alpha=0.7)

ax.text(-0.3, 1.8, f'$|PF_1|+|PF_2|=2a={2*a}$', fontsize=10,
        ha='center', bbox=dict(facecolor='lightyellow', alpha=0.8,
                                edgecolor='gray', boxstyle='round'))

ax.set_title('Ellipse: $|PF_1|+|PF_2|=2a$', fontsize=12)
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-3.2, 3.2)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# Top-right: Hyperbola with foci
# ============================================================
ax = axes[0, 1]
a_h, b_h = 2, 1.5
c_h = np.sqrt(a_h**2 + b_h**2)

# Right branch
t_hyp = np.linspace(-1.2, 1.2, 300)
x_hr = a_h * np.cosh(t_hyp)
y_hr = b_h * np.sinh(t_hyp)
ax.plot(x_hr, y_hr, 'b-', linewidth=2)
# Left branch
ax.plot(-x_hr, y_hr, 'b-', linewidth=2)

# Asymptotes
x_asym = np.linspace(-5, 5, 100)
ax.plot(x_asym, (b_h / a_h) * x_asym, 'k--', alpha=0.3, linewidth=1)
ax.plot(x_asym, -(b_h / a_h) * x_asym, 'k--', alpha=0.3, linewidth=1)

# Foci
ax.plot(-c_h, 0, 'ko', markersize=7, zorder=5)
ax.plot(c_h, 0, 'ko', markersize=7, zorder=5)
ax.text(-c_h, -0.5, '$F_1$', fontsize=12, ha='center', fontweight='bold')
ax.text(c_h, -0.5, '$F_2$', fontsize=12, ha='center', fontweight='bold')

# Point P on right branch
idx_p = 200
px_h = x_hr[idx_p]
py_h = y_hr[idx_p]
ax.plot(px_h, py_h, 'ro', markersize=8, zorder=5)
ax.text(px_h + 0.2, py_h + 0.2, '$P$', fontsize=12, color='red',
        fontweight='bold')

# Distance lines
ax.plot([-c_h, px_h], [0, py_h], 'r--', linewidth=1.5, alpha=0.7)
ax.plot([c_h, px_h], [0, py_h], 'r--', linewidth=1.5, alpha=0.7)

ax.text(0, 2.5, '$||PF_1|-|PF_2||=2a$', fontsize=10, ha='center',
        bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='gray',
                  boxstyle='round'))

ax.set_title('Hyperbola: $||PF_1|-|PF_2||=2a$', fontsize=12)
ax.set_xlim(-5, 5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# Bottom-left: Parabola with focus and directrix
# ============================================================
ax = axes[1, 0]
p_val = 2
focus = (p_val / 2, 0)  # Focus at (1, 0)
directrix_x = -p_val / 2  # x = -1

y_par = np.linspace(-4, 4, 400)
x_par = y_par**2 / (2 * p_val)
ax.plot(x_par, y_par, 'b-', linewidth=2)

# Focus
ax.plot(focus[0], focus[1], 'ko', markersize=7, zorder=5)
ax.text(focus[0] + 0.15, focus[1] - 0.4, '$F$', fontsize=12,
        ha='left', fontweight='bold')

# Directrix
ax.axvline(directrix_x, color='gray', linewidth=2, linestyle='--')
ax.text(directrix_x - 0.15, 3.5, 'directrix', fontsize=9, ha='right',
        color='gray', rotation=90)

# Point P on parabola
y_p = 2.5
x_p = y_p**2 / (2 * p_val)
ax.plot(x_p, y_p, 'ro', markersize=8, zorder=5)
ax.text(x_p + 0.2, y_p + 0.2, '$P$', fontsize=12, color='red',
        fontweight='bold')

# Equal distance lines
ax.plot([focus[0], x_p], [focus[1], y_p], 'r-', linewidth=1.5, alpha=0.7)
ax.plot([directrix_x, x_p], [y_p, y_p], 'r-', linewidth=1.5, alpha=0.7)

# Foot of perpendicular
ax.plot(directrix_x, y_p, 'ko', markersize=5, zorder=5)
ax.text(directrix_x - 0.1, y_p + 0.3, '$H$', fontsize=10, ha='right')

# Distance labels
mid_pf_x = (focus[0] + x_p) / 2
mid_pf_y = (focus[1] + y_p) / 2
ax.text(mid_pf_x - 0.3, mid_pf_y + 0.1, '$|PF|$', fontsize=9, color='red')
mid_ph_x = (directrix_x + x_p) / 2
ax.text(mid_ph_x, y_p + 0.3, '$|PH|$', fontsize=9, color='red')

ax.text(2.5, -3.5, '$|PF|=|PH|$', fontsize=10, ha='center',
        bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='gray',
                  boxstyle='round'))

ax.set_title('Parabola: $|PF|=|PH|$ (dist to directrix)', fontsize=12)
ax.set_xlim(-2, 5)
ax.set_ylim(-4.5, 4.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# Bottom-right: Apollonius circle
# ============================================================
ax = axes[1, 1]

# Points A and B
A = np.array([-2, 0])
B = np.array([2, 0])
k = 2  # |PA|/|PB| = k

# Apollonius circle for |PA|/|PB| = k with A(-2,0), B(2,0), k=2
# From |PA|^2 = k^2 |PB|^2:
#   (x+2)^2 + y^2 = 4[(x-2)^2 + y^2]
#   => 3x^2 + 3y^2 - 20x + 12 = 0
#   => (x - 10/3)^2 + y^2 = 64/9
center_x = 10 / 3
radius = 8 / 3

circle_theta = np.linspace(0, 2 * np.pi, 300)
x_apo = center_x + radius * np.cos(circle_theta)
y_apo = radius * np.sin(circle_theta)
ax.plot(x_apo, y_apo, 'b-', linewidth=2)

# Points A and B
ax.plot(A[0], A[1], 'ko', markersize=7, zorder=5)
ax.plot(B[0], B[1], 'ko', markersize=7, zorder=5)
ax.text(A[0], -0.45, '$A$', fontsize=12, ha='center', fontweight='bold')
ax.text(B[0], -0.45, '$B$', fontsize=12, ha='center', fontweight='bold')

# Center of Apollonius circle
ax.plot(center_x, 0, 'g+', markersize=10, markeredgewidth=2, zorder=5)

# Point P on the circle
t_p2 = np.pi / 3
px_a = center_x + radius * np.cos(t_p2)
py_a = radius * np.sin(t_p2)
ax.plot(px_a, py_a, 'ro', markersize=8, zorder=5)
ax.text(px_a + 0.15, py_a + 0.25, '$P$', fontsize=12, color='red',
        fontweight='bold')

# Distance lines
ax.plot([A[0], px_a], [A[1], py_a], 'r--', linewidth=1.5, alpha=0.7)
ax.plot([B[0], px_a], [B[1], py_a], 'r--', linewidth=1.5, alpha=0.7)

ax.text(center_x, -3.0, f'$|PA|/|PB|=k={k}$', fontsize=10, ha='center',
        bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='gray',
                  boxstyle='round'))

ax.set_title('Apollonius Circle: $|PA|/|PB|=k$', fontsize=12)
ax.set_xlim(-4, 7.5)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
