def is_valid(s: str) -> bool:
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


input1 = "()"
output1 = is_valid(input1)
print(output1)

input2 = "()[]{}"
output2 = is_valid(input2)
print(output2)

input3 = "(]"
output3 = is_valid(input3)
print(output3)