import math # Importing math although not strictly necessary for the final algorithm

def minStartValue(nums: list[int]) -> int:
    """
    Calculates the minimum positive startValue such that the step-by-step sum
    of startValue plus elements in nums (from left to right) is never less than 1.

    Args:
        nums: A list of integers.

    Returns:
        The minimum positive integer startValue.

    Example:
    If nums = [-3, 2, -3, 4, 2], the prefix sums are:
    -3
    -3 + 2 = -1
    -1 + -3 = -4
    -4 + 4 = 0
    0 + 2 = 2
    The minimum prefix sum is -4.
    We need startValue + prefix_sum >= 1 for all prefix sums.
    So, startValue >= 1 - prefix_sum for all prefix sums.
    This means startValue >= 1 - min(prefix_sums).
    startValue >= 1 - (-4) = 5.
    Since startValue must be positive (>= 1), the minimum startValue is max(1, 5) = 5.

    Algorithm:
    1. Calculate the prefix sums iteratively and find the minimum prefix sum encountered.
       Initialize current_sum = 0 and min_prefix_sum = 0.
       The reason for initializing min_prefix_sum = 0 is that if all prefix sums
       are positive, the minimum calculated this way will be 0, leading to
       required_start = 1 - 0 = 1, which is correct (startValue=1 works).
       If any prefix sum is negative, the minimum calculated this way will be the
       actual minimum negative prefix sum.
    2. Iterate through nums:
       current_sum += num
       min_prefix_sum = min(min_prefix_sum, current_sum)
    3. The condition is startValue + prefix_sum >= 1 for all steps.
       This implies startValue >= 1 - min_prefix_sum found in step 2.
       Let required_start = 1 - min_prefix_sum.
    4. Since startValue must be a positive integer (>= 1), the final answer is
       max(1, required_start).
    """
    min_prefix_sum = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        min_prefix_sum = min(min_prefix_sum, current_sum)

    # We need startValue + prefix_sum >= 1 for all prefix sums.
    # This means startValue >= 1 - min_prefix_sum.
    required_start = 1 - min_prefix_sum

    # The startValue must also be positive (>= 1).
    # Therefore, the minimum startValue is max(1, required_start).
    return max(1, required_start)

# Define the test cases
# Each tuple contains (input_nums, expected_output)
test_cases = [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5),
    ([-1, -2, -3], 7),
    ([5, 4, 3, 2, 1], 1),
    ([2, 3, 5, -10, 6], 1),
    ([-5, 4, -2, 3, 1], 6),
    ([0, 0, 0], 1), # Test with zeros
    ([-1], 2),      # Test with single negative number
    ([1], 1),       # Test with single positive number
]

# Run the tests
correct_tests = 0
total_tests = len(test_cases)

for i, (nums, expected_output) in enumerate(test_cases):
    # Calculate the result using the student's function
    result = minStartValue(nums)
    
    # Compare the result with the expected output
    passed = (result == expected_output)
    
    # Print 'True' or 'False' for each test
    print(f"{passed}")
    
    # Increment the count of correct tests if passed
    if passed:
        correct_tests += 1

# Print the final summary: number of correct tests over total tests
print(f"{correct_tests}/{total_tests}")