import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // values[i]):
                roman_num += roman_values[i]
                num -= values[i]
            i += 1
        return roman_num

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().intToRoman(3), 'III')

    def test_2(self):
        self.assertEqual(Solution().intToRoman(4), 'IV')

    def test_3(self):
        self.assertEqual(Solution().intToRoman(9), 'IX')

    def test_4(self):
        self.assertEqual(Solution().intToRoman(58), 'LVIII')

    def test_5(self):
        self.assertEqual(Solution().intToRoman(1994), 'MCMXCIV')

if __name__ == '__main__':
    unittest.main()