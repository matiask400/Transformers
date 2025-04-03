def solve():
    def candy(ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

    test_cases = [
        {"ratings": [1, 0, 2], "expected": 5},
        {"ratings": [1, 2, 2], "expected": 4},
        {"ratings": [1, 2, 3, 4, 5], "expected": 15},
        {"ratings": [5, 4, 3, 2, 1], "expected": 15},
        {"ratings": [1, 1, 1, 1, 1], "expected": 5},
        {"ratings": [2, 1, 0, 1, 2], "expected": 9},
        {"ratings": [0], "expected": 1},
        {"ratings": [1, 1, 2], "expected": 4},
        {"ratings": [1, 2, 1], "expected": 4},
        {"ratings": [2, 2, 1], "expected": 4},
    ]

    correct_tests = 0
    for i, case in enumerate(test_cases):
        result = candy(case["ratings"])
        if result == case["expected"]:
            print(True)
            correct_tests += 1
        else:
            print(False)
            print(f"Test case {i+1} failed: Input={case['ratings']}, Expected={case['expected']}, Got={result}")

    print(f"{correct_tests}/{len(test_cases)}")

solve()