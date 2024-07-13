def myAtoi(s: str) -> int:
    s = s.strip()
    if not s or s[0] not in {'-', '+', str(i) for i in range(10)}:
        return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in {'-', '+'}: s = s[1:]
    num = 0
    for c in s:
        if not c.isdigit(): break
        num = num * 10 + int(c)
    num *= sign
    if num < -2 ** 31: return -2 ** 31
    if num > 2 ** 31 - 1: return 2 ** 31 - 1
    return num