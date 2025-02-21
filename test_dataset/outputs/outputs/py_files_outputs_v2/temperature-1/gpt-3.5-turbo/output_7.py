def reverse_integer(x):
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1
    reversed_x = 0
    while x != 0:
        digit = x % 10
        x = x // 10
        reversed_x = reversed_x * 10 + digit
    reversed_x *= sign
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

# Test cases
print(reverse_integer(123) == 321)
print(reverse_integer(-123) == -321)
print(reverse_integer(120) == 21)
print(reverse_integer(0) == 0)