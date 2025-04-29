def myAtoi(s):
    """
    Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).
    """
    s = s.lstrip()
    if not s:
        return 0

    sign = 1
    index = 0

    if s[0] == '+':
        index += 1
    elif s[0] == '-':
        sign = -1
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
            return 2**31 - 1 if sign == 1 else -2**31
        result = result * 10 + digit
        index += 1

    return sign * result