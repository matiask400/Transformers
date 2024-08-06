import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        result = ''
        for value, symbol in roman_map.items():
            while num >= value:
                result += symbol
                num -= value
        return result

class TestRomanToInt(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(3), "III")

    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(4), "IV")

    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(9), "IX")

    def test_example_4(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(58), "LVIII")

    def test_example_5(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(1994), "MCMXCIV")


if __name__ == '__main__':
    unittest.main()