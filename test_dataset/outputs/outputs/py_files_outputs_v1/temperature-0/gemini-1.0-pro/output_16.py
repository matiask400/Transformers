def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                l += 1
            else:
                r -= 1
    return closest_sum