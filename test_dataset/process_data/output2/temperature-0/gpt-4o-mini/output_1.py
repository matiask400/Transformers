def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

# Example inputs
inputs = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6)
]
outputs = [
    [0, 1],
    [1, 2],
    [0, 1]
]

for i, (input_data, expected_output) in enumerate(zip(inputs, outputs)):
    result = two_sum(*input_data)
    print(f'Input {i + 1}: {input_data}, Output: {result}, Correct: {result == expected_output}')