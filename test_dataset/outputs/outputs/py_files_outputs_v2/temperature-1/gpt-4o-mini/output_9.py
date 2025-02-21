def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

inputs = [121, -121, 10]
outputs = [True, False, False]

for i, input_value in enumerate(inputs):
    print(is_palindrome(input_value) == outputs[i])