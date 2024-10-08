def isPalindrome(x):
    if x < 0:
        return False
    div = 1
    while x // div >= 10:
        div *= 10
    while x != 0:
        left = x // div
        right = x % 10
        if left != right:
            return False
        x = (x % div) // 10
        div //= 100
    return True

# Test cases
print(isPalindrome(121) == True)
print(isPalindrome(-121) == False)
print(isPalindrome(10) == False)