def reverse(x):
    """
    Given a signed 32-bit integer `x`, return `x` with its digits reversed.
    If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0

    while x > 0:
        pop = x % 10
        x //= 10

        if reversed_x > 214748364 or (reversed_x == 214748364 and pop > 7):
            return 0

        reversed_x = (reversed_x * 10) + pop

    return sign * reversed_x