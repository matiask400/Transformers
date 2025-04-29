def subarray_sum_equals_k(nums, k):
    """
    Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

    Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

    Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

    Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107
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
        {"nums": [1], "k": 1, "expected": 1},
        {"nums": [1], "k": 2, "expected": 0},
        {"nums": [], "k": 0, "expected": 0},
        {"nums": [-1, -1, 1], "k": -2, "expected": 1},
        {"nums": [0, 0, 0], "k": 0, "expected": 6},
        {"nums": [1, -1, 0], "k": 0, "expected": 3},
        {"nums": [1, 2, 3, 4, 5], "k": 9, "expected": 2},
        {"nums": [1, 2, 1, 2, 1], "k": 3, "expected": 4},
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, test_case in enumerate(test_cases):
        nums = test_case["nums"]
        k = test_case["k"]
        expected = test_case["expected"]
        actual = subarray_sum_equals_k(nums, k)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")

    print(f"\n{correct_count}/{total_count}")

if __name__ == '__main__':
    run_tests()