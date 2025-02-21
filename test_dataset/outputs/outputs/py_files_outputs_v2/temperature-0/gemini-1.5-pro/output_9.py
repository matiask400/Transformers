def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    copy = x
    reverse = 0
    while copy > 0:
        digit = copy % 10
        reverse = reverse * 10 + digit
        copy //= 10
    return x == reverse

print(f"Input: 121, Output: {isPalindrome(121) == True}")
print(f"Input: -121, Output: {isPalindrome(-121) == False}")
print(f"Input: 10, Output: {isPalindrome(10) == False}")