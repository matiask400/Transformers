def generateParenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)

    res = []
    backtrack()
    return res

# Example 1
input_1 = 3
output_1 = ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(input_1) == output_1)

# Example 2
input_2 = 1
output_2 = ["()"]
print(generateParenthesis(input_2) == output_2)