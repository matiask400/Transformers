def roman_to_integer(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s[::-1]:
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

example_inputs_outputs = [
    ("III", 3),
    ("IV", 4),
    ("IX", 9)
]

for s, expected in example_inputs_outputs:
    result = roman_to_integer(s)
    print(result == expected)
