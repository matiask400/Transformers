def is_palindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return original == reversed_num

# Test cases
inputs = [121, -121, 10]
outputs = [True, False, False]
for i in range(len(inputs)):
    print(is_palindrome(inputs[i]) == outputs[i])