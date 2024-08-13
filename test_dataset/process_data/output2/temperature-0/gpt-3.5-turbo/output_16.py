def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum

# Test the solution with example inputs
print(threeSumClosest([-1, 2, 1, -4], 1) == 2)
print(threeSumClosest([1, 1, 1, 0], -100) == 2)
print(threeSumClosest([0, 0, 0], 1) == 0)