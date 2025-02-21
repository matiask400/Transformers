import unittest

def two_sum(nums:list, target:int)->list:
    result = []
    already_seen = dict()
    for index, item in enumerate(nums):
        difference = target - item
        if difference in already_seen:
            result.append(already_seen[difference])
            result.append(index)
            return result
        already_seen[item] = index
    return result

class TwoSumTests(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_another_simple_case(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_corner_case(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()