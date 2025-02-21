def roman_to_int(s: str) -> int:
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
    prev_value = 0
    for char in s[::-1]:
        value = roman_numerals[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result


input_1 = "III"
output_1 = roman_to_int(input_1)
print(output_1 == 3)

input_2 = "LVIII"
output_2 = roman_to_int(input_2)
print(output_2 == 58)

input_3 = "MCMXCIV"
output_3 = roman_to_int(input_3)
print(output_3 == 1994)