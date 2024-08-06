def roman_to_integer(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    num = roman_map[s[n - 1]]
    for i in range(n - 2, -1, -1):
        if roman_map[s[i]] >= roman_map[s[i + 1]]:
            num += roman_map[s[i]]
        else:
            num -= roman_map[s[i]]
    return num


# Test cases
input1 = "III"
output1 = 3
input2 = "IV"
output2 = 4
input3 = "IX"
output3 = 9

print(roman_to_integer(input1) == output1)  # True
print(roman_to_integer(input2) == output2)  # True
print(roman_to_integer(input3) == output3)  # True