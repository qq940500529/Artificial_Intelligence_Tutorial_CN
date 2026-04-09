"""
plot_probability_distribution.py
用途：绘制两颗骰子之和的概率分布 + 二项分布 B(10, 0.3)
环境：Python 3.10+, matplotlib, numpy
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from math import comb

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'probability_distribution.png')

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# ============================================================
# Top: Sum of two dice
# ============================================================
ax = axes[0]

# Calculate probabilities
sums = list(range(2, 13))
counts = [0] * 11
for d1 in range(1, 7):
    for d2 in range(1, 7):
        counts[d1 + d2 - 2] += 1
probs = [c / 36 for c in counts]

colors = ['#4CAF50' if s == 7 else '#2196F3' for s in sums]

bars = ax.bar(sums, probs, color=colors, edgecolor='white', linewidth=0.8,
              width=0.7, zorder=3)

# Add probability labels on top of each bar
for s, p, bar in zip(sums, probs, bars):
    label = f'{p:.3f}'
    if s == 7:
        label = f'{p:.3f}'
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.004,
                label, ha='center', va='bottom', fontsize=8,
                fontweight='bold', color='#2E7D32')
    else:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.004,
                label, ha='center', va='bottom', fontsize=7.5,
                color='#333333')

# Highlight X=7
ax.annotate('Max at $X=7$\n$P=1/6$', xy=(7, 6 / 36), xytext=(9.5, 0.16),
            fontsize=10, ha='center', color='#2E7D32', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.5))

ax.set_title('Probability Distribution: Sum of Two Dice', fontsize=13)
ax.set_xlabel('Sum $X$', fontsize=12)
ax.set_ylabel('Probability $P(X)$', fontsize=12)
ax.set_xticks(sums)
ax.set_ylim(0, 0.21)
ax.grid(True, alpha=0.3, axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# Bottom: Binomial distribution B(10, 0.3)
# ============================================================
ax = axes[1]

n, p = 10, 0.3
k_vals = list(range(0, n + 1))
binom_probs = [comb(n, k) * p**k * (1 - p)**(n - k) for k in k_vals]

# Find mode
mode_idx = np.argmax(binom_probs)
colors_b = ['#FF9800' if k == k_vals[mode_idx] else '#9C27B0'
             for k in k_vals]

bars_b = ax.bar(k_vals, binom_probs, color=colors_b, edgecolor='white',
                linewidth=0.8, width=0.7, zorder=3)

# Add probability labels
for k, prob, bar in zip(k_vals, binom_probs, bars_b):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f'{prob:.3f}', ha='center', va='bottom', fontsize=7.5,
            color='#333333')

# Mark E(X) with vertical line
ex = n * p
ax.axvline(ex, color='red', linestyle='--', linewidth=1.5, alpha=0.8,
           zorder=4)
ax.text(ex + 0.15, max(binom_probs) * 0.95,
        f'$E(X)=np={ex:.0f}$', fontsize=10, color='red')

# Mark mode
ax.annotate(f'Mode at $k={k_vals[mode_idx]}$',
            xy=(k_vals[mode_idx], binom_probs[mode_idx]),
            xytext=(k_vals[mode_idx] + 2.5, binom_probs[mode_idx]),
            fontsize=10, ha='center', color='#E65100', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#E65100', lw=1.5))

ax.set_title('Binomial Distribution $B(10,\\ 0.3)$', fontsize=13)
ax.set_xlabel('Number of successes $k$', fontsize=12)
ax.set_ylabel('Probability $P(X=k)$', fontsize=12)
ax.set_xticks(k_vals)
ax.set_ylim(0, max(binom_probs) + 0.06)
ax.grid(True, alpha=0.3, axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
