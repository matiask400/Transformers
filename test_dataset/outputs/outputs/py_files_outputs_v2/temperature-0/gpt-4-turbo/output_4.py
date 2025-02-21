def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 1:
        return float(nums[n // 2])
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0

# Test cases
print(findMedianSortedArrays([1,3], [2]) == 2.00000)
print(findMedianSortedArrays([1,2], [3,4]) == 2.50000)
print(findMedianSortedArrays([0,0], [0,0]) == 0.00000)