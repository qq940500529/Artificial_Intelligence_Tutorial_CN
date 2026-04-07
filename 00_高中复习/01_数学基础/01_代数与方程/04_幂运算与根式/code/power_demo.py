# 文件：code/power_demo.py
# 用途：演示幂运算与根式的基本操作，验证运算律
# 环境要求：Python 3.10+（仅使用标准库 math）

import math

# ============================================================
# 1. 整数指数幂的基本运算
# ============================================================
print("=" * 50)
print("1. 整数指数幂的基本运算")
print("=" * 50)

base = 2
print(f"{base}^1 = {base**1}")
print(f"{base}^2 = {base**2}")
print(f"{base}^3 = {base**3}")
print(f"{base}^10 = {base**10}")
print(f"{base}^0 = {base**0}")       # 零指数
print(f"{base}^(-1) = {base**-1}")   # 负整数指数
print(f"{base}^(-3) = {base**-3}")   # 等价于 1/2^3

# ============================================================
# 2. 验证幂运算律
# ============================================================
print(f"\n{'=' * 50}")
print("2. 验证幂运算律")
print("=" * 50)

a, m, n = 3, 4, 5

# 同底数幂相乘：a^m * a^n = a^(m+n)
left = a**m * a**n
right = a**(m + n)
print(f"同底数幂相乘: {a}^{m} * {a}^{n} = {left}, {a}^({m}+{n}) = {right}, 相等: {left == right}")

# 幂的幂：(a^m)^n = a^(m*n)
left = (a**m)**n
right = a**(m * n)
print(f"幂的幂: ({a}^{m})^{n} = {left}, {a}^({m}*{n}) = {right}, 相等: {left == right}")

# 积的幂：(a*b)^n = a^n * b^n
b = 5
left = (a * b)**n
right = a**n * b**n
print(f"积的幂: ({a}*{b})^{n} = {left}, {a}^{n}*{b}^{n} = {right}, 相等: {left == right}")

# 商的幂：(a/b)^n = a^n / b^n
left = (a / b)**n
right = a**n / b**n
print(f"商的幂: ({a}/{b})^{n} = {left}, {a}^{n}/{b}^{n} = {right}, 相等: {math.isclose(left, right)}")

# ============================================================
# 3. 有理数指数与根式
# ============================================================
print(f"\n{'=' * 50}")
print("3. 有理数指数与根式")
print("=" * 50)

# a^(1/n) 等价于 n次方根
x = 27
print(f"{x}^(1/3) = {x**(1/3):.6f}, 即 ∛{x} = {x**(1/3):.6f}")
print(f"验证: {x**(1/3):.6f}^3 = {(x**(1/3))**3:.6f}")

# a^(m/n) 等价于 (n次方根(a))^m
x = 8
m_val, n_val = 2, 3
result = x**(m_val / n_val)
print(f"\n{x}^({m_val}/{n_val}) = {result:.6f}")
print(f"等价于 (∛{x})^{m_val} = ({x**(1/n_val):.6f})^{m_val} = {(x**(1/n_val))**m_val:.6f}")

# 使用 math.isqrt 进行精确整数平方根运算
print(f"\nmath.isqrt(144) = {math.isqrt(144)}  (精确整数平方根)")
print(f"math.sqrt(144)  = {math.sqrt(144)}  (浮点平方根)")

# ============================================================
# 4. 浮点精度问题——AI 开发者必知
# ============================================================
print(f"\n{'=' * 50}")
print("4. 浮点精度问题（AI 开发中的常见陷阱）")
print("=" * 50)

# 经典精度问题
val = 0.1 + 0.2
print(f"0.1 + 0.2 = {val}  (不精确等于 0.3!)")
print(f"0.1 + 0.2 == 0.3 ? {val == 0.3}")
print(f"math.isclose(0.1 + 0.2, 0.3) ? {math.isclose(val, 0.3)}")

# 幂运算中的精度问题
val1 = 10**0.1 * 10**0.2
val2 = 10**0.3
print(f"\n10^0.1 * 10^0.2 = {val1:.15f}")
print(f"10^0.3         = {val2:.15f}")
print(f"直接比较相等: {val1 == val2}")
print(f"使用 isclose: {math.isclose(val1, val2)}")

# 大数幂运算——Python 的优势
print(f"\n2^100 = {2**100}")
print(f"(Python 支持任意精度整数，这在密码学和 AI 哈希计算中很重要)")

# ============================================================
# 5. 根式化简示例
# ============================================================
print(f"\n{'=' * 50}")
print("5. 根式化简验证")
print("=" * 50)

# √12 = 2√3
print(f"√12 = {math.sqrt(12):.6f}")
print(f"2√3 = {2 * math.sqrt(3):.6f}")
print(f"√12 == 2√3 ? {math.isclose(math.sqrt(12), 2 * math.sqrt(3))}")

# √50 = 5√2
print(f"\n√50 = {math.sqrt(50):.6f}")
print(f"5√2 = {5 * math.sqrt(2):.6f}")
print(f"√50 == 5√2 ? {math.isclose(math.sqrt(50), 5 * math.sqrt(2))}")

# 有理化分母验证: 1/√3 = √3/3
val_before = 1 / math.sqrt(3)
val_after = math.sqrt(3) / 3
print(f"\n1/√3  = {val_before:.6f}")
print(f"√3/3  = {val_after:.6f}")
print(f"1/√3 == √3/3 ? {math.isclose(val_before, val_after)}")
