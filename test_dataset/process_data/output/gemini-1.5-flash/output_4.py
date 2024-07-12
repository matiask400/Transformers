import math

def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    
    low = 0
    high = m
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = ((m + n + 1) // 2) - partitionX
        
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return -1

# Test cases
nums1_1 = [1, 3]
nums2_1 = [2]
output_1 = findMedianSortedArrays(nums1_1, nums2_1)
print(f"Input 1: nums1 = {nums1_1}, nums2 = {nums2_1}")
print(f"Output 1: {output_1}")

nums1_2 = [1, 2]
nums2_2 = [3, 4]
output_2 = findMedianSortedArrays(nums1_2, nums2_2)
print(f"Input 2: nums1 = {nums1_2}, nums2 = {nums2_2}")
print(f"Output 2: {output_2}")

nums1_3 = [0, 0]
nums2_3 = [0, 0]
output_3 = findMedianSortedArrays(nums1_3, nums2_3)
print(f"Input 3: nums1 = {nums1_3}, nums2 = {nums2_3}")
print(f"Output 3: {output_3}")