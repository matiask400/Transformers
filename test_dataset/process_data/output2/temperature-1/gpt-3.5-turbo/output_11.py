def max_area(height):
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

# Test Cases
print(max_area([1,8,6,2,5,4,8,3,7]) == 49)
print(max_area([1,1]) == 1)
print(max_area([4,3,2,1,4]) == 16)