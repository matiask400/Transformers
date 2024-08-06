import math

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = math.inf
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum

# Example 1: Input and Output
nums1 = [-1,2,1,-4]
target1 = 1
output1 = threeSumClosest(nums1, target1)
print(output1 == 2)

# Example 2: Input and Output
nums2 = [0,0,0]
target2 = 1
output2 = threeSumClosest(nums2, target2)
print(output2 == 0)

# Example 3: Input and Output
nums3 = [1,1,-1,-1,3]
target3 = -1
output3 = threeSumClosest(nums3, target3)
print(output3 == -1)