def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed = 0
    while x > 0:
        digit = x % 10
        reversed = reversed * 10 + digit
        x //= 10
    return original == reversed

# Example 1
x = 121
print(isPalindrome(x) == True)

# Example 2
x = -121
print(isPalindrome(x) == False)

# Example 3
x = 10
print(isPalindrome(x) == False)

# Example 4
x = -101
print(isPalindrome(x) == False) 