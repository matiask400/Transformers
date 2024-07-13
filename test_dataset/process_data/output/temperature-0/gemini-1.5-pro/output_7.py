def reverse_integer(x):
    """
    Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    if x == 0:
        return 0
    sign = 1 if x > 0 else -1
    x = abs(x)
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    reversed_x = sign * reversed_x
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

# Test cases
input_1 = 123
output_1 = 321
input_2 = -123
output_2 = -321
input_3 = 120
output_3 = 21

print(reverse_integer(input_1) == output_1)  # True
print(reverse_integer(input_2) == output_2)  # True
print(reverse_integer(input_3) == output_3)  # True