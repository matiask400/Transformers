def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example 1
height_1 = [1,8,6,2,5,4,8,3,7]
output_1 = maxArea(height_1)
print(output_1 == 49)  # True

# Example 2
height_2 = [1,1]
output_2 = maxArea(height_2)
print(output_2 == 1)  # True

# Example 3
height_3 = [4,3,2,1,4]
output_3 = maxArea(height_3)
print(output_3 == 16)  # True

# Example 4
height_4 = [1,2,1]
output_4 = maxArea(height_4)
print(output_4 == 2)  # True