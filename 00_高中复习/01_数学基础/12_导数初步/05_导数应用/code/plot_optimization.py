# 文件：code/plot_optimization.py
# 用途：绘制围栏优化问题 S(x)=x(60-2x) 的面积函数与最大值
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
output_path = os.path.join(output_dir, 'optimization.png')

# Area function S(x) = x(60 - 2x) = 60x - 2x²
def S(x):
    return 60 * x - 2 * x**2

x = np.linspace(0, 30, 500)
x_max = 15.0
S_max = S(x_max)  # 450

fig, ax = plt.subplots(figsize=(9, 6))

# Shade the valid domain
ax.fill_between(x, S(x), alpha=0.12, color='#1F77B4', zorder=1)

# Plot the curve
ax.plot(x, S(x), color='#1F77B4', linewidth=2.5, zorder=3,
        label='$S(x) = x(60 - 2x)$')

# Mark the maximum point with a star
ax.plot(x_max, S_max, '*', color='#D62728', markersize=20, zorder=5,
        markeredgecolor='black', markeredgewidth=0.8,
        label=f'Maximum: $({x_max:.0f},\\, {S_max:.0f})$')

# Dashed horizontal tangent line at the maximum
ax.plot([5, 25], [S_max, S_max], '--', color='#D62728',
        linewidth=1.5, alpha=0.7, zorder=4)
ax.text(25.5, S_max, 'slope = 0', fontsize=11, color='#D62728',
        va='center')

# Vertical dashed line from max point to x-axis
ax.plot([x_max, x_max], [0, S_max], ':', color='gray',
        linewidth=1.2, zorder=2)

# Annotation with formula
ax.annotate(
    "$S'(x) = 0$\n$60 - 4x = 0$\n$x = 15$ → maximum",
    xy=(x_max, S_max), xytext=(22, 380),
    fontsize=12, ha='center',
    arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow',
              edgecolor='gray', alpha=0.95))

# Mark domain endpoints
ax.plot(0, 0, 'o', color='gray', markersize=8, zorder=4, fillstyle='none',
        linewidth=2)
ax.plot(30, 0, 'o', color='gray', markersize=8, zorder=4, fillstyle='none',
        linewidth=2)
ax.text(0.5, -25, '$x=0$', fontsize=10, color='gray', ha='center')
ax.text(29.5, -25, '$x=30$', fontsize=10, color='gray', ha='center')

# Domain annotation
ax.annotate('', xy=(1, -45), xytext=(29, -45),
            arrowprops=dict(arrowstyle='<->', color='#666666', lw=1.5))
ax.text(15, -55, 'Valid domain: $0 < x < 30$',
        fontsize=11, ha='center', color='#666666')

# Increasing / decreasing labels
ax.text(7, 280, r"$S'(x) > 0$" + "\nincreasing",
        fontsize=11, ha='center', color='#2CA02C', fontstyle='italic')
ax.text(23, 280, r"$S'(x) < 0$" + "\ndecreasing",
        fontsize=11, ha='center', color='#D62728', fontstyle='italic')

# Styling
ax.set_xlabel('Width $x$ (meters)', fontsize=13)
ax.set_ylabel('Area $S(x)$ (square meters)', fontsize=13)
ax.set_title('Optimization: Maximum Area with 60m of Fencing',
             fontsize=14, pad=12)
ax.legend(fontsize=11, loc='upper left')
ax.set_xlim(-1, 32)
ax.set_ylim(-70, 500)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Plot saved to {output_path}")
