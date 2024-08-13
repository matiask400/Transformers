def myAtoi(s: str) -> int:
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    i, n, sign, result = 0, len(s), 1, 0

    while i < n and s[i] == ' ':
        i += 1

    if i < n and s[i] in ('+', '-'): 
        sign = -1 if s[i] == '-' else 1
        i += 1

    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

# Test cases
inputs = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
outputs = [42, -42, 4193, 0, -2147483648]

results = [myAtoi(inputs[i]) == outputs[i] for i in range(len(inputs))]
print(results)