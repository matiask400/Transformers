def find_max_average(nums, k):
    """
    Finds the contiguous subarray of given length k that has the maximum average value.

    Args:
        nums: A list of integers.
        k: The length of the subarray.

    Returns:
        The maximum average value.
    """
    n = len(nums)
    if n < k or k <= 0:
        return 0.0  # Or raise an exception, depending on desired behavior

    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k


def test_find_max_average():
    """
    Tests the find_max_average function with several test cases.
    """
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 4, 0, 3, 2], 1, 4.0),
        ([4, 2, 1, 3, 3], 2, 3.0),
        ([1, 12, -5, -6, 50, 3], 1, 50.0),
        ([-1,-1,-2,-3,-4], 2, -1.5)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (nums, k, expected) in enumerate(test_cases):
        result = find_max_average(nums, k)
        if abs(result - expected) < 1e-5:  # Allow for small floating-point errors
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")

    print(f"\nCorrect: {correct_count}/{total_count}")


if __name__ == "__main__":
    test_find_max_average()