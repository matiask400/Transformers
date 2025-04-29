def min_start_value(nums):
    """
    Finds the minimum positive value of startValue such that the step by step sum is never less than 1.

    Args:
        nums: An array of integers.

    Returns:
        The minimum positive value of startValue.
    """
    start_value = 1
    while True:
        current_sum = start_value
        is_valid = True
        for num in nums:
            current_sum += num
            if current_sum < 1:
                is_valid = False
                break
        if is_valid:
            return start_value
        start_value += 1

def test_min_start_value():
    """
    Tests the min_start_value function with several test cases.
    """
    test_cases = [
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ([-1, -2], 4),
        ([2, -5, 3], 3),
        ([-5, 4, -2, 3, 1, -1, -6, -1, 0, 5], 8)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (nums, expected) in enumerate(test_cases):
        actual = min_start_value(nums)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {nums}, Expected: {expected}, Actual: {actual})")

    print(f"\nCorrect: {correct_count}/{total_count}")

if __name__ == "__main__":
    test_min_start_value()