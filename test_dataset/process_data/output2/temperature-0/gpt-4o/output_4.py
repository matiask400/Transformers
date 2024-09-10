def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

# Example 1
nums1 = [1, 3]
nums2 = [2]
expected_output = 2.00000
print(findMedianSortedArrays(nums1, nums2) == expected_output)

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
expected_output = 2.50000
print(findMedianSortedArrays(nums1, nums2) == expected_output)

# Example 3
nums1 = [0, 0]
nums2 = [0, 0]
expected_output = 0.00000
print(findMedianSortedArrays(nums1, nums2) == expected_output)

# Example 4
nums1 = []
nums2 = [1]
expected_output = 1.00000
print(findMedianSortedArrays(nums1, nums2) == expected_output)

# Example 5
nums1 = [2]
nums2 = []
expected_output = 2.00000
print(findMedianSortedArrays(nums1, nums2) == expected_output)