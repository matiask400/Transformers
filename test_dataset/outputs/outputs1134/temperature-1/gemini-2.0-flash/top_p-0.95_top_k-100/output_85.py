def find_max_average(nums, k):
    """
    Finds the contiguous subarray of length k that has the maximum average value.

    Args:
        nums: A list of integers.
        k: The length of the subarray.

    Returns:
        The maximum average value.
    """

    n = len(nums)
    if k > n:
        return None  # Or raise an exception, depending on desired behavior

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

def test_find_max_average():
    """Tests the find_max_average function."""

    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5),
        ([1,2,3,4,5], 3, 4.0),
        ([4,2,1,3,3], 2, 3.0),
        ([0,4,0,3,2], 1, 4.0)
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for nums, k, expected in test_cases:
        result = find_max_average(nums, k)
        if abs(result - expected) < 1e-5:  # Compare floating-point numbers with tolerance
            print("True")
            num_correct += 1
        else:
            print("False")
    print(f"{num_correct}/{total_tests}")

if __name__ == '__main__':
    test_find_max_average()