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
nums = [-1, 2, 1, -4]
target = 1
output_1 = threeSumClosest(nums, target)
print(f"Input 1: nums = {nums}, target = {target}")
print(f"Output 1: {output_1}")

# Example 2
nums = [0, 0, 0]
target = 1
output_2 = threeSumClosest(nums, target)
print(f"Input 2: nums = {nums}, target = {target}")
print(f"Output 2: {output_2}")

# Example 3
nums = [1, 1, 1, 0]
target = -100
output_3 = threeSumClosest(nums, target)
print(f"Input 3: nums = {nums}, target = {target}")
print(f"Output 3: {output_3}")