def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    original_x = x
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    return original_x == reversed_x

# Example 1
x = 121
output = isPalindrome(x)
expected_output = True
print(output == expected_output)

# Example 2
x = -121
output = isPalindrome(x)
expected_output = False
print(output == expected_output)

# Example 3
x = 10
output = isPalindrome(x)
expected_output = False
print(output == expected_output)

# Example 4
x = -101
output = isPalindrome(x)
expected_output = False
print(output == expected_output) 