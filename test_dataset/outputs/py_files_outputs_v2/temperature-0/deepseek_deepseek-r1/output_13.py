def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for char in s:
        total += roman[char]
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            total -= 2 * roman[s[i]]
    return total