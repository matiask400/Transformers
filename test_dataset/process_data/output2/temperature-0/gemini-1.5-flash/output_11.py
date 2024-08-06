import unittest

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

class TestMaxArea(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)
    def test_example_2(self):
        self.assertEqual(maxArea([1,1]), 1)
    def test_example_3(self):
        self.assertEqual(maxArea([4,3,2,1,4]), 16)
    def test_example_4(self):
        self.assertEqual(maxArea([1,2,1]), 2)

if __name__ == '__main__':
    unittest.main()