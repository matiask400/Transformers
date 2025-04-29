def min_start_value(nums):
    """
    Calculates the minimum positive value of startValue such that the step by step sum is never less than 1.

    Args:
        nums (list of int): An array of integers.

    Returns:
        int: The minimum positive value of startValue.
    """
    startValue = 1
    while True:
        step_sum = startValue
        is_valid = True
        for num in nums:
            step_sum += num
            if step_sum < 1:
                is_valid = False
                break
        if is_valid:
            return startValue
        else:
            startValue += 1

def test_min_start_value():
    """
    Tests the min_start_value function with several test cases.
    """
    test_cases = [
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ([1, -1, -2], 3),
        ([-5, -2, 4, 5], 8),
        ([0], 1),
        ([0, -1], 2)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (nums, expected) in enumerate(test_cases):
        actual = min_start_value(nums)
        if actual == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {nums}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")
    
    print(f"\n{correct_count} / {total_count}")
    
    

if __name__ == "__main__":
    test_min_start_value()