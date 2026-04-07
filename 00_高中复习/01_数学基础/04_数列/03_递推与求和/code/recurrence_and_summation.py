# 文件：code/recurrence_and_summation.py
# 递推数列计算与求和技巧验证
# 环境要求：Python 3.10+（仅使用标准库）


def fibonacci(n: int) -> list[int]:
    """生成斐波那契数列前 n 项"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def telescoping_sum(n: int) -> float:
    """裂项相消法：sum(1/(k*(k+1)), k=1..n) = n/(n+1)"""
    s = sum(1 / (k * (k + 1)) for k in range(1, n + 1))
    return s


if __name__ == "__main__":
    # 斐波那契数列
    print("=" * 50)
    print("斐波那契数列前 15 项：")
    fib = fibonacci(15)
    print(f"  {fib}")
    print("  相邻项比值趋近黄金比例 φ ≈ 1.618：")
    for i in range(5, 15):
        ratio = fib[i] / fib[i - 1]
        print(f"  F_{i+1}/F_{i} = {fib[i]}/{fib[i-1]} = {ratio:.6f}")

    # 递推数列 a_1=1, a_{n+1}=2a_n+1
    print("\n" + "=" * 50)
    print("递推数列 a_1=1, a_{n+1}=2a_n+1：")
    a = [1]
    for i in range(9):
        a.append(2 * a[-1] + 1)
    print(f"  前 10 项：{a}")
    print(f"  通项公式 2^n - 1：{[2**n - 1 for n in range(1, 11)]}")
    print(f"  一致：{'✓' if a == [2**n - 1 for n in range(1, 11)] else '✗'}")

    # 裂项相消法验证
    print("\n" + "=" * 50)
    print("裂项相消法：sum(1/(k(k+1)), k=1..n) = n/(n+1)")
    for n in [10, 100, 1000]:
        computed = telescoping_sum(n)
        formula = n / (n + 1)
        print(f"  n={n}: 逐项累加={computed:.10f}, 公式={formula:.10f}")

    # 错位相减法验证
    print("\n" + "=" * 50)
    print("错位相减法：sum(k*2^k, k=1..n) = (n-1)*2^(n+1) + 2")
    for n in [5, 10, 15]:
        computed = sum(k * 2**k for k in range(1, n + 1))
        formula = (n - 1) * 2**(n + 1) + 2
        print(f"  n={n}: 逐项累加={computed}, 公式={formula}, 一致：{'✓' if computed == formula else '✗'}")
