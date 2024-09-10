import itertools

def fourSum(nums, target):
    result = []
    nums.sort()
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                total = v + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([v, nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

nums1 = [1,0,-1,0,-2,2]
target1 = 0
nums2 = []
target2 = 0

print(fourSum(nums1, target1) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
print(fourSum(nums2, target2) == [])