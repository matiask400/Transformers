def threeSum(nums):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]: