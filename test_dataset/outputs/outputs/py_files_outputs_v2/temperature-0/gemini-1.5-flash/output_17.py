from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
                for word in result:
                    temp.append(word + letter)
            result = temp
        return result

# Test cases

solution = Solution()

input_1 = "23"
output_1 = solution.letterCombinations(input_1)
print(output_1 == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])  # True

input_2 = ""
output_2 = solution.letterCombinations(input_2)
print(output_2 == [])  # True

input_3 = "2"
output_3 = solution.letterCombinations(input_3)
print(output_3 == ['a', 'b', 'c'])  # True