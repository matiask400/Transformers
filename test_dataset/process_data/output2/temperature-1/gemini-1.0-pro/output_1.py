from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hashtable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable:
            return [hashtable[complement], i]
        hashtable[nums[i]] = i

# Example 1: Input: nums = [2,7,11,15], target = 9
input1 = [2,7,11,15]
target1 = 9
output1 = two_sum(input1, target1)
print(output1 == [0,1])

# Example 2: Input: nums = [3,2,4], target = 6
input2 = [3,2,4]
target2 = 6
output2 = two_sum(input2, target2)
print(output2 == [1,2])

# Example 3: Input: nums = [3,3], target = 6
input3 = [3,3]
target3 =6
output3 = two_sum(input3, target3)
print(output3 == [0,1])