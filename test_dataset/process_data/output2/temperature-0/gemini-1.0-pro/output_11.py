import unittest

class Solution:
    def maxArea(self, height: list[int]) -> int:
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


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_2(self):
        self.assertEqual(Solution().maxArea([1,1]), 1)

    def test_3(self):
        self.assertEqual(Solution().maxArea([4,3,2,1,4]), 16)

    def test_4(self):
        self.assertEqual(Solution().maxArea([1,2,1]), 2)

if __name__ == '__main__':
    unittest.main()