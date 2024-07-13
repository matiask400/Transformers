import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
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
            result = [prefix + letter for prefix in result for letter in mapping[digit]]
        return result

# Test the solution

solution = Solution()

input_1 = "23"
output_1 = solution.letterCombinations(input_1)

input_2 = ""
output_2 = solution.letterCombinations(input_2)

input_3 = "2"
output_3 = solution.letterCombinations(input_3)

print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")
print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")

# Check if the outputs match the expected results
print(f"Output 1 matches expected: {output_1 == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']}")
print(f"Output 2 matches expected: {output_2 == []}")
print(f"Output 3 matches expected: {output_3 == ['a', 'b', 'c']}")