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


input_1 = "()"
output_1 = True
input_2 = "()[]{}"
output_2 = True
input_3 = "(]"
output_3 = False

print(isValid(input_1) == output_1)
print(isValid(input_2) == output_2)
print(isValid(input_3) == output_3)