def minStartValue(nums):
    min_sum = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
    return 1 - min_sum if min_sum < 1 else 1

def run_tests():
    test_cases = [
        ([-3,2,-3,4,2], 5),
        ([1,2], 1),
        ([1,-2,-3], 5),
        ([1], 1),
        ([-1], 2),
        ([2,3,1,2,4,3], 1),
        ([3, -2, -3, 4, 2], 1),
        ([-2,-3,4], 5),
        ([1,-1,1,-1], 1),
        ([100], 1)
    ]
    correct = 0
    total = len(test_cases)
    for i, (nums, expected) in enumerate(test_cases):
        result = minStartValue(nums)
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

run_tests()