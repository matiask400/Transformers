def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else ' '
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Example inputs and validation
inputs = [
    '()',
    '()[]{}',
    '(]'
]
outputs = [
    True,
    True,
    False
]

for i in range(len(inputs)):
    print(is_valid(inputs[i]) == outputs[i])
