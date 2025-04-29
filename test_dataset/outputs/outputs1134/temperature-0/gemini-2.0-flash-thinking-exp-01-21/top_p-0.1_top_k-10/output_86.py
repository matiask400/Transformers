def subarray_sum_equals_k(nums, k):
    """
    Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count

def run_tests():
    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},
        {"nums": [1, 2, 3], "k": 3, "expected": 2},
        {"nums": [1, 2, 3, 4, 5], "k": 7, "expected": 2},
        {"nums": [1, -1, 0], "k": 0, "expected": 3},
        {"nums": [0, 0, 0, 0, 0], "k": 0, "expected": 15},
        {"nums": [-1, -1, 1], "k": 0, "expected": 1},
        {"nums": [1], "k": 1, "expected": 1},
        {"nums": [1], "k": 0, "expected": 0},
        {"nums": [], "k": 0, "expected": 0},
        {"nums": [1, 2, 1, 2, 1], "k": 3, "expected": 4},
        {"nums": [1, 2, 3, -3, 1, 1, 1, 4, 2, -3], "k": 3, "expected": 7}
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        nums = test["nums"]
        k = test["k"]
        expected_output = test["expected"]
        actual_output = subarray_sum_equals_k(nums, k)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()