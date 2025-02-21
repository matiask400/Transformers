import sys

def threeSumClosest(nums, target):
    nums.sort()
    closestSum = sys.maxsize
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum
            if currentSum < target:
                left += 1
            else:
                right -= 1
    return closestSum

# Example 1
nums1 = [-1, 2, 1, -4]
 target1 = 1
 output1 = threeSumClosest(nums1, target1)
 print(output1 == 2) # True

# Example 2
# ... (Add more examples here if needed)