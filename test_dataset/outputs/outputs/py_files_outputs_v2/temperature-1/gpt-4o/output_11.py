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

# Test cases
input_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output_1 = 49
input_2 = [1, 1]
output_2 = 1
input_3 = [4, 3, 2, 1, 4]
output_3 = 16

print(max_area(input_1) == output_1)  # Should print True
print(max_area(input_2) == output_2)  # Should print True
print(max_area(input_3) == output_3)  # Should print True
