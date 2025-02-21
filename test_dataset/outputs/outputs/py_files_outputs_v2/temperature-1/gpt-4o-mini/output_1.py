def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

# Test examples
inputs = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6)
]
outputs = [
    [0, 1],
    [1, 2],
    [0, 1]
]

for i in range(len(inputs)):
    result = two_sum(*inputs[i])
    print(result == outputs[i])