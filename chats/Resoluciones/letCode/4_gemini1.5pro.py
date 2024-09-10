class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays in O(log(m+n)) time.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the two sorted arrays.
        """
        m, n = len(nums1), len(nums2)
        # Ensure nums1 is the shorter array for efficiency
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # Boundary checks to determine partition correctness
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # Correct partition found
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    # Odd total length, median is max_left
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                # Even total length, median is average
                return (max_left + min_right) / 2.0