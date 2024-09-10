def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    result = max(-2**31, min(sign * result, 2**31 - 1))
    return result

# Test cases
print(myAtoi("42") == 42)
print(myAtoi("   -42") == -42)
print(myAtoi("4193 with words") == 4193)
