def roman_to_integer(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    num = roman_map[s[n - 1]]
    for i in range(n - 2, -1, -1):
        if roman_map[s[i]] >= roman_map[s[i + 1]]:
            num += roman_map[s[i]]
        else:
            num -= roman_map[s[i]]
    return num


# Example usage and verification
input_1 = "III"
output_1 = 3
input_2 = "IV"
output_2 = 4
input_3 = "IX"
output_3 = 9

print(roman_to_integer(input_1) == output_1)  # True
print(roman_to_integer(input_2) == output_2)  # True
print(roman_to_integer(input_3) == output_3)  # True