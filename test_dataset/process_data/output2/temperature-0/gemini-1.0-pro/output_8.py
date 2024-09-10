import re

def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-', '+']:
        s = s[1:]
    num = 0
    for c in s:
        if not c.isdigit():
            break
        num = num * 10 + ord(c) - ord('0')
    num *= sign
    if num < -2**31:
        return -2**31
    if num > 2**31 - 1:
        return 2**31 - 1
    return num

print(myAtoi('42') == 42)
print(myAtoi('   -42') == -42)
print(myAtoi('4193 with words') == 4193)
print(myAtoi('words and 987') == 0)
print(myAtoi('-91283472332') == -2147483648)