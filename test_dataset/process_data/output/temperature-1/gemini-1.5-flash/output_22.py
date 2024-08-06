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

# Example Usage:
input_1 = 3
output_1 = generateParentheses(input_1)
print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")

input_2 = 1
output_2 = generateParentheses(input_2)
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")

# Check if the output matches the expected output
print(f"Output 1 matches expected output: {output_1 == ['((()))', '(()())', '(())()', '()(())', '()()()']}")
print(f"Output 2 matches expected output: {output_2 == ['()']}")