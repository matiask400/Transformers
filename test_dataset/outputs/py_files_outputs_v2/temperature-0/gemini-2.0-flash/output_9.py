def isPalindrome(x):
    """
    Given an integer `x`, return `true` if `x` is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.
    """
    if x < 0:
        return False

    original_x = x
    reversed_x = 0

    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    return original_x == reversed_x