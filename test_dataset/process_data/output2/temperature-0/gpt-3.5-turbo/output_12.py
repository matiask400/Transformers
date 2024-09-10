def intToRoman(num: int) -> str:
    roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_numeral = ''
    for value, numeral in roman_numerals:
        count = num // value
        roman_numeral += numeral * count
        num -= value * count
    return roman_numeral

# Test cases
print(intToRoman(3) == 'III')
print(intToRoman(4) == 'IV')
print(intToRoman(9) == 'IX')