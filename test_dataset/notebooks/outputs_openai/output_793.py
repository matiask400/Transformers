def find_x_count(K):
    def f(x):
        count = 0
        while x >= 5:
            x = x // 5
            count += x
        return count

    left = 0
    right = 5 * K + 5 if K > 0 else 5
    result = -1
    while left <= right:
        mid = (left + right) // 2
        current = f(mid)
        if current < K:
            left = mid + 1
        else:
            right = mid - 1
    if f(left) == K:
        return 5
    return 0

def run_tests():
    test_cases = [
        {"Input": 0, "Output": 5},
        {"Input": 5, "Output": 0},
        {"Input": 1, "Output": 5},
        {"Input": 2, "Output": 5},
        {"Input": 24, "Output": 5},
        {"Input": 25, "Output": 0},
        {"Input": 6, "Output": 5},
        {"Input": 120, "Output": 5},
        {"Input": 100000, "Output": 5},
        {"Input": 1000000000, "Output": 0},
    ]
    correct = 0
    total = len(test_cases)
    for test in test_cases:
        K = test["Input"]
        expected = test["Output"]
        actual = find_x_count(K)
        if actual == expected:
            print(True)
            correct +=1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()