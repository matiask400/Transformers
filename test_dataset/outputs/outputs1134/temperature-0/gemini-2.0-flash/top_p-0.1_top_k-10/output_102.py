def max_a(n):
    """
    Calculates the maximum number of 'A's that can be printed on the screen
    given N key presses.

    Args:
        n: The number of key presses.

    Returns:
        The maximum number of 'A's that can be printed.
    """
    if n <= 6:
        return n

    dp = [0] * (n + 1)
    for i in range(1, 7):
        dp[i] = i

    for i in range(7, n + 1):
        dp[i] = max(dp[i - 1] + 1, dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

    return dp[n]

def test_max_a():
    """
    Tests the max_a function with several test cases.
    """
    test_cases = [
        (3, 3),
        (7, 9),
        (1, 1),
        (6, 6),
        (8, 12),
        (9, 16),
        (10, 20),
        (11, 27),
        (12, 36),
        (13, 48),
        (14, 64),
        (15, 81),
        (16, 108),
        (17, 144),
        (18, 192),
        (19, 256),
        (20, 324),
        (50, 5704887808)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (n, expected) in enumerate(test_cases):
        actual = max_a(n)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {n}, Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_max_a()