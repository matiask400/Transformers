def findMedianSortedArrays(nums1, nums2):
  m, n = len(nums1), len(nums2)
  p1, p2 = 0, 0  # pointers for nums1 and nums2
  merged = []
  while p1 < m and p2 < n:
    if nums1[p1] < nums2[p2]:
      merged.append(nums1[p1])
      p1 += 1
    else:
      merged.append(nums2[p2])
      p2 += 1
  merged.extend(nums1[p1:])  # append the remaining elements of nums1
  merged.extend(nums2[p2:])  # append the remaining elements of nums2
  mid = (len(merged) - 1) // 2
  if len(merged) % 2 == 1:  # odd number of elements
    return merged[mid]
  else:  # even number of elements
    return (merged[mid] + merged[mid + 1]) / 2

# Example 1
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.5

# Example 3
nums1 = [0, 0]
nums2 = [0, 0]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 0.0