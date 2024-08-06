def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        current_area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, current_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


# Test cases
input_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output_1 = 49
input_2 = [1, 1]
output_2 = 1
input_3 = [4, 3, 2, 1, 4]
output_3 = 16

print(True if maxArea(input_1) == output_1 else False)
print(True if maxArea(input_2) == output_2 else False)
print(True if maxArea(input_3) == output_3 else False)