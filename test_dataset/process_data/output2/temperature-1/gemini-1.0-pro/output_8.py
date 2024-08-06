def myAtoi(s):
  s = s.lstrip()  # Remove leading whitespace

  # Handle sign
  sign = 1
  if s[0] == '-':
    sign = -1
    s = s[1:]
  elif s[0] == '+':
    s = s[1:]

  # Convert string to integer
  num = 0
  for c in s:
    if not c.isdigit():
      break
    num = num * 10 + ord(c) - ord('0')

  # Clamp integer to 32-bit signed integer range
  MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1
  num = max(MIN_INT, min(MAX_INT, num * sign))

  return num

# Test examples
input1 = "42"
output1 = myAtoi(input1)
print(output1 == 42)

input2 = "   -42"
output2 = myAtoi(input2)
print(output2 == -42)

input3 = "4193 with words"
output3 = myAtoi(input3)
print(output3 == 4193)

input4 = "words and 987"
output4 = myAtoi(input4)
print(output4 == 0)

input5 = "-91283472332"
output5 = myAtoi(input5)
print(output5 == -2147483648)