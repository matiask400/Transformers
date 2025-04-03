import sys
import io

def solve(A, K):
    """
    Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
    Return the length of the longest (contiguous) subarray that contains only 1s.

    Args:
        A: A list of integers (0s and 1s).
        K: The maximum number of 0s allowed to be flipped to 1s.

    Returns:
        The length of the longest contiguous subarray containing only 1s 
        after flipping at most K zeros.
    """
    start = 0
    max_length = 0
    zero_count = 0

    for end in range(len(A)):
        # If the current element is 0, increment the count of zeros in the window
        if A[end] == 0:
            zero_count += 1

        # If the number of zeros in the current window exceeds K,
        # shrink the window from the left until it's valid again.
        while zero_count > K:
            # If the element leaving the window is a 0, decrement the count
            if A[start] == 0:
                zero_count -= 1
            # Move the start pointer to the right
            start += 1

        # After ensuring the window is valid (zero_count <= K),
        # calculate its length and update max_length if it's larger.
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length

def run_tests():
    """
    Runs test cases against the solve function and prints the results.
    """
    test_cases = [
        # Provided examples
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
        
        # Edge cases
        ([0,0,0,0], 0, 0), # K=0, only zeros
        ([1,1,1,1], 2, 4), # K > 0, only ones
        ([0,0,0,1], 4, 4), # K >= len(A)
        ([1,0,1,0,1], 1, 3), # Flip one 0
        ([0,0,0,0,0], 2, 2), # Flip some zeros
        ([1], 1, 1),       # Single element array (1)
        ([0], 1, 1),       # Single element array (0), can flip
        ([0], 0, 0),       # Single element array (0), cannot flip
        
        # Larger cases
        ([0]*5 + [1]*5 + [0]*5 + [1]*5, 3, 8), # Mix of blocks
        ([1,0,0,1,0,1,0,0,0,1,1,0], 3, 7), # Example: [0,1,0,1,1,1,1,1,1,1,1,0] -> len 7
        
        # Cases testing window shrinking logic
        ([0,0,0,1,1,1,0,0], 1, 4), # Window: [1,1,1,0] or [0,1,1,1] -> Max len 4
        ([0,0,0,1,1,1,0,0], 0, 3), # K=0 -> [1,1,1] -> Max len 3
        
        # Performance considerations (simulated large inputs)
        ([1]*10000 + [0]*10000, 5000, 15000),
        ([0]*10000 + [1]*10000, 5000, 15000),
        ([i % 2 for i in range(20000)], 10000, 20000), # Alternating, K=num_zeros
        ([i % 2 for i in range(20000)], 5000, 10000), # Alternating, K=half_num_zeros
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Capture stdout to prevent intermediate prints from interfering
    # This part is mainly for cleaner output formatting when running locally
    # In platforms like LeetCode, you'd just return the value from solve()
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, (A, K, expected) in enumerate(test_cases):
        # Create a copy to avoid potential modification by the function if it did so
        A_copy = list(A) 
        result = solve(A_copy, K)
        passed = result == expected
        print(f"{passed}") # Print True/False for each test result
        if passed:
            correct_count += 1

    # Restore stdout and print summary
    sys.stdout = old_stdout
    print(captured_output.getvalue().strip()) # Print the captured True/False results
    print(f"\nPassed {correct_count} out of {total_tests} tests.")

# Execute the tests when the script is run
if __name__ == '__main__':
    run_tests()