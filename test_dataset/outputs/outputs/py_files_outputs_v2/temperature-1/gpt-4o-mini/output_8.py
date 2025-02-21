def myAtoi(s):
    i = 0
    n = len(s)
    # Step 1: Read in and ignore leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Check for '+' or '-'
    sign = 1
    if i < n and s[i] in ['-', '+']:
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Step 3: Read in digits
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    # Apply sign
    num *= sign

    # Clamp to 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

# Test cases
inputs = ["42", "   -42", "4193 with words"]
outputs = [42, -42, 4193]
for inp, expected in zip(inputs, outputs):
    result = myAtoi(inp)
    print(result == expected)