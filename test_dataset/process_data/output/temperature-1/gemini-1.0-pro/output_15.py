def threeSum(nums):
        
    result = []
    nums.sort()
    
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = v + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                result.append([v, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result