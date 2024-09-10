def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    return result

# Test cases
print(romanToInt('III') == 3)
print(romanToInt('IV') == 4)
print(romanToInt('IX') == 9)
print(romanToInt('LVIII') == 58)
print(romanToInt('MCMXCIV') == 1994)