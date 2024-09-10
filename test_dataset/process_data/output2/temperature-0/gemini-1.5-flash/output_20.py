def is_valid(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if stack and stack[-1] == parentheses[char]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0

# Example 1
s = "()"
print(is_valid(s) == True)

# Example 2
s = "()[]{}"
print(is_valid(s) == True)

# Example 3
s = "(]"
print(is_valid(s) == False)

# Example 4
s = "([)]"
print(is_valid(s) == False)

# Example 5
s = "{[]}"
print(is_valid(s) == True)