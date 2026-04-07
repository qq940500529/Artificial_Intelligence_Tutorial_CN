# 文件：code/plot_logarithmic.py
# 绘制对数函数图像及其与指数函数的反函数关系
# 环境要求：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：不同底数的对数函数
ax1 = axes[0]
x = np.linspace(0.01, 10, 300)

for a, color, label in [(2, '#2196f3', '$y = \\log_2 x$'),
                          (np.e, '#4caf50', '$y = \\ln x$'),
                          (10, '#f44336', '$y = \\lg x$'),
                          (0.5, '#9c27b0', '$y = \\log_{0.5} x$')]:
    y = np.log(x) / np.log(a)
    ax1.plot(x, y, color=color, linewidth=2, label=label)

ax1.axhline(y=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax1.axvline(x=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax1.axvline(x=1, color='gray', linewidth=0.5, linestyle=':', alpha=0.3)
ax1.plot(1, 0, 'ko', markersize=6, zorder=5)
ax1.annotate('$(1, 0)$', xy=(1, 0), xytext=(1.8, -1.5),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='black'))
ax1.set_xlim(-0.5, 10)
ax1.set_ylim(-4, 4)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$y$', fontsize=12)
ax1.set_title('Logarithmic Functions', fontsize=13)
ax1.legend(fontsize=10, loc='lower right')
ax1.grid(alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# 右图：指数函数与对数函数的反函数关系
ax2 = axes[1]
x1 = np.linspace(-2, 3.5, 300)
x2 = np.linspace(0.01, 10, 300)
x_sym = np.linspace(-2, 10, 300)

ax2.plot(x1, 2**x1, color='#2196f3', linewidth=2, label='$y = 2^x$')
ax2.plot(x2, np.log2(x2), color='#f44336', linewidth=2, label='$y = \\log_2 x$')
ax2.plot(x_sym, x_sym, color='gray', linewidth=1, linestyle='--', label='$y = x$')

ax2.plot(0, 1, 'o', color='#2196f3', markersize=6, zorder=5)
ax2.plot(1, 0, 'o', color='#f44336', markersize=6, zorder=5)
ax2.annotate('$(0, 1)$', xy=(0, 1), xytext=(-1.5, 1.5), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#2196f3'))
ax2.annotate('$(1, 0)$', xy=(1, 0), xytext=(2, -1.5), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#f44336'))

ax2.set_xlim(-2, 8)
ax2.set_ylim(-2, 8)
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_title('Inverse Function Symmetry', fontsize=13)
ax2.legend(fontsize=10, loc='lower right')
ax2.set_aspect('equal')
ax2.grid(alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, '..', 'assets', 'logarithmic_functions.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"图片已保存到 {output_path}")
