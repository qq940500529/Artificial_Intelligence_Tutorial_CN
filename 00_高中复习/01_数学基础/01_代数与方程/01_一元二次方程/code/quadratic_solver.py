# 文件：code/quadratic_solver.py
# 一元二次方程求解器
# 环境要求：Python 3.10+（无需额外库）

import math


def solve_quadratic(a: float, b: float, c: float) -> str:
    """
    求解一元二次方程 ax² + bx + c = 0
    返回解的情况和结果
    """
    if a == 0:
        raise ValueError("a 不能为 0，否则不是二次方程")

    # 计算判别式
    delta = b**2 - 4 * a * c

    print(f"方程：{a}x² + {b}x + {c} = 0")
    print(f"判别式 Δ = {b}² - 4×{a}×{c} = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Δ > 0，方程有两个不同的实数解：")
        print(f"  x₁ = {x1}")
        print(f"  x₂ = {x2}")
        return f"x₁ = {x1}, x₂ = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Δ = 0，方程有一个实数解（重根）：")
        print(f"  x = {x}")
        return f"x = {x}"
    else:
        print(f"Δ < 0，方程无实数解")
        return "无实数解"


if __name__ == "__main__":
    # 示例 1：花坛问题 x² + 4x - 5 = 0
    print("=" * 40)
    print("示例 1：花坛问题")
    solve_quadratic(1, 4, -5)

    # 示例 2：重根情况 x² - 4x + 4 = 0
    print("\n" + "=" * 40)
    print("示例 2：重根情况")
    solve_quadratic(1, -4, 4)

    # 示例 3：无实数解 x² + x + 1 = 0
    print("\n" + "=" * 40)
    print("示例 3：无实数解")
    solve_quadratic(1, 1, 1)
