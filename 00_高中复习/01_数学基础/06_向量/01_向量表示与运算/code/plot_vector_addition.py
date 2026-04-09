# plot_vector_addition.py
# Purpose: Visualize vector addition using parallelogram and triangle rules
# Requirements: Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Font settings for cross-platform compatibility
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Output path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left panel: Triangle Rule ---
a = np.array([3, 1])
b = np.array([1, 2.5])
c = a + b

ax1.annotate('', xy=a, xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#2196F3', lw=2.5))
ax1.annotate('', xy=c, xytext=a,
             arrowprops=dict(arrowstyle='->', color='#FF9800', lw=2.5))
ax1.annotate('', xy=c, xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#E91E63', lw=2.8))

ax1.text(a[0] / 2 - 0.15, a[1] / 2 + 0.3, r'$\vec{a}$',
         fontsize=16, color='#2196F3', fontweight='bold')
ax1.text((a[0] + c[0]) / 2 + 0.2, (a[1] + c[1]) / 2 + 0.15, r'$\vec{b}$',
         fontsize=16, color='#FF9800', fontweight='bold')
ax1.text(c[0] / 2 + 0.15, c[1] / 2 - 0.35, r'$\vec{a}+\vec{b}$',
         fontsize=15, color='#E91E63', fontweight='bold')

ax1.set_xlim(-0.5, 5.5)
ax1.set_ylim(-0.5, 4.5)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.set_title('Triangle Rule', fontsize=14, fontweight='bold')
ax1.set_xlabel('$x$', fontsize=13)
ax1.set_ylabel('$y$', fontsize=13)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.plot(0, 0, 'ko', markersize=5)
ax1.text(-0.3, -0.3, 'O', fontsize=12)

# --- Right panel: Parallelogram Rule ---
ax2.annotate('', xy=a, xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#2196F3', lw=2.5))
ax2.annotate('', xy=b, xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#FF9800', lw=2.5))
ax2.annotate('', xy=c, xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#E91E63', lw=2.8))

# Dashed parallelogram lines
ax2.plot([a[0], c[0]], [a[1], c[1]], '--', color='gray', alpha=0.5, lw=1.2)
ax2.plot([b[0], c[0]], [b[1], c[1]], '--', color='gray', alpha=0.5, lw=1.2)

ax2.text(a[0] / 2 - 0.15, a[1] / 2 + 0.3, r'$\vec{a}$',
         fontsize=16, color='#2196F3', fontweight='bold')
ax2.text(b[0] / 2 - 0.4, b[1] / 2, r'$\vec{b}$',
         fontsize=16, color='#FF9800', fontweight='bold')
ax2.text(c[0] / 2 + 0.15, c[1] / 2 - 0.35, r'$\vec{a}+\vec{b}$',
         fontsize=15, color='#E91E63', fontweight='bold')

# Shade the parallelogram
parallelogram = plt.Polygon(
    [(0, 0), a, c, b], alpha=0.08, color='#9C27B0'
)
ax2.add_patch(parallelogram)

ax2.set_xlim(-0.5, 5.5)
ax2.set_ylim(-0.5, 4.5)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.set_title('Parallelogram Rule', fontsize=14, fontweight='bold')
ax2.set_xlabel('$x$', fontsize=13)
ax2.set_ylabel('$y$', fontsize=13)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.plot(0, 0, 'ko', markersize=5)
ax2.text(-0.3, -0.3, 'O', fontsize=12)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'vector_addition.png'),
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Image saved to assets/vector_addition.png")
