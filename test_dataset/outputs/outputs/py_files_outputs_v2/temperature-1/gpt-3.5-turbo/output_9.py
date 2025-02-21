def isPalindrome(x):
    if x < 0:
        return False
    temp = x
    reverse_num = 0
    while x > 0:
        digit = x % 10
        reverse_num = reverse_num * 10 + digit
        x = x // 10
    return temp == reverse_num

# Test cases
print(isPalindrome(121) == True)
print(isPalindrome(-121) == False)
print(isPalindrome(10) == False)