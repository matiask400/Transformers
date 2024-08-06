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
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    result = result * sign
    if result > 2**31 - 1:
        return 2**31 - 1
    elif result < -2**31:
        return -2**31
    else:
        return result

# Example 1:
input_1 = "42"
output_1 = myAtoi(input_1)
print(f"Example 1: {output_1 == 42}")

# Example 2:
input_2 = "   -42"
output_2 = myAtoi(input_2)
print(f"Example 2: {output_2 == -42}")

# Example 3:
input_3 = "4193 with words"
output_3 = myAtoi(input_3)
print(f"Example 3: {output_3 == 4193}")

# Example 4:
input_4 = "words and 987"
output_4 = myAtoi(input_4)
print(f"Example 4: {output_4 == 0}")

# Example 5:
input_5 = "-91283472332"
output_5 = myAtoi(input_5)
print(f"Example 5: {output_5 == -2147483648}")