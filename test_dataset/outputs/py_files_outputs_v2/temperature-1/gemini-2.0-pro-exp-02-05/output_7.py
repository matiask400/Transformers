def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0

    while x > 0:
        pop = x % 10
        x //= 10

        if reversed_x > 214748364 or (reversed_x == 214748364 and pop > 7):
            return 0
        if reversed_x < -214748364 or (reversed_x == -214748364 and pop < -8):
            return 0

        reversed_x = reversed_x * 10 + pop

    return sign * reversed_x