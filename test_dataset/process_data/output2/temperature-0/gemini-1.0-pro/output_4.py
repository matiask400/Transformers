import statistics


nums1 = [1,3]
nums2 = [2]
print(statistics.median(nums1 + nums2) == 2.0)

nums1 = [1,2]
nums2 = [3,4]
print(statistics.median(nums1 + nums2) == 2.5)

nums1 = [0,0]
nums2 = [0,0]
print(statistics.median(nums1 + nums2) == 0.0)

nums1 = []
nums2 = [1]
print(statistics.median(nums1 + nums2) == 1.0)

nums1 = [2]
nums2 = []
print(statistics.median(nums1 + nums2) == 2.0)