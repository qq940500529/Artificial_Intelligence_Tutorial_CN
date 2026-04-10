# plot_dice_sample_space.py
# 用途：绘制两枚骰子样本空间（6x6 网格），高亮 sum=7 的事件
# 环境：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'dice_sample_space.png')

fig, ax = plt.subplots(figsize=(8, 7), facecolor='white')

# Build 6x6 sum grid
sums = np.zeros((6, 6), dtype=int)
for i in range(6):
    for j in range(6):
        sums[i, j] = (i + 1) + (j + 1)

# Color mapping: base color by sum value, highlight sum=7
norm = Normalize(vmin=2, vmax=12)
cmap = plt.cm.YlOrBr

for i in range(6):
    for j in range(6):
        s = sums[i, j]
        if s == 7:
            facecolor = '#e74c3c'
            textcolor = 'white'
            fontweight = 'bold'
        else:
            facecolor = cmap(norm(s))
            textcolor = 'black' if norm(s) < 0.7 else 'white'
            fontweight = 'normal'
        rect = plt.Rectangle((j, i), 1, 1, facecolor=facecolor, edgecolor='white',
                              linewidth=2)
        ax.add_patch(rect)
        ax.text(j + 0.5, i + 0.5, str(s), ha='center', va='center',
                fontsize=14, fontweight=fontweight, color=textcolor)

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_xticks(np.arange(0.5, 6.5, 1))
ax.set_xticklabels(range(1, 7), fontsize=12)
ax.set_yticks(np.arange(0.5, 6.5, 1))
ax.set_yticklabels(range(1, 7), fontsize=12)
ax.set_xlabel('Die 1', fontsize=13, fontweight='bold')
ax.set_ylabel('Die 2', fontsize=13, fontweight='bold')
ax.set_title('Sample Space of Two Dice\n(Red = Sum is 7, P = 6/36 = 1/6)',
             fontsize=13, fontweight='bold', pad=12)
ax.invert_yaxis()
ax.set_aspect('equal')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Colorbar for non-highlighted sums
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Sum value', fontsize=11)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
