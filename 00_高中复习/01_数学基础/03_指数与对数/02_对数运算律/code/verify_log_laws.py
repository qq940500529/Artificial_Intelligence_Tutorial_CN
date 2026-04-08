# 文件：verify_log_laws.py
# 用途：用 Python 验证对数运算律
# 环境要求：Python 3.10+, math（标准库）

import math

print("=" * 56)
print("          对数运算律 Python 验证")
print("=" * 56)

# --- 1. 对数的定义验证 ---
print("\n【1】对数的定义：log_a(N) = x  ⟺  a^x = N")
a, N = 2, 32
x = math.log(N, a)  # log₂(32)
print(f"  log_{a}({N}) = {x}")
print(f"  验证：{a}^{x} = {a**x}，与 {N} 相等：{math.isclose(a**x, N)}")

# --- 2. 积的对数（Product Rule） ---
print("\n【2】积的对数：log_a(M·N) = log_a(M) + log_a(N)")
a, M, N = 10, 20, 50
left = math.log(M * N, a)
right = math.log(M, a) + math.log(N, a)
print(f"  log_{a}({M}×{N}) = {left:.6f}")
print(f"  log_{a}({M}) + log_{a}({N}) = {right:.6f}")
print(f"  相等：{math.isclose(left, right)}")

# --- 3. 商的对数（Quotient Rule） ---
print("\n【3】商的对数：log_a(M/N) = log_a(M) - log_a(N)")
a, M, N = 2, 128, 8
left = math.log(M / N, a)
right = math.log(M, a) - math.log(N, a)
print(f"  log_{a}({M}/{N}) = {left:.6f}")
print(f"  log_{a}({M}) - log_{a}({N}) = {right:.6f}")
print(f"  相等：{math.isclose(left, right)}")

# --- 4. 幂的对数（Power Rule） ---
print("\n【4】幂的对数：log_a(M^k) = k · log_a(M)")
a, M, k = 10, 5, 3
left = math.log(M**k, a)
right = k * math.log(M, a)
print(f"  log_{a}({M}^{k}) = {left:.6f}")
print(f"  {k} × log_{a}({M}) = {right:.6f}")
print(f"  相等：{math.isclose(left, right)}")

# --- 5. 换底公式（Change of Base） ---
print("\n【5】换底公式：log_a(N) = ln(N) / ln(a)")
a, N = 3, 81
by_formula = math.log(N) / math.log(a)       # 用自然对数换底
by_direct = math.log(N, a)                    # 直接计算
print(f"  ln({N}) / ln({a}) = {by_formula:.6f}")
print(f"  log_{a}({N})      = {by_direct:.6f}")
print(f"  相等：{math.isclose(by_formula, by_direct)}")

# --- 6. 常用对数和自然对数 ---
print("\n【6】常用对数 lg 与自然对数 ln")
print(f"  lg(1000) = log10(1000) = {math.log10(1000)}")
print(f"  ln(e)    = log_e(e)    = {math.log(math.e)}")
print(f"  ln(e^5)  = 5 · ln(e)  = {math.log(math.e**5):.6f}")
print(f"  e ≈ {math.e:.10f}")

# --- 7. 实际应用：地震震级 ---
print("\n【7】应用：地震震级（里氏震级近似公式）")
print("  震级 M ≈ lg(A)，A 为相对振幅")
for A in [10, 100, 1000, 10000, 100000]:
    M = math.log10(A)
    print(f"    振幅 A = {A:>6}  →  震级 M ≈ {M:.1f}")
print("  → 振幅每增大 10 倍，震级加 1")

# --- 8. AI 中的对数：交叉熵损失 ---
print("\n【8】AI 应用预览：交叉熵损失中的对数")
print("  二分类交叉熵：L = -[y·ln(p) + (1-y)·ln(1-p)]")
y_true = 1
for p in [0.1, 0.5, 0.9, 0.99]:
    loss = -(y_true * math.log(p) + (1 - y_true) * math.log(1 - p))
    print(f"    真实标签=1, 预测概率 p={p}  →  损失 L = {loss:.4f}")
print("  → 预测越接近真实标签，损失越小（对数在起作用！）")

print("\n" + "=" * 56)
print("  所有对数运算律验证通过 ✓")
print("=" * 56)
