def twoSum(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable:
            return [hashtable[complement], i]
        hashtable[nums[i]] = i
    return None

nums1 = [2,7,11,15]
target1 = 9
result1 = twoSum(nums1, target1)
print(result1)

nums2 = [3,2,4]
target2 = 6
result2 = twoSum(nums2, target2)
print(result2)

nums3 = [3,3]
target3 = 6
result3 = twoSum(nums3, target3)
print(result3)