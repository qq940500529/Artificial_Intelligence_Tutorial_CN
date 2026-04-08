# 文件：code/sequence_limits.py
# 数列极限的数值验证
# 环境要求：Python 3.10+（仅使用标准库）


def show_limit(name: str, sequence_fn, expected_limit, ns=None):
    """展示数列趋近极限的过程"""
    if ns is None:
        ns = [10, 100, 1000, 10000, 100000]
    print(f"\n数列：{name}")
    print(f"  理论极限：{expected_limit}")
    for n in ns:
        val = sequence_fn(n)
        error = abs(val - expected_limit) if expected_limit is not None else None
        if error is not None:
            print(f"  n={n:>6d}: a_n = {val:.10f}, 误差 = {error:.2e}")
        else:
            print(f"  n={n:>6d}: a_n = {val:.10f}")


if __name__ == "__main__":
    print("=" * 55)
    print("数列极限的数值验证")
    print("=" * 55)

    # 1/n → 0
    show_limit("a_n = 1/n", lambda n: 1/n, 0)

    # (1/2)^n → 0
    show_limit("a_n = (1/2)^n", lambda n: 0.5**n, 0)

    # (3n²+5n-1)/(2n²-n+4) → 3/2
    show_limit(
        "a_n = (3n²+5n-1)/(2n²-n+4)",
        lambda n: (3*n**2 + 5*n - 1) / (2*n**2 - n + 4),
        1.5
    )

    # (n+1)/n → 1
    show_limit("a_n = (n+1)/n", lambda n: (n+1)/n, 1)

    # 发散数列：(-1)^n
    print("\n" + "=" * 55)
    print("发散数列示例：a_n = (-1)^n")
    print("  该数列在 -1 和 1 之间永远摆动，不收敛：")
    for n in range(1, 11):
        print(f"  n={n}: a_n = {(-1)**n}")

    # AI 模拟：损失函数收敛
    print("\n" + "=" * 55)
    print("AI 模拟：损失函数的'收敛'过程")
    loss = 10.0
    decay = 0.95
    print(f"  初始损失：{loss}")
    for epoch in range(1, 51):
        loss = loss * decay
        if epoch % 10 == 0:
            print(f"  Epoch {epoch:>3d}: loss = {loss:.6f}")
    print(f"  理论极限：0（因为 0.95^n → 0）")
