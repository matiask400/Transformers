import unittest

def three_sum(nums):
    result = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = a + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result

class TestThreeSum(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    def test_example_2(self):
        self.assertEqual(three_sum([]), [])

    def test_example_3(self):
        self.assertEqual(three_sum([0]), [])

if __name__ == '__main__':
    unittest.main()