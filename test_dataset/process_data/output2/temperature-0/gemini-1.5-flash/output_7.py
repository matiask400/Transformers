import math

def reverse_integer(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    reversed_x *= sign
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

# Example 1
input_1 = 123
output_1 = reverse_integer(input_1)
print(output_1 == 321)  # True

# Example 2
input_2 = -123
output_2 = reverse_integer(input_2)
print(output_2 == -321)  # True

# Example 3
input_3 = 120
output_3 = reverse_integer(input_3)
print(output_3 == 21)  # True

# Example 4
input_4 = 0
output_4 = reverse_integer(input_4)
print(output_4 == 0)  # True