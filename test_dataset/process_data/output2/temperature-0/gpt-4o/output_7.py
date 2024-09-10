def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    res = 0
    while x != 0:
        pop = x % 10 if x > 0 else x % -10
        x = x // 10 if x > 0 else (x - pop) // 10
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
            return 0
        if res < INT_MIN // 10 or (res == INT_MIN // 10 and pop < -8):
            return 0
        res = res * 10 + pop
    return res

# Test cases
inputs = [123, -123, 120]
expected_outputs = [321, -321, 21]

for i, input_val in enumerate(inputs):
    output = reverse(input_val)
    print(output == expected_outputs[i])