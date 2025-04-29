import sys 
from typing import List # Typing can be helpful but is not strictly required for execution

# Function implementing the solution using XOR
def missingNumber(nums: List[int]) -> int:
    """
    Finds the missing number in a list containing n distinct numbers
    taken from the range [0, n]. Uses the XOR property for O(n) time
    and O(1) space complexity.

    The core idea is that XORing a number with itself results in 0.
    If we XOR all numbers from 0 to n, and then XOR all numbers in the input array,
    all numbers present in both will cancel out, leaving only the missing number.
    missing = (0^1^2^...^n) ^ (nums[0]^nums[1]^...^nums[n-1])

    This can be efficiently calculated in a single loop:
    Initialize missing = n (to include n in the XOR range).
    Then, for each index i from 0 to n-1, XOR missing with i and nums[i].
    missing = n ^ (0^nums[0]) ^ (1^nums[1]) ^ ... ^ ((n-1)^nums[n-1])
          = (0^1^...^(n-1)^n) ^ (nums[0]^nums[1]^...^nums[n-1])

    Args:
        nums: A list of n distinct integers from the range [0, n].

    Returns:
        The missing integer from the range [0, n].
    """
    n = len(nums)
    # Initialize missing result with n. This handles the case where n is missing
    # and ensures n is included in the full range XOR calculation.
    missing = n 
    # Iterate through indices 0 to n-1
    for i in range(n):
        # XOR with the index (representing the expected number at this position if sorted)
        missing ^= i
        # XOR with the actual number present in the array
        missing ^= nums[i]
    # The final value of 'missing' is the number absent from the nums array.
    return missing

# Test runner integrated into the script
def run_solution_tests():
    """
    Runs predefined test cases against the missingNumber function
    and prints the results according to the specified format:
    'True' for each passed test, 'False' for each failed test,
    followed by the final count 'correct_tests/total_tests'.
    """
    test_cases = [
        # Provided Examples
        {'input': {'nums': [3, 0, 1]}, 'expected': 2},
        {'input': {'nums': [0, 1]}, 'expected': 2},
        {'input': {'nums': [9, 6, 4, 2, 3, 5, 7, 0, 1]}, 'expected': 8},
        {'input': {'nums': [0]}, 'expected': 1},
        # Additional Test Cases
        {'input': {'nums': list(range(10))}, 'expected': 10}, # n is missing
        {'input': {'nums': list(range(1, 11))}, 'expected': 0}, # 0 is missing
        {'input': {'nums': [0, 1, 2, 4, 5]}, 'expected': 3}, # Middle number missing
        {'input': {'nums': [1, 2]}, 'expected': 0}, # Small case, 0 missing
        {'input': {'nums': [1]}, 'expected': 0}, # Smallest case n=1, 0 missing
        {'input': {'nums': [2, 0]}, 'expected': 1}, # Another small case
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for test in test_cases:
        # Make a copy of the input list to ensure the original test case is not modified.
        # list() constructor or slicing [:] can be used for this.
        nums_input = list(test['input']['nums']) 
        expected_output = test['expected']
        
        # Execute the function under test
        actual_output = missingNumber(nums_input) 
        
        # Compare the actual result with the expected result
        is_correct = (actual_output == expected_output)
        
        # Print 'True' or 'False' for the current test case
        print(f"{is_correct}") 
        
        # Increment the counter if the test passed
        if is_correct:
            correct_count += 1

    # Print the final summary: correct_count / total_tests
    print(f"{correct_count}/{total_tests}")

# Execute the test runner function directly when the script is run
run_solution_tests()