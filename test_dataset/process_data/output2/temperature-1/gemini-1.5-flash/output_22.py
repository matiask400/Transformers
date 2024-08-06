import unittest

def generateParenthesis(n: int) -> list[str]:
    result = []
    def backtrack(s: str, open: int, close: int):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open < n:
            backtrack(s + "(", open + 1, close)
        if close < open:
            backtrack(s + ")", open, close + 1)
    backtrack("", 0, 0)
    return result

class TestGenerateParenthesis(unittest.TestCase):
    def test_case_1(self):
        n = 3
        expected_output = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(generateParenthesis(n), expected_output)
        print(f"Input: {n}, Output: {generateParenthesis(n)}, Expected: {expected_output}, Result: {generateParenthesis(n) == expected_output}")
    def test_case_2(self):
        n = 1
        expected_output = ["()"]
        self.assertEqual(generateParenthesis(n), expected_output)
        print(f"Input: {n}, Output: {generateParenthesis(n)}, Expected: {expected_output}, Result: {generateParenthesis(n) == expected_output}")

if __name__ == '__main__':
    unittest.main()