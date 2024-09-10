def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    result = 0
    negative = x < 0
    x = abs(x)
    while x != 0:
        pop = x % 10
        x //= 10
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
            return 0
        if result < INT_MIN // 10 or (result == INT_MIN // 10 and pop < -8):
            return 0
        result = result * 10 + pop
    return -result if negative else result

# Test cases
print(reverse_integer(123) == 321)
print(reverse_integer(-123) == -321)
print(reverse_integer(120) == 21)
print(reverse_integer(0) == 0)