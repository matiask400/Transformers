def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed_num = 0
    original = x
    while x != 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return original == reversed_num

# Example inputs and expected outputs
inputs = [121, -121, 10]
outputs = [True, False, False]

# Test the function with the example inputs
for i in range(len(inputs)):
    result = is_palindrome(inputs[i])
    print(result == outputs[i])  # Should output True for each input if the function is correct