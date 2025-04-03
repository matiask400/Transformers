import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays using a binary search approach.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the two sorted arrays as a float.
        """
        m = len(nums1)
        n = len(nums2)

        # Ensure nums1 is the shorter array for optimization
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        total_length = m + n
        half_len = (total_length + 1) // 2 # Calculate the size of the left partition

        low = 0
        high = m # Binary search range for partition index in nums1

        while low <= high:
            partition1 = (low + high) // 2 # Partition index for nums1
            partition2 = half_len - partition1 # Corresponding partition index for nums2

            # Determine the boundary elements around the partitions
            # Use -infinity and +infinity for elements outside the array bounds
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')

            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')

            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correct partition found, calculate median
                if total_length % 2 == 1: # Odd total length
                    return float(max(maxLeft1, maxLeft2))
                else: # Even total length
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # Partition in nums1 is too large, move left
                high = partition1 - 1
            else: # maxLeft2 > minRight1
                # Partition in nums1 is too small, move right
                low = partition1 + 1

        # This part should technically not be reached if inputs are valid sorted arrays
        # According to constraints and logic, a solution must exist within the loop.
        # However, including a fallback or error for completeness.
        raise ValueError("Input arrays are not sorted or invalid.")


# --- Testing Framework ---
def run_tests():
    solution = Solution()
    test_cases = [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
        ([0, 0], [0, 0], 0.00000),
        ([], [1], 1.00000),
        ([2], [], 2.00000),
        ([1], [1], 1.00000),
        ([1, 2, 3], [4, 5, 6], 3.50000),
        ([1, 2, 3, 4], [5, 6], 3.50000),
        ([5, 6], [1, 2, 3, 4], 3.50000),
        ([1, 1, 1], [1, 1, 1], 1.00000),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.50000),
        ([1], [2,3,4,5,6,7,8,9,10], 5.5), # Test with very different sizes
        ([100], [1,2,3], 2.5),
        ([1,2,3,4,5],[], 3.0),
        ([], [2,3,4,5,6], 4.0)
    ]

    correct_count = 0
    total_tests = len(test_cases)
    epsilon = 1e-5 # Tolerance for floating point comparison

    for i, (nums1, nums2, expected) in enumerate(test_cases):
        result = solution.findMedianSortedArrays(nums1, nums2)
        passed = abs(result - expected) < epsilon
        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1

    print(f"\nResult: {correct_count} / {total_tests} correct")

if __name__ == "__main__":
    run_tests()