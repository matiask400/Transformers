import math

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
output_1 = reverse_integer(input_1)
print(f'Input 1: {input_1}, Output 1: {output_1}')

input_2 = -123
output_2 = reverse_integer(input_2)
print(f'Input 2: {input_2}, Output 2: {output_2}')

input_3 = 120
output_3 = reverse_integer(input_3)
print(f'Input 3: {input_3}, Output 3: {output_3}')

input_4 = 0
output_4 = reverse_integer(input_4)
print(f'Input 4: {input_4}, Output 4: {output_4}')