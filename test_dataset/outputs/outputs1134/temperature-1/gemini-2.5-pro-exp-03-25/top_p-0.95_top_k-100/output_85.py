import math

def solve_and_test():
    """
    Solves the Maximum Average Subarray I problem for predefined test cases.
    It calculates the maximum average for a contiguous subarray of length k
    for each test case, compares the result to the expected output,
    prints 'True' or 'False' for each test, and finally prints the
    ratio of correct tests.
    """

    # --- Test Case Data ---
    # Each element is a tuple: (nums_array, k_value, expected_output)
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 0, 0, 0, 0], 3, 0.0),
        ([-1, -2, -3, -4, -5], 2, -1.5),
        ([1, 2, 3, 4, 5], 5, 3.0),
        # Use float division for expected value when it's non-terminating
        ([10000, 10000, -10000, -10000, 10000], 3, 10000.0 / 3.0), 
        ([4, 0, 4, 3, 3], 5, 2.8),
        # Additional test cases
        ([1, 1, 1, 1, 1], 2, 1.0),
        ([-1], 1, -1.0) 
    ]

    correct_count = 0
    total_tests = len(test_cases)
    # Tolerance for comparing floating-point numbers
    epsilon = 1e-9 

    for i, (nums, k, expected) in enumerate(test_cases):

        # --- Core Logic: Find Max Average Subarray ---
        n = len(nums)
        result = float('-inf') # Initialize with negative infinity for max comparison

        # Validate constraints (although problem statement guarantees valid inputs)
        # 1 <= k <= n <= 30000
        # If constraints were not guaranteed, more robust checks would be needed.
        if not (1 <= k <= n):
             # According to problem constraints, this block should not be reached.
             # If it could, define appropriate behavior (e.g., raise error, return NaN)
             # We'll calculate normally assuming constraints hold.
             pass # Fall through to calculation

        # Handle edge case of empty array (not possible by constraints n>=k>=1)
        if n == 0:
             result = 0.0 # Or handle as error
        # Handle k=0 (not possible by constraints k>=1)
        elif k == 0:
             result = 0.0 # Or handle as error
        else:
            # Calculate sum of the first window
            current_sum = sum(nums[0:k])
            max_sum = current_sum

            # Slide the window across the array
            for j in range(k, n):
                # Efficiently update sum: add new element, remove old element
                current_sum += nums[j] - nums[j - k]
                max_sum = max(max_sum, current_sum)

            # Calculate the maximum average
            result = float(max_sum) / k
        
        # --- End of Core Logic ---

        # --- Test Comparison ---
        passed = False
        # Use tolerance for comparing floats
        if abs(result - expected) < epsilon:
            passed = True
        # Handle potential edge case where both are NaN (e.g., from invalid inputs if allowed)
        elif math.isnan(result) and math.isnan(expected):
             passed = True

        if passed:
            print(f"True")
            correct_count += 1
        else:
            # As required, print False for failed tests. 
            # Debugging info is commented out per instruction to provide only executable code.
            # print(f"False (Input: {nums}, k={k}, Expected: {expected}, Got: {result})")
            print(f"False")

    # --- Final Summary ---
    print(f"{correct_count}/{total_tests}")

# --- Execute the function ---
# This function call will run the tests when the script is executed.
solve_and_test()