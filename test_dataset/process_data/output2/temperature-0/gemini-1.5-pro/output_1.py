def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


input_1 = [2,7,11,15]
target_1 = 9
output_1 = [0,1]
print(two_sum(input_1, target_1) == output_1)

input_2 = [3,2,4]
target_2 = 6
output_2 = [1,2]
print(two_sum(input_2, target_2) == output_2)

input_3 = [3,3]
target_3 = 6
output_3 = [0,1]
print(two_sum(input_3, target_3) == output_3)