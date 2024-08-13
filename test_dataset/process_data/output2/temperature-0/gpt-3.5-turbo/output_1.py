def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

# Test the solution with example inputs
print(two_sum([2,7,11,15], 9) == [0, 1])
print(two_sum([3,2,4], 6) == [1, 2])
print(two_sum([3,3], 6) == [0, 1])