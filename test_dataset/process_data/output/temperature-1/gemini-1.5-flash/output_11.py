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

# Test cases
input_1 = [1,8,6,2,5,4,8,3,7]
output_1 = 49
input_2 = [1,1]
output_2 = 1
input_3 = [4,3,2,1,4]
output_3 = 16

# Check if the solution is correct
print(f"Input 1: {input_1}, Output 1: {maxArea(input_1)}, Expected Output 1: {output_1}, Result: {maxArea(input_1) == output_1}")
print(f"Input 2: {input_2}, Output 2: {maxArea(input_2)}, Expected Output 2: {output_2}, Result: {maxArea(input_2) == output_2}")
print(f"Input 3: {input_3}, Output 3: {maxArea(input_3)}, Expected Output 3: {output_3}, Result: {maxArea(input_3) == output_3}")