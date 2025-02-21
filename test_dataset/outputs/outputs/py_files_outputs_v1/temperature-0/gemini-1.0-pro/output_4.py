def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    p1, p2 = 0, 0
    merged = []
    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            merged.append(nums1[p1])
            p1 += 1
        else:
            merged.append(nums2[p2])
            p2 += 1
    while p1 < m:
        merged.append(nums1[p1])
        p1 += 1
    while p2 < n:
        merged.append(nums2[p2])
        p2 += 1
    l = len(merged)
    if l % 2 == 0:
        return (merged[l // 2 - 1] + merged[l // 2]) / 2
    else:
        return merged[l // 2]

# Example 1
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
result = findMedianSortedArrays(nums1, nums2)
print(result)

# Example 3
nums1 = [0, 0]
nums2 = [0, 0]
result = findMedianSortedArrays(nums1, nums2)
print(result)

# Example 4
nums1 = []
nums2 = [1]
result = findMedianSortedArrays(nums1, nums2)
print(result)

# Example 5
nums1 = [2]
nums2 = []
result = findMedianSortedArrays(nums1, nums2)
print(result)