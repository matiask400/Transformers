import itertools

def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return result

# Example 1
nums1 = [-1,0,1,2,-1,-4]
output1 = threeSum(nums1)
print(f'Input 1: {nums1}')
print(f'Output 1: {output1}')
print(f'Test 1: {output1 == [[-1,-1,2],[-1,0,1]]}')

# Example 2
nums2 = []
output2 = threeSum(nums2)
print(f'Input 2: {nums2}')
print(f'Output 2: {output2}')
print(f'Test 2: {output2 == []}')

# Example 3
nums3 = [0]
output3 = threeSum(nums3)
print(f'Input 3: {nums3}')
print(f'Output 3: {output3}')
print(f'Test 3: {output3 == []}')