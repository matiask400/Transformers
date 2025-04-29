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
        ([1, -1, 0], 0, 3),
        ([0, 0, 0, 0, 0], 0, 15),
        ([-1, -1, 1], 0, 1),
        ([1], 0, 0),
        ([1], 1, 1),
        ([1, 2, 1, 2, 1], 3, 4),
        ([1, 1, 1, 1, 1], 3, 3),
        ([28,54,7,-70,22,65,-6],100,0)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for nums, k, expected in test_cases:
        result = subarray_sum(nums, k)
        if result == expected:
            print("True")
            correct_count += 1
        else:
            print("False")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_subarray_sum()