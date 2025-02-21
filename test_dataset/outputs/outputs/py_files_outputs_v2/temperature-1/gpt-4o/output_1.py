def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

# Test cases
inputs = [
    {'nums': [2, 7, 11, 15], 'target': 9},
    {'nums': [3, 2, 4], 'target': 6},
    {'nums': [3, 3], 'target': 6}
]

expected_outputs = [
    [0, 1],
    [1, 2],
    [0, 1]
]

for i, input_data in enumerate(inputs):
    result = two_sum(input_data['nums'], input_data['target'])
    print(result == expected_outputs[i])