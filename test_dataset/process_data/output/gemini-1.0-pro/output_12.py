def int_to_roman(num):
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  roman_num = ''
  i = 0
  while num > 0:
    for _ in range(num // values[i]):
      roman_num += roman_values[i]
      num -= values[i]
    i += 1
  return roman_num

# Example 1
num1 = 3
result1 = int_to_roman(num1)
print(f"Input: num = {num1}")
print(f"Output: {result1}")

# Example 2
num2 = 4
result2 = int_to_roman(num2)
print(f"Input: num = {num2}")
print(f"Output: {result2}")

# Example 3
num3 = 9
result3 = int_to_roman(num3)
print(f"Input: num = {num3}")
print(f"Output: {result3}")