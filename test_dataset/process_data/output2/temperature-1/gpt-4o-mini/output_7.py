def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = int(str(x)[::-1]) * sign
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

inputs = [123, -123, 120, 0]
outputs = [321, -321, 21, 0]
for i in range(3):
    print(reverse_integer(inputs[i]) == outputs[i])