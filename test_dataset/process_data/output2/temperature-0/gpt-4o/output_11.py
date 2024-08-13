def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example inputs and expected outputs
inputs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1],
    [4, 3, 2, 1, 4],
    [1, 2, 1]
]
expected_outputs = [49, 1, 16, 2]

# Verify the solution
for i, input_data in enumerate(inputs):
    result = max_area(input_data)
    print(result == expected_outputs[i])