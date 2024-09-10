import sys

def reverse_integer(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    if reversed_x > (sys.maxsize) or reversed_x < -(sys.maxsize - 1):
        return 0
    return reversed_x * sign

# Test cases
inputs = [
    123,
    -123,
    120,
    0
]
outputs = [
    321,
    -321,
    21,
    0
]

for i in range(len(inputs)):
    result = reverse_integer(inputs[i])
    print(f'Input {i+1}: {inputs[i]}, Output: {result}, Expected: {outputs[i]}, Result: {result == outputs[i]}')