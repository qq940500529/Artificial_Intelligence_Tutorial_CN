# plot_binomial.py
# 用途：绘制二项分布 B(10, p) 在 p=0.2, 0.5, 0.8 下的概率质量函数
# 环境：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt
from math import comb

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'binomial_distribution.png')

def binomial_pmf(n, p, k):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

n = 10
k_vals = np.arange(0, n + 1)
p_values = [0.2, 0.5, 0.8]
colors = ['#3498db', '#2ecc71', '#e74c3c']
labels = ['$p = 0.2$', '$p = 0.5$', '$p = 0.8$']

fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')

bar_width = 0.25
offsets = [-bar_width, 0, bar_width]

for idx, (p, color, label) in enumerate(zip(p_values, colors, labels)):
    probs = [binomial_pmf(n, p, k) for k in k_vals]
    positions = k_vals + offsets[idx]
    bars = ax.bar(positions, probs, width=bar_width, color=color, alpha=0.8,
                  edgecolor='white', linewidth=0.8, label=label)
    # Highlight peak
    peak_k = int(np.argmax(probs))
    ax.bar(positions[peak_k], probs[peak_k], width=bar_width, color=color,
           edgecolor='black', linewidth=2)
    ax.text(positions[peak_k], probs[peak_k] + 0.008,
            f'{probs[peak_k]:.3f}', ha='center', va='bottom', fontsize=8,
            fontweight='bold', color=color)

ax.set_xlabel('$k$ (number of successes)', fontsize=12, fontweight='bold')
ax.set_ylabel('$P(X = k)$', fontsize=12, fontweight='bold')
ax.set_title('Binomial Distribution $B(10, p)$', fontsize=14, fontweight='bold')
ax.set_xticks(k_vals)
ax.set_xticklabels(k_vals, fontsize=11)
ax.legend(fontsize=12, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3)
ax.set_xlim(-0.5, 10.5)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
