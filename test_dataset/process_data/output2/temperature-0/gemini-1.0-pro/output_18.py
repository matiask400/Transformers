import itertools

def fourSum(nums, target):
    result = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        for j, b in enumerate(nums[i + 1:]):
            if j > 0 and b == nums[i + j]:
                continue
            left, right = i + j + 2, len(nums) - 1
            while left < right:
                c, d = nums[left], nums[right]
                total = a + b + c + d
                if total == target:
                    result.append([a, b, c, d])
                    while left < right and c == nums[left]:
                        left += 1
                    while left < right and d == nums[right]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

nums1 = [1,0,-1,0,-2,2]
target1 = 0
output1 = fourSum(nums1, target1)
print(output1 == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

nums2 = []
target2 = 0
output2 = fourSum(nums2, target2)
print(output2 == [])