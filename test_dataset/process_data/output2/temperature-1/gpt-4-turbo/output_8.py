def myAtoi(s: str) -> int:
    i, n, result, sign = 0, len(s), 0, 1
    int_max, int_min = 2**31 - 1, -2**31

    # Read and ignore leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # Check sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Read numbers until non-digit
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        # Check for overflow/underflow
        if result > (int_max - digit) // 10:
            return int_min if sign == -1 else int_max
        result = 10 * result + digit
        i += 1

    return sign * result

# Test cases
inputs = ['42', '   -42', '4193 with words']
expected_outputs = [42, -42, 4193]

# Evaluate
results = [myAtoi(inp) == exp for inp, exp in zip(inputs, expected_outputs)]
for result in results:
    print(result)