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
    result = max(min(result, 2**31 - 1), -2**31)
    return result


# Test cases
inputs = [
    "42",
    "   -42",
    "4193 with words",
    "words and 987",
    "-91283472332"
]
outputs = [
    42,
    -42,
    4193,
    0,
    -2147483648
]

for i in range(len(inputs)):
    output = myAtoi(inputs[i])
    print(output == outputs[i])