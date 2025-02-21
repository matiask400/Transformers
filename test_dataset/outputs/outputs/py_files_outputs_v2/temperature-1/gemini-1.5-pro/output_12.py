# Define integer to roman mapping 
int_to_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}

def intToRoman(num):
    """
    Given an integer, convert it to a roman numeral.
    """
    i = 12
    result = ""
    while num != 0:
        if list(int_to_roman.keys())[i] <= num:
            result += list(int_to_roman.values())[i]
            num -= list(int_to_roman.keys())[i]
        else:
            i -= 1
    return result

# Test cases
inputs = [3, 4, 9, 58, 1994]
outputs = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

for i in range(len(inputs)):
    output = intToRoman(inputs[i])
    print(output == outputs[i])