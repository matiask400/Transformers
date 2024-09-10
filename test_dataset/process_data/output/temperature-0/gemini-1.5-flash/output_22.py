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

# Check if the outputs match the expected results
output_1_match = output_1 == ['((()))', '(()())', '(())()', '()(())', '()()()']
output_2_match = output_2 == ['()']

print(f"Output 1 match: {output_1_match}")
print(f"Output 2 match: {output_2_match}")