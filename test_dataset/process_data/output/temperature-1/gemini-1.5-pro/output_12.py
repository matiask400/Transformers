def intToRoman(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman_num += roman[i]
            num -= values[i]
        i += 1
    return roman_num


# Test cases
input1 = 3
output1 = "III"
input2 = 4
output2 = "IV"
input3 = 9
output3 = "IX"

print(f'Input 1: {input1}, Output 1: {output1}, Result: {intToRoman(input1) == output1}')
print(f'Input 2: {input2}, Output 2: {output2}, Result: {intToRoman(input2) == output2}')
print(f'Input 3: {input3}, Output 3: {output3}, Result: {intToRoman(input3) == output3}')