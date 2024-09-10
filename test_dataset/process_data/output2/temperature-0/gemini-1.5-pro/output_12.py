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


input_1 = 3
output_1 = "III"
print(f"Input 1: {intToRoman(input_1) == output_1}")

input_2 = 4
output_2 = "IV"
print(f"Input 2: {intToRoman(input_2) == output_2}")

input_3 = 9
output_3 = "IX"
print(f"Input 3: {intToRoman(input_3) == output_3}")