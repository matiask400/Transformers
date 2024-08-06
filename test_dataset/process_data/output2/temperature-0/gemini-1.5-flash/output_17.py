import unittest

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
            temp = []
            for letter in mapping[digit]:
                for combination in result:
                    temp.append(combination + letter)
            result = temp
        return result

class TestLetterCombinations(unittest.TestCase):
    def test_example_1(self):
        digits = "23"
        expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(Solution().letterCombinations(digits), expected_output)
        print(True)
    
    def test_example_2(self):
        digits = ""
        expected_output = []
        self.assertEqual(Solution().letterCombinations(digits), expected_output)
        print(True)
    
    def test_example_3(self):
        digits = "2"
        expected_output = ["a","b","c"]
        self.assertEqual(Solution().letterCombinations(digits), expected_output)
        print(True)

if __name__ == '__main__':
    unittest.main()