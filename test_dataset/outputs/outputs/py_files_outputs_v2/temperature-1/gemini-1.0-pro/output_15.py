import unittest

def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result


class SolutionTest(unittest.TestCase):
    def test_cases(self):
        test_cases = [
            ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
            ([], []),
            ([0], [])
        ]
        for input, output in test_cases:
            assert three_sum(input) == output, False

if __name__ == '__main__':
    unittest.main()