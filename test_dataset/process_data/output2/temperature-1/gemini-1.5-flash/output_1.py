import unittest

def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(two_sum(nums, target), expected_output)
        print(True)

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(two_sum(nums, target), expected_output)
        print(True)

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(two_sum(nums, target), expected_output)
        print(True)

if __name__ == '__main__':
    unittest.main()