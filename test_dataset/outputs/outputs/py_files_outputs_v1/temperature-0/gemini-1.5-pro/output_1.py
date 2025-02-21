def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


# Test cases
inputs = [([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6)]
outputs = [[0,1], [1,2], [0,1]]

for i in range(len(inputs)):
    solution = two_sum(inputs[i][0], inputs[i][1])
    print(solution == outputs[i])