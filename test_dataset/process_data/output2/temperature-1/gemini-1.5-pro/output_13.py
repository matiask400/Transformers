def roman_to_integer(s: str) -> int:
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
print(f"Input: {input_1}, Output: {roman_to_integer(input_1)}, Expected: {output_1}, Result: {roman_to_integer(input_1) == output_1}")

input_2 = "IV"
output_2 = 4
print(f"Input: {input_2}, Output: {roman_to_integer(input_2)}, Expected: {output_2}, Result: {roman_to_integer(input_2) == output_2}")

input_3 = "IX"
output_3 = 9
print(f"Input: {input_3}, Output: {roman_to_integer(input_3)}, Expected: {output_3}, Result: {roman_to_integer(input_3) == output_3}")