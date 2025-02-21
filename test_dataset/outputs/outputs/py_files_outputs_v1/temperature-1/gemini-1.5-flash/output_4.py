import math

def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    
    low, high = 0, m
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = ((m + n + 1) // 2) - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return -1

# Example usage

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.00000

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.50000

nums1 = [0, 0]
nums2 = [0, 0]
print(findMedianSortedArrays(nums1, nums2)) # Output: 0.00000

nums1 = []
nums2 = [1]
print(findMedianSortedArrays(nums1, nums2)) # Output: 1.00000

nums1 = [2]
nums2 = []
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.00000