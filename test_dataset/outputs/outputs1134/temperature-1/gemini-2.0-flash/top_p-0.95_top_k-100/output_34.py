def least_operators(x, target):
    """
    Finds the least number of operators to reach the target.

    Args:
        x: The single positive integer.
        target: The target value.

    Returns:
        The least number of operators used.
    """
    dp = {}

    def solve(val):
        if (val, ) in dp:
            return dp[(val, )]

        if abs(val - target) < x:
            dp[(val, )] = min(abs(val - target), 2 if target != x else float('inf'))
            return dp[(val, )]

        ans = float('inf')
        ans = min(ans, 1 + solve(val * x))
        ans = min(ans, 1 + solve(val / x))
        ans = min(ans, 1 + solve(val + x))
        ans = min(ans, 1 + solve(val - x))
        dp[(val, )] = ans
        return ans

    if x == target:
        return 0

    result = solve(x)
    return result


def test_cases():
    test_data = [
        (3, 19, 5),
        (5, 501, 8),
        (100, 100000000, 3),
        (2, 1, float('inf')),
        (2, 3, 2),
        (2, 4, 1),
        (2, 5, 2),
        (3, 1, float('inf')),
        (3, 3, 0),
        (3, 6, 1),
        (3, 9, 1),
        (3, 12, 2),
    ]

    correct_count = 0
    total_count = len(test_data)

    for x, target, expected in test_data:
        result = least_operators(x, target)

        if result == expected or (expected == float('inf') and result == float('inf')):

            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_cases()