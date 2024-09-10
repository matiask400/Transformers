def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    index = 0
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1
    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1
    result *= sign
    INT_MIN, INT_MAX = -2147483648, 2147483647
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    return result

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
    print(myAtoi(inputs[i]) == outputs[i])