import re

def roman_to_integer(s: str) -> int:
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

# Example 1
input_1 = "III"
output_1 = roman_to_integer(input_1)
print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")

# Example 2
input_2 = "IV"
output_2 = roman_to_integer(input_2)
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")

# Example 3
input_3 = "IX"
output_3 = roman_to_integer(input_3)
print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")

# Example 4
input_4 = "LVIII"
output_4 = roman_to_integer(input_4)
print(f"Input 4: {input_4}")
print(f"Output 4: {output_4}")

# Example 5
input_5 = "MCMXCIV"
output_5 = roman_to_integer(input_5)
print(f"Input 5: {input_5}")
print(f"Output 5: {output_5}")