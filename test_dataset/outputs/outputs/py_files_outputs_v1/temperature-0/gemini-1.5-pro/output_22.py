def generateParenthesis(n):
    result = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    backtrack('', 0, 0)
    return result


# Test cases
input1 = 3
output1 = ["((()))","(()())","(())()","()(())","()()()"]
input2 = 1
output2 = ["()"]

print({"Input 1": input1 == input1, "Output 1": generateParenthesis(input1) == output1, "Input 2": input2 == input2, "Output 2": generateParenthesis(input2) == output2})