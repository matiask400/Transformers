def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

input_1 = ([1, 3], [2])
output_1 = findMedianSortedArrays(*input_1)
print(output_1 == 2.00000)  # True

input_2 = ([1, 2], [3, 4])
output_2 = findMedianSortedArrays(*input_2)
print(output_2 == 2.50000)  # True

input_3 = ([0, 0], [0, 0])
output_3 = findMedianSortedArrays(*input_3)
print(output_3 == 0.00000)  # True