from itertools import product

def letter_combinations(digits):
    if not digits:
        return []
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    letter_lists = [digit_to_letters[digit] for digit in digits]
    return [''.join(combo) for combo in product(*letter_lists)]

# Test examples
input_1 = '23'
out_1 = letter_combinations(input_1)
expected_output_1 = ['ad','ae','af','bd','be','bf','cd','ce','cf']
print(out_1 == expected_output_1)  # Should print True if correct

input_2 = ''
out_2 = letter_combinations(input_2)
expected_output_2 = []
print(out_2 == expected_output_2)  # Should print True if correct

input_3 = '2'
out_3 = letter_combinations(input_3)
expected_output_3 = ['a','b','c']
print(out_3 == expected_output_3)  # Should print True if correct