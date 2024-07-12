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


input1 = "()"
input2 = "()[]{}"
input3 = "(]"

output1 = isValid(input1)
output2 = isValid(input2)
output3 = isValid(input3)

print(output1 == True)
print(output2 == True)
print(output3 == False)