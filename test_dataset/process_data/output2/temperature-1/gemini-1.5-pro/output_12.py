def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            result += roman[i]
            num -= values[i]
        i += 1
    return result

# Test cases
inputs = [3, 4, 9, 58, 1994]
outputs = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']

for i in range(len(inputs)):
    print(intToRoman(inputs[i]) == outputs[i])