def generateParenthesis(n):
    def backtrack(S='', left=0, right=0):
        if len(S) == 2*n:
            output.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)
    output = []
    backtrack()
    return output

# Test the function with example inputs
print(generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'])
print(generateParenthesis(1) == ['()'])