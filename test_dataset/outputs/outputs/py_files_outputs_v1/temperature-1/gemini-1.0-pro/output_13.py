def roman_to_int(s: str) -> int:
    roman_dict = {
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
        value = roman_dict[char]

        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result


inputs = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
outputs = [3, 4, 9, 58, 1994]

for i, input_value in enumerate(inputs):
    output_value = roman_to_int(input_value)
    print(f"Input {i+1}: {input_value}")
    print(f"Output {i+1}: {output_value}")
    print(f"Correct: {output_value == outputs[i]}

")
