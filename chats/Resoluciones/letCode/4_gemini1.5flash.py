class Solution:
    def findMedianSortedArrays(self, nums1 = [1,3], nums2 = [2]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)  # Ensure nums1 is the shorter array

        low, high = 0, m  # Binary search on nums1
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = ((m + n + 1) // 2) - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:  # Even total length
                    print(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                    return
                else:  # Odd total length
                    print(max(maxLeftX, maxLeftY))
                    return
            elif maxLeftX > minRightY:
                high = partitionX - 1
                print(high)
            else:
                low = partitionX + 1
                print(low)
