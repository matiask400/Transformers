import math

def solve():
    """
    Solves the Median of Two Sorted Arrays problem.
    Finds the median of two sorted arrays nums1 and nums2.
    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        # Ensure nums1 is the shorter array for optimization
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        low = 0
        high = m
        total_length = m + n
        half_len = (total_length + 1) // 2 # Size of the left partition

        while low <= high:
            partition1 = (low + high) // 2 # Partition index for nums1
            partition2 = half_len - partition1 # Corresponding partition index for nums2

            # Get elements around the partition for nums1
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')

            # Get elements around the partition for nums2
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')

            # Check if the partitions are correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found the correct partition
                if total_length % 2 == 0:
                    # Even total length, median is the average of the two middle elements
                    median = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    # Odd total length, median is the maximum of the left parts
                    median = float(max(maxLeft1, maxLeft2))
                return median
            elif maxLeft1 > minRight2:
                # partition1 is too large, need to move left in nums1
                high = partition1 - 1
            else: # maxLeft2 > minRight1
                # partition1 is too small, need to move right in nums1
                low = partition1 + 1

        # Should not be reached if inputs are valid sorted arrays
        return 0.0 # Or raise an error


    # --- Testing ---
    tests = [
        {"nums1": [1, 3], "nums2": [2], "expected": 2.0},
        {"nums1": [1, 2], "nums2": [3, 4], "expected": 2.5},
        {"nums1": [0, 0], "nums2": [0, 0], "expected": 0.0},
        {"nums1": [], "nums2": [1], "expected": 1.0},
        {"nums1": [2], "nums2": [], "expected": 2.0},
        {"nums1": [1], "nums2": [1], "expected": 1.0},
        {"nums1": [1, 2, 3], "nums2": [4, 5, 6], "expected": 3.5},
        {"nums1": [1, 2, 3, 4], "nums2": [5, 6], "expected": 3.5},
        {"nums1": [4, 5, 6], "nums2": [1, 2, 3], "expected": 3.5},
        {"nums1": [3], "nums2": [-2, -1], "expected": -1.0},
        {"nums1": [1,3,8,9,15], "nums2": [7,11,18,19,21,25], "expected": 11.0},
        {"nums1": [23,26,31,35], "nums2": [3,5,7,9,11,16], "expected": 13.5},
    ]

    correct_count = 0
    for i, test in enumerate(tests):
        nums1 = test["nums1"]
        nums2 = test["nums2"]
        expected = test["expected"]
        result = findMedianSortedArrays(nums1, nums2)
        # Use math.isclose for floating point comparison
        passed = math.isclose(result, expected, rel_tol=1e-5)
        print(f"{passed}")
        if passed:
            correct_count += 1

    print(f"{correct_count}/{len(tests)}")

# Execute the solve function
solve()