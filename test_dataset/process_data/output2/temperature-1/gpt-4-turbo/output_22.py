def generate_parenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

# Test cases
print(generate_parenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']) # Output 1 comparison
print(generate_parenthesis(1) == ['()']) # Output 2 comparison