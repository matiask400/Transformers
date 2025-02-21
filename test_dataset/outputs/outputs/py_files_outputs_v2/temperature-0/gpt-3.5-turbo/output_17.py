def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in mapping[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    output = []
    backtrack('', digits)
    return output

# Test Cases
print(letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
print(letterCombinations('') == [])
print(letterCombinations('2') == ['a', 'b', 'c'])