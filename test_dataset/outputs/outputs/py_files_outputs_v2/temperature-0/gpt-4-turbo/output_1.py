def two_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], index]
        num_map[num] = index

# Test cases
print(two_sum([2,7,11,15], 9) == [0,1])
print(two_sum([3,2,4], 6) == [1,2])
print(two_sum([3,3], 6) == [0,1])