import statistics


nums1 = [1,3]
nums2 = [2]
print(statistics.median(nums1 + nums2) == 2.00000)

nums1 = [1,2]
nums2 = [3,4]
print(statistics.median(nums1 + nums2) == 2.50000)

nums1 = [0,0]
nums2 = [0,0]
print(statistics.median(nums1 + nums2) == 0.00000)

nums1 = []
nums2 = [1]
print(statistics.median(nums1 + nums2) == 1.00000)

nums1 = [2]
nums2 = []
print(statistics.median(nums1 + nums2) == 2.00000)