def isPalindrome(x):
    if x < 0:
        return False
    reversed_num = 0
    original_num = x
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
    return original_num == reversed_num

# Test cases
print(isPalindrome(121) == True)
print(isPalindrome(-121) == False)
print(isPalindrome(10) == False)