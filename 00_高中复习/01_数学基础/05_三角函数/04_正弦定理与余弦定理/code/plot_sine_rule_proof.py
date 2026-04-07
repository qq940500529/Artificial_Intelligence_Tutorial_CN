# 文件：code/plot_sine_rule_proof.py
# 用途：绘制正弦定理推导过程的三角形图（从C向AB作高）
# 环境要求：Python 3.10+, matplotlib, numpy

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, '..', 'assets')
os.makedirs(assets_dir, exist_ok=True)

# ========== 正弦定理推导图 ==========
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# 三角形顶点
A = np.array([0, 0])
B = np.array([6, 0])
C = np.array([2, 4])

# 画三角形
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(triangle)

# 从 C 向 AB 作高 h
# AB 在 x 轴上，所以高的垂足 D 就是 (C[0], 0)
D = np.array([C[0], 0])

# 画高 h (虚线)
ax.plot([C[0], D[0]], [C[1], D[1]], 'r--', linewidth=2, zorder=3)

# 直角符号
sq = 0.25
ax.plot([D[0], D[0], D[0] + sq], [D[1] + sq, D[1], D[1]], 'r-', linewidth=1.2)

# 标注顶点
ax.text(A[0] - 0.3, A[1] - 0.3, r'$A$', fontsize=16, fontweight='bold', color='blue')
ax.text(B[0] + 0.15, B[1] - 0.3, r'$B$', fontsize=16, fontweight='bold', color='blue')
ax.text(C[0] - 0.1, C[1] + 0.2, r'$C$', fontsize=16, fontweight='bold', color='blue')
ax.text(D[0] + 0.15, D[1] - 0.3, r'$D$', fontsize=14, color='red')

# 标注边
# a = BC (对角A), b = AC (对角B), c = AB (对角C)
mid_BC = (B + C) / 2
mid_AC = (A + C) / 2
mid_AB = (A + B) / 2

ax.text(mid_BC[0] + 0.25, mid_BC[1] + 0.1, r'$a$', fontsize=16, color='darkgreen', fontweight='bold')
ax.text(mid_AC[0] - 0.45, mid_AC[1] + 0.1, r'$b$', fontsize=16, color='darkgreen', fontweight='bold')
ax.text(mid_AB[0], mid_AB[1] - 0.4, r'$c$', fontsize=16, color='darkgreen', fontweight='bold')

# 标注高 h
ax.text(C[0] + 0.2, C[1] / 2, r'$h$', fontsize=16, color='red', fontweight='bold')

# 标注角 A
angle_A = np.arctan2(C[1] - A[1], C[0] - A[0])
arc_theta_A = np.linspace(0, angle_A, 50)
arc_r_A = 0.7
ax.plot(A[0] + arc_r_A * np.cos(arc_theta_A), A[1] + arc_r_A * np.sin(arc_theta_A),
        'orange', linewidth=1.5)
ax.text(A[0] + 0.8, A[1] + 0.25, r'$A$', fontsize=14, color='orange')

# 标注角 B
angle_B_start = np.pi - np.arctan2(C[1] - B[1], B[0] - C[0])
angle_B_end = np.pi
arc_theta_B = np.linspace(angle_B_start, angle_B_end, 50)
arc_r_B = 0.7
ax.plot(B[0] + arc_r_B * np.cos(arc_theta_B), B[1] + arc_r_B * np.sin(arc_theta_B),
        'purple', linewidth=1.5)
ax.text(B[0] - 0.95, B[1] + 0.3, r'$B$', fontsize=14, color='purple')

# 关键等式标注
eq_text = (r'$h = b \sin A = a \sin B$' + '\n'
           + r'$\Rightarrow \dfrac{a}{\sin A} = \dfrac{b}{\sin B}$')
ax.text(4.0, 3.5, eq_text, fontsize=13,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange', alpha=0.9))

ax.set_xlim(-0.8, 7.5)
ax.set_ylim(-0.8, 5)
ax.set_aspect('equal')
ax.set_title('Law of Sines: Proof by Altitude from $C$ to $AB$', fontsize=14, pad=10)
ax.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'sine_rule_proof.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("Generated: sine_rule_proof.png")
