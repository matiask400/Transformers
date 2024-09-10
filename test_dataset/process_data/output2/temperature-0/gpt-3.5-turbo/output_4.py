def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]

# Test cases
print(findMedianSortedArrays([1,3], [2]) == 2.0)
print(findMedianSortedArrays([1,2], [3,4]) == 2.5)
print(findMedianSortedArrays([0,0], [0,0]) == 0.0)