# 文件：code/plot_regression.py
# 用途：绘制散点图、最小二乘回归线和残差
# 环境要求：Python 3.10+, matplotlib>=3.7, numpy

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Output path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'regression_line.png')

# Data: study hours vs test scores
x = np.array([2, 4, 5, 6, 7, 8, 10, 12], dtype=float)
y = np.array([50, 58, 63, 70, 72, 78, 85, 92], dtype=float)
n = len(x)

# Least squares regression
x_mean, y_mean = x.mean(), y.mean()
b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
a = y_mean - b * x_mean
y_pred = b * x + a

# R-squared
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - y_mean) ** 2)
r_squared = 1 - ss_res / ss_tot

# Indices for residual lines (show a representative subset)
residual_indices = [0, 2, 3, 5, 6, 7]

fig, ax = plt.subplots(figsize=(9, 6))

# Residual lines (draw first so they're behind)
for i in residual_indices:
    ax.plot([x[i], x[i]], [y[i], y_pred[i]],
            color='#FF7F0E', linewidth=1.5, linestyle='--', alpha=0.7,
            zorder=2)
    # Small label for residual
    mid_y = (y[i] + y_pred[i]) / 2
    sign = '+' if y[i] > y_pred[i] else ''
    ax.text(x[i] + 0.2, mid_y,
            f'{sign}{y[i] - y_pred[i]:.1f}',
            fontsize=8, color='#FF7F0E', va='center', alpha=0.85)

# Regression line
x_line = np.linspace(0, 14, 100)
y_line = b * x_line + a
ax.plot(x_line, y_line, color='#D62728', linewidth=2.2, zorder=3,
        label=f'$\\hat{{y}} = {b:.2f}x + {a:.2f}$')

# Scatter points
ax.scatter(x, y, color='#1F77B4', s=90, zorder=4, edgecolors='white',
           linewidths=0.8, label='Observed data')

# Mean point
ax.plot(x_mean, y_mean, 'D', color='#2CA02C', markersize=10, zorder=5,
        label=f'Mean ($\\bar{{x}}={x_mean:.1f}$, $\\bar{{y}}={y_mean:.0f}$)')

# R² annotation
ax.text(0.03, 0.95,
        f'$R^2 = {r_squared:.4f}$\n$b = {b:.2f}$\n$a = {a:.2f}$',
        transform=ax.transAxes, fontsize=13,
        va='top', ha='left',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.9))

# Residual legend entry (manual)
ax.plot([], [], color='#FF7F0E', linewidth=1.5, linestyle='--',
        label='Residuals ($y_i - \\hat{y}_i$)')

# Styling
ax.set_xlabel('Study Hours per Week ($x$)', fontsize=13)
ax.set_ylabel('Exam Score ($y$)', fontsize=13)
ax.set_title('Least Squares Regression: Study Hours vs Exam Score',
             fontsize=14, pad=12)
ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(0, 14)
ax.set_ylim(40, 100)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Plot saved to {output_path}")
