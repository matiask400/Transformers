import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        result = []
        for combination in itertools.product(*[phone[digit] for digit in digits]):
            result.append(''.join(combination))
        return result

# Test the code with the example inputs
solution = Solution()

input_1 = '23'
output_1 = solution.letterCombinations(input_1)
print(f'Input 1: {input_1}')
print(f'Output 1: {output_1}')

input_2 = ''
output_2 = solution.letterCombinations(input_2)
print(f'Input 2: {input_2}')
print(f'Output 2: {output_2}')

input_3 = '2'
output_3 = solution.letterCombinations(input_3)
print(f'Input 3: {input_3}')
print(f'Output 3: {output_3}')