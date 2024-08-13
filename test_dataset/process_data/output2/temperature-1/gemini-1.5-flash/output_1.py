def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Example 1
nums = [2, 7, 11, 15]
target = 9
output_1 = twoSum(nums, target)
print(output_1 == [0, 1])  # Output: True

# Example 2
nums = [3, 2, 4]
target = 6
output_2 = twoSum(nums, target)
print(output_2 == [1, 2])  # Output: True

# Example 3
nums = [3, 3]
target = 6
output_3 = twoSum(nums, target)
print(output_3 == [0, 1])  # Output: True