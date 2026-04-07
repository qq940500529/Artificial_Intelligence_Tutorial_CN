# 文件：code/plot_exponential.py
# 绘制不同底数的指数函数图像
# 环境要求：Python 3.10+, matplotlib, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

# 字体设置
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 生成 x 值
x = np.linspace(-3, 4, 300)

# 创建图形
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：a > 1（指数增长）
ax1 = axes[0]
for a, color, label in [(1.5, '#2196f3', '$y = 1.5^x$'),
                          (2, '#4caf50', '$y = 2^x$'),
                          (3, '#f44336', '$y = 3^x$'),
                          (np.e, '#ff9800', '$y = e^x$')]:
    ax1.plot(x, a**x, color=color, linewidth=2, label=label)

ax1.axhline(y=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax1.axhline(y=1, color='gray', linewidth=0.5, linestyle=':', alpha=0.3)
ax1.axvline(x=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax1.plot(0, 1, 'ko', markersize=6, zorder=5)
ax1.annotate('$(0, 1)$', xy=(0, 1), xytext=(0.3, 1.5),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='black'))
ax1.set_xlim(-3, 4)
ax1.set_ylim(-0.5, 15)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$y$', fontsize=12)
ax1.set_title('Exponential Growth ($a > 1$)', fontsize=13)
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# 右图：0 < a < 1（指数衰减）
ax2 = axes[1]
for a, color, label in [(0.5, '#2196f3', '$y = 0.5^x$'),
                          (0.7, '#4caf50', '$y = 0.7^x$'),
                          (1/np.e, '#ff9800', '$y = e^{-x}$')]:
    ax2.plot(x, a**x, color=color, linewidth=2, label=label)

ax2.axhline(y=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax2.axhline(y=1, color='gray', linewidth=0.5, linestyle=':', alpha=0.3)
ax2.axvline(x=0, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax2.plot(0, 1, 'ko', markersize=6, zorder=5)
ax2.annotate('$(0, 1)$', xy=(0, 1), xytext=(0.3, 1.5),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='black'))
ax2.set_xlim(-3, 4)
ax2.set_ylim(-0.5, 15)
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_title('Exponential Decay ($0 < a < 1$)', fontsize=13)
ax2.legend(fontsize=10, loc='upper right')
ax2.grid(alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()

# 保存图片
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, '..', 'assets', 'exponential_functions.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"图片已保存到 {output_path}")
