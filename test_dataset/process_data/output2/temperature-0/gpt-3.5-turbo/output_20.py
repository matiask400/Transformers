def isValid(s):
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

# Test the solution with example inputs
print(isValid('()') == True)
print(isValid('()[]{}') == True)
print(isValid('(]') == False)
print(isValid('([)]') == False)
print(isValid('{[]}') == True)