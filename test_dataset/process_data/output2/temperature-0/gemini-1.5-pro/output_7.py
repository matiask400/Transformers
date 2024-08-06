def reverse_integer(x):
    sign = 1 if x >= 0 else -1
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
inputs = [123, -123, 120, 0]
outputs = [321, -321, 21, 0]

for i in range(len(inputs)):
    result = reverse_integer(inputs[i])
    print(result == outputs[i])