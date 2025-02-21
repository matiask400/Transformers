def myAtoi(s: str) -> int:
  s = s.lstrip()
  if not s:
    return 0
  sign = -1 if s[0] == '-' else 1
  if s[0] in ('-', '+'):
    s = s[1:]
  i = 0
  num = 0
  while i < len(s) and s[i].isdigit():
    num = num * 10 + ord(s[i]) - ord('0')
    i += 1
  num *= sign
  if num < -2**31:
    return -2**31
  if num > 2**31 - 1:
    return 2**31 - 1
  return num