from typing import List
def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
output1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(f"Input 1: {nums1} Target: {target1} - Output: {four_sum(nums1, target1) == output1}")

nums2 = []
target2 = 0
output2 = []
print(f"Input 2: {nums2} Target: {target2} - Output: {four_sum(nums2, target2) == output2}")