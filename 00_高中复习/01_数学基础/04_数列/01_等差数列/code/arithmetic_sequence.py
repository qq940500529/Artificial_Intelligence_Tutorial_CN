# 文件：code/arithmetic_sequence.py
# 等差数列的通项公式与求和
# 环境要求：Python 3.10+（仅使用标准库）


def arithmetic_term(a1: float, d: float, n: int) -> float:
    """等差数列通项公式：a_n = a_1 + (n-1)d"""
    return a1 + (n - 1) * d


def arithmetic_sum(a1: float, d: float, n: int) -> float:
    """等差数列求和公式：S_n = n(2a_1 + (n-1)d) / 2"""
    return n * (2 * a1 + (n - 1) * d) / 2


if __name__ == "__main__":
    # 示例 1：高斯求和 1 + 2 + ... + 100
    print("=" * 50)
    print("示例 1：高斯求和 1 + 2 + ... + 100")
    s = arithmetic_sum(a1=1, d=1, n=100)
    print(f"  公式计算：S_100 = {s}")
    print(f"  逐项累加：S_100 = {sum(range(1, 101))}")
    print(f"  两者一致：{'✓' if s == sum(range(1, 101)) else '✗'}")

    # 示例 2：等差数列 3, 8, 13, 18, ...
    print("\n" + "=" * 50)
    print("示例 2：a_1 = 3, d = 5 的等差数列")
    print("  前 10 项：", [arithmetic_term(3, 5, n) for n in range(1, 11)])
    print(f"  第 100 项：a_100 = {arithmetic_term(3, 5, 100)}")
    print(f"  前 100 项和：S_100 = {arithmetic_sum(3, 5, 100)}")

    # 示例 3：线性关系验证
    print("\n" + "=" * 50)
    print("示例 3：等差数列与线性函数的关系")
    a1, d = 2, 3
    print(f"  a_1 = {a1}, d = {d}")
    print(f"  通项公式：a_n = {d}n + {a1 - d}")
    print(f"  这是一个关于 n 的一次函数（斜率={d}，截距={a1 - d}）")
    for n in [1, 5, 10, 20]:
        an = arithmetic_term(a1, d, n)
        linear = d * n + (a1 - d)
        print(f"  n={n}: a_n = {an}, 线性函数值 = {linear}, 一致：{'✓' if an == linear else '✗'}")
