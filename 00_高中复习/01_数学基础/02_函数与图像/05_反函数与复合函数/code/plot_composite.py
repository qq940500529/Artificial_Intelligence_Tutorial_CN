# 文件：plot_composite.py
# 用途：绘制复合函数的可视化示例及神经网络函数组合示意图
# 环境要求：Python 3.10+, numpy, matplotlib

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# ── 配置 ──
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ── 输出路径 ──
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'composite_function.png')

# ── 绘图 ──
x = np.linspace(-3, 3, 500)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# ── 左图：g(x) = x + 1（内层函数） ──
ax1 = axes[0]
g_x = x + 1
ax1.plot(x, g_x, 'b-', linewidth=2.2, label='$g(x) = x + 1$')
ax1.plot(1, 2, 'ro', markersize=8, zorder=5)
ax1.annotate('$x=1 \\to g(1)=2$', xy=(1, 2), xytext=(1.3, 3.2),
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 5)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$y$', fontsize=12)
ax1.set_title('Step 1: Inner $g(x) = x + 1$', fontsize=13)
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axvline(x=0, color='k', linewidth=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# ── 中图：f(x) = x^2（外层函数） ──
ax2 = axes[1]
f_x = x ** 2
ax2.plot(x, f_x, 'g-', linewidth=2.2, label='$f(x) = x^2$')
ax2.plot(2, 4, 'ro', markersize=8, zorder=5)
ax2.annotate('$x=2 \\to f(2)=4$', xy=(2, 4), xytext=(0.3, 7),
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax2.set_xlim(-3, 3)
ax2.set_ylim(-1, 9)
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_title('Step 2: Outer $f(x) = x^2$', fontsize=13)
ax2.legend(fontsize=11, loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axvline(x=0, color='k', linewidth=0.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# ── 右图：复合函数 f(g(x)) = (x+1)^2 ──
ax3 = axes[2]
fg_x = (x + 1) ** 2
ax3.plot(x, fg_x, 'm-', linewidth=2.5, label='$(f \\circ g)(x) = (x+1)^2$')
ax3.plot(x, x ** 2, 'k--', linewidth=1.2, alpha=0.4, label='$x^2$ (reference)')
ax3.plot(1, 4, 'ro', markersize=8, zorder=5)
ax3.annotate('$x=1 \\to (1+1)^2=4$', xy=(1, 4), xytext=(-2.5, 7),
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax3.set_xlim(-3, 3)
ax3.set_ylim(-1, 9)
ax3.set_xlabel('$x$', fontsize=12)
ax3.set_ylabel('$y$', fontsize=12)
ax3.set_title('Result: $(f \\circ g)(x) = (x+1)^2$', fontsize=13)
ax3.legend(fontsize=10, loc='upper left')
ax3.grid(True, alpha=0.3)
ax3.axhline(y=0, color='k', linewidth=0.5)
ax3.axvline(x=0, color='k', linewidth=0.5)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f"Plot saved to: {output_path}")
