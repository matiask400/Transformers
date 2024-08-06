import itertools

def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return result

# Example 1
nums1 = [-1,0,1,2,-1,-4]
output1 = threeSum(nums1)
print(output1 == [[-1,-1,2],[-1,0,1]])

# Example 2
nums2 = []
output2 = threeSum(nums2)
print(output2 == [])

# Example 3
nums3 = [0]
output3 = threeSum(nums3)
print(output3 == [])