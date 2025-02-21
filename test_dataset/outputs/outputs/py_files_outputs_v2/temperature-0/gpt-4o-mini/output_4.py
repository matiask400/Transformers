def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]

# Example inputs
inputs = [
    ([1, 3], [2]),
    ([1, 2], [3, 4]),
    ([0, 0], [0, 0])
]
# Expected outputs
outputs = [2.00000, 2.50000, 0.00000]

# Testing the function
for (nums1, nums2), expected in zip(inputs, outputs):
    result = findMedianSortedArrays(nums1, nums2)
    print(result == expected)
