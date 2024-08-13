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

s = Solution()

# Example 1
input_1 = "III"
output_1 = s.romanToInt(input_1)
print(output_1 == 3)  # True

# Example 2
input_2 = "IV"
output_2 = s.romanToInt(input_2)
print(output_2 == 4)  # True

# Example 3
input_3 = "IX"
output_3 = s.romanToInt(input_3)
print(output_3 == 9)  # True