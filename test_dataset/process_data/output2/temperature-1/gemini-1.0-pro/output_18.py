import itertools
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            if not nums:
                return res
            
            average_value = target // k

            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]

                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo -1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) -1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)

# Example 1: 
input1 = [1,0,-1,0,-2,2]
target1 = 0
output1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum(input1, target1) == output1)

# Example 2: 
input2 = []
target2 = 0
output2 = []
print(Solution().fourSum(input2, target2) == output2)