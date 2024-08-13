def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Example 1
nums = [2,7,11,15]
target = 9
output = twoSum(nums, target)
expected_output = [0,1]
print(output == expected_output)

# Example 2
nums = [3,2,4]
target = 6
output = twoSum(nums, target)
expected_output = [1,2]
print(output == expected_output)

# Example 3
nums = [3,3]
target = 6
output = twoSum(nums, target)
expected_output = [0,1]
print(output == expected_output)