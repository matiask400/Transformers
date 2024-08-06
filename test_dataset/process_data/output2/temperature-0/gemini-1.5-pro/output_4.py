class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums1[i] < nums2[j-1]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

test_cases = [
    (([1, 3], [2]), 2.00000),
    (([1, 2], [3, 4]), 2.50000),
    (([0, 0], [0, 0]), 0.00000),
    (([], [1]), 1.00000),
    (([2], []), 2.00000),
]

s = Solution()
for i, (input_args, expected_output) in enumerate(test_cases):
    result = s.findMedianSortedArrays(*input_args)
    print(f"Test Case {i+1}: {'True' if result == expected_output else 'False'}")