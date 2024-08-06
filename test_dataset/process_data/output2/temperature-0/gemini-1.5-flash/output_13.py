import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s):
            current_symbol = s[i]
            next_symbol = s[i + 1] if i + 1 < len(s) else None
            if next_symbol and roman_map[current_symbol] < roman_map[next_symbol]:
                result += roman_map[next_symbol] - roman_map[current_symbol]
                i += 2
            else:
                result += roman_map[current_symbol]
                i += 1
        return result

class TestRomanToInt(unittest.TestCase):
    def test_example_1(self):
        s = "III"
        expected_output = 3
        solution = Solution()
        self.assertEqual(solution.romanToInt(s), expected_output)
        print(f"Example 1: {solution.romanToInt(s) == expected_output}")

    def test_example_2(self):
        s = "IV"
        expected_output = 4
        solution = Solution()
        self.assertEqual(solution.romanToInt(s), expected_output)
        print(f"Example 2: {solution.romanToInt(s) == expected_output}")

    def test_example_3(self):
        s = "IX"
        expected_output = 9
        solution = Solution()
        self.assertEqual(solution.romanToInt(s), expected_output)
        print(f"Example 3: {solution.romanToInt(s) == expected_output}")

    def test_example_4(self):
        s = "LVIII"
        expected_output = 58
        solution = Solution()
        self.assertEqual(solution.romanToInt(s), expected_output)
        print(f"Example 4: {solution.romanToInt(s) == expected_output}")

    def test_example_5(self):
        s = "MCMXCIV"
        expected_output = 1994
        solution = Solution()
        self.assertEqual(solution.romanToInt(s), expected_output)
        print(f"Example 5: {solution.romanToInt(s) == expected_output}")

if __name__ == '__main__':
    unittest.main()