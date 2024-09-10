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
expected_outputs = [True, True, False, False, True]

for s, expected in zip(inputs, expected_outputs):
    result = isValid(s)
    print(result == expected)
