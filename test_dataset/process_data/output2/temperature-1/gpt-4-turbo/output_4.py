def findMedianSortedArrays(nums1, nums2):
    n = nums1 + nums2
    n.sort()
    l = len(n)
    if l % 2 == 1:
        return float(n[l // 2])
    else:
        return float((n[l // 2 - 1] + n[l // 2]) / 2)

# Test Cases
inputs = [([1,3], [2]), ([1,2], [3,4]), ([0,0], [0,0])]
outputs = [2.00000, 2.50000, 0.00000]
results = []

for i, (nums1, nums2) in enumerate(inputs):
    result = findMedianSortedArrays(nums1, nums2)
    results.append(result == outputs[i])

print(results)