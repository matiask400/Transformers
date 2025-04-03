def find_max_average_subarray(nums, k):
    """
    Finds the contiguous subarray of length k with the maximum average value.

    Args:
        nums: A list of integers.
        k: The length of the subarray.

    Returns:
        The maximum average value.
    """
    n = len(nums)
    if k > n:
        return 0.0  # Or handle as error, depending on requirements

    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)

    return max_sum / k

def run_tests():
    test_cases = [
        (([1, 12, -5, -6, 50, 3], 4), 12.75),
        (([5], 1), 5.0),
        (([1, 2, 3, 4, 5], 3), 4.0),
        (([0, 0, 0, 0], 2), 0.0),
        (([-1, -2, -3, -4], 2), -1.5),
        (([4, 2, 1, 3, 3], 2), 3.0),
        (([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), 8.0),
        (([1, 1, 1, 1, 1], 5), 1.0),
        (([1, 2, 3, 4, 5], 1), 5.0),
        (([5, 4, 3, 2, 1], 1), 5.0),

    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for input_data, expected_output in test_cases:
        nums, k = input_data
        actual_output = find_max_average_subarray(nums, k)
        if abs(actual_output - expected_output) < 1e-9:  # Using a small tolerance for float comparison
            print("True")
            correct_tests += 1
        else:
            print("False")
            print(f"  Input: nums={nums}, k={k}")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output:   {actual_output}")

    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    run_tests()