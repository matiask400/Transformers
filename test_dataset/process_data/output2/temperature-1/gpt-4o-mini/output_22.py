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

# Example Inputs
inputs = [3, 1]
outputs = ["((()))","(()())","(())()","()(())","()()()"], ["()"]

for index, input_value in enumerate(inputs):
    result = generate_parentheses(input_value)
    output_value = outputs[index]
    print(result == output_value)