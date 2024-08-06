import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        if x < 0:
            return False
        if x == 0:
            return True

        # Convert the integer to a string
        str_x = str(x)

        # Check if the string is a palindrome
        return str_x == str_x[::-1]


# Test the solution
test_cases = [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False),
]
for input, expected_output in test_cases:
    solution = Solution()
    output = solution.isPalindrome(input)
    print(output == expected_output)