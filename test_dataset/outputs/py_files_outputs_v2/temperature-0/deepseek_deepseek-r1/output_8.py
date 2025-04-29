def myAtoi(s: str) -> int:
    index = 0
    n = len(s)
    
    # Skip leading whitespace
    while index < n and s[index] == ' ':
        index += 1
    
    if index == n:
        return 0
    
    # Determine sign
    sign = 1
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1
    
    # Build number from digits
    num = 0
    while index < n and s[index].isdigit():
        digit = ord(s[index]) - ord('0')
        num = num * 10 + digit
        index += 1
    
    # Apply sign
    num *= sign
    
    # Clamp to 32-bit integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if num < INT_MIN:
        return INT_MIN
    elif num > INT_MAX:
        return INT_MAX
    else:
        return num