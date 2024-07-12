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
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

# Test cases
nums1 = [-1,0,1,2,-1,-4]
output1 = threeSum(nums1)
print(f"Input 1: {nums1}")
print(f"Output 1: {output1}")

nums2 = []
output2 = threeSum(nums2)
print(f"Input 2: {nums2}")
print(f"Output 2: {output2}")

nums3 = [0]
output3 = threeSum(nums3)
print(f"Input 3: {nums3}")
print(f"Output 3: {output3}")

# Check if the outputs match the expected outputs
print(f"Output 1 matches expected output: {output1 == [[-1,-1,2],[-1,0,1]]}")
print(f"Output 2 matches expected output: {output2 == []}")
print(f"Output 3 matches expected output: {output3 == []}")