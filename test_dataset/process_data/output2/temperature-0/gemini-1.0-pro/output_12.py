import math


def int_to_roman(num):
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


# Example 1: Input: num = 3, Output: "III"
print(int_to_roman(3) == "III")  # True

# Example 2: Input: num = 4, Output: "IV"
print(int_to_roman(4) == "IV")  # True

# Example 3: Input: num = 9, Output: "IX"
print(int_to_roman(9) == "IX")  # True

# Example 4: Input: num = 58, Output: "LVIII"
print(int_to_roman(58) == "LVIII")  # True

# Example 5: Input: num = 1994, Output: "MCMXCIV"
print(int_to_roman(1994) == "MCMXCIV")  # True