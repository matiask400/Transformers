def is_palindrome(x: int) -> bool:
  """Given an integer `x`, return `true` if `x` is palindrome integer.

A integer is a palindrome when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

  Args:
      x (int): The integer to check.

  Returns:
      bool: `True` if `x` is a palindrome, `False` otherwise.
  """
  # Special cases:
  if x < 0:
    return False
  if x == 0:
    return True
  if x % 10 == 0:
    return False

  reversed_x = 0
  while x > reversed_x:
    reversed_x = reversed_x * 10 + x % 10
    x //= 10

  return x == reversed_x or x == reversed_x // 10


# Example 1:
input_1 = 121
output_1 = is_palindrome(input_1)
print(output_1)  # Output: True

# Example 2:
input_2 = -121
output_2 = is_palindrome(input_2)
print(output_2)  # Output: False

# Example 3:
input_3 = 10
output_3 = is_palindrome(input_3)
print(output_3)  # Output: False