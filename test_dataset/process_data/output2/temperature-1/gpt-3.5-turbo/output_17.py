def letter_combinations(digits):
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
    result = ['']
    for digit in digits:
        new_result = []
        for char in mapping[digit]:
            for word in result:
                new_result.append(word + char)
        result = new_result
    return result

# Test Cases
print(letter_combinations('23') == ['ad','ae','af','bd','be','bf','cd','ce','cf'])
print(letter_combinations('') == [])
print(letter_combinations('2') == ['a', 'b', 'c'])