# Function to generate all combinations of well-formed parentheses
def generateParenthesis(n):
    result = []
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    backtrack()
    return result

# Test cases
input_1 = 3
output_1 = ["((()))","(()())","(())()","()(())","()()()"]
input_2 = 1
output_2 = ["()"]

print(f'Input 1: {generateParenthesis(input_1) == output_1}')
print(f'Input 2: {generateParenthesis(input_2) == output_2}')