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

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return

            for letter in mapping[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, '')
        return result


# Example 1: Input: digits = "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
input1 = "23"
output1 = Solution().letterCombinations(input1)
print(output1 == ["ad","ae","af","bd","be","bf","cd","ce","cf"])

# Example 2: Input: digits = "" Output: []
input2 = ""
output2 = Solution().letterCombinations(input2)
print(output2 == [])

# Example 3: Input: digits = "2" Output: ["a","b","c"]
input3 = "2"
output3 = Solution().letterCombinations(input3)
print(output3 == ["a","b","c"])