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

    result = sign * result
    return max(min(result, 2**31 - 1), -2**31)


# Test cases
inputs = [
    "42",
    "   -42",
    "4193 with words"
]
outputs = [
    42,
    -42,
    4193
]

for i in range(len(inputs)):
    result = myAtoi(inputs[i])
    print(result == outputs[i])