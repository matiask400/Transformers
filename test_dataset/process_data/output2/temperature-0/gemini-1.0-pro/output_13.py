import unittest

class RomanNumerals:
    def roman_to_int(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
                result += roman_numerals[s[i]] - 2 * roman_numerals[s[i - 1]]
            else:
                result += roman_numerals[s[i]]
        return result

class TestRomanNumerals(unittest.TestCase):
    def test_roman_to_int(self):
        roman_numerals = RomanNumerals()
        self.assertEqual(roman_numerals.roman_to_int('III'), 3)
        self.assertEqual(roman_numerals.roman_to_int('IV'), 4)
        self.assertEqual(roman_numerals.roman_to_int('IX'), 9)
        self.assertEqual(roman_numerals.roman_to_int('LVIII'), 58)
        self.assertEqual(roman_numerals.roman_to_int('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()