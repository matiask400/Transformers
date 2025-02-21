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
input1 = 3
output1 = "III"
input2 = 4
output2 = "IV"
input3 = 9
output3 = "IX"

print(intToRoman(input1) == output1)  # True
print(intToRoman(input2) == output2)  # True
print(intToRoman(input3) == output3)  # True