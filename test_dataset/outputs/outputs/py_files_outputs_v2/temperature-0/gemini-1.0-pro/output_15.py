import unittest

def threeSum(nums):
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
        input_1 = [-1,0,1,2,-1,-4]
        output_1 = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(threeSum(input_1), output_1)

    def test_example_2(self):
        input_2 = []
        output_2 = []
        self.assertEqual(threeSum(input_2), output_2)

    def test_example_3(self):
        input_3 = [0]
        output_3 = []
        self.assertEqual(threeSum(input_3), output_3)

if __name__ == '__main__':
    unittest.main()