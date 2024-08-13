def isPalindrome(x):
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
input_1 = 121
output_1 = isPalindrome(input_1)
print(f"Example 1: {output_1 == True}")

# Example 2
input_2 = -121
output_2 = isPalindrome(input_2)
print(f"Example 2: {output_2 == False}")

# Example 3
input_3 = 10
output_3 = isPalindrome(input_3)
print(f"Example 3: {output_3 == False}")