import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
        """
        # Special cases:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0 and x != 0:
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # When the length is an even number
        if x == reversed_num:
            return True
        # When the length is an odd number
        if x == reversed_num // 10:
            return True
        return False


# Example 1: Input: x = 121, Output: true
print(Solution().isPalindrome(121) == True)

# Example 2: Input: x = -121, Output: false
print(Solution().isPalindrome(-121) == False)

# Example 3: Input: x = 10, Output: false
print(Solution().isPalindrome(10) == False)

# Example 4: Input: x = -101, Output: false
print(Solution().isPalindrome(-101) == False)