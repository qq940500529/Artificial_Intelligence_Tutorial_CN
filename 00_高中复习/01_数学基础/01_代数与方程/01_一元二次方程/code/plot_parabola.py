# 文件：code/plot_parabola.py
# 绘制一元二次方程与抛物线的关系图：展示判别式 Δ 的三种情况
# 环境要求：Python 3.10+, matplotlib, numpy

import numpy as np
import matplotlib.pyplot as plt
import os

# 设置字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# 定义三个二次函数，分别对应 Δ > 0、Δ = 0、Δ < 0
cases = [
    {
        'a': 1, 'b': -3, 'c': -4,
        'title': '$\\Delta > 0$: Two intersections',
        'equation': '$y = x^2 - 3x - 4$',
    },
    {
        'a': 1, 'b': -4, 'c': 4,
        'title': '$\\Delta = 0$: One tangent point',
        'equation': '$y = x^2 - 4x + 4$',
    },
    {
        'a': 1, 'b': 0, 'c': 2,
        'title': '$\\Delta < 0$: No intersection',
        'equation': '$y = x^2 + 2$',
    },
]

fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

for ax, case in zip(axes, cases):
    a, b, c = case['a'], case['b'], case['c']
    delta = b**2 - 4*a*c

    # 计算顶点位置以确定绘图范围
    vertex_x = -b / (2 * a)

    # 设置 x 范围（以顶点为中心）
    x = np.linspace(vertex_x - 5, vertex_x + 5, 300)
    y = a * x**2 + b * x + c

    # 绘制抛物线
    ax.plot(x, y, color='#2196F3', linewidth=2.5, label=case['equation'])

    # 绘制坐标轴
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.axvline(x=0, color='black', linewidth=0.3, linestyle='--')

    # 标注交点
    if delta > 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        ax.plot([x1, x2], [0, 0], 'o', color='#F44336', markersize=10, zorder=5)
        ax.annotate(f'$x_1={x1:.0f}$', (x1, 0), textcoords="offset points",
                    xytext=(-5, 15), ha='center', fontsize=11, color='#F44336')
        ax.annotate(f'$x_2={x2:.0f}$', (x2, 0), textcoords="offset points",
                    xytext=(5, 15), ha='center', fontsize=11, color='#F44336')
    elif delta == 0:
        x0 = -b / (2 * a)
        ax.plot(x0, 0, 'o', color='#F44336', markersize=10, zorder=5)
        ax.annotate(f'$x={x0:.0f}$', (x0, 0), textcoords="offset points",
                    xytext=(15, -18), ha='center', fontsize=11, color='#F44336')

    # 设置标题和图例
    ax.set_title(case['title'], fontsize=14, fontweight='bold', pad=12)
    ax.legend(loc='upper center', fontsize=10, framealpha=0.9)

    # 美化
    ax.set_ylim(-7, 12)
    ax.set_xlabel('$x$', fontsize=13)
    ax.set_ylabel('$y$', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()

output_path = os.path.join(assets_dir, 'parabola_discriminant.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print(f"图片已保存到: {output_path}")
