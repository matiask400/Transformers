import re

def is_match(s, p):
    return bool(re.fullmatch(p, s))

s1 = "aa"
p1 = "a"
output1 = is_match(s1, p1)
expected_output1 = False
print(output1 == expected_output1)

s2 = "aa"
p2 = "a*"
output2 = is_match(s2, p2)
expected_output2 = True
print(output2 == expected_output2)

s3 = "ab"
p3 = ".*"
output3 = is_match(s3, p3)
expected_output3 = True
print(output3 == expected_output3)

s4 = "aab"
p4 = "c*a*b"
output4 = is_match(s4, p4)
expected_output4 = True
print(output4 == expected_output4)

s5 = "mississippi"
p5 = "mis*is*p*."
output5 = is_match(s5, p5)
expected_output5 = False
print(output5 == expected_output5)