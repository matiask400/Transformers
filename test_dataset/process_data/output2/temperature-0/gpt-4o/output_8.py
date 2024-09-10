def myAtoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0

    sign = 1
    if s[i] == '-' or s[i] == '+':
        sign = -1 if s[i] == '-' else 1
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX

    return num

# Test cases
inputs = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
outputs = [42, -42, 4193, 0, -2147483648]

for i, input_str in enumerate(inputs):
    result = myAtoi(input_str)
    print(result == outputs[i])