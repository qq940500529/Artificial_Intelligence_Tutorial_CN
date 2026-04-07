# 文件：plot_inverse.py
# 用途：绘制函数及其反函数关于 y=x 对称的示例图
# 环境要求：Python 3.10+, numpy, matplotlib

import os
import numpy as np
import matplotlib.pyplot as plt

# ── 配置 ──
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ── 输出路径 ──
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'inverse_function.png')

# ── 绘图 ──
x = np.linspace(-2, 5, 500)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# ── 左图：线性函数 f(x)=2x+1 与反函数 f^{-1}(x)=(x-1)/2 ──
ax1 = axes[0]
x1 = np.linspace(-1, 4, 400)

y_f = 2 * x1 + 1
y_inv = (x1 - 1) / 2
y_diag = x1

ax1.plot(x1, y_f, 'b-', linewidth=2.2, label='$f(x) = 2x + 1$')
ax1.plot(x1, y_inv, 'r-', linewidth=2.2, label=r'$f^{-1}(x) = \frac{x-1}{2}$')
ax1.plot(x1, y_diag, 'k--', linewidth=1, alpha=0.5, label='$y = x$')

# 标注对称点对
pts = [(1, 3), (2, 5)]
for px, py in pts:
    # 原函数上的点
    ax1.plot(px, py, 'bo', markersize=7, zorder=5)
    ax1.annotate(f'({px}, {py})', xy=(px, py), xytext=(px - 0.8, py + 0.3),
                 fontsize=9, color='blue')
    # 反函数上的对称点
    ax1.plot(py, px, 'ro', markersize=7, zorder=5)
    ax1.annotate(f'({py}, {px})', xy=(py, px), xytext=(py + 0.1, px - 0.5),
                 fontsize=9, color='red')
    # 连线显示对称关系
    ax1.plot([px, py], [py, px], 'g:', linewidth=1, alpha=0.6)

ax1.set_xlim(-1.5, 5.5)
ax1.set_ylim(-1.5, 7)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$y$', fontsize=12)
ax1.set_title('Linear: $f(x) = 2x+1$ and its inverse', fontsize=13)
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axvline(x=0, color='k', linewidth=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_aspect('equal', adjustable='box')

# ── 右图：指数与对数 f(x)=2^x 与 f^{-1}(x)=log2(x) ──
ax2 = axes[1]
x2 = np.linspace(-2, 3.5, 400)
x2_pos = np.linspace(0.05, 8, 400)
x2_diag = np.linspace(-2, 4, 400)

y_exp = 2 ** x2
y_log = np.log2(x2_pos)

ax2.plot(x2, y_exp, 'b-', linewidth=2.2, label='$f(x) = 2^x$')
ax2.plot(x2_pos, y_log, 'r-', linewidth=2.2, label=r'$f^{-1}(x) = \log_2 x$')
ax2.plot(x2_diag, x2_diag, 'k--', linewidth=1, alpha=0.5, label='$y = x$')

# 标注对称点
exp_pts = [(0, 1), (1, 2), (2, 4)]
for px, py in exp_pts:
    ax2.plot(px, py, 'bo', markersize=6, zorder=5)
    ax2.plot(py, px, 'ro', markersize=6, zorder=5)
    ax2.plot([px, py], [py, px], 'g:', linewidth=1, alpha=0.6)

ax2.annotate('(0, 1)', xy=(0, 1), xytext=(-1.5, 1.5), fontsize=9, color='blue')
ax2.annotate('(1, 0)', xy=(1, 0), xytext=(1.2, -0.8), fontsize=9, color='red')

ax2.set_xlim(-2.5, 5)
ax2.set_ylim(-2.5, 5)
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_title('Exponential $2^x$ and Logarithmic $\\log_2 x$', fontsize=13)
ax2.legend(fontsize=10, loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axvline(x=0, color='k', linewidth=0.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f"Plot saved to: {output_path}")
