def intToRoman(num):
    """
    Given an integer, convert it to a roman numeral.
    """
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                  50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
                  900: 'CM', 1000: 'M'}
    
    integers = list(roman_map.keys())
    romans = list(roman_map.values())
    
    i = 12
    result = ""
    while num != 0:
        if integers[i] <= num:
            result += romans[i]
            num -= integers[i]
        else:
            i -= 1
            
    return result