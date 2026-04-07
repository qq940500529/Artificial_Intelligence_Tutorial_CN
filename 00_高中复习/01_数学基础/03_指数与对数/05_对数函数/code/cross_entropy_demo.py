# 文件：code/cross_entropy_demo.py
# 交叉熵损失的对数直觉
# 环境要求：Python 3.10+（仅使用标准库 math）

import math

print("=" * 50)
print("交叉熵损失 L = -log(p) 随预测概率 p 的变化")
print("=" * 50)
print(f"{'预测概率 p':>12} | {'损失 -ln(p)':>12} | {'判断':>10}")
print("-" * 42)

for p in [0.99, 0.9, 0.7, 0.5, 0.3, 0.1, 0.01, 0.001]:
    loss = -math.log(p)
    if loss < 0.5:
        judge = "低损失 ✓"
    elif loss < 2:
        judge = "中等损失"
    else:
        judge = "高损失 ✗"
    print(f"{p:>12.3f} | {loss:>12.4f} | {judge:>10}")

print("\n观察：当预测概率接近 1 时损失很小，接近 0 时损失急剧增大。")
print("这就是对数函数的'压缩'特性在损失函数中的体现。")
