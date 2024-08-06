import random

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example 1:
input_1 = [1,8,6,2,5,4,8,3,7]
output_1 = maxArea(input_1)
asserted_1 = output_1 == 49
print(asserted_1)

# Example 2:
input_2 = [1,1]
output_2 = maxArea(input_2)
asserted_2 = output_2 == 1
print(asserted_2)

# Example 3:
input_3 = [4,3,2,1,4]
output_3 = maxArea(input_3)
asserted_3 = output_3 == 16
print(asserted_3)

# Example 4:
input_4 = [1,2,1]
output_4 = maxArea(input_4)
asserted_4 = output_4 == 2
print(asserted_4)