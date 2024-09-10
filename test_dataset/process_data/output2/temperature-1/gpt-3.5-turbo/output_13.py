def romanToInt(s: str) -> int:
    roman_values = {
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
    for c in s:
        curr_value = roman_values[c]
        result += curr_value
        if curr_value > prev_value:
            result -= 2 * prev_value
        prev_value = curr_value
    return result

# Test cases
print(romanToInt("III") == 3)
print(romanToInt("IV") == 4)
print(romanToInt("IX") == 9)