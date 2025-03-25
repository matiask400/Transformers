def maxArea(height):
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        current_height = min(height[left], height[right])
        max_area = max(max_area, (right - left) * current_height)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area