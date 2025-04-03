def subarray_sum(nums, k):
    """
    Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

    Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

    Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

    Constraints:
    `1 <= nums.length <= 2 * 104`
    `-1000 <= nums[i] <= 1000`
    `-107 <= k <= 107`
    """

    count = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count

def test_subarray_sum():
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0),
        ([0,0,0,0,0,0,0,0,0,0],0, 55),
        ([-1,-1,1],0,1),
        ([-1, -1, 1], -2, 1)
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (nums, k, expected) in enumerate(test_cases):
        result = subarray_sum(nums, k)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: nums={nums}, k={k}")
            print(f"  Expected: {expected}, Got: {result}")

    print(f"\nCorrect tests: {correct_tests}/{total_tests}")

if __name__ == '__main__':
    test_subarray_sum()