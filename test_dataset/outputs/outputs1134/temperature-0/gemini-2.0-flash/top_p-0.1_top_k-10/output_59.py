def missingNumber(nums):
    """
    Finds the missing number in the range [0, n] in the array nums.

    Args:
        nums: A list of n distinct numbers in the range [0, n].

    Returns:
        The missing number in the range.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def test_missingNumber():
    """
    Tests the missingNumber function with several test cases.
    """
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([0, 2, 3], 1),
        ([1, 2, 3], 0)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (nums, expected) in enumerate(test_cases):
        actual = missingNumber(nums)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {nums}, Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_missingNumber()