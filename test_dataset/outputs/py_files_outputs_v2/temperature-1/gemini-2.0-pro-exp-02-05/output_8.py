def myAtoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    start = 0
    if s[0] == '-':
        sign = -1
        start = 1
    elif s[0] == '+':
        start = 1

    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        digit = int(s[i])
        if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
            return 2**31 - 1 if sign == 1 else -2**31
        result = result * 10 + digit

    return sign * result