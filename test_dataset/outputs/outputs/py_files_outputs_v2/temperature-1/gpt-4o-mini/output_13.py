def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Example inputs and verification
input_1 = 'III'
expected_output_1 = 3
output_1 = roman_to_int(input_1)
print(output_1 == expected_output_1)  # True

input_2 = 'IV'
expected_output_2 = 4
output_2 = roman_to_int(input_2)
print(output_2 == expected_output_2)  # True

input_3 = 'IX'
expected_output_3 = 9
output_3 = roman_to_int(input_3)
print(output_3 == expected_output_3)  # True