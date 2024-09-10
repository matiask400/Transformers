def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


input_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output_1 = 49
input_2 = [1, 1]
output_2 = 1
input_3 = [4, 3, 2, 1, 4]
output_3 = 16

print(maxArea(input_1) == output_1)
print(maxArea(input_2) == output_2)
print(maxArea(input_3) == output_3)