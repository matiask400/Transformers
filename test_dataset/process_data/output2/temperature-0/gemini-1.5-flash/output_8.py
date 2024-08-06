import sys

def myAtoi(s: str) -> int:
    """
    Converts a string to a 32-bit signed integer.

    Args:
        s: The string to convert.

    Returns:
        The integer representation of the string.
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

# Example 1
s = "42"
output = myAtoi(s)
print(f"Input: {s}")
print(f"Output: {output}")
print(f"Expected Output: 42")
print(f"Output matches expected: {output == 42}")
print()

# Example 2
s = "   -42"
output = myAtoi(s)
print(f"Input: {s}")
print(f"Output: {output}")
print(f"Expected Output: -42")
print(f"Output matches expected: {output == -42}")
print()

# Example 3
s = "4193 with words"
output = myAtoi(s)
print(f"Input: {s}")
print(f"Output: {output}")
print(f"Expected Output: 4193")
print(f"Output matches expected: {output == 4193}")
print()

# Example 4
s = "words and 987"
output = myAtoi(s)
print(f"Input: {s}")
print(f"Output: {output}")
print(f"Expected Output: 0")
print(f"Output matches expected: {output == 0}")
print()

# Example 5
s = "-91283472332"
output = myAtoi(s)
print(f"Input: {s}")
print(f"Output: {output}")
print(f"Expected Output: -2147483648")
print(f"Output matches expected: {output == -2147483648}")
print()