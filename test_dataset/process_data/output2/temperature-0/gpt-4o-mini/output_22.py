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

# Example inputs
input_1 = 3
output_1 = generate_parentheses(input_1)
expected_output_1 = ["((()))","(()())","(())()","()(())","()()()"]
print(output_1 == expected_output_1)

input_2 = 1
output_2 = generate_parentheses(input_2)
expected_output_2 = ["()"]
print(output_2 == expected_output_2)

# No third example input or output provided in the problem description.