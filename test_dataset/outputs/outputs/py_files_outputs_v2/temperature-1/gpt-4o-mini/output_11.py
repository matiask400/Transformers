def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        max_area = max(max_area, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example inputs
input_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output_1 = maxArea(input_1)
print(output_1 == 49)  # True

input_2 = [1, 1]
output_2 = maxArea(input_2)
print(output_2 == 1)  # True

input_3 = [4, 3, 2, 1, 4]
output_3 = maxArea(input_3)
print(output_3 == 16)  # True