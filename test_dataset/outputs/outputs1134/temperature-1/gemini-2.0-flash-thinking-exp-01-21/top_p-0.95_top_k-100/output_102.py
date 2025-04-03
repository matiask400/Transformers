def solve():
    def max_a_pressed(n):
        if n <= 0:
            return 0
        dp = [0] * (n + 1)
        for i in range(1, min(7, n + 1)):
            dp[i] = i
        for i in range(7, n + 1):
            dp[i] = dp[i-1] + 1
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[n]

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 9),
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
        (20, 341),
        (21, 455),
        (22, 607),
        (23, 809),
        (24, 1079),
        (25, 1439),
        (26, 1919),
        (27, 2559),
        (28, 3412),
        (29, 4549),
        (30, 6065),
        (31, 8087),
        (32, 10783),
        (33, 14377),
        (34, 19169),
        (35, 25559),
        (36, 34079),
        (37, 45439),
        (38, 60581),
        (39, 80775),
        (40, 107693),
        (50, 537777),
    ]

    correct_count = 0
    for n, expected_output in test_cases:
        actual_output = max_a_pressed(n)
        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')
            print(f"Input: {n}, Expected: {expected_output}, Actual: {actual_output}")

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == "__main__":
    solve()