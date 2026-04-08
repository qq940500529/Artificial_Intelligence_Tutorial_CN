# 文件：verify_exponent_laws.py
# 用途：用 Python 验证指数运算律
# 环境要求：Python 3.10+（无需额外库）

# --- 运算律一：同底数幂相乘 ---
a, m, n = 2, 3, 4
left = a**m * a**n
right = a**(m + n)
print(f"运算律一：{a}^{m} × {a}^{n} = {left}, {a}^({m}+{n}) = {right}, 相等：{left == right}")

# --- 运算律二：同底数幂相除 ---
a, m, n = 5, 6, 2
left = a**m / a**n
right = a**(m - n)
print(f"运算律二：{a}^{m} ÷ {a}^{n} = {left}, {a}^({m}-{n}) = {right}, 相等：{left == right}")

# --- 运算律三：幂的幂 ---
a, m, n = 3, 2, 4
left = (a**m)**n
right = a**(m * n)
print(f"运算律三：({a}^{m})^{n} = {left}, {a}^({m}×{n}) = {right}, 相等：{left == right}")

# --- 零指数 ---
a = 7
print(f"零指数：{a}^0 = {a**0}")

# --- 负指数 ---
a, n = 2, 3
print(f"负指数：{a}^(-{n}) = {a**(-n)}, 1/{a}^{n} = {1/a**n}, 相等：{a**(-n) == 1/a**n}")

# --- 分数指数 ---
a = 8
frac_exp = a**(2/3)
root_then_pow = round(a**(1/3))**2  # 先开三次方再平方
print(f"分数指数：{a}^(2/3) = {frac_exp}, (³√{a})² = {root_then_pow}")

# --- 指数增长示例：棋盘上的米粒 ---
total_rice = sum(2**i for i in range(64))
print(f"\n棋盘米粒总数：{total_rice}")
print(f"即 2^64 - 1 = {2**64 - 1}")
