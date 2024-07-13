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

    result = ['']
    for digit in digits:
        temp = []
        for letter in mapping[digit]:
            for combination in result:
                temp.append(combination + letter)
        result = temp
    return result


# Test cases
input1 = "23"
output1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(input1) == output1)

input2 = ""
output2 = []
print(letterCombinations(input2) == output2)

input3 = "2"
output3 = ["a","b","c"]
print(letterCombinations(input3) == output3)