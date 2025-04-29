def max_a(n):
    """
    Finds the maximum number of 'A's that can be printed on screen using the given keyboard operations within N presses.

    Args:
        n (int): The number of key presses allowed.

    Returns:
        int: The maximum number of 'A's that can be printed.
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1  # Press 'A'
        for j in range(3, i):
            dp[i] = max(dp[i], dp[i - j] * (j - 1))  # Ctrl-A, Ctrl-C, (j-2) times Ctrl-V
    return dp[n]


def test_max_a():
    """
    Tests the max_a function with various inputs and expected outputs.
    """
    test_cases = [
        (3, 3),
        (7, 9),
        (1, 1),
        (2, 2),
        (4, 4),
        (5, 5),
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
        (20, 336),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_n, expected_output in test_cases:
        actual_output = max_a(input_n)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {input_n}, Expected: {expected_output}, Actual: {actual_output}")

    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_max_a()