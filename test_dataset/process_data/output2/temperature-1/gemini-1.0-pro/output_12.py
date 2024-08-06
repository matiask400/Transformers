import math

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_number = ''

        for i in range(len(values)):
            while num >= values[i]:
                roman_number += roman_values[i]
                num -= values[i]

        return roman_number


input_1 = 3
output_1 = 'III'
input_2 = 4
output_2 = 'IV'
input_3 = 9
output_3 = 'IX'

solution = Solution()
print(solution.intToRoman(input_1) == output_1)
print(solution.intToRoman(input_2) == output_2)
print(solution.intToRoman(input_3) == output_3)