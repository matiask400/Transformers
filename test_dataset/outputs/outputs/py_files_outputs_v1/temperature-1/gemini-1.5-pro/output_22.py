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

assert generateParenthesis(input1) == output1, 'Test 1 Failed'
assert generateParenthesis(input2) == output2, 'Test 2 Failed'
print('All tests passed!')