s = '()[]{}'
res = isValid(s)
print(res == True)
s = '([{}])'
res = isValid(s)
print(res == True)
s = '(])'
res = isValid(s)
print(res == False)
s = '([)]'
res = isValid(s)
print(res == False)
s = '{[]}' 
res = isValid(s)
print(res == True)

def isValid(s: str) -> bool:
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['} 

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
        else:
            return False

    return not stack