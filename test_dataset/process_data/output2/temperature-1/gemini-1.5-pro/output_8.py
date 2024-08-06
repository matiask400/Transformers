def myAtoi(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    res = 0
    for i in range(len(s)):
        if not s[i].isdigit():
            break
        res = res * 10 + int(s[i])
    res = sign * res
    if res > 2**31 - 1:
        return 2**31 - 1
    elif res < -2**31:
        return -2**31
    else:
        return res


print(myAtoi("42") == 42)
print(myAtoi("   -42") == -42)
print(myAtoi("4193 with words") == 4193)
print(myAtoi("words and 987") == 0)
print(myAtoi("-91283472332") == -2147483648)