def letter_combinations(digits):
    if not digits:
        return []
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    def backtrack(index, path):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    combinations = []
    backtrack(0, [])
    return combinations

# Example inputs and expected outputs
input_1 = "23"
output_1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

input_2 = ""
output_2 = []

input_3 = "2"
output_3 = ["a","b","c"]

# Test function to verify the outputs
print(letter_combinations(input_1) == output_1)  # Expected: True
print(letter_combinations(input_2) == output_2)  # Expected: True
print(letter_combinations(input_3) == output_3)  # Expected: True