# 文件：code/plot_sum_angle.py
# 用途：绘制和角公式的几何证明图（单位圆方法）
# 环境要求：Python 3.10+, matplotlib, numpy

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# ========== 和角公式几何证明图 ==========
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# 画单位圆
theta_circle = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(theta_circle), np.sin(theta_circle), 'b-', linewidth=1, alpha=0.5)

# 定义角度
alpha = np.radians(30)  # α = 30°
beta = np.radians(25)   # β = 25°

# 关键点
O = np.array([0, 0])
# P 是角 α 对应的点
P = np.array([np.cos(alpha), np.sin(alpha)])
# Q 是角 (α+β) 对应的点
Q = np.array([np.cos(alpha + beta), np.sin(alpha + beta)])
# A 是 (1, 0)
A = np.array([1, 0])

# 画从原点到各点的线
ax.plot([0, A[0]], [0, A[1]], 'k-', linewidth=1.5)
ax.plot([0, P[0]], [0, P[1]], 'g-', linewidth=2, label=r'angle $\alpha$')
ax.plot([0, Q[0]], [0, Q[1]], 'r-', linewidth=2, label=r'angle $\alpha + \beta$')

# Q 到 x 轴的投影
Qx = np.array([Q[0], 0])
ax.plot([Q[0], Q[0]], [0, Q[1]], 'r--', linewidth=1.5, alpha=0.7)
ax.plot([0, Q[0]], [0, 0], 'r-', linewidth=1.5, alpha=0.3)

# Q 到 OP 线上的投影
# OP 方向: (cos α, sin α)，Q 在 OP 上的投影
proj_len = Q[0] * np.cos(alpha) + Q[1] * np.sin(alpha)
H = proj_len * np.array([np.cos(alpha), np.sin(alpha)])
ax.plot([Q[0], H[0]], [Q[1], H[1]], 'purple', linewidth=2, linestyle='--')

# H 到 x 轴的投影
Hx = np.array([H[0], 0])
ax.plot([H[0], H[0]], [0, H[1]], 'g--', linewidth=1.5, alpha=0.7)

# 标注点
ax.plot(*O, 'ko', markersize=5)
ax.plot(*P, 'go', markersize=8, zorder=5)
ax.plot(*Q, 'ro', markersize=8, zorder=5)
ax.plot(*A, 'ko', markersize=5)
ax.plot(*H, 'mo', markersize=7, zorder=5)

ax.text(A[0] + 0.05, A[1] - 0.08, r'$A(1,0)$', fontsize=11, ha='left')
ax.text(P[0] + 0.05, P[1] + 0.05, r'$P(\cos\alpha, \sin\alpha)$', fontsize=11, color='green')
ax.text(Q[0] - 0.55, Q[1] + 0.05, r'$Q(\cos(\alpha\!+\!\beta), \sin(\alpha\!+\!\beta))$',
        fontsize=10, color='red')
ax.text(H[0] - 0.05, H[1] + 0.08, r'$H$', fontsize=12, color='purple', ha='right')

# 画角 α 的弧
arc_alpha = np.linspace(0, alpha, 50)
arc_r1 = 0.3
ax.plot(arc_r1 * np.cos(arc_alpha), arc_r1 * np.sin(arc_alpha), 'g-', linewidth=1.5)
ax.text(0.33, 0.08, r'$\alpha$', fontsize=13, color='green')

# 画角 β 的弧
arc_beta = np.linspace(alpha, alpha + beta, 50)
arc_r2 = 0.45
ax.plot(arc_r2 * np.cos(arc_beta), arc_r2 * np.sin(arc_beta), 'r-', linewidth=1.5)
ax.text(0.38, 0.28, r'$\beta$', fontsize=13, color='red')

# 直角符号 at H
# QH ⊥ OP，画一个小直角符号
perp_dir = np.array([Q[0] - H[0], Q[1] - H[1]])
perp_dir = perp_dir / np.linalg.norm(perp_dir) * 0.05
along_dir = np.array([np.cos(alpha), np.sin(alpha)]) * 0.05
sq_pts = [H, H + perp_dir, H + perp_dir + along_dir, H + along_dir]
sq_patch = plt.Polygon(sq_pts, fill=False, edgecolor='purple', linewidth=1)
ax.add_patch(sq_patch)

# 坐标轴
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)

# 公式标注框
formula_text = (
    r'$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$'
    + '\n'
    + r'$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$'
)
ax.text(-0.95, -0.55, formula_text, fontsize=11,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange', alpha=0.9))

ax.set_xlim(-1.3, 1.5)
ax.set_ylim(-0.8, 1.3)
ax.set_aspect('equal')
ax.set_title(r'Geometric Proof of Sum Angle Formulas', fontsize=14, pad=10)
ax.grid(True, alpha=0.2)
ax.legend(fontsize=11, loc='upper right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'sum_angle_proof.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("Generated: sum_angle_proof.png")
