def generate_parentheses(n):
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
inputs = [3, 1]
expected_outputs = [["((()))","(()())","(())()","()(())","()()()"], ["()"]]

for i, input_val in enumerate(inputs):
    output = generate_parentheses(input_val)
    print('Test', i + 1, ':', output == expected_outputs[i])