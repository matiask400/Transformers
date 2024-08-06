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
inputs = [3, 1]
outputs = [["((()))","(()())","(())()","()(())","()()()"], ["()"]]

for i in range(len(inputs)):
    output = generateParenthesis(inputs[i])
    print(output == outputs[i])