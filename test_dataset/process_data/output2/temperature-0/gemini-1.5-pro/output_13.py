def roman_to_integer(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    num = 0
    i = 0
    while i < n:
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
            num += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            num += roman_map[s[i]]
            i += 1
    return num


input_1 = "III"
output_1 = 3
print(f"Input 1: {roman_to_integer(input_1) == output_1}")

input_2 = "IV"
output_2 = 4
print(f"Input 2: {roman_to_integer(input_2) == output_2}")

input_3 = "IX"
output_3 = 9
print(f"Input 3: {roman_to_integer(input_3) == output_3}")

input_4 = "LVIII"
output_4 = 58
print(f"Input 4: {roman_to_integer(input_4) == output_4}")

input_5 = "MCMXCIV"
output_5 = 1994
print(f"Input 5: {roman_to_integer(input_5) == output_5}")