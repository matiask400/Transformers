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
    result = 0
    for c in s:
        if not c.isdigit():
            break
        result = result * 10 + int(c)
    result *= sign
    if result > 2**31 - 1:
        return 2**31 - 1
    elif result < -2**31:
        return -2**31
    else:
        return result


assert myAtoi("42") == 42, 'Test 1 Failed'
assert myAtoi("   -42") == -42, 'Test 2 Failed'
assert myAtoi("4193 with words") == 4193, 'Test 3 Failed'