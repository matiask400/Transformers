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
    def test_1(self):
        self.assertEqual(Solution().intToRoman(3), "III")
    def test_2(self):
        self.assertEqual(Solution().intToRoman(4), "IV")
    def test_3(self):
        self.assertEqual(Solution().intToRoman(9), "IX")
    def test_4(self):
        self.assertEqual(Solution().intToRoman(58), "LVIII")
    def test_5(self):
        self.assertEqual(Solution().intToRoman(1994), "MCMXCIV")

if __name__ == '__main__':
    unittest.main()