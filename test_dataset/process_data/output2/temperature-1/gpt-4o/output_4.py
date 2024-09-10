def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    l = len(nums)
    if l % 2 == 0:
        return (nums[l//2 - 1] + nums[l//2]) / 2
    else:
        return nums[l//2]

# Test inputs and outputs
input_1 = ([1, 3], [2])
output_1 = 2.00000
print(findMedianSortedArrays(*input_1) == output_1)

input_2 = ([1, 2], [3, 4])
output_2 = 2.50000
print(findMedianSortedArrays(*input_2) == output_2)

input_3 = ([0, 0], [0, 0])
output_3 = 0.00000
print(findMedianSortedArrays(*input_3) == output_3)