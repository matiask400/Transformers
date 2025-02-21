def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums)-2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            current_sum = nums[i] + nums[start] + nums[end]
            if current_sum == target:
                return target
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                start += 1
            else:
                end -= 1
    return closest_sum

# Test the solution with example inputs
print(threeSumClosest([-1, 2, 1, -4], 1) == 2)
print(threeSumClosest([1, 2, 3, 4, 5], 100) == 12)
print(threeSumClosest([0, 0, 0], 1) == 0)