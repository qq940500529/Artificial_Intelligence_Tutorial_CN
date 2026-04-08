# 文件：code/geometric_sequence.py
# 等比数列的通项公式、求和与无穷级数
# 环境要求：Python 3.10+（仅使用标准库）


def geometric_term(a1: float, q: float, n: int) -> float:
    """等比数列通项公式：a_n = a_1 * q^(n-1)"""
    return a1 * q ** (n - 1)


def geometric_sum(a1: float, q: float, n: int) -> float:
    """等比数列求和公式"""
    if q == 1:
        return n * a1
    return a1 * (1 - q ** n) / (1 - q)


def geometric_infinite_sum(a1: float, q: float) -> float:
    """无穷等比级数求和（|q| < 1）"""
    if abs(q) >= 1:
        raise ValueError("|q| 必须小于 1")
    return a1 / (1 - q)


if __name__ == "__main__":
    # 示例 1：复利增长
    print("=" * 50)
    print("示例 1：1000 元存款，年利率 10%，10 年后")
    a1, q, n = 1000, 1.1, 10
    an = geometric_term(a1, q, n)
    print(f"  第 {n} 年末金额：{an:.2f} 元")

    # 示例 2：学习率指数衰减
    print("\n" + "=" * 50)
    print("示例 2：学习率从 0.01 开始，每 epoch 乘以 0.95")
    lr0, decay = 0.01, 0.95
    for epoch in [1, 10, 50, 100]:
        lr = geometric_term(lr0, decay, epoch)
        print(f"  Epoch {epoch}: lr = {lr:.6f}")

    # 示例 3：无穷等比级数
    print("\n" + "=" * 50)
    print("示例 3：1 + 1/2 + 1/4 + 1/8 + ...")
    s_inf = geometric_infinite_sum(1, 0.5)
    print(f"  理论值（公式）：{s_inf}")
    s_approx = geometric_sum(1, 0.5, 30)
    print(f"  前 30 项近似值：{s_approx:.10f}")

    # 示例 4：强化学习折扣累积奖励
    print("\n" + "=" * 50)
    print("示例 4：折扣累积奖励（每步奖励 1，折扣因子 γ=0.99）")
    gamma = 0.99
    s_inf = geometric_infinite_sum(1, gamma)
    print(f"  理论最大累积奖励：{s_inf:.2f}")
    s_100 = geometric_sum(1, gamma, 100)
    print(f"  前 100 步累积奖励：{s_100:.2f}")
