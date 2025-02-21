import sys

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = sys.maxsize
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum

# Example 1
nums1 = [-1, 2, 1, -4]
target1 = 1
output1 = threeSumClosest(nums1, target1)
print(output1 == 2)  # True

# Example 2
# (No second example provided)

# Example 3
# (No third example provided)