def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        if height[left] < height[right]:
            max_water = max(max_water, height[left] * width)
            left += 1
        else:
            max_water = max(max_water, height[right] * width)
            right -= 1
    return max_water

# Test cases
print(max_area([1,8,6,2,5,4,8,3,7]) == 49)
print(max_area([1,1]) == 1)
print(max_area([4,3,2,1,4]) == 16)