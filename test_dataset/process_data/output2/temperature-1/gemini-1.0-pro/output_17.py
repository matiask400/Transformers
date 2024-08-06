from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or '1' in digits: return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = ['']
        for digit in digits:
            nextans = []
            for s in ans:
                for c in mapping[digit]:
                    nextans.append(s+c)
            ans = nextans
        return ans

if __name__ == "__main__":
    testCases = [('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']), ('', []), ('2', ['a','b','c'])]
    all_correct = True
    for digits, expectedOutput in testCases:
        output = Solution().letterCombinations(digits)
        if set(output) != set(expectedOutput):
            print(f'Wrong answer for {digits}, expected {expectedOutput} but got {output}')
            all_correct = False
        else:
            print("Correct answer for", digits)
    if all_correct:
        print('All test cases passed!')