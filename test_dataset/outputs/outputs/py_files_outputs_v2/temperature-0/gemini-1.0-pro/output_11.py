import unittest

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

class TestMaxArea(unittest.TestCase):

    def test_example_1(self):
        input_1 = [1,8,6,2,5,4,8,3,7]
        output_1 = 49
        self.assertEqual(maxArea(input_1), output_1)

    def test_example_2(self):
        input_2 = [1,1]
        output_2 = 1
        self.assertEqual(maxArea(input_2), output_2)

    def test_example_3(self):
        input_3 = [4,3,2,1,4]
        output_3 = 16
        self.assertEqual(maxArea(input_3), output_3)

if __name__ == '__main__':
    unittest.main()