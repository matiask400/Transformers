import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                result += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                result += roman[s[i]]
        return result

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Solution().romanToInt("III"), 3)
        self.assertEqual(Solution().romanToInt("IV"), 4)
        self.assertEqual(Solution().romanToInt("IX"), 9)
        self.assertEqual(Solution().romanToInt("LVIII"), 58)
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)

if __name__ == "__main":
    unittest.main()