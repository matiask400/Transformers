def letter_combinations(digits):
    if not digits:
        return []
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    output = []
    backtrack('', digits)
    return output

# Example inputs and expected outputs
inputs = ["23", "", "2"]
expected_outputs = [
    ["ad","ae","af","bd","be","bf","cd","ce","cf"],
    [],
    ["a","b","c"]
]

# Verify the solution
for i, digits in enumerate(inputs):
    result = letter_combinations(digits)
    print(result == expected_outputs[i])