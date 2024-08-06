import unittest

def two_sum(nums, target):
    num_to_index = {}  # map number to its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

class TwoSumTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()