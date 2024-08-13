def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

# Test cases
inputs = ["()", "()[]{}", "(]", "([)]", "{[]}"]
outputs = [True, True, False, False, True]

for i, input_str in enumerate(inputs):
    result = isValid(input_str)
    print(result == outputs[i])