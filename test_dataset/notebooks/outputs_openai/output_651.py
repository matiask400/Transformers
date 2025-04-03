def maxA(N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i-1] + 1  # Press 'A'
        for j in range(1, i-2):
            dp[i] = max(dp[i], dp[j] * (i - j -1))
    return dp[N]

def run_tests():
    test_cases = [
        (3, 3),
        (7, 9),
        (1, 1),
        (5, 5),
        (6, 6),
        (8, 12),
        (10, 18),
        (11, 27),
        (15, 81),
        (20, 243)
    ]
    correct = 0
    for inp, expected in test_cases:
        output = maxA(inp)
        result = output == expected
        print(result)
        if result:
            correct += 1
    print(f"{correct}/{len(test_cases)}")

run_tests()