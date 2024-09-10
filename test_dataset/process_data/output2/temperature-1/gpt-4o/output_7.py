def reverse_integer(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    res = 0
    while x != 0:
        digit = int(x % 10)
        x = int(x / 10)
        # Check for overflow:
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
            return 0
        if res < INT_MIN // 10 or (res == INT_MIN // 10 and digit < -8):
            return 0
        res = res * 10 + digit
    return res

# Testing the examples provided
inputs = [123, -123, 120, 0]
expected_outputs = [321, -321, 21, 0]

for i, inp in enumerate(inputs):
    result = reverse_integer(inp)
    print(result == expected_outputs[i])
