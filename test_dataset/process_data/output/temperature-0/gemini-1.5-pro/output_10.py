import re
def isMatch(s, p):
    return re.fullmatch(p, s) is not None

# Test cases
print(isMatch("aa", "a") == False)
print(isMatch("aa", "a*") == True)
print(isMatch("ab", ".*") == True)