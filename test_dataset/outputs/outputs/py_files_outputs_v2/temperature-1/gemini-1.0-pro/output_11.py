import unittest

def maxArea(height) -> int:
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


class ExampleTests(unittest.TestCase):

    def test_Example_1(self):
        solution = maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(solution, 49)

    def test_Example_2(self):
        solution = maxArea([1,1])
        self.assertEqual(solution, 1)

    def test_Example_3(self):
        solution = maxArea([4,3,2,1,4])
        self.assertEqual(solution, 16)

    def test_Example_4(self):
        solution = maxArea([1,2,1])
        self.assertEqual(solution, 2)

unittest.main()