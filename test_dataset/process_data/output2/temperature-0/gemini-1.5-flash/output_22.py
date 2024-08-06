import unittest

def generateParenthesis(n: int) -> list[str]:
    result = []
    def backtrack(s: str, left: int, right: int):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    backtrack("", 0, 0)
    return result

class TestGenerateParenthesis(unittest.TestCase):
    def test_example_1(self):
        n = 3
        expected_output = ['((()))', '(()())', '(())()', '()(())', '()()()']
        self.assertEqual(generateParenthesis(n), expected_output)
        print(f"Input: {n}, Output: {generateParenthesis(n)}, Expected Output: {expected_output}, Result: {generateParenthesis(n) == expected_output}")
    def test_example_2(self):
        n = 1
        expected_output = ['()']
        self.assertEqual(generateParenthesis(n), expected_output)
        print(f"Input: {n}, Output: {generateParenthesis(n)}, Expected Output: {expected_output}, Result: {generateParenthesis(n) == expected_output}")

if __name__ == '__main__':
    unittest.main()