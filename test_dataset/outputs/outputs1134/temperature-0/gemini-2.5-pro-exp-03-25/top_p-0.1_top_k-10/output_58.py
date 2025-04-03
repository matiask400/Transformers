import sys 

# Function definition
def minStartValue(nums: list[int]) -> int:
    """
    Calculates the minimum positive startValue such that the step-by-step sum
    is never less than 1.

    Args:
        nums: A list of integers representing the steps.

    Returns:
        The minimum positive integer startValue.
    """
    min_prefix_sum = 0  # Initialize minimum prefix sum seen so far
    current_prefix_sum = 0 # Initialize current prefix sum

    # Iterate through the numbers in the input list
    for num in nums:
        # Update the current prefix sum by adding the current number
        current_prefix_sum += num
        # Update the minimum prefix sum encountered
        min_prefix_sum = min(min_prefix_sum, current_prefix_sum)

    # The condition is: startValue + prefix_sum >= 1 for all prefix sums.
    # This must hold true for the minimum prefix sum as well:
    # startValue + min_prefix_sum >= 1
    # Rearranging the inequality to solve for startValue:
    # startValue >= 1 - min_prefix_sum
    
    # Calculate the minimum startValue required based on the minimum prefix sum
    required_start_value = 1 - min_prefix_sum

    # The problem states that startValue must be a positive value (i.e., startValue >= 1).
    # Therefore, the minimum positive startValue is the maximum of 1 and the calculated required value.
    return max(1, required_start_value)

# Testing framework
def run_tests():
    """
    Runs predefined test cases against the minStartValue function and prints the 
    results in the specified format (True/False for each test, then summary).
    """
    # List of test cases, each is a tuple: (input_nums, expected_output)
    test_cases = [
        # Provided examples
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        # Additional test cases
        ([-5], 6), # Single negative number
        ([5], 1),  # Single positive number
        ([2, 3, 5, -5, -1], 1), # Prefix sums never go below 1
        ([-1, -2, -3], 7), # All negative numbers
        ([0, 0, 0], 1), # All zeros
        ([-1, 1, -1, 1], 2), # Alternating signs resulting in negative min prefix sum
        ([100], 1), # Large positive number
        ([-100], 101), # Large negative number
    ]

    correct_count = 0 # Counter for passed tests
    total_tests = len(test_cases) # Total number of tests

    # Iterate through each test case
    for nums_input, expected_output in test_cases:
        # Calculate the result using the implemented function
        result = minStartValue(nums_input)
        # Check if the calculated result matches the expected output
        passed = result == expected_output
        # Print 'True' if the test passed, 'False' otherwise
        print(f"{passed}")
        # Increment the counter if the test passed
        if passed:
            correct_count += 1

    # After running all tests, print the final summary
    # Format: "number_of_correct_tests/total_number_of_tests"
    print(f"{correct_count}/{total_tests}")

# Execute the tests when the script is run directly
if __name__ == "__main__":
    run_tests()