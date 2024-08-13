def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    rev = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x != 0:
        pop = x % 10
        x //= 10
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
        if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and pop < -8):
            return 0
        rev = rev * 10 + pop
    return sign * rev

x1 = 123
output1 = 321
result1 = reverse_integer(x1) == output1
print('Test input 1:', result1)

x2 = -123
output2 = -321
result2 = reverse_integer(x2) == output2
print('Test input 2:', result2)

x3 = 120
output3 = 21
result3 = reverse_integer(x3) == output3
print('Test input 3:', result3)