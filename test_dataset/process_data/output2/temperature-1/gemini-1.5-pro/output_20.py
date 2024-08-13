def isValid(s):
    stack = []
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"

print(isValid(s1) == True)
print(isValid(s2) == True)
print(isValid(s3) == False)
print(isValid(s4) == False)
print(isValid(s5) == True)