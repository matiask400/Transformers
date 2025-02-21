import sys

def reverse(x: int) -> int:
    """Reverses the digits of a 32-bit signed integer.
    """
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    reversed = 0
    if x > 0:
        while x > 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        return reversed if reversed <= INT_MAX else 0
    elif x < 0:
        x = -x
        while x > 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        reversed = -reversed
        return reversed if reversed >= INT_MIN else 0
    else:
        return 0


# Example 1: Input x = 123, Output: 321
print(reverse(123) == 321)

# Example 2: Input x = -123, Output: -321
print(reverse(-123) == -321)

# Example 3: Input x = 120, Output: 21
print(reverse(120) == 21)

# Example 4: Input x = 0, Output: 0
print(reverse(0) == 0)