import math

def reverse(x: int) -> int:
    """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""
    is_negative = x < 0
    x = abs(x)
    reversed_x = int(str(x)[::-1])
    if is_negative:
        reversed_x *= -1
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x


print(reverse(123) == 321)
print(reverse(-123) == -321)
print(reverse(120) == 21)
print(reverse(0) == 0)