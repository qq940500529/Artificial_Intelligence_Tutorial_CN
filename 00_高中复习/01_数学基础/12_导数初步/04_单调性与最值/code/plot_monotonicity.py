# 文件：code/plot_monotonicity.py
# 用途：绘制 f(x)=x³-3x 的单调性与导函数符号对照图
# 环境要求：Python 3.10+, matplotlib>=3.7, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Output path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'monotonicity.png')

# Functions
def f(x):
    return x**3 - 3*x

def f_prime(x):
    return 3*x**2 - 3

x = np.linspace(-2.5, 2.5, 500)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left subplot: f(x) with colored increasing/decreasing regions ---
ax1.plot(x, f(x), 'k-', linewidth=2.2, zorder=3)

# Colored segments: green for increasing, red for decreasing
mask_inc1 = x <= -1
mask_dec = (x >= -1) & (x <= 1)
mask_inc2 = x >= 1

ax1.fill_between(x[mask_inc1], f(x[mask_inc1]), alpha=0.15,
                 color='#2CA02C', zorder=1)
ax1.fill_between(x[mask_dec], f(x[mask_dec]), alpha=0.15,
                 color='#D62728', zorder=1)
ax1.fill_between(x[mask_inc2], f(x[mask_inc2]), alpha=0.15,
                 color='#2CA02C', zorder=1)

# Plot colored curve segments for emphasis
ax1.plot(x[mask_inc1], f(x[mask_inc1]), color='#2CA02C', linewidth=3,
         zorder=4, label="$f'(x) > 0$ (increasing)")
ax1.plot(x[mask_dec], f(x[mask_dec]), color='#D62728', linewidth=3,
         zorder=4, label="$f'(x) < 0$ (decreasing)")
ax1.plot(x[mask_inc2], f(x[mask_inc2]), color='#2CA02C', linewidth=3,
         zorder=4)

# Critical points
ax1.plot(-1, f(-1), 'r^', markersize=14, zorder=5,
         markeredgecolor='black', markeredgewidth=0.8)
ax1.plot(1, f(1), 'bv', markersize=14, zorder=5,
         markeredgecolor='black', markeredgewidth=0.8)

ax1.annotate(f'Local max\n$(-1,\\, {f(-1):.0f})$',
             xy=(-1, f(-1)), xytext=(-2.2, 3.5),
             fontsize=11, ha='center', color='#D62728',
             arrowprops=dict(arrowstyle='->', color='#D62728', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.3', fc='white',
                       ec='#D62728', alpha=0.9))
ax1.annotate(f'Local min\n$(1,\\, {f(1):.0f})$',
             xy=(1, f(1)), xytext=(2.2, -3.5),
             fontsize=11, ha='center', color='#1F77B4',
             arrowprops=dict(arrowstyle='->', color='#1F77B4', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.3', fc='white',
                       ec='#1F77B4', alpha=0.9))

ax1.axhline(y=0, color='gray', linewidth=0.5, zorder=1)
ax1.set_xlabel('$x$', fontsize=14)
ax1.set_ylabel('$f(x)$', fontsize=14)
ax1.set_title('$f(x) = x^3 - 3x$', fontsize=15, pad=10)
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# --- Right subplot: f'(x) with shading above/below zero ---
ax2.plot(x, f_prime(x), 'k-', linewidth=2.2, zorder=3)
ax2.axhline(y=0, color='gray', linewidth=1.0, zorder=2)

# Shading: green above zero, red below zero
ax2.fill_between(x, f_prime(x), 0, where=(f_prime(x) >= 0),
                 alpha=0.25, color='#2CA02C', zorder=1,
                 label="$f'(x) \\geq 0$ → increasing")
ax2.fill_between(x, f_prime(x), 0, where=(f_prime(x) <= 0),
                 alpha=0.25, color='#D62728', zorder=1,
                 label="$f'(x) \\leq 0$ → decreasing")

# Zero crossings
ax2.plot([-1, 1], [0, 0], 'ko', markersize=9, zorder=5)
ax2.annotate('$x = -1$', xy=(-1, 0), xytext=(-1.8, 4),
             fontsize=11, ha='center',
             arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
ax2.annotate('$x = 1$', xy=(1, 0), xytext=(1.8, 4),
             fontsize=11, ha='center',
             arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

# Sign annotations
ax2.text(-2.0, 5.5, '$+$', fontsize=22, color='#2CA02C',
         fontweight='bold', ha='center')
ax2.text(0, -2.0, '$-$', fontsize=22, color='#D62728',
         fontweight='bold', ha='center')
ax2.text(2.0, 5.5, '$+$', fontsize=22, color='#2CA02C',
         fontweight='bold', ha='center')

ax2.set_xlabel('$x$', fontsize=14)
ax2.set_ylabel("$f'(x)$", fontsize=14)
ax2.set_title("$f'(x) = 3x^2 - 3$", fontsize=15, pad=10)
ax2.legend(fontsize=10, loc='upper center')
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Plot saved to {output_path}")
