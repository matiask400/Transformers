def myAtoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    result = 0
    for c in s:
        if not c.isdigit():
            break
        result = result * 10 + int(c)

    result *= sign
    result = max(-2**31, min(2**31 - 1, result))
    return result


input_1 = "42"
output_1 = 42
input_2 = "   -42"
output_2 = -42
input_3 = "4193 with words"
output_3 = 4193

print(myAtoi(input_1) == output_1)
print(myAtoi(input_2) == output_2)
print(myAtoi(input_3) == output_3)