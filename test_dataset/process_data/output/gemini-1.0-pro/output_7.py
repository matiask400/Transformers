def reverse(x: int) -> int:
    rev = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    if rev > 2**31 - 1 or rev < -2**31:
        return 0
    return rev * sign