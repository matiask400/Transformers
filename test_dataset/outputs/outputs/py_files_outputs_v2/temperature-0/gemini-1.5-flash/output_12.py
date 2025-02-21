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

# Test cases

solution = Solution()

# Example 1
input_1 = 3
output_1 = solution.intToRoman(input_1)
print(output_1 == "III")

# Example 2
input_2 = 4
output_2 = solution.intToRoman(input_2)
print(output_2 == "IV")

# Example 3
input_3 = 9
output_3 = solution.intToRoman(input_3)
print(output_3 == "IX")