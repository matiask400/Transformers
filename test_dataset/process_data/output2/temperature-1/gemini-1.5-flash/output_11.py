import unittest

def maxArea(height):
    left, right = 0, len(height) - 1
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
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(maxArea(height), 49)

    def test_example2(self):
        height = [1, 1]
        self.assertEqual(maxArea(height), 1)

    def test_example3(self):
        height = [4, 3, 2, 1, 4]
        self.assertEqual(maxArea(height), 16)

    def test_example4(self):
        height = [1, 2, 1]
        self.assertEqual(maxArea(height), 2)


if __name__ == '__main__':
    unittest.main()