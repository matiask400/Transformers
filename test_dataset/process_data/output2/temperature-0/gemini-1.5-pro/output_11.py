def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

input_1 = [1,8,6,2,5,4,8,3,7]
output_1 = 49
input_2 = [1,1]
output_2 = 1
input_3 = [4,3,2,1,4]
output_3 = 16

print(f"Input 1: {input_1}, Output: {output_1}, Result: {maxArea(input_1) == output_1}")
print(f"Input 2: {input_2}, Output: {output_2}, Result: {maxArea(input_2) == output_2}")
print(f"Input 3: {input_3}, Output: {output_3}, Result: {maxArea(input_3) == output_3}")