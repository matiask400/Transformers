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


assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([1,1]) == 1
assert maxArea([4,3,2,1,4]) == 16
assert maxArea([1,2,1]) == 2