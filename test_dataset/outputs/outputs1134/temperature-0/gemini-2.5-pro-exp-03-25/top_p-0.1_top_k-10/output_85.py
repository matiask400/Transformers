import math

def findMaxAverage(nums, k):
    """
    Finds the contiguous subarray of length k with the maximum average value.

    Args:
        nums: A list of integers.
        k: The length of the subarray.

    Returns:
        The maximum average value as a float.
    """
    n = len(nums)
    if n < k:
        # This case should not happen based on constraints 1 <= k <= n
        # but good practice to handle it.
        return 0.0 if n == 0 else sum(nums) / n

    # Calculate the sum of the first window of size k
    current_sum = sum(nums[0:k])
    max_sum = current_sum

    # Slide the window from the k-th element to the end
    for i in range(k, n):
        # Update the sum by subtracting the element that just left the window
        # and adding the new element that just entered the window.
        current_sum = current_sum - nums[i - k] + nums[i]
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)

    # The maximum average is the maximum sum divided by k
    return max_sum / k

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the findMaxAverage function.
    """
    test_cases = [
        # Format: (input_nums, input_k, expected_output)
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 1, 1, 3, 3], 4, 2.0),
        ([-1], 1, -1.0),
        ([1, 2, 3, 4, 5], 1, 5.0),
        ([1, 2, 3, 4, 5], 5, 3.0),
        ([4, 0, 4, 3, 3], 5, 2.8),
        ([1,1,1,1,1], 2, 1.0),
        ([-10000, 10000, -10000, 10000], 2, 0.0),
        ([0, 0, 0, 0, 0], 3, 0.0),
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (nums, k, expected) in enumerate(test_cases):
        result = findMaxAverage(nums, k)
        # Using math.isclose for robust floating-point comparison
        if math.isclose(result, expected):
            print(f"Test {i + 1}: True")
            correct_count += 1
        else:
            print(f"Test {i + 1}: False. Input: ({nums}, {k}), Expected: {expected}, Got: {result}")

    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()