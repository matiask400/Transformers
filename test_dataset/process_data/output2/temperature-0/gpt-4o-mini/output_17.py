def letter_combinations(digits):
    if not digits:
        return []
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

# Test cases
inputs = [
    "23",
    "",
    "2"
]
outputs = [
    ["ad","ae","af","bd","be","bf","cd","ce","cf"],
    [],
    ["a","b","c"]
]
for i in range(len(inputs)):
    result = letter_combinations(inputs[i])
    print(result == outputs[i])