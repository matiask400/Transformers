def isPalindrome(x):
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
input_1 = 121
output_1 = isPalindrome(input_1)
print(output_1 == True)

# Example 2
input_2 = -121
output_2 = isPalindrome(input_2)
print(output_2 == False)

# Example 3
input_3 = 10
output_3 = isPalindrome(input_3)
print(output_3 == False)