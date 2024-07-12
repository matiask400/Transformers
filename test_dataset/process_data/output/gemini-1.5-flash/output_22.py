def generateParentheses(n):
    result = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    backtrack("", 0, 0)
    return result

# Test cases
input_1 = 3
output_1 = generateParentheses(input_1)
input_2 = 1
output_2 = generateParentheses(input_2)
input_3 = 2
output_3 = generateParentheses(input_3)

# Check if the outputs match the expected results
output_1_match = output_1 == ['((()))', '(()())', '(())()', '()(())', '()()()']
output_2_match = output_2 == ['()']
output_3_match = output_3 == ['(())', '()()']

print(f"Input 1: {input_1}, Output 1: {output_1}, Match: {output_1_match}")
print(f"Input 2: {input_2}, Output 2: {output_2}, Match: {output_2_match}")
print(f"Input 3: {input_3}, Output 3: {output_3}, Match: {output_3_match}")