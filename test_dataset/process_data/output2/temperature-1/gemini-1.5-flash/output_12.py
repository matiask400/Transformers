import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
        i = 12
        result = ''
        while num > 0:
            if list(roman_map.keys())[i] <= num:
                result += list(roman_map.values())[i]
                num -= list(roman_map.keys())[i]
            else:
                i -= 1
        return result

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        num = 3
        expected_output = "III"
        self.assertEqual(Solution().intToRoman(num), expected_output)
    def test_case_2(self):
        num = 4
        expected_output = "IV"
        self.assertEqual(Solution().intToRoman(num), expected_output)
    def test_case_3(self):
        num = 9
        expected_output = "IX"
        self.assertEqual(Solution().intToRoman(num), expected_output)
    def test_case_4(self):
        num = 58
        expected_output = "LVIII"
        self.assertEqual(Solution().intToRoman(num), expected_output)
    def test_case_5(self):
        num = 1994
        expected_output = "MCMXCIV"
        self.assertEqual(Solution().intToRoman(num), expected_output)


if __name__ == '__main__':
    unittest.main()