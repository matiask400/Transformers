def is_palindrome(x):
    if x < 0:
        return False
    original = x
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    return original == reversed_x

# Test cases
print(is_palindrome(121) == True)  # Output: True
print(is_palindrome(-121) == False)  # Output: True
print(is_palindrome(10) == False)  # Output: True