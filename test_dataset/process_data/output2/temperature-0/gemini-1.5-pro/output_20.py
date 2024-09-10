def is_valid(s):
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


s1 = "()"
output1 = is_valid(s1)
expected_output1 = True
print(f"Input: {s1}, Output: {output1}, Expected: {expected_output1}, Result: {output1 == expected_output1}")

s2 = "()[]{}"
output2 = is_valid(s2)
expected_output2 = True
print(f"Input: {s2}, Output: {output2}, Expected: {expected_output2}, Result: {output2 == expected_output2}")

s3 = "(]"
output3 = is_valid(s3)
expected_output3 = False
print(f"Input: {s3}, Output: {output3}, Expected: {expected_output3}, Result: {output3 == expected_output3}")

s4 = "([)]"
output4 = is_valid(s4)
expected_output4 = False
print(f"Input: {s4}, Output: {output4}, Expected: {expected_output4}, Result: {output4 == expected_output4}")

s5 = "{[]}"
output5 = is_valid(s5)
expected_output5 = True
print(f"Input: {s5}, Output: {output5}, Expected: {expected_output5}, Result: {output5 == expected_output5}")