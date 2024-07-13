def isValid(s):
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0


# test
print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)