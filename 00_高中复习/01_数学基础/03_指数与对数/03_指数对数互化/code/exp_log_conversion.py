# 文件：code/exp_log_conversion.py
# 指数与对数互化验证
# 环境要求：Python 3.10+（仅使用标准库 math）

import math


def demo_inverse_properties():
    """验证指数与对数的互逆性质"""
    print("=" * 50)
    print("性质验证：指数与对数互为逆运算")
    print("=" * 50)

    # 性质一：log_a(a^x) = x
    a, x = 2, 5
    result = math.log(a**x, a)
    print(f"\nlog_{a}({a}^{x}) = log_{a}({a**x}) = {result}")
    print(f"  期望值：{x}  ✓" if abs(result - x) < 1e-10 else f"  期望值：{x}  ✗")

    # 性质二：a^(log_a(N)) = N
    a, N = 3, 81
    result = a ** math.log(N, a)
    print(f"\n{a}^(log_{a}({N})) = {result}")
    print(f"  期望值：{N}  ✓" if abs(result - N) < 1e-10 else f"  期望值：{N}  ✗")


def solve_equations():
    """用互化技巧解方程"""
    print("\n" + "=" * 50)
    print("方程求解演示")
    print("=" * 50)

    # 例1：3^x = 20
    x = math.log(20, 3)
    print(f"\n3^x = 20")
    print(f"  x = log_3(20) = ln(20)/ln(3) = {math.log(20):.4f}/{math.log(3):.4f} = {x:.4f}")
    print(f"  验证：3^{x:.4f} = {3**x:.4f}")

    # 例2：log_2(x) = 5
    x = 2**5
    print(f"\nlog_2(x) = 5")
    print(f"  x = 2^5 = {x}")
    print(f"  验证：log_2({x}) = {math.log2(x):.1f}")

    # 存款翻倍时间
    t = math.log(2) / math.log(1.05)
    print(f"\n存款翻倍时间（年利率 5%）：")
    print(f"  t = ln(2)/ln(1.05) = {t:.2f} 年")
    print(f"  72法则估算：72/5 = {72/5} 年")

    # 训练误差下降
    n = math.log(0.01) / math.log(0.9)
    print(f"\n训练误差降至 1%（每 epoch 下降 10%）：")
    print(f"  n = ln(0.01)/ln(0.9) = {n:.1f} epochs")


if __name__ == "__main__":
    demo_inverse_properties()
    solve_equations()
