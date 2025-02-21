def intToRoman(num): 
    value_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    for value, numeral in value_map:
        while num >= value:
            roman += numeral
            num -= value
    return roman

test_cases = {3: 'III', 4: 'IV', 9: 'IX'}
results = {k: intToRoman(k)==v for k, v in test_cases.items()}
for k, v in results.items():
    print(f'Input: {k}, Output Correct: {v}')