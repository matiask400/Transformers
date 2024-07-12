import sys

def myAtoi(s: str) -> int:
    """
    Converts a string to a 32-bit signed integer.

    Args:
        s: The string to convert.

    Returns:
        The converted integer.
    """
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
    for i in range(len(s)):
        if not s[i].isdigit():
            break
        result = result * 10 + int(s[i])
    result *= sign
    if result > 2**31 - 1:
        return 2**31 - 1
    elif result < -2**31:
        return -2**31
    return result

# Test cases
input_1 = "42"
output_1 = myAtoi(input_1)
print(f"Input 1: {input_1}, Output 1: {output_1}")

input_2 = "   -42"
output_2 = myAtoi(input_2)
print(f"Input 2: {input_2}, Output 2: {output_2}")

input_3 = "4193 with words"
output_3 = myAtoi(input_3)
print(f"Input 3: {input_3}, Output 3: {output_3}")