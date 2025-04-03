import math # Included for completeness, though not strictly needed for this specific solution

def fixed_point(arr):
    """
    Finds the smallest index i such that arr[i] == i in a sorted array of distinct integers.

    Args:
        arr: A list of distinct integers sorted in ascending order.

    Returns:
        The smallest index i such that arr[i] == i, or -1 if no such index exists.
    """
    left, right = 0, len(arr) - 1
    result = -1  # Initialize result to -1 (no fixed point found yet)

    while left <= right:
        mid = left + (right - left) // 2  # Calculate midpoint to avoid potential overflow

        if arr[mid] == mid:
            # Found a potential fixed point. Since we want the smallest,
            # store this index and continue searching in the left half.
            result = mid
            right = mid - 1
        elif arr[mid] < mid:
            # If arr[mid] < mid, then for any index j < mid, arr[j] must also be < j
            # because the array is sorted with distinct integers (arr[j] <= arr[mid] - (mid - j) < mid - (mid - j) = j).
            # Therefore, the fixed point (if it exists) must be in the right half.
            left = mid + 1
        else: # arr[mid] > mid
            # If arr[mid] > mid, then for any index k > mid, arr[k] must also be > k
            # because arr[k] >= arr[mid] + (k - mid) > mid + (k - mid) = k.
            # Therefore, the fixed point (if it exists) must be in the left half.
            # This also covers the case where we found a fixed point earlier (result != -1)
            # and are now looking for a potentially smaller one to the left.
            right = mid - 1

    return result

def run_tests():
    """
    Runs test cases against the fixed_point function and prints the results.
    """
    test_cases = [
        # Example 1
        {"input": [-10, -5, 0, 3, 7], "expected": 3},
        # Example 2
        {"input": [0, 2, 5, 8, 17], "expected": 0},
        # Example 3
        {"input": [-10, -5, 3, 4, 7, 9], "expected": -1},
        # Additional Test Cases
        {"input": [-1, 1], "expected": 1}, # Smallest is not the first found during search
        {"input": [-5, -3, 0, 1, 4], "expected": 4}, # Fixed point at the end
        {"input": [0], "expected": 0}, # Single element, fixed point
        {"input": [1], "expected": -1}, # Single element, no fixed point
        {"input": [-2, 0, 2, 3, 6, 7, 9], "expected": 2}, # Another test case
        {"input": [-10, -5, -2, 0, 4, 5, 9], "expected": 4}, # Fixed point in the middle
        {"input": [0, 1, 2, 3, 4, 5], "expected": 0}, # All elements are fixed points, return smallest (0)
        {"input": [1, 2, 3, 4, 5], "expected": -1}, # No fixed points
        {"input": [-5, -4, -3, -2, -1], "expected": -1}, # No fixed points (all negative)
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, test in enumerate(test_cases):
        arr = test["input"]
        expected = test["expected"]
        actual = fixed_point(arr)
        
        result = actual == expected
        print(f"{result}")
        
        if result:
            correct_count += 1

    print(f"\n{correct_count} / {total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()