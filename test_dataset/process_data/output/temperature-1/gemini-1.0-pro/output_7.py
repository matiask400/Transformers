def reverse(x: int) -> int:
    """Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return 0."""
    INT_MAX = (1 << 31) - 1
    INT_MIN = -INT_MAX - 1

    reversed_integer = 0
    if x < 0:
        reversed_integer = -x
        x = abs(x)

    while(x):
        reversed_integer = (reversed_integer * 10) + x % 10
        x //= 10

    if reversed_integer > INT_MAX or reversed_integer < INT_MIN:
        return 0

    return -reversed_integer if reversed_integer < 0 else reversed_integer

input_1 = 123
output_1 = reverse(input_1)
print(output_1)
input_2 = -123
output_2 = reverse(input_2)
print(output_2)
input_3 = 120
output_3 = reverse(input_3)