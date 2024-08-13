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
print(f"Input 1: {input_1}, Output 1: {output_1}, Expected Output 1: 3, Result: {output_1 == 3}")

# Example 2
input_2 = "IV"
output_2 = s.romanToInt(input_2)
print(f"Input 2: {input_2}, Output 2: {output_2}, Expected Output 2: 4, Result: {output_2 == 4}")

# Example 3
input_3 = "IX"
output_3 = s.romanToInt(input_3)
print(f"Input 3: {input_3}, Output 3: {output_3}, Expected Output 3: 9, Result: {output_3 == 9}")