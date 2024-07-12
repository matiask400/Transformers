import math

def reverse_integer(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    if reversed_x > math.pow(2, 31) - 1 or reversed_x < -math.pow(2, 31):
        return 0
    return reversed_x * sign

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

# Check if the outputs are correct
print(f'Output 1 is correct: {output_1 == 321}')
print(f'Output 2 is correct: {output_2 == -321}')
print(f'Output 3 is correct: {output_3 == 21}')