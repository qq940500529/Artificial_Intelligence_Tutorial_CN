# plot_derivative_rules.py
# 用途：绘制四组函数及其导数的对比图，并在指定点标注切线
# 环境：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'derivative_rules.png')

fig, axes = plt.subplots(2, 2, figsize=(12, 9), facecolor='white')

# Shared tangent-line helper
def draw_tangent(ax, x0, y0, slope, length=1.0, color='green'):
    dx = length / 2
    x_t = np.array([x0 - dx, x0 + dx])
    y_t = y0 + slope * (x_t - x0)
    ax.plot(x_t, y_t, color=color, linewidth=2, linestyle='-', alpha=0.8,
            label=f'Tangent at $x={x0}$')
    ax.scatter([x0], [y0], color=color, s=70, zorder=5, edgecolors='black', linewidths=0.8)

def style_ax(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.6)
    ax.axvline(0, color='black', linewidth=0.6)
    ax.legend(fontsize=9, loc='best')

# ---------- 1. f(x)=x², f'(x)=2x ----------
ax = axes[0, 0]
x = np.linspace(-3, 3, 300)
y = x ** 2
dy = 2 * x
ax.plot(x, y, 'b-', linewidth=2.2, label=r"$f(x)=x^2$")
ax.plot(x, dy, 'r--', linewidth=2, label=r"$f'(x)=2x$")
x0 = 1.0
draw_tangent(ax, x0, x0**2, 2*x0, length=2.0)
ax.set_title(r"Power Rule: $(x^2)' = 2x$", fontsize=12, fontweight='bold')
ax.set_xlabel('$x$', fontsize=10)
ax.set_ylabel('$y$', fontsize=10)
ax.set_ylim(-4, 9)
style_ax(ax)

# ---------- 2. f(x)=sin(x), f'(x)=cos(x) ----------
ax = axes[0, 1]
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = np.sin(x)
dy = np.cos(x)
ax.plot(x, y, 'b-', linewidth=2.2, label=r"$f(x)=\sin x$")
ax.plot(x, dy, 'r--', linewidth=2, label=r"$f'(x)=\cos x$")
x0 = np.pi / 4
draw_tangent(ax, x0, np.sin(x0), np.cos(x0), length=2.0)
ax.set_title(r"Trig Rule: $(\sin x)' = \cos x$", fontsize=12, fontweight='bold')
ax.set_xlabel('$x$', fontsize=10)
ax.set_ylabel('$y$', fontsize=10)
style_ax(ax)

# ---------- 3. f(x)=eˣ, f'(x)=eˣ ----------
ax = axes[1, 0]
x = np.linspace(-2, 2.5, 300)
y = np.exp(x)
ax.plot(x, y, 'b-', linewidth=2.2, label=r"$f(x)=e^x$")
ax.plot(x, y, 'r--', linewidth=2, alpha=0.7, label=r"$f'(x)=e^x$ (same!)")
x0 = 1.0
draw_tangent(ax, x0, np.exp(x0), np.exp(x0), length=1.5)
ax.set_title(r"Exp Rule: $(e^x)' = e^x$", fontsize=12, fontweight='bold')
ax.set_xlabel('$x$', fontsize=10)
ax.set_ylabel('$y$', fontsize=10)
ax.set_ylim(-1, 12)
style_ax(ax)

# ---------- 4. f(x)=ln(x), f'(x)=1/x ----------
ax = axes[1, 1]
x = np.linspace(0.2, 5, 300)
y = np.log(x)
dy = 1.0 / x
ax.plot(x, y, 'b-', linewidth=2.2, label=r"$f(x)=\ln x$")
ax.plot(x, dy, 'r--', linewidth=2, label=r"$f'(x)=1/x$")
x0 = 1.0
draw_tangent(ax, x0, np.log(x0), 1.0 / x0, length=2.0)
ax.set_title(r"Log Rule: $(\ln x)' = 1/x$", fontsize=12, fontweight='bold')
ax.set_xlabel('$x$', fontsize=10)
ax.set_ylabel('$y$', fontsize=10)
ax.set_ylim(-2, 6)
style_ax(ax)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
