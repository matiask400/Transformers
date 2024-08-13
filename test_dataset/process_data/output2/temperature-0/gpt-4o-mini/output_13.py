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

# Example inputs
inputs = ["III", "IV", "IX"]
outputs = [3, 4, 9]

for i in range(len(inputs)):
    result = roman_to_int(inputs[i])
    print(result == outputs[i])