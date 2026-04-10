"""
plot_vector_decomposition.py
用途：绘制向量坐标分解示意图（标准基底、分量投影）
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
output_path = os.path.join(assets_dir, 'vector_decomposition.png')

fig, ax = plt.subplots(figsize=(8, 6))

origin = np.array([0, 0])
v = np.array([3, 2])

# Grid background
ax.set_xlim(-0.8, 4.5)
ax.set_ylim(-0.8, 3.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Dashed projection lines
ax.plot([v[0], v[0]], [0, v[1]], 'k--', alpha=0.4, linewidth=1)
ax.plot([0, v[0]], [v[1], v[1]], 'k--', alpha=0.4, linewidth=1)

# Component vectors (3i and 2j) - draw first so main vectors overlay
# 3i component (along x-axis)
ax.annotate('', xy=(3, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#2196F3', lw=2.5,
                            shrinkA=0, shrinkB=0))
ax.text(1.5, -0.35, r'$3\vec{i}$', fontsize=14, ha='center',
        color='#2196F3', fontweight='bold')

# 2j component (along y-axis from (3,0) to (3,2))
ax.annotate('', xy=(3, 2), xytext=(3, 0),
            arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=2.5,
                            shrinkA=0, shrinkB=0))
ax.text(3.45, 1.0, r'$2\vec{j}$', fontsize=14, ha='left',
        color='#4CAF50', fontweight='bold')

# Basis vectors i and j (unit length, blue)
ax.annotate('', xy=(1, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='navy', lw=2,
                            shrinkA=0, shrinkB=0))
ax.text(0.5, -0.55, r'$\vec{i}=(1,0)$', fontsize=11, ha='center',
        color='navy')

ax.annotate('', xy=(0, 1), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='navy', lw=2,
                            shrinkA=0, shrinkB=0))
ax.text(-0.55, 0.5, r'$\vec{j}=(0,1)$', fontsize=11, ha='center',
        color='navy', rotation=90)

# Main vector v = (3, 2) in red
ax.annotate('', xy=(v[0], v[1]), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='red', lw=3,
                            shrinkA=0, shrinkB=0))
ax.text(1.3, 1.3, r'$\vec{v}=(3,2)$', fontsize=14, ha='center',
        color='red', fontweight='bold')

# Mark the endpoint
ax.plot(v[0], v[1], 'ro', markersize=8, zorder=5)

# Decomposition equation
ax.text(0.5, 3.0, r'$\vec{v} = 3\vec{i} + 2\vec{j}$',
        fontsize=15, ha='left', color='black',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.9))

# Origin label
ax.text(-0.15, -0.25, '$O$', fontsize=12, ha='center')

# Coordinate markers
ax.plot(v[0], 0, 'ko', markersize=5, zorder=4)
ax.text(v[0], -0.25, '$(3,0)$', fontsize=9, ha='center')
ax.plot(0, v[1], 'ko', markersize=5, zorder=4)

# Axes
ax.axhline(0, color='k', linewidth=0.8)
ax.axvline(0, color='k', linewidth=0.8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$y$', fontsize=13)
ax.set_title('Vector Decomposition: $\\vec{v} = 3\\vec{i} + 2\\vec{j}$',
             fontsize=14)

plt.tight_layout()
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
