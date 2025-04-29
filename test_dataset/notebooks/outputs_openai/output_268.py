def missingNumber(nums):
    total = len(nums)
    expected_sum = total * (total + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def run_tests():
    test_cases = [
        {"input": [3, 0, 1], "expected": 2},
        {"input": [0, 1], "expected": 2},
        {"input": [9,6,4,2,3,5,7,0,1], "expected": 8},
        {"input": [0], "expected": 1},
    ]
    correct = 0
    total = len(test_cases)
    for test in test_cases:
        result = missingNumber(test["input"])
        is_correct = result == test["expected"]
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

run_tests()