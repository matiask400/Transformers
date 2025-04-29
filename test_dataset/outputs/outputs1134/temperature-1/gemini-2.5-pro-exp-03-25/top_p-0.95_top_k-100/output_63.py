import math
from typing import List

class Solution:
    """
    Implements the solution to find a peak element using binary search.
    A peak element is an element that is strictly greater than its neighbors.
    The array is treated as if nums[-1] = nums[n] = -infinity.
    """
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element using binary search.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        n = len(nums)
        left, right = 0, n - 1

        # Handle edge case of single element array
        if n == 1:
            return 0

        while left < right:
            mid = left + (right - left) // 2

            # Compare middle element with its right neighbor
            # If nums[mid] < nums[mid + 1], it means the peak must be to the right
            # because we are currently on an upward slope (or starting one).
            # Since nums[n] = -infinity, the slope must eventually go down.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If nums[mid] > nums[mid + 1], it means nums[mid] could be a peak,
            # or the peak is to the left. We are on a downward slope (or at the peak).
            # Since nums[-1] = -infinity, there must be a peak to the left or at mid.
            else:
                right = mid

        # When the loop terminates, left == right, which points to a peak element.
        # The loop invariant maintained is that a peak exists within the [left, right] range.
        # When left == right, the range contains a single element, which must be a peak.
        return left

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the Solution's findPeakElement method.
    """
    solver = Solution()
    # Format: (input_nums, possible_expected_outputs)
    # Since multiple peaks might exist, we list all valid indices.
    test_cases = [
        ([1, 2, 3, 1], {2}),
        ([1, 2, 1, 3, 5, 6, 4], {1, 5}),
        ([1], {0}),
        ([3, 2, 1], {0}),
        ([1, 2, 3], {2}),
        ([5, 4, 3, 2, 1], {0}),
        ([1, 3, 2, 0, -1], {1}),
        ([-1, 0, 2, 3, 1], {3}),
        ([1,2,1,2,1], {1, 3}), # Test multiple peaks
        ([6,5,4,3,2,3,2], {0, 5}), # Test peaks at edges and middle
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, (nums, expected_indices) in enumerate(test_cases):
        try:
            result = solver.findPeakElement(nums.copy()) # Use copy to avoid modification if needed
            # Check if the returned index is one of the valid peak indices
            passed = result in expected_indices
            print(f"Test Case {i + 1}: Input={nums}, Output={result}, Expected Possible={expected_indices} -> {passed}")
            if passed:
                correct_tests += 1
        except Exception as e:
            print(f"Test Case {i + 1}: Input={nums} -> Failed with error: {e}")

    print(f"\nResult: {correct_tests} / {total_tests} tests passed.")

if __name__ == "__main__":
    run_tests()