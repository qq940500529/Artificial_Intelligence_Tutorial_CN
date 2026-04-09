"""
plot_parametric_curves.py
用途：绘制四种经典参数曲线（圆、椭圆、摆线、利萨如图形）
环境：Python 3.10+, matplotlib, numpy
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Output path based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'parametric_curves.png')

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# --- Top-left: Circle ---
ax = axes[0, 0]
theta = np.linspace(0, 2 * np.pi, 300)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
ax.plot(x_circle, y_circle, 'b-', linewidth=2)

# Mark several theta values with arrows showing direction
mark_angles = [0, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2]
labels = [r'$\theta=0$', r'$\theta=\pi/4$', r'$\theta=\pi/2$',
          r'$\theta=\pi$', r'$\theta=3\pi/2$']
for ang, label in zip(mark_angles, labels):
    px, py = np.cos(ang), np.sin(ang)
    ax.plot(px, py, 'ro', markersize=7, zorder=5)
    offset_x = 0.15 * np.cos(ang)
    offset_y = 0.15 * np.sin(ang)
    ax.annotate(label, (px, py), textcoords="offset points",
                xytext=(offset_x * 60, offset_y * 60),
                fontsize=8, ha='center', va='center')

# Direction arrows
for i in range(0, 250, 60):
    idx = i
    dx = x_circle[idx + 5] - x_circle[idx]
    dy = y_circle[idx + 5] - y_circle[idx]
    ax.annotate('', xy=(x_circle[idx + 5], y_circle[idx + 5]),
                xytext=(x_circle[idx], y_circle[idx]),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.set_title('Circle: $x=\\cos\\theta,\\ y=\\sin\\theta$', fontsize=11)
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# --- Top-right: Ellipse ---
ax = axes[0, 1]
a_ell, b_ell = 3, 2
x_ell = a_ell * np.cos(theta)
y_ell = b_ell * np.sin(theta)
ax.plot(x_ell, y_ell, 'g-', linewidth=2)

# Direction arrows
for i in range(0, 250, 60):
    ax.annotate('', xy=(x_ell[i + 5], y_ell[i + 5]),
                xytext=(x_ell[i], y_ell[i]),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# Mark semi-axes
ax.plot([0, a_ell], [0, 0], 'k--', alpha=0.5)
ax.plot([0, 0], [0, b_ell], 'k--', alpha=0.5)
ax.annotate('$a=3$', (1.5, -0.3), fontsize=10, ha='center')
ax.annotate('$b=2$', (0.3, 1.0), fontsize=10, ha='left')
ax.plot(a_ell, 0, 'ro', markersize=6, zorder=5)
ax.plot(0, b_ell, 'ro', markersize=6, zorder=5)
ax.plot(-a_ell, 0, 'ro', markersize=6, zorder=5)
ax.plot(0, -b_ell, 'ro', markersize=6, zorder=5)

ax.set_title('Ellipse: $x=3\\cos\\theta,\\ y=2\\sin\\theta$', fontsize=11)
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# --- Bottom-left: Cycloid ---
ax = axes[1, 0]
t_cyc = np.linspace(0, 4 * np.pi, 500)
r_cyc = 1
x_cyc = r_cyc * (t_cyc - np.sin(t_cyc))
y_cyc = r_cyc * (1 - np.cos(t_cyc))
ax.plot(x_cyc, y_cyc, 'm-', linewidth=2)

# Direction arrows
for i in range(0, 450, 100):
    ax.annotate('', xy=(x_cyc[i + 5], y_cyc[i + 5]),
                xytext=(x_cyc[i], y_cyc[i]),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))

# Mark cusps
for k in range(3):
    cx = r_cyc * 2 * np.pi * k
    ax.plot(cx, 0, 'ro', markersize=7, zorder=5)

ax.set_title('Cycloid: $x=t-\\sin t,\\ y=1-\\cos t$', fontsize=11)
ax.set_xlim(-0.5, 13)
ax.set_ylim(-0.3, 2.8)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# --- Bottom-right: Lissajous ---
ax = axes[1, 1]
t_lis = np.linspace(0, 2 * np.pi, 1000)
x_lis = np.sin(3 * t_lis)
y_lis = np.sin(2 * t_lis)
ax.plot(x_lis, y_lis, color='darkorange', linewidth=2)

# Direction arrows
for i in range(0, 900, 200):
    ax.annotate('', xy=(x_lis[i + 5], y_lis[i + 5]),
                xytext=(x_lis[i], y_lis[i]),
                arrowprops=dict(arrowstyle='->', color='darkorange', lw=1.5))

# Mark start point
ax.plot(x_lis[0], y_lis[0], 'ro', markersize=7, zorder=5)
ax.annotate('$t=0$', (x_lis[0], y_lis[0]), textcoords="offset points",
            xytext=(10, 10), fontsize=9)

ax.set_title('Lissajous: $x=\\sin 3t,\\ y=\\sin 2t$', fontsize=11)
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

plt.tight_layout()
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
