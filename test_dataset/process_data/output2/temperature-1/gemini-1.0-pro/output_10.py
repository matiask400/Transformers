import re


def isMatch(s, p):
    """ :type s: str
    :type p: str
    :rtype: bool
    """
    # Use re module to check if the string matches the pattern
    return re.fullmatch(p, s) is not None



input1 = "aa"
input2 = "a"
print(isMatch(input1, input2))  # False


input1 = "aa"
input2 = "a*"
print(isMatch(input1, input2))  # True


input1 = "ab"
input2 = ".*"
print(isMatch(input1, input2))  # True


input1 = "aab"
input2 = "c*a*b"
print(isMatch(input1, input2))  # True


input1 = "mississippi"
input2 = "mis*is*p*."
print(isMatch(input1, input2))  # False