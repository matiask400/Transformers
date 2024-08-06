def intToRoman(num: int) -> str:
    symbol_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    integers = list(symbol_map.keys())
    symbols = list(symbol_map.values())

    i = 12
    result = ''

    while num != 0:
        if integers[i] <= num:
            result += symbols[i]
            num -= integers[i]
        else:
            i -= 1

    return result

# Test cases
input_values = [3, 4, 9, 58, 1994]
output_values = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

for i in range(len(input_values)):
    print(intToRoman(input_values[i]) == output_values[i])