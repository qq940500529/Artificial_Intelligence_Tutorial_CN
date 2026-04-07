# 文件：inverse_demo.py
# 用途：演示反函数与复合函数的基本运算
# 环境要求：Python 3.10+

# ============================================================
# 第一部分：反函数验证
# ============================================================
print("=" * 50)
print("反函数验证：f(x) = 2x + 1, f⁻¹(x) = (x - 1) / 2")
print("=" * 50)


def f(x):
    """原函数 f(x) = 2x + 1"""
    return 2 * x + 1


def f_inv(x):
    """反函数 f⁻¹(x) = (x - 1) / 2"""
    return (x - 1) / 2


# 验证 f⁻¹(f(x)) = x
test_values = [-2, 0, 1, 3.5, 10]
print("\n验证 f⁻¹(f(x)) = x：")
for x in test_values:
    result = f_inv(f(x))
    print(f"  x = {x:>5}  →  f(x) = {f(x):>5}  →  f⁻¹(f(x)) = {result:>5}")

# 验证 f(f⁻¹(x)) = x
print("\n验证 f(f⁻¹(x)) = x：")
for x in test_values:
    result = f(f_inv(x))
    print(f"  x = {x:>5}  →  f⁻¹(x) = {f_inv(x):>5}  →  f(f⁻¹(x)) = {result:>5}")

# ============================================================
# 第二部分：温度转换——反函数的实际应用
# ============================================================
print("\n" + "=" * 50)
print("实际应用：摄氏度 ↔ 华氏度 转换")
print("=" * 50)


def celsius_to_fahrenheit(c):
    """摄氏度 → 华氏度：F = 9/5 * C + 32"""
    return 9 / 5 * c + 32


def fahrenheit_to_celsius(f_val):
    """华氏度 → 摄氏度（反函数）：C = 5/9 * (F - 32)"""
    return 5 / 9 * (f_val - 32)


temps_c = [0, 20, 37, 100]
print("\n摄氏度 → 华氏度 → 摄氏度（往返验证）：")
for c in temps_c:
    f_val = celsius_to_fahrenheit(c)
    c_back = fahrenheit_to_celsius(f_val)
    print(f"  {c}°C  →  {f_val:.1f}°F  →  {c_back:.1f}°C  ✓")

# ============================================================
# 第三部分：复合函数
# ============================================================
print("\n" + "=" * 50)
print("复合函数：f(x) = x², g(x) = x + 1")
print("=" * 50)


def g(x):
    """g(x) = x + 1"""
    return x + 1


def f_square(x):
    """f(x) = x²"""
    return x ** 2


print("\n逐步计算 f(g(x)) = (x + 1)²：")
for x in [-2, -1, 0, 1, 2]:
    step1 = g(x)
    step2 = f_square(step1)
    direct = (x + 1) ** 2
    print(f"  x = {x:>2}  →  g({x}) = {step1:>2}"
          f"  →  f({step1}) = {step2:>2}  =  (x+1)² = {direct}")

print("\n注意：f(g(x)) ≠ g(f(x))！复合函数的顺序很重要：")
print("  f(g(x)) = (x+1)²")
print("  g(f(x)) = x² + 1")
print()
for x in [-2, -1, 0, 1, 2]:
    fg = f_square(g(x))
    gf = g(f_square(x))
    print(f"  x = {x:>2}:  f(g(x)) = {fg:>2},  g(f(x)) = {gf:>2},"
          f"  {'相等' if fg == gf else '不等'}")

# ============================================================
# 第四部分：模拟神经网络的函数组合
# ============================================================
print("\n" + "=" * 50)
print("神经网络视角：多层函数组合")
print("=" * 50)


def layer1(x):
    """第 1 层：线性变换"""
    return 2 * x + 1


def relu(x):
    """激活函数 ReLU"""
    return max(0, x)


def layer2(x):
    """第 2 层：线性变换"""
    return -0.5 * x + 3


inputs = [-3, -1, 0, 1, 3, 5]
print("\n输入 → 第1层(2x+1) → ReLU → 第2层(-0.5x+3) → 输出：")
for x in inputs:
    z1 = layer1(x)
    a1 = relu(z1)
    z2 = layer2(a1)
    print(f"  x = {x:>2}  →  z1 = {z1:>5.1f}"
          f"  →  ReLU = {a1:>4.1f}"
          f"  →  output = {z2:>5.1f}")
