def twoSum(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable:
            return [hashtable[complement], i]
        hashtable[nums[i]] = i
    return None

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums = [3,3]
target = 6