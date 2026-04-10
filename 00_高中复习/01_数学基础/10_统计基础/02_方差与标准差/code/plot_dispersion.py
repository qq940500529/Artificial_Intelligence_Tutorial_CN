"""
plot_dispersion.py
用途：绘制离散程度对比图（散点带状图 + 正态分布曲线对比）
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
output_path = os.path.join(assets_dir, 'dispersion_comparison.png')

np.random.seed(42)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

mean = 80

# ============================================================
# Top: Dot strip plots comparing two groups
# ============================================================
ax = axes[0]

group_a = np.array([78, 80, 82, 80, 80, 79, 81, 80, 79, 81,
                     80, 78, 82, 80, 81, 79, 80, 80, 81, 79])
group_b = np.array([60, 70, 80, 90, 100, 65, 75, 85, 95, 68,
                     72, 88, 92, 55, 105, 63, 77, 83, 97, 58])

sigma_a = np.std(group_a)
sigma_b = np.std(group_b)

# Strip plot with jitter
jitter_a = np.random.uniform(-0.15, 0.15, len(group_a))
jitter_b = np.random.uniform(-0.15, 0.15, len(group_b))

ax.scatter(group_a, 1 + jitter_a, color='#2196F3', s=60, alpha=0.7,
           edgecolors='white', linewidths=0.5, zorder=5,
           label=f'Group A ($\\sigma \\approx {sigma_a:.1f}$)')
ax.scatter(group_b, 2 + jitter_b, color='#F44336', s=60, alpha=0.7,
           edgecolors='white', linewidths=0.5, zorder=5,
           label=f'Group B ($\\sigma \\approx {sigma_b:.1f}$)')

# Mean line
ax.axvline(mean, color='black', linewidth=2, linestyle='-', alpha=0.8,
           zorder=4)
ax.text(mean, 2.55, f'Mean = {mean}', fontsize=11, ha='center',
        fontweight='bold')

# ±σ bands for Group A
ax.axvspan(mean - sigma_a, mean + sigma_a, ymin=0.05, ymax=0.45,
           alpha=0.15, color='#2196F3', zorder=1)
ax.annotate('', xy=(mean - sigma_a, 0.7), xytext=(mean + sigma_a, 0.7),
            arrowprops=dict(arrowstyle='<->', color='#2196F3', lw=1.5))
ax.text(mean, 0.55, f'$\\pm\\sigma_A={sigma_a:.1f}$', fontsize=9,
        ha='center', color='#1565C0')

# ±σ bands for Group B
ax.axvspan(mean - sigma_b, mean + sigma_b, ymin=0.55, ymax=0.95,
           alpha=0.12, color='#F44336', zorder=1)
ax.annotate('', xy=(mean - sigma_b, 2.45), xytext=(mean + sigma_b, 2.45),
            arrowprops=dict(arrowstyle='<->', color='#F44336', lw=1.5))
ax.text(mean, 2.32, f'$\\pm\\sigma_B={sigma_b:.1f}$', fontsize=9,
        ha='center', color='#C62828')

ax.set_yticks([1, 2])
ax.set_yticklabels(['Group A\n(low var)', 'Group B\n(high var)'],
                   fontsize=10)
ax.set_ylim(0.3, 2.8)
ax.set_xlim(45, 115)
ax.set_xlabel('Score', fontsize=12)
ax.set_title('Dot Strip Plot: Same Mean, Different Variance', fontsize=13)
ax.grid(True, alpha=0.3, axis='x')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper left', fontsize=10)

# ============================================================
# Bottom: Normal distribution curves with different σ
# ============================================================
ax = axes[1]

x = np.linspace(50, 110, 500)

sigma_vals = [3, 8, 15]
colors = ['#2196F3', '#FF9800', '#F44336']
labels = ['$\\sigma=3$ (concentrated)', '$\\sigma=8$ (moderate)',
          '$\\sigma=15$ (spread out)']

for sigma, color, label in zip(sigma_vals, colors, labels):
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * \
        np.exp(-0.5 * ((x - mean) / sigma)**2)
    ax.plot(x, y, color=color, linewidth=2.5, label=label)
    # Fill under curve lightly
    ax.fill_between(x, y, alpha=0.1, color=color)

# Mean line
ax.axvline(mean, color='black', linewidth=1.5, linestyle='--', alpha=0.6)
ax.set_xlim(50, 110)
y_max = (1 / (3 * np.sqrt(2 * np.pi)))
ax.text(mean + 0.5, y_max * 0.85, f'$\\mu={mean}$', fontsize=11,
        color='black')

ax.set_xlabel('Value $x$', fontsize=12)
ax.set_ylabel('Probability Density $f(x)$', fontsize=12)
ax.set_title('Normal Distributions: Same Mean $\\mu$, Different $\\sigma$',
             fontsize=13)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10, loc='upper right')

plt.tight_layout()
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
