def reverse_integer(x):
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

# Test cases
input_1 = 123
output_1 = 321
input_2 = -123
output_2 = -321
input_3 = 120
output_3 = 21

print(reverse_integer(input_1) == output_1)
print(reverse_integer(input_2) == output_2)
print(reverse_integer(input_3) == output_3)