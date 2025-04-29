import math

def findPeakElement(nums: list[int]) -> int:
    """
    Finds a peak element in an integer array.

    A peak element is strictly greater than its neighbors.
    The array is considered to have nums[-1] = nums[n] = -infinity.

    Args:
        nums: A list of integers where nums[i] != nums[i+1].

    Returns:
        The index of any peak element found.
    """
    n = len(nums)
    left, right = 0, n - 1

    # Binary search approach
    # The loop invariant is that there is at least one peak
    # within the range [left, right].
    while left < right:
        mid = left + (right - left) // 2
        
        # Compare mid element with its right neighbor
        if nums[mid] < nums[mid + 1]:
            # The numbers are increasing at mid.
            # This means a peak must exist to the right of mid (inclusive of mid+1).
            # Why? If the sequence keeps increasing, the last element is a peak.
            # If it starts decreasing at some point k > mid, then nums[k] is a peak.
            left = mid + 1
        else:
            # nums[mid] > nums[mid + 1] (since nums[i] != nums[i+1])
            # The numbers are decreasing at mid.
            # This means a peak must exist at mid or to the left of mid.
            # Why? nums[mid] is greater than its right neighbor.
            # If it's also greater than its left neighbor (or it's the first element),
            # then nums[mid] is a peak.
            # If nums[mid-1] > nums[mid], then we look left. Eventually, we either
            # find an element k < mid which is a peak, or the first element nums[0]
            # must be a peak (since nums[-1] = -inf).
            # Therefore, we can safely discard the right part [mid+1, right].
            # We keep 'mid' in the search space because it might be the peak itself.
            right = mid

    # When the loop terminates, left == right.
    # This 'left' index points to a peak element based on the loop invariant
    # and the logic of narrowing the search space.
    return left

# Helper function to verify if an index corresponds to a peak
def is_peak(nums: list[int], index: int) -> bool:
    """Checks if the element at the given index is a peak."""
    n = len(nums)
    if not (0 <= index < n):
        return False # Index out of bounds is not a peak

    # Get value of neighbors, considering boundaries as -infinity
    left_neighbor = nums[index - 1] if index > 0 else -math.inf
    right_neighbor = nums[index + 1] if index < n - 1 else -math.inf

    return nums[index] > left_neighbor and nums[index] > right_neighbor

# Test runner function
def run_tests():
    """Runs test cases and prints the results."""
    test_cases = [
        ([1, 2, 3, 1]),          # Example 1
        ([1, 2, 1, 3, 5, 6, 4]), # Example 2
        ([1]),                   # Single element
        ([1, 2]),                # Two elements, increasing
        ([2, 1]),                # Two elements, decreasing
        ([1, 2, 3, 4, 5]),       # Strictly increasing
        ([5, 4, 3, 2, 1]),       # Strictly decreasing
        ([3, 1, 4, 1, 5, 9, 2, 6]), # Multiple peaks
        ([-2147483648, 2147483647]), # Min/Max int values
        ([10, 20, 15, 2, 23, 90, 67]), # More complex case
        ([6, 5, 4, 3, 2, 3, 2]), # Peak in the middle after decrease
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, nums in enumerate(test_cases):
        # Find a peak using the implemented function
        try:
            actual_index = findPeakElement(nums)
            # Verify if the returned index is actually a peak
            test_passed = is_peak(nums, actual_index)
        except Exception as e:
            print(f"Test Case {i+1} (Input: {nums}) failed with error: {e}")
            test_passed = False
            
        print(f"{test_passed}") # Print True or False for the test result

        if test_passed:
            correct_count += 1

    print(f"{correct_count}/{total_tests}") # Print final count

# Execute the tests
if __name__ == "__main__":
    run_tests()