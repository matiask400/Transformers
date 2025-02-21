def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x != 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return original == reversed_num

# Test cases
inputs = [121, -121, 10, -101]
expected_outputs = [True, False, False, False]

for i, input_val in enumerate(inputs):
    result = is_palindrome(input_val)
    print(result == expected_outputs[i])