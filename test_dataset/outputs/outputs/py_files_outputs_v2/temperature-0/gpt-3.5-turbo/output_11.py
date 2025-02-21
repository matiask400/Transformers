def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Test the solution with example inputs
print(maxArea([1,8,6,2,5,4,8,3,7]) == 49)
print(maxArea([1,1]) == 1)
print(maxArea([4,3,2,1,4]) == 16)
print(maxArea([1,2,1]) == 2)