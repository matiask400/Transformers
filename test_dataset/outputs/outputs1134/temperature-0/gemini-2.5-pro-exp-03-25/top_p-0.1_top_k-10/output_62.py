import sys

def longestOnes(A, K):
    """
    Finds the length of the longest contiguous subarray containing only 1s,
    allowing up to K flips from 0 to 1.

    Args:
        A: A list of 0s and 1s.
        K: The maximum number of 0s allowed to be flipped to 1s.

    Returns:
        The length of the longest such subarray.
    """
    left = 0
    max_len = 0
    zero_count = 0
    n = len(A)

    for right in range(n):
        # If the current element is 0, increment the count of zeros in the window
        if A[right] == 0:
            zero_count += 1

        # If the number of zeros in the current window exceeds K,
        # shrink the window from the left until the condition is met again.
        while zero_count > K:
            # If the element leaving the window from the left is a 0, decrement zero_count
            if A[left] == 0:
                zero_count -= 1
            # Move the left boundary of the window one step to the right
            left += 1

        # After potentially shrinking, the current window [left, right] is valid
        # (contains at most K zeros). Calculate its length and update max_len.
        current_len = right - left + 1
        max_len = max(max_len, current_len)

    return max_len

def run_tests():
    """
    Runs predefined test cases against the longestOnes function and prints the results.
    """
    test_cases = [
        # Example 1
        {"input": ([1,1,1,0,0,0,1,1,1,1,0], 2), "expected": 6},
        # Example 2
        {"input": ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), "expected": 10},
        # Additional Test Cases
        {"input": ([0,0,0,1], 4), "expected": 4}, # K >= num_zeros
        {"input": ([1,1,1,1,1], 2), "expected": 5}, # All ones
        {"input": ([0,0,0,0], 0), "expected": 0}, # All zeros, K=0
        {"input": ([0,0,0,0], 2), "expected": 2}, # All zeros, K=2
        {"input": ([], 1), "expected": 0}, # Empty array
        {"input": ([1], 0), "expected": 1}, # Single 1, K=0
        {"input": ([0], 0), "expected": 0}, # Single 0, K=0
        {"input": ([0], 1), "expected": 1}, # Single 0, K=1
        {"input": ([1,0,1,0,1], 1), "expected": 3}, # Flip one 0
        {"input": ([1,0,0,1,1,0,1], 1), "expected": 4}, # Window [1,1,0,1] -> [1,1,1,1]
        {"input": ([0,0,0,0,0], 5), "expected": 5}, # Flip all
        {"input": ([1,1,1,1,1,1], 0), "expected": 6}, # No flips needed
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        A, K = test_case["input"]
        expected = test_case["expected"]
        # Pass a copy of A to avoid potential modification issues if the function were mutable
        result = longestOnes(list(A), K) 
        
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            # It's helpful to see the inputs on failure
            print(f"Test {i+1}: False. Input: A={A}, K={K}. Expected: {expected}, Got: {result}")

    print(f"\n{correct_count}/{total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()