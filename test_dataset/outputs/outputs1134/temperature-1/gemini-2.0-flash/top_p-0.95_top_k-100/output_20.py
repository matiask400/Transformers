def solve():
    """
    This function provides a template for solving problems with test cases.
    It includes example tests and a framework for verifying the solution.
    You should replace the example problem with your actual problem.
    """

    def is_palindrome(s):
        """
        Checks if a string is a palindrome (reads the same forwards and backward).
        """
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        return s == s[::-1]

    def test_is_palindrome():
        """
        Tests the is_palindrome function with various inputs.
        """
        tests = [
            ("", True),
            ("a", True),
            ("aba", True),
            ("abba", True),
            ("abc", False),
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False)
        ]

        correct_count = 0
        total_tests = len(tests)

        for i, (input_str, expected_output) in enumerate(tests):
            actual_output = is_palindrome(input_str)
            if actual_output == expected_output:
                print(f"Test {i+1}: True")
                correct_count += 1
            else:
                print(f"Test {i+1}: False")

        print(f"\nCorrect: {correct_count}/{total_tests}")

    test_is_palindrome()

if __name__ == "__main__":
    solve()