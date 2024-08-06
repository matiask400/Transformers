import re

def isMatch(s: str, p: str) -> bool:
    return re.fullmatch(p, s) is not None


# Test Cases

s1 = "aa"
p1 = "a"
output1 = isMatch(s1, p1)
expected_output1 = False
print(f"Test Case 1 Result: {output1 == expected_output1}")

s2 = "aa"
p2 = "a*"
output2 = isMatch(s2, p2)
expected_output2 = True
print(f"Test Case 2 Result: {output2 == expected_output2}")

s3 = "ab"
p3 = ".*"
output3 = isMatch(s3, p3)
expected_output3 = True
print(f"Test Case 3 Result: {output3 == expected_output3}")