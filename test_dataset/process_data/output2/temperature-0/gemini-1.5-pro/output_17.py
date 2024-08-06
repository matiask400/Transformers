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
digits1 = "23"
output1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits2 = ""
output2 = []
digits3 = "2"
output3 = ["a","b","c"]

print(letterCombinations(digits1) == output1)  
print(letterCombinations(digits2) == output2)  
print(letterCombinations(digits3) == output3)  