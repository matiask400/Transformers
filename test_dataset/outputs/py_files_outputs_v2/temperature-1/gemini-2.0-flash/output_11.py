def maxArea(height):
    """
    Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`.
    `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`.
    Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
    """
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = width * min_height
        max_area = max(max_area, area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area