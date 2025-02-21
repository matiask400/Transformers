def roman_to_integer(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    num = roman_map[s[n - 1]]
    for i in range(n - 2, -1, -1):
        if roman_map[s[i]] >= roman_map[s[i + 1]]:
            num += roman_map[s[i]]
        else:
            num -= roman_map[s[i]]
    return num


input_1 = "III"
output_1 = 3
input_2 = "IV"
output_2 = 4
input_3 = "IX"
output_3 = 9
input_4 = "LVIII"
output_4 = 58
input_5 = "MCMXCIV"
output_5 = 1994

print(roman_to_integer(input_1) == output_1)
print(roman_to_integer(input_2) == output_2)
print(roman_to_integer(input_3) == output_3)
print(roman_to_integer(input_4) == output_4)
print(roman_to_integer(input_5) == output_5)