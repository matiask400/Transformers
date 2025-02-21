def letterCombinations(digits):
    if not digits:
        return []

    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = ['' for _ in range(len(digits))]

    def backtrack(index):
        if index == len(digits):
            output.append(''.join(result))
            return

        for char in mapping[digits[index]]:
            result[index] = char
            backtrack(index + 1)

    output = []
    backtrack(0)
    return output