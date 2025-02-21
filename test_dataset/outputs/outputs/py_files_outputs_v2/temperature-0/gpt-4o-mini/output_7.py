def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = int(str(x)[::-1])
    if reversed_x > 2**31 - 1:
        return 0
    return sign * reversed_x

# Test cases
inputs = [123, -123, 120]
outputs = [321, -321, 21]
for i in range(len(inputs)):
    result = reverse_integer(inputs[i])
    print(result == outputs[i])