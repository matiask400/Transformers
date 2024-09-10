def max_area(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        max_area = max(max_area, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

# Test cases
height1 = [1,8,6,2,5,4,8,3,7]
expected1 = 49
result1 = max_area(height1) == expected1

height2 = [1,1]
expected2 = 1
result2 = max_area(height2) == expected2

height3 = [4,3,2,1,4]
expected3 = 16
result3 = max_area(height3) == expected3

print('Input 1 is correct:', result1)
print('Input 2 is correct:', result2)
print('Input 3 is correct:', result3)